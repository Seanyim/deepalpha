# Dashboard spec — deepalpha visualization (mandatory, reproducible)

This is the **authoritative layout** for STEP 3. Render one combined dashboard with `visualize:show_widget` (HTML mode). If `visualize:read_me` is available, load `["mockup","chart","data_viz"]` first. Reproduce this structure faithfully — it is the house style.

## Design tokens (dark, fixed)
Use hex inside `<canvas>` (CSS vars don't resolve there); CSS vars elsewhere ok.
- Surface: page transparent · card `#1e1e1e` · card border `#333` · callout border `#3a3a3a`
- Text: heading `#e5e5e5` · **label** small UPPERCASE `#8a8a8a` · value bold white `#fafafa` · muted `#8a8a8a`
- Semantics: hot/down/warn **red** `#f87171` · caution **amber** `#fbbf24` · good/up **green** `#4ade80` · neutral `#d4d4d4`
- Series: A=`#60a5fa` (blue) · B=`#4ade80` (green) · C=`#f472b6` (pink)
- Card radius 10px · padding 16px · grid gap 12px · font system-ui

## Layout skeleton (top → bottom, render only sections whose module is active)
1. **One-line preamble** in chat before the widget (e.g. "Data's in — here's the dashboard."). Keep it short, never narrate tool calls.
2. **KPI strip** — header `Macro snapshot — [Month Year]`, then a responsive row of 3–5 metric cards. Always include whichever of these the active modules produced: CPI YoY, SOFR, S&P fwd P/E, NAAIM, MOVE, Fed net-liq Δ. Each card = label · big color-coded value · sublabel/threshold. Color the value by its threshold (e.g. NAAIM 77 amber, >80 red; fwd PE >20 amber, >22 red; CPI hot = red).
3. **Status callouts** — wide cards, one per macro module active: `LIQUIDITY` (icon ⚠️/✅ + verdict + one-line rationale) and `SENTIMENT` (icon 📈/📉 + verdict + `X/5 warnings · note`).
4. **Module panels** (in execution order, each only if active):
   - **VALUE** → radar, axes ROE / Debt safety / FCF quality / Moat, scale 0–3. Supports **multi-name comparison**: overlay one dataset per name, legend shows `NAME — score/12 (grade)`. (See radar snippet.)
   - **EARNINGS / price context** → "from ATH" cards: header `NAME — from ATH $X`, hero = big color-coded `−Y%`, sublabel `~$price · P/E ~N · <one-line fact>`.
   - **SENTIMENT** → 5 horizontal bars (NAAIM, instit alloc, retail, fwd PE, HF leverage) with warn-zone marker; X/5 badge.
   - **LIQUIDITY** → 4 traffic-light cards (Fed net-liq, SOFR, MOVE, USDJPY) + net-liq component breakdown.
   - **BTC** → 0–100 heat thermometer; daily pulse (0–32) vs weekly structure (0–68); top-3 extreme readings.
   - **POSITION** → current-vs-target weight bars per holding; cap/sector breach flags (red); Kelly `f*` vs fractional-target gauge; trade-ticket card (`NAME · $amt · N shares · cash after`).
5. **Action chips** — pill buttons (`text ↗`) wired to `sendPrompt()` for drill-down, e.g. "Action Price at 15% IRR ↗", "Size this with Kelly ↗".
6. **Combined verdict card** at the bottom when ≥2 modules active.
(Router decision + full module reports are prose in chat, below the widget.)

## Chart.js
`https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.js` · `responsive:true, maintainAspectRatio:false` · custom HTML legends (not Chart.js default) · metric cards above charts.

## Card pattern (HTML)
```html
<div style="background:#1e1e1e;border:1px solid #333;border-radius:10px;padding:16px">
  <div style="font:600 11px system-ui;letter-spacing:.06em;text-transform:uppercase;color:#8a8a8a">S&P FWD P/E</div>
  <div style="font:700 28px system-ui;color:#fbbf24;margin:4px 0">21.1</div>
  <div style="font:400 12px system-ui;color:#8a8a8a">10y avg 18.9</div>
</div>
```
KPI strip wraps these in `display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px`.

## Status callout pattern
```html
<div style="background:#1e1e1e;border:1px solid #3a3a3a;border-radius:10px;padding:16px">
  <div style="font:600 11px system-ui;text-transform:uppercase;color:#8a8a8a">Liquidity</div>
  <div style="font:700 16px system-ui;color:#fbbf24;margin:6px 0">⚠️ Slightly tight</div>
  <div style="font:400 13px system-ui;color:#8a8a8a">Plumbing fine; inflation re-pricing the rate path</div>
</div>
```

## Comparison radar (Chart.js, multi-name)
```js
new Chart(ctx,{type:'radar',
 data:{labels:['ROE','Debt safety','FCF quality','Moat'],
  datasets:[
   {label:'WMT',data:[2,2,2,2],borderColor:'#60a5fa',backgroundColor:'rgba(96,165,250,.15)',pointBackgroundColor:'#60a5fa'},
   {label:'COST',data:[3,3,3,3],borderColor:'#4ade80',backgroundColor:'rgba(74,222,128,.12)',borderDash:[5,4],pointBackgroundColor:'#4ade80'}
  ]},
 options:{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false}},
  scales:{r:{min:0,max:3,ticks:{stepSize:1,color:'#8a8a8a',backdropColor:'transparent'},
   grid:{color:'#333'},angleLines:{color:'#333'},pointLabels:{color:'#e5e5e5',font:{size:12}}}}}});
```
Render a custom HTML legend above it: `■ WMT — 8/12 (B)   ■ COST — 12/12 (A)` using the series colors.

## Action chip + sendPrompt
```html
<button onclick="sendPrompt('Walk me through the action price at a 15% IRR')"
 style="background:#262626;border:1px solid #3a3a3a;border-radius:8px;padding:8px 14px;
 color:#e5e5e5;font:600 13px system-ui;cursor:pointer">Action Price at 15% IRR ↗</button>
```

## Rules
- Never skip the dashboard when any module ran. Match the user's language in all labels.
- Only show panels for active modules; a single-stock VALUE question = radar + ATH card, no macro strip.
- Color is semantic, not decorative — green good / amber caution / red warn|down. Keep it information-dense and calm (no gradients, no emoji spam).

---

## [deepalpha extension] Added panels

Render only for active modules, same dark-theme tokens & Chart.js setup as above:

- **TECHNICAL** — price line + MA50/150/200 overlay, RSI sub-panel; mark support/resistance/pivot/stop. Market-tape strip: breadth %, distribution-day count, FTD flag, bubble phase gauge.
- **FLOW** — diverging bars: institutional net QoQ (tier-weighted) and insider net buy/sell; tag top holders.
- **THEME** — horizontal supply-chain ladder (demand→infra) with each layer's bottleneck score as a heat bar; finalists highlighted.
- **SCREENER** — ranked comparison table (Grid.js or HTML table) with composite scores; per-column leader highlighted.
- **VALUATION** — football-field horizontal bars (bear/base/bull fair-value bands) with a marker at current price.

- **ANALYST TARGETS** — horizontal price-target bracket: a track from low→high target with markers for low, mean (bold), high, and current price; sublabel `N analys