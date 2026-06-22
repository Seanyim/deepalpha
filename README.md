# deepalpha

> **Unified equity, crypto & macro research router for Claude — backed by primary-source SEC data (free, no API key).**

deepalpha is a [Claude skill](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview): a self-contained package of instructions, reference docs, and Python calculators that turns Claude into an investment-research analyst. Ask any investing question — a single stock, an ETF, a sector, Bitcoin, the macro backdrop, or your whole portfolio — and deepalpha auto-classifies the intent, fires only the relevant analysis modules, pulls primary-source data, runs each framework, and synthesizes a dashboard plus a consistent **Investment Signal Block**.

> ⚠️ **Research support only.** deepalpha drafts analysis — scores, theses, sizing math — for your review. It does **not** execute trades, move money, or guarantee returns. Final buy/sell decisions are yours. **This is not investment advice.**

---

## What it does

deepalpha is built around a **router + eleven self-contained modules** sitting on a **primary-source data backbone** (SEC EDGAR via MCP). On each question the router classifies intent into one or more domains and runs only those, in a fixed risk-first order:

| # | Module | Answers |
|---|--------|---------|
| 1 | **LIQUIDITY** | Is the macro plumbing safe? (Fed net liquidity, SOFR, MOVE, yen carry) |
| 2 | **SENTIMENT** | Is the crowd / breadth too hot or cold? (NAAIM, HF leverage, breadth, bubble score) |
| 3 | **THEME** | Is this the right part of the industry chain? (bottleneck / chokepoint scoring) |
| 4 | **SCREENER** | Which names clear the filters? (CANSLIM, VCP, value-dividend, PEAD) |
| 5 | **VALUE** | Is the business sound & honest? (ROIC, Piotroski, accounting flags, moat, dividend safety) |
| 6 | **VALUATION** | What is it worth vs price? (DCF, reverse DCF, comps, SOTP, fair-value bands) |
| 7 | **EARNINGS** | What did the quarter actually say? (beat/miss, guidance, NDR, Rule of 40) |
| 8 | **FLOW** | Is smart money / are insiders confirming? (13F, superinvestors, Form 4) |
| 9 | **TECHNICAL** | Is the chart / timing aligned? (trend template, breadth, distribution days, FTD, VCP) |
| 10 | **BTC** | Where in the crypto cycle? (MVRV, NUPL, SOPR, funding) |
| 11 | **POSITION** | How much, given edge + live portfolio? (Kelly, ATR stops, exposure ceilings) |

A **research-extras** evidence layer (analyst price targets, Morningstar / big-bank / Seeking Alpha research, an investing-master composite score, and a QGpro growth-quality score) is woven into single-name questions.

Every analysis ends with a color-coded **Investment Signal Block** (Signal · Confidence · Horizon · Score · Action · Conviction) so verdicts are consistent and comparable.

---

## Why it's accurate

deepalpha prefers **primary-source SEC data over web scraping.** For any US-company fundamental, filing, holdings, or insider data it reaches for the **SEC EDGAR MCP first** (free, no key) and only falls back to web search for things SEC can't give (live prices, analyst targets, sentiment surveys, news) — always date-stamped. If no SEC MCP is connected it says so, falls back to web, and flags that fundamentals are scraped, not primary-source. It never invents filing data.

---

## Repository layout

