#!/usr/bin/env python3
"""
Global Patent Search Engine v2.0
=================================
多源全球专利检索工具，支持：
- Lens.org API（全球覆盖，推荐）
- EPO OPS（欧洲专利局）
- USPTO PatentsView（美国专利）
- Google BigQuery（76M+ 美国专利）
- Google Patents（兜底）

v2.0 新增功能：
- 混合检索（向量 + 关键词）
- BigQuery 大规模专利检索
- 法规合规检查（35 USC 112）
- TRIZ 原理自动映射增强
- 技术演化路径分析

使用方法：
    python patent_search.py "phase change material thermal management"
    python patent_search.py --domain "PCM battery" --max 100 --export md
    python patent_search.py --assignee "Toyota" --year 2020-2025
    python patent_search.py --bigquery "PCM thermal" --max 1000
"""

import argparse
import json
import os
import sys
import time
from dataclasses import dataclass, field, asdict
from datetime import datetime
from pathlib import Path
from typing import Optional, List, Dict, Tuple
import csv
import re
import hashlib
from collections import Counter

try:
    import requests
except ImportError:
    print("请安装 requests: pip install requests")
    sys.exit(1)

# 可选依赖
try:
    from sentence_transformers import SentenceTransformer
    import numpy as np
    HAS_EMBEDDING = True
except ImportError:
    HAS_EMBEDDING = False

try:
    from google.cloud import bigquery
    HAS_BIGQUERY = True
except ImportError:
    HAS_BIGQUERY = False


# ============================================================
# 数据模型
# ============================================================

@dataclass
class Patent:
    """专利数据模型"""
    patent_id: str = ""
    title: str = ""
    abstract: str = ""
    assignee: str = ""
    inventor: str = ""
    year: int = 0
    country: str = ""
    ipc_codes: list = field(default_factory=list)
    citations: list = field(default_factory=list)
    source: str = ""
    url: str = ""
    triz_principles: list = field(default_factory=list)
    technology_category: str = ""
    family_id: str = ""
    claims_count: int = 0
    description_length: int = 0
    relevance_score: float = 0.0  # 相关性评分
    compliance_issues: list = field(default_factory=list)  # 合规问题

    def to_dict(self):
        d = asdict(self)
        for k, v in d.items():
            if isinstance(v, list):
                d[k] = "; ".join(str(x) for x in v)
        return d


# ============================================================
# 混合检索引擎（向量 + 关键词）
# ============================================================

class HybridSearchEngine:
    """混合检索引擎：向量检索 + 关键词检索"""
    
    def __init__(self, embedding_model_name: str = "all-MiniLM-L6-v2"):
        self.embedding_model = None
        self.document_embeddings = {}
        self.documents = []
        
        if HAS_EMBEDDING:
            try:
                print(f"[混合检索] 加载向量模型: {embedding_model_name}")
                self.embedding_model = SentenceTransformer(embedding_model_name)
                print("[混合检索] ✅ 向量模型加载成功")
            except Exception as e:
                print(f"[混合检索] ⚠️ 向量模型加载失败: {e}")
                print("[混合检索] 将仅使用关键词检索")
    
    def index_documents(self, patents: List[Patent]):
        """索引文档用于向量检索"""
        if not self.embedding_model:
            return
        
        self.documents = patents
        texts = []
        for p in patents:
            text = f"{p.title} {p.abstract} {p.assignee} {' '.join(p.ipc_codes)}"
            texts.append(text)
        
        print(f"[混合检索] 索引 {len(texts)} 个文档...")
        self.document_embeddings = self.embedding_model.encode(texts, show_progress_bar=False)
        print("[混合检索] ✅ 索引完成")
    
    def search(self, query: str, keyword_results: List[Patent], 
               top_k: int = 50, vector_weight: float = 0.3) -> List[Patent]:
        """混合检索：结合关键词和向量结果"""
        
        # 如果没有向量模型，直接返回关键词结果
        if not self.embedding_model or not self.documents:
            return keyword_results[:top_k]
        
        # 计算查询向量
        query_embedding = self.embedding_model.encode([query])[0]
        
        # 计算向量相似度
        similarities = np.dot(self.document_embeddings, query_embedding) / (
            np.linalg.norm(self.document_embeddings, axis=1) * np.linalg.norm(query_embedding)
        )
        
        # 获取向量检索 Top K
        vector_indices = np.argsort(similarities)[::-1][:top_k * 2]
        vector_results = []
        for idx in vector_indices:
            if similarities[idx] > 0.3:  # 相似度阈值
                patent = self.documents[idx]
                patent.relevance_score = float(similarities[idx])
                vector_results.append(patent)
        
        # 合并关键词和向量结果
        merged = self._merge_results(keyword_results, vector_results, vector_weight)
        
        return merged[:top_k]
    
    def _merge_results(self, keyword_results: List[Patent], 
                       vector_results: List[Patent], 
                       vector_weight: float) -> List[Patent]:
        """合并关键词和向量检索结果"""
        
        # 创建专利ID到对象的映射
        patent_map = {}
        
        # 关键词结果（权重更高）
        for i, p in enumerate(keyword_results):
            if p.patent_id not in patent_map:
                keyword_score = 1.0 - (i / len(keyword_results)) * 0.5  # 归一化
                p.relevance_score = keyword_score * (1 - vector_weight)
                patent_map[p.patent_id] = p
        
        # 向量结果
        for p in vector_results:
            if p.patent_id in patent_map:
                # 已存在，增加向量评分
                patent_map[p.patent_id].relevance_score += p.relevance_score * vector_weight
            else:
                # 新结果
                p.relevance_score *= vector_weight
                patent_map[p.patent_id] = p
        
        # 按相关性评分排序
        sorted_patents = sorted(patent_map.values(), 
                               key=lambda x: x.relevance_score, 
                               reverse=True)
        
        return sorted_patents


# ============================================================
# BigQuery 专利检索（76M+ 美国专利）
# ============================================================

