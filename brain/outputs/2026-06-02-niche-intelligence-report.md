---
schema_version: 1.2.0
date: 2026-06-02
type: output
output_type: niche-intelligence-report
status: draft
skill_origin: niche-intelligence
people:
  - "[[entities/kay-schneider]]"
companies:
  - "[[entities/greenwich-and-barrow]]"
projects: []
tags:
  - date/2026-06-02
  - output
  - output/niche-intelligence-report
  - status/draft
  - person/kay-schneider
  - company/greenwich-and-barrow
  - topic/niche-intelligence
  - topic/search-fund
  - skill/niche-intelligence
---

# Niche Intelligence Report — 2026-06-02 (Tuesday Headless Run)

## Executive Summary

The Tuesday-night gather (RECENT 14-day + HISTORICAL full-search) produced **two niches advanced to WEEKLY REVIEW**, both clearing all four INITIAL-SCREEN gates. The synthesizer's convergence report reinforced the existing 16-row pipeline and surfaced six candidate signals; the identifier advanced two on independent data and explicitly held back four (one as a one-off-target-not-a-niche, three on soft/hard excludes), while confirming three DEAD/KILLED leads were not resurfaced.

- **Fine-Art Logistics Services — 2.39/3 (79.6%), PROMISING.** The strongest net-new of the cycle. This is the *asset-light services layer only* (crating, fine-art trucking, installation/rigging, customs brokerage) — a deliberate re-scope that strips out the capital-intensive, low-margin storage business that `learnings.md` repeatedly flags as incompatible with the search-fund model. It is the single richest cross-source signal (6+ sources, hard economics, named comps, named warm-intro path via Warren Chan/Anacapa ~June 9). **Decision flagged for the analyst call: treat as a services-only re-scope of tracked #8 (Storage for HVA) or carry as net-new — do not double-count.**
- **Insurance FMO/IMO Distribution-Aggregator — 2.20/3 (73.5%), MODERATE / probe-gated.** Structurally attractive (capital-light override economics, high recurring, 4/4 screen pass, annuity tailwind) but advanced as a one-pager + **target-discovery probe** because the named-target pool is thin (single historical source, no live target) and the top tier is consolidating (Integrity/AmeriLife/Simplicity). The play, if any, is mid/small tier below the Big Three.

No organic net-new niches surfaced beyond the candidate pool above; the rest of the cycle's value was **reinforcement of existing rows** with fresh quant and a hard **lifecycle flag** preventing dead leads from re-entering as live recommendations.

## Run Metadata

| Field | Value |
|---|---|
| Run mode | Tuesday headless (launchd, wrapper `scripts/run-skill.sh niche-intelligence:tuesday`) |
| Orchestrator | Claude (Chief of Staff) |
| Chatroom | `brain/traces/agents/2026-06-02-niche-intelligence.md` (RECENT + HISTORICAL + synthesizer + identifier + 2 one-pager + scorer + tracker posts) |
| Niches evaluated | 6 candidate signals given screen/convergence treatment |
| Niches identified (advanced) | 2 (Fine-Art Logistics Services, Insurance FMO/IMO Distribution-Aggregator) |
| Niches surfaced-not-advanced | 4 (heat-transfer label mfg, carpet/flooring install, warranty-pipe install, VA-benefits consultancy) |
| DEAD/KILLED confirmed not resurfaced | 3 (whole-firm insurance acquisition, pure art advisory standalone, art-tech platforms) |
| One-pagers written | 2 |
| Scorecards written | 2 |
| Tracker updated | Yes — WEEKLY REVIEW ranks 17 & 18 (sheet rows 20 & 21) |
| Runtime | ~1,300s |

## Data Sources This Week

**RECENT track — COMPLETE (all 6 sources reached).** last30days returned mostly noise on niche-specific queries (Reddit 0 items; HN entity-miss) — WebSearch carried niche market data. Granola MCP unauthenticated in headless (PKCE OAuth, standing constraint) — `brain/calls/` (14 files in window) used as proxy. Newsletters (`auto/subscriptions & education` + `auto/industry research`), Gmail (`auto/deal flow` + `auto/investors`), vault outputs/calls, and passive inbox all complete.

**HISTORICAL track — PARTIAL (2 of 4 clusters reached).** Historical calls (~50 substantive notes ≤2026-05-19) and Gmail full-history (5 query sets) COMPLETE. **OneNote MCP UNAVAILABLE** (not installed in this environment — recurring headless gap). **ChatGPT export UNAVAILABLE** (`~/Downloads` absent; no `selected_business_conversations.json` on disk — recurring headless gap). These two gaps are the same as the 2026-05-26 run and warrant a standing infra decision (see Open Loops).

## Niches Advanced

