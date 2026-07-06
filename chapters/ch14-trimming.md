# Chapter 14: Trimming for Elegant, Low-Cost Solutions

## Core Idea
Trimming is the systematic TRIZ method for improving a system by removing components while retaining all their useful actions -- you transfer the functions of the removed component to other parts of the system, resources, or the environment, producing a leaner, cheaper, and often better system.

## Frameworks Introduced
- **The Trimming Rules**: six sequential questions that guide you to remove a component without losing its useful actions.
  - When to use: after completing a Function Analysis, when you want to reduce costs, eliminate harms, simplify a system, or create strong intellectual property.
  - How: for each useful action the target component delivers, ask in order:
    1. **Do we need its useful actions?** If no, trim it.
    2. **Could the object perform the useful actions itself?** If yes, trim the subject.
    3. **Could another component perform the useful actions?** If yes, trim it.
    4. **Could a resource perform the useful actions?** If yes, trim it.
    5. **Could we trim the component after its useful actions?** If yes, trim it in time.
    6. **Could we trim any harmful parts of the component?** If yes, trim it partially (in space).

- **Ideality Equation**: the TRIZ measure of system goodness, expressed as Ideality = Benefits / (Costs + Harms). Trimming improves Ideality by reducing the denominator (costs and harms) while preserving or increasing benefits.

- **Deep Trimming Process**: trim, redraw the Function Map, and trim again -- iterating until the system stops working, then step back.
  - When to use: when seeking radically innovative concepts or strong patent positions.
  - How: start with components far from the Prime Function for incremental improvement; start close to the Prime Function for radical concepts. After each trim cycle, redraw the system as a new Function Map and trim again. Stop only when removing one more component breaks the system -- then you know you have pushed as far as possible.

- **Trimming for Intellectual Property**: two strategies depending on your goal.
  - Patent circumvention: trim components closest to the Prime Function to produce a concept so fundamentally different it no longer resembles the original patent.
  - Strengthening your own patent: trim components far from the Prime Function to generate dependent claims; also simulate competitor circumvention by trimming your own system to preemptively claim alternative embodiments.

## Key Concepts
- **Trimming**: removing a component from a system while transferring all its useful functions to other components, resources, or the environment -- the opposite of traditional "add something to fix it" problem solving.
- **Ideality**: the ratio of all benefits you want to all inputs (costs) plus all unwanted outputs (harms). Higher Ideality means more benefits with fewer costs and harms.
- **Function Map**: the visual output of Function Analysis showing every Subject-action-Object relationship in the system -- the mandatory starting point for Trimming because you must know every useful action a component delivers before you can safely remove it.
- **Transferring functions**: the core mechanism of Trimming -- each useful action of the removed component is reassigned to another element (object, another component, resource, etc.), one action at a time.
- **Smuggling**: intentionally adding a new component that delivers a missing useful function, then attempting to trim that new component out -- a technique for expanding system benefits while still ending up with fewer total components.
- **Deep Trimming**: iterative Trimming that removes components increasingly close to the Prime Function, eventually asking fundamentally new questions about how the system operates and what it can offer.
- **Prime Function**: the main thing your system is designed to deliver -- Trimming close to it produces radical innovation; Trimming far from it produces incremental improvement.

## Mental Models
- Use "Transfer, Don't Lose" when someone says "we can't remove that, we need it": the Function Map proves that the component's actions can be delivered elsewhere. The component is just one way of getting those functions -- not the only way.
- Use "Trim Until It Breaks" when you are unsure if you have gone far enough: keep removing components conceptually until the system stops delivering its Prime Function, then step back. Thinking time is cheap; the last step before breakage is where the most innovative concepts live.
- Use "Trim the New Guy" when you discover a missing function that would add value: add a component to deliver it, capture that new benefit, then immediately try to trim that new component. You may end up with more benefits and fewer components.
- Use "Iterate the Trim" when initial Trimming produces good but not radical results: redraw the trimmed system as a new Function Map and trim again. What was untrimmable in the original configuration often becomes removable after the first round of Trimming changes the system's structure.

## Anti-patterns
- **Trimming without a Function Map**: if you do not know every useful action a component delivers, you will lose functionality when you remove it. The Function Map is non-negotiable preparation.
- **Stopping after one component**: Trimming is iterative. Removing one component often opens the possibility of removing others. Redraw and trim again.
- **Smuggling without trimming**: adding new components to deliver new functions is fine, but forgetting to then try to trim them out defeats the purpose of building a simpler system.
- **Starting with the hardest component for beginners**: if you are new to Trimming, start with components far from the Prime Function that have many harms and few useful actions (low Ideality). Working close to the Prime Function is for experienced practitioners seeking radical concepts.
- **Confusing trimming with cost-cutting**: indiscriminate cost-cutting removes components and their benefits together. Trimming removes components while keeping all benefits -- it is intelligent cost reduction, not austerity.

