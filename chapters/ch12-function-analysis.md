# Chapter 12: Getting to Grips with Your Problems with Function Analysis

## Core Idea
Function Analysis breaks any complex, messy system into a visual map of binary Subject-Action-Object relationships, revealing every harm, insufficiency, and excess as a discrete, solvable problem that connects directly to the TRIZ Standard Solutions.

## Frameworks Introduced

- **Function Analysis (the Process)**:
  - When to use: for any difficult or messy problem where understanding the situation is as important as finding solutions. Essential when the team disagrees about root causes, when problems are interconnected, or when you need to communicate issues to non-specialists. Also critical before applying the Standard Solutions.
  - How: six steps: (1) List all components (system + environmental). (2) Create a table of all interactions -- identify whether each component could physically touch or directly interact with each other component. (3) Draw the Function Map -- place components on sticky notes first, position physically close components near each other, draw Subject-Action-Object relationships. (4) List all problems (every insufficient, excessive, harmful, or missing action). (5) Prioritize and solve: trim first, then apply Standard Solutions to harms/insufficiencies; for useful+harmful pairs, identify contradictions. (6) Take the new improved system and repeat.

- **Function Map (the Diagram)**:
  - When to use: to communicate system behavior visually at a glance, to engage non-specialists, and to focus problem-solving attention on the most problematic areas.
  - How: draw components as shapes (rectangles/ovals for system components you control; hexagons for environmental components you cannot change). Connect with lines showing four interaction types:
    - **Useful actions**: solid line (green in color).
    - **Insufficient useful actions**: dotted line.
    - **Excessive useful actions**: double line or double arrowheads.
    - **Harmful actions**: wavy line (red in color).
    - **Missing useful actions** (optional): different dashes or blue -- treat as insufficient actions so insufficient they do not yet exist.

- **Subject-Action-Object Logic**:
  - When to use: every time you define a function, to ensure functional thinking rather than tautological or colloquial description.
  - How: The subject is the thing performing the action. The object is the thing being changed. The action is what changes the object. The function is "action + object" together. Critical rule: the verb must differ from the subject or object -- "printer prints paper" is tautological and creates psychological inertia; "printer marks paper" is correct functional language. Also: the object must genuinely be changed. "I love George Clooney" is not a functional description because George Clooney is not changed by your love; "George Clooney inspires love in you" is correct (you are the object, you are changed).

- **Prime Function**:
  - When to use: to anchor the Function Analysis to the system's fundamental purpose, and to choose the correct level for analysis.
  - How: write as a Subject-Action-Object -- what your system exists to deliver. The object of the Prime Function is the "main object" -- what is intended to be changed by the system. Example: for an ICU, the Prime Function is "doctors and nurses treat patient" -- the patient is the main object.

## Key Concepts

- **Function Analysis**: the process of understanding your system by focusing on its functions -- what each component does to each other component -- mapping both useful and harmful interactions.
- **Function Map**: the visual diagram showing all components, their interactions, and all problems (harms, insufficiencies, excesses). A snapshot at one moment in time.
- **Subject-Action-Object (SAO)**: the fundamental building block -- a subject performs an action on an object, and the object is changed. The function is the action+object pair (e.g., "treat patient").
- **System Components**: components you control, depicted as white rectangles or ovals.
- **Environmental Components**: components that interact with your system but you cannot change (e.g., gravity, seawater, a user), depicted as hexagons. Essential to include because they affect your system and reveal opportunities to improve the parts you can control.
- **Main Object**: the target of the Prime Function -- what is intended to be changed by the system. Everything else in the Function Analysis should ultimately contribute to delivering the Prime Function on the main object.
- **Inherent Features**: recursive actions on a single component (e.g., a dog is inherently "territorial," "affectionate," or "aggressive"). These carry useful information about inherent qualities of components.
- **TRIZ Function Analysis vs. Value Engineering Function Analysis**: TRIZ Function Analysis maps ALL problems (not just a perfect-world ideal) and connects directly to the Standard Solutions. It is a simplified form of Substance-Field Analysis from classical TRIZ.

## Mental Models

- Use "every harm is an opportunity" when looking at a completed Function Map -- three of the four interaction types are problems (insufficient, excessive, harmful). A map full of red wavy lines looks alarming, but each red line is a specific, binary problem you can solve with the Standard Solutions.
- Use "start at high level, zoom in later" when scoping a Function Analysis -- it is easy to add detail but hard to remove it. A high-level map shows where the biggest problem clusters are, helping you choose where to focus a more detailed sub-analysis. Never mix levels within a single Function Analysis.
- Use "the object must be changed" as a litmus test when writing SAO statements -- if the object is not genuinely affected by the action, reverse the relationship or find a different verb. This discipline alone produces insight: "heart monitor measures heart rate" is wrong (the heart rate is not changed by the monitor); "patient's heart rate informs monitor" is correct.
- Use "the red tangle heuristic" when prioritizing -- look for components at the center of many red (harmful) arrows. Tackling those components first, or trimming them out, will have the greatest systemic impact.