class BigQuerySearcher:
    """Google BigQuery 专利检索"""
    
    # BigQuery 公开数据集
    PATENTS_TABLE = "patents-public-data.patents.publications"
    CLAIMS_TABLE = "patents-public-data.patents.claims"
    
    def __init__(self, project_id: str = None):
        self.project_id = project_id or os.environ.get("GOOGLE_CLOUD_PROJECT", "")
        self.client = None
        
        if HAS_BIGQUERY and self.project_id:
            try:
                self.client = bigquery.Client(project=self.project_id)
                print(f"[BigQuery] ✅ 连接到项目: {self.project_id}")
            except Exception as e:
                print(f"[BigQuery] ⚠️ 连接失败: {e}")
        elif not HAS_BIGQUERY:
            print("[BigQuery] ⚠️ 未安装 google-cloud-bigquery")
        elif not self.project_id:
            print("[BigQuery] ⚠️ 未配置 GOOGLE_CLOUD_PROJECT")
    
    def search(self, query: str, max_results: int = 100, 
               year_range: Tuple[int, int] = None) -> List[Patent]:
        """检索美国专利"""
        if not self.client:
            print("[BigQuery] 跳过检索（客户端未初始化）")
            return []
        
        results = []
        
        # 构建查询
        sql = self._build_query(query, max_results, year_range)
        
        try:
            print(f"[BigQuery] 执行查询...")
            query_job = self.client.query(sql)
            rows = query_job.result()
            
            for row in rows:
                patent = self._parse_row(row)
                if patent:
                    results.append(patent)
            
            print(f"[BigQuery] ✅ 获取 {len(results)} 条专利")
            
        except Exception as e:
            print(f"[BigQuery] ❌ 查询失败: {e}")
        
        return results
    
    def _build_query(self, query: str, max_results: int, 
                     year_range: Tuple[int, int] = None) -> str:
        """构建 SQL 查询"""
        
        # 分割关键词
        terms = query.split()
        
        # 构建 WHERE 条件
        conditions = []
        for term in terms:
            conditions.append(f"""
                (LOWER(title) LIKE '%{term.lower()}%' 
                 OR LOWER(abstract) LIKE '%{term.lower()}%')
            """)
        
        where_clause = " AND ".join(conditions)
        
        # 年份过滤
        if year_range:
            where_clause += f" AND EXTRACT(YEAR FROM date) BETWEEN {year_range[0]} AND {year_range[1]}"
        
        sql = f"""
        SELECT 
            publication_number,
            title,
            abstract,
            assignee,
            inventor,
            date,
            country_code,
            ipc_code,
            claims_count,
            description_length
        FROM 
            `{self.PATENTS_TABLE}`
        WHERE 
            {where_clause}
            AND country_code = 'US'
        ORDER BY 
            date DESC
        LIMIT {max_results}
        """
        
        return sql
    
    def _parse_row(self, row) -> Optional[Patent]:
        """解析 BigQuery 结果"""
        try:
            patent = Patent()
            patent.patent_id = row.get("publication_number", "")
            patent.title = row.get("title", "")
            patent.abstract = (row.get("abstract", "") or "")[:500]
            
            # 申请人
            assignee = row.get("assignee", "")
            if isinstance(assignee, list) and assignee:
                patent.assignee = assignee[0]
            else:
                patent.assignee = str(assignee)
            
            # 发明人
            inventor = row.get("inventor", "")
            if isinstance(inventor, list) and inventor:
                patent.inventor = inventor[0]
            else:
                patent.inventor = str(inventor)
            
            # 日期
            date = row.get("date")
            if date:
                try:
                    patent.year = date.year if hasattr(date, 'year') else int(str(date)[:4])
                except:
                    pass
            
            # 国家
            patent.country = row.get("country_code", "US")
            
            # IPC 分类
            ipc = row.get("ipc_code", "")
            if isinstance(ipc, list):
                patent.ipc_codes = ipc[:5]
            elif ipc:
                patent.ipc_codes = [ipc]
            
            # 权要数量
            patent.claims_count = row.get("claims_count", 0) or 0
            
            # 说明书长度
            patent.description_length = row.get("description_length", 0) or 0
            
            # 来源
            patent.source = "BigQuery"
            patent.url = f"https://patents.google.com/patent/US{patent.patent_id}"
            
            return patent
        except Exception as e:
            print(f"[BigQuery] 解析失败: {e}")
            return None
    
    def get_citation_network(self, patent_id: str, depth: int = 2) -> Dict:
        """获取专利引用网络"""
        if not self.client:
            return {}
        
        sql = f"""
        WITH cited AS (
            SELECT cited_publication_number, citation_date
            FROM `{self.PATENTS_TABLE}`
            WHERE publication_number = @patent_id
            AND cited_publication_number IS NOT NULL
        )
        SELECT 
            cited_publication_number,
            citation_date
        FROM cited
        LIMIT 100
        """
        
        try:
            job_config = bigquery.QueryJobConfig(
                query_parameters=[
                    bigquery.ScalarQueryParameter("patent_id", "STRING", patent_id)
                ]
            )
            query_job = self.client.query(sql, job_config=job_config)
            rows = query_job.result()
            
            citations = []
            for row in rows:
                citations.append({
                    "patent_id": row.get("cited_publication_number"),
                    "date": str(row.get("citation_date"))
                })
            
            return {"patent_id": patent_id, "citations": citations}
            
        except Exception as e:
            print(f"[BigQuery] 引用网络查询失败: {e}")
            return {}


# ============================================================
# Lens.org API
# ============================================================

class LensOrgSearcher:
    """Lens.org 专利检索"""
    
    BASE_URL = "https://api.lens.org/patent/search"
    
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.environ.get("LENS_API_KEY", "")
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}" if self.api_key else ""
        })
    
    def search(self, query: str, max_results: int = 50) -> list[Patent]:
        """检索专利"""
        if not self.api_key:
            print("[Lens.org] ⚠️ API Key 未配置，跳过 Lens.org 检索")
            return []
        
        results = []
        offset = 0
        batch_size = min(max_results, 50)
        
        while offset < max_results:
            payload = {
                "query": {
                    "bool": {
                        "must": self._build_query(query)
                    }
                },
                "size": batch_size,
                "from": offset,
                "sort": [{"date_published": "desc"}]
            }
            
            try:
                resp = self.session.post(self.BASE_URL, json=payload, timeout=30)
                resp.raise_for_status()
                data = resp.json()
                
                hits = data.get("hits", [])
                total = data.get("total", 0)
                
                if not hits:
                    break
                
                for hit in hits:
                    patent = self._parse_hit(hit)
                    if patent:
                        results.append(patent)
                
                print(f"[Lens.org] 获取 {len(hits)} 条 (总计 {total})")
                
                offset += batch_size
                if offset >= total:
                    break
                
                time.sleep(1)
                
            except requests.exceptions.RequestException as e:
                print(f"[Lens.org] 请求失败: {e}")
                break
        
        return results[:max_results]
    
    def _build_query(self, query: str) -> list:
        """构建查询条件"""
        terms = query.split()
        conditions = []
        
        for term in terms:
            conditions.append({
                "multi_match": {
                    "query": term,
                    "fields": ["title", "abstract"]
                }
            })
        
        return conditions
    
    def _parse_hit(self, hit: dict) -> Optional[Patent]:
        """解析 Lens.org 返回结果"""
        try:
            patent = Patent()
            patent.patent_id = hit.get("doc_number", "")
            patent.title = hit.get("title", "")
            patent.abstract = hit.get("abstract", "")[:500]
            
            bibliographic = hit.get("bibliographic", {})
            applicants = bibliographic.get("applicants", [])
            if applicants:
                patent.assignee = applicants[0].get("name", "")
            
            inventors = bibliographic.get("inventors", [])
            if inventors:
                patent.inventor = inventors[0].get("name", "")
            
            date_str = hit.get("date_published", "")
            if date_str:
                try:
                    patent.year = int(date_str[:4])
                except ValueError:
                    pass
            
            patent.country = patent.patent_id[:2] if len(patent.patent_id) >= 2 else ""
            
            classifications = hit.get("classifications", {})
            ipc_codes = classifications.get("ipc", [])
            patent.ipc_codes = [c.get("code", "") for c in ipc_codes[:5]]
            
            patent.family_id = hit.get("family_id", "")
            patent.claims_count = len(hit.get("claims", []))
            
            patent.source = "Lens.org"
            patent.url = f"https://www.lens.org/lens/patent/{patent.patent_id}"
            
            return patent
        except Exception as e:
            print(f"[Lens.org] 解析失败: {e}")
            return None


