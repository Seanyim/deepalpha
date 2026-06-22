# THEME module — industry-chain decomposition & bottleneck research (Serenity method)

For "which part of the [AI / semis / CPO / robotics / power / 创新药] boom should I actually research?" Turns a hot narrative into a logic-ranked, evidence-backed shortlist. The edge: **real value in a big trend hides at the hardest-to-replace chokepoint, not the most-hyped logo.**

Fused from: serenity-skill (supply-chain bottleneck method), claude-trading-skills (theme-detector, sector-analyst), Octagon (deep multi-source research). Strong conclusions must rest on the evidence ladder below — social media is a lead, never a proof.

## Step 1 — Decompose the chain

Break the theme into layers, from end demand back to raw inputs:

```
end demand → system integration → chips / core devices → equipment → materials → packaging & test → infrastructure (power, cooling, network)
```

Map who plays where. State where the *real* incremental demand comes from (not the storyline).

## Step 2 — Find the bottleneck (chokepoint)

Score each candidate layer/company on bottleneck strength (the harder to bypass, the better the pricing power). Five tests — score 0–3 each, /15:

1. **Supplier scarcity** — few credible suppliers / high concentration.
2. **Validation cycle** — long qualification/design-in cycles that lock incumbents in.
3. **Capacity inelasticity** — hard/slow/expensive to expand (capex, lead times, tacit know-how).
4. **Certification stringency** — strict customer/regulatory qualification (autos, medical, hyperscaler).
5. **Material/purity barrier** — extreme purity, IP, or process barriers.

High score = closer to a true chokepoint with durable pricing power. Low score + lots of hype = "just renting the theme."

## Step 3 — Position vs hype (who's real)

For each candidate name: where it sits in the chain, **evidence it's a real beneficiary** (named customers, design wins, revenue mix actually exposed to the theme), and what's still just narrative. Down-rank names whose story is hot but lack order/customer/revenue proof.

## Step 4 — Theme heat & lifecycle (timing the narrative)

- **Heat (0–100):** momentum, volume, breadth of participation, uptrend ratio across the theme's names.
- **Lifecycle:** Emerging → Accelerating → Trending → Mature → Exhausting (gauge via duration, RSI extremity, valuation stretch, ETF/product proliferation, IPO/SPAC heat). Late-lifecycle + extreme valuation = research, don't chase.
- Works for **bearish themes** too (inverted indicators).

## Step 5 — Evidence ladder (strength of proof)

Rank every claim by source strength — escalate before drawing a strong conclusion:

```
strongest → company announcements · exchange filings (10-K/10-Q/8-K, 招股书/问询函) · audited financials · earnings-call transcripts
          → regulatory/project docs · patents · industry standards · tenders/能评环评
          → credible media · sell-side / specialist analysis
weakest   → social media (X/Reddit/雪球) — leads only, must be confirmed upstream
```

Use the SEC/EDGAR data layer and full-text filing search to confirm customer, capacity, and revenue claims (`data-layer.md`).

## Output — prioritized research list

```
### THEME — [theme]
Chain layers:  [demand → … → infra], real demand driver = [..]
Bottleneck ranking (each /15):
  1. [Layer/Company] — score, why it's hard to bypass, evidence, key risk
  2. ...
ETF/fund angle: [thematic products + the chain segment they're really exposed to; check top-10 holdings]
De-prioritized: [hot but unproven names + the missing evidence]
Next 3 checks: [the specific filings/metrics to verify next]
```

Hand the top 1–3 finalists to VALUE / VALUATION / FLOW for deep due diligence, and to SCREENER if you need to widen the candidate net within the bottleneck layer.

## Bundled engine
- `scripts/serenity_scorecard.py` — weighted bottleneck/chokepoint scorecard (run `--template` for the JSON schema; `--format md` for a report). Input schema: `assets/bottleneck-scorecard.json`. Thesis output: `assets/thesis-template.md`.
- `scripts/theme_detector/` — theme heat / lifecycle / industry-ranker scoring.
- Canonical method docs (real, from source): `references/serenity/evidence-ladder.md`, `deep-research-workflow.md`, `risk-and-compliance.md`.
