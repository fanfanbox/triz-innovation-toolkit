# Superpowers Skills 完全实操指南

> 基于 Superpowers v6.1.0 的 10 个真实 Skill，用一个 DHT 项目实例，Step-by-Step 展示从想法到合并的全流程。

---

## 前置概念：什么是 Skill？

Skill 不是"快捷指令"。Skill 是**行为约束规则**——它规定了 Claude 在特定场景下**必须做什么、禁止做什么、以什么顺序做**。

```
你说 "我想加个功能"
     ↓
Claude 检查: 这触发了 brainstorming skill 吗？ → 是 → 加载 brainstorming 规则
     ↓
规则说: "设计批准前禁止写代码" → Claude 不会写代码，而是先问你问题
```

**每一个 Skill 都有"铁律"（Iron Law）和"红线"（Red Flags）**。铁律是不可违反的约束；红线是触发时必须停下来的信号。

本 Tutorial 会逐条标注：每一条行为来自哪个 Skill 的哪条规则。

---

## 示例任务：为 DHT 项目增加 Range Extender 多工况功率扫描

**项目背景**：DHT（Dedicated Hybrid Transmission）拓扑自动探索平台，MATLAB R2025a classdef + dht_core graph API。当前分支 `feature/range-extender-power-scan`，19/19 tests passing。核心组件：`SynthesisController`、`ParallelCandidateGenerator`、`RatioEvaluator`、`RangeExtenderController`。

**需求**：当前的 RangeExtenderController 只在单一额定工况下评估增程器功率。用户希望扩展为"在 WLTC 多工况下扫描增程器的最佳功率匹配点"。

**用户不会写代码。全程用对话驱动。**

---

## Round 1 — brainstorming：从想法到 Spec

### 触发条件

```
用户: "我想给 RangeExtenderController 加一个多工况功率扫描功能。"
```

Claude 内部判断：用户描述的是"创建功能、添加功能"→ 触发 `brainstorming` skill。

### 规则来源

所有以下行为均来自 [brainstorming/SKILL.md](C:\Users\jianw\.claude\plugins\cache\claude-plugins-official\superpowers\6.1.0\skills\brainstorming\SKILL.md)：

| 规则 | SKILL.md 原文 |
|------|--------------|
| HARD-GATE: 设计批准前禁止写代码 | `<HARD-GATE> Do NOT invoke any implementation skill, write any code...until you have presented a design and the user has approved it.</HARD-GATE>` |
| 先检查项目上下文 | Checklist #1: "Explore project context — check files, docs, recent commits" |
| 一次只问一个问题 | "One question at a time" |
| 多选优先 | "Multiple choice preferred" |
| 提 2-3 个方案 | "Propose 2-3 different approaches with trade-offs" |
| 设计分节呈现 | "Present design — in sections scaled to their complexity, get user approval after each section" |
| Spec 自审 | "Spec Self-Review: placeholder scan, internal consistency, scope check, ambiguity check" |
| 用户审阅门 | "User Review Gate: ask user to review the written spec before proceeding" |
| 终态是 writing-plans | "The terminal state is invoking writing-plans. Do NOT invoke any other skill." |

### 实时对话

