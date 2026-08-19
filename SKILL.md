---
name: triz-innovation-toolkit
version: 3.7.0
author: fanfanbox
license: MIT
platforms: [linux, macos, windows]
description: "TRIZ systematic innovation toolkit with integrated Triz-AI patent analysis — 24 chapters, 4-dimension analysis (technical contradiction, physical contradiction, Su-Field, evolution trends), ARIZ-85C deep analysis, parallel report generation (100+ pages), triple format output (MD+DOCX+PDF with cover page+TOC+chapter breaks), quality self-assessment (10 dimensions)"
---

# TRIZ Innovation Toolkit — 系统化创新 + 专利分析

综合 TRIZ 方法论 + AI 专利挖掘的一体化创新工具包。

## 更新日志

### v3.7.0 (2026-08-19)
- ✅ 新增方案辩论系统（solution-debate）— 四角色架构（正方/反方/裁判/落地专家）
- ✅ 新增排名稳定性+评分差值混合收敛判定机制（最多3轮辩论）
- ✅ 新增 Top 3 方案 8维度落地分析（市场/竞品/护城河/成本/GTM/路线图/风险/ROI）
- ✅ 新增 Go/No-Go 决策框架（含置信度评估）
- ✅ 集成辩论系统到 TRIZ 工具包（报告生成后自动触发）
- ✅ 端到端测试验证（V4+双转子电机混动热管理课题，9分钟完成辩论）
- ✅ 更新 EPO OPS 凭据配置（~/.patent-search/config.env）
- ✅ 新增专利来源汇总功能（triz-ai + EPO OPS + Google Patents 三源合并）
- ✅ 新增21个参考文档（references/目录）
- ✅ 修复 patent_search.py EPO OPS 认证方式（Basic Auth → OAuth2）

### v3.6.0 (2026-08-02)
- ✅ 新增 EPO OPS 专利检索引擎（OAuth2 认证，覆盖 90+ 国家）
- ✅ 新增 patent_search.py v2.0（多源检索 + TRIZ 映射 + 合规检查）
- ✅ 新增混合检索支持（向量 + 关键词）
- ✅ 新增 BigQuery 集成（76M+ 美国专利）
- ✅ 新增 Google Custom Search 集成
- ✅ 新增 requirements.txt、install.sh、config.env.template
- ✅ 修复 CSV 导出字段缺失问题
- ✅ 修复 EPO OPS expires_in 类型转换问题
- ✅ 更新专利检索 API 状态文档
- ✅ 清理所有私人信息（API Key 等）

### v3.5.1 (2026-07-30)
- 新增智能 PCM 控制技术空白分析
- 新增 80 件专利完整数据整合
- 新增 TRIZ 理论学习手册

### v3.5.0 (2026-07-29)
- 新增专利搜索引擎基础框架
- 新增 triz_md_to_docx.py 脚本
- 新增并行报告生成工作流

## 工具体系架构

```
┌─────────────────────────────────────────────────┐
│        triz-innovation-toolkit (本 Skill)        │
│                                                  │
│  TrizInv 知识层    +    Triz-AI 数据层            │
│  (SKILL.md/chapters)     (Python CLI)            │
│                                                  │
│  "如何思考创新问题"    "专利数据告诉我们什么"        │
└─────────────────────────────────────────────────┘
```

**二者互补不可合并** — 一个是知识文档加载到 LLM 上下文，一个是独立 Python CLI 程序。本 Skill 在关键节点自动调用 Triz-AI CLI。

## Skill 文件结构

| 文件 | 用途 | 何时读取 |
|------|------|----------|
| `SKILL.md` | **入口**：路径选择、工具路由、Triz-AI 集成 | 首先 |
| `chapters/ch01-24*.md` | 24 章详细内容（框架、反模式、案例） | 需要某个工具完整细节时 |
| `cheatsheet.md` | 快速查表：39 参数、矛盾矩阵、路由流程图 | 解题过程中 |
| `patterns.md` | 40 原理详解、8 趋势、76 标准解、ARIZ 步骤 | 应用特定模式时 |
| `glossary.md` | 全部 TRIZ 术语 A-Z 定义 | 遇到陌生术语时 |
| `references/triz-ai-setup.md` | Triz-AI 安装配置详细指南 | 首次配置时 |
| `references/triz-quick-reference.md` | TRIZ 理论快速参考（工具选择、15高频原理、物场模型、IFR公式） | 学习和快速查询时 |
| `references/patent-search-api-status.md` | 专利检索API状态报告（Lens/EPO/BigQuery/Google） | 配置专利检索时 |
| `references/smart-pcm-control-analysis.md` | 智能PCM控制技术空白分析（15件专利+5大空白） | PCM热管理课题时 |
| `references/report-generation-guide.md` | 报告生成指南：三段式并行+Word转换+质量自评 | 生成报告时参考 |
| `references/workflow-lessons.md` | AGENTS.md 迭代经验：常见遗漏点和修复方法 | 开发和维护流程时 |
| `references/workflow-lessons-addendum.md` | v3.4.1补充经验：脚本缺失修复、Windows路径陷阱、docx2pdf依赖 | 遇到环境问题时 |
| `references/triz-theory-quick-reference.md` | TRIZ理论快速参考：工具清单、39参数分类、矛盾矩阵用法、物场模型 | 生成学习材料时 |
| `references/report-generation-pattern.md` | 100页+报告的并行生成模式 | 生成详细报告时 |
| `references/parallel-report-generation.md` | 并行报告生成工作流（3子代理+合并+Word转换） | 生成详细报告时 |
| `references/sequential-report-generation.md` | 单代理顺序报告生成模式（无子代理时） | 单代理生成报告时 |
| `references/patent-db-direct-access.md` | triz-ai SQLite 专利数据库直接访问 | 需要批量导出专利数据时 |
| `scripts/patent_search.py` | **全球专利检索引擎**（多源检索+TRIZ映射+合规检查） | 专利分析时 |
| `scripts/triz_md_to_docx.py` | **专业 Word 报告生成**（封面页+三级目录+章节分页+表格样式） | 报告生成后 |
| `scripts/convert_to_word.sh` | 简单 pandoc 转换（备用） | 快速转换时 |
| `scripts/install.sh` | 专利搜索引擎安装脚本 | 首次安装时 |
| `scripts/requirements.txt` | Python 依赖清单 | 安装依赖时 |
| `scripts/config.env.template` | API Key 配置模板 | 配置 API 时 |

