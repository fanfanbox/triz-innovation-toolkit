---
name: TrizInv
description: >
  TRIZ systematic innovation toolkit — 24 chapters covering all classical and modern TRIZ tools:
  40 Inventive Principles, Contradiction Matrix (39×39), Physical Contradictions, 8 Trends of Technical
  Evolution, Ideality Equation, Ideal Final Result (IFR), Function Analysis, Su-Field Analysis, 76 Standard
  Solutions (Classical + Oxford), ARIZ 5-Step Algorithm, AFI (Anticipatory Failure Identification), 12
  Business TRIZ Double Principles, Effects Database, Psychological Inertia Tools (SLP, DTC,
  Size-Time-Cost), 9-Windows, Trimming, S-Curve Analysis, 10-Step Innovation Process, Customer Benefit
  Analysis (I-S Matrix), Implementation Methodology (5-Stage Pipeline), Computer-Aided Innovation (CAI),
  and Corporate TRIZ Training (MATRIZ 5-Level Competency Model). Includes full glossary, patterns
  reference, and quick-reference cheatsheet. Route any engineering or business problem to the right
  TRIZ tool. Synthesized from 8 authoritative sources.
---

# TRIZ Skill — Systematic Innovation & Inventive Problem Solving

Comprehensive TRIZ toolkit synthesized from 8 authoritative sources:
- *TRIZ For Dummies* (Haines-Gadd, 2016) — 93K words, complete beginner-to-intermediate
- *TRIZ Handbook* (Livotov & Petrov) — 284 pages, AFI, Business TRIZ, CAI, innovation process
- *TRIZ POWER TOOLS: Job #6 Implementing* (Ball) — concept refinement, prototyping, patents, commercialization
- *TRIZ for Engineers* (Gadd) — Oxford Standard Solutions, ARIZ with coal pipe example
- *金钥匙Ⅰ & 金钥匙2* (Sun Yongwei, Chinese) — classical TRIZ from Chinese perspective
- *创新算法* (Altshuller, Chinese translation) — original ARIZ source material
- *推动创新的技术* (Bukhman, Chinese translation) — technology-driven innovation

## Skill File Structure

| File | Purpose | When to Read |
|------|---------|-------------|
| `SKILL.md` (this file) | Problem routing, tool selection, conceptual overview | First — find the right tool for your problem |
| `chapters/ch01-*.md` through `ch24-*.md` | Deep-dive chapter summaries with frameworks, mental models, anti-patterns, worked examples | When you need the full detail on a specific tool |
| `cheatsheet.md` | Quick-reference tables: 39 Parameters, top contradictions, routing flowchart, tool selector, ARIZ steps, AFI checklist, I-S Matrix, Business Principles, MATRIZ levels | During problem-solving — fast lookups without reading full chapters |
| `patterns.md` | Complete pattern catalog: 40 Principles (detailed), 8 Trends (stage strategies), 76 Standards (5 classes), ARIZ 5-Step, AFI 4-Step, 12 Double Business Principles, 5 Thinking Components, 10-Step Innovation Process, Implementation Pipeline, CAI Categories, MATRIZ Levels, TRIZ Maturity Model | When applying a specific pattern and need sub-steps, stage details, or implementation guidance |
| `glossary.md` | A-Z definitions of every TRIZ term from all 8 source books, with chapter cross-references | When encountering an unfamiliar term or verifying precise definitions |
| `report/` | Generated TRIZ analysis reports (Markdown) + auto-generated design PPTs (via NotebookLM) | After completing a TRIZ analysis — reports and slide decks are saved here |

## When to Use This Skill

Invoke this skill when the user faces:

- **Engineering contradictions**: "I want X better but Y gets worse"
- **Physical contradictions**: "I need this to be both big AND small"
- **Product innovation / next-generation design**: "What should our next product look like?"
- **Cost reduction / simplification**: "How can we make this cheaper without losing function?"
- **Stuck on a hard problem**: "We've tried everything and nothing works"
- **Patent strategy**: "How do we protect our invention roadmap?"
- **System optimization**: "Where should we focus improvement efforts?"
- **Creative block**: "We can't think of any new approaches"
- **Failure prediction**: "What could go wrong with this design?" → AFI (Ch18)
- **Business innovation**: "How do we innovate our business model?" → TRIZ for Business (Ch19)
- **R&D process design**: "How do we structure our innovation pipeline?" → Innovation Process (Ch20)
- **Implementing a solution**: "How do we prototype, patent, and commercialize?" → Implementation (Ch22)