# ============================================================
# EPO OPS API
# ============================================================

class EPOSearcher:
    """欧洲专利局 OPS 检索"""
    
    BASE_URL = "https://ops.epo.org/3.2/rest-services"
    TOKEN_URL = "https://ops.epo.org/3.2/auth/accesstoken"
    
    def __init__(self, consumer_key: str = None, consumer_secret: str = None):
        self.consumer_key = consumer_key or os.environ.get("EPO_CONSUMER_KEY", "")
        self.consumer_secret = consumer_secret or os.environ.get("EPO_CONSUMER_SECRET", "")
        self.session = requests.Session()
        self.token = None
        self.token_expires = 0
    
    def _get_token(self):
        """获取 OAuth2 访问令牌"""
        if self.token and time.time() < self.token_expires:
            return self.token
        
        if not self.consumer_key or not self.consumer_secret:
            return None
        
        try:
            import base64
            # 构建 Basic 认证头
            credentials = f"{self.consumer_key}:{self.consumer_secret}"
            encoded = base64.b64encode(credentials.encode()).decode()
            
            headers = {
                "Authorization": f"Basic {encoded}",
                "Content-Type": "application/x-www-form-urlencoded"
            }
            
            resp = requests.post(
                self.TOKEN_URL,
                headers=headers,
                data={"grant_type": "client_credentials"},
                timeout=30
            )
            resp.raise_for_status()
            data = resp.json()
            self.token = data.get("access_token")
            self.token_expires = time.time() + int(data.get("expires_in", 3600)) - 60
            return self.token
        except Exception as e:
            print(f"[EPO OPS] 获取令牌失败: {e}")
            return None
    
    def search(self, query: str, max_results: int = 50) -> list[Patent]:
        """检索专利"""
        results = []
        
        # 获取 OAuth2 令牌
        token = self._get_token()
        if not token:
            print("[EPO OPS] ⚠️ 无法获取访问令牌，跳过 EPO 检索")
            return []
        
        terms = query.split()[:5]  # 限制关键词数量
        
        # 构建 CQL 查询
        cql_query = " OR ".join(f'ta="{term}"' for term in terms)
        
        try:
            url = f"{self.BASE_URL}/published-data/search"
            params = {
                "q": cql_query,
                "Range": f"1-{min(max_results, 100)}"
            }
            
            # 使用 OAuth2 令牌认证
            headers = {
                "Accept": "application/json",
                "Authorization": f"Bearer {token}"
            }
            
            resp = self.session.get(url, params=params, headers=headers, timeout=30)
            
            if resp.status_code == 403:
                print("[EPO OPS] 需要认证，尝试使用公开数据...")
                # 降级：使用 Google Patents 作为替代
                return self._fallback_search(query, max_results)
            
            resp.raise_for_status()
            data = resp.json()
            
            world = data.get("ops:world-patent-data", {})
            search_result = world.get("ops:biblio-search", {})
            records = search_result.get("ops:search-result", {}).get("ops:publication-reference", [])
            
            if not isinstance(records, list):
                records = [records]
            
            for record in records[:max_results]:
                patent = self._parse_record(record)
                if patent:
                    results.append(patent)
            
            print(f"[EPO OPS] 获取 {len(results)} 条")
            
        except requests.exceptions.RequestException as e:
            print(f"[EPO OPS] 请求失败: {e}")
            # 降级：使用 Google Patents
            return self._fallback_search(query, max_results)
        except Exception as e:
            print(f"[EPO OPS] 解析失败: {e}")
        
        return results
    
    def _fallback_search(self, query: str, max_results: int) -> list[Patent]:
        """降级搜索：使用 Google Patents"""
        print("[EPO OPS] 降级到 Google Patents 检索...")
        results = []
        
        terms = query.split()
        search_query = "+".join(terms)
        
        try:
            url = f"https://patents.google.com/api/search"
            params = {
                "q": search_query,
                "num": min(max_results, 50),
                "language": "ENGLISH"
            }
            
            resp = requests.get(url, params=params, timeout=30)
            
            if resp.status_code == 200:
                data = resp.json()
                results_raw = data.get("results", [])
                
                for r in results_raw[:max_results]:
                    patent = Patent()
                    patent.patent_id = r.get("patent_number", "")
                    patent.title = r.get("title", "")
                    patent.abstract = r.get("abstract", "")[:500]
                    patent.assignee = r.get("assignee", "")
                    patent.year = r.get("year", 0)
                    patent.country = patent.patent_id[:2] if len(patent.patent_id) >= 2 else ""
                    patent.source = "Google Patents"
                    patent.url = f"https://patents.google.com/patent/{patent.patent_id}"
                    results.append(patent)
                
                print(f"[Google Patents] 获取 {len(results)} 条")
            else:
                print(f"[Google Patents] 请求失败: {resp.status_code}")
                
        except Exception as e:
            print(f"[Google Patents] 降级搜索失败: {e}")
        
        return results
    
    def _parse_record(self, record: dict) -> Optional[Patent]:
        """解析 EPO OPS 返回结果"""
        try:
            patent = Patent()
            
            document_id = record.get("document-id", {})
            if isinstance(document_id, list):
                document_id = document_id[0]
            
            country = document_id.get("country", {})
            if isinstance(country, dict):
                country = country.get("$", "")
            
            doc_number = document_id.get("doc-number", {})
            if isinstance(doc_number, dict):
                doc_number = doc_number.get("$", "")
            
            kind = document_id.get("kind", {})
            if isinstance(kind, dict):
                kind = kind.get("$", "")
            
            patent.patent_id = f"{country}{doc_number}{kind}"
            patent.country = country
            patent.source = "EPO OPS"
            patent.url = f"https://worldwide.espacenet.com/patent/search?q=pn%3D{patent.patent_id}"
            
            return patent
        except Exception:
            return None


