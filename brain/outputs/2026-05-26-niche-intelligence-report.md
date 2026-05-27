---
schema_version: 1.2.0
date: 2026-05-26
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
  - date/2026-05-26
  - output
  - output/niche-intelligence-report
  - status/draft
  - person/kay-schneider
  - company/greenwich-and-barrow
  - topic/niche-intelligence
  - topic/search-fund
  - skill/niche-intelligence
---

# Niche Intelligence Report — 2026-05-26 (Tuesday Headless Run)

## Executive Summary

The Tuesday-night gather (RECENT 14-day + HISTORICAL full-search) produced **zero net-new niches** that cleared all gates cleanly. The synthesizer's verdict reinforced the existing 15-row WEEKLY REVIEW pipeline and flagged 3 latent candidates for identifier discretion (Fine Jewelry Insurance carve-out, Art Escrow Services-not-Software, Truck Licensing & Compliance Platform). Of these, the identifier rejected 2 on overlap / market-thinness grounds and flagged **Truck Licensing & Compliance Platform (IFTA/IRP/DOT services)** as a THIN-POOL CAVEAT candidate (target count 50-200 is healthy; the caveats are single-source signal + no documented network anchor). Per headless doctrine (flag thin pools, do not gate), it was advanced through one-pager → scoring → tracker. **One niche identified and added to WEEKLY REVIEW row 16 at score 2.33/3 (78%) with explicit caveats** for the Wednesday analyst-call decision.

## Run Metadata

| Field | Value |
|---|---|
| Run mode | Tuesday headless (launchd, wrapper `scripts/run-skill.sh niche-intelligence:tuesday`) |
| Orchestrator | Claude (Chief of Staff) |
| Chatroom | `brain/traces/agents/2026-05-26-niche-intelligence.md` (~86 KB, 4 agent posts + orchestrator) |
| Niches evaluated | 3 latent candidates given full INITIAL SCREEN + TARGET TAM + MARKET TAM blocks |
| Niches identified | 1 (Truck Licensing & Compliance Platform) |
| Niches rejected | 2 (Fine Jewelry Insurance carve-out, Art Escrow Services) |
| One-pagers written | 1 |
| Scorecards written | 1 |
| Tracker updated | Yes — WEEKLY REVIEW row 16 |

## Data Sources This Week

| Track | Sources Covered | Status | Key Signals |
|---|---|---|---|
| RECENT (last 14 days, 2026-05-12 → 2026-05-26) | Web/social (last30days HN + 7 WebSearches), Newsletters (auto/subscriptions & education + auto/industry research), Granola calls (MCP unauthenticated — fallback to `brain/calls/`), Gmail deal flow + investors, Vault outputs + calls, Passive inbox | partial (Granola MCP unavailable) | Pest PE consolidation deepening (10-15x platform, 7-10x tuck-in), Commercial cleaning bifurcation toward technical segment, Funeral SaaS 9.2% CAGR, Gallagher/AssuredPartners $13.45B closed Aug 2025 (insurance exit channel intact). One single-source candidate: Truck Licensing (Helen Guo SMB Deal Hunter newsletter). |
| HISTORICAL (full search history excl. last 14 days) | Fireflies vault calls (94 pre-cutoff files), Gmail full-history (5 queries, 104 unique subjects). OneNote MCP + ChatGPT export unavailable. | partial (OneNote + ChatGPT unavailable) | 11 latent niche signals. Two strongest single-source-caveat candidates: Fine Jewelry Insurance carve-out (Hunter 2026-01-12) and Art Escrow Services (Chris Wise 1/22 + Amanda Lo Iacono 1/29). Three independent build-vs-buy MGA recommendations across 90 days flagged as recurring unanswered Lifecycle item. |

## Synthesizer Verdict (Step 1b)

> "No net-new niches; existing WEEKLY REVIEW pipeline reinforced by these signals: rows 1 (Premium Pest), 5 (High-End/Technical Commercial Cleaning), 7 (Specialty Insurance Art & Collectibles), 9/10/13/15 (insurance brokerage cluster via Gallagher exit-channel signal), 14 (Funeral Home Mgmt Software). Three latent candidates flagged for identifier discretion."

## New Niches Identified

### Truck Licensing & Compliance Platform (IFTA/IRP/DOT) — Score: 2.33/3 (78%)

**Thesis:** Fragmented specialist firms serve a regulatory-driven recurring services market — a chokepoint between trucking carriers and multi-jurisdictional state DOT/FMCSA regulators. Owner-operators and small/mid-fleet carriers outsource IFTA quarterly, IRP annual, and DOT ongoing compliance work to firms that combine regulatory expertise with per-vehicle delivery — a fragmented universe of ~600 NATSA-credentialed specialists + several hundred non-NATSA generalists.