## PROBLEM ROUTING — Which TRIZ Tool to Use First

Answer these diagnostic questions in order. The first "yes" tells you where to start:

### 1. Is the problem clearly defined?

| Situation | Tool | Go To |
|-----------|------|-------|
| NO — messy, unclear what's wrong | Function Analysis | [Ch12](chapters/ch12-function-analysis.md) |
| YES — specific technical conflict known | Contradiction Analysis | → Question 2 |
| YES — but need to define ideal outcome first | Ideal Final Result (IFR) | [Ch09](chapters/ch09-ideal-final-result.md) |

### 2. What type of contradiction is it?

| Contradiction Type | Definition | Resolution Tool |
|-------------------|------------|-----------------|
| **Technical Contradiction** | Improving parameter A worsens parameter B | Contradiction Matrix → 40 Principles |
| **Physical Contradiction** | One parameter must be in two opposite states | Separation Principles (Time/Space/Condition/System) |
| **Either/both** | Start here for diagnosis | [Ch03](chapters/ch03-40-principles.md) |

### 3. Do you need to predict future technology?

| Need | Tool |
|------|------|
| Predict next-generation product | Trends of Technical Evolution |
| Understand where your system is on S-Curve | S-Curve Analysis |
| Patent strategy / IP roadmap | Trends + Ideality |
| → Go to | [Ch04](chapters/ch04-trends-evolution.md) |

### 4. Are you trying to reduce cost or simplify?

| Need | Tool |
|------|------|
| Eliminate components without losing function | Trimming |
| → Go to | [Ch14](chapters/ch14-trimming.md) |

### 5. Are you stuck creatively?

| Need | Tool |
|------|------|
| Breaking mental blocks | Psychological Inertia tools (SLP, DTC, Size-Time-Cost) |
| Thinking across time/scale dimensions | 9-Windows |
| → Go to | [Ch07](chapters/ch07-psychological-inertia.md), [Ch08](chapters/ch08-time-and-scale.md) |

### 6. Is it a substance-field interaction problem?

| Need | Tool |
|------|------|
| Model interactions between substances and fields | Su-Field Analysis |
| Apply proven solution patterns | 76 Standard Solutions (Classical + Oxford) |
| → Go to | [Ch13](chapters/ch13-standard-solutions.md) |

### 7. Need to find HOW to achieve a specific function?

| Need | Tool |
|------|------|
| Find physical/chemical/geometric effects that deliver a function | Effects Database |
| → Go to | [Ch06](chapters/ch06-effects-database.md) |

### 8. Is this a very hard, ambiguous problem where nothing else works?

| Need | Tool |
|------|------|
| Step-by-step algorithmic solution finding | ARIZ (Algorithm of Inventive Problem Solving) |
| → Go to | [Ch17](chapters/ch17-ariz.md) |

### 9. Do you need to predict/prevent failures?

| Need | Tool |
|------|------|
| Identify what could go wrong BEFORE it happens | AFI (Anticipatory Failure Identification) |
| → Go to | [Ch18](chapters/ch18-afi.md) |

### 10. Is this a business or management problem?

| Need | Tool |
|------|------|
| Business model innovation | TRIZ for Business (12 double principles) |
| Customer needs analysis | Customer Benefit Analysis |
| R&D pipeline design | Innovation Process Management |
| → Go to | [Ch19](chapters/ch19-triz-for-business.md), [Ch20](chapters/ch20-innovation-process.md), [Ch21](chapters/ch21-customer-benefit.md) |

### 11. Are you ready to implement a solution?

| Need | Tool |
|------|------|
| Refine concepts, prototype, patent, commercialize | Implementation Methodology |
| → Go to | [Ch22](chapters/ch22-implementation.md) |

## TRIZ Problem-Solving Process (Full Flow)

For complex, multi-faceted problems, follow the complete process:

```
1. Problem Definition     → Function Analysis, IFR, Customer Benefit Analysis
2. Problem Solving        → Contradictions, Standard Solutions, Effects, ARIZ
3. Solution Generation    → 40 Principles, Trends, Trimming, Separation Principles
4. Failure Prevention     → AFI (find what could go wrong)
5. Solution Evaluation    → Ideality Equation, S-Curve, PUGH Matrix
6. Implementation         → Prototyping, Patenting, Commercialization
```

