# Index glossary — all indicators across the deepalpha modules

Load this when the user asks "what does X mean?" or wants indicator explanations.

## SENTIMENT — us-market-sentiment
| Indicator | Plain English | Threshold |
|---|---|---|
| NAAIM Exposure Index | Weekly survey: % of active fund managers' portfolios in US stocks. 0=cash, 100=fully in, 100+=leveraged | Warn >80 |
| Institutional equity allocation | State Street custodian tracks real $ flow from pension funds/SWFs globally. High = big money already in | Warn: 17yr high (Oct 2007 level) |
| Retail net buying (JPMorgan) | Daily retail investor $ into equities. Procyclical — peaks at tops, craters at bottoms | Warn: >85th historical pctile |
| S&P 500 forward P/E | Price ÷ next-12m EPS. Cost per $1 of future profit. High = less margin of safety | Warn: >22–23× |
| HF gross leverage (Goldman PB) | Hedge fund borrowed exposure as % of equity. High = forced selling cascade if market drops | Warn: near-record ~312% |

## LIQUIDITY — macro-liquidity
| Indicator | Plain English | Threshold |
|---|---|---|
| Fed net liquidity | Fed assets − TGA − ON RRP = actual money in the market pipes | Alert: drops >5%/week |
| TGA (Treasury General Account) | US Treasury's bank at the Fed. Rising = market drained. Falling = government spending = injecting | Component of net liquidity |
| ON RRP (Overnight Reverse Repo) | Money market funds parking at Fed. High = money frozen. Draining = returns to markets | Component of net liquidity |
| SOFR | Rate banks lend cash overnight using Treasuries as collateral. Spike = funding stress | Alert: >Fed upper bound + 10bp |
| MOVE Index | Bond market VIX. Treasury option implied vol. >130 = institutions forced to de-risk everything | Alert: >130 (SVB crisis: 180) |
| USDJPY / Yen carry | Borrow near-zero yen → buy US assets. Fast yen strength = forced unwind → global selloff | Alert: USDJPY −3%/week |
| US-JP 2yr spread | Profit source of yen carry. Narrowing = carry less attractive = unwind risk | Alert: narrows >50bp/month |

## VALUE — us-value-investing
| Dimension | Plain English | Target |
|---|---|---|
| ROE (Return on Equity) | Net income ÷ equity. Profit per $100 invested. Sustained >15% = genuine competitive edge | Excellent: >20% for 3+ yrs |
| Debt-to-asset ratio | Liabilities ÷ assets. Low = doesn't need borrowing. High = vulnerable to rate rises | Excellent: <30%. Warn: >70% |
| FCF quality | FCF ÷ net income. Cash that can't be faked. FCF > income = "real money" profits | Excellent: FCF >100% of income |
| Economic moat | Durable advantage: Brand (Apple), Network (Visa), Cost (TSMC), Switching cost (Salesforce) | Target: 2+ strong types |

## EARNINGS — tech-earnings-deepdive (16 modules)
| Module | Core question |
|---|---|
| A: Revenue quality | Real growth or accounting-driven? Recurring %, organic vs acquisition |
| B: Margin trends | Gross/op/net QoQ + YoY. GAAP vs non-GAAP gap >50% = investigate |
| C: Cash flow | OCF vs net income, FCF margin, buybacks vs SBC dilution |
| D: Guidance signals | Guidance vs consensus, management tone shifts, exec departures |
| E: Competitive moat | Market share, competitor multiples, moat quantified |
| F: Core KPIs | ARR, NDR (>120%=excellent), Rule of 40, book-to-bill, design wins |
| G: Product narrative | AI story real or marketing? Core product review vs user data |
| H: Supply chain | Partner risk, customer in-sourcing, frenemy dynamics |
| I: Governance | Incentive structures, insider skin-in-game, board independence |
| J: Macro impact | Rates, FX, geopolitics, US-China export controls |
| K: Valuation matrix | DCF, reverse DCF, EV/EBITDA, PEG. IRR rule: long ≥15%, short ≥25% |
| L: Ownership/insider | 13F changes, Form 4 insider trades, short interest, days-to-cover |
| M: Monitoring vars | Add/exit trigger conditions, incremental drivers, landmines |
| N: R&D pipeline | R&D % of revenue vs peers, patent activity, talent signals |
| O: Accounting quality | Accrual ratio, deferred revenue trends, off-balance-sheet items |
| P: ESG flows | Index inclusion/exclusion, capital flow screening |

**6 Philosophy perspectives**: Buffett (moat + FCF) · Baillie Gifford (10× TAM) · Tiger Cubs (GARP) · Klarman (margin of safety) · Tepper (macro + catalyst) · Druckenmiller (liquidity + asymmetric)