## ⚠️ 强制执行规则（必须严格遵守）

> **本 skill 定义了严格的三阶段分析流程，任何分析任务都必须按照以下步骤执行，不得跳过任何步骤。**
> **详细规则见 [AGENTS.md](AGENTS.md)**

### 报告生成最佳实践（100页+详细报告）

**并行子代理模式**：将报告分为3部分并行生成，最后合并：
1. 第一部分（~40页）：第一阶段 问题分析（课题信息+课题梳理+功能分析+裁剪+因果链+聚焦关键问题）
2. 第二部分（~40页）：第二阶段 方案产出（11题路由+专利挖掘+矛盾分析+物场分析+功能导向搜索+方案矩阵+ARIZ+方案说明书）
3. 第三部分（~25页）：第三阶段 方案落地 + 附录（实施路线图+原理样件设计+结论+质量自评+格式检查）

**单代理顺序模式**（无子代理时）：每个部分顺序写入临时文件，最后 `cat` 合并：
```bash
# 写入临时文件 part_01.md, part_02.md, ...
# 合并
cat part_01.md part_02.md part_03.md > 完整版.md
# 验证
wc -c 完整版.md && wc -l 完整版.md
# 清理
rm -f part_*.md
```
详细流程见 `references/sequential-report-generation.md`。

**输出格式**：每个报告必须生成3种格式：
- `.md` — 版本控制、在线查看
- `.docx` — 正式提交、打印（使用 `scripts/triz_md_to_docx.py`）
- `.pdf` — 分发、归档（使用 docx2pdf）

**Word 文档生成**：使用 `scripts/triz_md_to_docx.py` 脚本（python-docx），**不要用 pandoc**（无法生成正确目录和封面页）。

```bash
# 基本用法
python scripts/triz_md_to_docx.py input.md output.docx --author "作者名"

# 批量转换
for file in TRIZ_*_完整版.md; do
  python scripts/triz_md_to_docx.py "$file" "${file%.md}.docx" --author "作者名"
done

# 转换为 PDF（需要 docx2pdf）
pip install docx2pdf
python -c "from docx2pdf import convert; convert('report.docx', 'report.pdf')"
```

**Word 文档特性**：
- 封面页（标题+副标题+作者+日期）
- 目录页（三级目录，打开 Word 后右键"更新域"生成）
- 一级标题前自动分页
- 表格样式（深蓝表头白字，交替行颜色）
- 页边距：上下2.54cm，左右3.18cm

### 流程总览

```
步骤 0：路径选择网关（必须首先执行）
  ├── 判断：问题边界清晰 + 核心矛盾明确 + 约束已知？
  ├── ✅ 三项都满足 → 放射型 (Radial) — 全自动分析
  └── ❌ 任一项缺失 → 收敛型 (Convergent) — 对话教练

第一阶段：问题分析
  ├── 1.1 课题收集（3轮追问）
  ├── 1.2 课题梳理（背景、缺陷、目标、MPV、S曲线、IFR）
  ├── 1.3 功能分析（组件矩阵、相互作用、功能建模）
  ├── 1.4 裁剪（裁剪方案+次级问题）
  ├── 1.5 因果链分析（逐级分解）
  └── 1.6 聚焦关键问题（评估排序）

【11题问题路由诊断】（第一阶段完成后必须执行）
  └── 按顺序回答，第一个"Yes"指向起始工具

第二阶段：方案产出
  ├── 2.1 Triz-AI 专利挖掘（全局必选）
  ├── 2.2 矛盾矩阵 + 40 原理
  ├── 2.3 物理矛盾分析（分离原理）
  ├── 2.4 物场分析（Su-Field + 76标准解）
  ├── 2.5 功能导向搜索（跨行业借鉴）
  ├── 2.6 综合解决方案矩阵（四维度交叉）
  ├── 2.7 ARIZ-85C 深度分析（可选）
  ├── 2.8 扩展专利全景分析（可选）
  └── 2.9 方案说明书（详细技术方案）

第三阶段：方案落地
  ├── 3.1 实施路线图（短期/中期/长期）
  ├── 3.2 原理样件概念设计（可选）
  └── 3.3 结论
```

### 路径选择网关（必须首先执行）

**规则：每个分析任务必须首先执行路径选择，不得跳过。**

| 条件 | 判断依据 | 推荐路径 |
|------|----------|----------|
| ✅ 三项都满足 | 问题边界清晰 + 核心矛盾明确 + 约束已知 | **放射型 (Radial)** |
| ❌ 任一项缺失 | 问题模糊、矛盾不明确、约束未知 | **收敛型 (Convergent)** |

**放射型**：全自动分析，一次输入输出完整报告，中间过程零打断。
**收敛型**：多轮对话教练，4阶段收敛（问题初探→TRIZ深挖→边界收敛→路线图），用户确认后转入放射型。

### 强制流程检查清单

#### 第一阶段检查清单

- [ ] 1.1 课题收集（3轮追问）完成
- [ ] 1.2 课题梳理完成（背景、缺陷、目标、MPV、S曲线、IFR、组件、流程）
- [ ] 1.3 功能分析完成（组件矩阵、相互作用、功能建模）
- [ ] 1.4 裁剪完成（裁剪对象、方案、次级问题）
- [ ] 1.5 因果链分析完成（至少3级分解）
- [ ] 1.6 聚焦关键问题完成（评估排序）

#### 第一阶段与第二阶段之间检查清单