See [Ch11](chapters/ch11-problem-solving-process.md) for the core process, [Ch20](chapters/ch20-innovation-process.md) for the 10-step innovation management framework, and [Ch22](chapters/ch22-implementation.md) for implementation methodology.

## Business Innovation Process (from Livotov)

For business and management innovation:

```
STRATEGIC PHASE (5 steps):
1. Situation Analysis     → Market, competition, technology trends
2. Strategic Diagnosis     → Identify innovation bottlenecks
3. Innovation Goals        → Define target parameters
4. Strategy Development    → Select TRIZ tools for each goal
5. Strategic Controlling   → KPIs, feedback loops

EXECUTION PHASE (5 steps):
6. Idea Generation         → TRIZ tools applied systematically
7. Idea Evaluation         → Multi-criteria assessment
8. Concept Development     → Detailed solution design
9. Implementation          → Prototyping, testing, launch
10. Innovation Controlling → Post-launch performance tracking
```

See [Ch20](chapters/ch20-innovation-process.md) for full details.

## Core TRIZ Equation

**Ideality = Σ Benefits / (Σ Costs + Σ Harms)**

Every TRIZ tool aims to increase Ideality — either by increasing benefits or reducing costs and harms. This is the North Star of all TRIZ work. See [Ch05](chapters/ch05-ideality-resources.md).

## AFI Core Formula (from Livotov)

**AFI Process:** Invert Task → Exaggerate Faults → Generate Faults with TRIZ Tools → Re-invert & Find Fixes

Turn "How to make this safe?" into "How to make this fail catastrophically?" — then invert the found failure modes into design fixes. See [Ch18](chapters/ch18-afi.md).

## Quick Tool Selector

| I want to... | Use this tool | Chapter |
|-------------|---------------|---------|
| Solve a known trade-off | Contradiction Matrix + 40 Principles | [Ch03](chapters/ch03-40-principles.md) |
| See the future of my product | 8 Trends of Technical Evolution | [Ch04](chapters/ch04-trends-evolution.md) |
| Make my product cheaper/better | Trimming + Ideality | [Ch05](chapters/ch05-ideality-resources.md), [Ch14](chapters/ch14-trimming.md) |
| Find a physical effect to solve this | Effects Database | [Ch06](chapters/ch06-effects-database.md) |
| Break out of rigid thinking | SLP, DTC, Size-Time-Cost, 9-Windows | [Ch07](chapters/ch07-psychological-inertia.md), [Ch08](chapters/ch08-time-and-scale.md) |
| Define the perfect solution | Ideal Final Result (IFR) | [Ch09](chapters/ch09-ideal-final-result.md) |
| Run a TRIZ workshop with a team | Group creativity process | [Ch10](chapters/ch10-group-creativity.md) |
| Map out what's wrong with my system | Function Analysis | [Ch12](chapters/ch12-function-analysis.md) |
| Fix a Su-Field interaction problem | 76 Standard Solutions | [Ch13](chapters/ch13-standard-solutions.md) |
| Solve an ultra-hard, ambiguous problem | ARIZ (26-step algorithm) | [Ch17](chapters/ch17-ariz.md) |
| Predict and prevent design failures | AFI (Anticipatory Failure Identification) | [Ch18](chapters/ch18-afi.md) |
| Innovate a business model | 12 Business TRIZ Double Principles | [Ch19](chapters/ch19-triz-for-business.md) |
| Design an R&D innovation pipeline | 10-Step Innovation Process | [Ch20](chapters/ch20-innovation-process.md) |
| Analyze customer needs systematically | Customer Benefit Analysis (I-S Matrix) | [Ch21](chapters/ch21-customer-benefit.md) |
| Prototype, patent, and commercialize | Implementation Methodology (5-Stage Pipeline) | [Ch22](chapters/ch22-implementation.md) |
| Use software to assist innovation | CAI (Computer-Aided Innovation) | [Ch23](chapters/ch23-cai.md) |
| Set up corporate TRIZ training | MATRIZ 5-Level Training Program | [Ch24](chapters/ch24-corporate-training.md) |
| Understand TRIZ philosophy | TRIZ thinking pillars | [Ch02](chapters/ch02-triz-philosophy.md) |
| Get started as a beginner | First steps + common mistakes | [Ch01](chapters/ch01-zero-to-triz.md), [Ch15](chapters/ch15-ten-pitfalls.md), [Ch16](chapters/ch16-ten-tips.md) |

