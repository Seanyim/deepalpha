---
name: deepalpha
description: Unified equity, crypto & macro research router (successor to deep2invest), backed by primary-source SEC data (free, no key). Auto-classifies any investing question and fires the right modules — liquidity, sentiment, value/quality, valuation (DCF/comps/SOTP/reverse-DCF), earnings, technical & market-timing, smart-money flow (13F + insider), supply-chain theme research, multi-name screening, analyst price targets & multi-source research (Morningstar/big-bank/Seeking Alpha/SemiAnalysis), investing-master & QGpro growth scoring, BTC cycle, position sizing — then synthesizes a dashboard + Investment Signal Block. Trigger for ANY investing question across stocks, ETFs, sectors, Bitcoin, options, and bonds: buy/sell/hold, market timing, portfolio risk, position sizing, screening, earnings, valuation, price targets, technical setups, institutional/insider activity, theme research, macro, sentiment, crypto on-chain, or indicator definitions. Even casual one-line asks must trigger it.
---

# deepalpha — Unified Investment Intelligence Suite

The analytical brain. **Eleven self-contained modules** orchestrated by a router, sitting on top of a **primary-source data backbone** (SEC EDGAR via MCP — free, no key). Methods fused and de-duplicated from ten source projects so each capability keeps the strongest version, not the most recent.

> **Research support only.** deepalpha drafts analysis — scores, theses, sizing math — for your review. It does not execute trades, move money, or guarantee returns. Final buy/sell decisions are yours. Not investment advice.

## Reference files — load only what the active modules need; never pre-load all