- [ ] 11题问题路由诊断已完成
- [ ] 问题是否明确？ [是/否]
- [ ] 矛盾类型已确定：[技术矛盾/物理矛盾]
- [ ] 指向工具已确定：[工具名称] (ChXX)
- [ ] 8趋势分析已完成（如果路由指向趋势）

#### 第二阶段检查清单

- [ ] 2.1 Triz-AI 专利挖掘完成（discover + matrix stats + analyze）
- [ ] 2.2 矛盾矩阵 + 40 原理完成
- [ ] 2.3 物理矛盾分析完成（分离原理）
- [ ] 2.4 物场分析完成（Su-Field + 76标准解）
- [ ] 2.5 功能导向搜索完成（跨行业借鉴）
- [ ] 2.6 综合解决方案矩阵完成（四维度交叉）
- [ ] 2.7 ARIZ-85C 深度分析完成（可选）
- [ ] 2.8 扩展专利全景分析完成（可选）
- [ ] 2.9 方案说明书完成（详细技术方案+实施示例）

#### 第三阶段检查清单

- [ ] 3.1 实施路线图完成（短期/中期/长期）
- [ ] 3.2 原理样件概念设计完成（可选）

### 违反规则的处理

如果发现跳过了某个步骤：
1. 立即停止当前分析
2. 回溯到缺失步骤
3. 重新执行后续步骤
4. 向用户说明回溯原因

---

## When to Use This Skill

当用户面对以下场景时触发：

- **技术矛盾**："想提升X但Y变差了"
- **物理矛盾**："一个部件既要A又要B"
- **产品创新/下一代设计**："下一代产品应该是什么样？"
- **降本简化**："如何在不损失功能的情况下降成本？"
- **难题攻关**："所有方法都试过了都不行"
- **专利策略**："如何保护我们的发明路线图？"
- **系统优化**："应该在哪里集中改进？"
- **创意枯竭**："想不出新方案了"
- **失效预测**："这个设计可能出什么问题？" → AFI
- **商业创新**："如何创新商业模式？" → 商业 TRIZ
- **R&D 流程设计**："如何构建创新管线？"
- **专利分析**："这个领域有哪些专利空白？" → Triz-AI discover

---

## 路径选择网关（统一入口）

每个 TRIZ 分析都从这里开始。判断：**问题边界清晰 + 核心矛盾明确 + 约束已知？**

| 条件 | 推荐路径 | 说明 |
|------|----------|------|
| ✅ 三项都满足 | **放射型 (Radial)** | 全自动分析，一次输入输出完整报告 |
| ❌ 任一项缺失 | **收敛型 (Convergent)** | 多轮对话教练，共同定义问题后转入放射型 |

### 放射型 — TRIZ 分析师

**人格**：静默执行的全自动分析引擎。中间过程零打断，缺失信息用假设填补并标注，只汇报 4 类里程碑通知。

**执行流程**：
```
用户输入 → 问题解析 & 工具路由 → Triz-AI 专利挖掘 → 工具执行 → 融合专利 → 报告
```

### 收敛型 — TRIZ 教练

**人格**：Socratic 式对话者。每次只问一个问题，自然引入 TRIZ 术语，4 阶段收敛：

1. **问题初探**：谁、什么事、为什么 → 能一句话说清场景
2. **TRIZ 深挖**：矛盾识别、IFR 定义 → 矛盾+IFR 都明确
3. **边界收敛**：锁定问题边界 → 用户确认"这就是我要解决的问题"
4. **输出路线图**：问题定义书 + 执行路线图 → 转入放射型执行

用户随时可以说"直接分析"跳转到放射型。

---

## 11 题问题路由诊断

按顺序回答，第一个"Yes"指向起始工具：

| # | 问题 | 指向工具 |
|---|------|----------|
| 1 | 问题是否明确定义？ | ❌ → 功能分析 (Ch12) / ✅ → #2 / 只需定义理想结果 → IFR (Ch09) |
| 2 | 什么类型的矛盾？ | 技术矛盾 → 矛盾矩阵+40 原理 (Ch03) / 物理矛盾 → 分离原理 |
| 3 | 需要预测未来技术？ | → 8 趋势 (Ch04) |
| 4 | 需要降本简化？ | → 裁剪 (Ch14) |
| 5 | 创意枯竭？ | → SLP/DTC/九屏幕 (Ch07-08) |
| 6 | 物质-场交互问题？ | → 76 标准解 (Ch13) |
| 7 | 找实现功能的方法？ | → 效应数据库 (Ch06) |
| 8 | 超级难题，其他方法失效？ | → ARIZ (Ch17) |
| 9 | 需要预测/预防失效？ | → AFI (Ch18) |
| 10 | 商业/管理问题？ | → 商业 TRIZ (Ch19-21) |
| 11 | 准备实施解决方案？ | → 实施方法论 (Ch22) |

---

## Triz-AI CLI 集成（专利数据驱动）

### 运行环境

```bash
# triz-ai 需要 Python >=3.12，当前系统需要清除 PYTHONPATH 避免 Hermes venv 冲突
export PYTHONPATH="" && export PATH="/c/Users/jianw/AppData/Local/Programs/Python/Python314:/c/Users/jianw/AppData/Local/Programs/Python/Python314/Scripts:$PATH"
```

### 当前配置（~/.triz-ai/config.yaml）

```yaml
llm:
  default_model: mimo-v2.5-pro        # MiMo API 主分析
  classify_model: mimo-v2.5            # MiMo API 分类（快速）
  deep_model: mimo-v2.5-pro            # ARIZ 深度分析
  api_base: https://api.xiaomimimo.com/v1
  api_key: ${XIAOMI_API_KEY}
embeddings:
  model: nomic-embed-text              # Ollama 本地
  dimensions: 768
  api_base: http://localhost:11434/v1
  api_key: ollama
```

### 核心命令