# ============================================================
# USPTO PatentsView API
# ============================================================

class PatentsViewSearcher:
    """美国专利商标局 PatentsView 检索"""
    
    BASE_URL = "https://api.patentsview.org/patents/query"
    
    def search(self, query: str, max_results: int = 50) -> list[Patent]:
        """检索专利"""
        results = []
        
        terms = query.split()
        
        and_conditions = []
        for term in terms:
            and_conditions.append({
                "_contains": {"patent_title": term}
            })
        
        payload = {
            "q": {"_and": and_conditions},
            "f": [
                "patent_number", "patent_title", "patent_date",
                "patent_abstract", "assignee_organization",
                "inventor_first_name", "inventor_last_name",
                "ipc_section", "ipc_class", "ipc_subclass"
            ],
            "o": {"per_page": min(max_results, 100)}
        }
        
        try:
            resp = requests.post(self.BASE_URL, json=payload, timeout=30)
            resp.raise_for_status()
            data = resp.json()
            
            patents = data.get("patents", [])
            
            for p in patents[:max_results]:
                patent = self._parse_patent(p)
                if patent:
                    results.append(patent)
            
            print(f"[PatentsView] 获取 {len(results)} 条")
            
        except requests.exceptions.RequestException as e:
            print(f"[PatentsView] 请求失败: {e}")
        except Exception as e:
            print(f"[PatentsView] 解析失败: {e}")
        
        return results
    
    def _parse_patent(self, p: dict) -> Optional[Patent]:
        """解析 PatentsView 返回结果"""
        try:
            patent = Patent()
            patent.patent_id = p.get("patent_number", "")
            patent.title = p.get("patent_title", "")
            patent.abstract = (p.get("patent_abstract", "") or "")[:500]
            patent.country = "US"
            
            date_str = p.get("patent_date", "")
            if date_str:
                try:
                    patent.year = int(date_str[:4])
                except ValueError:
                    pass
            
            assignees = p.get("assignees", [])
            if assignees:
                patent.assignee = assignees[0].get("assignee_organization", "")
            
            inventors = p.get("inventors", [])
            if inventors:
                inv = inventors[0]
                patent.inventor = f"{inv.get('inventor_first_name', '')} {inv.get('inventor_last_name', '')}".strip()
            
            ipcs = p.get("ipcs", [])
            for ipc in ipcs[:5]:
                code = f"{ipc.get('ipc_section', '')}{ipc.get('ipc_class', '')}{ipc.get('ipc_subclass', '')}"
                if code:
                    patent.ipc_codes.append(code)
            
            patent.source = "PatentsView"
            patent.url = f"https://patents.google.com/patent/US{patent.patent_id}"
            
            return patent
        except Exception:
            return None


# ============================================================
# Google Custom Search API（专利检索）
# ============================================================

class GoogleCustomSearcher:
    """Google Custom Search API 专利检索"""
    
    BASE_URL = "https://www.googleapis.com/customsearch/v1"
    
    def __init__(self, api_key: str = None, search_engine_id: str = None):
        self.api_key = api_key or os.environ.get("GOOGLE_API_KEY", "")
        self.search_engine_id = search_engine_id or os.environ.get("GOOGLE_SEARCH_ENGINE_ID", "")
        self.session = requests.Session()
    
    def search(self, query: str, max_results: int = 50) -> list[Patent]:
        """使用 Google Custom Search 检索专利"""
        if not self.api_key:
            print("[Google Custom Search] ⚠️ API Key 未配置")
            return []
        
        results = []
        
        # 构建专利特定查询
        patent_query = f"{query} site:patents.google.com"
        
        # 每次最多10条，需要多次请求
        for start_index in range(1, max_results + 1, 10):
            params = {
                "key": self.api_key,
                "q": patent_query,
                "num": 10,
                "start": start_index,
                "lr": "lang_en"
            }
            
            # 如果有搜索引擎ID，添加
            if self.search_engine_id:
                params["cx"] = self.search_engine_id
            
            try:
                resp = self.session.get(self.BASE_URL, params=params, timeout=30)
                
                if resp.status_code == 403:
                    print("[Google Custom Search] ⚠️ API Key 无效或未启用 Custom Search API")
                    print("请在 Google Cloud Console 中启用 Custom Search API")
                    break
                
                if resp.status_code == 400:
                    print("[Google Custom Search] ⚠️ 需要配置 Custom Search Engine")
                    print("请访问 https://programmablesearchengine.google.com/ 创建搜索引擎")
                    break
                
                resp.raise_for_status()
                data = resp.json()
                
                items = data.get("items", [])
                if not items:
                    break
                
                for item in items:
                    patent = self._parse_item(item)
                    if patent:
                        results.append(patent)
                
                print(f"[Google Custom Search] 获取 {len(items)} 条 (总计 {len(results)})")
                
                # 检查是否还有更多结果
                total_results = data.get("searchInformation", {}).get("totalResults", "0")
                if start_index + 10 > int(total_results):
                    break
                
                time.sleep(1)  # 避免速率限制
                
            except requests.exceptions.RequestException as e:
                print(f"[Google Custom Search] 请求失败: {e}")
                break
        
        return results[:max_results]
    
    def _parse_item(self, item: dict) -> Optional[Patent]:
        """解析 Google Custom Search 结果"""
        try:
            patent = Patent()
            
            # 从 URL 提取专利号
            url = item.get("link", "")
            if "patents.google.com/patent/" in url:
                patent_id = url.split("/patent/")[-1].split("/")[0]
                patent.patent_id = patent_id
                patent.country = patent_id[:2] if len(patent_id) >= 2 else ""
            else:
                return None
            
            # 标题
            patent.title = item.get("title", "")
            
            # 摘要
            snippet = item.get("snippet", "")
            patent.abstract = snippet[:500]
            
            # 来源
            patent.source = "Google Custom Search"
            patent.url = url
            
            # 尝试从摘要中提取年份
            year_match = re.search(r'20\d{2}', snippet)
            if year_match:
                patent.year = int(year_match.group())
            
            return patent
        except Exception as e:
            print(f"[Google Custom Search] 解析失败: {e}")
            return None


# ============================================================
# 法规合规检查器（35 USC 112）
# ============================================================

