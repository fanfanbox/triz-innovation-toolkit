# TRIZ Quick Reference Cheatsheet

Concise lookup tables and flowcharts for TRIZ application. Use this when you know what you need and just want the parameters, principles, or routing.

---

## The 39 Engineering Parameters

Use these with the Contradiction Matrix to identify which Principles to apply.

**WEIGHT / FORCE:**
1. Weight of moving object
2. Weight of stationary object
3. Length of moving object
4. Length of stationary object
5. Area of moving object
6. Area of stationary object
7. Volume of moving object
8. Volume of stationary object
9. Speed
10. Force (intensity)
11. Stress or pressure
12. Shape

**DURABILITY / STABILITY:**
13. Stability of the object's composition
14. Strength
15. Duration of action of moving object
16. Duration of action of stationary object
17. Temperature
18. Illumination intensity (brightness)

**ENERGY / EFFICIENCY:**
19. Use of energy by moving object
20. Use of energy by stationary object
21. Power
22. Loss of Energy
23. Loss of substance
24. Loss of Information
25. Loss of Time
26. Quantity of substance/the matter
27. Reliability
28. Measurement accuracy

**MANUFACTURE / CONTROL:**
29. Manufacturing precision
30. External harm affects the object
31. Object-generated harmful factors
32. Ease of manufacture
33. Ease of operation
34. Ease of repair
35. Adaptability or versatility
36. Device complexity
37. Difficulty of detecting and measuring
38. Extent of automation
39. Productivity

---

## Top 20 Most Common Contradictions & Principles

| Improving (Row) | Worsening (Col) | Top Principles |
|---|---|---|
| Strength | Weight (moving) | 1, 8, 15, 40 |
| Weight (moving) | Strength | 28, 27, 18, 40 |
| Speed | Power | 8, 15, 35, 38 |
| Power | Weight (moving) | 35, 19, 2, 15 |
| Reliability | Device complexity | 35, 13, 1, 28 |
| Productivity | Accuracy | 10, 28, 32, 1 |
| Shape | Speed | 5, 14, 36, 35 |
| Temperature | Strength | 35, 3, 19, 2 |
| Durability | Weight | 3, 10, 29, 40 |
| Loss of Energy | Productivity | 35, 28, 2, 14 |
| Ease of operation | Productivity | 1, 28, 13, 35 |
| Adaptability | Device complexity | 15, 29, 37, 28 |
| Loss of substance | Area (moving) | 10, 14, 18, 35 |
| Force | Shape | 10, 35, 40, 34 |
| Speed | Loss of Energy | 14, 19, 28, 35 |
| Measurement accuracy | Ease of operation | 32, 28, 1, 24 |
| Harmful effects | Productivity | 22, 35, 18, 39 |
| Strength | Loss of Energy | 35, 29, 28, 2 |
| Ease of manufacture | Device complexity | 1, 13, 28, 32 |
| Reliability | Temperature | 35, 2, 28, 3 |

---

## Separation Principles (Physical Contradictions)

| Separation Type | When to Use | Example |
|---|---|---|
| **In Space** | X must be big HERE and small THERE | Bicycle chain: rigid at teeth, flexible between |
| **In Time** | X must be big NOW and small LATER | Aircraft landing gear: down for landing, up in flight |
| **Upon Condition** | X must be X₁ under condition A, X₂ under condition B | Viscous clutch: locks when hot, slips when cool |
| **System-Level** | X must be X₁ at macro level, X₂ at micro level | Solid beam vs many fibres (strong + flexible) |

---

## Physical Contradiction → Principle Quick-Map

| Physical Contradiction | Start with Principles |
|---|---|
| Must be strong AND flexible | 1, 7, 15, 35 |
| Must be hot AND cold | 35, 36, 38, 5 |
| Must be present AND absent | 2, 10, 24, 34 |
| Must be big AND small | 1, 7, 17, 5 |
| Must be fast AND slow | 19, 21, 20, 15 |
| Must be heavy AND light | 8, 40, 31, 29 |
| Must be moving AND stationary | 15, 19, 17, 5 |

---

## Quick Problem Routing

```
Problem? ──┬── Already a contradiction? ──→ Contradiction Matrix → 40 Principles
           │
           ├── Something missing/excessive/bad interaction? ──→ Su-Field → 76 Standards
           │
           ├── Don't know which direction to evolve? ──→ 8 Trends + S-Curve
           │
           ├── Resisted simpler tools? ──→ ARIZ (5-step)
           │
           ├── Need a physical mechanism? ──→ Effects Database
           │
           ├── System too complex? ──→ Function Analysis → Trimming
           │
           ├── Innovating for business? ──→ 12 Double Principles + I-S Matrix
           │
           └── Before launch/design freeze? ──→ AFI (4-step)
```

---