| 命令 | 功能 | 输出 |
|------|------|------|
| `triz-ai analyze "问题"` | 自动分类 → 路由到最佳 TRIZ 方法 | 矛盾分析 + 推荐原理 + 方案方向 |
| `triz-ai analyze "问题" --deep` | ARIZ-85C 深度 3 轮分析 | 重制定→多工具并行→IFR 验证 |
| `triz-ai discover --domain "领域"` | 发现该领域低频 TRIZ 原理 | 机会空白列表 |
| `triz-ai matrix stats` | 矛盾矩阵统计 | 填充率、高频参数对 |
| `triz-ai ingest <files>` | 导入专利数据 | 存入 SQLite |
| `triz-ai evolve --review` | 从专利发现候选新原理 | 交互式审核 |
| `triz-ai consolidate` | 合并搜索观察到矩阵 | 矩阵数据更新 |

### 6 种分析方法

| 方法 | 场景 | 示例 |
|------|------|------|
| `technical-contradiction` | 改善 X 但恶化 Y | 提升功率密度但温度升高 |
| `physical-contradiction` | 既要 A 又要 B | 焊点既要刚性又要柔性 |
| `su-field` | 检测/测量问题 | 不加传感器检测分层 |
| `function-analysis` | 组件造成损害 | 粘接层在热循环中损伤芯片 |
| `trimming` | 简化/降本 | 降低驱动电路 BOM 成本 |
| `trends` | 技术走向预测 | SiC 封装下一代技术？ |

### 自动调用规则（全局必选）

**专利挖掘是全局必选项**，无论走哪条路径都必须经过 Triz-AI 检索节点。

| 触发点 | 自动执行命令 | 条件 |
|--------|-------------|------|
| ★ 全局必选 | `triz-ai discover --domain "<领域>"` | 领域不能太模糊 |
| A 用户陈述技术领域 | `triz-ai discover --domain "<domain>"` | 同上 |
| B 发现技术矛盾 | `triz-ai matrix stats` | 本次会话未显示过 |
| C 询问现有技术/竞争 | `triz-ai discover --domain "<domain>"` | 始终执行 |
| D 需要方案生成 | `triz-ai analyze` | 用户未拒绝 LLM 辅助 |
| E 分析结束 | 提及 `triz-ai evolve` 作为后续选项 | 用户有专利数据 |

### 降级方案（Triz-AI 不可用时）

| 功能 | 降级方案 |
|------|----------|
| `discover` | 用 `patterns.md` 原理频率数据 + AI 知识 |
| `matrix stats` | 用 `cheatsheet.md` 静态 39×39 矩阵 |
| `analyze` | 纯 TrizInv 方法论（物场/趋势/效应库/ARIZ） |

始终告知用户：triz-ai CLI not available — using cached TRIZ data. Install with `pip install triz-ai` for live patent mining.

### 直接访问 triz-ai SQLite 专利数据库（高级）

当 CLI 不可用或需要批量导出专利数据时，可以直接访问 SQLite 数据库：

```bash
# 数据库位置
~/.triz-ai/patents.db

# 快速统计
python -c "
import sqlite3
conn = sqlite3.connect('C:/Users/jianw/.triz-ai/patents.db')
cur = conn.cursor()
cur.execute('SELECT domain, COUNT(*) FROM patents GROUP BY domain')
for row in cur.fetchall(): print(f'{row[0]}: {row[1]}')
conn.close()
"
```

**数据库主要表**：`patents`（id, title, abstract, domain, assignee）, `matrix_observations`（矛盾矩阵数据）

详细查询和使用方法见 `references/patent-db-direct-access.md`。

### 全球专利检索引擎（patent_search.py v2.0）

**新增工具**：`scripts/patent_search.py` — 多源全球专利检索工具

**v2.0 新增功能**：

| 功能 | 说明 |
|------|------|
| **混合检索** | 向量 + 关键词混合检索，提升相关性 |
| **BigQuery** | 76M+ 美国专利大规模检索 |
| **法规合规检查** | 35 USC 112 合规性自动检查 |
| **TRIZ 原理映射增强** | 40 原理 + 12 技术类别自动识别 |
| **相关性评分** | 基于向量相似度的相关性排序 |

**支持数据源**：

| 数据源 | 覆盖范围 | API Key | 推荐度 |
|--------|----------|---------|--------|
| **Lens.org** | 全球 1.5亿+ 专利 | 需注册（免费1000次/月） | ⭐⭐⭐⭐⭐ |
| **EPO OPS** | 欧洲+全球 90+ 国家 | 需注册（免费非商业） | ⭐⭐⭐⭐⭐ |
| **USPTO PatentsView** | 美国专利 | 无需注册 | ⭐⭐⭐⭐ |
| **Google BigQuery** | 76M+ 美国专利 | 需 Google Cloud | ⭐⭐⭐⭐ |
| **Google Patents** | 全球 | 无需注册（不稳定） | ⭐⭐⭐ |
| **Google Custom Search** | 全球（专利网页） | 需API Key+搜索引擎 | ⭐⭐⭐ |

**基本用法**：

```bash
# 基本检索（默认使用全部数据源）
python scripts/patent_search.py "phase change material thermal management"

# 指定技术领域
python scripts/patent_search.py --domain "PCM battery thermal management"

# 按申请人筛选
python scripts/patent_search.py --assignee "Toyota" --year 2020-2025

# 指定数据源和输出格式
python scripts/patent_search.py "PCM" --sources lens epo --export md --max 100

# 使用 Lens.org API Key
python scripts/patent_search.py "PCM" --lens-key YOUR_API_KEY

# 使用 BigQuery（大规模检索）
python scripts/patent_search.py "PCM" --bigquery-project YOUR_PROJECT_ID --max 1000

# 禁用混合检索
python scripts/patent_search.py "PCM" --no-hybrid

# 执行法规合规检查
python scripts/patent_search.py "PCM" --compliance
```

**输出格式**：
- **JSON**：完整数据，适合程序处理
- **CSV**：表格数据，适合 Excel 分析
- **Markdown**：报告格式，适合直接引用

