---
date: 2026-05-20
deals_found: 0
sources_scanned: 4
sources_blocked_verified: 0
sources_blocked_single_attempt: 2
email_deals: 0
dealsx_replies: 0
morning_artifact_present: true
---
# Deal Aggregator Scan — 2026-05-20 (Afternoon Top-Up)

Afternoon top-up run (`--afternoon`). Lightweight rescan per SKILL.md "Afternoon Run" — Channel 2 (email-driven) plus time-sensitive platforms (Rejigg, Flippa, Everingham & Kerr) only. Full Channel 1 + 3 scans skipped — morning run already covered those (118 listings reviewed, 0 buy-box-clearing thesis matches; see `deal-aggregator-scan-2026-05-20.md`).

Buy-boxes re-read live from Drive this run (Services / Insurance / SaaS — `gog docs cat` succeeded on all three doc IDs). Active niches re-read from Industry Research Tracker WEEKLY REVIEW tab — 8 active niches confirmed unchanged since morning (rows 1–8: Premium Pest, Private Art Advisory, Estate Management, Specialty Coffee Equipment Service, High-End Commercial Cleaning, Vertical SaaS Luxury, Specialty Insurance Brokerage, Specialty Storage & Handling). No mid-day edits by Kay detected. agent-browser still NOT installed (consistent with morning) — Flippa JS shell and Rejigg `/businesses` login-gated path remain blocked.

`email-scan-results-2026-05-20.md` re-read for any post-7am email inbound — no new actionable deals beyond what the morning artifact already processed. The DCA / "Project Drone" agtech teaser (Carlos Nieto, msg `19e41c8761d4c882`) remains the only broker BLAST listing of the day; Kay replied 5/19 20:34 and morning artifact logged it as FLAG / out-of-niche. Not re-surfaced here.

## Deals Surfaced (sent to Slack individually)
None today. No new matches cleared the buy-box gate AND matched an active niche corpus in the afternoon window. No Slack posts to `#active-deals` this run.

## Email Inbound Deals
None today. No new CIM, broker blast, or teaser landed in the afternoon window beyond the morning-captured DCA "Project Drone" (already FLAGged, Kay already replied). No `BOOKKEEPER-PL-CHAIN`, no Active-Deal stage-3-9 trigger, no NDA confirmation, no new sell-side teaser.

## DealsX Proprietary Outreach Replies
None today. No new "Prospect Geni" / `dealsx.notifaction@gmail.com` lead notification landed in the afternoon window. Fingerprint store still carries `0e5d5fd7…` (Bruyere/Tristate STL, 2026-05-17) and `149e3b2c…` (Mitidieri/emiliomiti, 2026-05-18) — both inside 30-day TTL, dedup active, not re-surfaced.

## Near Misses (not Slacked)
- Rejigg `/businesses` route — gated (JS-shell / login-required on `WebFetch`); no active listings retrievable without agent-browser. Standing remediation: install agent-browser (morning artifact noted same gap).
- Rejigg homepage — 7 recent-closing tombstones surfaced ($1.8M farming, $4.2M consultancy PE buyer, $4.2M SaaS search-fund, $3.1M B2B services, $950K home services, manufacturing PE-backed, $2.4M logistics). All are completed-transaction stats with NO entity/geography/industry granularity — market-color only, not listings to flag. Logged in Listings Reviewed below as FLAG / intel-only-tombstone.
- Flippa SaaS browse — JS shell, no server-rendered listings on `WebFetch`. Blocked single-attempt; email subscription remains active path (no Flippa blast in email-scan-results today).
- Everingham & Kerr — email-only channel; no new blast in `email-scan-results-2026-05-20.md` since the 7am scan. Active via email when blasts arrive; quiet today.

## Listings Reviewed (full log)

| Source | Headline | Geo | Revenue | EBITDA | Margin | Industry | Verdict | Reject Reason |
|--------|----------|-----|---------|--------|--------|----------|---------|---------------|
| Rejigg (homepage tombstone) | Farming operation closed to PE buyer | undisclosed | $1.8M asking | undisclosed | undisclosed | Farming/agriculture | FLAG | intel-only tombstone — no entity/geography detail; closed transaction, not active listing |
| Rejigg (homepage tombstone) | Consultancy closed to strategic buyer | undisclosed | $4.2M asking | undisclosed | undisclosed | Consulting | FLAG | intel-only tombstone — closed transaction, no entity detail |
| Rejigg (homepage tombstone) | SaaS closed to search fund | undisclosed | $4.2M asking | undisclosed | undisclosed | SaaS (unspecified vertical) | FLAG | intel-only tombstone — no vertical detail, cannot route to SaaS buy-box |
| Rejigg (homepage tombstone) | B2B services closed to individual buyer | undisclosed | $3.1M asking | undisclosed | undisclosed | B2B services | FLAG | intel-only tombstone — closed transaction, no entity detail |
| Rejigg (homepage tombstone) | Home services closed to strategic buyer | undisclosed | $950K asking | undisclosed | undisclosed | Home services | FLAG | intel-only tombstone — below rev floor + closed transaction |
| Rejigg (homepage tombstone) | Manufacturing closed to PE-backed buyer | undisclosed | undisclosed | undisclosed | undisclosed | Manufacturing | FLAG | intel-only tombstone — no detail, closed transaction |
| Rejigg (homepage tombstone) | Logistics closed to strategic buyer | undisclosed | $2.4M asking | undisclosed | undisclosed | Logistics | FLAG | intel-only tombstone — closed transaction, no entity detail |

## Source Scorecard

| Source | Category | Status | HTTP | Listings Reviewed | Matches | Last Match Date |
|--------|----------|--------|------|-------------------|---------|-----------------|
| Rejigg | General (email-only; web tombstones) | active (homepage tombstones); `/businesses` blocked (single-attempt) | 200 / 404 | 7 | 0 | — |
| Flippa | General | blocked (single-attempt — JS shell, no agent-browser) | 200 (JS shell) | 0 | 0 | — |
| Everingham & Kerr | General (email-only) | active (email) — quiet today | n/a | 0 | 0 | — |
| Email channel (email-scan-results) | Inbound | active | n/a | 0 (no new since morning) | 0 | — |

## Volume Check
- Deals surfaced today (combined morning + afternoon): 0
- 7-day rolling average: 0.14/day (unchanged from morning run — afternoon added no new matches)
- Target: 1–3/day — **BELOW TARGET**

Afternoon top-up confirms the morning verdict: persistent volume gap, same drivers (agent-browser unavailable → BizBuySell/Quiet Light/Flippa/businessesforsale blocked; specialty insurance market saturated by consolidator roll-ups; niche-specific sources surfacing tombstones rather than live listings). No mid-day intervention possible from this run — agent-browser install + Rejigg `/businesses` login walkthrough remain the standing remediations, surfaced via the Friday digest, not this top-up's deliverable.