### 1. Fine-Art Logistics Services — 2.39/3 (PROMISING)

**Thesis:** The asset-light services layer of the fine-art supply chain — bespoke crating, climate-controlled fine-art trucking, white-glove installation/rigging, and fine-art customs brokerage — sits at a referral-locked chokepoint for galleries, museums, collectors, and estates. Unlike storage (capital-intensive, ~5-16% margins, project-based), the services layer runs 15-25% EBITDA on an asset-light footprint with ~60% of revenue convertible to retainer/contract via gallery and estate relationships. G&B's art-world network and luxury-client-service credibility are a direct right-to-win.

| Field | Value |
|---|---|
| INITIAL SCREEN | **4/4 PASS** — Margins (Moderate, 15-25%), Recurring (Moderate, ~60% convertible), Growth (Moderate, ~4-5% CAGR), TAM (Pass, US services ~$1-2B) |
| Industry score | 2.39/3 — leads on Mission Criticality (3.0) and Impact (3.0) |
| Margins | Medium (15-25%) · Recurring: Medium · AI Defensibility: High · RTW (G&B): Strong · Network Access: Strong |
| Target pool | ~150-300 US operators, majority owner-run; ~5-8 PE platforms (UOVO, Crozier/Iron Mountain, Cadogan Tate). PE risk Medium |
| Market TAM | ~$1-2B US services slice (of ~$3.5-4B global), ~4-5% CAGR |
| Caveats | Weight install/customs over labor-heavy trucking; screen single-owner (multi-partner = deal-killer per Acumen lesson). **Re-scope vs net-new decision for the analyst call — do not double-count vs #8.** Warm access: Warren Chan/Anacapa ~June 9. |
| Drive folder | `1cwIJl72r8nak7hReixXVOYtdj4gHsjPb` |
| One-pager | file `1KpO70vnxYlS_cwNsDgqGzmteDRY11ZIa` |
| Scorecard | file `1fZxFGvKxtrcG4JyC7yltWnE2ZN7iV6Hs` |

### 2. Insurance FMO/IMO Distribution-Aggregator — 2.20/3 (MODERATE, probe-gated)

**Thesis:** Field/Independent Marketing Organizations are the wholesale distribution layer that sits between carriers and independent annuity/life agents, earning override commissions on agent production. The model is capital-light (no reserves/underwriting/balance sheet), the override + renewal/trail stream recurs with the agent network's in-force block (no book-portability problem), and the annuity wave (US retail annuity sales $464.1B in 2025, +7% YoY, 4th straight record) is a structural tailwind. Distinct from the retail-brokerage cluster (#7/#10/#13) — this is the upstream distribution layer.

| Field | Value |
|---|---|
| INITIAL SCREEN | **4/4 PASS** — Margins (Very High, capital-light overrides), Recurring (High), Growth (Moderate, ~5-7% CAGR), TAM (Pass, multi-$B override layer) |
| Industry score | 2.20/3 — leads on Industry Economics (2.67); dragged by regulatory risk + thin validated pool |
| Margins | Very High · Recurring: High · AI Defensibility: Medium · RTW (G&B): Moderate · Network Access: Some/Thin |
| Target pool | Hundreds of FMO/IMO/BGAs nationally (fragmented long tail) but **thin NAMED pool** — single historical source, no live target |
| Market TAM | Multi-$B override layer on top of $464B annuity flow + life/Medicare; ~5-7% CAGR |
| Caveats | **PROBE-GATED** — advance one-pager + target-discovery probe before channel commitment. Big-Three consolidation (Integrity/Silver Lake; AmeriLife/Genstar+THL; Simplicity/Lee Equity) = play mid/small tier. Watch carrier disintermediation; confirm B2B agent-network economics. |
| Drive folder | `1se2WtUaF11jY3iDvgsgjQGmVuDDFJV8i` |
| One-pager | file `1QfEL9glJSz87X9E8famSHiDOW9nWFqr-` |
| Scorecard | file `1cdBW9emWbutPqtW6FWxiYA78RSyqap25` |

## Surfaced But Not Advanced

| Candidate | Reason held back |
|---|---|
| Heat-transfer / on-demand label & decoration manufacturing | Validation killed niche-level fit: capital-intensive printing/converting, only moderately fragmented (top-5 ~55%). The 30%-margin firm G&B diligenced Feb 2026 is an **outlier = one-off target, not a niche thesis**. Flagged, not auto-killed. |
| Carpet/flooring installation (NJ) | Construction-adjacent soft-exclude. Surfaced from Matt Luczyk (Peapack) as a directed signal; flag at any future screen. |
| Insurance-fed warranty-pipe installation | Construction-trades + residential B2B2C; fails core excludes. |
| VA-benefits consultancy | Near-DEAD: likely B2C + severe regulatory headwind (CA fee-ban end-2026, LA fee caps) + "claims sharks" reputational stigma. No PE-acquisition activity. |