**核心功能**：
1. **多源并行检索**：同时从 Lens.org、EPO、PatentsView、BigQuery 检索
2. **混合检索**：向量 + 关键词混合检索，提升相关性
3. **自动去重合并**：基于专利号标准化去重
4. **TRIZ 原理自动映射**：根据标题/摘要自动识别 40 原理
5. **技术类别分类**：自动分类到 12 个技术类别
6. **竞争态势分析**：自动统计 Top 申请人、年份分布、国家分布
7. **法规合规检查**：35 USC 112 合规性自动检查

**环境变量配置**：

```bash
# Windows
set LENS_API_KEY=your_api_key_here
set GOOGLE_CLOUD_PROJECT=your_project_id

# Linux/Mac
export LENS_API_KEY=your_api_key_here
export GOOGLE_CLOUD_PROJECT=your_project_id

# 或保存到配置文件
echo "LENS_API_KEY=your_api_key" > ~/.patent-search/config.env
```

**依赖安装**：

```bash
# 基础依赖
pip install requests

# 混合检索（可选）
pip install sentence-transformers numpy

# BigQuery（可选）
pip install google-cloud-bigquery
```

**专利分析工作流（v2.0 更新）**：

1. **triz-ai discover** → 获取中国专利（CNIPA）
2. **patent_search.py** → 获取国际专利（Lens.org + EPO + PatentsView + BigQuery）
3. **合并去重** → 统一专利集合
4. **TRIZ 原理映射** → 自动识别发明原理
5. **竞争格局分析** → 全球 Top 申请人排名
6. **技术空白识别** → 低频原理 + 未覆盖领域
7. **法规合规检查** → 确保专利质量（可选）

**降级方案**：
- 如果 Lens.org API Key 未配置 → 自动跳过，使用 EPO + PatentsView
- 如果 BigQuery 未配置 → 自动跳过，使用其他数据源
- 如果向量模型未安装 → 禁用混合检索，仅使用关键词检索
- 如果所有 API 都不可用 → 使用 Google Patents（可能被限流）
- 如果完全无法访问外部 API → 使用 triz-ai 本地数据库 + AI 知识

**与 patent-search-engine skill 的关系**：
- `patent_search.py` 是实际的检索工具
- `patent-search-engine` skill 提供详细的使用文档和 API 参考
- 两者配合使用，实现完整的专利检索能力

---

## 24 章知识体系

### 四维度 TRIZ 分析框架（v3.0 新增）

对于复杂技术问题，必须从四个维度进行分析：

| 维度 | 方法 | 核心工具 | 章节 |
|------|------|----------|------|
| **技术矛盾** | 矛盾矩阵 + 40 原理 | 识别改善/恶化参数，查询推荐原理 | Ch03 |
| **物理矛盾** | 分离原理 | 条件/空间/时间/系统分离 | Ch03 |
| **物场分析** | Su-Field + 76 标准解 | 建立物场模型，应用标准解 | Ch13 |
| **技术进化** | S曲线 + 8 趋势 | 定位当前阶段，预测进化方向 | Ch04 |

**综合解决方案矩阵**：将四个维度的分析结果交叉映射，形成优先级排序。

---

### Part I-II: 基础 + 核心矛盾工具 (Ch01-05)
- Ch01-02: TRIZ 概述、五大思维支柱
- **Ch03: 40 发明原理 + 矛盾矩阵** — 解决技术矛盾的核心工具
- **Ch04: 8 技术进化趋势** — 预测下一代产品形态
- Ch05: 理想化方程 — Ideality = ΣBenefits / (ΣCosts + ΣHarms)

### Part III: 知识与思维工具 (Ch06-08)
- Ch06: 效应数据库 — 按功能查找物理/化学/几何效应
- Ch07: 心理惯性突破 — SLP、DTC Operator、Size-Time-Cost
- Ch08: 九屏幕法 — 时间×尺度多维思考

### Part IV: 高级问题求解 (Ch09-13)
- **Ch09: IFR (最终理想结果)** — 定义"完美解决方案"
- Ch10: 团队创造力 — 团队 TRIZ 引导流程
- Ch11: 问题求解流程 — 5 步核心流程
- **Ch12: 功能分析** — 梳理组件功能关系
- **Ch13: 物场分析 + 76 标准解** — 物质-场相互作用的标准解法

### Part V: 系统优化 (Ch14)
- **Ch14: 裁剪** — 删除组件但保留功能

### Part VI: 算法方法 (Ch17-18)
- **Ch17: ARIZ 5 步算法** — 超级难题的系统化求解
- **Ch18: AFI 预期失效识别** — 反转任务→夸大缺陷→生成缺陷→反转修复

### Part VII-VIII: 商业创新 + 落地实施 (Ch19-24)
- Ch19: 12 商业 TRIZ 双重原理 — 商业模式创新
- Ch20: 10 步创新流程 — 战略(5步) + 执行(5步)
- Ch21: 客户收益分析 — I-S 矩阵
- Ch22: 实施方法论 — 5 阶段管线：原型→专利→商业化
- Ch23: CAI 计算机辅助创新
- Ch24: 企业 TRIZ 培训 — MATRIZ 5 级认证模型

---

## Quick Tool Selector

| 我想... | 用这个工具 | 章节 |
|---------|-----------|------|
| 解决已知的权衡取舍 | 矛盾矩阵 + 40 原理 | Ch03 |
| 预测产品未来 | 8 趋势 | Ch04 |
| 降本增效 | 裁剪 + 理想化 | Ch05, Ch14 |
| 找物理效应 | 效应数据库 | Ch06 |
| 打破思维定式 | SLP/DTC/九屏幕 | Ch07-08 |
| 定义完美方案 | IFR | Ch09 |
| 梳理系统问题 | 功能分析 | Ch12 |
| 物场交互问题 | 76 标准解 | Ch13 |
| 超级难题 | ARIZ | Ch17 |
| 预测失效 | AFI | Ch18 |
| 商业模式创新 | 12 商业原理 | Ch19 |
| R&D 管线设计 | 10 步流程 | Ch20 |
| 专利空白分析 | **triz-ai discover** | CLI |
| AI 辅助方案生成 | **triz-ai analyze** | CLI |