```
Claude: 让我先看看项目当前状态。
        [自动读取 CLAUDE.md、项目结构、最近的 spec 文件]
        [自动读取 RangeExtenderController.m 了解当前接口]

        看完了。你的项目是 MATLAB classdef + dht_core graph API。
        RangeExtenderController 目前:
        - 输入: 单一工况点 (转速, 扭矩)
        - 输出: 最佳增程器功率匹配
        - 调用方: SynthesisController.postProcess()

        第一个问题：多工况扫描的范围是什么？
        A. WLTC 的 3 个速度段（低/中/高）各取代表点
        B. WLTC 全工况点逐个扫描
        C. 用户自定义工况列表
        D. A + C（默认 WLTC 代表点，支持自定义覆盖）

你: A + C，默认 WLTC 代表点但允许自定义。

Claude: 明白。下一个问题：扫描结果的输出形式？
        A. 每个工况点的最优功率值（数值数组）
        B. 包含功率 + 效率 + 约束边界的完整报告
        C. 自动选择覆盖最多工况的"全能型"功率点
        D. B + C

你: D — 既要完整报告，也要自动推荐。

Claude: 好。最后一个问题：这个功能对现有接口的破坏程度？
        A. 新增独立方法，不改现有接口（完全向后兼容）
        B. 修改现有 evaluate() 方法签名，增加工况列表参数
        C. 新建一个 MultiConditionScanner 类，RangeExtenderController 保持不变

你: A — 独立方法，不影响现有调用。

Claude: 清楚了。我建议的方案：

        **方案 A（推荐）：独立扫描方法 + Struct 报告**

        在 RangeExtenderController 中新增：
        - scanMultipleConditions(conditions) → 对每个工况点运行现有 evaluate()，
          汇总为 struct array
        - recommendBestMatch(scanResults) → 从扫描结果中选最优功率点
        - 默认 WLTC 代表点作为类的 constant property

        优势：
        - 零破坏性（现有 evaluate() 不变）
        - 每个方法可独立测试
        - 默认工况点内置，开箱即用

        **方案 B：独立 Scanner 类**

        新建 MultiConditionScanner 类，组合 RangeExtenderController：
        - 更清晰的关注点分离
        - 但增加了类的数量，且两个类耦合度高

        **方案 C：Pipeline 模式**

        在 ParallelCandidateGenerator 中增加扫描步骤：
        - 集成度最高，但会污染候选生成逻辑
        - 不推荐（违反单一职责）

        我推荐方案 A。你看这个方向对吗？

你: 方案 A 可以。

Claude: [写 spec → 自审]

        Spec 自审完成：
        ✅ 无 placeholder / TBD
        ✅ 接口定义与现有代码一致
        ✅ scope 适中（单个类加 2 个方法 + 测试）
        ✅ 无歧义

        Spec 已保存到:
        docs/superpowers/specs/2026-07-07-range-extender-multi-condition-scan-design.md

        请 review 这个 spec，有任何修改告诉我，然后我们写 implementation plan。
```

### 这一步你看到了什么

1. **HARD-GATE 生效**：Claude 没有写一行代码，尽管"加两个方法"听起来很简单
2. **逐题递进**：每次只问一个问题，每个问题给多选
3. **2-3 方案对比**：A/B/C 三个方案，各有利弊，有推荐
4. **Spec 自审**：写完后自己检查 placeholder、一致性、scope、歧义
5. **用户审阅门**：不是直接开始实现，而是等你 review spec

---

## Round 2 — writing-plans：从 Spec 到可执行 Plan

### 触发条件

```
用户: "spec 没问题，继续"
```

Claude 判断：设计已批准 → 自动过渡到 `writing-plans`（brainstorming checklist #9 规定）。

### 规则来源

所有以下行为均来自 [writing-plans/SKILL.md](C:\Users\jianw\.claude\plugins\cache\claude-plugins-official\superpowers\6.1.0\skills\writing-plans\SKILL.md)：

| 规则 | SKILL.md 原文 |
|------|--------------|
| Plan Header 格式 | "Every plan MUST start with this header: Goal / Architecture / Tech Stack / Global Constraints" |
| 任务结构 | checkbox 语法 + Files + Interfaces (Consumes/Produces) |
| Bite-sized | "Each step is one action (2-5 minutes)" |
| TDD 强制 | "TDD" 在 Remember 中列出 |
| 禁止占位符 | "No Placeholders" 章节列出 6 种禁止模式 |
| 自审 | "Self-Review: spec coverage, placeholder scan, type consistency" |
| 执行交接 | "Execution Handoff: Two execution options — Subagent-Driven (recommended) or Inline Execution" |

### Plan 文件内容（关键部分节选）

````markdown
# Range Extender Multi-Condition Power Scan Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development
> (recommended) or superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Extend RangeExtenderController with multi-condition scanning and automatic
best-match recommendation.

**Architecture:** Two new methods on RangeExtenderController — scanMultipleConditions()
loops over evaluate() per condition point, recommendBestMatch() scores and ranks results.
Default WLTC points stored as constant property. Zero breaking changes to existing API.

**Tech Stack:** MATLAB R2025a classdef, dht_core graph API, MATLAB unit test framework

## Global Constraints

- All methods must be backward-compatible (existing evaluate() signature unchanged)
- Use MATLAB classdef property validation
- Test class inherits from matlab.unittest.TestCase
- WLTC default points: [low=40km/h, mid=70km/h, high=100km/h] with corresponding load factors

