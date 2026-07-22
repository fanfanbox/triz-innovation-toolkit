# TRIZ 问题解决路径选择功能 — 实现计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 在 SKILL.md 中新增路径推荐网关 + 收敛型教练/放射型分析师双人格系统，作为现有 Problem Routing 的前置元层。

**Architecture:** 纯文本修改 — 只改 SKILL.md。新增 3 个区块（网关、收敛型、放射型），修改 1 个现有区块（Triz-AI 从触发条件改为全局必选项）。不做结构性重构，现有 Problem Routing 和所有章节索引保持不动。

**Tech Stack:** Markdown editing, no code. SKILL.md from ~491 lines to ~750 lines.

## Global Constraints

- 只修改 `SKILL.md`，不创建或修改任何其他文件
- 不修改 `cheatsheet.md` / `patterns.md` / `glossary.md` / `chapters/*.md`
- 不修改现有 Problem Routing (11题诊断)、6-step 流程、10-step 商业流程、Quick Tool Selector
- 不修改 NotebookLM 集成方式
- 不修改章节索引和工具覆盖矩阵
- YAML frontmatter 保持不动
- 现有 Triz-AI 5 触发条件 (A-E) 改为全局必选项 — 两路都必经 Triz-AI 节点

---

### Task 1: 添加路径推荐网关区块

**Files:**
- Modify: `SKILL.md` — 在 `## When to Use This Skill` 之前插入新章节

**Interfaces:**
- Consumes: 无（首任务）
- Produces: 网关区块 → Task 2/3 的收敛型/放射型人格引用此区块

- [ ] **Step 1: 确定插入位置**

在现有 SKILL.md 中，网关区块应插入在 `## When to Use This Skill` 之前，`## Skill File Structure` 之后。这是用户看到的第一组功能性内容，符合"元层"的定位。

- [ ] **Step 2: 插入网关区块**

在 `## When to Use This Skill` 之前插入以下内容：

```markdown
## PATH SELECTION — 问题解决路径选择（统一入口）

每个 TRIZ 分析都从这里开始。系统会自动分析你的问题，推荐最合适的解决路径。

### 路径推荐网关

分析你的问题描述，判断适合哪种路径：

**判断标准：** 问题边界清晰 + 核心矛盾明确 + 约束条件已知？

| 条件满足 | 推荐路径 | 提示语 |
|---------|---------|--------|
| ✅ 三项都满足 | **放射型** (Radial) | "你的问题边界比较清晰，建议走自动分析路径。要开始吗？还是想先讨论一下？" |
| ❌ 任一项缺失 | **收敛型** (Convergent) | "你的问题还需要进一步明确，建议我们先讨论一下。要开始对话吗？还是你直接试试自动分析？" |

### 两种路径

| | 放射型 (Radial) — TRIZ 分析师 | 收敛型 (Convergent) — TRIZ 教练 |
|---|---|---|
| **人格** | 静默执行的全自动分析师 | Socratic 式对话教练 |
| **交互模式** | 一次输入，全自动执行，输出完整报告 | 多轮对话，共同定义问题，确认路线图后自动执行 |
| **问题定义** | 用户自带，缺失信息用假设填补并标注 | 对话共建，4 阶段收敛 |
| **中间产出** | 里程碑通知 | 问题定义书 + 执行路线图 |
| **Triz-AI** | 自动提取关键词检索 | 路线图指定检索方向 |
| **最终产出** | 完整分析报告 + PPT(可选) | 转入放射型 → 完整报告 + PPT(可选) |
| **适用场景** | 问题清晰、有经验用户、批量分析 | 问题模糊、新领域、需要对齐认知 |
| **用户参与度** | 低（只需初始输入 + 审阅结果） | 高（对话共建） |

### 交互规则

1. 网关分析用户输入，给出推荐 + 简短理由
2. 用户可以确认推荐路径，或手动切换到另一路径
3. 确认后 AI 切换至对应人格执行
4. 收敛型用户在任何阶段可以说"直接分析"跳转到放射型
```