## Reference Materials

- **40 Inventive Principles** — full listing with examples and sub-principles: see [patterns.md](patterns.md)
- **Contradiction Matrix** — 39×39 parameter lookup: see [cheatsheet.md](cheatsheet.md)
- **Separation Principles** — Time/Space/Condition/System mapping with physical contradiction quick-map: see [cheatsheet.md](cheatsheet.md)
- **76 Standard Solutions** — Classical (5 Su-Field classes) + Oxford (3 categories): see [patterns.md](patterns.md)
- **8 Trends of Technical Evolution** — full stage strategies and S-Curve positioning: see [patterns.md](patterns.md)
- **ARIZ Algorithm** — complete 5-step ARIZ process (Mini-Problem, Contradiction, Resources & ZoF, Solution Search, Refinement): see [patterns.md](patterns.md) and [Ch17](chapters/ch17-ariz.md)
- **AFI Methodology** — 4-step failure prediction checklist (Invert, Exaggerate, Generate, Re-invert & Fix): see [patterns.md](patterns.md), [cheatsheet.md](cheatsheet.md), and [Ch18](chapters/ch18-afi.md)
- **12 Business TRIZ Double Principles** — for business model innovation with anti-principles: see [patterns.md](patterns.md) and [cheatsheet.md](cheatsheet.md)
- **Customer Benefit Analysis** — I-S Matrix with 4 zones (Sweet Spot, Parity, Overshoot, Irrelevance): see [cheatsheet.md](cheatsheet.md) and [Ch21](chapters/ch21-customer-benefit.md)
- **10-Step Innovation Process** — strategic (Steps 1-5) + execution (Steps 6-10) framework: see [cheatsheet.md](cheatsheet.md) and [Ch20](chapters/ch20-innovation-process.md)
- **Implementation Pipeline** — 5 stages + 5-level prototype escalation: see [patterns.md](patterns.md), [cheatsheet.md](cheatsheet.md), and [Ch22](chapters/ch22-implementation.md)
- **CAI (Computer-Aided Innovation)** — 7 tool categories + Function-Oriented Search: see [patterns.md](patterns.md) and [Ch23](chapters/ch23-cai.md)
- **MATRIZ 5-Level Competency Model** — Foundation through Master certification paths: see [patterns.md](patterns.md), [cheatsheet.md](cheatsheet.md), and [Ch24](chapters/ch24-corporate-training.md)
- **TRIZ Glossary** — A-Z definitions of all terms, all 8 source books: see [glossary.md](glossary.md)

## Chapter Index

### Part I: Foundations
| # | Chapter | Slug | Core Tool |
|---|---------|------|-----------|
| 1 | Going from Zero to TRIZ | [ch01-zero-to-triz.md](chapters/ch01-zero-to-triz.md) | TRIZ overview, history, levels of invention |
| 2 | Understanding the Fundamental TRIZ Philosophy | [ch02-triz-philosophy.md](chapters/ch02-triz-philosophy.md) | 5 pillars of TRIZ thinking |

### Part II: Core Contradiction Tools
| # | Chapter | Slug | Core Tool |
|---|---------|------|-----------|
| 3 | Solving Contradictions with the 40 Inventive Principles | [ch03-40-principles.md](chapters/ch03-40-principles.md) | Contradiction Matrix, 40 Principles, Separation Principles |
| 4 | Applying the Trends of Technical Evolution | [ch04-trends-evolution.md](chapters/ch04-trends-evolution.md) | 8 Trends, S-Curve, evolution prediction |
| 5 | Improving Ideality by Using Resources | [ch05-ideality-resources.md](chapters/ch05-ideality-resources.md) | Ideality equation, 6 resource types |

### Part III: Knowledge & Thinking Tools
| # | Chapter | Slug | Core Tool |
|---|---------|------|-----------|
| 6 | Using the TRIZ Effects Database | [ch06-effects-database.md](chapters/ch06-effects-database.md) | Scientific effects lookup by function |
| 7 | Breaking Psychological Inertia | [ch07-psychological-inertia.md](chapters/ch07-psychological-inertia.md) | SLP, DTC Operator, Size-Time-Cost |
| 8 | Thinking in Time and Scale | [ch08-time-and-scale.md](chapters/ch08-time-and-scale.md) | 9-Windows, system operator |

