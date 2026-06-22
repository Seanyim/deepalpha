# POSITION module — sizing, exposure & live-portfolio review

Runs **last** — it consumes the edge produced upstream (VALUE / VALUATION / EARNINGS / FLOW / TECHNICAL / MASTER-SCORE / QGPRO conviction) and converts it into concrete $ / share actions against the live portfolio. Three layers: macro exposure ceiling → per-trade size → reconcile with current holdings.

---

## Live portfolio — Notion connector (real-time, never hardcoded)

**How the live read works — this is the answer to "is it real-time?"**
The portfolio is pulled through the **Notion MCP connector** (`Notion:notion-fetch`), authenticated as the user — **not** a public share link and **not** `web_fetch`. The connector returns the database **as of the current moment**; every response is stamped with an `as of <ISO-8601>` timestamp, so the snapshot is genuinely live each time POSITION runs. A public Notion link fetched via `web_fetch` would **not** work: those pages are JS-rendered, and the connector also sees private/permissioned rows a public link cannot. → Always use `notion-fetch`; never scrape a URL.

**Pinned IDs** — the entry page is stable; data-source `collection://` IDs can drift, so if a fetch returns empty, re-read the parent page to recover them:

```
PORTFOLIO_PAGE   = e2c46ae68a704cfeb48e4ab6af589b43   # 🦅 Falconcrest Fund (entry point — fetch first)
PARENT_FINANCE   = fc007ec26d42486eb7b66269e4ea9b82   # Finance (context)
HOLDINGS_DS      = collection://28e0e500-11c9-4ba7-b07f-5c47f989c38c   # 持仓 / Holdings (per-position)
NAV_RETURNS_DS   = collection://ad858a4d-6cc2-480f-998c-4428e63546b8   # 总资产收益 (total assets / cash / NAV)
UNIT_NAV_DS      = collection://99631d58-904d-4e55-a462-c6179b5a06e4   # 每日单位净值变化 (unit-NAV history)
```
> Recovery: fetch `PORTFOLIO_PAGE` and read the `data-source-url="collection://…"` tags to refresh IDs. Treat the entry page as ground truth.

**Read sequence.**
1. Fetch `HOLDINGS_DS` → one row per position. **Verified field map:** 代码 = ticker (title) · 数量 = shares · 当前股价 = current price ($) · 证券市值 = market value (rollup) · 持仓占比 = weight of total NAV (formula) · 占证券仓位 = weight of securities sleeve (formula) · Market Value = formula. Weights are computed inside Notion — read them, don't recompute unless needed.
2. Fetch `NAV_RETURNS_DS` for total assets, cash, NAV; `UNIT_NAV_DS` for unit-NAV history only if the question needs performance context.
3. **Date-stamp the read** using the connector's `as of` timestamp. If `当前股价` looks stale vs the live tape, re-verify prices via web search (or Crypto.com connector for BTC) and say which figure you used.

If the connector is unreachable or a row is empty → **ask before sizing. Never invent positions, prices, or cash.**

### User-configurable defaults (edit to taste)
- Single-name cap: 15% of NAV · Sector cap: 20% of NAV
- Kelly fraction: ½-Kelly (range ¼–½) · IRR hurdle: 15% base-case for longs
- Per-trade risk: 0.5–1.0% of NAV at stop (fixed-fractional)
- Cash-deploy triggers: NAAIM <55, OR name at technical support, OR post-earnings dip with thesis intact

---

## Layer 1 — Exposure ceiling (how much equity at all)

Before sizing any single name, set the portfolio's equity ceiling (0–100%) from LIQUIDITY + SENTIMENT + TECHNICAL breadth: plumbing safe? crowd/breadth hot or washed out? market in confirmed uptrend or distribution? Output: exposure ceiling, growth-vs-value tilt, and a posture — `NEW ENTRY ALLOWED` / `REDUCE ONLY` / `CASH PRIORITY`. A name can be great and still be a "wait" if the ceiling says reduce-only.

## Layer 2 — Per-trade size (three methods, reconcile)

- **Kelly (edge-based).** Discrete: **f\* = p − (1−p)/b** where p = thesis-success prob (base-rate-adjusted, haircut for estimation error), b = expected upside ÷ downside. Continuous equity analogue: **f\* ≈ (μ − r) / σ²**. Apply fractional Kelly: `f_target = kelly_mult × f*` (default ½). Negative f\* → no position. Set `b` from VALUATION's upside/downside band; inform `p` with the MASTER-SCORE and the analyst-target consensus (see `research-extras.md`).
- **ATR / risk-based (entry & stop known).** shares = (NAV × risk%) ÷ (entry − stop), stop from ATR or structure (TECHNICAL). Caps the dollar loss if the stop hits.
- **Fixed-fractional.** Simple % of NAV per idea, scaled by conviction tier.

Reconcile: take the **most conservative** applicable method, then clamp `f_target = min(f_target, single-name cap, cash-available%)`, and respect the sector cap on the aggregate. Report f\*, the fractional target, the chosen method, and the **binding constraint**. Buys must clear the IRR hurdle.

## Layer 3 — Holdings reconciliation (gap to target)

- Each position's weight from **持仓占比** (or 证券市值 ÷ NAV); show top-5 and sector aggregates.
- **Concentration:** f