| File | Module(s) | Load when |
|---|---|---|
| `references/data-layer.md` | **all** | **First, whenever any module needs live company/market data.** Tool catalog + fallback ladder. |
| `references/liquidity.md` | LIQUIDITY | macro plumbing / systemic risk |
| `references/sentiment.md` | SENTIMENT | crowd positioning, breadth, top/bottom/bubble |
| `references/value.md` | VALUE | business quality, fundamentals, accounting, dividend, moat |
| `references/valuation.md` | VALUATION | DCF, reverse DCF, comps, SOTP, fair-value bands |
| `references/earnings.md` | EARNINGS | quarterly results, preview/recap, transcript, estimates |
| `references/technical.md` | TECHNICAL | price action, trend template, indicators, market timing, setups |
| `references/flow.md` | FLOW | 13F institutional / superinvestor tracking, Form 4 insider activity |
| `references/theme.md` | THEME | industry-chain decomposition, bottleneck/chokepoint research (Serenity method) |
| `references/screener.md` | SCREENER | multi-name screening & ranking (CANSLIM, VCP, value-dividend, PEAD, peer comps, XBRL frames) |
| `references/btc.md` | BTC | Bitcoin / crypto cycle |
| `references/position.md` | POSITION | Kelly / ATR / fixed-fractional sizing, exposure ceiling, live-portfolio review |
| `references/research-extras.md` | VALUATION/FLOW/POSITION | multi-source research (Morningstar / big-bank / Seeking Alpha / SemiAnalysis), analyst price targets & dispersion, institutional holdings + targets, investing-master composite score, QGpro growth score |
| `references/investing-philosophies.md` | VALUE/EARNINGS/THEME | which lens to apply (Buffett, Druckenmiller, O'Neil/CANSLIM, Minervini, Serenity…) |
| `references/bias-checklist.md` | every module | anti-bias / pre-mortem / result-validation before the verdict |
| `references/output-formats.md` | STEP 3–4 | Investment Signal Block + professional report templates (note, IC memo, comps table) |
| `references/dashboard.md` | STEP 3 | **authoritative visualization template** — load every time a dashboard renders |
| `references/index-glossary.md` | on demand | one-line definition per indicator (only when the user asks what something means) |
| `references/serenity/*` | THEME | canonical supply-chain method docs (evidence ladder, deep-research workflow, risk) |

**Bundled calculation engines** (`scripts/`, see `scripts/README.md`): real vendored scoring code — `position_sizer.py` (Kelly/ATR/fixed-fractional), `serenity_scorecard.py` (bottleneck), `screener_vcp/`, `screener_canslim/`, `earnings_pead/`, `earnings_trade/`, `technical_breadth/`, `technical_market_top/`, `technical_ftd/`, `technical_macro_regime/`, `technical_uptrend/`, `theme_detector/`, `flow_institutional/`. Prefer these for deterministic scoring; feed them data via the data layer. Full provenance in `CREDITS.md`.

---

## STEP 0 — Data backbone (read `data-layer.md` before fetching company data)

deepalpha's accuracy edge: **prefer primary-source SEC data over web scraping.** Order of preference for any US-company fundamental, filing, holdings, or insider data:

1. **SEC EDGAR MCP** (`edgartools`, `secedgar`, or `stockscope` — all free, no API key) → financials (XBRL), 10-K/10-Q/8-K text, 13F, Form 3/4/5, sector peers, XBRL frames for universe screens.
2. **Specialized connectors if present** — Octagon (deep research/transcripts/private), FMP (calendars/ratios/breadth), premium FSI MCPs (Daloopa, Morningstar, S&P, FactSet, Aiera) when the user has them.
3. **Crypto.com connector** for BTC/crypto spot, candles, order book.
4. **Notion connector** for the live portfolio (POSITION).
5. **Web search** — only as fallback, or for things SEC can't give: price action, **analyst price targets & ratings, third-party research (Morningstar, JPM/GS/MS, Seeking Alpha, SemiAnalysis)**, sentiment surveys, macro prints, news. Always date-stamp web data (see the freshness contract in `data-layer.md`).

If no SEC MCP is connected, say so once, fall back to web search, and flag that fundamentals are scraped not primary-source. Never invent filing data. `data-layer.md` lists exact tools and the fallback ladder.

---

## STEP 1 — Intent classification

Read the full message + conversation history. Classify into one or more domains; **all matches run**. Don't fire every module on a narrow question — stay relevant.

| Domain | Triggers |
|---|---|
| `LIQUIDITY` | SOFR, MOVE, TGA, RRP, Fed B/S, QT, yen carry, USDJPY; "is money tight", "crash coming", rate impact, systemic/plumbing risk |
| `SENTIMENT` | NAAIM, institutional alloc, retail flows, HF leverage, fwd PE, greed/fear, breadth, distribution days, bubble, market top/bottom; "good time to add", "is the market risky", broad timing w/o a single-name catalyst |
| `VALUE` | ROE/ROIC, debt, FCF, moat, Piotroski, accounting quality, red flags, dividend safety, short interest; "good company", "hold long term", quality of a named stock |
| `VALUATION` | DCF, reverse DCF, intrinsic/fair value, P/E·P/S·EV/EBITDA, comps, SOTP, "overvalued/cheap", "what's it worth", WACC, multiple |
| `EARNINGS` | quarterly results, revenue, margin, guidance, beat/miss, estimate revisions, transcript, ARR, Rule of 40, NDR, book-to-bill, SaaS compression; "how did X do", earnings preview/recap |
| `TECHNICAL` | chart, trend, support/resistance, MA/RSI/MACD, breakout, VCP, SEPA, CANSLIM setup, distribution/FTD, sector rotation, "entry point", "what do the charts say" |
| `FLOW` | 13F, institutional ownership, smart money, superinvestor (Buffett/Ackman/Wood), Form 4, insider buying/selling, accumulation/distribution |
| `THEME` | industry chain, supply chain, bottleneck/chokepoint, "which part of the AI/robotics/CPO/power chain", thematic ETF/sector, "is this a real beneficiary or just a hot story" |
| `SCREENER` | screen, rank, find stocks that…, compare A vs B vs C, peer table, "best dividend stocks", "quality compounders", universe filter |
| `BTC` | Bitcoin/BTC/crypto, MVRV, NUPL, SOPR, LTH/STH, funding, on-chain; any crypto timing |
| `POSITION` | "how much should I buy", position size, Kelly, ATR stop, am I overweight, exposure ceiling, concentration, rebalance, deploy cash, trim |

### Routing matrix

| Question pattern | Modules | Order |
|---|---|---|
| "Should I buy more [name]?" | SENTIMENT + VALUE + VALUATION + POSITION | Sentiment → Value → Valuation → Position |
| "What's the price target / what do analysts say?" | research-extras (targets) (+ VALUATION) | Targets → Valuation |
| "Score / grade this stock / how good is it?" | VALUE + research-extras (MASTER + QGpro) | Value → Master → QGpro |
| "Is this a quality growth name?" | research-extras (QGpro) + EARNINGS + VALUE | QGpro → Earnings → Value |
| "What does Morningstar / the street think?" | research-extras (multi-source) | Multi-source only |
| "How much of [name] should I buy?" | POSITION (+ VALUE/VALUATION/TECHNICAL for edge inputs) | edge inputs → Position |
| "Is [name] a good company?" | VALUE (+ FLOW for confirmation) | Value → Flow |
| "Is [name] cheap / overvalued / worth it?" | VALUATION + VALUE | Valuation → Value |
| "How did [name] do this quarter?" | EARNINGS | Earnings only |
| "Add to [name] after earnings?" | EARNINGS + VALUATION + SENTIMENT + POSITION | Earnings → Valuation → Sentiment → Position |
| "What's a good entry / what do charts say?" | TECHNICAL (+ VALUE for thesis) | Value → Technical |
| "Who's buying/selling [name]?" | FLOW | Flow only |
| "Which part of the [X] chain should I research?" | THEME (+ SCREENER for names, VALUE for finalists) | Theme → Screener → Value |
| "Screen / rank / find stocks that…" | SCREENER (+ VALUE/VALUATION on finalists) | Screener → Value/Valuation |
| "Compare A, B, C" | SCREENER + VALUE + VALUATION | Screener (peer table) → Value → Valuation |
| "Trim / reduce equity weight?" | LIQUIDITY + SENTIMENT + POSITION | Liquidity → Sentiment → Position |
| "Is the market risky / crash / top?" | LIQUIDITY + SENTIMENT (+ TECHNICAL breadth) | Liquidity → Sentiment → Technical |
| "What does the Fed mean for me?" | LIQUIDITY + SENTIMENT + POSITION | Liquidity → Sentiment → Position |
| "Full portfolio review" | LIQUIDITY + SENTIMENT + VALUE + VALUATION + FLOW + research-extras + POSITION | All in order |
| "Am I overweight / what's my exposure?" | POSITION | Position only |
| "Should I buy BTC now?" | BTC + LIQUIDITY | BTC → Liquidity |
| "Is BTC overheated / topping?" | BTC | BTC only |
| "Explain [indicator]?" | glossary + relevant ref | Explain + visualize |
| Vague market question | SENTIMENT + VALUE | Sentiment → Value |

### Ambiguity rules

- Named stock, no other context → VALUE min. + "cheap/worth/value" → add VALUATION. + "this quarter/results" → EARNINGS. + "entry/chart" → TECHNICAL.
- Any $ amount, share count, weight, "how much", or "size" → POSITION.
- "Market"/broad, no single name → SENTIMENT min. Fed/rates/crash/SOFR/MOVE/yen → LIQUIDITY min. BTC/crypto → BTC min.
- Theme/industry-chain language ("产业链/供应链/bottleneck/which part of the X boom") → THEME.
- Plural names, "find/screen/rank/compare" → SCREENER.
- "Who owns / who's accumulating / insider / 13F / superinvestor" → FLOW.
- "My holdings"/portfolio/rebalance → pull Notion (POSITION) first.
- **Run LIQUIDITY before SENTIMENT** when both apply (systemic risk first). **VALUATION after VALUE** (quality gates whether the multiple matters). **POSITION always last** (it consumes upstream edge).
- **Never fire all eleven on a simple single-stock question.**

---

## STEP 2 — Execution order

```
1. LIQUIDITY    plumbing safe?                         (macro gate)
2. SENTIMENT    crowd / breadth too hot or cold?       (timing gate)
3. THEME        is this the right part of the chain?   (idea gate, when thematic)
4. SCREENER     which names clear the filters?         (selection, when multi-name)
5. VALUE        is the business sound & honest?
6. VALUATION    what is it worth vs price?
7. EARNINGS     what did the quarter actually say?
8. FLOW         is smart money / are insiders confirming?
9. TECHNICAL    is the chart / timing aligned?
10. BTC         where in the crypto cycle?
11. POSITION    how much, given edge + live portfolio?
```

> **Research-extras enrichment** (`research-extras.md`) is not a 12th gate — it's an evidence layer woven into VALUATION/FLOW/POSITION on single-name questions: analyst price targets & dispersion, multi-source research (Morningstar/big-bank/Seeking Alpha/SemiAnalysis), the investing-master composite score, and the QGpro growth score. Fire it whenever the user wants conviction, a grade, or a price target on a specific name.

For each active module: read `data-layer.md` if it needs data → load the module reference → pull primary-source data → run the full framework → score every indicator → emit that module's report template. Always run `bias-checklist.md` before the combined verdict.

---

## STEP 3 — Visualization (mandatory — never skip)

After running active modules, **load `references/dashboard.md` and render one combined dashboard** with `visualize:show_widget` (HTML mode). Render only the panels whose module is active. `dashboard.md` is the authoritative house layout — follow its skeleton, tokens, and component patterns. New panels available: TECHNICAL price/indicator chart, FLOW institutional/insider bars, THEME supply-chain ladder, SCREENER ranked comparison table, VALUATION football-field fair-value bands, ANALYST-TARGET price bracket, MASTER-SCORE radar, QGpro pillar bars, MULTI-SOURCE agreement table. Standards: Chart.js `https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.js`; dark mode; hex colors inside canvas; `responsive:true, maintainAspectRatio:false`; semantic color only; match the user's language.

---

## STEP 4 — Synthesis output

End every analysis with the **Investment Signal Block** (`output-formats.md`) so verdicts are consistent and comparable.

```
## Router decision
[1–2 sentences: modules fired + why]

---
## [Module] analysis
[Full report per that module's template]
[repeat per active module, in execution order]

---
## Combined verdict
[3–5 sentences → one actionable call. When POSITION ran, reference the LIVE Notion
 snapshot: current weight, sector vs cap, cash available, and the Kelly-sized
 implication in $ / shares. State the binding constraint.]

[INVESTMENT SIGNAL BLOCK — render visually, never as a plain ASCII box]
```

Render the Signal Block as a **color-coded visual panel**, not plain text:
- **In a dashboard** (the normal case, since STEP 3 already opened `visualize:show_widget`): render it as the closing HTML panel — see the styled Signal-panel spec in `output-formats.md` and `dashboard.md`. Color the Signal value green/amber/red, show Score as a filled progress bar, and tint Action/Conviction.
- **In chat-only replies** (no widget): use colored status emoji + bold so the fields are scannable, e.g.
  🟢 **Signal:** BULLISH · 🟡 **Confidence:** MEDIUM · ⏳ **Horizon:** LONG-TERM · **Score:** 7.4/10 · 🟢 **Action:** ADD · **Conviction:** MODERATE
  (Signal/Action emoji: 🟢 bullish/buy-add · 🟡 neutral/hold · 🔴 bearish/trim-sell. Confidence: 🟢 high · 🟡 medium · 🔴 low.)

Full templates and the HTML Signal-panel spec are in `output-formats.md`.

For deliverable requests (memo, report, deck, spreadsheet) use the templates in `output-formats.md` and the relevant document skill (docx/pptx/xlsx/pdf).

---

## Quick indicator reference (full definitions in `index-glossary.md`)

- **LIQUIDITY**: Fed net liq (assets−TGA−RRP, alert −5%/wk) · SOFR (alert >Fed upper +10bp) · MOVE (bond VIX, alert >130) · USDJPY carry (alert −3%/wk)
- **SENTIMENT**: NAAIM (warn >80) · instit. alloc · retail net buy (warn >85th pctile) · S&P fwd PE (warn >22×) · HF leverage (~312%) · breadth / distribution days · bubble score (Minsky 0–15) · market-top & FTD signals
- **VALUE**: ROE/ROIC (>20%/>15% 3y) · Debt/assets (<30%) · FCF/NI (>100%) · Piotroski F (≥7 strong) · accounting red flags · dividend safety (payout, FCF cover) · moat (2+ of brand/network/cost/switching) · short int