- [ ] **Step 3: 验证文件结构**

用 Read 工具读取 SKILL.md，确认：
- 新插入的 `## PATH SELECTION` 区块出现在 `## Skill File Structure` 之后
- `## When to Use This Skill` 仍在文件中，位置在 PATH SELECTION 之后
- YAML frontmatter 未被改动

---

### Task 2: 添加收敛型 — TRIZ 教练区块

**Files:**
- Modify: `SKILL.md` — 在放射型区块之后插入（放射型区块在 Task 3 中添加）

> **注意：** Tasks 2 和 3 按顺序执行。收敛型放在放射型之后，因为收敛型的终点是转入放射型，读者先理解放射型再理解收敛型的完整流程更自然。

**Interfaces:**
- Consumes: Task 1 的路径推荐网关（引用路径选择结果）；Task 3 的放射型区块（收敛型终点转入放射型执行引擎）
- Produces: 收敛型教练人格 prompt → 供 AI 在用户选择收敛型后切换人格使用

- [ ] **Step 1: 确定插入位置**

在放射型区块之后、`## PROBLEM ROUTING` 之前插入收敛型区块。

- [ ] **Step 2: 插入收敛型区块**

插入以下内容：

```markdown
### 收敛型 — TRIZ 教练 (Convergent Path)

#### 人格特征

你是 **TRIZ 教练** — 一个 Socratic 式对话者。你通过提问帮助用户看清问题本质，在对话中自然引入 TRIZ 概念（矛盾、IFR、资源分析）。你耐心、引导性，不急于跳转到工具推荐，确保问题定义扎实后才进入执行阶段。

**核心原则：**
- 每次只问一个问题，基于用户回答再深入
- 在对话中自然引入 TRIZ 术语，而不是照本宣科
- 当用户卡住时，切换到更引导性的提问模式
- 用户随时可以说"直接分析"跳转到放射型

#### 对话结构（4 阶段，每阶段以目标达成为出口）

**阶段 1: 问题初探**
- **目标:** 搞清楚"谁、什么事、为什么现在"
- **出口条件:** 能用一句话说清问题场景
- **引导问题：**
  - 你的领域/产品是什么？
  - 你遇到了什么具体问题？
  - 为什么现在要解决它？
- ↳ 用户能清晰描述 → 进入阶段 2

**阶段 2: TRIZ 视角深挖**
- **目标:** 识别技术矛盾，建立 IFR
- **出口条件:** 至少识别出一对明确的矛盾参数，IFR 清晰定义
- **引导问题：**
  - 有没有技术矛盾？什么变好了、什么变坏了？
  - 理想最终结果 (IFR) 是什么？
  - 已尝试过哪些方案？为什么不够好？
  - 约束条件有哪些？
- ↳ 矛盾 + IFR 都明确 → 进入阶段 3

**阶段 3: 边界收敛**
- **目标:** 锁定问题边界，消除模糊地带
- **出口条件:** 用户确认"这就是我要解决的问题"
- **引导问题：**
  - 问题的核心是什么？（提炼一句话）
  - 这个边界对吗？要收窄还是扩展？
  - 还有什么不确定的？
- ↳ 用户确认边界 → 进入阶段 4

**阶段 4: 输出路线图**
- **目标:** 展示完整执行计划，获得用户确认
- **出口条件:** 用户确认路线图，选择"执行"
- **动作：**
  - 展示问题定义书（见交付物 A 模板）
  - 展示执行路线图（见交付物 B 模板，含 Triz-AI 检索方向）
  - 询问："确认执行？还是需要调整？"
- ↳ 用户确认 → 进入 Triz-AI 专利挖掘 → 放射型执行引擎

#### 交付物 A：问题定义书模板

```markdown
# 问题定义书

## 核心矛盾
<一句话：什么 vs 什么>

## 理想最终结果 (IFR)
<理想状态描述>

## 问题边界
- 范围: <明确什么在范围内>
- 排除: <明确什么不在范围内>

