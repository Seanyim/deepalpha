
# Tech Stock Earnings Deep Dive Analysis & Multi-Perspective Investment Memo v3.0

## Positioning & Design Philosophy

Provide **institutional-grade** earnings analysis for a "large retail investor" — someone investing their own capital, no LPs, holding tech stock positions on a quarterly and annual basis.

Core principles:
- **Key Forces Driven**: Identify 1-3 decisive forces first; prioritize the 16 modules around those forces
- **Multi-Philosophy Confrontation**: Review the same dataset through 6 investment worldviews
- **Primary Evidence First**: Trace information to its source (SEC filings, CEO quotes, etc.)
- **Actionable Decisions**: Not "bullish/bearish" — "at what price, what action, what triggers an exit"
- **Quarterly Tracking**: Each module has built-in QoQ and YoY comparison frameworks

---

## Master Execution Flow

```
Step Zero : Key Forces Identification (anchor on 1-3 decisive forces)
Step One  : 16 Major Analysis Modules (A-P)
Step Two  : 6 Investment Philosophy Perspectives  →  read references/investing-philosophies.md
Step Three: Valuation Matrix                       →  read references/valuation-models.md
Step Four : Anti-Bias & Pre-Mortem                 →  read references/bias-checklist.md
Step Five : Decision Framework & Output
```

---

## Step Zero: Key Forces Identification

**Before any module analysis**, answer:

> **Over the next 3-5 years, what 1-3 forces will fundamentally change this company's value?**

Possible forces: AI/technology paradigm shift, regulatory policy, management strategic pivot, competitive landscape change, market misunderstanding of structural changes, hidden asset monetization.

**Two modes**:
- **Discovery Mode**: Quick scan of A-P summaries to identify Key Forces
- **Validation Mode**: Prioritize modules for deep/standard coverage around identified Key Forces

**Anti-pattern**: Modules directly related to Key Forces get 2-3x coverage. If the analysis reads like a checklist that "touches everything but goes deep on nothing," the Key Forces haven't been identified.

---

## Step One: 16 Major Analysis Modules (A-P)

### Evidence Tiers

| Tier | Type | Examples | Minimum |
|------|------|----------|---------|
| Tier 1 | Primary | CEO quotes, Glassdoor/Blind, G2/AppStore, GitHub activity, patents, hiring, insider transactions | ≥3 per report |
| Tier 2 | Factual | SEC filings (10-K/10-Q/8-K/DEF 14A), financial data, court documents | Core data must trace here |
| Tier 3 | Opinion | Sell-side research, news analysis, price targets | May cite; cannot be sole basis |

Never fabricate citations. If an exact quote is unavailable, paraphrase and note the source.

---

### Module A: Revenue Scale & Quality
**Core Question**: Is revenue growth "real" or "on paper"?
- A1. Revenue composition breakdown (each business line: amount, share, YoY/QoQ)
- A2. Growth trend (4-8 quarter trend line vs. Wall Street consensus)
- A3. Revenue quality (recurring %, organic vs. acquisition-driven, geographic mix, customer concentration)

### Module B: Profitability & Margin Trends
**Core Question**: Is the efficiency of making money improving or deteriorating?
- B1. Three-line margin tracking (gross / operating / net margin, QoQ and YoY)
- B2. GAAP vs. Non-GAAP variance audit (gap >50% must be investigated; SBC as % of revenue)
- B3. Earnings vs. expectations (EPS beat/miss and quality)

### Module C: Cash Flow & Capital Allocation
**Core Question**: Are profits real cash or accounting artifacts?
- C1. Cash flow quality (OCF vs. net income, FCF margin, DSO trends)
- C2. CapEx direction (allocation and historical ROI)
- C3. Capital return (buyback vs. SBC net dilution, dividends, M&A)
- C4. Balance sheet health (net cash/debt, maturity schedule, interest coverage)

### Module D: Forward Guidance & Management Signals
**Core Question**: What is management's true read on the future? Are words and actions consistent?
- D1. Guidance vs. expectations table (revenue / profit / EPS)
- D2. Cross-period comparison (guidance accuracy over past 4 quarters)
- D3. Management tone & behavior (Earnings Call key statements, tone shifts)
- D4. Anomaly signals (executive departures, accounting policy changes, auditor changes)

### Module E: Competitive Landscape & Industry Position
**Core Question**: Is the company on offense or defense?
- E1. Industry overview (TAM, CAGR, current stage)
- E2. Ranking & competitor comparison (market share, valuation multiples)
- E3. External threat assessment (cross-industry giants, open-source alternatives)
- E4. Moat status (quantifiable evidence)