---

### Task 1: Default WLTC Condition Points

**Files:**
- Modify: `dht_core/RangeExtenderController.m` (add constant property)
- Test: `tests/testRangeExtenderController.m` (add test for new property)

**Interfaces:**
- Produces: `RangeExtenderController.DEFAULT_WLTC_CONDITIONS` — struct array with fields
  `.speed_kmh` (double), `.load_factor` (double), `.label` (string)

- [ ] **Step 1: Write the failing test**

```matlab
function testDefaultWLTCConditions(testCase)
    points = RangeExtenderController.DEFAULT_WLTC_CONDITIONS;
    testCase.verifyEqual(numel(points), 3);
    testCase.verifyEqual(points(1).speed_kmh, 40);
    testCase.verifyEqual(points(3).speed_kmh, 100);
end
```

- [ ] **Step 2: Run test to verify it fails**

Run: `matlab -batch "runtests('tests/testRangeExtenderController.m', 'ProcedureName', 'testDefaultWLTCConditions')"`
Expected: FAIL — "Unrecognized property 'DEFAULT_WLTC_CONDITIONS'"

- [ ] **Step 3: Add constant property to RangeExtenderController**

```matlab
properties (Constant)
    DEFAULT_WLTC_CONDITIONS = struct(...
        'speed_kmh', {40, 70, 100}, ...
        'load_factor', {0.3, 0.5, 0.7}, ...
        'label', {'WLTC-Low', 'WLTC-Mid', 'WLTC-High'});
end
```

- [ ] **Step 4: Run test to verify it passes**

Run: `matlab -batch "runtests('tests/testRangeExtenderController.m', 'ProcedureName', 'testDefaultWLTCConditions')"`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add dht_core/RangeExtenderController.m tests/testRangeExtenderController.m
git commit -m "feat: add DEFAULT_WLTC_CONDITIONS constant property to RangeExtenderController"
```

---

### Task 2: scanMultipleConditions Method

**Files:**
- Modify: `dht_core/RangeExtenderController.m`
- Test: `tests/testRangeExtenderController.m`

**Interfaces:**
- Consumes: `DEFAULT_WLTC_CONDITIONS` (from Task 1), `evaluate(speed_kmh, load_factor)` (existing)
- Produces: `scanResults = scanMultipleConditions(conditions)` where `conditions` is a struct
  array like DEFAULT_WLTC_CONDITIONS; `scanResults` is a struct array with additional fields
  `.optimal_power_kw` (double), `.efficiency` (double), `.constraint_satisfied` (logical)

- [ ] **Step 1: Write failing test**

```matlab
function testScanMultipleConditions(testCase)
    ctrl = RangeExtenderController();
    results = ctrl.scanMultipleConditions(ctrl.DEFAULT_WLTC_CONDITIONS);
    testCase.verifyEqual(numel(results), 3);
    testCase.verifyTrue(all([results.constraint_satisfied]));
    testCase.verifyTrue(all([results.optimal_power_kw] > 0));
end
```

- [ ] **Step 2: Verify test fails**

Run: `matlab -batch "runtests('tests/testRangeExtenderController.m', 'ProcedureName', 'testScanMultipleConditions')"`
Expected: FAIL — "Undefined method 'scanMultipleConditions'"

- [ ] **Step 3: Implement scanMultipleConditions**

```matlab
function results = scanMultipleConditions(obj, conditions)
    arguments
        obj
        conditions struct
    end
    results = conditions;
    for i = 1:numel(conditions)
        evalResult = obj.evaluate(conditions(i).speed_kmh, conditions(i).load_factor);
        results(i).optimal_power_kw = evalResult.power_kw;
        results(i).efficiency = evalResult.efficiency;
        results(i).constraint_satisfied = evalResult.feasible;
    end
end
```

- [ ] **Step 4: Run test to verify pass**

Run: `matlab -batch "runtests('tests/testRangeExtenderController.m', 'ProcedureName', 'testScanMultipleConditions')"`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add dht_core/RangeExtenderController.m tests/testRangeExtenderController.m
git commit -m "feat: add scanMultipleConditions method to RangeExtenderController"
```

---

### Task 3: recommendBestMatch Method + Integration

（Task 3 结构同上，包含 recommendBestMatch 的实现 + 集成测试，此处省略以节省篇幅）
````

