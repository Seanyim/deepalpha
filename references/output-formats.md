# Output formats — Investment Signal Block & professional report templates

Consistent endings make verdicts comparable across time and names. Always close an analysis with the Signal Block; use the longer templates only when the user asks for a deliverable (memo, note, report, deck).

## 1. Investment Signal Block (always — render visually, never a plain ASCII box)

Two render modes; pick by context.

**A. Chat-only (no widget open).** Colored status emoji + bold so each field is scannable:

> 🟢 **Signal:** BULLISH  ·  🟡 **Confidence:** MEDIUM  ·  ⏳ **Horizon:** LONG-TERM
> **Score:** 7.4 / 10  ·  🟢 **Action:** ADD  ·  💪 **Conviction:** MODERATE

Color key — **Signal / Action:** 🟢 bullish · buy/add · 🟡 neutral · hold · 🔴 bearish · trim/sell. **Confidence:** 🟢 high · 🟡 medium · 🔴 low.

**B. Dashboard (normal case — STEP 3 already opened the widget).** Close the dashboard with this styled HTML panel (dark-theme tokens from `dashboard.md`). The Signal value is color-coded, Score is a filled progress bar, Action/Conviction are tinted chips:

```html
<div style="background:#1e1e1e;border:1px solid #333;border-radius:10px;padding:18px;max-width:520px">
  <div style="font:600 11px system-ui;letter-spacing:.08em;text-transform:uppercase;color:#8a8a8a">Investment Signal</div>
  <div style="display:flex;align-items:baseline;gap:10px;margin:8px 0">
    <!-- Signal color: green #4ade80 bull / amber #fbbf24 neutral / red #f87171 bear -->
    <span style="font:800 26px system-ui;color:#4ade80">BULLISH</span>
    <span style="font:600 13px system-ui;color:#8a8a8a">· LONG-TERM</span>
  </div>
  <!-- Score bar (7.4/10) -->
  <div style="font:600 11px system-ui;text-transform:uppercase;color:#8a8a8a;margin-top:6px">Score 7.4 / 10</div>
  <div style="background:#333;border-radius:6px;height:10px;margin:5px 0 12px;overflow:hidden">
    <div style="width:74%;height:100%;background:linear-gradient(90deg,#fbbf24,#4ade80)"></div>
  </div>
  <div style="display:flex;gap:8px;flex-wrap:wrap">
    <span style="background:#16331f;border:1px solid #2c5f3a;color:#4ade80;border-radius:6px;padding:5px 11px;font:700 13px system-ui">Action: ADD</span>
    <span style="background:#2a2a14;border:1px solid #5f5a2c;color:#fbbf24;border-radius:6px;padding:5px 11px;font:700 13px system-ui">Confidence: MEDIUM</span>
    <span style="background:#262626;border:1px solid #3a3a3a;color:#e5e5e5;border-radius:6px;padding:5px 11px;font:700 13px system-ui">Conviction: MODERATE</span>
  </div>
</div>
```
Tint each chip by its value: Action green (buy/add) / amber (hold) / red (trim/sell); Confidence green/amber/red for high/medium/low. The Score-bar fill % = score×10; its color shifts amber→green as score rises.

Score = weighted blend of the active modules' sub-scores. Confidence reflects data quality + module agreement (modules contradicting each other ⇒ lower confidence). Horizon reflects the dominant thesis (technical = short, quality compounder = long).

## 2. One-page stock memo (quick deliverable)
Thesis (2–3 lines) → Business & moat → Fundamentals & quality (Piotroski/ROIC/FCF) → Valuation (fair-value band, upside/downside) → Catalysts & timeline → Flow & technical confirmation → Risks / what breaks the thesis → Signal Block. Cite filings.

## 3. IC-memo / initiation (full deliverable, → docx/pdf)
Executive summary & recommendation · Company & industry cha