**Key metrics**:
| Metric | Plain English |
|---|---|
| NDR (Net Dollar Retention) | Revenue from existing customers this yr ÷ last yr. >120% = customers expand spend = excellent |
| Rule of 40 | Revenue growth % + FCF margin %. >40 = healthy SaaS. NVDA-tier: often 80+ |
| Reverse DCF | Work backwards: what growth rate does today's price imply? If implied > realistic → overvalued |
| SBC (Stock-Based Comp) | Shares paid to employees. Dilutes existing holders. SBC > 10% revenue = red flag |
| Book-to-bill | Orders received ÷ orders shipped. >1.0 = demand outpacing supply (semis signal) |
| Design wins | Customer designs built on your chip = locked-in future revenue (key for AVGO/CRDO) |

## BTC — btc-bottom-model (13 indicators, 0–100 heat score)
| Indicator | Weight | Plain English | Warn threshold |
|---|---|---|---|
| ETF daily net flow | 12pt | BlackRock IBIT + Fidelity FBTC inflows/outflows. Sustained large inflow = FOMO near top | Large sustained inflow |
| Funding rate | 8pt | Perp futures: longs pay shorts (positive=bullish bias). High = crowded = liquidation risk | >0.05% persistently |
| Fear & Greed Index | 7pt | 0-100 composite: volatility + volume + social + surveys + BTC dominance | >80 = euphoria |
| Long/short ratio | 5pt | Longs ÷ shorts on Binance/OKX. >2.0 = extreme crowding = squeeze risk | >2.0 |
| LTH-MVRV | 12pt | Long-term holder market value ÷ cost basis. <1.0 = LTH underwater = only at cycle bottoms | <1.0 = buy; >3.5 = distribute |
| NUPL | 11pt | Network unrealized P&L. Negative = majority underwater = capitulation | <0 = buy; >0.75 = sell |
| LTH-SOPR | 9pt | Long holders selling at profit (>1) or loss (<1). <1 = rare = bottom | <1.0 = bottom signal |
| STH-SOPR | 8pt | Recent buyers selling at profit or loss. Persistently <1 = bear market | <0.95 = capitulation |
| LTH supply % | 7pt | % of BTC held by long-term holders. High = accumulation. Low = distribution | >75% = bottom; <55% = top |
| 365d MA ratio | 6pt | Price ÷ 1yr moving avg. <1.0 = below annual avg = bear/buy zone | <1.0 = opportunity |
| 200w MA multiplier | 6pt | Price ÷ 200-week MA. Historically the "ultimate floor." <1.0 = generational buy | >3.5 = cycle top |
| Weekly RSI | 5pt | 14-period RSI on weekly chart. <30 = only at major bottoms historically | <30 = buy; >80 = sell |
| Volume change % | 4pt | vs 30d avg. Low volume after crash = seller exhaustion. Spike = blow-off top | 200%+ spike = climax |

**Heat score bands**: 0-15 Extreme Fear (accumulate aggressively) · 16-30 Fear (batch buy) · 31-45 Moderate Fear (start building) · 46-55 Neutral (hold) · 56-70 Moderate Greed (tighten stops) · 71-85 Greed (trim) · 86-100 Extreme Greed (exit aggressively)


---

## [deepalpha extension] Added indicators

- **Piotroski F-Score** — 0–9 financial-strength checklist (profitability, leverage, efficiency); ≥7 strong.
- **ROIC** — NOPAT ÷ invested capital; want > WACC and >15% sustained.
- **DCF / Reverse DCF** — intrinsic value from discounted FCF / the growth rate the current price implies.
- **SOTP** — sum-of-the-parts: value each segment on its own multiple.
- **Distribution day** — index −0.2%+ on higher volume; 5–6 in ~25 sessions = topping signal (O'Neil).
- **Follow-Through Day (FTD)** — index +1.5%+ on rising volume, day 4–7 of a rally = bottom confirmation.
- **VCP** — Volatility Contraction Pattern: tightening pullbacks + drying volume into a pivot (Minervini).
- **CANSLIM** — O'Neil growth screen (Current/Annual earnings, New, Supply-demand, Leader, Institutional, Market).
- **Trend template (Stage 2)** — price > MA50 > MA150 > MA200, MA200 rising.
- **13F** — quarterly institutional long holdings (45-day lag, long-only).
- **Form 4** — insider transaction filing; open-market purchases are the high-signal event.
- **NDR/NRR** — net dollar/revenue retention; >120% strong for SaaS.
- **Rule of 40** — revenue growth% + FCF margin% > 40.
- **Bubble score** — Minsky–Kindleberger 0–15 composite (put/call, VIX, margin debt, breadth, IPO heat, valuation).
- **Bottleneck score** — Serenity chokepoint strength (supplier scarcity, validation cycle, capacity, certification, purity).
- **ATR sizing** — shares = (NAV × risk%) ÷ (entry − stop).
  