### 实时对话

```
Claude: [加载 writing-plans skill]

        I'm using the writing-plans skill to create the implementation plan.

        [按 spec 逐条拆解为 bite-sized 任务]
        [每个任务有: Files / Interfaces (Consumes & Produces) / 5步 TDD 循环]
        [每个步骤有: 完整代码 + 精确命令 + 期望输出]
        [自审: spec 覆盖 ✅ / 无 placeholder ✅ / 类型一致 ✅]

        Plan 完成，保存到:
        docs/superpowers/plans/2026-07-07-range-extender-multi-condition-scan.md

        两个执行选项：

        1. Subagent-Driven (推荐) — 每个任务派一个全新的子代理，
           任务间自动 review，快速迭代
        2. Inline Execution — 在当前会话中按步执行，批量推进

        选哪个？

你: 选 1，Subagent-Driven。
```

### 这一步你看到了什么

1. **Header 格式**：Goal / Architecture / Tech Stack / Global Constraints 四项必填
2. **Interfaces 块**：每个任务明确声明 Consumes（依赖哪个前置任务的输出）和 Produces（产出什么接口给后续任务）
3. **Bite-sized**：每个步骤 2-5 分钟，不是"实现 XX 功能"这种模糊任务
4. **无占位符**：没有 TBD、TODO、"添加适当的错误处理"这种空洞描述
5. **执行交接**：不是自动开始写代码，而是给你两个选项

---

## Round 3 — subagent-driven-development：SDD 执行

### 触发

```
用户: "选 1，Subagent-Driven"
```

### 规则来源

所有以下行为均来自 [subagent-driven-development/SKILL.md](C:\Users\jianw\.claude\plugins\cache\claude-plugins-official\superpowers\6.1.0\skills\subagent-driven-development\SKILL.md)：

| 规则 | SKILL.md 原文 |
|------|--------------|
| Fresh subagent per task | "Execute plan by dispatching a fresh implementer subagent per task" |
| 预检 | "Pre-Flight Plan Review: scan the plan once for conflicts" |
| Model 选择 | "Mechanical implementation tasks → cheap model; Integration tasks → standard model; Architecture tasks → most capable model" |
| Task brief 提取 | "run this skill's `scripts/task-brief PLAN_FILE N` — it extracts the task's full text to a uniquely named file" |
| 四种状态处理 | "DONE / DONE_WITH_CONCERNS / NEEDS_CONTEXT / BLOCKED" |
| 两阶段 review | "task review (spec compliance + code quality) after each task" |
| Review package | "run `scripts/review-package BASE HEAD` and pass the reviewer the file path it prints" |
| Fix subagent | "Dispatch fix subagents for Critical and Important findings" |
| 进度账本 | "append one line to the ledger: `Task N: complete (commits <base7>..<head7>, review clean)`" |
| 连续执行 | "Continuous execution: Do not pause to check in with your human partner between tasks" |
| 不并行 | "Never dispatch multiple implementation subagents in parallel" |
| Final review | "dispatch a broad whole-branch review at the end" 使用 requesting-code-review 的 code-reviewer.md |

### 实时过程