### Module F: Core KPI Dashboard
**Core Question**: What are the 2-5 "thermometer" metrics for this company's business health?

| Type | Core Metrics |
|------|-------------|
| SaaS/Cloud | ARR growth, NDR (>120% excellent), RPO, Rule of 40 |
| Consumer Internet | DAU/MAU ratio, ARPU, engagement time, CAC/LTV |
| Semiconductor/Hardware | Backlog, Book-to-Bill, inventory days, Design Wins, ASP |
| Ad-Driven | Advertiser count, avg spend per advertiser, CPM/CPC trends |
| Platform/Ecosystem | Developer count, third-party apps, GMV/TPV |

### Module G: Core Products, New Business & Market Narrative
**Core Question**: How competitive is the core business? Are new growth drivers real?
- G1. Core product (real user reviews, innovation cadence, pricing power, stickiness)
- G2. New business (revenue contribution, business model validation, TAM reasonableness)
- G3. AI narrative reality check (AI revenue definition, recurring vs. one-time, pilot vs. at-scale)
- G4. Market narrative buy-in (analyst sentiment, multiple changes, falsifiable timeline)

### Module H: Core Partners & Supply Chain Ecosystem
**Core Question**: Are key relationships stable? Is there a "broken link" risk?
- H1. Key partner relationship mapping
- H2. Client-vendor dependency assessment
- H3. Wildcards (customer in-sourcing, frenemy dynamics, geopolitics, contract expirations)

### Module I: Executive Team & Corporate Governance
**Core Question**: Are these people trustworthy enough to manage your capital?
- I1. Core management backgrounds (experience, tenure, stability)
- I2. Incentive structure (compensation mix, incentive metrics, skin in the game)
- I3. Governance structure (board independence, dual-class voting, shareholder friendliness)
- I4. Landmines (related-party transactions, SEC investigations, audit committee independence)

### Module J: Macro Environment & Policy Impact
**Core Question**: Is the external environment a tailwind or headwind?
- J1. Macro impact (interest rates, liquidity, economic cycle, FX)
- J2. Policy & regulation (antitrust, AI regulation, data privacy, industry-specific)
- J3. Geopolitics (US-China, export controls, regional conflicts)

> If the user has `macro-liquidity` or `us-market-sentiment` installed, recommend using them in conjunction.

### Module K: Valuation Matrix
**Read `references/valuation-models.md` before executing this module.**
- K1. Method selection (≥2 methods, recommended 3-4)
- K2. Comparable company selection (premium/discount rationale, SOTP if applicable)
- K3. Core assumptions (base / bull / bear scenarios)
- K4. Sensitivity analysis (≥1 two-dimensional matrix)
- K5. Probability-weighted scenarios & IRR (**Iron rule: long ≥15%, short ≥20-25%**)
- K6. Action Price: `Independent valuation → Fair value range → Margin of safety → Action Price → Check vs. current price`

### Module L: Ownership Distribution & Position Structure
**Core Question**: Who is buying, who is selling, what is the long/short force balance?
- L1. Ownership structure (founder, executive, top-10 institutional changes)
- L2. Capital flows (13F data, notable fund movements, ETF weight changes)
- L3. Long/short comparison (Short Interest, Days to Cover, cost to borrow)
- L4. Insider behavior (Form 4 records, 10b5-1 plans vs. anomalous selling)
- L5. Liquidity (average daily volume, bid-ask spread)

### Module M: Long-Term Monitoring Variables Checklist
**Core Question**: After buying, what to watch? What signals to add, what signals to exit?
- M1. Incremental Drivers (3-5 growth drivers + quantified metrics + quarterly benchmarks)
- M2. Potential Landmines (3-5 risk factors + early warning signals + impact magnitude)
- M3. Action Triggers (specific, quantifiable, verifiable trigger conditions)

### Module N: R&D Efficiency & Innovation Pipeline
**Core Question**: Does this company have enough ammunition for the future?
- R&D spending as % of revenue (vs. peers), R&D efficiency, innovation pipeline, patent portfolio, talent competitiveness

### Module O: Accounting Quality Signals
**Core Question**: Are the financial numbers themselves trustworthy?
- Accrual ratio, revenue recognition policy changes, deferred revenue trends, off-balance-sheet items, audit opinions

### Module P: ESG & Institutional Capital Flow Screening
**Core Question**: Are there non-fundamental capital inflow/outflow factors?
- ESG ratings, controversy events, index inclusion/exclusion expectations

---

## Step Two: 6 Investment Philosophy Perspectives

**Read `references/investing-philosophies.md` before executing this step.**