---

## Pitfalls

### ⚠️ triz-ai 模型名称不能带 `openai/` 前缀

triz-ai 未安装 litellm 时使用原生 OpenAI SDK，会把模型名原样发送到 API。

```yaml
# ❌ 错误 — MiMo API 返回 "Unsupported model openai/mimo-v2.5-pro"
default_model: openai/mimo-v2.5-pro

# ✅ 正确 — 直接用模型 ID
default_model: mimo-v2.5-pro
```

### ⚠️ Embedding 必须单独配置 api_base

不在 `embeddings:` 下指定 `api_base` 会用 LLM 的 api_base（MiMo）请求 embedding，导致失败。Ollama 端点：`http://localhost:11434/v1`。

### ⚠️ Python 版本与 Hermes venv 冲突

运行 triz-ai 前必须：
```bash
export PYTHONPATH="" && export PATH="/c/Users/jianw/AppData/Local/Programs/Python/Python314:/c/Users/jianw/AppData/Local/Programs/Python/Python314/Scripts:$PATH"
```

### ⚠️ MiMo API 可用模型

`mimo-v2.5`, `mimo-v2.5-pro`, `mimo-v2.5-asr`, `mimo-v2.5-tts`。不存在 `mimo-v2-pro` 或 `mimo-v2-flash`。

### ⚠️ 报告必须保存为文件

分析完成后，报告必须同时输出到聊天 **AND** 保存为 Markdown 文件。

```bash
# 文件路径格式
~/Documents/TRIZ_创新分析报告_<课题简称>.md
```

使用 `write_file` 工具将完整报告保存到文件，确保用户有持久化副本。不要只在聊天中输出报告而不保存。

### ⚠️ 大文件写入必须分块（防 stream timeout）

单次 `write_file` 超过 ~20KB 会导致 stream timeout（tool call 被截断，文件未写入）。**必须分块写入**：

**分块策略**：
1. **第一块** (`write_file`)：封面+目录+1.1+1.2前半，控制在 ~20KB
2. **后续块** (`patch` mode='patch')：用 `@@ context @@` 锚点追加，每块 ~15-25KB
3. **锚点技巧**：context hint 用上一块最后一行的唯一文本，确保定位准确
4. **验证**：每次写入后用 `terminal` 执行 `wc -l -c file.md` 确认文件增长正常

**第一部分（~40页）推荐分块**：
| 块 | 工具 | 内容 | 预估大小 |
|----|------|------|---------|
| 1 | `write_file` | 封面+目录+1.1课题收集+1.2前半 | ~20KB |
| 2 | `patch` | 1.2后半（MPV+S曲线+IFR+组件+流程+约束） | ~18KB |
| 3 | `patch` | 1.3功能分析（矩阵+功能建模+物场模型） | ~15KB |
| 4 | `patch` | 1.4裁剪+1.5因果链+1.6聚焦+检查清单 | ~20KB |

**错误模式**：直接 `write_file` 写入 40 页完整报告 → stream timeout → 文件为空或不完整。

### ⚠️ 必须严格遵循 AGENTS.md 流程（关键）

用户明确要求：**分析过程必须严格按照 AGENTS.md 定义的流程执行，不得跳过任何步骤。**

常见错误：
1. **跳过路径选择网关** — 必须首先判断放射型/收敛型
2. **跳过11题问题路由** — 第一阶段完成后必须执行
3. **报告过于简略** — 参考 AITRIZ 91页报告标准，每个节点必须有详细输出
4. **只在聊天输出不保存** — 报告必须保存为文件
5. **缺少物理矛盾分析** — 分离原理是四维度TRIZ分析的核心维度之一
6. **缺少物场分析** — Su-Field模型+76标准解是四维度TRIZ分析的核心维度之一
7. **缺少综合解决方案矩阵** — 必须将四个TRIZ维度交叉映射

### ⚠️ Word 生成必须用 python-docx 脚本（关键）

**不要用 pandoc 生成 Word**，pandoc 无法生成正确的三级目录和封面页。

必须使用 `scripts/triz_md_to_docx.py`：
```bash
python scripts/triz_md_to_docx.py input.md output.docx --author "作者名"
```

转换为 PDF：
```bash
pip install docx2pdf
python -c "from docx2pdf import convert; convert('report.docx', 'report.pdf')"
```

详细工作流见 `references/parallel-report-generation.md`。

### ⚠️ Windows/MSYS 路径陷阱（关键）

在 Windows + Git Bash (MSYS) 环境下运行 Python 脚本时，路径格式必须注意：

```bash
# ❌ 错误 — 反斜杠路径被 MSYS 双重转义，导致文件找不到
python "C:\Users\jianw\...\script.py" "C:\Users\jianw\...\input.md"

# ❌ 错误 — MSYS 风格路径在 Python 命令中也会被错误转换
python "/c/Users/jianw/...\script.py"

# ✅ 正确 — 使用正斜杠的 Windows 路径
python "C:/Users/jianw/.../script.py" "C:/Users/jianw/.../input.md" --author "作者名"
```

**根本原因**：MSYS 的路径自动转换 (`MSYS_NO_PATHCONV`) 会把 `/c/...` 转成 `C:\...`，但当路径已经在引号内时，反斜杠可能被二次转义为 `\\`。

### ⚠️ docx2pdf 在 Windows 上需要 Microsoft Word

`docx2pdf` 在 Windows 上依赖 Microsoft Word 进行转换。如果未安装 Word，会报错。替代方案：
```bash
# 使用 LibreOffice
soffice --headless --convert-to pdf report.docx
```

如果发现跳过了某个步骤：
1. 立即停止当前分析
2. 回溯到缺失步骤
3. 重新执行后续步骤
4. 向用户说明回溯原因

### ⚠️ 报告颗粒度必须达标（关键）