```
Claude: [加载 subagent-driven-development skill]

        [预检: 扫描 plan，无冲突]

        [检查进度账本: .superpowers/sdd/progress.md]
        账本显示: 已有 9 个里程碑完成，19/19 tests passing。
        新任务从 Task 1 开始。

        ┌──── Task 1: Default WLTC Condition Points ─────────────────────┐
        │                                                                │
        │ [运行 scripts/task-brief plan.md 1 → 提取 Task 1 文本到文件]    │
        │                                                                │
        │ [派遣 implementer subagent]                                    │
        │  Model: cheap (机械任务: 加一个 constant property + 测试)        │
        │  输入: task-1-brief.md (需求) + 项目上下文 + report 文件路径    │
        │                                                                │
        │ Implementer: (无问题，直接开始)                                  │
        │   → 写了 testDefaultWLTCConditions (RED, FAIL)                  │
        │   → 加了 DEFAULT_WLTC_CONDITIONS 属性 (GREEN, PASS)            │
        │   → self-review: 无问题                                        │
        │   → 提交: commit abc1234                                       │
        │   状态: DONE                                                    │
        │                                                                │
        │ [运行 scripts/review-package abc1234 HEAD → diff 文件]          │
        │ [派遣 task reviewer subagent]                                  │
        │   → Spec ✅: 属性名/字段/默认值 全部匹配 spec                    │
        │   → Quality: Approved, 无 issues                               │
        │                                                                │
        │ [更新进度账本: Task 1 complete (abc1234..def5678, review clean)]│
        │                                                                │
        └────────────────────────────────────────────────────────────────┘

        ┌──── Task 2: scanMultipleConditions Method ─────────────────────┐
        │                                                                │
        │ [运行 scripts/task-brief plan.md 2 → 提取 Task 2 文本]         │
        │                                                                │
        │ [派遣 implementer subagent]                                    │
        │  Model: cheap (单个方法 + loop，spec 提供完整代码)               │
        │  输入: task-2-brief.md + "Consumes: DEFAULT_WLTC_CONDITIONS     │
        │        from Task 1, evaluate() existing"                       │
        │                                                                │
        │ Implementer:                                                    │
        │   → 写了 testScanMultipleConditions (RED, FAIL)                 │
        │   → 实现了 scanMultipleConditions() (GREEN, PASS)               │
        │   → self-review: 无问题                                        │
        │   → 提交: commit ghi9012                                       │
        │   状态: DONE                                                    │
        │                                                                │
        │ [运行 scripts/review-package def5678 ghi9012 → diff 文件]      │
        │ [派遣 task reviewer]                                           │
        │   → Spec ❌:                                                   │
        │     Missing: scanMultipleConditions 未处理空 conditions 输入     │
        │     (spec 要求 "返回空 struct array，不抛异常")                  │
        │   → Issues (Important): 缺少参数校验                            │
        │                                                                │
        │ [派遣 fix subagent 修复两个问题]                                │
        │ Fixer:                                                         │
        │   → 加了 arguments block 校验                                   │
        │   → 加了空输入 early return                                    │
        │   → 加了对应的 edge case test                                   │
        │   → 重新跑测试: 全部通过                                        │
        │   → 提交: commit jkl3456                                       │
        │                                                                │
        │ [重新 review]                                                   │
        │ Task reviewer: Spec ✅ — 包括空输入边界条件。Quality: Approved.  │
        │                                                                │
        │ [更新进度账本: Task 2 complete (def5678..jkl3456, review clean)]│
        │                                                                │
        └────────────────────────────────────────────────────────────────┘

        ┌──── Task 3: recommendBestMatch + Integration ──────────────────┐
        │  ... (同 Task 2 流程) ...                                      │
        │  状态: DONE, review clean                                      │
        └────────────────────────────────────────────────────────────────┘

        [全部 3 个 Task 完成]

        [Final whole-branch review]
        [运行 scripts/review-package MERGE_BASE HEAD → 全分支 diff]
        [派遣 final code reviewer subagent (最强大模型)]
        Final reviewer: 所有需求满足, 0 Critical, 0 Important, 2 Minor
        → Minor 1: scanMultipleConditions 的 for 循环可以 preallocate
        → Minor 2: 建议在类文档注释中加 usage example

        [Minor 记录到进度账本，不阻塞 merge]
```

### 这一步你看到了什么

1. **Fresh subagent per task**：每个任务派一个全新的子代理，不继承你的会话历史，只看到 task brief + 上下文
2. **Task brief 文件传递**：不是把 plan 粘贴到 prompt 里，而是用 `scripts/task-brief` 提取后作为文件路径传给子代理
3. **Model 分层**：加属性用 cheap model，加方法用 cheap model，final review 用最强 model
4. **两阶段 Review**：每个任务完成后 → spec compliance check（有没有遗漏需求）+ code quality check（代码质量）
5. **Review loop**：reviewer 发现问题 → fix subagent 修 → re-review → 通过才标记完成
6. **进度账本**：`.superpowers/sdd/progress.md` 记录每个 Task 的完成状态和 commit 范围——即使上下文被压缩丢失，账本 + git log 也能恢复进度
7. **连续执行**：任务之间不停下来问"要继续吗"
8. **Final review**：全部完成后，对整个分支做一次合并基差分的整体审查

---

## Round 4 — verification-before-completion：证据门

### 这是什么

`verification-before-completion` 不是一个"阶段"，而是一道**贯穿所有阶段的闸门**。每当 Claude 想说"做完了""通过了""没问题了"，这道闸门就会拦下它。

