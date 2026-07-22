# Chapter 13: Solving Problems using the TRIZ Standard Solutions

## Core Idea
The 76 Standard Solutions are a library of proven inventive answers from patent analysis, organized by problem type (harm, insufficiency, measurement/detection) rather than solution type -- you model your problem as a Subject-action-Object, look up the relevant class, and then turn the conceptual suggestion into a concrete solution using your domain expertise.

## Frameworks Introduced
- **Subject-action-Object (SaO) Model**: the fundamental unit of problem definition for accessing the Standard Solutions.
  - When to use: any time you need to apply Standard Solutions, or when you want to decompose a complex system into manageable problem units.
  - How: identify the Subject (component delivering the action), the Action (a "doing word" or change), and the Object (component changed by the action). Get Subject and Object the right way round per the Trimming Rules.

- **Oxford TRIZ Standard Solutions Classification**: reorganizes the classical five-class system into three problem-driven classes.
  - When to use: after completing a Function Analysis and identifying which SaOs are harmful, insufficient, or excessive.
  - How: pick one problematic SaO, look up the relevant class (H1-H4 for harm, i1-i2-i.a. for insufficiency, M1-M5 for measurement/detection), read each solution aloud substituting your specific SaO, and brainstorm concrete implementations.

- **Steps for Applying Standard Solutions**:
  1. Complete Function Analysis (or define a single SaO for fast problem solving).
  2. Pick a place to start: near the Prime Function, components with many problems, or components with low Ideality.
  3. Try Trimming first (the most radical approach).
  4. Pick one harmful, insufficient, or excessive action.
  5. Look up the relevant Standard Solutions and read them out loud, replacing the generic SaO with yours.
  6. Brainstorm new ideas from each solution suggestion.
  7. Combine multiple solutions into a better overall system.
  8. Repeat with the improved system.

## Key Concepts
- **Standard Solutions**: 76 simple lists of solution directions derived from patent analysis, organized by problem type -- they tell you what to do conceptually, and your expertise turns that into a specific idea.
- **Subject-action-Object (SaO)**: the atomic description of one interaction in a system. The Subject delivers the action; the Object is changed by it.
- **Prime Output**: the main purpose your system exists to deliver -- the one thing you most want to achieve.
- **Harm**: any output you don't want, including excessive useful actions and risks that could manifest. Treated identically because unwanted output always requires input you are paying for.
- **Insufficient useful action**: delivers something you want but not enough of it. Mark borderline cases as insufficient to force yourself to find improvement opportunities.
- **Missing action**: a useful action you want but that does not currently exist in the system. Treated the same as an insufficient action (just insufficient to the point of non-existence).
- **Super-system**: everything outside your system boundary -- the environment and surrounding context that Standard Solutions frequently prompt you to use.
- **Function Analysis**: the process of modeling every interaction in your system as SaOs, producing a Function Map that reveals all problems, component relationships, and improvement opportunities.
- **H2.1-H4.3 numbering**: each Standard Solution has a letter for problem class (H/i.a./M), a digit for category, and a digit for the specific solution -- e.g., H2.3 means "Harm, Block category, solution 3: change zone/duration."
- **Prism of TRIZ**: the mental model of stepping through from a real-world problem to a conceptual model (SaO/Function Map) to a conceptual solution (Standard Solution suggestion) and back to a real-world implementation -- moving from specific to abstract to specific.

## Mental Models
- Use the "Problem-as-Interaction" model when you are overwhelmed by a complex system: reduce every issue to one Subject-action-Object so you can solve problems one at a time rather than grasping the whole situation at once.
- Use the "Radical-First Gradient" when applying any Standard Solution class: each class starts with the most radical suggestion (e.g., eliminate the need to measure entirely) and progresses to less radical ones. Attempt the boldest change first; only settle for smaller changes when the big one proves impossible.
- Use the "Read It Aloud" technique when a Standard Solution seems abstract: literally substitute the words of your SaO into the generic solution text and speak it -- this triggers concrete thinking that reading silently often misses.
- Use "Combine and Re-trim" when you have generated many solution ideas: the best systems come from combining multiple solutions, then running the process again on the improved system to discover further opportunities.

## Anti-patterns
- **Applying Standard Solutions without an SaO**: without defining the Subject and Object precisely, the solutions offer only approximate directions because you have nothing to apply them to specifically.
- **Getting bogged down on one solution**: with 24 harm solutions, 35 insufficiency solutions, or 17 measurement solutions available, some will fit better than others. Keep moving rather than struggling with a single suggestion -- solutions start overlapping and interconnecting.
- **Avoiding identifying problems**: if you are unsure whether an action is useful or insufficient, err on the side of marking it insufficient. This prompts you to find improvements; you can always decide later that none are needed.
- **Treating measurement as an end in itself**: measuring is rarely the real outcome you want -- it is a proxy for monitoring performance to enable changes. The most inventive approach is making the system self-adjusting so no measurement is needed at all.