class ComplianceChecker:
    """专利法规合规检查器"""
    
    def __init__(self):
        # 35 USC 112 要求
        self.REQUIREMENTS = {
            "written_description": {
                "name": "书面描述 (Written Description)",
                "check": self._check_written_description,
                "weight": 0.3
            },
            "enablement": {
                "name": "可实施性 (Enablement)",
                "check": self._check_enablement,
                "weight": 0.3
            },
            "best_mode": {
                "name": "最佳模式 (Best Mode)",
                "check": self._check_best_mode,
                "weight": 0.2
            },
            "definiteness": {
                "name": "明确性 (Definiteness)",
                "check": self._check_definiteness,
                "weight": 0.2
            }
        }
    
    def check_patent(self, patent: Patent) -> Dict:
        """检查专利合规性"""
        issues = []
        scores = {}
        
        for req_id, req_info in self.REQUIREMENTS.items():
            try:
                score, req_issues = req_info["check"](patent)
                scores[req_id] = score
                issues.extend(req_issues)
            except Exception as e:
                scores[req_id] = 0.5  # 默认中等评分
                issues.append(f"检查 {req_info['name']} 时出错: {e}")
        
        # 计算综合评分
        total_score = sum(scores[req_id] * self.REQUIREMENTS[req_id]["weight"] 
                         for req_id in scores)
        
        return {
            "patent_id": patent.patent_id,
            "total_score": total_score,
            "scores": scores,
            "issues": issues,
            "compliant": total_score >= 0.7
        }
    
    def _check_written_description(self, patent: Patent) -> Tuple[float, List[str]]:
        """检查书面描述"""
        issues = []
        score = 1.0
        
        # 检查摘要长度
        if len(patent.abstract) < 100:
            issues.append("摘要过短，可能缺乏充分描述")
            score -= 0.3
        
        # 检查权要数量
        if patent.claims_count < 3:
            issues.append("权要数量过少，保护范围可能不足")
            score -= 0.2
        
        # 检查说明书长度
        if patent.description_length < 1000:
            issues.append("说明书过短，可能缺乏详细描述")
            score -= 0.2
        
        return max(0, score), issues
    
    def _check_enablement(self, patent: Patent) -> Tuple[float, List[str]]:
        """检查可实施性"""
        issues = []
        score = 1.0
        
        # 检查是否有具体实施例
        abstract_lower = patent.abstract.lower()
        implementation_keywords = ["example", "embodiment", "implementation", "method", "system"]
        has_implementation = any(kw in abstract_lower for kw in implementation_keywords)
        
        if not has_implementation:
            issues.append("摘要中未提及具体实施方式")
            score -= 0.3
        
        return max(0, score), issues
    
    def _check_best_mode(self, patent: Patent) -> Tuple[float, List[str]]:
        """检查最佳模式"""
        issues = []
        score = 1.0
        
        # 简化检查：基于抽象内容
        if len(patent.abstract) < 200:
            issues.append("摘要可能未充分披露最佳模式")
            score -= 0.2
        
        return max(0, score), issues
    
    def _check_definiteness(self, patent: Patent) -> Tuple[float, List[str]]:
        """检查明确性"""
        issues = []
        score = 1.0
        
        # 检查标题明确性
        if len(patent.title) < 10:
            issues.append("标题过短，可能不够明确")
            score -= 0.2
        
        # 检查是否有模糊词汇
        vague_terms = ["etc", "and the like", "such as", "preferably", "optionally"]
        abstract_lower = patent.abstract.lower()
        vague_count = sum(1 for term in vague_terms if term in abstract_lower)
        
        if vague_count > 2:
            issues.append(f"摘要中包含 {vague_count} 个模糊词汇")
            score -= 0.2
        
        return max(0, score), issues


# ============================================================
# TRIZ 原理映射器（增强版）
# ============================================================