### 规则来源

所有以下行为均来自 [verification-before-completion/SKILL.md](C:\Users\jianw\.claude\plugins\cache\claude-plugins-official\superpowers\6.1.0\skills\verification-before-completion\SKILL.md)：

### 铁律

```
NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE
```

### Gate Function（闸门函数）

```
在声称任何状态之前：

1. IDENTIFY: 什么命令能证明这个声称？
2. RUN: 执行完整命令（新的、完整的运行）
3. READ: 读完整输出，检查退出码，数失败数
4. VERIFY: 输出确认了声称吗？
   - 如果没有 → 陈述实际状态 + 证据
   - 如果是 → 陈述声称 + 证据
5. ONLY THEN: 做出声称

跳过任何一步 = 撒谎，不是验证
```

### 在 SDD 流程中如何体现

```
每个 Task 的 implementer subagent 报告 "DONE" 时:
  → 不是说 "我写完了"
  → 而是说 "测试命令运行了，输出是: 5/5 PASS，退出码 0"

Task reviewer 报告 "Spec ✅" 时:
  → 不是说 "看起来符合 spec"
  → 而是逐条对照 spec 要求 + diff 内容，列出匹配/不匹配

Claude controller 标记 Task complete 时:
  → 不是说 "看起来好了"
  → 而是确认 review 的两个 verdict (spec + quality) 都返回了 Approved
```

### 红线速查

以下措辞一旦出现，说明验证门没触发：

| 危险措辞 | 应该换成 |
|---------|---------|
| "应该通过了" | 运行命令，贴输出 |
| "看起来没问题" | 运行命令，贴输出 |
| "Agent 说成功了" | 检查 VCS diff，独立验证 |
| "Great! Done!"（验证前） | 先验证，再说 Great |

---

## Round 5 — requesting-code-review：派遣 Reviewer

### 触发

SDD 流程中的 "final whole-branch review" 步骤自动触发。

### 规则来源

所有以下行为均来自 [requesting-code-review/SKILL.md](C:\Users\jianw\.claude\plugins\cache\claude-plugins-official\superpowers\6.1.0\skills\requesting-code-review\SKILL.md)：

### 不是"四维审查"，是 Reviewer 子代理

`requesting-code-review` 不让你在对话里"四维审查"。它的做法是：**派遣一个 `general-purpose` 子代理，填入 `code-reviewer.md` 模板**。

```
派遣参数:
  DESCRIPTION: "RangeExtenderController 多工况功率扫描 — 新增 3 个方法"
  PLAN_OR_REQUIREMENTS: "Task 1-3 from docs/superpowers/plans/2026-07-07-..."
  BASE_SHA: main (merge-base)
  HEAD_SHA: HEAD (当前分支最新 commit)

Reviewer (子代理返回):
  Strengths: 接口设计干净, 测试覆盖全面, 完全向后兼容

  Issues:
    Critical: (无)
    Important: (无)
    Minor:
      - scanMultipleConditions 的 for 循环用到了 struct 动态字段扩展，
        大数据量下建议 preallocate
      - 类文档注释中建议加 usage example

  Assessment: Ready to merge
```

### 处理反馈

```
Critical   → 立即修复，修复后才能继续
Important  → 在进入下一步前修复
Minor      → 记录，后续处理。在 SDD 中，Minor 记录到进度账本，
              final whole-branch review 时统一评估
```

---

## Round 6 — finishing-a-development-branch：完成与合并

### 触发

全部 Task 完成 + final review 通过后，自动触发。

### 规则来源

所有以下行为均来自 [finishing-a-development-branch/SKILL.md](C:\Users\jianw\.claude\plugins\cache\claude-plugins-official\superpowers\6.1.0\skills\finishing-a-development-branch\SKILL.md)：

### 6 步流程

```
Step 1: 验证测试全部通过 (必须先做 — "If tests fail: Stop. Don't proceed.")
Step 2: 检测环境 (normal repo / worktree / detached HEAD)
Step 3: 确定 base branch
Step 4: 呈现选项

普通分支 — 4 个选项:
  1. Merge back to main 本地合并
  2. Push and create a Pull Request
  3. Keep the branch as-is (先留着)
  4. Discard this work (丢弃)

Detached HEAD — 3 个选项:
  1. Push as new branch and create PR
  2. Keep as-is
  3. Discard

Step 5: 执行用户选择
Step 6: 清理 (仅 Option 1 & 4 — Option 2 保留 worktree 给 PR 迭代)
```

