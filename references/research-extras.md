# Research extras — multi-source research, price targets, master scores & QGpro

Five cross-cutting layers that sharpen any single-name analysis. Load this when the question is about a specific stock and the user wants conviction beyond the core modules. All external figures are **web/connector-sourced and must be date-stamped** (see `data-layer.md` freshness contract). Never invent a target, rating, or grade.

---

## 1. Multi-source research aggregation

Triangulate views from independent professional sources, then state where they agree and disagree. Pull the latest note/rating for each and cite the date.

| Source | What to extract | How to get it |
|---|---|---|
| **Morningstar** | Star rating (1–5), economic-moat rating (None/Narrow/Wide), fair-value estimate, uncertainty | web search; premium Morningstar MCP if connected |
| **Sell-side big banks** (JPM, Goldman, Morgan Stanley, BofA, Barclays…) | rating (OW/EW/UW or Buy/Hold/Sell), price target, thesis one-liner, recent up/downgrades | web search for latest notes; date-stamp each |
| **Seeking Alpha** | Quant rating + factor grades (valuation/growth/profitability/momentum/revisions), SA Analyst vs Wall St split | web search |
| **SemiAnalysis** (semis / AI infra / data-center names only) | supply-chain & capacity read, accelerator/CoWoS/HBM/power commentary | web search; pairs with THEME |
| **Specialist desks** as relevant | e.g. Redburn, Bernstein, New Street for hardware; pair with the right theme | web search |

Output an **agreement matrix**: source · rating/score · target/fair value · date · one-line thesis. Then a synthesis line: "N of M sources constructive; the bear case rests on [X]." Treat heavy unanimity with mild caution (crowded view); a credible dissent is information, not noise.

---

## 2. Analyst price targets (consensus + dispersion)

Don't quote a single mean. Report the **distribution**:

- **Consensus target** (mean and median) and implied upside/downside vs current price.
- **High / low range** and **number of analysts** — a wide range = low conviction; a tight range = consensus crowding.
- **Recent revisions** — are targets being raised or cut over the last 30/90 days? Revision *direction* matters more than the level.
- **Rating mix** — count of Buy / Hold / Sell.

Source: FMP if connected, else web (TipRanks / Seeking Alpha / Koyfin aggregations). Place the consensus target on the VALUATION football field alongside deepalpha's own fair-value band so the user sees street vs independent in one view.

```
### ANALYST TARGETS — [name]  (as of <date>)
Consensus: $[mean] (median $[..]) → [+/–X%] vs $[price] · range $[low]–$[high] (N analysts)
Ratings: [b] Buy / [h] Hold / [s] Sell · 90d revision: [raising/cutting/flat]
Read: [street constructive/divided/cautious]; deepalpha fair value $[..] sits [above/below/in-line]
```

---

## 3. Institutional holdings + their targets (smart-money positioning)

Extends FLOW with a price-context overlay. Primary holdings data stays SEC-sourced (13F, 45-day lag — see `flow.md`); the *targets* are web/research-sourced.

- **Who owns it** — top institutional holders, % held by institutions, QoQ tier-weighted accumulation/distribution (from FLOW).
- **Conviction holders** — superinvestors (Berkshire, Baupost, Pershing, ARK for thematic) with the name as a top position.
- **Where the street thinks it goes** — bracket the consensus and notable single-bank targets against current price and the names' own holders' likely cost basis (from 13F trend).
- **Tension check** — institutions accumulating *into* a rising consensus target = trend confirmation; accumulating while targets are cut = contrarian / value setup worth a closer look.

Always restate the 13F lag and that targets are estimates, not commitments.

---

## 4. Investing-master scoring system (composite grade, 0–100)

Score the name through several master lenses and blend into one grade. Each lens is 0–100; the composite is the (optionally weighted) average. Use `investing-philosophies.md` for the full worldview behind each.

| Lens | Master | What scores high (→100) |
|---|---|---|
| Quality compounder | Buffett / Munger | wide moat, ROIC≫WACC, FCF conversion >80%, honest capital allocation, low leverage |
| Deep value / safety | Graham / Klarman | ≥30% margin of safety, asset backing, normalized-earnings cheapness, no value-trap signs |
| GARP growth | Lynch / Tiger | sustainable >15% growth at a reasonable PEG, earnings-revision tailwind, understandable story |
| Imaginative growth | Baillie Gifford / ARK | large/expanding TAM, optionality, exponential not linear, category leadership |
| Catalyst / event | Tepper / Ackman | named catalyst <12–18m, ≥2:1 asymmetric payoff, balance-sheet clean |
| Macro / regime fit | Druckenmiller / Soros | aligned with the current liquidity & rate tide, right factor for the regime |

```
### MASTER SCORE — [name]
Buffett [..] · Graham/Klarman [..] · Lynch/GARP [..] · BG/ARK [..] · Tepper/Ackman [..] · Druckenmiller [..]
Composite: [XX]/100  → grade [A 80+ / B 65–79 / C 50–64 / D <50]
Drivers: [top 2 lenses] · Drags: [bottom 2 lenses]
```
A high composite with wide lens **dispersion** (e.g. 90 Buffett, 30 ARK) means "great by one philosophy, not another" — say which, and which kind of investor it suits. Convergence across lenses = the strongest signal.

---

## 5. QGpro growth-scoring system (0–100, growth-name lens)

A structured growth-quality score for fast-growers, complementing the VALUE four-dimension (which is quality/value-tilted) and EARNINGS module. Six pillars, ~16–17 pts each, capped at 100. Pull inputs from SEC XBRL (rung 1) + estimates (web/FMP).

| Pillar (≈17 pts) | Measures | Strong reading |
|---|---|---|
| **Q — Quality of growth** | organic vs acquired revenue, recurring %, gross-margin durability | mostly organic, recurring, stable/expanding GM |
| **G — Growth rate & durability** | revenue & EPS CAGR (3y trailing + fwd), deceleration check | >20% with no sharp decel; long runway |
| **P — Profitability trajectory** | operating-margin trend, Rule of 40 (growth%+FCF margin%), path to/expansion of FCF | Rule of 40 >40 (>60 exceptional), margins rising |
| **R — Retention & unit economics** | NDR/NRR, cohort behavior, customer concentration, CAC efficiency where visible | NDR >120%, low concentration |
| **O — Operating leverage & reinvestment** | incremental margins, ROIC on growth capex, SBC discipline | positive incremental margins, ROIC>WACC, SBC <10% rev |
| **(scale gate)** | revenue-revision trend, estimate momentum, durability of the above through a cycle | upward revisions, holds through soft macro |

```
### QGpro — [name]  (growth-quality)
Q[..] G[..] P[..] R[..] O[..] → QGpro [XX]/100  (tier: Elite 80+ / Strong 65–79 / Watch 50–64 / Avoid <50)
Edge: [the 1–2 pillars carrying the score] · Risk: [weakest pillar + what would break it]
```

QGpro is a **growth** lens; pair it with the MASTER SCORE and VALUE four-dimension so a name gets read on both growth *and* durability/value — never on growth alone.

---

## How these feed the rest of the pipeline

- **VALUATION** — consensus target + Morningstar fair value go on the football field next to deepalpha's band.
- **POSITION** — MASTER-SCORE composite and analyst-target gap inform Kelly `p` and the ADD/HOLD/TRIM call.
- **Dashboard** — render the price-target bracket, master-score radar, and QGpro pillar bars (see `dashboard.md`).
- **Signal Block** — blend these sub-scores into the overall Score and Confidence (more sources agreeing → higher Confidence).
