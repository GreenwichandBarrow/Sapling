---
date: 2026-05-13
run_mode: afternoon
deals_found: 0
sources_scanned: 4
sources_blocked_verified: 2
sources_blocked_single_attempt: 0
email_deals: 0
buy_box_source: live
morning_artifact_present: true
---
# Deal Aggregator Scan — 2026-05-13 (Afternoon)

Afternoon top-up run. Re-read all three buy-box docs live from Drive (Services / Insurance / SaaS). Re-loaded active niches from Industry Research Tracker WEEKLY REVIEW tab (8 active: Premium Pest Management, Private Art Advisory, Estate Management, Specialty Coffee Equipment Service, High-End Commercial Cleaning, Vertical SaaS for Luxury, Specialty Insurance Brokerage Art & Collectibles, Storage for High-Value Assets). Read `email-scan-results-2026-05-13.md` for inbound that landed after the 7am email-intelligence run. Rescanned time-sensitive channels only: Rejigg, Flippa, Everingham & Kerr afternoon blast. Full Channel 1 + 3 sweep skipped per afternoon mode.

## Deals Surfaced (sent to Slack individually)

None today.

## Email Inbound Deals

None today.

One Everingham & Kerr email landed at 11:01 ET (msg `19e21dbde972c7be`) but is a **buy-side search letter** — Joseph Vanore representing a family-office buyer seeking to acquire a NY/NJ/CT service/distribution company. This is competitor intermediary buy-side outreach, not a sell-side listing. Logged in Listings Reviewed as HARD-REJECT (not a deal).

## Near Misses (not Slacked)

- **Everingham & Kerr buy-side search letter (5/13 11:01 ET)** — buy-side search rep'd by Joseph Vanore for an unnamed family-office buyer. Not a sell-side listing. Worth noting as competitor intermediary intel; no Slack ping.

## Listings Reviewed (full log)

| Source | Headline | Geo | Revenue | EBITDA | Margin | Industry | Verdict | Reject Reason |
|--------|----------|-----|---------|--------|--------|----------|---------|---------------|
| Everingham & Kerr (email) | Buy-side search: Service and/or Distribution Company | NY/N+C NJ/CT | undisclosed | undisclosed | undisclosed | Service / Distribution (buy-side) | HARD-REJECT | Buy-side search letter, not a sell-side listing |

## Source Scorecard

| Source | Category | Status | HTTP | Listings Reviewed | Matches | Last Match Date |
|--------|----------|--------|------|-------------------|---------|-----------------|
| Rejigg | General | login-gated | 200 | 0 | 0 | — |
| Flippa | General | blocked (verified) | 404 | 0 | 0 | — |
| Everingham & Kerr (email) | Email-only broker | active | n/a | 1 | 0 | — |
| Email channel (email-scan-results) | Email inbound | active | n/a | 0 | 0 | — |

Notes:
- **Rejigg** — homepage returned 200 but listings live behind `/businesses` NDA gate; member-tier required for visibility. Logged login-gated, not blocked.
- **Flippa** — JS-shell route per SKILL.md fetcher routing. Requires `agent-browser`. `agent-browser` is NOT installed on this VPS host (verified `which agent-browser` → not found). Per SKILL.md stop-hook: `BROWSER_AUTOMATION_UNAVAILABLE: Flippa skipped, requires agent-browser install`. Status set to `blocked (verified)` because two attempts confirmed the source is dark to this run (WebFetch + missing-browser fallback).
- **Everingham & Kerr** — afternoon email arrived 11:01 ET. Parsed; classified as buy-side search letter (not sell-side listing). One row logged in Listings Reviewed.
- **Email channel** — no new CIMs / sell-side broker blasts since 7am email-intelligence run. The morning broker BLAST already captured (Quiet Light Amazon FBA Kitchen Brand) was filtered by morning run as outside buy-box (Amazon FBA marketplace-dependent, sub-$2M EBITDA threshold).

## Volume Check

- Deals surfaced today (afternoon top-up): 0
- Deals surfaced today (morning + afternoon combined): see morning artifact for morning count
- Target: 1–3/day — afternoon contributes 0 today; full daily volume tracked on morning artifact