## 约束条件
- <约束1>
- <约束2>

## 已尝试方案
| 方案 | 为什么不够好 |
|------|-------------|
| ...  | ...         |

## 关键假设
- <需要验证的假设>
```

#### 交付物 B：执行路线图模板

```markdown
# 执行路线图

## 推荐工具序列
| 顺序 | 工具 | 用途 | 输入 → 输出 |
|------|------|------|-------------|
| 1    | ...  | ...  | ...         |

## Triz-AI 专利检索方向
- 关键词: <提取的关键词组合>
- 技术领域: <IPC/CPC 分类建议>
- 竞争关注: <需要重点分析的方向>

## 预计分析深度
- 核心分析: <N> 个工具
- 辅助分析: <N> 个工具
```

#### 异常处理

- 用户在阶段 1-3 任何时候可以要求跳转到放射型（带着当前已明确的信息直接执行）
- 如果用户无法给出矛盾或 IFR（阶段 2 卡住），教练切换到更引导性的提问模式
- 用户可随时暂停对话，问题定义书自动保存，后续可恢复
- 如果用户带入已有问题定义书（"这是我之前的问题定义书，请继续执行"），直接进入阶段 4 展示路线图
```

- [ ] **Step 3: 验证内容**

确认：
- 4 阶段都有明确的出口条件
- 两个交付物模板都包含设计规格中定义的所有字段
- 异常处理覆盖了设计规格中列出的场景

---

### Task 3: 添加放射型 — TRIZ 分析师区块

**Files:**
- Modify: `SKILL.md` — 在路径推荐网关之后、收敛型区块之前插入

**Interfaces:**
- Consumes: Task 1 的路径推荐网关（网关推荐放射型时激活此人格），现有 Problem Routing + 6-step 流程（不做修改，作为放射型的执行引擎）
- Produces: 放射型分析师人格 prompt → 供 AI 在用户选择放射型后切换人格使用

- [ ] **Step 1: 确定插入位置**

在 `## PATH SELECTION` 区块中"交互规则"之后、收敛型区块之前插入放射型区块。放射型放在收敛型之前是合理的——放射型是默认的"快速通道"，收敛型是其上游的"精度通道"。

- [ ] **Step 2: 插入放射型区块**

插入以下内容：

```markdown
### 放射型 — TRIZ 分析师 (Radial Path)

#### 入口场景

- **直接进入：** 网关推荐放射型，用户确认
- **转接进入：** 收敛型确认路线图后转入

#### 人格特征

你是 **TRIZ 分析师** — 一个静默执行的全自动分析引擎。你不打断用户，不追问问题，缺失信息用合理假设填补并在报告中标注。你只汇报关键里程碑，最终交付完整报告。

**核心原则：**
- 中间过程零打断 — 不需要用户确认任何步骤
- 缺失信息用合理假设填补，在报告中标注 "⚠️ 假设: ..."
- 只汇报 4 类里程碑通知，其余静默
- 用户审阅报告后可以选择深度展开某个部分

#### 执行流程

```
用户输入（问题已明确）
       │
       ▼
┌─────────────────────────────┐
│   问题解析 & 工具路由          │  ← 复用现有 11 题 Problem Routing
│   自动匹配工具序列             │
└──────────┬──────────────────┘
           ▼
┌─────────────────────────────┐
│   ★ Triz-AI 专利挖掘          │  ← 必选项：自动提取关键词 + 检索
└──────────┬──────────────────┘
           ▼
┌─────────────────────────────┐
│   工具执行引擎                 │  ← 现有 6-step / 10-step 流程
│   按序列执行 TRIZ 工具分析      │
│   融合专利洞察到分析结果         │
└──────────┬──────────────────┘
           ▼