**用户明确要求：报告必须达到100页以上的细致程度，每个步骤都必须详细展开，不得泛化。**

**参考标准**：AITRIZ 91页报告（`references/report-granularity-standard.md`）

**禁止事项**：
- ❌ 禁止使用简单列表替代详细表格
- ❌ 禁止省略分析过程只给结论
- ❌ 禁止使用泛化描述替代具体数据
- ❌ 禁止跳过次级问题分析
- ❌ 禁止省略实施示例

**四维度TRIZ分析必须完整**：
1. 技术矛盾分析（矛盾矩阵 + 40 原理）
2. 物理矛盾分析（分离原理）
3. 物场分析（Su-Field + 76 标准解）
4. 技术进化趋势分析（S曲线 + 8 趋势）

**专利分析必须深入**：
- 至少20件专利
- 4+个子方向详解
- 专利权人竞争格局
- 技术空白与机会

### ⚠️ triz-ai 只检索中国专利（CNIPA）— 必须补充国际专利

triz-ai 的 `discover` 命令**只接入 CNIPA（中国国家知识产权局）数据库**，结果 100% 为中国专利。对于需要全球视野的课题，必须手动补充国际专利检索。

**补充检索方法**：

| 数据源 | 方法 | 注意事项 |
|--------|------|----------|
| Google Patents | `browser_navigate` 到 `patents.google.com` 搜索 | API 有速率限制（~3次查询后返回503），需用多个子代理并行检索 |
| Espacenet | `patents.epo.org` 搜索 | 可能有 Cloudflare 防护 |
| WIPO PATENTSCOPE | `patentscope.wipo.int` 搜索 | 需注册 |

**推荐检索策略**：
1. 中文关键词 + 英文关键词 + IPC分类号 三管齐下
2. 按主要申请人（Toyota, Samsung SDI, Bosch 等）定向检索
3. 至少覆盖 US/EP/JP/KR 四个地区的专利

**IPC 分类号速查（PCM 热管理相关）**：
- H01M：电池热管理
- B60L：电动车动力系统
- B60H：车辆 HVAC
- F28D：PCM 换热器
- Y02E/Y02T：储能/交通（环保分类）

**输出格式**：国际专利补充分析作为独立报告，与主报告合并参考。
文件命名：`TRIZ_报告_<课题>_国际专利补充分析.md`

### ⚠️ Google Patents API 速率限制

Google Patents REST API 在 ~3 次查询后返回 503 错误。应对策略：
- 使用**多个子代理并行**检索不同关键词，在限速前各完成 1-2 次查询
- 每次查询尽量用更精确的筛选条件（Assignee+关键词），减少结果数量
- 被限速后等待 24 小时再重试

### ⚠️ 专利检索 API 可靠性排序（2026-08 实测更新）

| 数据源 | 状态 | 可靠性 | 备注 |
|--------|------|--------|------|
| **EPO OPS** | ✅ 可用 | ⭐⭐⭐⭐⭐ | OAuth2认证，覆盖90+国家，36万+结果 |
| **triz-ai discover** | ✅ 可用 | ⭐⭐⭐⭐ | 仅中国专利(CNIPA) |
| **子代理浏览器检索** | ✅ 可用 | ⭐⭐⭐⭐⭐ | 最可靠，每次都能获取结果 |
| **Google Patents API** | ⚠️ 限流 | ⭐⭐⭐ | ~3次查询后返回503，需等待24h |
| **Lens.org** | ❌ 需付费 | — | 免费版功能有限 |
| **PatentsView** | ❌ 已迁移 | — | API端点变更，返回HTML |
| **Google Custom Search** | ⚠️ 需配置 | ⭐⭐ | 需项目启用API+计费账户+搜索引擎ID |
| **BigQuery** | ⚠️ 需配置 | ⭐⭐⭐ | 需Google Cloud服务账号 |

**推荐专利检索策略**（按优先级）：
1. `triz-ai discover` → 中国专利
2. `patent_search.py --sources epo` → 国际专利（EPO OPS，需配置凭据）
3. 子代理浏览器检索 Google Patents → 补充
4. Google Patents API（限流前3次）→ 补充

### ⚠️ EPO OPS OAuth2 认证方式（关键）

EPO OPS 使用 **HTTP Basic Auth + OAuth2** 认证，**不能用 `requests.auth` 参数**：

```python
import base64

# ✅ 正确 — 手动构建 Basic 认证头
credentials = f"{consumer_key}:{consumer_secret}"
encoded = base64.b64encode(credentials.encode()).decode()
headers = {
    "Authorization": f"Basic {encoded}",
    "Content-Type": "application/x-www-form-urlencoded"
}
resp = requests.post(token_url, headers=headers, data={"grant_type": "client_credentials"})

# ❌ 错误 — requests.auth 会导致 401 "Client credentials are invalid"
resp = requests.post(token_url, auth=(consumer_key, consumer_secret), ...)
```

**当前 EPO OPS 配置**（App: jianpatentops, Status: approved）：
```bash
export EPO_CONSUMER_KEY="your_consumer_key"
export EPO_CONSUMER_SECRET="your_consumer_secret"
```

### ⚠️ EPO OPS 返回 expires_in 是字符串（关键）

EPO OPS API 返回的 `expires_in` 是**字符串**而非整数，必须转换：

```python
# ❌ 错误 — TypeError: unsupported operand type(s) for +: 'float' and 'str'
self.token_expires = time.time() + data.get("expires_in", 3600) - 60

# ✅ 正确
self.token_expires = time.time() + int(data.get("expires_in", 3600)) - 60
```

### ⚠️ CSV 导出必须处理额外字段（关键）

Patent 数据类有 `family_id`, `claims_count`, `description_length`, `compliance_issues`, `citations` 等字段，CSV fieldnames 必须包含或使用 `extrasaction='ignore'`：

