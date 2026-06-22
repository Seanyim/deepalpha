# Anti-Bias & Pre-Mortem Checklist

Use this file when executing **Step Four: Anti-Bias & Pre-Mortem**. Work through all four sections before finalizing any recommendation.

---

## Section 1: 6 Cognitive Trap Self-Checks

For each trap, explicitly state whether it is active in this analysis and how it has been mitigated.

### 1. Confirmation Bias
**Trap**: Seeking evidence that supports a pre-existing view; discounting contradictory evidence.  
**Check**: Have I actively searched for the strongest bearish case (if long) or bullish case (if short)?  
**Mitigation**: List the 3 best arguments for the *opposing* position before finalizing.

### 2. Narrative Fallacy
**Trap**: Building a compelling story that feels coherent but is not falsifiable.  
**Check**: Is every key claim in the thesis backed by quantitative evidence or Tier 1/2 sources?  
**Mitigation**: Identify which single data point, if wrong, would collapse the entire thesis.

### 3. Anchoring
**Trap**: Over-weighting the first piece of information encountered (e.g., the current stock price, a recent analyst target).  
**Check**: Was the Action Price derived *before* checking the current stock price?  
**Mitigation**: Re-run the valuation blind, then compare to market price at the end.

### 4. Recency Bias
**Trap**: Over-weighting the most recent quarter's results relative to the longer trend.  
**Check**: Does the analysis include at least 4–8 quarters of trend data, not just the latest print?  
**Mitigation**: Explicitly state the multi-year earnings/margin trajectory alongside the most recent quarter.

### 5. Authority Bias
**Trap**: Deferring to high-profile investor positions or sell-side consensus without independent verification.  
**Check**: Are conclusions based on primary analysis, or primarily on "Buffett owns it" / "consensus is bullish"?  
**Mitigation**: State which conclusions are independently derived vs. corroborated by external sources.

### 6. Sunk Cost Fallacy (for existing positions)
**Trap**: Holding or adding to a position because of prior losses/gains rather than forward-looking expected value.  
**Check**: If starting fresh today with no prior position, would the same action be taken at the current price?  
**Mitigation**: Evaluate the position as if seeing it for the first time at today's price.

---

## Section 2: 7 Financial Red Flags

Score each as 🟢 Green / 🟡 Yellow / 🔴 Red. A single Red warrants deep investigation before proceeding.

| # | Red Flag | Signal to Look For | Rating |
|---|----------|--------------------|--------|
| 1 | Revenue quality deterioration | Rising DSO, deferred revenue decline, one-time items boosting revenue | |
| 2 | GAAP vs. Non-GAAP gap widening | Non-GAAP adjustments growing faster than revenue; SBC >15% of revenue | |
| 3 | FCF disconnecting from earnings | Operating cash flow consistently below net income; rising accrual ratio | |
| 4 | Guidance credibility breakdown | Management has missed guidance 2+ consecutive quarters | |
| 5 | Insider selling acceleration | Multiple executives selling via non-10b5-1 plans; CEO selling >10% of holdings | |
| 6 | Balance sheet deterioration | Net debt rising rapidly; interest coverage ratio <3x; covenant risks | |
| 7 | Auditor / accounting changes | Auditor switch, restatements, changes in revenue recognition policy | |

---

## Section 3: 5 Tech Stock Blind Spots

These are failure modes specific to technology investing. Check each explicitly.

### 1. AI Revenue Inflation
Many companies claim "AI revenue" that is actually repackaged existing SaaS or usage fees. Verify:
- Is AI revenue separately disclosed and defined?
- Is it recurring or one-time (pilots, professional services)?
- What % of total revenue does it represent, and is it growing?

### 2. Platform Risk Underestimation
Tech companies often depend on platforms (Apple App Store, Google Search, AWS, Salesforce AppExchange) for distribution or infrastructure. Verify:
- What % of revenue or users come through a single platform?
- Has the platform provider made moves that compete with or disadvantage this company?

### 3. Moat Misidentification
"Network effects" and "switching costs" are commonly claimed but rarely verified. Demand evidence:
- Net Dollar Retention >120% (real switching cost signal)
- Churn rate trends over multiple years
- Customer references citing specific reasons for staying vs. competitive pressure

### 4. TAM Arithmetic Abuse
Large TAMs are often cited without credible penetration paths. Stress-test by:
- Working bottom-up from current customer count × ACV expansion potential
- Comparing to actual market share gains in the past 3 years
- Identifying who the company is specifically taking share *from*

### 5. Management Hype vs. Execution Gap
Flashy vision without operational follow-through. Check:
- Has the company hit its own 2-year-ago guidance?
- Are product launch timelines consistently slipping?
- Is headcount growth (a leading indicator) aligned with revenue guidance?

---

## Section 4: Pre-Mortem Analysis

**Assume it is 18 months from now. The position has lost 40–50%. Write the post-mortem.**

Answer these questions *before* taking the position:

### If Long — Failure Path:
1. What specific assumptions in the bull thesis proved incorrect?
2. Which Key Force reversed or failed to materialize?
3. Was the failure foreseeable from data available today? What was being ignored?
4. At what price/signal should the position have been exited?

### If Short — Failure Path:
1. What did the bull case get right that the short thesis missed?
2. Which catalyst failed to materialize, or took longer than expected?
3. Did a macro tailwind (liquidity surge, sector rotation) overwhelm the fundamental short?
4. At what price/signal should the short have been covered?

### Kill Conditions (define before entry)
State 2–3 explicit, quantifiable conditions that would force an exit regardless of conviction:

| Kill Condition | Metric | Threshold |
|---------------|--------|-----------|
| Example: Revenue growth stalls | QoQ revenue growth | Drops below X% for 2 consecutive quarters |
| Example: Margin compression | Operating margin | Falls below X% |
| Example: Moat breach | NDR | Drops below 100% |

**Rule**: If a Kill Condition is met, the position is reassessed within 72 hours. Conviction is not a substitute for evidence.

---

## [deepalpha extension] Result-validation & backtest discipline

Before emitting the Signal Block, run a quick self-audit (from InvestSkill result-validator + claude-trading-skills backtest-expert):

**Result validation**
- **Data quality** — every key figure dated & sourced? primary (SEC) vs scraped flagged? any stale (>2wk) prices?
- **Methodology** — right module(s) fired? thresholds applied consistently? math checked (sizing arithmetic, multiples)?
- **Signal consistency** — do the modules agree? If TECHNICAL says buy but VALUATION says rich and FLOW says distribution, **lower confidence** and say why — don't paper over contradictions.
- **Disconfirmation** — what would the smartest bear say? Did I look for it, or just confirm the prior?

**Backtest / strategy discipline** (when a *rule* or *system* is proposed, not a single name)
- Realistic assumptions: slippage, transaction costs, survivorship bias removed, out-of-sample / walk-forward validation. Beware curve-fitting (too many parameters, suspiciously clean equity curve). A backtested edge that ignores costs is not an edge.

If the audit weakens the case, downgrade Confidence/Conviction in the Signal Block rather than hiding it.
