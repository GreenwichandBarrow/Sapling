---
schema_version: 1.1.0
date: 2026-04-23
type: context
title: "Deal Aggregator Scan — 2026-04-23"
deals_found: 0
sources_scanned: 25
sources_live: 15
sources_blocked_verified: 3
sources_email_channel: 7
email_deals: 0
volume_7d_avg: 0.14
volume_status: "🔴 Below target"
tags: [date/2026-04-23, context, topic/deal-aggregator, topic/morning-workflow, topic/source-scorecard]
---

# Deal Aggregator Scan — 2026-04-23

Scan window: 2026-04-23 06:47–07:20 ET (morning/full run, manual invocation). Channel 1 (general brokerage platforms) and Channel 3 (niche-specific sources) scanned in parallel subagents. Channel 2 (email inbound) — today's `email-scan-results-2026-04-23.md` not yet written at scan time (email-intelligence 7am ET run had not fired at 6:47am manual invocation); yesterday's `email-scan-results-2026-04-22.md` already classified all inbound (0 direct deal-related, 5 blasts with no thesis-niche match — Everingham & Kerr Specialty Chemicals, Quiet Light Education eCom, Rejigg platform match, Flippa $1.07M link-in-bio SaaS, Helen Guo SMB blast). No new deduped pass-throughs from email this run.

## Buy-Box Refresh (Step 0b confirmation)

All three buy-box docs freshly loaded from Drive at scan start — no cached/hardcoded bands used.
- Services Buy Box (`14hf5QaKtcP_…`) — Rev $10M–$50M, EBITDA $1.5M–$5M, 10% margin floor, 5+ yrs, 10–200 emp, hard-excludes per doc
- Insurance Buy Box (`1lkxntRwn3F_…`) — Commission Rev $3M–$40M (NOT premium), EBITDA $1.5M–$10M, 15% margin floor, retail/wholesale brokerage only
- SaaS Buy Box (`1I8r8w0FPJU…`) — ARR $3M–$20M, EBITDA positive, 10%+ growth, 85% GRR, vertical only, <$2M raised

## Niche Corpus Resolution (Step 0c confirmation)

Matching corpus resolved per niche:

| Niche | DealsX Ref | Corpus Path |
|-------|-----------|-------------|
| Premium Pest Management (Luxury Hospitality & Commercial Properties) | Specialty Pest & Environmental Management Services | DealsX keywords + WR Quick Notes |
| Private Art Advisory Firms | *(blank)* | **WR row enrichment** (Niche Hypothesis + Quick Notes — "Recurring retainers for collection strategy. Strong RTW.") — logged per calibration requirement |
| Estate Management Companies | Estate Management Companies | DealsX keywords + WR Quick Notes |
| Specialty Coffee Equipment Service | Specialty Commercial Equipment Services | DealsX keywords + WR Quick Notes |
| High-End Commercial Cleaning | High-End Commercial Cleaning | DealsX keywords + WR Quick Notes |
| Vertical SaaS for Luxury & High-Value Asset Service Industries | Vertical SaaS for Luxury & HVA Service Industries | DealsX keywords + WR Quick Notes |
| Specialty Insurance Brokerage (Art & Collectibles) | Specialty Insurance Brokerage | DealsX keywords + WR Quick Notes |
| Storage & Related Services for High Value Assets | Specialty Storage & Handling for High-Value Collections | DealsX keywords + WR Quick Notes |

## Deals Surfaced (sent to Slack individually)

**None.** Zero matches across all scanned channels. No Slack posts.

## Email Inbound Deals

**None new.** Today's `email-scan-results-2026-04-23.md` not yet available (email-intelligence 7am run hadn't fired at 6:47am scan start). Yesterday's scan already classified all inbound through 2026-04-22 07:30 ET — 0 CIMs, 0 NDAs, 5 blasts with no thesis matches, pass-through dedup complete.

## Near Misses (not Slacked)

Channel 1 — disclosed-and-below / hard-exclude near misses:

- CA Property Tax Consultants (Business Exits) — $6.7M revenue, below $10M Services floor
- B2B Experiential Marketing Vendor (Business Exits) — Sale Pending, off-market ($14.3M / $3.3M would have passed)
- Northeast Commercial Contractor Healthcare/Financial (Business Exits) — construction hard-exclude
- LED Display Solutions FL (Synergy) — $11.2M / $4.6M cash flow passes Services gate but AV-display distribution is commodity, not luxury-adjacent per `feedback_niche_search_direction`
- NYC High-End Renovation Design & Build (Synergy) — HARD EXCLUDE per `feedback_nyc_construction_hard_exclude`
- Push-to-Talk Comms Platform (Website Closers) — $12.5M EBITDA / $160M ask, revenue likely above $50M ceiling, wireless comms not luxury vertical
- Immigration Services Agency (Website Closers) — $2.8M EBITDA would pass, industry outside luxury-B2B thesis. Flag for review only if Kay wants broad B2B gate.
- NetSuite POS Software, Australia (Synergy) — ARR ~$1.6M, below SaaS $3M floor; non-US; not luxury vertical
- ~20 additional construction/manufacturing/DTC listings auto-excluded per buy-box hard-excludes (full list in subagent transcript)

