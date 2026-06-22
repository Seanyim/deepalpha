# deepalpha — how this skill was assembled

> **This file documents how deepalpha was merged from its source projects.** For installation and usage, see [`README.md`](README.md). Full source attribution is in [`CREDITS.md`](CREDITS.md).


**deepalpha** is the merged successor to your `deep2invest` skill. It keeps deep2invest's router + dashboard architecture and your calibrated thresholds, then fuses in the strongest methods from the ten source projects you listed — de-duplicated so each capability keeps the best version, not the most recent one. Your original `deep2invest` is untouched as a backup.

> Research support only — drafts for your review, not investment advice. No trade execution.

## What changed vs deep2invest

**6 modules → 11**, plus a primary-source data backbone and a consistent output contract.

| deep2invest | deepalpha |
|---|---|
| SENTIMENT, LIQUIDITY, VALUE, EARNINGS, BTC, POSITION (inline) | LIQUIDITY, SENTIMENT, **VALUE**, **VALUATION** (new, split out), EARNINGS, **TECHNICAL** (new), **FLOW** (new), **THEME** (new), **SCREENER** (new), BTC, POSITION (now its own module) |
| All data via web search | **STEP 0 data backbone** — SEC EDGAR MCP first (free, no key) for fundamentals/13F/Form4/8-K; web only as fallback |
| Dashboard only | Dashboard + **Investment Signal Block** + professional report templates |

## Where each source repo landed

- **edgartools · secedgar-mcp · stockscope-mcp** → `data-layer.md` (the free, no-key SEC primary-source backbone) — powers VALUE, VALUATION, EARNINGS, FLOW, SCREENER.
- **InvestSkill** (21 frameworks) → Piotroski/ROIC into VALUE; DCF/comps/SOTP/reverse-DCF into VALUATION; insider/13F into FLOW; the **Investment Signal Block** into `output-formats.md`; result-validator into `bias-checklist.md`.
- **claude-trading-skills** (tradermonty) → `technical.md` (trend template, breadth, market-top/FTD, bubble, VCP), `screener.md` (CANSLIM/VCP/value-dividend/PEAD), `flow.md` (institutional-flow tier framework), ATR/exposure into `position.md`, backtest discipline into `bias-checklist.md`, Druckenmiller/O'Neil/Minervini into `investing-philosophies.md`.
- **finance-skills** (himself65) → SaaS compression & earnings preview/recap into `earnings.md`; SEPA into `technical.md`; SOTP triangulation into `valuation.md`; social sentiment into `sentiment.md`.
- **serenity-skill** → `theme.md` (industry-chain decomposition, bottleneck scoring, evidence ladder).
- **Octagon (skills + MCP)** → deep multi-source research / transcripts into `theme.md` + `earnings.md`; listed in the data-layer ladder.
- **anthropics/financial-services** → professional report templates (IC memo, initiation, comps, earnings note) into `output-formats.md`; premium MCP connectors noted in the data-layer ladder.

Overlaps were collapsed: position sizing (deep2invest Kelly + tradermonty ATR/fixed-fractional + InvestSkill portfolio-review) → one `position.md`; insider/13F (InvestSkill + tradermonty + EDGAR parsers) → one `flow.md`; valuation (deep2invest valuation-models + InvestSkill DCF + finance-skills triangulation) → one `valuation.md`.

## Recommended data backbone (optional but high-impact)

deepalpha works web-only, but accuracy jumps when an SEC MCP is connected. The **free, no-key** option:

```jsonc
// edgartools (Python) — financials, 13F, Form 4, 8-K, XBRL frames
{ "mcpServers": { "edgartools": {
  "command": "uvx",
  "args": ["--from", "edgartools[ai]", "edgartools-mcp"],
  "env": { "EDGAR_IDENTITY": "Sean Yim seanyim99@gmail.com" } } } }
```

or the TypeScript alternative (cyanheads/secedgar — set `EDGAR_USER_AGENT="Sean seanyim99@gmail.com"`), or the zero-config `stockscope-mcp` via `npx -y stockscope-mcp`. The Notion connector (portfolio) and Crypto.com connector (BTC) are reused from deep2invest.

## Install

Copy the `deepalpha/` folder into your skills directory (`~/.claude/skills/` or the Cowork skills folder), or upload the `deepalpha.skill` zip via **Settings → Capabilities/Skills**. Only `SKILL.md` + `references/` are loaded; this README is for you.

## Files

`SKILL.md` (router) · `references/`: data-layer, liquidity, sentiment, value, valuation, earnings, technical, flow, theme, screener, btc, position, **research-extras**, investing-philosophies, bias-checklist, output-formats, dashbo