### Part IV: Advanced Problem Solving
| # | Chapter | Slug | Core Tool |
|---|---------|------|-----------|
| 9 | Living in Utopia (then Coming Back to Reality) | [ch09-ideal-final-result.md](chapters/ch09-ideal-final-result.md) | IFR, ideality visioning |
| 10 | Problem Solving and Being Creative with Others | [ch10-group-creativity.md](chapters/ch10-group-creativity.md) | Group TRIZ facilitation, Bad Solution Park |
| 11 | Applying the TRIZ Problem-Solving Process | [ch11-problem-solving-process.md](chapters/ch11-problem-solving-process.md) | 5-step process flow |
| 12 | Getting to Grips with Function Analysis | [ch12-function-analysis.md](chapters/ch12-function-analysis.md) | Component, interaction, function modeling |
| 13 | Solving Problems with Standard Solutions | [ch13-standard-solutions.md](chapters/ch13-standard-solutions.md) | Su-Field, 76 Standards (Classical + Oxford) |

### Part V: System Optimization
| # | Chapter | Slug | Core Tool |
|---|---------|------|-----------|
| 14 | Trimming for Elegant, Low-Cost Solutions | [ch14-trimming.md](chapters/ch14-trimming.md) | Systematic component elimination |

### Part VI: Algorithmic Methods for Hardest Problems
| # | Chapter | Slug | Core Tool |
|---|---------|------|-----------|
| 17 | ARIZ — Algorithm of Inventive Problem Solving | [ch17-ariz.md](chapters/ch17-ariz.md) | 26-step algorithm, coal pipe example |
| 18 | AFI — Anticipatory Failure Identification | [ch18-afi.md](chapters/ch18-afi.md) | Invert-exaggerate-generate-reinvert |

### Part VII: Beyond Engineering — Business & Management
| # | Chapter | Slug | Core Tool |
|---|---------|------|-----------|
| 19 | TRIZ for Business & Management | [ch19-triz-for-business.md](chapters/ch19-triz-for-business.md) | 5 thinking components, 12 double principles |
| 20 | Innovation Process Management | [ch20-innovation-process.md](chapters/ch20-innovation-process.md) | 10-step strategic + execution framework |
| 21 | Customer Benefit Analysis | [ch21-customer-benefit.md](chapters/ch21-customer-benefit.md) | Importance-satisfaction matrix |

### Part VIII: Implementation & Practice
| # | Chapter | Slug | Core Tool |
|---|---------|------|-----------|
| 22 | Implementation Methodology | [ch22-implementation.md](chapters/ch22-implementation.md) | 5-stage pipeline, prototyping, patents, commercialization |
| 23 | CAI — Computer-Aided Innovation | [ch23-cai.md](chapters/ch23-cai.md) | 7 tool categories, Function-Oriented Search |
| 24 | Corporate TRIZ Training & Certification | [ch24-corporate-training.md](chapters/ch24-corporate-training.md) | MATRIZ 5-level competency, deployment maturity model |

### Part IX: Practical Guidance
| # | Chapter | Slug | Core Tool |
|---|---------|------|-----------|
| 15 | Ten Pitfalls to Avoid | [ch15-ten-pitfalls.md](chapters/ch15-ten-pitfalls.md) | Common mistakes |
| 16 | Ten Tips for Getting Started with TRIZ | [ch16-ten-tips.md](chapters/ch16-ten-tips.md) | Best practices for beginners |

## Tool Coverage Matrix — Which Book Covers What