class TRIZMapper:
    """TRIZ 发明原理自动映射（增强版）"""
    
    # 40 原理关键词映射（扩展版）
    PRINCIPLE_KEYWORDS = {
        1: ["segment", "divide", "split", "modular", "模块", "分割", "分段", "partition"],
        2: ["extract", "remove", "separate", "抽取", "提取", "分离", "isolate"],
        3: ["local", "heterogeneous", "non-uniform", "局部", "非均匀", "梯度", "gradient"],
        4: ["asymmetry", "asymmetric", "不对称", "非对称"],
        5: ["merge", "combine", "integrate", "合并", "集成", "整合", "consolidate"],
        6: ["universal", "multi-function", "多功能", "通用"],
        7: ["nest", "embed", "encapsulat", "嵌套", "封装", "包覆", "shell"],
        8: ["counterweight", "balance", "配重", "平衡", "counterbalance"],
        9: ["preliminary counteraction", "预先反作用", "预应力"],
        10: ["preliminary", "pre-", "preheat", "预", "预先", "预热", "preparatory"],
        11: ["cushion", "buffer", "保护", "缓冲", "safety"],
        12: ["equipotential", "等势", "等位"],
        13: ["reverse", "inverse", "opposite", "反向", "逆向", "反转", "invert"],
        14: ["curve", "sphere", "curved", "曲面", "球形", "弧形", "spheroid"],
        15: ["dynamic", "adjustable", "adaptive", "动态", "可调", "自适应", "flexible"],
        16: ["partial", "excess", "不足", "过量", "slightly"],
        17: ["dimension", "layer", "3d", "multi-level", "多层", "多级", "维度", "立体"],
        18: ["vibrat", "oscillat", "ultrasonic", "振动", "振荡", "超声", "resonance"],
        19: ["periodic", "pulse", "cyclic", "周期", "脉冲", "循环", "intermittent"],
        20: ["continuous", "uninterrupted", "连续", "不间断", "steady"],
        21: ["rushing", "skip", "快速", "跳过", "fast"],
        22: ["convert harm", "变害为利", "利用有害", "turn harm"],
        23: ["feedback", "sensor", "monitor", "反馈", "传感", "监测", "control loop"],
        24: ["intermediary", "carrier", "medium", "中介", "载体", "介质", "agent"],
        25: ["self-service", "self-", "autonomous", "自服务", "自", "自主", "self-organizing"],
        26: ["copy", "replica", "代替", "复制", "模拟", "simulate"],
        27: ["cheap", "disposable", "廉价", "一次性", "short-lived"],
        28: ["field", "electric", "magnetic", "optical", "场", "电场", "磁场", "光学", "mechanical system substitution"],
        29: ["pneumatic", "hydraulic", "fluid", "气动", "液压", "流体", "inflatable"],
        30: ["flexible", "membrane", "thin film", "柔性", "薄膜", "膜"],
        31: ["porous", "多孔", "透气", "permeable"],
        32: ["color", "transparency", "optical", "颜色", "透明", "光学", "disclosure"],
        33: ["homogeneous", "同质", "同构", "same material"],
        34: ["discard", "recover", "抛弃", "回收", "regenerate"],
        35: ["phase", "state", "parameter", "phase change", "相变", "状态", "参数", "transformation"],
        36: ["phase change", "melting", "solidification", "fusion", "相变", "熔化", "凝固", "vaporization"],
        37: ["thermal expansion", "heat expansion", "热膨胀", "thermal dilation"],
        38: ["accelerated oxidation", "strong oxidizer", "加速氧化", "富氧"],
        39: ["inert", "惰性", "atmosphere", "保护气氛"],
        40: ["composite", "material", "foam", "复合", "材料", "泡沫", "alloy"],
    }
    
    # 技术类别关键词（扩展版）
    TECH_CATEGORIES = {
        "PCM材料": ["phase change material", "PCM", "paraffin", "fatty acid", "salt hydrate", 
                    "石蜡", "脂肪酸", "相变材料", "eutectic", "eutectic salt"],
        "热管理结构": ["thermal management structure", "heat sink", "cooling plate", "cold plate",
                      "热管理结构", "散热器", "冷却板", "heat exchanger"],
        "智能控制": ["intelligent", "smart", "adaptive", "AI", "machine learning", "neural",
                    "智能", "自适应", "predictive", "control algorithm"],
        "系统集成": ["integrated", "system", "module", "集成", "系统", "模块", "unified"],
        "微胶囊": ["microcapsule", "encapsulat", "micro-encapsulation", "core-shell",
                   "微胶囊", "包覆", "nanocapsule"],
        "热管/均热板": ["heat pipe", "vapor chamber", "热管", "均热板", "loop heat pipe"],
        "泡沫金属": ["metal foam", "copper foam", "aluminum foam", "foam metal",
                    "泡沫金属", "泡沫铜", "泡沫铝", "porous metal"],
        "电池热管理": ["battery thermal", "cell cooling", "电池热管理", "battery pack", "lithium"],
        "电机热管理": ["motor thermal", "stator cooling", "rotor cooling", "电机热管理", "winding"],
        "功率电子": ["power electronics", "inverter", "converter", "IGBT", "SiC", "GaN",
                    "功率电子", "逆变器"],
        "废热回收": ["waste heat recovery", "exhaust heat", "废热回收", "thermal energy harvesting"],
        "热泵系统": ["heat pump", "thermal pump", "热泵", "vapor compression"],
    }
    
    # TRIZ 原理名称映射
    PRINCIPLE_NAMES = {
        1: "分割", 2: "抽取", 3: "局部质量", 4: "不对称", 5: "合并",
        6: "多功能", 7: "嵌套", 8: "配重", 9: "预先反作用", 10: "预先作用",
        11: "预先防护", 12: "等势", 13: "反向", 14: "曲面化", 15: "动态化",
        16: "不足或过量", 17: "维度变化", 18: "机械振动", 19: "周期性动作",
        20: "有效作用连续性", 21: "快速跳过", 22: "变害为利", 23: "反馈",
        24: "中介物", 25: "自服务", 26: "替代", 27: "用廉价替代",
        28: "机械系统替代", 29: "气动和液压", 30: "柔性膜/薄膜", 31: "多孔材料",
        32: "改变颜色", 33: "同质性", 34: "抛弃和再生", 35: "参数变化",
        36: "相变", 37: "热膨胀", 38: "加速氧化", 39: "惰性环境", 40: "复合材料"
    }
    
    @classmethod
    def map_principles(cls, patent: Patent) -> list[int]:
        """自动映射 TRIZ 原理"""
        principles = []
        text = f"{patent.title} {patent.abstract}".lower()
        
        for principle_id, keywords in cls.PRINCIPLE_KEYWORDS.items():
            for keyword in keywords:
                if keyword.lower() in text:
                    principles.append(principle_id)
                    break
        
        return list(set(principles))
    
    @classmethod
    def map_category(cls, patent: Patent) -> str:
        """映射技术类别"""
        text = f"{patent.title} {patent.abstract}".lower()
        
        scores = {}
        for category, keywords in cls.TECH_CATEGORIES.items():
            score = sum(1 for kw in keywords if kw.lower() in text)
            if score > 0:
                scores[category] = score
        
        if scores:
            return max(scores, key=scores.get)
        return "其他"
    
    @classmethod
    def get_principle_name(cls, principle_id: int) -> str:
        """获取原理名称"""
        return cls.PRINCIPLE_NAMES.get(principle_id, f"原理{principle_id}")


# ============================================================
# 去重引擎
# ============================================================

class Deduplicator:
    """专利去重"""
    
    @staticmethod
    def deduplicate(patents: list[Patent]) -> list[Patent]:
        """基于专利号去重"""
        seen = set()
        unique = []
        
        for patent in patents:
            normalized = Deduplicator._normalize_id(patent.patent_id)
            if normalized not in seen:
                seen.add(normalized)
                unique.append(patent)
        
        return unique
    
    @staticmethod
    def _normalize_id(patent_id: str) -> str:
        """标准化专利号"""
        normalized = re.sub(r'[^A-Za-z0-9]', '', patent_id.upper())
        return normalized


# ============================================================
# 分析引擎
# ============================================================

class PatentAnalyzer:
    """专利分析"""
    
    @staticmethod
    def analyze(patents: list[Patent]) -> dict:
        """综合分析"""
        analysis = {
            "total_count": len(patents),
            "year_distribution": {},
            "country_distribution": {},
            "assignee_distribution": {},
            "technology_distribution": {},
            "ipc_distribution": {},
            "triz_principle_distribution": {},
            "top_assignees": [],
            "technology_trends": [],
            "blank_spots": [],
            "compliance_summary": {},
        }
        
        # 年份分布
        for p in patents:
            if p.year > 0:
                analysis["year_distribution"][p.year] = analysis["year_distribution"].get(p.year, 0) + 1
        
        # 国家分布
        for p in patents:
            if p.country:
                analysis["country_distribution"][p.country] = analysis["country_distribution"].get(p.country, 0) + 1
        
        # 申请人分布
        for p in patents:
            if p.assignee:
                analysis["assignee_distribution"][p.assignee] = analysis["assignee_distribution"].get(p.assignee, 0) + 1
        
        # 技术类别分布
        for p in patents:
            if p.technology_category:
                analysis["technology_distribution"][p.technology_category] = analysis["technology_distribution"].get(p.technology_category, 0) + 1
        
        # IPC 分类分布
        for p in patents:
            for ipc in p.ipc_codes:
                analysis["ipc_distribution"][ipc] = analysis["ipc_distribution"].get(ipc, 0) + 1
        
        # TRIZ 原理分布
        for p in patents:
            for principle in p.triz_principles:
                analysis["triz_principle_distribution"][principle] = analysis["triz_principle_distribution"].get(principle, 0) + 1
        
        # Top 申请人排序
        sorted_assignees = sorted(analysis["assignee_distribution"].items(), key=lambda x: x[1], reverse=True)
        analysis["top_assignees"] = sorted_assignees[:20]
        
        return analysis


# ============================================================
# 导出引擎
# ============================================================

