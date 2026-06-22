# Valuation Models Reference

Use this file when executing **Module K: Valuation Matrix**. Select at least 2 methods; 3–4 is recommended. Match the method to the company profile.

---

## Method Selection Guide

| Company Profile | Primary Method | Secondary Method |
|----------------|---------------|-----------------|
| Profitable, mature | Owner Earnings, EV/EBITDA | PEG, Reverse DCF |
| High-growth, profitable | PEG, Reverse DCF | EV/EBITDA, Earnings Yield + ROIC |
| High-growth, unprofitable or marginal | EV/Revenue + Rule of 40, Reverse DCF | Comparable company PS multiples |
| Cyclical | EV/EBITDA (normalized earnings) | Replacement cost |

---

## Method Definitions

### 1. Owner Earnings (Buffett method)
`Owner Earnings = Net Income + D&A + Other Non-Cash Charges − CapEx (maintenance) − Working Capital Increases`
- Capitalize at an appropriate discount rate (typically 8–12% for quality businesses)
- Use normalized earnings over a cycle, not peak or trough
- Best for mature, capital-light businesses with stable FCF

### 2. EV/EBITDA
- Compare against 3–5 direct peers on trailing and forward EV/EBITDA
- Adjust for differences in growth rate, margin profile, and capital intensity
- Apply premium/discount with explicit rationale
- For cyclicals: use normalized (mid-cycle) EBITDA, not spot

### 3. PEG Ratio
`PEG = Forward P/E ÷ (5-year EPS CAGR expressed as a whole number)`
- Use the growth rate as a number, not a decimal: a 20% CAGR is **20**, so P/E 25 → PEG 1.25.
- PEG <1 = potentially undervalued relative to growth; >2 = likely expensive
- Most useful for profitable growth companies with earnings visibility
- Limitation: sensitive to earnings estimate accuracy

### 4. Reverse DCF (most rigorous for growth stocks)
Work backwards from the current stock price to determine what growth rate is implied:
1. Set WACC (typically 8–12%)
2. Set terminal growth rate (typically 2–4%)
3. Solve for the revenue/earnings CAGR that justifies the current price
4. Ask: "Is this implied growth rate achievable, conservative, or heroic?"
5. Build bull/base/bear scenarios and map to price targets

**Iron rule**: Long position requires ≥15% IRR in base case. Short requires ≥20–25%.

### 5. EV/Revenue + Rule of 40
`Rule of 40 = Revenue Growth Rate (%) + FCF Margin (%)`
- Score >40: healthy SaaS business
- Score >60: exceptional
- Use EV/Revenue multiple benchmarked against Rule of 40 score vs. peers
- Plot company on a "Rule of 40 vs. EV/Revenue" scatter chart vs. peer set

### 6. Comparable Company Multiples (Comps)
- Select 5–8 true peers (similar business model, growth, margins, geography)
- Compile: EV/EBITDA, EV/Revenue, P/E, P/FCF — trailing and forward
- Derive implied range for the subject company
- State premium/discount thesis explicitly: why does this company deserve to trade at X vs. the peer median?

### 7. SOTP (Sum of the Parts)
- Use when the company has 2+ distinct business segments with different growth/margin profiles
- Value each segment independently using the most appropriate method per segment
- Sum segment values; subtract net debt; divide by diluted shares
- Useful for conglomerates, holding companies, or companies with embedded "hidden" assets

### 8. Replacement Cost / Liquidation Value
- What would it cost a rational buyer to rebuild this business from scratch?
- Most relevant for asset-heavy companies or deep value situations
- Provides a hard floor on valuation

---

## Sensitivity Analysis

Always produce at least one two-dimensional sensitivity table. Common axes:

| Axis A | Axis B |
|--------|--------|
| Revenue CAGR (3 scenarios) | Terminal FCF margin |
| WACC | Terminal growth rate |
| EV/EBITDA multiple | EBITDA margin expansion |
| NDR assumption | New logo growth rate |

---

## Probability-Weighted Scenario Template

| Scenario | Probability | Key Assumption | Implied Price | IRR |
|----------|-------------|---------------|--------------|-----|
| Bull | 25% | | | |
| Base | 50% | | | |
| Bear | 25% | | | |
| **Weighted Average** | 100% | | | |

**Minimum thresholds**: Long ≥15% IRR (base case). Short ≥20–25% IRR.

---

## Action Price Derivation (K6)

Follow this sequence strictly:
```
1. Independent valuation (your model, not consensus)
2. Derive fair value range (bull/base/bear weighted)
3. Apply margin of safety (typically 20–30% for growth; 30–40% for uncertain businesses)
4. Set Action Price = fair value × (1 − margin of safety)
5. Compare Action Price to current stock price
6. State the gap: "Stock is X% above/below Action Price"
```

Never anchor Action Price to the current stock price. Derive it independently first.

---

## [deepalpha extension] Triangulated fair value (three methods → one band)

Never rely on a single number. Triangulate, then show a **football-field band** (bear–base–bull) vs current price.

1. **DCF (intrinsic).** Project FCF, discount at WACC, terminal value (Gordon or exit multiple). Report a **WACC × g sensitivity grid**; Bear/Base/Bull on growth, margins, terminal assumptions.
2. **Reverse DCF (expectations).** Solve for the growth the *current price* implies; compare to plausibility and estimates. The cleanest "is the market too optimistic?" test.
3. **Relative / comps.** P/E, P/S, EV/EBITDA, EV/Sales, FCF yield vs peer set (SEC SIC peers) **and** vs the name's own history. Justify any premium/discount (growth, margins, moat).
4. **SOTP (segmented businesses).** Value each segment on its own multiple, sum, subtract net debt.

Output: a fair-value range, implied upside/downside vs price, the most-wei