### 实时对话

```
Claude: [加载 finishing-a-development-branch skill]

        I'm using the finishing-a-development-branch skill to complete this work.

        [Step 1: 运行测试]
        $ matlab -batch "runtests('tests')"
        ✅ All 23 tests passed (19 original + 4 new)

        [Step 2: 检测环境]
        GIT_DIR == GIT_COMMON → 普通仓库

        [Step 3: base branch = main]

        [Step 4: 呈现选项]
        实现完成，所有测试通过。你想怎么做？

        1. 本地合并到 main
        2. Push 并创建 Pull Request
        3. 保留分支不动（你后续处理）
        4. 丢弃本次工作

        选哪个？

你: 2 — 创建 PR

Claude: [git push -u origin feature/range-extender-power-scan]
        Branch pushed. PR 已创建。
        (Worktree 保留以便 PR 迭代。)
```

---

## 跨领域 Skill：贯穿全流程的行为约束

以下三个 Skill 不是"阶段"，而是**作用于每个阶段的横切约束**。

### test-driven-development (TDD)

**规则**：[test-driven-development/SKILL.md](C:\Users\jianw\.claude\plugins\cache\claude-plugins-official\superpowers\6.1.0\skills\test-driven-development\SKILL.md)

**铁律**：
```
NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST
```

**如果先写了代码再写测试？** 删掉代码。重新来。

| 借口 | 现实 |
|------|------|
| "留着当参考" | 删掉。你会"参考"着把它改回去。 |
| "代码写了 X 小时删了可惜" | 沉没成本谬误。不可信代码 = 技术债。 |
| "这个太简单不需要 TDD" | 简单代码也会坏。30 秒写个测试。 |

**Red-Green-Refactor 循环**：
```
RED   → 写一个失败的测试
GREEN → 写最少代码让测试通过
      → 确认测试通过
      → 确认其他测试没挂
REFACTOR → 清理重复、改进命名（不改行为）
      → 保持绿色
```

**在 SDD 中**：每个 Task 的 implementer subagent 被要求使用 TDD。Plan 中的每个任务本身就按 TDD 步骤编写（Step 1: 写测试 → Step 2: 验证失败 → Step 3: 实现 → Step 4: 验证通过 → Step 5: 提交）。

### systematic-debugging

**规则**：[systematic-debugging/SKILL.md](C:\Users\jianw\.claude\plugins\cache\claude-plugins-official\superpowers\6.1.0\skills\systematic-debugging\SKILL.md)

**铁律**：
```
NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST
```

**四阶段**：

| 阶段 | 做什么 | 成功标准 |
|------|--------|---------|
| **Phase 1: Root Cause** | 读错误、复现、检查最近改动、搜集证据 | 理解 WHAT 和 WHY |
| **Phase 2: Pattern** | 找能正常工作的相似代码、对比差异 | 识别差异点 |
| **Phase 3: Hypothesis** | 单一假设、最小测试 | 确认或形成新假设 |
| **Phase 4: Implementation** | 创建失败测试 → 修 → 验证 | Bug 解决，测试通过 |

**如果 3 次修复都失败**：停止修，质疑架构。
```
不是你的假设不对 —— 是架构层面有问题。
和用户讨论是否重构，而不是继续往上堆修复。
```

**SDD 中的体现**：当 implementer 返回 `BLOCKED` 或 reviewer 发现重复问题时，controller 不会"再试一次"，而是走 Phase 2-3 的诊断流程。

### 红线速查（来自 systematic-debugging SKILL.md）

如果发现自己这么想，停下来回到 Phase 1：
- "先快速修一下，后面再查"
- "试试改 X 看看效果"
- "多加几个改动一起跑"
- "跳过测试，手动验证一下"
- "应该就是 X 的问题，直接修"

---

## 完整 Skill 链路总图

