# SCREENER module — multi-name screening, ranking & peer comparison

For "find / rank / compare" requests: turn a universe into a short, ranked list, or build a peer table. Pick the recipe that matches the user's intent; always end with a ranked table and a one-line call per name.

Fused from: claude-trading-skills (CANSLIM, VCP, value-dividend, dividend-growth-pullback, PEAD, earnings-trade-analyzer, finviz-screener), InvestSkill (stock-eval, sector-analysis), finance-skills (sepa-strategy), edgartools/secedgar XBRL frames (universe screen + DuckDB SQL) — see `data-layer.md`.

## Data approach

- **Cross-company fundamentals:** use XBRL **frames** (one concept × one period across all filers) → rank/filter via the SQL canvas. Free, primary-source, whole-universe. Good for value/quality screens.
- **Price/technical screens (trend, RSI, breakout, VCP):** need price data → web / FMP / FINVIZ. State the source.
- **Peer set:** sector/SIC peers from EDGAR, or a user-supplied list.

## Recipes

**1. Quality compounder (Buffett/Piotroski lens).** ROIC >15%, gross margin stable/expanding, FCF/NI >100%, Debt/EBITDA <2.5, Piotroski F ≥7, reasonable reinvestment runway. Rank by composite quality.

**2. CANSLIM growth (O'Neil).** C current EPS accel · A annual growth · N new high/new catalyst · S supply-demand (volume accumulation, low float churn) · L leadership (RS rank) · I institutional sponsorship rising (tie to FLOW) · M market in confirmed uptrend (tie to TECHNICAL). Composite 0–100; M gates buys (bear market → raise cash).

**3. VCP / SEPA technical setup (Minervini).** Stage-2 trend template → tight base with 2–4 contracting pullbacks → pivot. Two-axis score: pattern quality vs execution readiness (don't chase extended). Output pivot, stop, 2R target.

**4. Value-dividend / income.** P/E ≤20, P/B ≤2, yield ≥3.5%, 3-yr dividend+EPS+revenue uptrend, payout & FCF-coverage sustainable, healthy D/E. Yield-trap filter (cut unsustainable payouts). For *dividend-growth* tilt: ≥12% dividend CAGR + ≥1.5% yield + RSI ≤40 pullback entry.

**5. PEAD / post-earnings drift.** Post-earnings gap-ups with strong pre-trend, volume surge, above MA50/200; monitor for red-candle pullback → breakout (entry, stop = pullback low, 2R target). Liquidity floor (ADV ≥ $25M, price ≥ $10).

**6. Peer comparison table.** For "A vs B vs C": one row per name, columns = growth, margins, ROIC, leverage, FCF yield, valuation multiples (P/E, EV/EBITDA, P/S), quality (Piotroski), and the deepalpha module verdicts. Highlight the leader per column.

## Scoring & output

Normalize each factor, weight per the recipe, rank descending. Always show the **screen definition** (filters + thresholds + data source + date) so it's reproducible.

```
### SCREENER — [recipe], universe = [..], as of [date], source = [SEC frames / FMP / FINVIZ]
| Rank | Ticker | [key factors…] | Composite | Call |
|------|--------|----------------|-----------|------|
| 1    | …      | …              | xx/100    | research-first |
Filters: [exact thresholds]
Notes: [survivorship / data caveats]
```

Hand the top finalists to VALUE → VALUATION → FLOW → TECHNICAL for full due diligence before any POSITION sizing. A screen is a candidate generator, not a buy list.

## Bundled engines (offline scoring — feed with data from `data-layer.md`)
- `scripts/screener_vcp/` — trend-template, VCP pattern, pivot proximity, relative strength, volume contraction, execution-state.
- `scripts/screener_canslim/` — C/A/N/S/L/I/M component calculators (composite 0–100).
- `scripts/earnings_pead/` & `scripts/earnings_trade/` — post-earnings drift & reaction scoring (also used by EARNINGS).
