# TECHNICAL module — price action, trend, indicators & market timing

Pure price/volume read, no fundamental bias. Two jobs: (1) **timing** an entry/exit on a name whose thesis is already set elsewhere, and (2) **market-level timing** — is the broad tape healthy, topping, or bottoming. Data: price/volume via web search or a price MCP (SEC EDGAR does not provide prices — see `data-layer.md`).

Fused from: claude-trading-skills (technical-analyst, market-top-detector, ftd-detector, breadth/uptrend analyzers, vcp-screener), finance-skills (sepa-strategy), InvestSkill (technical-analysis).

## A. Single-name technical read

Score 0–3 per dimension; report total /15 with a one-line call.

1. **Stage / trend template (Minervini / Weinstein).** Stage 2 uptrend = price > MA50 > MA150 > MA200, MA200 rising ≥1 month, price ≥30% above 52-wk low and within ~25% of 52-wk high. Stage 1 base / Stage 3 top / Stage 4 decline downgrade conviction.
2. **Moving-average alignment & slope.** 50/150/200-day stacking and direction. Price extended >2 ATR above MA50 = chase risk.
3. **Momentum.** RSI(14) — overbought >70 / oversold <30, plus divergences. MACD cross & histogram. Relative strength vs S&P (RS line at new high = leadership).
4. **Structure.** Support/resistance, prior pivots, volume at price; trendlines; pattern (cup-with-handle, flat base, double bottom, head-and-shoulders). Note Dow-theory higher-highs/lows and any Elliott context only as supplementary.
5. **Base / setup quality (VCP / SEPA).** Volatility Contraction Pattern: 2–4 contractions each tighter, volume drying up into the pivot, then breakout on ≥40–50% volume surge. Define the **pivot buy point**, the **stop** (below last contraction low / base low), and a **2R target**.

Output: trend stage, key levels (support, resistance, pivot), the trigger that would change the read, and a scenario set (base/bull/bear with probabilities).

## B. Market-level timing (breadth & cycle)

- **Breadth health.** % of stocks above MA50/MA200, advance-decline, new highs vs new lows, sector participation. Narrowing breadth in an uptrend = distribution warning. Composite 0–100 read (healthy → narrowing → distribution).
- **Distribution days (O'Neil market-top).** Count days of −0.2%+ index decline on higher volume over ~25 sessions; 5–6 within a few weeks signals institutional selling / probable top. Combine with leading-stock deterioration and defensive rotation.
- **Follow-Through Day (O'Neil bottom confirmation).** After a correction: rally attempt → on day 4–7 a major index gains ~1.5%+ on higher volume = FTD, greenlight to re-add exposure. Track S&P + Nasdaq with a state machine (rally attempt → FTD → post-FTD health).
- **Sector rotation / regime.** Cyclical vs defensive leadership, RSP/SPY (breadth concentration), growth vs value, size factor — map to Early / Mid / Late cycle or Recession.

## C. Bubble / euphoria check (Minsky–Kindleberger, defensive)

Two-phase, evidence-required: quantitative score 0–12 (put/call, VIX, margin debt, breadth divergence, IPO/SPAC heat, valuation extremes) → small qualitative adjustment 0–3. Phases: Normal 0–4 · Caution 5–7 · Elevated 8–9 · Euphoria 10–12 · Critical 13–15. Each phase carries a risk budget and profit-taking guidance. Demand measurable evidence for any qualitative add (anti–confirmation-bias).

## Report template

```
### TECHNICAL — [name or "US market"]
Trend stage:    Stage [1–4] · MA50/150/200 [aligned? slope?]
Momentum:       RSI [x] · MACD [state] · RS [leading/lagging]
Key levels:     Support [$] · Resistance [$] · Pivot/buy [$] · Stop [$] · 2R target [$]
Setup:          [VCP/flat base/none] — [readiness]
Market tape:    Breadth [healthy/narrowing/distribution] · Distribution days [n] · FTD [yes/no] · Bubble phase [x/15]
Read:           [one line] — trigger to flip: [level/condition]
```

Technicals **confirm or time** a thesis; they don't override a broken fundamental case. Always pair extended/overbought signals with the bias-checklist before acting.

## Bundled engines
- `scripts/technical_breadth/` — trend level, MA crossover, divergence, cycle, historical context (breadth health).
- `scripts/technical_market_top/` — distribution-day, leading-stock, defensive-rotation, sentiment (O'Neil top).
- `scripts/technical_ftd/` — Follow-Through-Day state machine (bottom confirmation).
- `scripts/technical_macro_regime/` — cross-asset regime (concentration, yield-curve, credit, size, equity-bond, rotation).
- `scripts/screener_vcp/trend_template_calculator.py` — Stage-2 trend template.
Feed these with price data from the source connected per `data-layer.md` (SEC EDGAR has no prices).