| TRIZ Tool | Dummies | Livotov | POWER TOOLS | Gadd | 金钥匙 | Altshuller | Bukhman |
|-----------|---------|---------|-------------|------|--------|------------|---------|
| 40 Principles | ✓✓✓ | ✓✓ | — | ✓✓ | ✓✓✓ | ✓✓✓ | ✓✓ |
| Contradiction Matrix (39) | ✓✓✓ | ✓ (critique) | — | ✓✓ | ✓✓ | ✓✓✓ | ✓✓ |
| Physical Contradictions | ✓✓✓ | ✓✓ | — | ✓✓ | ✓✓ | ✓✓ | ✓✓ |
| 8 Trends of Evolution | ✓✓✓ | ✓✓ | — | ✓✓ | ✓✓ | ✓✓✓ | ✓✓ |
| Ideality Equation | ✓✓✓ | ✓✓ | — | ✓✓ | ✓ | ✓✓ | ✓ |
| IFR | ✓✓ | ✓✓ | — | ✓✓ | ✓✓ | ✓✓ | ✓ |
| Function Analysis | ✓✓ | ✓✓ | — | ✓✓✓ | ✓✓ | ✓ | ✓ |
| Su-Field / 76 Standards | ✓✓ | ✓✓ | — | ✓✓✓ (Oxford) | ✓✓ | ✓✓✓ | ✓✓ |
| ARIZ | ✓ | ✓✓✓ | — | ✓✓ (5-step) | ✓ | ✓✓✓ | ✓ |
| AFI | — | ✓✓✓ | — | — | — | — | — |
| TRIZ for Business | — | ✓✓✓ | — | — | — | — | — |
| Effects Database | ✓✓ | ✓ | — | ✓ | ✓ | ✓✓ | ✓ |
| Psychological Inertia | ✓✓✓ | ✓ (DTC) | — | ✓ | ✓ | ✓ | — |
| 9-Windows | ✓✓ | ✓ | — | ✓ | ✓ | ✓✓ | — |
| Trimming | ✓✓✓ | ✓ | — | ✓ | ✓✓ | ✓ | — |
| S-Curve Analysis | ✓✓ | ✓✓ | — | ✓ | ✓✓ | ✓✓✓ | ✓ |
| Implementation | — | — | ✓✓✓ | — | — | — | — |
| CAI | — | ✓✓✓ | — | — | — | — | — |
| Innovation Process | — | ✓✓✓ | — | — | — | — | — |
| Customer Benefit Analysis | — | ✓✓✓ | — | — | — | — | — |
| Corporate Training | — | ✓✓✓ | — | — | — | — | — |

✓✓✓ = Comprehensive coverage, ✓✓ = Good coverage, ✓ = Brief mention, — = Not covered

## Report Generation & PPT Delivery (NotebookLM Integration)

After every TRIZ analysis or problem-solving session, produce a comprehensive report AND a presentation-ready slide deck.

### Step 1: Save the TRIZ Report

All generated reports go to the `report/` subdirectory:

```
C:\01_JianWANG\01_Projects\Skills\Triz\report\<topic-slug>.md
```

The report should be a well-structured Markdown file containing:
- Problem statement and context
- TRIZ tools applied and why
- Key findings, contradictions resolved, and solution concepts
- Visual descriptions (diagrams, tables, matrices)
- Recommendations and next steps

### Step 2: Generate Design PPT via NotebookLM

Once the report Markdown file is saved, **automatically invoke the `qiaomu-anything-to-notebooklm` skill** to produce a professional slide deck. The skill accepts local Markdown files directly — no format conversion needed.

**Workflow:**

1. **Invoke the NotebookLM skill** — use natural language: "将这份TRIZ报告生成一份设计PPT"
2. **The NotebookLM skill executes these commands internally:**
   ```
   notebooklm source add "<absolute-path-to-report>.md"
   notebooklm generate slide-deck
   artifact wait <task_id>
   download slide-deck "./report/<topic-slug>-ppt.pdf"
   ```
3. **Output** — PPT/PDF saved to `report/` alongside the original report

**Prerequisites:**
- `notebooklm login` must be completed before first use (one-time setup)
- Generation time: typically 1–3 minutes for PPT
- NotebookLM skill version: v1.0.0+ (recommended)

**Natural-language triggers (mapped by the NotebookLM skill):**
- "做成PPT" / "生成幻灯片" / "生成设计PPT" → `slide-deck` → `notebooklm generate slide-deck`

### Step 3: Confirm Delivery

After generation, confirm both outputs to the user:

```
✅ TRIZ Report: report/<topic-slug>.md
✅ Design PPT:  report/<topic-slug>-ppt.pdf
```

### Important Rules

