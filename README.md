# TRIZ Innovation Toolkit 🚀 / TRIZ 创新工具箱

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
[![Chapters](https://img.shields.io/badge/Chapters-24-blue)](./chapters/)
[![Tools](https://img.shields.io/badge/TRIZ%20Tools-22-orange)](#whats-inside--内容概览)
[![Platform](https://img.shields.io/badge/Platform-Claude%20Code%20%7C%20Copilot%20CLI%20%7C%20Amp-green)]()

> **A comprehensive TRIZ systematic innovation skill for AI coding agents — 24 chapters, 22 tools, synthesized from 8 authoritative sources.**
>
> **面向 AI 编程助手的 TRIZ 系统创新技能包 — 24 章、22 种工具，源自 8 本权威著作。**

---

## What is TRIZ? / 什么是 TRIZ？

**TRIZ** (Teoriya Resheniya Izobretatelskikh Zadach / 发明问题解决理论) is the "science of inventiveness" — a systematic methodology for solving engineering and business problems by leveraging patterns extracted from millions of patents. Developed by Genrich Altshuller starting in 1946, TRIZ replaces trial-and-error with principled problem-solving.

**TRIZ** 是"发明问题解决理论"——一种通过分析数百万专利中提取的创新模式，系统化解决工程和商业问题的方法论。由 Genrich Altshuller 于 1946 年创建，TRIZ 用原则驱动的问题解决方式取代了试错法。

**Ideality = Σ Benefits / (Σ Costs + Σ Harms)**

**The North Star of TRIZ**: maximize useful functions while driving costs and harms toward zero.

**TRIZ 的北极星指标**：最大化有用功能，同时将成本和危害趋近于零。

---

## What's Inside / 内容概览

| File / 文件 | Purpose / 用途 | Lines |
|-------------|---------------|-------|
| [`SKILL.md`](./SKILL.md) | Entry point — YAML frontmatter, problem routing, tool selector, chapter index | 338 |
| [`cheatsheet.md`](./cheatsheet.md) | Quick-reference: 39 parameters, top contradictions, routing flowchart, checklists | 349 |
| [`patterns.md`](./patterns.md) | Full pattern catalog: 40 Principles, 8 Trends, 76 Standards, ARIZ, AFI | 251 |
| [`glossary.md`](./glossary.md) | A-Z term definitions from all 8 source books | 197 |
| [`chapters/`](./chapters/) | **24 deep-dive chapter summaries** (see full map below) | ~2,100 |

### Chapter Map / 章节地图

| # | Chapter / 章节 | Core Tool / 核心工具 |
|---|---------------|---------------------|
| 01 | Zero to TRIZ | Overview & learning roadmap |
| 02 | TRIZ Philosophy | Ideality, Contradictions, System Operator |
| 03 | 40 Principles | Contradiction Matrix + Inventive Principles |
| 04 | Trends of Evolution | 8 Trends, S-Curve Analysis |
| 05 | Ideality & Resources | Ideality equation, 7 resource types |
| 06 | Effects Database | Physical/chemical/geometric effects |
| 07 | Psychological Inertia | SLP, DTC, Size-Time-Cost thinking tools |
| 08 | Time and Scale | 9-Windows, System Operator |
| 09 | Ideal Final Result | IFR formulation, X-Element |
| 10 | Group Creativity | Brainstorming, Synectics, facilitation |
| 11 | Problem Solving Process | Problem definition, root cause analysis |
| 12 | Function Analysis | Component analysis, interaction matrix |
| 13 | Standard Solutions | 76 Standards (Classical + Oxford) |
| 14 | Trimming | Component elimination, function transfer |
| 15 | Ten Pitfalls | Common TRIZ mistakes & how to avoid |
| 16 | Ten Tips | Practical application advice |
| 17 | ARIZ | 5-step algorithm for hard problems |
| 18 | AFI | Anticipatory Failure Identification (4-step) |
| 19 | TRIZ for Business | 12 Double Business Principles |
| 20 | Innovation Process | 10-step strategic-to-execution pipeline |
| 21 | Customer Benefit | I-S Matrix, customer value analysis |
| 22 | Implementation | 5-stage pipeline, prototype ladder |
| 23 | CAI | Computer-Aided Innovation tools |
| 24 | Corporate Training | MATRIZ 5-level competency model |

**80/20 Rule / 二八法则**: 5 core tools — Contradiction Matrix, Separation Principles, Function Analysis + Trimming, IFR, and AFI — solve ~80% of engineering problems.

---

## Quick Start / 快速开始

### Install as Claude Code Skill

```bash
# Clone the repository
git clone https://github.com/fanfanbox/triz-innovation-toolkit.git

# Copy to Claude Code skills directory
cp -r triz-innovation-toolkit ~/.claude/skills/triz/

# The skill auto-registers — invoke with:
# "Use the TRIZ skill to solve: <your problem>"
```

### Install as GitHub Copilot CLI Skill

```bash
# Clone and place in Copilot skills
git clone https://github.com/fanfanbox/triz-innovation-toolkit.git
cp -r triz-innovation-toolkit ~/.copilot/skills/triz/

# Or for project-level use:
# cp -r triz-innovation-toolkit .github/skills/triz/
```

### Install as Amp Agent Skill

```bash
# Clone and place in Amp skills
git clone https://github.com/fanfanbox/triz-innovation-toolkit.git
cp -r triz-innovation-toolkit ~/.agents/skills/triz/
```

---

## Usage Examples / 使用示例

### Example 1: Engineering Trade-off / 工程权衡

> **Problem**: "My electric motor needs thinner laminations to reduce eddy current loss, but thinner laminations reduce mechanical strength."

**Route**: Technical Contradiction → Contradiction Matrix → Principles 1 (Segmentation), 15 (Dynamicity), 40 (Composite Materials)

**Outcome**: Stack thin laminations bonded with high-strength epoxy — segmentation at micro scale preserves both electrical and mechanical properties.

### Example 2: System Simplification / 系统简化

> **Problem**: "Our gearbox has 47 components and the assembly cost is killing margins."

**Route**: System too complex → Function Analysis → Trimming (Ch14)

**Outcome**: Identify components performing auxiliary functions. Transfer their useful functions to remaining components. Eliminate 12 parts without losing any functionality.

### Example 3: Before Design Freeze / 设计冻结前

> **Problem**: "We're about to freeze the battery pack design. What could go wrong?"

**Route**: Before launch → AFI (Ch18) — Invert → Amplify → Generate → Fix

**Outcome**: Deliberately imagine 15 failure modes. Apply TRIZ tools to prevent each. Catch 3 critical thermal runaway scenarios before they become recall triggers.

---

## Source Attribution / 来源声明

This skill synthesizes concepts from the following authoritative works. It is a **transformative educational synthesis** — a study guide, not a reproduction. Users should consult the original works for complete content.

本技能综合了以下权威著作的概念。这是一份**转化性教育综合**——学习指南，而非复制品。使用者应查阅原著获取完整内容。

| # | Title / 书名 | Author / 作者 | Language |
|---|-------------|--------------|----------|
| 1 | *TRIZ For Dummies* | Lilly Haines-Gadd | EN |
| 2 | *TRIZ for Engineers: Enabling Inventive Problem Solving* | Karen Gadd | EN |
| 3 | *TRIZ Handbook* | Dr. Pavel Livotov | EN |
| 4 | *TRIZ POWER TOOLS* | Larry Ball | EN |
| 5 | *TRIZ 打开创新之门的金钥匙 I* | 孙永伟 (Sun Yongwei) | ZH |
| 6 | *TRIZ 打开创新之门的金钥匙 II* | 孙永伟 (Sun Yongwei) | ZH |
| 7 | *TRIZ 推动创新的技术* | 布柯曼 (Bukhman) | ZH |
| 8 | *创新算法：TRIZ、系统创新和技术创造力* | 阿奇舒勒 (Altshuller) | ZH |

---

## License / 许可证

This work is licensed under **CC BY-NC-SA 4.0** (Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International).

See [LICENSE](./LICENSE) for the full legal text.

**In short / 简言之**:
- ✅ **Share** — copy and redistribute in any medium or format
- ✅ **Adapt** — remix, transform, and build upon the material
- ❌ **Commercial Use** — no commercial use without permission
- 🔗 **Attribution** — you must give appropriate credit
- 🔗 **ShareAlike** — derivatives must use the same license

---

## Contributing / 贡献

Contributions are welcome! See [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.

**Scope of contributions / 贡献范围**:
- Corrections to concepts, terminology, or translations / 概念、术语或翻译修正
- Additional worked examples for existing chapters / 为现有章节补充实例
- New TRIZ tools or frameworks not yet covered / 尚未涵盖的新 TRIZ 工具
- Better explanations or clearer formulations / 更清晰的解释或表述

**Not in scope / 不在范围内**: Reproducing more text from the copyrighted source books / 不得复制受版权保护的源书籍内容。

---

## Star History / 星标历史

If you find this toolkit useful, please ⭐ star this repo — it helps others discover TRIZ!

如果这个工具箱对你有用，请 ⭐ 点亮星标——帮助更多人发现 TRIZ！

---

*Synthesized with care from 8 authoritative sources spanning Chinese and English TRIZ literature. May the Ideality be with you. 🚀*