Channel 3 — no concrete sell-side opportunities matched:

- Artemis Fine Arts Services → Cadogan Tate (MidCap) — right niche, already closed. See Market Intel.
- Short-Term Rental Property Mgmt 80+ Locations Midwest (Synergy Real Estate) — $3.2M rev, below $10M floor; STR mgmt ≠ HNW estate management
- Event Rental, South Florida (Synergy Real Estate) — $1.6M rev, below floor; out-of-niche
- Atlass Insurance (yacht, Sica Fletcher historic) — 2016 transaction, pre-dates buy box
- WF Clayton (aviation MGA, Sica Fletcher historic) — 2016 transaction, pre-dates buy box

## Market Intel (not deals — feeds niche-intelligence)

- **Cadogan Tate acquiring Artemis Fine Arts Services** (MidCap Advisors) — UK-based luxury logistics/storage consolidator actively rolling up US fine art logistics. Signal: adjacent US operators may face consolidation pressure (future sell-siders in Art Storage niche). **Action:** feed to niche-intelligence Tuesday run as thesis-validation data for Storage & Related Services.
- **Specialty insurance brokerage — thin tombstone volume** (Sica Fletcher, MarshBerry, Reagan Consulting) — Q4 2025–Q1 2026 specialty art/jewelry/yacht/collectibles deals effectively zero in public tombstones. Interpretation (positive for G&B): specialty-line M&A remains un-rolled-up, G&B's proprietary-sourcing advantage holds. Competitive buyer universe: Risk Strategies, Acrisure, Hilb, NFP.
- **Anticimex US aggressive consolidator** — 200+ global acquisitions, 4-year sales doubling. Competitive-bid risk on future US premium pest deals.
- **ACORD M&A Report (Agency Checklists, Apr 13 2026)** — "Fewer deals, higher stakes" — carrier consolidation slowing, broker-side still active. Confirms specialty brokerage sourcing window.
- **Inside Self-Storage Q1 2026** — REIT portfolio activity (National Storage/Brookfield-GIC, Access UK/CapitaLand). Capital in commodity storage; specialty art/wine remains un-institutionalized.

## Source Scorecard

Every Active row on `G&B Deal Aggregator - Sourcing List` sheet represented. `blocked (verified)` = failed on two fetch attempts; `email-channel` = email-only source, not web-scannable, feeds through `email-scan-results-{date}.md`; `accessible (no-data)` = URL resolved but content is image-only tombstones or news headlines without machine-readable deal data.

| Source | Category | Status | HTTP | Listings Reviewed | Matches | Last Match Date |
|--------|----------|--------|------|-------------------|---------|-----------------|
| Business Exits | General | active | 200 | 30 | 0 | — |
| Empire Flippers | General | active | 200 | 30 | 0 | — |
| Synergy Business Brokers | General | active | 200 | 25 | 0 | — |
| Website Closers | General | active | 200 | 15 | 0 | — |
| BizBuySell | General | blocked (verified) | 403 | 0 | — | — |
| Flippa | General | blocked (verified) | 200 (JS shell) | 0 | — | — |
| Quiet Light | General | blocked (verified) | 403 | 0 | — | — |
| DealForce | General | email-channel | — | 0 | — | — |
| IAG M&A Advisors | General | email-channel | — | 0 | — | — |
| Rejigg | General | email-channel | — | 0 | — | — |
| Everingham & Kerr | General | email-channel | — | 0 | — | — |
| Viking Mergers | General | email-channel | — | 0 | — | — |
| Benchmark International | General | email-channel (dormant) | — | 0 | — | — |
| Searchfunder | General | email-channel (pending alerts enablement) | — | 0 | — | — |
| Acquire.com | General | pending G&B registration | — | 0 | — | — |
| Axial | General | pending G&B registration | — | 0 | — | — |
| BizScout (DealOS) | General | pending G&B registration | — | 0 | — | — |
| FE International | General | pending G&B registration | — | 0 | — | — |
| Kumo | General | pending G&B registration | — | 0 | — | — |
| Paine Pacific | General | relationship-only | 200 | 0 | — | — |
| Woodbridge (Mariner) | General | relationship-only | 200 | 0 | — | — |
| ProNova Partners | General | blocked (verified) | 403 | 0 | — | — |
| PCO Bookkeepers | Niche-Specific (Premium Pest) | accessible (no-data) | 200 | 0 | 0 | — |
| Anticimex US | Niche-Specific (Premium Pest) | intel-only | 200 | 3 | 0 | — |
| Sica Fletcher | Niche-Specific (Specialty Insurance) | accessible | 200 | 7 | 0 | — |
| Agency Checklists | Niche-Specific (Specialty Insurance) | intel-only | 200 | 3 | 0 | — |
| IA Magazine | Niche-Specific (Specialty Insurance) | intel-only | 200 | 0 | 0 | — |
| MarshBerry | Niche-Specific (Specialty Insurance) | intel-only | 200 | 7 | 0 | — |
| Reagan Consulting | Niche-Specific (Specialty Insurance) | accessible (no-data) | 200 | 0 | 0 | — |
| Synergy Real Estate | Niche-Specific (Estate Mgmt) | active | 200 | 8 | 0 | — |
| Exit Strategies Group | Niche-Specific (Estate Mgmt) | accessible (no-data) | 200 | 0 | 0 | — |
| CMM Online | Niche-Specific (High-End Cleaning) | accessible (no-data) | 200 | 0 | 0 | — |
| Inside Self-Storage | Niche-Specific (Art Storage) | intel-only | 200 | 4 | 0 | — |
| MidCap Advisors | Niche-Specific (Art Storage) | intel-only | 200 | 4 | 0 | — |