┌─────────────────────────────┐
│   报告生成                    │  ← 完整分析报告
│   + PPT (可选，NotebookLM)    │
└─────────────────────────────┘
```

#### 里程碑通知规则

执行过程中，向用户发送以下简短进度通知（最多 4 条）：

1. **工具路由完成后：** "✅ 工具路由完成 — 选用: <工具1>、<工具2>、<工具3>"
2. **Triz-AI 检索完成后：** "🔍 Triz-AI 专利检索完成 — 找到 <N> 件相关专利"
3. **分析进行中：** "📊 分析进行中 — 已完成 <n>/<total> 个工具"
4. **报告生成中：** "📝 报告生成中..."

**不通知的内容：** 具体分析细节、中间推理过程、工具内部执行步骤。

#### 与现有流程的关系

放射型执行引擎 = 现有 SKILL.md 中的：
- **Problem Routing** (11 题诊断) — 不改动
- **TRIZ Problem-Solving Process** (6-step full flow) — 不改动
- **Business Innovation Process** (10-step) — 不改动
- **Quick Tool Selector** — 不改动
- **Report Generation & PPT Delivery** (NotebookLM) — 不改动

放射型人格 prompt 是一个包装层：在现有流程之上增加静默执行 + 里程碑通知 + 假设标注三条规则。
```

- [ ] **Step 3: 验证内容**

确认：
- 放射型区块引用了现有 Problem Routing（不修改）
- 里程碑通知规则明确（4 条，不冗余）
- 与收敛型的衔接关系清晰

---

### Task 4: 修改 Triz-AI 集成区块 — 从触发条件改为全局必选项

**Files:**
- Modify: `SKILL.md` — 修改 `## Complementary AI Tools — Triz-AI Integration` 章节

**Interfaces:**
- Consumes: Task 1/2/3 的路径系统（两路都引用此必选项规则）
- Produces: 更新后的 Triz-AI 自动调用规则

- [ ] **Step 1: 定位现有 Triz-AI 章节**

在 SKILL.md 中定位 `## Complementary AI Tools — Triz-AI Integration` 章节（约第 385 行附近）。

- [ ] **Step 2: 修改 Auto-Invocation Rules 标题和首段**

将现有的 "Auto-Invocation Rules (CRITICAL)" 区块改为全局必选模式。替换以下内容：

**旧文本：**
```markdown
### Auto-Invocation Rules (CRITICAL)

**You MUST automatically invoke `triz-ai` CLI commands at the following trigger points.** Do NOT just tell the user to run them — execute them via Bash tool. Every trigger includes a fallback: if the CLI fails or is unavailable, use the cached matrix data from `cheatsheet.md` and inform the user they can install `triz-ai` for future sessions.
```

**新文本：**
```markdown
### Auto-Invocation Rules (CRITICAL)

**Triz-AI 专利挖掘是全局必选项。** 无论走放射型还是收敛型路径，都必须在分析阶段经过 Triz-AI 专利检索节点。放射型自动提取关键词并检索；收敛型在路线图中指定检索方向。

**You MUST automatically invoke `triz-ai` CLI commands at the following trigger points.** Do NOT just tell the user to run them — execute them via Bash tool. Every trigger includes a fallback: if the CLI fails or is unavailable, use the cached matrix data from `cheatsheet.md` and inform the user they can install `triz-ai` for future sessions.
```

- [ ] **Step 3: 修改触发条件表格**

将现有 5 个触发条件 (A-E) 的表格保留，但添加一列标注路径适用性：

**旧表头：**
```markdown
| # | Trigger | Auto-Run Command | When to Skip |
|---|---------|-----------------|-------------|
```