```
你说的话                        Skill                          产出
──────────                     ────────                       ────
"我想加新功能"                  brainstorming                  spec 文档
                                  ↓
"spec 没问题，继续"             writing-plans                  plan 文档
                                  ↓
"选 SDD 执行"                  subagent-driven-development   代码 (逐 task)
                                  │
                                  ├─→ 每个 Task: TDD (red-green-refactor)
                                  ├─→ 每个 Task 后: 两阶段 review
                                  ├─→ review 有问题: fix subagent → re-review
                                  └─→ 进度账本: .superpowers/sdd/progress.md
                                  ↓
(全部 Task 完成后)              requesting-code-review        审查报告
                                  ↓
"创建 PR"                      finishing-a-development-branch PR / Merge

横向贯穿全程:
  verification-before-completion ─→ 每次声称之前：运行 → 读输出 → 再声称
  tdd                            ─→ 每个 Task: RED → GREEN → REFACTOR
  systematic-debugging           ─→ 任何 bug: Phase 1 根因 → Phase 2 模式 → Phase 3 假设 → Phase 4 修复

总耗时: ~20-30 分钟 (取决于 Task 数量和复杂度)
你写的代码: 0 行
你做的决策: 3-5 次多选 + 2 次 "继续/选择"
```

---

## Skill 选用速查表

此表基于各 Skill 的 `description` 和 `When to Use` 章节：

| 场景 / 你说的话 | 自动选用的 Skill | 触发依据 |
|----------------|-----------------|---------|
| "我想加一个功能 / 改一个行为 / 创建新项目" | `brainstorming` | 任何 creative work — "creating features, building components, adding functionality, or modifying behavior" |
| "设计确认了，写 plan / 继续" | `writing-plans` | brainstorming 终态 = writing-plans |
| "按 SDD 执行 plan" | `subagent-driven-development` | "when executing implementation plans with independent tasks in the current session" |
| "在当前会话内按步执行 plan" | `executing-plans` | "when you have a written implementation plan to execute in a separate session with review checkpoints" |
| (任何声称成功/完成之前) | `verification-before-completion` | 铁律："NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE" |
| (每个实现步骤中) | `test-driven-development` | 铁律："NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST" |
| "报错了 / 测试挂了 / 行为不对" | `systematic-debugging` | "when encountering any bug, test failure, or unexpected behavior, before proposing fixes" |
| "帮我审查这些改动" | `requesting-code-review` | "when completing tasks, implementing major features, or before merging" |
| "全部做完了，怎么合并" | `finishing-a-development-branch` | "when implementation is complete, all tests pass, and you need to decide how to integrate" |

---

## 三个最重要的原则

### 1. 描述意图，不描述操作

```
❌ "帮我写一个 RangeExtenderController.m 文件，里面加 scanMultipleConditions 方法"
   → Claude 可能直接写代码，跳过了设计

✅ "我想给 RangeExtenderController 增加多工况功率扫描功能"
   → Claude 判断这是 "adding functionality" → 触发 brainstorming
```

### 2. 信任流程，不跳步

```
brainstorming → writing-plans → SDD/executing-plans → code-review → finish

每一步都有铁律保护。跳过 brainstorming 直接写代码 =
省了 5 分钟设计，可能浪费 2 小时返工。

跳过 TDD 直接写实现 =
测试永远不会失败，你不知道它测的是不是对的。
```

### 3. 让 Skill 自动接力，不手动切换

```
不要说: "现在切换到 writing-plans skill"
而是说: "设计没问题，继续"
→ Claude 根据当前状态自动判断该加载哪个 Skill

(brainstorming SKILL.md 明确规定终态是 writing-plans,
 不需要用户手动指定)
```

### 4. Skill 是约束，不是建议

```
每个 Skill 都有:
  - Iron Law (铁律): 不可违反
  - Red Flags (红线): 触发时必须停止
  - Rationalization Prevention (借口预防表): 针对"就这一次"的消解

如果你发现 Claude 跳过了某个步骤 → 直接指出:
"brainstorming 的 HARD-GATE 说设计批准前不能写代码"
"TDD 的铁律说没有失败测试不能写实现代码"
```

---

## 延伸阅读

- 各 Skill 完整规则：`C:\Users\jianw\.claude\plugins\cache\claude-plugins-official\superpowers\6.1.0\skills\`
- DHT 项目 SDD 进度账本：`.superpowers/sdd/progress.md`
- DHT 项目 Spec 目录：`docs/superpowers/specs/`
- DHT 项目 Plan 目录：`docs/superpowers/plans/`
