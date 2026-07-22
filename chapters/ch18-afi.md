# Chapter 18: AFI — Anticipatory Failure Identification

## Core Idea
AFI (Anticipatory Failure Identification) is the TRIZ tool for predicting and preventing failures BEFORE they happen. Instead of asking "How do we make this safe?", it inverts the question to "How do we make this fail catastrophically?" — then uses TRIZ tools to generate failure modes systematically, and finally re-inverts to find design fixes. It's the pre-mortem of engineering design, adapted from Livotov's TRIZ Handbook.

## Frameworks Introduced

- **AFI 4-Step Core Process**: The fundamental algorithm for failure prediction and prevention.
  - When to use: During design phase BEFORE prototyping; when safety is critical; when failure modes are not obvious; when traditional FMEA misses systemic interactions.
  - When NOT to use: For well-understood, standard designs with exhaustive failure databases. For simple single-point failures easily caught by FMEA.

- **AFI + TRIZ Tool Chain**: Systematically applying TRIZ tools to the INVERTED problem (generating failures, not solutions).
  - When to use: When brainstorming failure modes produces nothing new. The structured TRIZ approach uncovers non-obvious failure cascades.

## Key Concepts

- **Task Inversion**: The core AFI move — turn "Ensure X doesn't happen" into "Make X happen as spectacularly as possible." This bypasses cognitive biases that make us blind to our own design's weaknesses.
- **Failure Mode Exaggeration**: Don't just list failures — intensify them. "Leak" becomes "catastrophic blowout." "Overheat" becomes "meltdown and fire." Exaggerated failures reveal chain reactions invisible in mild form.
- **Saboteur Mindset**: AFI requires genuinely trying to break the system. The psychological shift from "defender" to "attacker" is what makes AFI effective — it's the same cognitive mechanism that makes external red teams more effective than internal reviews.
- **Re-inversion**: After generating failures, flip back: "If the saboteur can cause X by doing Y, then the fix is to prevent Y." Each failure mechanism points directly to a design countermeasure.
- **AFI vs FMEA**: Traditional FMEA relies on expert experience to list failure modes. AFI uses TRIZ tools (Contradiction Matrix, 40 Principles, Su-Field, Trends) to GENERATE failure modes that experts might miss — especially systemic, multi-component interaction failures.
- **Harmful Function Analysis**: Applying Function Analysis in reverse — instead of modeling useful functions, model what harmful functions the components COULD perform under failure conditions.

## The AFI 4-Step Process

```
STEP 1: INVERT THE TASK
  Original task:  "Prevent the battery from overheating"
  Inverted task:  "Make the battery overheat as intensely as possible"
  
  Key question: "If I were a saboteur trying to cause [original failure],
                how would I do it using only the system's own resources?"

STEP 2: EXAGGERATE THE FAULT
  For each failure mode, intensify to maximum:
  - "Overheat" → "Thermal runaway, fire, explosion"
  - "Leak" → "Complete seal failure, total fluid loss"
  - "Wear" → "Instant disintegration"
  
  Key question: "What's the worst possible version of this failure?
                What chain reaction does it trigger?"

STEP 3: GENERATE FAILURES WITH TRIZ TOOLS
  Apply TRIZ tools to the INVERTED problem:
  
  | TRIZ Tool | AFI Application |
  |-----------|----------------|
  | Contradiction Matrix | Find contradictions that, if resolved WRONGLY, cause failure |
  | 40 Principles | Apply each principle as a "how to break this" technique |
  | Su-Field Analysis | Model harmful interactions that could emerge |
  | Trends of Evolution | Predict failure modes from system evolution |
  | Function Analysis | Identify components with potential for harmful secondary functions |
  | Effects Database | Find physical effects that could cause damage |
  | Trimming (inverted) | "What if we remove the safety feature? What happens?" |
  
  Key question: "What does each TRIZ tool reveal when applied to the
                inverted problem?"

STEP 4: RE-INVERT & FIND FIXES
  For each generated failure mode:
  1. Identify the CAUSE chain (what enables the saboteur?)
  2. Re-invert: "How do we prevent this cause?"
  3. Apply normal TRIZ problem-solving to each fix
  4. Prioritize by: severity × likelihood × detectability
  
  Key question: "Now that we know HOW the system can fail, what design
                change makes that failure mode impossible?"
```

## Mental Models