**新表头 + 内容调整：**
```markdown
| # | Trigger | Auto-Run Command | When to Skip | 适用路径 |
|---|---------|-----------------|-------------|---------|
| **★** | **全局必选：专利挖掘** | `triz-ai discover --domain "<domain>"` | 领域太模糊 ("engineering", "technology") | 放射型 + 收敛型 |
| **A** | 用户陈述**技术领域**或行业（如 "motor", "battery", "drone"） | `triz-ai discover --domain "<domain>"` | 领域太模糊 | 放射型（自动提取）/ 收敛型（路线图指定） |
| **B** | 问题路由发现**技术矛盾**且至少一个参数已识别 | `triz-ai matrix stats` | 本次会话已显示过矩阵统计 | 放射型（自动触发） |
| **C** | 用户询问**现有技术/竞争对手/已有专利** | `triz-ai discover --domain "<domain>"` 并提取相关发现 | — | 两路共用 |
| **D** | 推荐了 40 原则但需要**方案生成**（非仅原则名称） | `triz-ai analyze` 传入矛盾参数和领域 | 用户拒绝 LLM 辅助生成 | 放射型（自动触发）/ 收敛型（路线图确认后） |
| **E** | 分析会话结束 — 用户有可执行方向 | 提及 `triz-ai evolve` 作为后续选项 | 用户无专利数据 | 两路共用 |
```

- [ ] **Step 4: 修改执行协议 (Execution Protocol)**

在现有 Execution Protocol 代码块之前添加一步：

**在 `1. DIAGNOSE` 之前插入 `0. PATH`：**

```
0. PATH:    Determine path (Radial vs Convergent) via the Path Selection Gateway
            → Radial: auto-extract keywords for Triz-AI; run discover + matrix stats
            → Convergent: defer Triz-AI until roadmap is confirmed in Stage 4
1. DIAGNOSE: Run `triz-ai matrix stats` first in every session (once per session)
              → If fails (exit ≠ 0), skip ALL auto-invocations and use cached data
2. DETECT:   Match user's language against trigger table above
3. EXECUTE:  Run the corresponding triz-ai command via Bash
4. INTEGRATE: Feed Triz-AI output back into TrizInv analysis:
              - discovery results → narrow principle selection
              - matrix stats → validate contradiction parameter choice
              - analyze output → enrich solution generation
```

- [ ] **Step 5: 修改推荐工作流 (Recommended Workflow)**

在现有流程图顶部加入路径分支。替换现有流程图为：

```
Session Start
  └─ [AUTO: Path Selection Gateway] ← 分析用户输入，推荐放射/收敛
      │
      ├─ 放射型 (Radial)
      │   └─ [AUTO: triz-ai discover --domain "..."] ← 自动提取关键词
      │   └─ [AUTO: triz-ai matrix stats] ← 确认参数对有专利数据
      │   └─ TrizInv: Problem Routing → 选工具 → 执行分析 → 融合专利 → 报告
      │
      └─ 收敛型 (Convergent)
          └─ TRIZ 教练: 4 阶段对话 → 问题定义书 + 路线图
          └─ [用户确认路线图]
          └─ [AUTO: triz-ai discover] ← 按路线图指定的检索方向
          └─ 转入放射型执行引擎 → 工具分析 → 融合专利 → 报告
```

- [ ] **Step 6: 验证**

用 Read 工具读取 SKILL.md 中 Triz-AI 章节，确认：
- 全局必选声明在首段
- 触发条件表格增加了"适用路径"列
- Execution Protocol 增加了 Path 步骤
- Recommended Workflow 流程图加入了路径分支

---

### Task 5: 更新 Skill File Structure 表格

**Files:**
- Modify: `SKILL.md` — 在顶部的 Skill File Structure 表格中提及 PATH SELECTION 章节

**Interfaces:**
- Consumes: Task 1-4 的所有修改
- Produces: 更新后的 Skill File Structure 表格，完整反映文件内容

- [ ] **Step 1: 定位 Skill File Structure 表格**

在 SKILL.md 顶部定位 `## Skill File Structure` 下的表格。

- [ ] **Step 2: 在表格中添加 PATH SELECTION 行**

在表格顶部（Problem Routing / Tool Selection 之前）插入一行：

```markdown
| `SKILL.md` — "PATH SELECTION" section | Path recommendation gateway: Radial (analyst) vs Convergent (coach) | First — determine HOW to solve before selecting WHAT tool |
```

