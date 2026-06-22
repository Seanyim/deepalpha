# deepalpha/scripts — vendored calculation engines

These are **real, runnable scoring engines** harvested from the source repos and folded in — not paraphrases. They back deepalpha's modules with deterministic math so verdicts are reproducible. Run them with `python` (3.10+); most need only the standard library.

## What backs which module

| Folder / file | Module | Source | Network? |
|---|---|---|---|
| `position_sizer.py` | POSITION | claude-trading-skills/position-sizer | **offline** — Kelly + ATR + fixed-fractional, caps & binding-constraint logic |
| `serenity_scorecard.py` + `../assets/bottleneck-scorecard.json` | THEME | serenity-skill | **offline** — weighted bottleneck/chokepoint score (run `--template` for the input schema) |
| `theme_detector/` | THEME | claude-trading-skills/theme-detector | offline scoring (heat, lifecycle, ranker); discovery layer expects price data |
| `screener_vcp/` | SCREENER, TECHNICAL | vcp-screener | **offline** — trend-template, VCP pattern, pivot proximity, RS, volume contraction |
| `screener_canslim/` | SCREENER | canslim-screener | **offline** — C/A/N/S/L/I/M component calculators |
| `earnings_pead/` | EARNINGS, SCREENER | pead-screener | **offline** — weekly-candle, breakout, liquidity, risk/reward |
| `earnings_trade/` | EARNINGS | earnings-trade-analyzer | **offline** — gap size, pre-earnings trend, volume, MA50/200 |
| `technical_breadth/` | TECHNICAL, SENTIMENT | market-breadth-analyzer | **offline** — trend level, MA crossover, divergence, cycle, historical context |
| `technical_uptrend/` | TECHNICAL | uptrend-analyzer | offline scoring; `sector_*` calcs expect an FMP data layer |
| `technical_market_top/` | TECHNICAL, SENTIMENT | market-top-detector | **offline** — distribution-day, leading-stock, defensive-rotation, sentiment |
| `technical_ftd/` | TECHNICAL | ftd-detector | **offline** — Follow-Through-Day state logic |
| `technical_macro_regime/` | LIQUIDITY, TECHNICAL | macro-regime-detector | **offline** — concentration, yield-curve, credit, size-factor, equity-bond, rotation |
| `flow_institutional/` | FLOW | institutional-flow-tracker | **needs a data layer** — reference orchestration (expects an FMP/`data_fetcher`); for live use, deepalpha's `flow.md` reads 13F/Form 4 directly from SEC EDGAR instead |

## Important: data layer

The source repos fetch market data from **FMP / FINVIZ / yfinance** (their `data_fetcher` modules, deliberately **not** bundled). deepalpha's design (see `references/data-layer.md`) prefers **SEC EDGAR MCP first** (free, no key) and web/connector fallback. So:

- The **pure calculators** (`*_calculator.py`, pattern/score logic) run on data you pass in — wire them to whatever source is connected.
- The few scripts that import `data_fetcher` / `data_quality` are kept as **reference implementations**; supply an FMP key + their original fetcher, or feed them data from deepalpha's data layer.

## License / attribution
See `../CREDITS.md`. All sources are MIT/Apache-2.0; calculator logic is unmodified except import-path fixes for the renamed folders.
