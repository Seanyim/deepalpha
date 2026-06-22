# Data layer — primary-source backbone, freshness rules & fallback ladder

deepalpha's accuracy edge over a web-search-only skill: **pull facts from primary sources first.** SEC filings are authoritative, free, and dated; web pages are not. This file is the contract for *where each kind of data comes from*, *how fresh it must be*, and *what to do when a source is missing*.

## Source preference ladder (use the highest available rung)

| Rung | Source | Best for | Cost / key |
|---|---|---|---|
| 1 | **SEC EDGAR MCP** — `edgartools`, `secedgar`, or `stockscope` | US-company fundamentals (XBRL), 10-K/10-Q/8-K text, 13F holdings, Form 3/4/5 insider, sector peers, cross-company XBRL frames | **Free, no key** |
| 2 | **Deep-research / specialist MCP** — Octagon | multi-source synthesis, earnings-call transcripts, private-market & funding data, prediction markets | free tier / key |
| 3 | **Quant/calendar MCP** — FMP (if user has it) | economic & earnings calendars, ratios, breadth CSVs, cross-asset ETF data, **analyst price targets & consensus estimates** | free tier 250/day |
| 4 | **Premium FSI MCPs** — Daloopa, Morningstar, S&P/Kensho, FactSet, Aiera, LSEG, PitchBook | institutional-grade models, estimates, ratings, fixed-income, vol | subscription |
| 5 | **Crypto.com connector** | BTC/crypto spot, candles, order book, index price | free |
| 6 | **Notion connector** | the user's live portfolio (POSITION module) — see note below | free |
| 7 | **Web search / fetch** | price action, analyst targets & ratings, research notes (Morningstar / big-bank / Seeking Alpha / SemiAnalysis), sentiment surveys, macro prints, news | free |

**Rule:** for any fundamental, filing, holdings, or insider fact about a US public company, try rung 1 before web search. If the SEC MCP isn't connected, say so **once**, fall back to web search, and label scraped fundamentals as non-primary. Never fabricate filing numbers, CIKs, or holdings.

**Notion is live, not scraped.** The portfolio (rung 6) is read through the **Notion connector** (`notion-fetch`), authenticated as the user, returning data **as of the request moment** with an `as of <timestamp>`. This *is* real-time. Do **not** use a public Notion share link or `web_fetch` for the portfolio — those are JS-rendered and miss permissioned rows. Details + pinned IDs in `position.md`.

> To suggest/connect an MCP that isn't present, use the connector registry (`mcp-registry`). edgartools and the cyanheads secedgar server are the recommended free SEC backbones; stockscope is a lighter zero-config alternative.

## Freshness contract (timeliness — read before quoting any number)

Every figure carries an implicit "shelf life." Match the source to how fast the data decays:

| Data class | Shelf life | Where to get it fresh | Must do |
|---|---|---|---|
| Live price / quote | seconds–minutes | web search, price MCP, Crypto.com (BTC) | re-fetch each session; never reuse a prior turn's price |
| Analyst targets / ratings / estimates | days | FMP, web (Morningstar, big-bank notes, TipRanks/Seeking Alpha aggregations) | date-stamp; note # of analysts + range, not just the mean |
| Sentiment surveys (NAAIM/AAII), breadth | weekly | web search | use the latest weekly print; state the week |
| Macro prints (CPI, PCE, NFP, Fed, SOFR, MOVE, TGA/RRP, USDJPY) | release-driven | web / FRED | confirm you have the most recent release, not last month's |
| Fundamentals (XBRL financials) | quarterly | SEC EDGAR (rung 1) | cite fiscal period + form/accession |
| 13F institutional holdings | quarterly, **45-day lag** | SEC EDGAR | always label the lag; never treat as current positioning |
| Insider Form 4 | event-driven (2-day filing) | SEC EDGAR | recent window 3/6/12m |
| Portfolio (Notion) | live | Notion connector | use the connector `as of` stamp |

**Hard rule:** if a figure's shelf life is shorter than the time since you last fetched it, **re-fetch before quoting.** Prices and macro prints from a previous turn are stale by default.

## SEC EDGAR tool catalog (names vary by which server is installed)

| Capability | edgartools (`edgar.*`) | secedgar (`secedgar_*`) | stockscope | Used by module |
|---|---|---|---|---|
| Resolve ticker/name/CIK | `Company("AAPL")` | `secedgar_company_search` | (ticker arg) | all |
| Financial statements (XBRL) | `get_financials()` | `secedgar_get_financials` | `stock_financials` | VALUE, VALUATION, EARNINGS |
| One concept across all filers | `Company.get_facts()` / frames | `secedgar_fetch_frames` (+ SQL) | — | SCREENER |
| 10-K / 10-Q / 8-K full text + sections | `get_filings(form=…)[0].obj()`, `.items` | `secedgar_get_filing` (section paging), `secedgar_search_filings` | `stock_filings` | VALUE, EARNINGS |
| Full-text search across filings | EFTS search | `secedgar_search_filings` | — | THEME, EARNINGS |
| 13F institutional holdings | `get_filings(form="13F-HR")[0].obj().holdings` | `secedgar_get_institutional_holdings` | — | FLOW |
| Form 3/4/5 insider transactions | `company.get_filings(form="4")[0].obj().transactions` | `secedgar_get_insider_transactions` | `stock_insiders` | FLOW |
| Sector / SIC peers | company subsets by SIC | (search + SIC) | `stock_sector_peers` | SCREENER, VALUE |
| Side-by-side compare | build from financials | financials × 2 | `stock_compare` | SCREENER |
| Price history | (use web/connector) | — | `stock_history` | TECHNICAL |
| In-conversation SQL over results | — | `secedgar_dataframe_describe/query` (DuckDB) | — | SCREENER, FLOW |

Setup note (tell the user once if they want it): edgartools needs `set_identity("Name email")`; secedgar needs `EDGAR_US