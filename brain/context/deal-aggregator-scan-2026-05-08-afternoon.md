---
date: 2026-05-08
deals_found: 0
sources_scanned: 4
sources_blocked_verified: 0
sources_blocked_single_attempt: 0
email_deals: 9
buy_box_source: live
morning_artifact_present: true
---
# Deal Aggregator Scan — 2026-05-08 (Afternoon Top-Up)

## Deals Surfaced (sent to Slack individually)

None today. All afternoon email-channel listings HARD-REJECT against Services / Insurance / SaaS buy-boxes.

## Email Inbound Deals

Two cohorts processed this afternoon:

**Cohort A — Morning ordering-gap catchup (5 BLAST listings from `email-scan-results-2026-05-08.md` section 7):** Morning run at 6:00 ET preceded email-intelligence's 7:22 ET artifact write, so these were not yet visible to the morning scan.

| Source | Listing | Geo | Revenue | EBITDA | Verdict |
|---|---|---|---|---|---|
| Quiet Light (David @ QL) | Leading Fashion Blog \| 2.4M Visitors/Yr | undisclosed (online) | undisclosed | undisclosed | HARD-REJECT (consumer DTC / e-commerce content) |
| Quiet Light (Joel @ QL) | 15-Year US-Made Pet Ramp Brand | USA | undisclosed | undisclosed | HARD-REJECT (consumer DTC / e-commerce) |
| Quiet Light (Brad @ QL) | 12-Year Prepper Food Business | USA | undisclosed | undisclosed | HARD-REJECT (consumer DTC / e-commerce) |
| Everingham & Kerr | Full-service Structural Engineering, Inspection & Consulting | New Jersey | $200K | $100K cash flow | HARD-REJECT (revenue + EBITDA below floors; engineering-services category but well below $2M EBITDA practical floor) |
| Everingham & Kerr | Cloud-Based SaaS Healthcare / Regulatory Compliance | Virtual / Remote | $700K | undisclosed | HARD-REJECT (SaaS BB ARR floor + healthcare hard-exclude) |

**Cohort B — Fresh broker emails since 7:22 ET (4 individual + 1 multi-blast → 5 sub-listings):**

| Source | Listing | Geo | Revenue | EBITDA | Verdict |
|---|---|---|---|---|---|
| Everingham & Kerr | Family Medical Practice | Southern NJ | $1.5M+ | $500K+ normalized | HARD-REJECT (physician practice / provider-owned healthcare hard-exclude + revenue + EBITDA below Services BB floors) |
| Rejigg | Specialized Mortgage Lending Business | undisclosed | undisclosed | undisclosed | HARD-REJECT (lending / credit extension hard-exclude — Services BB) |
| Quiet Light (Brad @ QL) | 29-Year Clip Art Subscription Business | undisclosed (online) | $211K | $81K earnings | HARD-REJECT (digital subscription / consumer-adjacent + far below floors) |
| Tory @ Flippa | 22% Growth Events Agency | undisclosed | undisclosed | undisclosed | HARD-REJECT (events / hospitality-adjacent + marketplace cattle-call) |
| Tory @ Flippa | 84% Margin Betting Site | undisclosed | undisclosed | undisclosed | HARD-REJECT (gambling consumer DTC + marketplace cattle-call) |
| Tory @ Flippa | $6.4M Collectible Store | undisclosed | $6.4M asking | undisclosed | HARD-REJECT (consumer retail hard-exclude) |
| Tory @ Flippa | 4-Year Japanese Collectibles Brand | Japan/online | undisclosed | undisclosed | HARD-REJECT (consumer retail + non-US) |
| Tory @ Flippa | Supplement Brand (500 monthly subs) | undisclosed | undisclosed | undisclosed | HARD-REJECT (consumer DTC) |

## Near Misses (not Slacked)

None this afternoon. No listing cleared the buy-box financial gate; all hits were disclosed-and-failed (revenue/EBITDA below floor) or industry hard-exclude (healthcare, lending, consumer DTC, marketplace).

## Listings Reviewed (full log)