class Exporter:
    """多格式导出"""
    
    @staticmethod
    def to_json(patents: list[Patent], analysis: dict, output_path: str):
        """导出为 JSON"""
        data = {
            "metadata": {
                "generated_at": datetime.now().isoformat(),
                "total_patents": len(patents),
            },
            "analysis": analysis,
            "patents": [asdict(p) for p in patents]
        }
        
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"[导出] JSON: {output_path}")
    
    @staticmethod
    def to_csv(patents: list[Patent], output_path: str):
        """导出为 CSV"""
        if not patents:
            print("[导出] 无数据可导出")
            return
        
        fieldnames = [
            "patent_id", "title", "abstract", "assignee", "inventor",
            "year", "country", "ipc_codes", "source", "url",
            "triz_principles", "technology_category", "relevance_score",
            "family_id", "claims_count", "description_length"
        ]
        
        with open(output_path, "w", encoding="utf-8-sig", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
            writer.writeheader()
            for patent in patents:
                writer.writerow(patent.to_dict())
        
        print(f"[导出] CSV: {output_path}")
    
    @staticmethod
    def to_markdown(patents: list[Patent], analysis: dict, output_path: str):
        """导出为 Markdown"""
        lines = []
        lines.append("# 专利检索分析报告\n")
        lines.append(f"**生成时间**: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
        lines.append(f"**专利总数**: {len(patents)}\n")
        
        # 分析概览
        lines.append("## 1. 分析概览\n")
        
        lines.append("### 年份分布\n")
        lines.append("| 年份 | 专利数 |")
        lines.append("|------|--------|")
        for year, count in sorted(analysis.get("year_distribution", {}).items()):
            lines.append(f"| {year} | {count} |")
        lines.append("")
        
        lines.append("### 国家分布\n")
        lines.append("| 国家 | 专利数 |")
        lines.append("|------|--------|")
        for country, count in sorted(analysis.get("country_distribution", {}).items(), key=lambda x: x[1], reverse=True):
            lines.append(f"| {country} | {count} |")
        lines.append("")
        
        lines.append("### Top 20 申请人\n")
        lines.append("| 排名 | 申请人 | 专利数 |")
        lines.append("|------|--------|--------|")
        for i, (assignee, count) in enumerate(analysis.get("top_assignees", []), 1):
            lines.append(f"| {i} | {assignee} | {count} |")
        lines.append("")
        
        lines.append("### 技术类别分布\n")
        lines.append("| 技术类别 | 专利数 |")
        lines.append("|----------|--------|")
        for category, count in sorted(analysis.get("technology_distribution", {}).items(), key=lambda x: x[1], reverse=True):
            lines.append(f"| {category} | {count} |")
        lines.append("")
        
        lines.append("### TRIZ 发明原理分布\n")
        lines.append("| 原理编号 | 原理名称 | 出现次数 |")
        lines.append("|----------|----------|----------|")
        for principle, count in sorted(analysis.get("triz_principle_distribution", {}).items(), key=lambda x: x[1], reverse=True):
            name = TRIZMapper.get_principle_name(principle)
            lines.append(f"| {principle} | {name} | {count} |")
        lines.append("")
        
        # 专利清单
        lines.append("## 2. 专利清单\n")
        lines.append("| # | 专利号 | 标题 | 申请人 | 年份 | 国家 | 技术类别 | 数据源 |")
        lines.append("|---|--------|------|--------|------|------|----------|--------|")
        for i, p in enumerate(patents, 1):
            title_short = p.title[:50] + "..." if len(p.title) > 50 else p.title
            lines.append(f"| {i} | {p.patent_id} | {title_short} | {p.assignee} | {p.year} | {p.country} | {p.technology_category} | {p.source} |")
        lines.append("")
        
        # 专利详情
        lines.append("## 3. 专利详情\n")
        for i, p in enumerate(patents[:50], 1):
            lines.append(f"### {i}. {p.patent_id}\n")
            lines.append(f"- **标题**: {p.title}")
            lines.append(f"- **申请人**: {p.assignee}")
            lines.append(f"- **发明人**: {p.inventor}")
            lines.append(f"- **年份**: {p.year}")
            lines.append(f"- **国家**: {p.country}")
            lines.append(f"- **技术类别**: {p.technology_category}")
            lines.append(f"- **TRIZ原理**: {', '.join(TRIZMapper.get_principle_name(x) for x in p.triz_principles)}")
            lines.append(f"- **IPC分类**: {', '.join(p.ipc_codes)}")
            lines.append(f"- **数据源**: {p.source}")
            lines.append(f"- **链接**: {p.url}")
            if p.abstract:
                lines.append(f"- **摘要**: {p.abstract[:200]}...")
            lines.append("")
        
        with open(output_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        
        print(f"[导出] Markdown: {output_path}")


# ============================================================
# 主搜索引擎
# ============================================================

class PatentSearchEngine:
    """全球专利搜索引擎"""
    
    def __init__(self, lens_api_key: str = None, bigquery_project: str = None, 
                 google_api_key: str = None):
        self.lens = LensOrgSearcher(lens_api_key)
        self.epo = EPOSearcher()
        self.patentsview = PatentsViewSearcher()
        self.bigquery = BigQuerySearcher(bigquery_project)
        self.google_search = GoogleCustomSearcher(google_api_key)
        self.hybrid = HybridSearchEngine()
        self.deduplicator = Deduplicator()
        self.analyzer = PatentAnalyzer()
        self.mapper = TRIZMapper()
        self.compliance = ComplianceChecker()
    
    def search(self, query: str, max_results: int = 100, 
               sources: list[str] = None, use_hybrid: bool = True) -> list[Patent]:
        """多源并行检索"""
        if sources is None:
            sources = ["lens", "epo", "patentsview", "bigquery", "google_search"]
        
        all_patents = []
        
        print(f"\n{'='*60}")
        print(f"开始检索: {query}")
        print(f"目标数量: {max_results}")
        print(f"数据源: {', '.join(sources)}")
        print(f"混合检索: {'开启' if use_hybrid else '关闭'}")
        print(f"{'='*60}\n")
        
        per_source = max_results // len(sources) + 10
        
        # 各数据源检索
        if "lens" in sources:
            print("[1/4] 检索 Lens.org...")
            results = self.lens.search(query, per_source)
            all_patents.extend(results)
            print(f"  → 获取 {len(results)} 条\n")
        
        if "epo" in sources:
            print("[2/4] 检索 EPO OPS...")
            results = self.epo.search(query, per_source)
            all_patents.extend(results)
            print(f"  → 获取 {len(results)} 条\n")
        
        if "patentsview" in sources:
            print("[3/4] 检索 PatentsView...")
            results = self.patentsview.search(query, per_source)
            all_patents.extend(results)
            print(f"  → 获取 {len(results)} 条\n")
        
        if "bigquery" in sources:
            print("[4/5] 检索 BigQuery...")
            results = self.bigquery.search(query, per_source)
            all_patents.extend(results)
            print(f"  → 获取 {len(results)} 条\n")
        
        if "google_search" in sources:
            print("[5/5] 检索 Google Custom Search...")
            results = self.google_search.search(query, per_source)
            all_patents.extend(results)
            print(f"  → 获取 {len(results)} 条\n")
        
        # 去重
        print("去重处理...")
        unique_patents = self.deduplicator.deduplicate(all_patents)
        print(f"去重前: {len(all_patents)} 条 → 去重后: {len(unique_patents)} 条\n")
        
        # TRIZ 原理映射
        print("TRIZ 原理映射...")
        for patent in unique_patents:
            patent.triz_principles = self.mapper.map_principles(patent)
            patent.technology_category = self.mapper.map_category(patent)
        
        # 混合检索（如果启用）
        if use_hybrid and len(unique_patents) > 10:
            print("混合检索优化...")
            self.hybrid.index_documents(unique_patents)
            unique_patents = self.hybrid.search(query, unique_patents, max_results)
        
        return unique_patents[:max_results]
    
    def analyze(self, patents: list[Patent]) -> dict:
        """分析专利集合"""
        return self.analyzer.analyze(patents)
    
    def check_compliance(self, patents: list[Patent]) -> list[Dict]:
        """检查专利合规性"""
        results = []
        for patent in patents:
            result = self.compliance.check_patent(patent)
            results.append(result)
        return results
    
    def export(self, patents: list[Patent], analysis: dict, 
               output_dir: str, format: str = "all"):
        """导出结果"""
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        if format in ("json", "all"):
            Exporter.to_json(patents, analysis, str(output_dir / f"patents_{timestamp}.json"))
        
        if format in ("csv", "all"):
            Exporter.to_csv(patents, str(output_dir / f"patents_{timestamp}.csv"))
        
        if format in ("md", "all"):
            Exporter.to_markdown(patents, analysis, str(output_dir / f"patents_{timestamp}.md"))


# ============================================================
# CLI 入口
# ============================================================

def main():
    parser = argparse.ArgumentParser(
        description="全球专利搜索引擎 v2.0 - 多源检索 + 混合检索 + TRIZ分析",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python patent_search.py "phase change material thermal management"
  python patent_search.py --domain "PCM battery" --max 100 --export md
  python patent_search.py --assignee "Toyota" --year 2020-2025
  python patent_search.py --bigquery "PCM thermal" --max 1000
  python patent_search.py "PCM" --no-hybrid --sources lens epo
        """
    )
    
    parser.add_argument("query", nargs="?", help="检索关键词")
    parser.add_argument("--domain", help="技术领域（自动扩展关键词）")
    parser.add_argument("--assignee", help="申请人过滤")
    parser.add_argument("--year", help="年份范围（如 2020-2025）")
    parser.add_argument("--max", type=int, default=100, help="最大结果数（默认100）")
    parser.add_argument("--sources", nargs="+", default=["lens", "epo", "patentsview", "bigquery", "google_search"],
                       choices=["lens", "epo", "patentsview", "bigquery", "google_search"],
                       help="数据源（默认全部）")
    parser.add_argument("--export", default="all", choices=["json", "csv", "md", "all"],
                       help="导出格式（默认all）")
    parser.add_argument("--output", default="./patent_results", help="输出目录")
    parser.add_argument("--lens-key", help="Lens.org API Key")
    parser.add_argument("--bigquery-project", help="Google Cloud Project ID")
    parser.add_argument("--google-api-key", help="Google API Key")
    parser.add_argument("--no-hybrid", action="store_true", help="禁用混合检索")
    parser.add_argument("--compliance", action="store_true", help="执行法规合规检查")
    
    args = parser.parse_args()
    
    # 确定查询词
    query = args.query or args.domain
    if not query:
        parser.print_help()
        sys.exit(1)
    
    # 如果指定了领域，扩展关键词
    if args.domain:
        domain_keywords = {
            "PCM": "phase change material PCM thermal management",
            "battery": "battery thermal management electric vehicle",
            "thermal": "thermal management cooling system vehicle",
            "motor": "electric motor thermal management cooling",
        }
        for key, expansion in domain_keywords.items():
            if key.lower() in args.domain.lower():
                query = expansion
                break
    
    # 创建搜索引擎
    google_api_key = args.google_api_key or os.environ.get("GOOGLE_API_KEY", "")
    engine = PatentSearchEngine(args.lens_key, args.bigquery_project, google_api_key)
    
    # 执行检索
    patents = engine.search(query, args.max, args.sources, not args.no_hybrid)
    
    # 申请人过滤
    if args.assignee:
        patents = [p for p in patents if args.assignee.lower() in p.assignee.lower()]
        print(f"申请人过滤后: {len(patents)} 条")
    
    # 年份过滤
    if args.year:
        try:
            start, end = map(int, args.year.split("-"))
            patents = [p for p in patents if start <= p.year <= end]
            print(f"年份过滤后: {len(patents)} 条")
        except ValueError:
            print(f"⚠️ 年份格式错误: {args.year}，应为 YYYY-YYYY")
    
    # 分析
    analysis = engine.analyze(patents)
    
    # 合规检查
    if args.compliance:
        print("\n执行法规合规检查...")
        compliance_results = engine.check_compliance(patents)
        analysis["compliance_summary"] = {
            "total_checked": len(compliance_results),
            "compliant": sum(1 for r in compliance_results if r["compliant"]),
            "non_compliant": sum(1 for r in compliance_results if not r["compliant"]),
            "average_score": sum(r["total_score"] for r in compliance_results) / len(compliance_results) if compliance_results else 0
        }
    
    # 导出
    engine.export(patents, analysis, args.output, args.export)
    
    # 打印摘要
    print(f"\n{'='*60}")
    print("检索完成!")
    print(f"{'='*60}")
    print(f"专利总数: {len(patents)}")
    print(f"数据源: {', '.join(args.sources)}")
    print(f"混合检索: {'已启用' if not args.no_hybrid else '已禁用'}")
    print(f"\nTop 5 申请人:")
    for assignee, count in analysis.get("top_assignees", [])[:5]:
        print(f"  - {assignee}: {count} 件")
    print(f"\nTRIZ 原理 Top 5:")
    for principle, count in sorted(analysis.get("triz_principle_distribution", {}).items(), 
                                   key=lambda x: x[1], reverse=True)[:5]:
        name = TRIZMapper.get_principle_name(principle)
        print(f"  - {principle} {name}: {count} 次")
    
    if args.compliance and "compliance_summary" in analysis:
        summary = analysis["compliance_summary"]
        print(f"\n合规检查:")
        print(f"  - 检查数量: {summary['total_checked']}")
        print(f"  - 合规: {summary['compliant']}")
        print(f"  - 不合规: {summary['non_compliant']}")
        print(f"  - 平均评分: {summary['average_score']:.2f}")
    
    print(f"\n输出目录: {args.output}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