**Signal source:** Helen Guo SMB Deal Hunter newsletter (2026-05-26, single source).

**INITIAL SCREEN (all 4 PASS):**
- Margins: Pass — 15-25% EBITDA at scale; smaller firms 10-15%
- Recurring Revenue: Pass — IFTA quarterly + IRP annual + DOT ongoing, convertible-to-recurring via per-vehicle subscription/retainer
- Industry Growth: Pass — ~5-7% (trucking employment + regulatory tightening)
- Growth TAM: Pass (extrapolated) — $1-3B US (per-vehicle × fleet-count proxy); ⚠️ extrapolation, not direct market report

**TARGET TAM:** 50-200 net acquirable firms in the $2-10M EBITDA / $5-50M revenue band (NATSA universe minus large incumbents minus sub-scale solo operators). Named examples: Foley Services (Hartford CT — Northeast in-box), Vehicle Licensing Consultants/im4trux, Compliance Navigation Specialists (CNS), Evilsizor & Associates, NATSA member network. J.J. Keller ($400M+) too large; Mike Albert is fleet-management not pure compliance.

**MARKET TAM:** $1-3B US commercial trucking compliance services. CAGR ~3-5% (trucking employment) + regulatory tailwind. Demand drivers: multi-state IFTA/IRP friction, FMCSA enforcement escalation, ELD compliance integration, owner-operator back-office outsourcing, fleet electrification creating new permitting categories.

**Detailed Scorecard (Industry — 7 categories, weighted):**

| Category | Weight | Score (1-3) | Notes |
|---|---|---|---|
| Growth, Penetration & Catalyst | 25% | 2.00 | Growth at edge of 1-3x GDP threshold; regulatory tailwind real but not a single named catalyst event |
| Size & Fragmentation | 10% | 2.50 | Thousands of players when including small permit-services firms; J.J. Keller largest but <20% share |
| Industry Economics | 10% | 2.33 | 40-55% gross / 15-25% EBITDA at scale / asset-light = high ROTC structurally |
| Mission Criticality | 15% | 2.33 | Carriers know they need it; switching costs from state DOT credentials + per-vehicle records |
| Exogenous Risks | 10% | 2.40 | FMCSA harmonization could simplify multi-state friction long-term (erodes moat); freight-cycle cyclicality |
| Porter's Five Forces | 15% | 2.40 | Low VC presence in this layer; NATSA + state DOT relationships = real entry friction |
| Value Creation Opportunities | 10% | 3.00 | Multi-state regulatory variance + under-professionalized bootstrapped operators = strongest score |
| Impact & Externalities | 5% | 2.00 | Neutral-to-mild positive (compliance enables safer trucking) |

**WEEKLY REVIEW Columns:** Margins = Medium, Recurring Revenue = High, AI Defensibility = Medium (regulatory specialization layer holds; per-vehicle filing software commoditizing), Right to Win (G&B) = **None**, Network Access = **None**.