- **Every design decision is a failure waiting to happen.** AFI treats every feature, every component, every parameter choice as a potential failure source. This paranoia is productive during design and expensive to skip.
- **Your own design is invisible to you.** Cognitive biases (confirmation bias, sunk cost, design fixation) make you blind to failures in your own work. AFI's inversion bypasses these by forcing you to switch sides — from creator to destroyer.
- **Systems fail at interactions, not components.** Most catastrophic failures are not single-component failures but unexpected interactions between components all operating within spec. AFI's use of Su-Field Analysis and Function Analysis specifically targets interaction failures.
- **The best failure mode is the one you didn't think of.** AFI's systematic TRIZ-based generation surfaces failures that brainstorming misses. The structured approach compensates for the limits of expert intuition.

## Worked Example: AFI on a Lithium-Ion Battery Pack

**Original Task**: Design a safe Li-ion battery pack for an eVTOL aircraft.

**Step 1 — Invert**: "How do we make the battery pack fail catastrophically in flight?"

**Step 2 — Exaggerate**: Not just "overheat" but "cascading thermal runaway leading to complete power loss + fire at 5000ft altitude."

**Step 3 — Generate with TRIZ tools**:
- *40 Principles applied as sabotage*:
  - Principle 25 (Self-Service): Let the battery's own heat accelerate the chemical reaction → thermal runaway loop
  - Principle 36 (Phase Transition): Electrolyte vaporizes → internal pressure → cell rupture
  - Principle 30 (Flexible Shells): Vibration fatigue on busbars → micro-cracks → resistance → heat → more expansion
- *Su-Field Analysis*: Vibration field (F_vib) acting on busbar (S1) → fatigue crack → partial connection → resistive heating (F_therm) → electrolyte decomposition
- *Function Analysis (inverted)*: The cooling system performs the HARMFUL function of masking thermal buildup by keeping external sensors cool while internal cells rise
- *Trends analysis*: Trend toward higher energy density → thinner separators → higher probability of dendrite puncture

**Step 4 — Re-invert & Fix**:
| Failure Mode | Cause | Fix |
|-------------|-------|-----|
| Thermal runaway cascade | Adjacent cell heating → neighbor ignition | Inter-cell thermal barriers + phase-change material |
| Busbar fatigue cracking | Vibration at resonant frequency | Vibration-damped mounting + flexible busbar design |
| Cooling masks hot spots | Sensors on casing, not cells | Per-cell temperature monitoring + internal cell sensors |
| Dendrite puncture | High energy density = thin separators | Ceramic-coated separators + dendrite-resistant electrolyte |

## Anti-patterns

- **Half-hearted inversion**: If you're still emotionally attached to the design while trying to sabotage it, you'll pull punches. The saboteur mindset must be genuine — actually TRY to break it.
- **Stopping after obvious failures**: AFI's value is in the non-obvious, systemic failures. If your AFI session only produces failure modes you already knew about, you're not using the TRIZ tools aggressively enough.
- **Skipping the exaggeration step**: Mild failures ("slight leak") don't trigger the cascading thinking that exaggeration ("complete seal failure → fluid loss → bearing seizure → shaft fracture →...") produces.
- **Treating AFI as one-pass**: Like FMEA, AFI should be iterative. First pass finds failures; second pass applies AFI to the FIXES to ensure they don't introduce new failure modes.

## Key Takeaways

1. AFI inverts the safety question: "How do we cause the failure?" instead of "How do we prevent it?"
2. The 4-step process: Invert → Exaggerate → Generate with TRIZ → Re-invert & Fix
3. Apply the full TRIZ toolkit to the INVERTED problem — each tool reveals different failure modes
4. Exaggerate every failure to its worst-case to reveal chain reactions and systemic interactions
5. The saboteur mindset is a psychological tool — it bypasses cognitive biases that blind you to your own design's weaknesses
6. AFI is complementary to FMEA, not a replacement — AFI generates failure modes; FMEA prioritizes and tracks them
7. Re-inversion maps each failure cause directly to a design fix — every failure found is an improvement opportunity

## Connects To

- **Ch03 (40 Principles)**: In AFI, each Principle is applied in reverse — "how can Segmentation cause failure?" instead of "how can Segmentation solve this?"
- **Ch12 (Function Analysis)**: AFI uses inverted Function Analysis to find harmful secondary functions
- **Ch13 (76 Standard Solutions)**: Su-Field models in AFI reveal harmful field-substance interactions
- **Ch04 (Trends of Evolution)**: Trends predict failure modes that will emerge as the system evolves
- **Ch17 (ARIZ)**: ARIZ and AFI are the two "power tools" — ARIZ solves hard problems, AFI prevents hard failures
- **Ch07 (Psychological Inertia)**: AFI directly attacks the designer's psychological inertia through forced role-switching
- **Ch09 (IFR)**: AFI can be applied to the IFR itself — "what failures could prevent achieving the ideal?"