## Tool Selection by Task Type

| Task Type | Primary Tool | Secondary |
|---|---|---|
| Solve a trade-off | Contradiction Matrix + 40 Principles | Separation Principles |
| Improve an existing system | Function Analysis + Trimming | 76 Standards |
| Predict next generation | Trends of Evolution | S-Curve Analysis |
| Find new physical mechanism | Effects Database | Function-Oriented Search (FOS) |
| Stuck on hard problem | ARIZ (5-step) | Smart Little People |
| Prevent future failures | AFI | FMEA (complementary) |
| Reduce cost | Function Analysis + Trimming | Value Engineering (CAI) |
| Business strategy/org design | 12 Double Principles + IFR | Trends of Evolution |
| Validate innovation direction | Customer Benefit (I-S Matrix) | Ideality KPIs |
| Scale from concept to production | Implementation Pipeline (5 stages) | AFI for risk |
| Train/organize TRIZ capability | MATRIZ 5-Level Model | Deployment Maturity Model |

---

## The Ideality Equation

$$\text{Ideality} = \frac{\sum \text{Benefits (Useful Functions)}}{\sum \text{Costs} + \sum \text{Harms (Harmful Functions)}}$$

**Business Ideality** = Σ Customer Value / (Σ Costs + Σ Harms)

Ideal Final Result (IFR): The system delivers the function WITHOUT the system existing — benefits remain, costs and harms go to zero.

---

## 5 Levels of Invention (Altshuller)

| Level | Description | % of Patents | Knowledge Source |
|---|---|---|---|
| 1 | Routine design (no contradiction) | 32% | Individual's knowledge |
| 2 | Minor improvement (weak contradiction) | 45% | Single company knowledge |
| 3 | Major improvement (resolved contradiction) | 18% | Cross-industry knowledge |
| 4 | New concept (new scientific principle) | 4% | Cross-science knowledge |
| 5 | Discovery (fundamentally new science) | <1% | Beyond current science |

---

## S-Curve Strategy by Stage

| Stage | Strategy | TRIZ Tools |
|---|---|---|
| **Infancy** | Invest, protect IP, prove viability | Patent analysis, Trends |
| **Growth** | Optimize reliability, scale production | Contradiction Matrix, Effects |
| **Maturity** | Cost reduction, add features | Trimming, Function Analysis |
| **Decline** | Transition to next-gen system | Trends, ARIZ, Effects |

---

## Resource Types (Remember These)

| Resource | Look For |
|---|---|
| Substances | Air, water, waste, parts already present |
| Fields | Gravity (free!), E/M fields, thermal, vibration |
| Space | Voids, unused volume, the other side |
| Time | Between cycles, pre-processing, post-processing |
| Information | Available data streams, signals already present |
| Functions | Functions already performed that can serve double duty |
| Harmful | Turn the harmful effect into a useful function (Principle 22) |

---

## ARIZ 5-Step Quick Reference (Ch17)

| Step | Action | Key Question |
|---|---|---|
| 1 — Problem Restatement | Define Mini-Problem + IFR | "System for X must provide Y with minimum changes." |
| 2 — Contradiction ID | Technical → Physical Contradiction | "X must be A and non-A simultaneously." |
| 3 — Resources | Map ZoF (space) + OT (time) + SFR | "What's already there at the point of conflict?" |
| 4 — Solution Search | Apply all TRIZ tools systematically | "What is X that solves this without complicating?" |
| 5 — Refinement | Evaluate, develop, resolve 2° problems | Back to Step 1 if no solution. |

**Trigger:** Problem resisted simpler tools for >2 hours. Level 3-4 problems.

---

## AFI 4-Step Checklist (Ch18)

| Step | Action | Output |
|---|---|---|
| 1 — Invert | "How CAN I deliberately cause this failure?" | List of 10+ failure modes |
| 2 — Exaggerate | Amplify each to worst-case extreme | Worst-case failure mechanisms |
| 3 — Generate | Apply TRIZ tools to prevent each failure | Prevention solutions |
| 4 — Re-invert & Fix | Prioritize: severity × likelihood | Fixed vulnerabilities |

**When:** Before design freeze, before production, safety-critical × 2.

---

## 12 Double Business Principles (Ch19)

| # | Principle | ↔ Anti-Principle |
|---|---|---|
| 1 | Segmentation | Merging |
| 2 | Taking Out | Adding In |
| 3 | Local Quality | Standardization |
| 4 | Asymmetry | Symmetry |
| 5 | Merging | Segmentation |
| 6 | Universality | Specialization |
| 7 | Nested | Flat |
| 8 | Anti-Weight | Added Weight |
| 9 | Preliminary Anti-Action | Reactive Action |
| 10 | Preliminary Action | Just-in-Time |
| 11 | Beforehand Cushioning | Lean/Bare |
| 12 | Feedback | Feedforward |