**Artifacts:**
- One-pager (with score applied): [Truck Licensing & Compliance Platform May 2026.pptx](https://drive.google.com/file/d/1qG2dGwq4JIhZ6THPiluPizC9UHI6bD95/view) — file ID `1qG2dGwq4JIhZ6THPiluPizC9UHI6bD95`
- Scorecard xlsx: [Truck Licensing & Compliance Platform Scorecard May 2026.xlsx](https://drive.google.com/file/d/11nYns3xaLEzQQqps0-YnmbjW7kWNho95/view) — file ID `11nYns3xaLEzQQqps0-YnmbjW7kWNho95`
- Drive folder: [WEEKLY REVIEW / Truck Licensing & Compliance Platform](https://drive.google.com/drive/folders/1XnUD0ylZ-N_NRwBnNNWzrzjDpD-sbPBe) — folder ID `1XnUD0ylZ-N_NRwBnNNWzrzjDpD-sbPBe`

**Caveats for the Wednesday analyst-call decision:**
1. **Single-source signal** — Helen Guo SMB Deal Hunter newsletter is the only mention this cycle. No second-source corroboration.
2. **No documented G&B network access** — no warm path into NATSA membership or the trucking-compliance specialist community. No female-led-network anchor identified in blue-collar trucking compliance.
3. **TAM and target-count estimates are extrapolated** — per-vehicle spend × fleet-count proxy, not from PitchBook/IBISWorld/Mordor. Direct market sourcing recommended before sprint commit.
4. **Adjacent fleet-tech PE consolidation** (Geotab, Samsara, Platform Science) complicates exit channel — strategic-acquirer optionality exists but pure-play compliance services consolidation is less mature.

**Recommendation:** Analyst-call decision niche on Wednesday. Either commission a second-source pull next Tuesday before promoting, or accept the risk profile and move to Under Review.

## Rejected Niches

### Fine Jewelry Insurance Brokerage (carve-out from Art & Collectibles) — REJECT
- **Source:** Hunter Hartwell call 2026-01-12 (HISTORICAL agent).
- **Reason:** Net acquirable as standalone jewelry-only brokerage <5. Most surviving firms are multi-line specialty brokers fully captured by active row 7. Carrier-led consolidation (Jewelers Mutual via JM Insurance Agency Partners + JIBNA acquisition) foreclosing the standalone-broker path. **Disposition:** Sotheby's/Jonathan Crystal introducer lane = river-guide/network asset for row 7, not a separate row.

### Art Escrow Services (broker-not-software, distinct from KILLED Fine Art Escrow Software) — REJECT
- **Source:** Chris Wise call 2026-01-22 + Amanda Lo Iacono call 2026-01-29 (HISTORICAL agent — two independent operator-level confirmations).
- **Reason:** Same market-thinness wall that killed the software framing applies to the services framing. Net acquirable <5 after California exclusions. Growth TAM fails the $500M+ gate at the art-specific sub-vertical (~$15-30M). Per learnings.md: "Pain point exists but willingness to pay does not — recurring pattern in HNW services." **Disposition:** Amanda Lo Iacono = river-guide candidate for row 2 (Art Advisory) and row 7 (Specialty Insurance Art), not a niche-promote trigger.

## Tabled Niche Review

Reviewed all 20 TABLED niches against this week's signals. **No tabled niche has NEW data that directly addresses its original table reason.** Specifically: Pest Mgmt Compliance Software (pest signals are owner-side row 1, not compliance-software-side), Healthcare SaaS, EV Software/Charging, Yacht/Fleet Maintenance Software, Landscape Services for HNW Clients — none warrant resurface.

## Lifecycle Items Surfaced (Not Niches — G&B Decision Items)

The HISTORICAL agent flagged three recurring unanswered Lifecycle items that are NOT niche candidates but ARE pending G&B decisions:
1. **MGA build-vs-buy decision** — three independent recommendations across 90 days (Hunter Hartwell 1/12, Camilla Castro 2/4, Jeremy Black 2/15). No documented response.
2. **OneNote MCP install decision** — historical research surface remains unavailable to headless runs.
3. **Granola MCP headless-compat decision** — PKCE OAuth interactive-only; three consecutive Tuesday runs (5/12, 5/19, 5/26) have used the `brain/calls/` fallback.

## Reinforced Existing Rows (No Action — for Analyst Context)

Signals this cycle independently reinforced these active WEEKLY REVIEW rows:
- **Row 1** Premium Pest Management — PE consolidation deepening (Anticimex/Aptive/Mantle), multiples 10-15x platform / 7-10x tuck-in, NPMA Women's Forum confirming network surface
- **Row 5** High-End Commercial Cleaning — ABM/WGNSTAR $275M pivot confirms technical-segment bifurcation; sharpens niche definition
- **Row 7** Specialty Insurance Brokerage (Art & Collectibles) — jewelry insurance carve-out folds in as network asset
- **Rows 9/10/13/15** Insurance brokerage cluster — Gallagher/AssuredPartners $13.45B Aug 2025 = exit channel intact
- **Row 14** Funeral Home Management Software — 9.2% CAGR confirmed; consolidation window not yet closed

## Recommended Actions for Wednesday Analyst Call

1. **Decide on Truck Licensing.** Either (a) ADVANCE to Under Review and commission JJ/analyst second-source pull, or (b) DROP back to inbox-with-note pending second corroboration. The score (2.33) and target count (50-200) are reasonable; the gates are the single-source signal and zero network anchor.
2. **Decide on MGA build-vs-buy.** Three unanswered recommendations across 90 days = decision debt that touches insurance brokerage cluster underwriting.
3. **No tabled niches to resurface.** Confirm no override.
4. **OneNote MCP / Granola MCP availability** — operational item, not niche: install OneNote MCP or confirm research-surface gap is acceptable; resolve Granola headless OAuth path.

## Process Notes & Diagnostics

- Both gathering agents returned `Status: partial` — Granola MCP unauthenticated (PKCE OAuth headless-incompatible, third consecutive Tuesday), OneNote MCP unavailable, ChatGPT export not present at expected path. RECENT used `brain/calls/` 14-day window as Granola proxy; HISTORICAL covered 94 pre-cutoff Fireflies vault calls + 5 Gmail queries (104 unique subjects).
- Wrapper validator (`scripts/validate_niche_intelligence_integrity.py`) will check this markdown report + the JSON sidecar at `brain/trackers/niches/niche-intel-2026-05-26.json` after run exit.
- Chatroom: `brain/traces/agents/2026-05-26-niche-intelligence.md` — full multi-agent trace.