## Worked Example
The author works through improving a toilet brush using the insufficiency Standard Solutions:

**Step 1**: Function Analysis of the toilet brush system. The Prime Function is "brush - moves - debris" (insufficient).
**Step 2**: Start near the Prime Function (the brush).
**Step 3**: Trim the subject -- as a toilet brush designer, you may not want to remove the brush entirely, so move to other Standard Solutions.
**Step 4**: Pick the insufficient Prime Function SaO: improve "brush - moves - debris".
**Step 5**: Apply Standard Solutions:
- **i1.1** (Add something to subject or object): make the handle hollow and add bleach that auto-dispenses during use.
- **i1.3** (Use external environment): vibrate the toilet bowl, add a "cleaning" flush setting, or make a non-stick bowl.
- **i1.4** (Change surroundings): add something to cistern water that loosens debris.
- **i2.1** (Segment): fragment bristles into more numerous thinner ones or add micro-bristles on each bristle tip.
- **i2.2** (Introduce voids/fields/foam): create a foaming bleach or detergent.
- **i2.10** (Deliver exactly what's needed in time/space): disposable toilet brush -- bristles exist only when cleaning, eliminating the dirty brush-in-holder problem.
- **i.a.2** (Add another action from existing components): add a water jet from the brush (water is available as a resource).
- **i.a.4** (Change uniform action to patterned): vibrate the bristles, analogous to an electric toothbrush -- or create a sonic toilet brush.

**Step 6**: Combine ideas: a vibrating toilet brush that sprays water/detergent from the handle and has micro-bristles.

A second worked example applies the Harm Standard Solutions to ICU noise: H2.1 (counteract with opposing field -- white noise improves sleep by ~40%), H2.3 (change zone/duration -- quiet times, private rooms), H2.4.1 (insulate -- ear plugs improve sleep by ~25%), H2.7 (protect parts -- separate critically ill from recovering patients), H2.8 (weaker action enhanced locally -- soundproofed staff offices in the ward), H2.9 (use sub-systems -- light alarms instead of audible ones), H2.10 (use environment -- soundproofing materials in walls, lowered ceilings).

## Key Takeaways
1. Always define your problem as a Subject-action-Object before applying Standard Solutions -- the SaO is the minimum unit that makes the solutions precise and effective.
2. The 76 Standard Solutions are organized by the kind of problem you have, not the kind of solution: Harm (24), Insufficiency (35), Measurement/Detection (17) -- look up solutions based on what is wrong.
3. Start with the most radical suggestion in each class (trim the cause, eliminate measurement entirely) and work down to less radical ones only if the bold approach is blocked by constraints.
4. Work through problems one SaO at a time on a Function Map -- this makes complex problem solving manageable by decomposing it into a series of small, well-defined tasks.
5. Read Standard Solutions out loud, substituting your specific SaO words into the generic text -- this simple technique dramatically improves idea generation.
6. Combine multiple Standard Solution ideas into one improved system, then re-apply the process to the improved system for even better results.
7. Standard Solutions regularly prompt you to look beyond your system boundary to the super-system and environment -- inventive solutions often come from clever use of things around you.

## Connects To
- **Ch 14**: Trimming (H1) is the first and most radical harm solution -- Ch 13 tells you to start with Trimming; Ch 14 teaches you how to do it systematically.
- **Ch 12**: Function Analysis produces the SaO models that Standard Solutions require as input -- the two tools are designed to work together as a complete problem-definition-to-solution pipeline.
- **Ch 5**: Resources are frequently prompted by Standard Solutions (especially i1.3, i1.4, H1.4) -- Ch 5 provides the systematic method for capturing all available resources.
- **Ch 4**: Trends of Technical Evolution -- the insufficiency solutions (i2, "Evolve the subject and object") directly map to Trend stages, connecting problem solving with technology forecasting.
- **Ch 6**: Effects Database -- when Standard Solutions suggest adding a field or function, the Effects Database provides the specific scientific effects to implement it.
- **Su-Field Analysis (Classical TRIZ)**: the classical five-class system (Build/Destruct, Strengthen, System Transition, Detection/Measurement, Helpers) is the parent framework from which Oxford TRIZ's three-class system was derived; Su-Fields use Substance-Field triangles rather than SaO arrows.