For each of the 6 perspectives, answer: **Long / Short / Pass?** Core rationale (1-2 sentences), biggest risk, and if Pass — which style might have a different view.

---

## Step Three: Variant View

**This is the soul of the report.** If the conclusion fully aligns with consensus, the analysis adds no value.

> **The market consensus believes ___. We believe ___. They are wrong because ___.**

Determine consensus through analyst rating distribution, forward PE, and reverse DCF implied growth rates — then provide your rebuttal and evidence chain.

---

## Step Four: Anti-Bias & Pre-Mortem

**Read `references/bias-checklist.md` before executing this step.**

Run the 6 cognitive trap checks, 7 financial red flags, 5 tech blind spots, and Pre-Mortem analysis defined there.

---

## Step Five: Comprehensive Judgment & Output

Use this output template exactly:

```
# $[TICKER]: [One-sentence Variant View thesis]

## Executive Summary
[2-3 paragraphs. First sentence = recommended action.]

**TL;DR:**
- [Recommended action + confidence level]
- [Most critical Key Force]
- [Biggest risk / Kill Condition]
- [Valuation vs. current price + implied IRR]

## Key Forces
[1-3 Key Forces, 2000-3000 chars each, with primary source citations]

## Modules A–P Analysis
[Expand sequentially by module]

## K. Valuation Matrix
[Multi-method table + comparable multiples + sensitivity + probability-weighted scenarios]

## L. Ownership Distribution
[Institutional holdings, capital flows, long/short, insider behavior]

## Variant View
Market consensus: ... | Our view: ... | Why the market is wrong: ...

## 6 Philosophy Perspectives Summary
[Long/Short/Pass table]

## Pre-Mortem & Anti-Bias Check
[Failure path + red flag / yellow flag / green light]

## M. Long-Term Monitoring Variables
[Incremental Drivers + Landmines + Action Trigger table]

## Decision Framework
Position classification | Action Price | Entry pacing | Position size

## Evidence Sources
[Source, link, type, summary]

## Disclaimer
This analysis is based on publicly available information and model estimates, for research reference only. Not investment advice.
```

---

## Writing Discipline

- Lead with the conclusion — never open with "This report aims to analyze..."
- 80%+ active voice; remove filler words (actually, really, basically, essentially)
- Assert when evidence supports it; flag genuine uncertainty honestly
- Give 2-3x coverage to Key Force modules; standard coverage for the rest
- End with Action Triggers and monitoring checklist, not a drawn-out summary

---

## Coordination with Other Skills

- **us-value-investing**: Run four-dimensional value scoring after this analysis for cross-validation
- **us-market-sentiment**: Use when Module J involves macro sentiment as a Key Force
- **macro-liquidity**: Use when liquidity environment is a Key Force

---

## Language & Output Rules

- **Match the user's input language.** Chinese input -> Chinese output; English input -> English output; mixed -> match the mix.
- All output is analytical reference only, not investment advice.

---

## [deepalpha extension] Preview / recap / transcript / estimates / SaaS

### Pre-earnings preview
Consensus (rev, EPS, key KPIs) · beat/miss history & typical reaction · estimate-revision trend into the print (up = momentum) · options-implied move (if available) · what the bull and bear need to see. Sets the baseline to judge the actual print against.

### Estimate-revision analysis
Direction and breadth of analyst revisions over 30/90 days; rising revisions are among the more durable post-earnings drift signals. Track own-model vs consensus gap.

### Transcript read (8-K / call)
Management tone vs last quarter, guidance language (raised/maintained/cut, and quality of the raise), hidden risks, what they dodged. Pull the 8-K / press release via the data layer; transcripts via Octagon/web.

### SaaS / growth deep-dive (extends the 16-module set)
NDR/NRR (>120% strong), Rule of 40 (growth% + FCF margin% > 40), book-to-bill (>1), SBC% of revenue (>10% = dilution flag), CAC payback / LTV-CAC, billings vs revenue. **SaaS multiple compression:** decompose a falling EV/Sales into growth decel vs rate/multiple regime vs execution — so you know if it's the business or the tape.

### Post-earnings recap
Actual vs consensus, guidance delta, margin trend, transcript tone, estimate implication, price reaction vs the technical setup → updated Signal Block. (See `output-formats.md` §5.)

## Bundled engines
- `scripts/earnings_trade/` — gap size, pre-earnings trend, volume trend, MA50/MA200 position (5-factor post-earnings score).
- `scripts/earnings_pead/` — weekly-candle aggregation, breakout, liquidity, risk/reward for post-earnings drift.