## Lead Lifecycle — Confirmed Dead/Killed (not resurfaced)

- **Whole-firm insurance brokerage acquisition at G&B size — DEAD.** Repeatedly challenged (Hunter Hartwell empty-handed at 12-14x, Chris Wise, Tobias, investor QSBS/multiple pushback) with a recurring "build don't buy" counter-thesis. Viable residue = carve-out / one specific anti-PE personal-lines target / Midwest-to-NY geographic arbitrage — NOT whole-firm.
- **Pure art advisory standalone — DEAD** (Margot Romano). Survives only as advisory + services.
- **Art-tech / transaction platforms — KILLED** (prior cycles; low TAM, low willingness-to-pay).

## Reinforcement of Existing Pipeline

- **#1 Premium Pest Management** — US market ~$29.7B (2026), 34,000+ firms, multiples +0.5x YoY on PE consolidation; Matt Luczyk corroborated "still very high." Strong exit/comp + women-network value; direct acquisition faces PE-owned-target / premium-bid pricing risk → favor sub-platform targets.
- **#5 High-End Commercial Cleaning** — live Axial teaser (Multi-Market Commercial Cleaning Services Provider, 6/2) in the deal-flow inbox.
- **#7/#9/#10/#13 Insurance cluster** — avg ~11.4x for >$1M EBITDA deals; PE momentum regaining with rate cuts; exit channel intact. Investor Warren Chan (Anacapa) actively interested in "services to the art world and their fit with the search-fund model" (meeting ~June 9) — validates art-advisory/art-insurance cluster AND the new Fine-Art Logistics entry.
- **#12 Truck Licensing & Compliance** — second independent sighting (Helen Guo deal-hunter listing), though the listed firm is California (hard-exclude geography).
- **Macro tailwind** — SBA walked back the "one-strike" rule for minority investors effective June 1 (waivers when investor owned <20%, non-guarantor, no control), easing acquisition financing for ETA/search-fund deals.

## New River-Guide / Network Assets

- **Warren Chan (Anacapa)** — investor, warm, interested in art-world services fit; meeting ~June 9. Access path for Fine-Art Logistics + art cluster.
- **Matt Luczyk (Peapack IB)** — offered to be a multiples-benchmark resource for any industry; June 16 Peapack owner event (Summit NJ); insurance-industry contact intro offered.
- **G&B family network contact (marine logistics)** — warm access to trade-credit/cargo-insurance brokers (#9 Trade Credit/Customs Bonds/Cargo Insurance).

## Open Loops / Infra Decisions (recurring)

1. **OneNote MCP not installed for headless runs** — 2nd+ consecutive Tuesday the historical INDUSTRY MEMOS / CONFERENCE LISTS surface is unavailable. Decision needed: install MCP, build a vendor-API path, or accept the gap.
2. **ChatGPT export path absent** (`~/Downloads/...selected_business_conversations.json`) — historical ChatGPT cluster unavailable. Decision: relocate the export to a stable repo path or retire the source from the sub-agent registry.
3. **Granola MCP headless-incompatible** (PKCE OAuth interactive-only) — `brain/calls/` proxy used for a 3rd+ Tuesday. Decision: headless-compatible auth or formalize the proxy.

These are surfaced for the Wednesday analyst call; none blocked this run.

## Machine-Readable Summary

```yaml
run_date: 2026-06-02
run_mode: tuesday
niches_evaluated: 6
niches_identified: 2
one_pagers_written: 2
scorecards_written: 2
tracker_updated: true
niches:
  - name: Fine-Art Logistics Services
    score: 2.39
    initial_screen: 4/4 PASS
    target_pool: "150-300"
    weekly_review_rank: 17
    drive_folder: https://drive.google.com/drive/folders/1cwIJl72r8nak7hReixXVOYtdj4gHsjPb
    verdict: PROMISING — strongest net-new; services-only re-scope of #8 (analyst call decides re-scope vs net-new)
  - name: Insurance FMO/IMO Distribution-Aggregator
    score: 2.20
    initial_screen: 4/4 PASS
    target_pool: "Hundreds (thin NAMED pool)"
    weekly_review_rank: 18
    drive_folder: https://drive.google.com/drive/folders/1se2WtUaF11jY3iDvgsgjQGmVuDDFJV8i
    verdict: MODERATE — probe-gated; thin named pool + Big-Three consolidation
```

## Related

- Chatroom trace: [[traces/agents/2026-06-02-niche-intelligence]]
- Prior cycle: [[outputs/2026-05-26-niche-intelligence-report]]
- Entity: [[entities/greenwich-and-barrow]] · [[entities/kay-schneider]]
