# Chapter 21: Customer Benefit Analysis

## Core Idea
Customer Benefit Analysis (from Livotov's TRIZ Handbook) is a systematic method for identifying what customers ACTUALLY value — as opposed to what engineers THINK they value. It maps customer needs onto importance and satisfaction axes, revealing the highest-leverage innovation opportunities: features that are highly important to customers but currently poorly satisfied. This ensures TRIZ problem-solving effort is directed at what matters most.

## Frameworks Introduced

- **Importance-Satisfaction Matrix**: A 2×2 grid plotting customer needs by importance (how much customers care) vs satisfaction (how well current solutions perform).
  - When to use: Early in any innovation project; before applying TRIZ problem-solving tools; when prioritizing which features to improve; when evaluating competitive position.
  - When NOT to use: When customer needs are already well-understood and validated with data. For pure technology-push innovations with no existing customers.

- **Customer Benefit Profile**: A structured decomposition of the customer experience into discrete benefit dimensions, each rated for importance and current satisfaction.
  - When to use: When customer needs are complex and multi-dimensional; when different customer segments may have different priorities.

- **Benefit Gap Analysis**: Identifying the specific gaps where improvement would create the most customer value — the "innovation sweet spots."
  - When to use: To prioritize TRIZ problem-solving effort across multiple potential improvement areas.

## Key Concepts

- **Importance (I)**: How much does the customer care about this benefit? Rated 1-10. NOT the same as what engineers think is important — must be validated through customer research.
- **Satisfaction (S)**: How well does the current solution (yours AND competitors') deliver this benefit? Rated 1-10. Low satisfaction on high-importance items = innovation priority.
- **Benefit Gap**: I - S for each dimension. Large positive gaps (high importance, low satisfaction) are the priority targets for TRIZ problem-solving.
- **Overshoot Zone**: High satisfaction + low importance = you're over-investing. Resources should be trimmed here.
- **Competitive Parity Zone**: High satisfaction + high importance = you're meeting expectations. Maintain, don't invest heavily.
- **Innovation Sweet Spot**: Low satisfaction + high importance = the highest-ROI innovation targets. This is where TRIZ tools should be focused.
- **Irrelevance Zone**: Low satisfaction + low importance = neither you nor customers care. Ignore unless trends suggest importance will rise.

## The Importance-Satisfaction Matrix

```
                HIGH IMPORTANCE
                      │
     ┌────────────────┼────────────────┐
     │                │                │
     │  INNOVATION    │  COMPETITIVE   │
     │  SWEET SPOT    │  PARITY ZONE   │
     │  (Priority #1) │  (Maintain)    │
     │                │                │
LOW  ├────────────────┼────────────────┤ HIGH
SATIS-│                │                │ SATIS-
FACTION│  IRRELEVANCE  │  OVERSHOOT     │ FACTION
     │  ZONE          │  ZONE          │
     │  (Ignore)      │  (Trim)        │
     │                │                │
     └────────────────┼────────────────┘
                      │
                LOW IMPORTANCE
```

## Process: Customer Benefit Analysis in 5 Steps

```
Step 1: IDENTIFY BENEFIT DIMENSIONS
  - List all aspects of the product/service that customers might value
  - Use Function Analysis to decompose the system into benefit-delivering functions
  - Segment by customer type if different segments value different things
  
  Example (eVTOL aircraft):
  - Range, speed, noise level, safety perception, cabin comfort, 
    operating cost, charging time, reliability, aesthetics, 
    accessibility, environmental impact, price

Step 2: MEASURE IMPORTANCE (I)
  - Survey/interview target customers
  - Rate each dimension 1-10 for importance
  - Use forced ranking or pairwise comparison for more precision
  - Watch for: what customers SAY is important vs what their behavior REVEALS

Step 3: MEASURE SATISFACTION (S)
  - How satisfied are customers with CURRENT solutions (yours + competitors)?
  - Rate each dimension 1-10 for current satisfaction
  - Include competitor performance, not just your own
  - Watch for: customers who've never experienced better may rate poor solutions highly

Step 4: CALCULATE GAPS & PLOT MATRIX
  - Gap = I - S for each dimension
  - Plot on 2×2 matrix (median split or absolute thresholds)
  - Sort by gap size — largest gaps = top priorities

Step 5: TRANSLATE GAPS TO TRIZ PROBLEMS
  - For each priority gap: "How to increase satisfaction on [dimension] 
    without increasing cost/complexity?"
  - This becomes the TRIZ problem statement
  - Feed into Contradiction Matrix or other TRIZ tools
```

## Worked Example: Smartphone Camera Innovation

**Step 1 — Benefit Dimensions**: Photo quality (day), photo quality (night), video quality, zoom capability, portrait/bokeh, camera app speed, camera app ease-of-use, lens durability, flash quality, selfie quality, size/thinness of phone

**Step 2-3 — Measure I and S** (hypothetical survey data):

| Dimension | Importance (I) | Satisfaction (S) | Gap (I-S) |
|-----------|---------------|------------------|-----------|
| Night photo quality | 9.2 | 4.5 | **+4.7** |
| Zoom capability | 8.1 | 5.0 | **+3.1** |
| Camera app speed | 7.8 | 6.5 | +1.3 |
| Portrait/bokeh | 6.5 | 8.0 | -1.5 |
| Lens durability | 5.0 | 9.0 | -4.0 |

**Step 4 — Matrix Placement**:
- **Sweet Spot** (High I, Low S): Night photo quality, Zoom capability ← INVEST HERE
- **Overshoot** (Low I, High S): Lens durability ← TRIM investment
- **Parity** (High I, High S): Camera app speed ← MAINTAIN
- **Irrelevance** (Low I, Low S): Flash quality ← IGNORE

**Step 5 — TRIZ Problem Statement**:
"How to improve night photo quality (satisfaction 4.5 → 8.0+) without increasing component cost or phone thickness?"

This feeds into the Contradiction Matrix: improving "image quality" (Parameter 29) without worsening "weight of moving object" (Parameter 1) or "device complexity" (Parameter 36).

## Mental Models

- **Your customers don't care about your technology — they care about what it does for them.** The benefit dimensions must be stated in customer language ("photos look great at night") not engineering language ("improved low-light SNR by 3dB").
- **What you're best at might not matter.** Overshoot zone items are often the ones engineers are most proud of — because they've been optimized for years. The discipline is to stop improving things customers don't value.
- **Importance is revealed, not stated.** Customers say "battery life is important" but buy the thinner phone. Behavioral importance data (purchase decisions, usage patterns) is more reliable than survey importance data.
- **The biggest gap is your best opportunity.** Don't start with what's technically interesting — start with what has the largest I-S gap. Let customer value pull the innovation, not technology push.

## Anti-patterns

- **Engineers rating importance instead of customers**: The #1 failure mode. Engineers systematically mis-rank customer priorities. Always validate with actual customer data.
- **Rating your own satisfaction instead of market satisfaction**: If competitors satisfy a need better, YOUR satisfaction score is irrelevant. The gap is measured against the best available alternative.
- **Too many benefit dimensions**: Beyond 15-20 dimensions, the analysis becomes noise. Aggregate and prioritize the dimensions themselves.
- **Treating the matrix as static**: Importance shifts over time (what was "delight" becomes "expected"). Re-run the analysis periodically.

## Key Takeaways

1. Customer Benefit Analysis ensures TRIZ effort targets what customers ACTUALLY value
2. The 2×2 matrix classifies every benefit dimension into one of four zones: Sweet Spot, Parity, Overshoot, Irrelevance
3. Innovation Sweet Spot = High Importance + Low Satisfaction — this is where TRIZ effort has the highest ROI
4. Overshoot Zone = Low Importance + High Satisfaction — stop investing here; trim instead
5. Measure importance and satisfaction from customer perspective, not engineer perspective
6. Translate each priority gap into a specific TRIZ problem statement before applying problem-solving tools
7. The process integrates directly with the 10-step Innovation Process (Steps 2-3)

## Connects To

- **Ch12 (Function Analysis)**: Function Analysis decomposes the system into functions; Customer Benefit Analysis maps those functions to customer value
- **Ch05 (Ideality)**: The ideality equation (Benefits / Costs+Harms) aligns with the I-S matrix — improve satisfaction on high-importance dimensions
- **Ch14 (Trimming)**: Overshoot zone items are prime candidates for trimming — remove investment in things customers don't value
- **Ch20 (Innovation Process)**: Customer Benefit Analysis feeds Steps 2 (Diagnosis) and 3 (Goal Setting) of the 10-step process
- **Ch19 (TRIZ for Business)**: Business Ideality uses customer value as the numerator of the ideality equation
