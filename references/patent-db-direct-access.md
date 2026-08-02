# triz-ai 专利数据库直接访问指南

## 概述

除了 `triz-ai` CLI 命令外，可以直接访问 SQLite 数据库获取专利数据。这在 CLI 不可用或需要批量导出数据时更可靠。

## 数据库位置

```
~/.triz-ai/patents.db
```

Windows: `C:\Users\<user>\.triz-ai\patents.db`

## 数据库 Schema

| 表名 | 用途 | 关键列 |
|------|------|--------|
| `patents` | 专利主表 | id, title, abstract, claims, domain, filing_date, assignee, source |
| `matrix_observations` | 矛盾矩阵观测 | improving_param, worsening_param, principle_id, patent_id, confidence |
| `search_observations` | 搜索观测 | title, snippet, problem_text, principle_ids |
| `classifications` | IPC分类 | — |
| `candidate_parameters` | 候选参数 | — |
| `candidate_principles` | 候选原理 | — |
| `patent_embeddings` | 专利向量 | — |

## 访问方法

### Python (推荐)

```bash
# 必须先设置正确的 Python 环境
export PYTHONPATH="" && export PATH="/c/Users/jianw/AppData/Local/Programs/Python/Python314:/c/Users/jianw/AppData/Local/Programs/Python/Python314/Scripts:$PATH"

python -c "
import sqlite3
conn = sqlite3.connect('C:/Users/jianw/.triz-ai/patents.db')
cur = conn.cursor()

# 统计
cur.execute('SELECT domain, COUNT(*) FROM patents GROUP BY domain')
for row in cur.fetchall():
    print(f'{row[0]}: {row[1]}')

# 按领域筛选
cur.execute('SELECT id, title, assignee FROM patents WHERE domain LIKE \"%thermal%\"')
for row in cur.fetchall():
    print(f'{row[0]} | {row[1][:70]} | {row[2]}')

conn.close()
"
```

### 常用查询

```sql
-- 按来源统计
SELECT source, COUNT(*) FROM patents GROUP BY source;

-- 按领域统计
SELECT domain, COUNT(*) FROM patents GROUP BY domain ORDER BY COUNT(*) DESC;

-- 搜索特定技术领域
SELECT id, title, assignee, domain FROM patents
WHERE domain LIKE '%thermal%' OR domain LIKE '%PCM%' OR title LIKE '%phase change%';

-- 矛盾矩阵高频原理
SELECT principle_id, COUNT(*) as cnt FROM matrix_observations
GROUP BY principle_id ORDER BY cnt DESC LIMIT 10;

-- 矛盾矩阵高频参数对
SELECT improving_param, worsening_param, COUNT(*) as cnt
FROM matrix_observations
GROUP BY improving_param, worsening_param ORDER BY cnt DESC LIMIT 10;
```

## ⚠️ Pitfalls

### SQLAlchemy 保留字引用问题

数据库由 SQLAlchemy 创建，某些列名是 SQL 保留字（如 `year`, `domain`）。直接 SQL 查询时可能需要引用：

```python
# ❌ 可能报错 — domain 是 SQLAlchemy 保留关键字在某些上下文中
cur.execute('SELECT domain, COUNT(*) FROM patents GROUP BY domain')

# ✅ 安全方式 — 使用方括号或反引号
cur.execute('SELECT [domain], COUNT(*) FROM patents GROUP BY [domain]')
```

实际上 SQLite 对保留字较宽松，大多数情况直接使用即可。如果遇到 `OperationalError`，再尝试加引号。

### 必须使用 Python 3.14

triz-ai 数据库使用 Python 3.14 环境。直接访问时也必须切换到正确的 Python：

```bash
export PYTHONPATH="" && export PATH="/c/Users/jianw/AppData/Local/Programs/Python/Python314:/c/Users/jianw/AppData/Local/Programs/Python/Python314/Scripts:$PATH"
```

### 数据库只读访问

报告生成时只需读取数据，使用 `sqlite3.connect()` 即可。不需要写入权限。

## 与 triz-ai CLI 的对比

| 方面 | CLI (`triz-ai discover`) | 直接 SQLite |
|------|-------------------------|-------------|
| 速度 | 较慢（需调用 LLM） | 即时 |
| 可靠性 | 依赖 API 可用性 | 100% 可靠 |
| 数据范围 | 仅 CNIPA 中国专利 | 所有已导入专利 |
| 筛选能力 | 按领域 | 按任意字段 |
| 批量导出 | 不支持 | 完全支持 |
| 适用场景 | 发现新原理、分析 | 报告数据提取、统计 |
