# Workflow Lessons Learned

## User Corrections from This Session

### 1. Strict Workflow Adherence is Mandatory

**User feedback**: "分析过程和之前定义的不符合" — The analysis must match the defined workflow exactly.

**Lesson**: Never skip steps or take shortcuts. When the user provides a technical problem, follow the AGENTS.md workflow step by step.

### 2. Report Depth Must Match Reference Standard (CRITICAL)

**User feedback**: "报告颗粒度不够，过于泛化，不够细致" — Reports are too shallow and generic.

**Reference**: AITRIZ 91-page report (`AITRIZ回答-课题报告：基于被动式预燃室的TGDI发动机全工况超稀薄燃烧稳定性研发-1.pdf`)

**Standard**: Each workflow node must produce detailed output:
- 课题梳理: 10 analysis items with detailed tables (background, defects, goals, MPV, S-curve, IFR, components, flow)
- 功能分析: Full component matrix, complete interaction analysis, function modeling for EVERY component
- 裁剪: At least 5 trimming plans with secondary problem resolution
- 因果链: At least 4 levels of decomposition, every leaf problem has a solution
- 聚焦关键问题: At least 10 problems evaluated with 4-dimension scoring
- 功能导向搜索: Every key problem gets 2+ cross-industry references
- 方案说明书: Detailed technical plan + implementation example + secondary problems
- 专利分析: At least 20 patents, 4+ sub-directions, competitive landscape, technology gaps

**禁止事项**:
- ❌ 禁止使用简单列表替代详细表格
- ❌ 禁止省略分析过程只给结论
- ❌ 禁止使用泛化描述替代具体数据
- ❌ 禁止跳过次级问题分析
- ❌ 禁止省略实施示例

### 3. Four-Dimension TRIZ Analysis Required

**User feedback**: Compared with reference report and found missing dimensions.

**Required TRIZ dimensions** (all must be analyzed):
1. **技术矛盾分析** — Contradiction Matrix + 40 Principles
2. **物理矛盾分析** — Separation Principles (时间/空间/条件/系统分离)
3. **物场分析** — Su-Field Model + 76 Standard Solutions
4. **技术进化趋势分析** — S-Curve + 8 Evolution Trends

**Additional required analyses**:
- 综合解决方案矩阵 (Cross-mapping all 4 dimensions)
- ARIZ-85C 深度分析 (3-Pass flow, optional but recommended)
- 扩展专利全景分析 (Deep patent mining, optional but recommended)
- 跨方法收敛分析 (Cross-method convergence verification)

### 4. Path Selection Gateway Was Missing in v2.0

**Issue**: When updating to v2.0 with 3-phase structure, the original path selection gateway (Radial/Convergent) was dropped.

**Fix**: Restored as "Step 0" before Phase 1.

### 5. 11-Question Routing Was Missing in v2.0

**Issue**: The 11-question problem routing diagnostic was not included in the v2.0 workflow.

**Fix**: Added between Phase 1 and Phase 2, with checklist verification.

### 6. 8 Trends Analysis Was Missing in v2.0

**Issue**: The 8 trends analysis tool was not explicitly required in the workflow.

**Fix**: Added as part of the routing step (when routing points to trends).

### 7. triz-ai CLI Pitfalls

**Model naming**: Must use raw model ID (e.g., `mimo-v2.5-pro`), NOT `openai/mimo-v2.5-pro`
**Embedding api_base**: Must be configured separately under `embeddings:` section
**Python version**: triz-ai requires Python >=3.12; must clear PYTHONPATH to avoid Hermes venv conflict
**MiMo API models**: Only `mimo-v2.5`, `mimo-v2.5-pro`, `mimo-v2.5-asr`, `mimo-v2.5-tts`

## Workflow Evolution Summary

| Version | Changes |
|---------|---------|
| v1.0 | Path gateway + 11-question routing + Triz-AI + tools + report (9 chapters) |
| v2.0 | Added 3-phase structure: Problem Analysis + Solution Generation + Implementation (12 chapters) |
| v2.1 | Restored path gateway, 11-question routing, 8 trends; added strict adherence pitfall |
| v3.0 | Added 4-dimension TRIZ analysis (physical contradiction, Su-Field), comprehensive solution matrix, ARIZ-85C, extended patent analysis, prototype design; added report granularity requirements |
| v3.1 | Added report detail requirements section (enforced 100+ page standard) |
| v3.2 | Added report quality self-assessment (10 dimensions, 100-point scoring) |

## 8. Report Generation Pattern (3-Part Parallel Delegation)

**Problem**: Single agent generating 100+ page reports hits context limits and produces thin content.

**Solution**: Split into 3 parts, delegate to 3 parallel subagents, then merge.

**Tested across 6 projects** with consistent results (217-281 KB, 92-117 pages).

See `references/report-generation-pattern.md` for detailed workflow.

## 9. Quality Self-Assessment Dimensions (v3.2)

**User feedback**: Reports need quality evaluation at the end.

**10 evaluation dimensions** (each 10 points, total 100):
1. 流程完整度 — Process completeness
2. 详细度 — Detail level
3. 数据支撑 — Data support
4. 表格规范 — Table standards
5. 专利分析深度 — Patent analysis depth
6. 方案可行性 — Solution feasibility
7. 次级问题分析 — Secondary problem analysis
8. 实施示例 — Implementation examples
9. 创新性 — Innovation
10. 可读性 — Readability

**Scoring**: 90-100 (优秀), 70-89 (良好), 50-69 (一般), 30-49 (较差), <30 (很差)