```
deepalpha/
├── SKILL.md                  # the router — Claude loads this first
├── README.md                 # this file
├── MERGE_NOTES.md            # how the skill was assembled from its sources
├── CREDITS.md                # full source attribution + licenses
├── LICENSE                   # MIT
├── references/               # one markdown framework per module, loaded on demand
│   ├── data-layer.md         # tool catalog + fallback ladder (loaded first when data is needed)
│   ├── liquidity.md  sentiment.md  value.md  valuation.md  earnings.md
│   ├── technical.md  flow.md  theme.md  screener.md  btc.md  position.md
│   ├── research-extras.md  investing-philosophies.md  bias-checklist.md
│   ├── output-formats.md  dashboard.md  index-glossary.md
│   └── serenity/             # canonical supply-chain method docs
├── scripts/                  # vendored, deterministic calculation engines (Python)
│   ├── position_sizer.py     # Kelly / ATR / fixed-fractional
│   ├── serenity_scorecard.py # supply-chain bottleneck scoring
│   ├── screener_vcp/  screener_canslim/
│   ├── earnings_pead/  earnings_trade/
│   ├── technical_breadth/  technical_market_top/  technical_ftd/
│   ├── technical_macro_regime/  technical_uptrend/
│   ├── theme_detector/  flow_institutional/
│   └── README.md             # which engine maps to which module
└── assets/                   # scorecard JSON, research prompt pack, thesis template
```

Only `SKILL.md` and the `references/` it pulls are loaded into Claude's context at runtime — the `scripts/` are invoked for deterministic scoring, and this README / MERGE_NOTES / CREDITS are for humans.

---

## Installation

### As a Claude skill (recommended)

Copy the `deepalpha/` folder into your skills directory:

- **Claude Code / Cowork:** drop it in your skills folder (e.g. `~/.claude/skills/deepalpha/`).
- **claude.ai (Settings → Capabilities → Skills):** zip the folder and upload it, or upload the provided `.skill` archive.

Once installed, just ask an investing question — the skill triggers automatically.

### Data backbone (optional but high-impact)

deepalpha works web-only, but accuracy jumps when an SEC MCP is connected. The **free, no-key** option (Python, `edgartools`):

```jsonc
{
  "mcpServers": {
    "edgartools": {
      "command": "uvx",
      "args": ["--from", "edgartools[ai]", "edgartools-mcp"],
      "env": { "EDGAR_IDENTITY": "Your Name your@email.com" }
    }
  }
}
```

Alternatives: `cyanheads/secedgar-mcp` (TypeScript, set `EDGAR_USER_AGENT`) or the zero-config `npx -y stockscope-mcp`. A Notion connector (live portfolio for POSITION) and a Crypto.com connector (BTC) are optional add-ons.

---

## Usage examples

| You ask | Modules that fire |
|---|---|
| "Should I buy more NVDA?" | Sentiment → Value → Valuation → Position |
| "Is the market risky right now?" | Liquidity → Sentiment → Technical (breadth) |
| "How did CRWD do this quarter?" | Earnings |
| "Which part of the AI power chain should I research?" | Theme → Screener → Value |
| "Who's accumulating this name?" | Flow (13F + insider) |
| "How much should I size this at?" | Position (Kelly + live portfolio) |
| "Where is BTC in the cycle?" | BTC → Liquidity |

deepalpha matches your input language (English → English, 中文 → 中文, mixed → mixed).

---

## Running the calculators standalone

The engines in `scripts/` are plain Python and run offline against data you supply:

```bash
python3 scripts/technical_ftd/ftd_calculator.py     # follow-through-day demo
python3 scripts/position_sizer.py                    # Kelly / ATR sizing
```

See `scripts/README.md` for the full engine → module map and which ones need a live data layer.

---

## Credits & license

deepalpha fuses methods and code from several permissively licensed projects (tradermonty/claude-trading-skills, muxuuu/serenity-skill, yennanliu/InvestSkill, himself65/finance-skills, anthropics/financial-services, OctagonAI/skills, dgunning/edgartools, and others). Full attribution and upstream licenses are in [`CREDITS.md`](CREDITS.md); the assembly history is in [`MERGE_NOTES.md`](MERGE_NOTES.md).

This repository is released under the [MIT License](LICENSE). Vendored components retain their original licenses — verify each upstream license before redistribution.

---

## Disclaimer

deepalpha is a research-support tool. It produces drafts and analysis for your review, not financial advice, and it does not execute trades or move money. Markets carry risk; you are solely responsible for your investment decisions. Verify all data — especially anything sourced from web fallback — before acting on it.