**Key insight:** BOTH sides are valid — the choice depends on the specific business context.

---

## I-S Matrix Quick Lookup (Ch21)

| | High Importance | Low Importance |
|---|---|---|
| **Low Satisfaction** | 🎯 PRIORITY #1 — TRIZ effort here | 🗑 Ignore |
| **High Satisfaction** | ✅ Maintain — don't over-invest | ✂ TRIM — cut investment |

**Process:** (1) List benefits in customer language → (2) Measure I (customer survey) → (3) Measure S vs best competitor → (4) Gap = I − S → (5) Translate largest gaps to TRIZ problem statements.

---

## Implementation Pipeline (Ch22)

| Stage | Purpose | Budget |
|---|---|---|
| 1 — Concept Validation | Prove core mechanism works | <5% |
| 2 — Detailed Design | Resolve ALL secondary problems; apply AFI | ~15% |
| 3 — Prototyping & Testing | Escalate: breadboard → engineering → production | ~30% |
| 4 — Production Ramp-Up | Tooling, training, pilot → full production | ~40% |
| 5 — Post-Launch Monitoring | Field data → next innovation cycle | ~10% |

**Prototype Ladder:** Thought → Simulation → Breadboard → Engineering → Production

---

## CAI Tool Categories (Ch23)

| Category | Function |
|---|---|
| Contradiction Solvers | Auto-match parameters → Principles |
| Effects Databases | Search physical/chemical effects by function |
| Patent Analyzers | Mine patents for trends & white spaces |
| Semantic Search | NLP match problem → TRIZ knowledge |
| Technology Forecasting | S-Curve + Trends prediction |
| Function Modelers | Auto-build function models, find contradictions |
| Value Engineering | Function Analysis + cost → trimming targets |

**Killer App:** Function-Oriented Search (FOS) — "How does ANY industry achieve function X?"

---

## MATRIZ 5-Level Competency (Ch24)

| Level | Role | Training |
|---|---|---|
| 1 — Foundation | Participant in facilitated sessions | 40h (5 days) |
| 2 — Practitioner | Independent solver, standard tools | 80h + 2-3 projects |
| 3 — Advanced | Lead projects, ARIZ, train L1-2 | 120h + 3-5 mentored projects + exam |
| 4 — Expert | Org-wide deployment, adapt TRIZ | 200h + 5+ major projects |
| 5 — Master | Theory advancement, global direction | Selection by Masters |

---

## TRIZ Deployment Maturity (Ch24)

| Level | Name | Sign |
|---|---|---|
| 0 | Unaware | Trial-and-error |
| 1 | Awareness | Isolated TRIZ projects |
| 2 | Adoption | Formal training, regular workshops |
| 3 | Integration | TRIZ in stage-gate, KPIs tracked |
| 4 | Culture | TRIZ is default thinking |
| 5 | Excellence | Published cases, internal research |

**Key principles:** Train in project-tied cohorts; build internal capability from day one; depth before breadth.

---

## 10-Step Innovation Process (Ch20)

```
STRATEGIC (Where & Why):           EXECUTION (What & How):
1. Situation Analysis               6. Idea Generation
2. Strategic Diagnosis              7. Idea Evaluation
3. Innovation Goal Setting          8. Concept Development
4. Strategy Development             9. Implementation
5. Strategic Controlling           10. Innovation Controlling
                                         ↓ feeds back to → 1
```

---

## Quick Reference: Key Concepts

| Concept | Meaning | Ch |
|---|---|---|
| Ideality | Benefits / (Costs + Harms) | 5 |
| IFR | System delivers function without existing | 5 |
| Contradiction | Improving A worsens B (TC); X must be BIG and SMALL (PC) | 2 |
| Su-Field | Substance-Field model: 2 substances + 1 field | 10 |
| S-Curve | Infancy → Growth → Maturity → Decline | 4 |
| Trimming | Remove component, transfer its useful function | 14 |
| 9 Windows | System/Sub/Super × Past/Present/Future | 8 |
| Smart Little People | Mental model: imagine problem as tiny agents | 8 |
| X-Element | Unknown that solves without complicating | 17 |
| Mini-Problem | System for X must deliver Y with minimum changes | 17 |
| ZoF + OT | Zone of Conflict at Operative Time | 17 |
| AFI | Anticipatory Failure Identification (Invert→Exaggerate→Generate→Fix) | 18 |
| FOS | Function-Oriented Search across all industries | 23 |
| B-IFR | Business IFR: max customer value, zero cost+harm | 19 |
| I-S Gap | Importance − Satisfaction = innovation priority | 21 |
| Secondary Problems | Sub-problems created by solving the primary problem | 22 |
| TRIZ Tourist | Knows terminology but can't apply — avoid via project-based training | 24 |
