# Chapter 17: ARIZ — Algorithm of Inventive Problem Solving

## Core Idea
ARIZ is the most powerful and complete TRIZ tool — a 26-step structured algorithm for solving the hardest, most ambiguous inventive problems where conventional TRIZ tools fail. It systematically reframes the problem, resolves contradictions, and iteratively eliminates psychological inertia until a breakthrough emerges.

## Frameworks Introduced

- **ARIZ-85 (Classical ARIZ)**: 26-step algorithm in 9 parts, from problem analysis through solution implementation. Developed by Altshuller as the "crown jewel" of TRIZ for Level 3-4 inventive problems.
  - When to use: When Contradiction Matrix, Standard Solutions, and other simpler TRIZ tools have been exhausted. The problem feels insoluble; multiple contradictory requirements; the "mini-problem" can't be clearly stated.
  - When NOT to use: For Level 1-2 problems (use 40 Principles or Standards instead). For problems with clear technical contradictions solvable through the Matrix.

- **Simplified 5-Step ARIZ (Gadd)**: A practical, condensed version for engineering use:
  1. **Define the Mini-Problem** — strip away constraints, state the simplest version
  2. **Identify the Contradiction** — both technical and physical
  3. **Apply IFR** — define the ideal solution ignoring all constraints
  4. **Apply Separation Principles** — time, space, condition, system
  5. **Apply Standard Solutions & Effects** — search for known patterns
  - When to use: When full 26-step ARIZ is too heavy for the problem complexity.

## Key Concepts

- **Mini-Problem**: The simplest possible formulation of the problem, stripped of all constraints, jargon, and "we can't because..." assumptions. ARIZ Step 1 forces this reduction.
- **Technical Contradiction (TC)**: Improving parameter A worsens parameter B. ARIZ identifies TC-1 (original) and TC-2 (intensified — make it even worse to force breakthrough thinking).
- **Physical Contradiction (PC)**: One parameter must be in two opposite states. ARIZ pushes you to intensify until a macro-PC and micro-PC are identified.
- **Ideal Final Result (IFR)**: In ARIZ, the IFR is formulated with extreme precision: "The X-element, without complicating the system or causing harmful effects, eliminates [harmful action] during [time/condition], while preserving [useful action]."
- **Substance-Field Resources (SFR)**: Systematically cataloging all available substances, fields, space, time, and information resources — ARIZ's Inventory step (Part 2).
- **Zone of Conflict**: The exact spatial location where the contradiction physically manifests, distinguished from the broader operational zone.
- **X-Element**: An unknown substance or field that resolves the contradiction. ARIZ helps you specify exactly what properties this X-element must have before you search for what it actually is.
- **Operative Time**: The exact time window when the conflict occurs, separated from pre-conflict and post-conflict time.

## Mental Models

- **Intensify the contradiction, don't soften it.** Most people instinctively compromise. ARIZ forces you to make the contradiction MORE extreme — "the part must be 1000°C hot and -200°C cold simultaneously" — because intensified contradictions reveal separation opportunities invisible in mild forms.
- **Define the X-element by what it must DO, not what it IS.** ARIZ builds a complete functional specification for an unknown solution element before searching for candidates. This prevents premature fixation on known technologies.
- **The problem you first define is never the real problem.** ARIZ's iterative refinement loop (Steps 1-7 explicitly re-check the mini-problem) is the algorithm's most valuable feature — it catches wrong framing that wastes weeks of effort.
- **Conflict resolution lives at the zone of conflict, not the whole system.** Zoom into the physical micro-location where the contradiction actually occurs. Solutions that change the whole system are usually over-designed.

## ARIZ-85 Structure (9 Parts, 26 Steps)