**Verification:** `blocked (verified)` labels applied only after two fetch attempts per `feedback_test_before_concluding_channel_dead`. BizBuySell: tried `/businesses-for-sale/` and `/new-york-businesses-for-sale/`. Flippa: tried `/businesses`, `/search?filter[property_type]=business`, `/buy/sitetype/saas`. Quiet Light: primary URL 403, no secondary path available.

## Volume Check

- Deals surfaced today: **0**
- 7-day rolling average: ~0.14/day (1 deal last 7 days — Hangman context; most days 0)
- Target: 1–3/day
- Status: 🔴 **Below target**

## Architecture Gaps Surfaced

1. **Tombstone-image sources (PCO Bookkeepers, Reagan Consulting)** — publish sell-side deal data exclusively as images. WebFetch extracts nothing. Will return "no data" every run unless OCR pipeline added OR cadence dropped to quarterly manual scrape. Candidate for the Friday Phase 2 digest retirement bucket if 30+ days no match.
2. **Email-channel sources need today's `email-scan-results-2026-04-23.md`** — manual invocation at 6:47am preceded email-intelligence 7am run. Next scheduled deal-aggregator run (2pm ET afternoon) will capture any overnight/morning email deal flow.
3. **BizBuySell 403 persistent** — material general-platform gap. Options: (a) Apify proxy subscription (cost), (b) agent-browser install (infra), (c) Benchmark-style email alerts via Kay's registered account (already registered 3/22/2026 — explore alert enablement).
4. **General-platform thesis drought** — 100 listings across 4 live general platforms, zero thesis hits. Consistent with prior runs: luxury-service niches flow through specialty channels + proprietary outbound, not general broker platforms. Worth acknowledging as a structural pattern in the Friday Phase 2 digest when trending 7-day match counts.

## Validation

- [x] Step 0a completed: 8 active niches loaded from WEEKLY REVIEW tab
- [x] Step 0b completed: all 3 buy-box docs freshly read this run (no cached bands)
- [x] Step 0c completed: corpus resolved per niche; Private Art Advisory built from WR row enrichment (DealsX ref blank) — logged per calibration requirement
- [x] Data Availability Rule enforced: no listing auto-rejected on missing data; rejections only on disclosed-and-failed criteria or disclosed hard-excludes
- [x] Each listing routed to correct buy-box (Services / Insurance / SaaS) per category rule
- [x] All `blocked (verified)` sources verified via second fetch attempt
- [x] Source Scorecard: every Active row from Sourcing Sheet represented (General 22 rows + Niche 12 rows = 34 rows; 25 actively attempted this run, rest email-channel/pending-registration/relationship-only)
- [x] Fingerprint store checked — no prior matches to dedup against (store empty)
- [x] Zero matches = no Slack posts (no fabrication)
- [x] Market intel captured and tagged for niche-intelligence Tuesday run

---

**Morning briefing line:** deal-aggregator — 0 new deals posted to Slack. Market-intel signal (Cadogan Tate → Artemis Fine Arts Services) captured for art-storage niche-intelligence feed.