- **Automatic chaining** — whenever a TRIZ report is generated and saved to `report/`, immediately chain into the NotebookLM skill. Do NOT wait for the user to ask.
- **Login check** — if `notebooklm login` has not been completed, remind the user to run it first, then deliver the report alone (PPT can be generated later).
- **Long reports** — for very long reports (>50 pages), consider generating a condensed "executive summary" version for the PPT to keep slide count manageable.
- **File naming** — the PPT filename should match the report slug with a `-ppt` suffix (e.g., `TRIZ_MultiStage_PCM_Thermal_Management-ppt.pdf`).

---

## Complementary AI Tools — Triz-AI Integration

TrizInv is a knowledge skill (methodology tutor). **[Triz-AI](https://github.com/fanfanbox/triz-ai)** is a Python CLI tool that complements it with **data-driven patent mining and LLM-assisted TRIZ analysis**. Use them together for maximum effect.

### What Triz-AI Does

| Capability | Command | What It Returns |
|-----------|---------|-----------------|
| Discover underused TRIZ principles in a domain | `triz-ai discover --domain "<domain>"` | Ranked list of TRIZ principles with low patent adoption in that domain — opportunity gaps |
| Analyze a technical problem with LLM | `triz-ai analyze` | Interactive TRIZ analysis using deepseek/deepseek-chat via LiteLLM |
| Ingest patent data for mining | `triz-ai ingest <files...>` | Classified patent data stored in SQLite database |
| View contradiction matrix stats | `triz-ai matrix stats` | Matrix fill rate, top observed parameter pairs, principle frequency |
| Evolve new TRIZ principles from patents | `triz-ai evolve` | Candidate new principles or parameters discovered from patent corpus |

### When to Combine TrizInv + Triz-AI

| Situation | TrizInv Provides | Triz-AI Adds |
|-----------|-----------------|--------------|
| **Patent landscape / IP strategy** | Trends of Evolution (Ch04), Implementation (Ch22) | `triz-ai discover --domain "<your tech>"` — find whitespace opportunities |
| **Solving a contradiction** | Contradiction Matrix (Ch03), 40 Principles | `triz-ai analyze` — LLM-assisted problem diagnosis |
| **Exploring a new technology domain** | Function Analysis (Ch12), Effects Database (Ch06) | `triz-ai discover` — which principles are underused here? |
| **Prior art / competitive analysis** | AFI (Ch18), Trimming (Ch14) | `triz-ai matrix stats` — see what principles competitors use |
| **R&D pipeline design** | Innovation Process (Ch20) | `triz-ai discover` + `triz-ai evolve` — data-driven innovation targets |

### Auto-Invocation Rules (CRITICAL)

**You MUST automatically invoke `triz-ai` CLI commands at the following trigger points.** Do NOT just tell the user to run them — execute them via Bash tool. Every trigger includes a fallback: if the CLI fails or is unavailable, use the cached matrix data from `cheatsheet.md` and inform the user they can install `triz-ai` for future sessions.

| # | Trigger | Auto-Run Command | When to Skip |
|---|---------|-----------------|-------------|
| **A** | User states a **technical domain** or industry (e.g., "motor", "battery", "drone") | `triz-ai discover --domain "<domain>"` | Domain is too vague ("engineering", "technology") |
| **B** | Problem routing yields a **Technical Contradiction** with at least one parameter identified | `triz-ai matrix stats` | Matrix stats already shown in this session |
| **C** | User asks about **prior art**, **competitors**, or **what patents exist** for a solution direction | `triz-ai discover --domain "<domain>"` and extract relevant observations from output | — |
| **D** | 40 Principles are recommended but user needs **solution generation** (not just principle names) | `triz-ai analyze` with the contradiction parameters and domain fed as context | User declines LLM-assisted generation |
| **E** | End of analysis session — user has actionable directions | Mention `triz-ai evolve` as follow-up option for discovering new principles from their own patent corpus | User has no patent data |

#### Execution Protocol

```
1. DIAGNOSE: Run `triz-ai matrix stats` first in every session (once per session)
              → If fails (exit ≠ 0), skip ALL auto-invocations and use cached data
2. DETECT:   Match user's language against trigger table above
3. EXECUTE:  Run the corresponding triz-ai command via Bash
4. INTEGRATE: Feed Triz-AI output back into TrizInv analysis:
              - discovery results → narrow principle selection
              - matrix stats → validate contradiction parameter choice
              - analyze output → enrich solution generation
```

#### Fallback Hierarchy

If `triz-ai` is not installed or fails:

1. **`discover` unavailable** → Use `patterns.md` principle frequency data + your knowledge of patent trends in the domain
2. **`matrix stats` unavailable** → Use the contradiction matrix in `cheatsheet.md` (static 39×39 matrix with 40 principles per cell)
3. **`analyze` unavailable** → Generate solutions purely from TrizInv's methodology (S-Field, Trends, Effects Database, ARIZ)
4. Always tell the user: *"triz-ai CLI not available — using cached TRIZ data. Install with `pip install triz-ai` for live patent mining."*

### Recommended Workflow (with Auto-Invocation)

```
Session Start
  └─ [AUTO: triz-ai matrix stats] ← runs once, validates CLI availability
      │
User states problem → TrizInv Problem Routing (contradiction type?)
  │
  ├─ Technical Contradiction detected
  │   ├─ [AUTO: triz-ai matrix stats] ← confirms parameter pair has patent data
  │   └─ TrizInv: Apply 40 Principles from contradiction matrix
  │       └─ [AUTO: triz-ai discover --domain "..."] ← find whitespace
  │       └─ [AUTO: triz-ai analyze] ← if user wants LLM synthesis
  │
  ├─ Physical Contradiction detected
  │   └─ TrizInv: Apply Separation Principles (Time/Space/Condition/System-level)
  │       └─ [AUTO: triz-ai discover] ← domain-specific principle gaps
  │
  └─ New domain exploration
      └─ [AUTO: triz-ai discover --domain "..."] ← mandatory trigger A
      └─ TrizInv: Function Analysis + Effects Database

Session End
  └─ TrizInv: Ideality evaluation, document in report/
  └─ Mention: `triz-ai evolve` if user has patent corpus to analyze
```

**Prerequisites:** `triz-ai` must be installed (`pip install triz-ai`). LLM backend: deepseek/deepseek-chat via LiteLLM. Embeddings: Ollama `nomic-embed-text`. Auto-invocation degrades gracefully if unavailable.

> **Note:** Triz-AI and TrizInv are fundamentally different tools that cannot be merged — one is a knowledge skill loaded into LLM context, the other is a standalone Python CLI program. They complement each other: TrizInv answers "how to think about innovation problems," Triz-AI answers "what do patents tell us about this domain?" The automation rules above bridge them: the Skill drives the CLI at the right moments.

---

## How to Use This Skill

**For solving a specific problem**: Start with the Problem Routing diagnostic above. Let the yes/no questions guide you to the right tool. Use [cheatsheet.md](cheatsheet.md) for quick parameter lookups and the contradiction matrix during problem-solving.

**For learning TRIZ systematically**: Read chapters in order. Parts I-V (Ch1-14) cover the core toolbox. Parts VI-VIII (Ch17-24) cover advanced and specialized methods. Part IX (Ch15-16) covers practical guidance. Use [glossary.md](glossary.md) for unfamiliar terms.

**For facilitating a team session**: Use [Ch10](chapters/ch10-group-creativity.md) for group process, then route to specific tools based on what emerges. Keep [cheatsheet.md](cheatsheet.md) open for quick reference during the session.

**For business innovation**: Start with [Ch19](chapters/ch19-triz-for-business.md) for the 12 Business TRIZ double principles, then use [Ch20](chapters/ch20-innovation-process.md) for the 10-step process, and [Ch21](chapters/ch21-customer-benefit.md) for customer analysis. See [patterns.md](patterns.md) for the full Business TRIZ pattern catalog.

**For failure prevention**: Use [Ch18](chapters/ch18-afi.md) — invert your safety goal into a failure goal, generate failures with TRIZ tools, then re-invert to find fixes. The AFI 4-step checklist is in [cheatsheet.md](cheatsheet.md).

**For implementing a solution**: Use [Ch22](chapters/ch22-implementation.md) for the complete 5-stage implementation pipeline from concept validation through post-launch monitoring. See [patterns.md](patterns.md) for the prototype escalation ladder.

**For quick reference during problem-solving**: Use [cheatsheet.md](cheatsheet.md) for the Contradiction Matrix, routing flow, and all checklists (AFI, ARIZ, I-S Matrix, MATRIZ levels, Business Principles). Use [patterns.md](patterns.md) for detailed sub-steps of each pattern. Use [glossary.md](glossary.md) for term definitions.