```
PART 1: PROBLEM ANALYSIS (Steps 1-7)
  1. Formulate the mini-problem
  2. Identify the conflicting pair (product + tool)
  3. Build graphic models of TC-1 and TC-2
  4. Select the best conflict model
  5. Intensify: state the limiting condition
  6. Formulate macro Physical Contradiction
  7. Formulate micro Physical Contradiction (interacting particles)

PART 2: RESOURCE ANALYSIS (Steps 8-10)
  8. Define the operational zone
  9. Define operative time
  10. Define Substance-Field Resources (SFR)

PART 3: IFR & PHYSICAL CONTRADICTION (Steps 11-13)
  11. Formulate IFR-1
  12. Intensify IFR with additional requirements
  13. Formulate Physical Contradiction at micro-level

PART 4: RESOURCE MOBILIZATION (Steps 14-19)
  14. Apply SLP (Smart Little People) modeling
  15. Step back from IFR toward feasible solution
  16. Apply substance mixtures
  17. Apply void/vacuum
  18. Apply derived substances from SFR
  19. Apply electrical/field solutions

PART 5: KNOWLEDGE BASE (Steps 20-21)
  20. Navigate solution toward IFR-1
  21. Apply Standards, Effects, and Principles

PART 6: CHANGE THE PROBLEM (Step 22)
  22. Reformulate the problem if no solution

PART 7: ELIMINATE PHYSICAL CONTRADICTION (Steps 23-24)
  23. Apply Separation Principles
  24. Apply phase transitions and physical effects

PART 8: SOLUTION ANALYSIS (Step 25)
  25. Verify the solution concept

PART 9: IMPLEMENTATION (Step 26)
  26. Apply the solution and evaluate sub-system effects
```

## The Coal Pipe Example (ARIZ in Practice)

From Gadd's coal pipe problem — coal dust flows through pipes, wearing them out where pipes bend:

1. **Mini-Problem**: "How to prevent coal dust from eroding pipe bends?"
2. **TC-1**: Improving pipe durability (strength) worsens cost and weight.
3. **TC-2 (intensified)**: Making the pipe harder causes coal dust to abrade even more aggressively.
4. **Phys Contradiction**: The pipe wall at the bend must be PRESENT (to guide coal) and ABSENT (to avoid being hit).
5. **IFR**: Coal dust does not contact the bend wall.
6. **Resource inventory**: Coal dust itself is already present, has mass, is moving at speed.
7. **Solution**: Let coal dust accumulate at the bend to form a self-replenishing protective layer — the coal wears on coal, not the pipe wall. Add a pocket at the bend to hold coal dust in place.

The solution uses **Principle 25 (Self-Service)** — the harmful substance becomes the protective substance.

## Anti-patterns

- **Skipping to Part 5 too early**: Jumping to the knowledge base (Standards, Effects, Principles) before completing resource analysis. ARIZ front-loads problem framing because most "unsolvable" problems are just poorly framed. Do not skip Parts 1-4.
- **Accepting the first TC without testing TC-2**: The first technical contradiction is usually too mild. Intensifying it (Step 5) regularly reveals that the original TC was misidentified.
- **Using ARIZ for routine problems**: ARIZ can take days. For Level 1-2 problems, it's massive overkill. Reserve it for the hardest ~5% of problems.
- **Treating ARIZ as linear**: Steps 22 explicitly tells you to restart if no solution is found. Treat ARIZ as iterative, not a one-pass checklist.

## Key Takeaways

1. ARIZ is a step-by-step algorithm for solving problems that have resisted all simpler TRIZ tools
2. The most critical phase is Problem Analysis (Steps 1-7): define the mini-problem, identify and INTENSIFY contradictions
3. Intensifying a contradiction reveals separation opportunities that mild forms hide
4. Complete a full resource inventory before searching for solutions — the answer is usually hiding in plain sight
5. The X-element is defined by function ("must prevent contact") before form ("it's coal dust")
6. Step 22 reformulation is not failure — it's the algorithm's way of catching incorrect early framing
7. For most practical engineering problems, the 5-step simplified ARIZ is sufficient

## Connects To

- **Ch03 (40 Principles)**: ARIZ applies Principles in Part 5 after deep problem analysis — the Principles are more powerful when the contradiction is precisely defined
- **Ch09 (IFR)**: ARIZ uses IFR with extreme precision (macro/micro, operational zone, operative time) — the most rigorous IFR formulation in all of TRIZ
- **Ch13 (76 Standard Solutions)**: ARIZ Part 5 explicitly calls the Standards as its fallback knowledge base
- **Ch07 (Psychological Inertia)**: ARIZ is fundamentally designed to overcome psychological inertia through structured reframing — SLP, DTC, and 9-Windows are integrated into the algorithm
- **Ch06 (Effects Database)**: ARIZ Part 5 queries the Effects Database when known patterns fail
- **Ch18 (AFI)**: AFI inverts ARIZ thinking — instead of "how to succeed?", ask "how to fail?" — both use intensive contradiction analysis
