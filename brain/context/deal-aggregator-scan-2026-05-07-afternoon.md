---
date: 2026-05-07
deals_found: 0
sources_scanned: 4
sources_blocked_verified: 0
sources_blocked_single_attempt: 1
email_deals: 0
run_mode: afternoon
morning_artifact_present: true
---
# Deal Aggregator Scan — 2026-05-07 (Afternoon Top-Up)

Lightweight afternoon rescan (`--afternoon` flag): time-sensitive email-driven channels only (Everingham & Kerr afternoon blasts, Rejigg afternoon listings/email, Flippa afternoon email). Full Channel 1 + 3 platform sweep ran in this morning's 6am artifact (`brain/context/deal-aggregator-scan-2026-05-07.md`) and is intentionally skipped here.

Buy-boxes re-read live from Drive (Services / Insurance / SaaS) at run start. Active niches re-read from Industry Research Tracker WEEKLY REVIEW.

## Deals Surfaced (sent to Slack individually)

None today.

## Email Inbound Deals

None today. (One Everingham & Kerr afternoon BLAST landed — Cloud-Based SaaS Healthcare / Regulatory Compliance Software, $700K revenue, virtual/remote — out of buy-box: ARR $700K << $3M SaaS floor, disclosed-and-failed. Logged for broker-channel volume tracking only.)

## Near Misses (not Slacked)

None this afternoon. The single new listing (Everkerr SaaS Healthcare) fails the SaaS financial gate on a disclosed-and-failed criterion (ARR < $3M floor), so it is HARD-REJECT, not NEAR-MISS. Near-misses are listings that clear the financial gate but fail niche-corpus matching.

Active-niche corpus paths used this run (re-resolved from WEEKLY REVIEW + DEALSX tabs):
- Premium Pest Management → DealsX keywords (Specialty Pest & Environmental Management Services)
- Private Art Advisory → WR row enrichment (Niche Hypothesis + Quick notes); DealsX reference blank
- Estate Management Companies → DealsX keywords
- Specialty Coffee Equipment Service → DealsX keywords (Specialty Commercial Equipment Services)
- High-End Commercial Cleaning → DealsX keywords
- Vertical SaaS for Luxury & High-Value Asset Service Industries → DealsX keywords
- Specialty Insurance Brokerage (Art & Collectibles) → DealsX keywords (Specialty Insurance Brokerage)
- Specialty Storage & Handling for High-Value Collections → DealsX keywords

## Listings Reviewed (full log)

| Source | Headline | Geo | Revenue | EBITDA | Margin | Industry | Verdict | Reject Reason |
|--------|----------|-----|---------|--------|--------|----------|---------|---------------|
| Everingham & Kerr (email, afternoon blast) | Cloud-Based SaaS Healthcare / Regulatory Compliance Software Company | Virtual / Remote | $700K (mostly recurring) | undisclosed | undisclosed | Vertical SaaS — healthcare regulatory compliance | HARD-REJECT | ARR $700K << $3M SaaS floor (disclosed-and-failed); not on active-niche corpus (Vertical SaaS thesis is luxury/HNW services, not healthcare) |

## Source Scorecard

| Source | Category | Status | HTTP | Listings Reviewed | Matches | Last Match Date |
|--------|----------|--------|------|-------------------|---------|-----------------|
| Everingham & Kerr (email) | General (email-only) | active | — | 1 | 0 | — |
| Rejigg (email) | General (email alerts) | active | — | 0 | 0 | — |
| Rejigg (web `/listings/`) | General (web) | blocked (single-attempt) | 404 | 0 | — | — |
| Flippa (email) | General (email + searchable) | active | — | 0 | 0 | — |

Notes:
- Rejigg `/listings/` returned 404 on direct fetch (default user-agent). Listings index has historically required authenticated session. Marked `blocked (single-attempt)` per `feedback_test_before_concluding_channel_dead` — second-attempt fallback (agent-browser w/ persisted profile) deferred to morning run; afternoon top-up does not re-verify dead channels (lightweight by design).
- Rejigg + Flippa email channels: zero new messages newer than 1d (most recent: Tory @ Flippa marketing email 2026-05-06 15:06, already captured in morning artifact's Empire Flippers / Flippa rows; no Rejigg email since prior business day).
- Everingham & Kerr afternoon blast captured one new listing (12:30 PM EDT, gmail msg `19e034732ed5648c`) — out-of-buy-box, logged.

## Volume Check

- Deals surfaced this afternoon: 0
- Combined daily total (morning + afternoon): 0
- 7-day rolling average: 0/day (last 7 daily totals all logged 0 deals_found)
- Target: 1-3/day — BELOW TARGET

Volume drivers (afternoon-specific): the time-sensitive email channels carried thin afternoon flow — one Everkerr blast, zero Rejigg/Flippa updates. The morning run's volume-driver analysis still applies (luxury/HNW thesis structurally underrepresented on cross-industry marketplaces; niche-specific channels are advisory/announcement, not active-listing). No new gap surfaced this afternoon beyond what morning already documented.