## Anti-patterns

- **Tautological function descriptions**: "printer prints paper" reinforces psychological inertia. Use a different verb from the component name: "printer marks paper."
- **Mixing levels in a single Function Analysis**: including both "insulin molecule moves into cell" and "healthcare system treats diabetes" in the same map creates confusion. Choose one level and stay there; create separate maps for different levels if needed.
- **Ignoring environmental components**: things you cannot control (users, weather, regulations) affect your system. Mapping their interactions shows you how to improve the parts you CAN control to mitigate their impacts.
- **Focusing only on the biggest contradiction**: a Function Analysis often reveals that the primary contradiction is only part of the problem -- many harms and insufficiencies exist alongside it. Solving all of them creates a more robust system.
- **Jumping to solutions before listing all problems**: the power of Function Analysis comes from creating a complete problem list first, then solving each one systematically. Skipping the list means missing opportunities.
- **Removing components without transferring their useful functions**: when trimming, people often resist because they list everything a component does. Capture all its useful functions and transfer them to other components before removing it. The Function Analysis makes this possible and visible.

## Worked Example

The author uses an Intensive Care Unit (ICU) as the primary worked example:

1. **Components identified**: doctors, nurses, patients, monitors (heart rate, blood pressure, breathing), ventilators, alarms, conversations, traffic noise.

2. **Key interactions mapped**:
   - Doctors and nurses **treat** patient (useful -- the Prime Function).
   - Monitors **inform** doctors and nurses of patient status (useful).
   - Alarms **notify** doctors and nurses (useful) but also **waken** patient (harmful).
   - Doctors and nurses **talk** to each other -- useful for sharing information and teamwork (which improves patient outcomes) but also **disturb** patient (harmful).
   - Ventilator **helps** patient breathe (useful) but also **creates** noise (harmful).
   - Traffic noise **disturbs** patient (harmful).

3. **What the Function Map reveals at a glance**: the ICU is a very noisy place, which is bad for patients (sleep is essential for recovery). However, the noise occurs as a side effect of useful actions -- the information from machines and staff must be captured. The map shows multiple components all contributing to one harm (waking/disturbing the patient), meaning a multi-pronged solution approach is needed.

4. **Contradiction example**: doctor treats patient is both useful AND harmful (wakens patient). This is a Physical Contradiction (want the doctor to treat AND not treat the patient). Could be solved by separating in Time (treat only at certain times) -- but this is hard because "treat patient" is the Prime Function and constraints may make complete resolution impossible. However, zooming in on specific treatment actions (injecting, washing, rolling to prevent pressure sores) reveals different harms that can be mitigated individually, leaving the Prime Function intact.

5. **Problem-solving sequence**: trim first -> apply Standard Solutions to each harm and insufficiency -> solve contradictions where useful + harmful actions appear together -> redraw the Function Map for the new system -> repeat.

## Key Takeaways
1. Function Analysis turns a messy situation into a series of simple binary Subject-Action-Object relationships -- big, intimidating problems become lists of small, well-defined problems you can solve one by one.
2. Every SAO statement must pass the "object is changed" test -- this discipline alone generates deep insight about how your system actually works, often revealing misunderstandings that have persisted for years.
3. Three of four interaction types are problems (insufficient, excessive, harmful) -- a Function Map is therefore a map of opportunities for improvement, not just a description.
4. Environmental components (things you cannot change) must be included because they reveal how to improve the parts of the system you DO control.
5. A Function Map communicates instantly to non-specialists -- the author's team used one so simple "even a politician could understand it at a glance" for a military regulatory system.
6. When trimming components, the Function Analysis captures every useful function so they can be transferred elsewhere -- this gives the team confidence to remove things without losing benefits.
7. Start high level, focus on the Prime Function, and zoom in only where the map shows dense clusters of red (harmful) arrows.
8. Repeat the Function Analysis on your improved system -- each iteration takes you further toward the ideal in relatively little time.

## Connects To
- **Ch 3 (Contradictions)**: when a Function Analysis reveals useful+harmful action pairs on the same Subject-Object, you have a contradiction -- use the 40 Principles or Separation Principles.
- **Ch 11 (Problem-Solving Process)**: Function Analysis is Stage 3 of the Oxford TRIZ process -- the critical "define the problem" stage that determines which solution tools to apply.
- **Ch 13 (Standard Solutions)**: Function Analysis connects directly to the Standard Solutions -- each insufficient or harmful SAO relationship points to a specific class of Standard Solution.
- **Ch 14 (Trimming)**: the first solution tool to apply after Function Analysis; the Function Map shows exactly which components carry the most harms and are therefore the best candidates for removal.
- **Concept: Substance-Field Analysis (Su-Field)**: TRIZ Function Analysis is a simplified form of classical Su-Field analysis; both connect identified problems to the Standard Solutions.
- **Concept: Value Engineering Function Analysis**: other forms of FA map a "perfect world" system; TRIZ Function Analysis additionally maps ALL problems, making it more rigorous for problem solving.
