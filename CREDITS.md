# deepalpha — sources & attribution

deepalpha fuses methods and code from the projects below. Vendored files keep their original logic (only import paths were adjusted for the renamed folders). All sources are permissively licensed (MIT / Apache-2.0). This is a personal research merge; verify each upstream license before redistribution.

## Skills — methods + vendored code
| Source | License | What was merged | Where it landed |
|---|---|---|---|
| **tradermonty/claude-trading-skills** | (see repo) | Position sizer (Kelly/ATR/fixed-fractional), VCP, CANSLIM, PEAD, earnings-trade, market-breadth, uptrend, market-top, FTD, macro-regime, theme-detector, institutional-flow — **actual calculator code** | `scripts/*`, `references/technical.md`, `screener.md`, `flow.md`, `position.md`, `investing-philosophies.md`, `bias-checklist.md` |
| **muxuuu/serenity-skill** | MIT | Supply-chain bottleneck method, evidence ladder, deep-research workflow — **scorecard engine + assets + reference docs** | `scripts/serenity_scorecard.py`, `assets/*`, `references/theme.md`, `references/serenity/*` |
| **yennanliu/InvestSkill** | MIT | 21 frameworks: stock-eval (Piotroski/ROIC), DCF/comps/SOTP/reverse-DCF, insider/13F, Investment Signal Block, result-validator | `references/value.md`, `valuation.md`, `flow.md`, `output-formats.md`, `bias-checklist.md` |
| **himself65/finance-skills** | MIT | SaaS multiple compression, earnings preview/recap, SOTP triangulation, SEPA, social sentiment | `references/earnings.md`, `valuation.md`, `technical.md`, `sentiment.md` |
| **anthropics/financial-services** | Apache-2.0 | Professional deliverables (IC memo, initiation, comps, earnings note); premium MCP connector catalog | `references/output-formats.md`, `data-layer.md` |
| **OctagonAI/skills** | MIT | Deep multi-source research, transcripts, private/prediction-market data | `references/theme.md`, `earnings.md`, `data-layer.md` |
| **deep2invest** (your skill) | — | Router + dashboard architecture, LIQUIDITY/SENTIMENT/VALUE/EARNINGS/BTC modules, Kelly, Notion live-portfolio, calibrated thresholds | `SKILL.md`, all ported `references/*` |

## MCPs / data libraries — data backbone (config + tool catalog, not vendored as code)
A skill cannot contain a server, so these are wired via `references/data-layer.md` as the preferred data sources:
| Source | License | Role |
|---|---|---|
| **dgunning/edgartools** | MIT | **Primary** free SEC backbone — XBRL financials, 13F, Form 3/4/5, 8-K, frames. MCP + Python. |
| **cyanheads/secedgar-mcp-server** | Apache-2.0 | Alt free SEC MCP — filings, financials, 13F, insider, frames + DuckDB SQL canvas. |
| **Stewyboy1990/stockscope-mcp** | MIT | Lightweight zero-config SEC MCP — financials, filings, compare, insiders, sector peers. |
| **OctagonAI/octagon-mcp-server** | MIT | Deep research / transcripts / private + prediction markets (API key). |

deep2invest's existing **Notion** (portfolio) and **Crypto.com** (BTC) connectors are reused.