```python
# ❌ 错误 — ValueError: dict contains fields not in fieldnames
writer = csv.DictWriter(f, fieldnames=fieldnames)

# ✅ 正确 — 忽略不在 fieldnames 中的字段
writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')

# ✅ 或者 — 在 fieldnames 中包含所有字段
fieldnames = ["patent_id", "title", ..., "family_id", "claims_count", "description_length"]
```

### ⚠️ Google Custom Search API 配置复杂度

Google Custom Search API 需要**三重配置**才能使用：
1. **项目级启用**：Google Cloud Console → API 和服务 → 启用 Custom Search API
2. **计费账户**：某些项目需要关联计费账户
3. **搜索引擎 ID**：在 programmablesearchengine.google.com 创建搜索引擎，获取 cx 参数

**常见陷阱**：
- API Key 在启用 API **之前**创建 → Key 没有新 API 的权限 → 需要重新创建 Key
- 不同项目中的 API Key 无法访问其他项目的 API → 确保 Key 和 API 在同一项目
- 即使显示"已启用"，仍可能返回 403 "project does not have access" → 等待 5-10 分钟或重新创建 Key

**建议**：如果配置困难，直接使用子代理浏览器检索（最可靠）。

### ⚠️ SKILL.md 中引用的文件可能不存在

`cheatsheet.md`、`patterns.md`、`glossary.md` 在文件结构表中列出，但实际可能不存在于 skill 目录中。当子代理需要这些内容时，应直接使用 SKILL.md 中的知识或基于 TRIZ 理论生成，而非尝试读取不存在的文件。

### ⚠️ triz_md_to_docx.py 脚本可能不存在（关键）

SKILL.md 引用 `scripts/triz_md_to_docx.py` 作为 Word 生成工具，但该脚本**可能不在 skill 目录中**。如果运行时报 `No such file or directory`，需要**现场创建**该脚本。

**创建位置**：`scripts/triz_md_to_docx.py`（相对于 skill 目录）

**脚本功能要求**：
- 封面页（标题+副标题+作者+日期）
- 三级 TOC（Word 中右键"更新域"生成）
- 一级标题前自动分页
- 表格样式（深蓝表头白字，交替行颜色）
- 页边距：上下2.54cm，左右3.18cm
- 默认字体：Microsoft YaHei，11pt
- 内联格式支持：**粗体**、`代码`、*斜体*

**关键实现细节**：
```python
# TOC 域代码（必须用 XML 注入）
fldChar1 = parse_xml(f'<w:fldChar {nsdecls("w")} w:fldCharType="begin"/>')
instrText = parse_xml(f'<w:instrText {nsdecls("w")} xml:space="preserve"> TOC \\o "1-3" \\h \\z \\u </w:instrText>')

# 表格样式（深蓝表头）
shading = parse_xml(f'<w:shd {nsdecls("w")} w:fill="003366" w:val="clear"/>')
cell._tc.get_or_add_tcPr().append(shading)
```

### ⚠️ Python 类定义中不能在类级别使用 self（关键）

在 Python 类定义中，**类级别的字典/列表不能引用 `self`**，因为 `self` 只在实例方法中可用。

```python
# ❌ 错误 — NameError: name 'self' is not defined
class ComplianceChecker:
    REQUIREMENTS = {
        "check": self._check_method,  # ❌ self 在类级别不可用
    }

# ✅ 正确 — 在 __init__ 中定义
class ComplianceChecker:
    def __init__(self):
        self.REQUIREMENTS = {
            "check": self._check_method,  # ✅ self 在实例方法中可用
        }
```

**此 bug 在 patent_search.py v2.0 中出现过**，已修复。

### ⚠️ 专利检索 API 认证要求（关键）

| API | 认证方式 | 配置方法 | 优先级 |
|-----|----------|----------|--------|
| **Lens.org** | Bearer Token | 注册后获取 API Key，设置 `LENS_API_KEY` | ⭐⭐⭐⭐⭐ |
| **EPO OPS** | OAuth2 | 注册后获取 consumer_key/secret | ⭐⭐⭐⭐⭐ |
| **BigQuery** | Google Cloud | 设置 `GOOGLE_APPLICATION_CREDENTIALS` | ⭐⭐⭐⭐ |
| **PatentsView** | 无需认证 | 直接使用（但 API 格式可能已变更） | ⭐⭐⭐ |
| **Google Patents** | 无需认证 | 直接使用，**速率限制严格**（~3次后503） | ⭐⭐ |

**降级策略**：
1. Lens.org 不可用 → 跳过，使用 EPO
2. EPO 不可用 → 降级到 Google Patents
3. Google Patents 被限流 → 使用 triz-ai 本地数据 + AI 知识
4. 所有 API 都不可用 → 启动子代理通过浏览器手动检索

### ⚠️ 方案辩论系统已集成（v2.0 新增）

TRIZ 报告生成完成后，可自动启动**方案辩论系统**（`solution-debate` skill），通过正反两派对抗性辩论筛选 Top 3 方案。

**触发条件**：报告方案矩阵 ≥ 5 个候选方案时建议启动。

**架构**：四角色模式（正方+反方+裁判+落地分析专家），采用排名稳定性+评分差值混合收敛判定。

**执行流程**：
```
报告完成 → 提取方案矩阵 → Round1辩论(并行) → 收敛检查
  ├── 已收敛 → 裁决+落地分析(并行) → 输出
  └── 未收敛 → Round2交叉反驳 → 收敛检查 → ...（最多3轮）
```

**输出**：Top 3 方案 + 每方案8维度落地分析（市场/竞品/护城河/成本/GTM/路线图/风险/ROI）。

详细规则见 `solution-debate` skill。

### ⚠️ TRIZ 理论学习材料已创建

完整的 TRIZ 理论学习手册已创建：`~/Documents/TRIZ_理论学习手册.md`

**内容**：13 章 + 3 个附录，覆盖所有 TRIZ 工具的原理、方法和评价标准，每个工具配有简单示例。

**可用于**：生成培训材料、回答 TRIZ 理论问题、指导初学者学习。