## Worked Example
The author works through Trimming a hotel mini-bar system:

**System**: A hotel mini-bar refrigerator that stores, cools, and displays high-priced drinks to guests. Harmful actions: creates noise, consumes electricity, requires daily staff replenishment, charges guests high prices.

**Step 1 -- Complete Function Analysis**: the mini-bar refrigerator is the Subject performing four useful actions on drinks and guests: stores drinks, cools drinks, informs guests, tempts guests. Problems: noise and energy use.

**Step 2 -- Pick a starting component**: the mini-bar refrigerator itself -- it has harms (noise, energy) and does not directly deliver the Prime Function (making drinks available to refresh guests).

**Step 3 -- Capture all resources**: super-system (corridors, lifts, bar, reception, staff, kitchen, local businesses), system (hotel room), sub-system (cupboards, air-conditioning, TV, information brochure), time (booking, check-in, walking to room), space (inside/outside room), harms/waste (noise, energy, expense), knowledge (staff and guest experience).

**Step 4 -- Apply the Trimming Rules to each of the four useful actions**:

| Rule | Stores Drinks | Cools Drinks | Informs Guests | Tempts Guests |
|------|--------------|--------------|----------------|---------------|
| Need it? | No -- use cupboard | No -- ambient temp drinks only | Yes | Yes |
| Object do it? | Self-contained drink packs | Self-cooling cans | Drinks on sideboard in plain view | Drinks on sideboard in plain view |
| Another component? | Check-in desk stores drinks; staff bring on request | Free room service from central fridge; ice on request | Staff inform when helping with luggage | Pre-order when booking; all-inclusive package |
| A resource? | Wardrobe/cupboard | Air-conditioning unit | TV welcome screen advertises drinks | Browse and order via TV |
| Trim after? | Disposable cardboard packaging | Chilled drinks in free cool-bag from reception | Leaflets on bed | Leaflets with daily special offers |
| Trim part? | Vending machine per floor | Smaller pre-order fridges; ice machines on each floor | Adverts in lifts | One free drink in room with purchase details |

**Result**: multiple alternative systems emerge -- from simple improvements (leaflets instead of mini-bar display) to radically different concepts (no mini-bar at all; order drinks via TV with room service from a central fridge; all-inclusive drink packages at check-in).

The author also notes the Deep Trimming principle with a torch example: starting from 13 components, first-pass Trimming reduces to 4 (LED bulb, battery, switch, housing). Second-pass Trimming on the 4-component system generates radically different concepts like a single-component bio-luminescent system that fluoresces on demand.

## Key Takeaways
1. Trimming is the first and most radical Standard Solution for dealing with harms (H1) -- remove the cause entirely rather than managing its effects.
2. The Trimming Rules are a sequence: always start by asking if the useful action is even needed (Rule 1) before trying to transfer it.
3. A Function Map is mandatory before Trimming -- you must know every useful action a component delivers so you can transfer all of them when you remove it.
4. Trimming systematically breaks the perceived connection between the functions you want and the current components delivering them -- the component is just one way, not the only way.
5. Deep Trimming (trim, redraw, trim again) produces the most innovative concepts -- trim until the system conceptually breaks, then take one step back.
6. Trimming for IP works in two directions: trim close to the Prime Function to circumvent competitors' patents; trim far from the Prime Function to build dependent claims on your own.
7. Smuggling in new components to add missing functions, then trimming them out, lets you expand benefits while still ending up with a simpler system.
8. Always list your resources before starting to trim -- knowing what is available makes the "Could a resource perform the useful action?" step fast and productive.

## Connects To
- **Ch 13**: Trimming (H1) is the first and most radical class of the Harm Standard Solutions -- Ch 13 tells you to start here; Ch 14 provides the detailed how-to.
- **Ch 12**: Function Analysis produces the Function Map that is the mandatory input to Trimming -- the two chapters form a complete "understand then simplify" workflow.
- **Ch 5**: Resource capture is explicitly required before successful Trimming -- Ch 5 provides the systematic resource categories (super-system, system, sub-system, time, space, harms, knowledge).
- **Ch 4**: Trends of Technical Evolution -- Deep Trimming often pushes a system along Trend lines (e.g., segmentation, transitioning to fields), connecting cost reduction with technology evolution.
- **Ch 9**: Ideal Outcome -- defining what you ideally want helps identify missing functions that you can smuggle in and then trim out, expanding benefits while simplifying.
- **Lean manufacturing**: Trimming provides the "how" for Lean's "what" -- when Lean identifies waste to eliminate, the Trimming Rules provide systematic ways to remove it without losing value.