| Source | Headline | Geo | Revenue | EBITDA | Margin | Industry | Verdict | Reject Reason |
|--------|----------|-----|---------|--------|--------|----------|---------|---------------|
| Everingham & Kerr | Family Medical Practice | Southern NJ | $1.5M+ | $500K+ normalized | ~33% | Healthcare / Physician Practice | HARD-REJECT | Physician practice hard-exclude + revenue + EBITDA below Services BB floors |
| Everingham & Kerr | Full-service Structural Engineering, Inspection & Consulting Firm | NJ | $200K | $100K cash flow | ~50% | Engineering services / B2B services | HARD-REJECT | Revenue 50× below Services BB $10M floor; EBITDA 15× below practical $2M floor |
| Everingham & Kerr | Cloud-Based SaaS Healthcare / Regulatory Compliance Software | Virtual / Remote | $700K | undisclosed | undisclosed | Healthcare regtech SaaS | HARD-REJECT | SaaS BB ARR $3M floor + healthcare hard-exclude (cross-buybox fail) |
| Rejigg | Specialized Mortgage Lending Business | undisclosed | undisclosed | undisclosed | undisclosed | Mortgage / Lending | HARD-REJECT | Lending / credit extension hard-exclude (Services BB + Insurance BB) |
| Quiet Light | Leading Fashion Blog \| 2.4M Visitors Per Year | undisclosed (online) | undisclosed | undisclosed | undisclosed | E-commerce / content site | HARD-REJECT | Consumer DTC / online media — wrong category |
| Quiet Light | 15-Year-Old US-Made Pet Ramp Brand | USA | undisclosed | undisclosed | undisclosed | E-commerce / consumer product | HARD-REJECT | Consumer DTC hard-exclude |
| Quiet Light | 12-Year-Old Prepper Food Business \| $629 AOV | USA | undisclosed | undisclosed | undisclosed | E-commerce / consumer goods | HARD-REJECT | Consumer DTC hard-exclude |
| Quiet Light | 29-Year-Old Clip Art Subscription Business | undisclosed (online) | $211K | $81K earnings | ~38% | Digital subscription / consumer-adjacent | HARD-REJECT | Far below revenue/EBITDA floors + consumer-adjacent |
| Tory @ Flippa | 22% Growth Events Agency | undisclosed | undisclosed | undisclosed | undisclosed | Events / Hospitality-adjacent | HARD-REJECT | Hospitality-adjacent + marketplace cattle-call (per `feedback_marketplace_vs_broker_distinction`) |
| Tory @ Flippa | 84% Margin Betting Site | undisclosed | undisclosed | undisclosed | ~84% | Gambling / Consumer digital | HARD-REJECT | Consumer DTC + marketplace cattle-call |
| Tory @ Flippa | $6.4M Collectible Store | undisclosed | $6.4M asking | undisclosed | undisclosed | Consumer retail / Collectibles | HARD-REJECT | Consumer retail hard-exclude |
| Tory @ Flippa | 4-Year-Old Japanese Collectibles Brand | Japan / online | undisclosed | undisclosed | undisclosed | Consumer retail / Collectibles | HARD-REJECT | Consumer retail + non-US |
| Tory @ Flippa | Supplement Brand (500 monthly subscribers) | undisclosed | undisclosed | undisclosed | undisclosed | Consumer DTC / Supplement | HARD-REJECT | Consumer DTC hard-exclude |

## Source Scorecard

Afternoon top-up — only time-sensitive sources scanned. Morning run already covered Channels 1 (general broker platforms) + 3 (industry-specific). Per SKILL.md afternoon spec.

| Source | Category | Status | HTTP | Listings Reviewed | Matches | Last Match Date |
|--------|----------|--------|------|-------------------|---------|-----------------|
| Everingham & Kerr (email channel) | General (email-only) | active | — | 3 | 0 | — |
| Rejigg (email channel) | General (email + marketplace) | active | — | 1 | 0 | — |
| Quiet Light (email channel) | General (email-only / web Cloudflare) | active | — | 4 | 0 | — |
| Flippa (email channel — Tory blast) | General (email-only / web JS-shell) | active | — | 5 | 0 | — |

**Notes on this run's scorecard:**
- All 4 time-sensitive sources processed via email channel (the listing-bearing surface) since the morning run's 6:00 ET fire preceded the 7:22 ET email-intelligence artifact write.
- Cohort A (5 listings from morning email-scan-results section 7) processed retroactively this afternoon — the listings were known to email-intelligence but had not been forensically logged in the deal-aggregator scan artifact.
- Cohort B (5 fresh listings + 1 newsletter Rejigg Report skipped as intel-only) processed from Gmail post-7:22 ET window.
- Channel 4 (association deal boards) skipped per afternoon spec — morning sweep covers those.
- No agent-browser web scrapes this afternoon (Quiet Light Cloudflare-blocked, Flippa JS-shell — email channel sufficient).

## Volume Check

- Deals surfaced today (afternoon): 0
- Deals surfaced today (morning + afternoon combined): 0
- 7-day rolling average: 0/day (fingerprint store empty across last 7 days — `brain/context/deal-aggregator-fingerprints.jsonl` is 0 bytes)
- Target: 1-3/day — **BELOW TARGET**
- Driving factor (afternoon): 4 active broker email channels delivered 13 listings between 5/6 and 5/8 — every single one fell into a Services/Insurance/SaaS hard-exclude (healthcare, lending, consumer DTC / e-commerce, hospitality, non-US, or far below floors). No active-niche corpus matches across the afternoon set. Combined with morning run's 99 hard-rejects + 4 near-misses, today's calendar is a clean shutout — symptom of the broker-channel funnel being dominated by SBA-grade ($1-3M EBITDA, consumer/construction/healthcare) businesses that fall outside G&B's $2M practical EBITDA floor + niche corpus + industry filters. Friday digest will be Phase-2 productivity input on whether the active source set is earning its slot.
