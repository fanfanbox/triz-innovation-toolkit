# Chapter 22: Implementation Methodology

## Core Idea
Having a brilliant TRIZ solution is worthless if it never reaches production. The Implementation Methodology (from Livotov's TRIZ Handbook and Gadd's TRIZ for Engineers) provides a structured approach to bridging the gap between TRIZ-generated concepts and validated, production-ready implementations — covering prototyping, testing, IP protection, resistance management, and organizational adoption.

## Frameworks Introduced

- **Implementation Pipeline (5 Stages)**: Concept Validation → Detailed Design → Prototyping & Testing → Production Ramp-Up → Post-Launch Monitoring.
  - When to use: Every time a TRIZ concept has passed initial evaluation (Step 7 of the 10-Step Innovation Process) and needs to be turned into reality.
  - When NOT to use: For ideas still at the raw brainstorming stage. For concepts that haven't passed basic feasibility screening.

- **Resistance Management Framework**: Systematic approach to overcoming organizational, technical, and psychological resistance to new solutions.
  - When to use: When the solution is unconventional or disruptive; when previous implementations have stalled; when organizational antibodies are active.
  - When NOT to use: For incremental improvements that fit within existing systems and processes.

- **Secondary Problem Cascade**: Mapping all the sub-problems that a TRIZ solution creates — solving one contradiction often creates 5-10 smaller problems that must be resolved for implementation.
  - When to use: After generating a strong solution concept but before committing to implementation timeline.

## Key Concepts

- **Concept Validation**: Before investing in detailed design, verify that the concept actually works at a fundamental level. This can be a simple proof-of-principle experiment, a simulation, or a breadboard prototype. The goal is to kill bad ideas cheaply.
- **Secondary Problems**: Every TRIZ solution introduces secondary effects. Applying one Principle (e.g., Segmentation) may create assembly complexity, reliability concerns, or cost increases in other subsystems. List ALL secondary effects before designing the final solution.
- **Prototype Escalation**: A deliberate sequence from low-fidelity to high-fidelity prototypes:
  1. Paper/thought experiment — free, immediate
  2. Simulation / CAE — low cost, high learning
  3. Breadboard / 3D-printed functional prototype — proves core mechanism
  4. Engineering prototype — near-production materials and processes
  5. Production prototype — final validation before tooling
- **Not-Invented-Here (NIH) Syndrome**: The organizational resistance to solutions originating outside the team. TRIZ's systematic approach can trigger NIH because the solution appears to come from a method rather than from the team's expertise.
- **Solution Ownership Transfer**: Techniques for making the implementing team feel ownership of a TRIZ-generated solution — involve them early in evaluation, let them add their refinements, credit them for implementation improvements.
- **IP Gateway**: The decision point where a solution concept is evaluated for patentability vs trade secret protection. TRIZ solutions, especially those solving contradictions, often have high patentability.
- **Implementation Contradiction**: The solution creates its own contradiction — "We need to implement this new design (A) without disrupting current production (B)." This is itself a TRIZ problem to be solved.

## The Implementation Pipeline

```
STAGE 1: CONCEPT VALIDATION
  - Build minimum proof-of-principle test
  - Run critical-to-function experiments
  - Answer: "Does the core mechanism work?"
  - Gate: Go/No-Go based on fundamental feasibility
  - Typical budget: <5% of total project cost

STAGE 2: DETAILED DESIGN
  - Resolve ALL secondary problems (use TRIZ on them too)
  - Complete engineering calculations and simulations
  - Design for manufacturing, assembly, reliability
  - Apply AFI (Ch18) to the detailed design
  - Create full specifications and drawings
  - Gate: Design review — all contradictions resolved?

STAGE 3: PROTOTYPING & TESTING
  - Escalate prototypes: breadboard → engineering → production
  - Test under real conditions, not just nominal
  - Validate against original innovation goals (Step 3 targets)
  - Run AFI again on test results — what nearly failed?
  - Gate: Does the prototype meet innovation goals?

STAGE 4: PRODUCTION RAMP-UP
  - Tooling, process documentation, supplier qualification
  - Worker training on new processes
  - Pilot production run → full production
  - Monitor defect rates, yield, cost vs target
  - Gate: Is production stable at target quality and cost?

STAGE 5: POST-LAUNCH MONITORING
  - Track field performance, warranty claims, customer feedback
  - Compare actual vs predicted ideality improvement
  - Identify next round of contradictions to solve
  - Feed learnings back to Step 1 of Innovation Process
  - Continuous improvement loop
```

## Mental Models

- **A solution without implementation is not a solution.** Until it's in the customer's hands, delivering value, it's just an idea. The implementation phase is where most innovations die — not because the ideas were bad, but because implementation was treated as an afterthought.
- **Secondary problems are primary to someone.** The assembly complexity your solution creates? That's the assembly team's entire job. List secondary problems and solve them with the same rigor you applied to the primary problem. Don't hand off half-solved designs.
- **Implementation resistance is information, not obstruction.** When people resist a new solution, they're often pointing to real constraints: manufacturability limits, maintenance concerns, supply chain realities. Listen to resistance as design feedback, not personal opposition.
- **Prototypes are for learning, not demonstrating.** Build the first prototype to find out what's wrong, not to prove you're right. A prototype that fails teaches more than a prototype that confirms expectations.

## Anti-patterns

- **Jumping from concept to production prototype**: Skipping the intermediate prototype stages. When it fails (and it will), you don't know whether the concept is wrong or the execution is wrong.
- **Ignoring secondary problems**: "We'll figure that out later." The secondary problems accumulate and kill the project during detailed design. Address them immediately.
- **Treating resistance as a people problem to overcome**: "They just don't get it." Often the resisters see real implementation issues. Diagnose before dismissing.
- **Over-protecting IP before validation**: Filing patents before the concept is validated wastes money on ideas that may not work. Validate first, protect second.

## Key Takeaways

1. Implementation is a structured pipeline, not a handoff — Concept → Design → Prototype → Production → Monitor
2. Every TRIZ solution creates secondary problems — list and solve them with the same rigor as the primary problem
3. Prototype escalation (thought → simulation → breadboard → engineering → production) reduces risk at each stage
4. Apply AFI to the implementation plan itself — "What could cause this implementation to fail?"
5. Organizational resistance often carries valid technical information — diagnose before dismissing
6. The Implementation Contradiction ("implement new without disrupting current") is itself a TRIZ problem
7. Post-launch monitoring closes the loop — field data feeds the next innovation cycle

## Connects To

- **Ch20 (Innovation Process)**: Implementation is Steps 8-9 of the 10-step process — the bridge from concept to production
- **Ch18 (AFI)**: Apply AFI at each implementation stage to anticipate and prevent implementation failures
- **Ch19 (TRIZ for Business)**: Resistance management uses business TRIZ principles (especially Double Principles 9-10 on preliminary action)
- **Ch11 (Problem-Solving Process)**: Secondary problems are themselves mini-TRIZ problems — use the same 5-step process on each
- **Ch05 (Ideality)**: Measure ideality improvement after implementation — did the solution actually increase the benefits/costs+harms ratio?
- **Ch21 (Customer Benefit Analysis)**: Validate that the implemented solution actually improves customer satisfaction on the targeted dimensions