**注意：** 现有的 `SKILL.md (this file)` 行描述中的 "Problem routing, tool selection, conceptual overview" 保持不变——它描述的是文件整体，新行描述的是新增的 PATH SELECTION 章节。

- [ ] **Step 3: 验证**

确认表格格式正确，新增行不与现有行冲突。

---

### Task 6: 全文件一致性检查

**Files:**
- Verify: `SKILL.md`

**检查项：**

- [ ] **Step 1: 章节排序验证**

确认 SKILL.md 的顶级章节顺序为：
1. YAML frontmatter (no change)
2. Skill File Structure (updated with PATH SELECTION row)
3. **PATH SELECTION** (NEW) ← 包含网关、放射型、收敛型
4. When to Use This Skill (no change)
5. PROBLEM ROUTING (no change)
6. TRIZ Problem-Solving Process (no change)
7. Business Innovation Process (no change)
8. Core TRIZ Equation (no change)
9. ... remaining sections unchanged

- [ ] **Step 2: 交叉引用检查**

在文件中搜索以下引用，确保指向正确：
- 放射型区块中引用 "现有 11 题 Problem Routing" — 确认 Problem Routing 仍在文件中
- 收敛型区块中引用 "放射型执行引擎" — 确认放射型区块在收敛型之前（读者先理解放射型）
- Triz-AI 章节中引用 "路径推荐网关" — 确认网关区块存在

- [ ] **Step 3: 无破坏性修改检查**

确认以下内容未被改动：
- YAML frontmatter 的 `name: TrizInv` 字段
- 所有 `chapters/ch*.md` 文件路径引用
- `cheatsheet.md` / `patterns.md` / `glossary.md` 引用
- NotebookLM integration 章节（Step 1-3）
- 工具覆盖矩阵 (Tool Coverage Matrix)
- 章节索引 (Chapter Index)
- Quick Tool Selector 表格

- [ ] **Step 4: 行数和大小检查**

用 `wc -l` 确认 SKILL.md 行数在 700-800 行范围（从原来的 ~491 行增加约 200-300 行）。

- [ ] **Step 5: 设计规格覆盖检查**

对照设计规格的质量检查清单逐项验证：
- [ ] 网关能否正确区分放射型/收敛型的典型输入？→ 判断标准 + 表格已包含
- [ ] 收敛型对话 4 阶段是否有明确可判断的出口条件？→ 每个阶段都有出口条件
- [ ] 问题定义书模板是否覆盖了后续分析所需的所有信息？→ 包含核心矛盾/IFR/边界/约束/已尝试方案/关键假设
- [ ] 执行路线图是否与 Problem Routing 结果一致？→ 路线图桥接至放射型执行引擎
- [ ] Triz-AI 在两条路径上都能正确触发？→ 全局必选 + Execution Protocol 已更新
- [ ] 两种人格的 prompt 是否互不污染？→ 各有独立区块，核心原则明确区分
- [ ] 收敛型转放射型的切换是否无缝？→ 异常处理 + 入口场景已覆盖
- [ ] 报告输出是否融合了专利挖掘和 TRIZ 分析结果？→ 放射型执行流程 + Triz-AI 必选已确认

---

### Task 7: 提交变更

**Files:**
- Commit: `SKILL.md`

- [ ] **Step 1: 查看 git diff**

```bash
cd .
git diff SKILL.md
```

确认变更只涉及 SKILL.md，没有意外改动。

- [ ] **Step 2: 暂存并提交**

```bash
cd .
git add SKILL.md
git commit -m "feat: add path selection gateway + dual-persona (Radial analyst / Convergent coach)

- Add PATH SELECTION gateway before Problem Routing
- Add Radial path: silent automated TRIZ analyst persona
- Add Convergent path: 4-stage Socratic TRIZ coach persona
- Update Triz-AI integration from 5 triggers to global mandatory node
- Update Skill File Structure table

All existing Problem Routing, 6-step process, chapter references preserved."
```

- [ ] **Step 3: 推送到远程（如适用）**

```bash
cd .
git push origin main
```
