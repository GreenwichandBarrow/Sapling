---
date: 2026-05-29
deals_found: 0
sources_scanned: 4
sources_blocked_verified: 1
sources_blocked_single_attempt: 1
email_deals: 0
dealsx_replies: 0
buy_box_source: live
morning_artifact_missing: false
---
# Deal Aggregator Scan — 2026-05-29 (Afternoon Top-Up)

Afternoon `--afternoon` run (2pm ET). Lightweight top-up: re-read buy-boxes + active niches (live), re-read this morning's `email-scan-results-2026-05-29.md`, rescanned time-sensitive platforms only (Rejigg, Flippa, Everingham & Kerr). Full Channel 1 + 3 sweep and Channel 4 association boards skipped — morning run owned those. Morning artifact (`deal-aggregator-scan-2026-05-29.md`, 26.6KB) untouched.

Buy-boxes re-read live (Services / Insurance / SaaS) — no edits detected vs. morning. Active-niche list re-read from WEEKLY REVIEW — 8 active niches unchanged (Premium Pest, Private art advisory, Estate Management, Specialty Coffee Equipment Service, High-End Commercial Cleaning, Vertical SaaS for Luxury, Specialty Insurance Brokerage (Art), Storage for High-Value Assets).

**Result: 0 new evaluable deals this afternoon.** No new email-inbound deals after the 7am scan; both searchable time-sensitive platforms gated/JS-shell-blocked (agent-browser not installed). No new Slack posts; fingerprint store unchanged (2 entries, both DealsX leads from 5/18–5/19).

## Deals Surfaced (sent to Slack individually)
None today.

## Email Inbound Deals
None new. `email-scan-results-2026-05-29.md` is the single 7am email-intelligence artifact (no afternoon email-intelligence run), so no inbound deal email landed after the morning deal-aggregator run. Morning run already processed today's email channel: 5 DIRECT (none carrying a new deal), 2 BLASTs decomposed to 21 per-listing rows, 18 newsletters. No CIM, no NDA/CIM attachment, no DealsX `Lead Interested` reply, no new broker introduction this cycle. The 21 broker-blast listings are logged in full in the morning artifact's Listings Reviewed section.

## DealsX Proprietary Outreach Replies
None today. No `Prospect Geni <dealsx.notifaction@gmail.com>` / `Lead Interested` notification in the morning email-scan; no forwarded `@dealsx.io` owner reply.

## Near Misses (not Slacked)
- Everingham & Kerr — Southern NJ Residential Landscaping ($1M rev / ~$300K cash flow, Southern NJ): morning-covered. HARD-REJECT under Services Buy Box — disclosed revenue $1M below $10M floor, and residential landscaping is labor-heavy field service (industry hard-exclude). Not re-Slacked. Listed here for continuity, not as a new afternoon item.
- email-scan-results artifact present and read — no afternoon gap to note.

## Listings Reviewed (full log)

Zero new listings successfully scraped or parsed this afternoon: both searchable time-sensitive platforms were gated/blocked (Rejigg NDA/login-gated, Flippa JS-shell requiring uninstalled agent-browser), Everingham & Kerr is email-only with no public listings page, and the email channel surfaced no new listings after the 7am scan. The 21 email-blast listings parsed today were logged in full in the morning artifact (`deal-aggregator-scan-2026-05-29.md`); they are not re-logged here. Header emitted with no data rows per the zero-listings-reviewed rule.

| Source | Headline | Geo | Revenue | EBITDA | Margin | Industry | Verdict | Reject Reason |
|--------|----------|-----|---------|--------|--------|----------|---------|---------------|

## Source Scorecard

Rows = time-sensitive platforms actually scanned this afternoon run (not the full source list — that was the morning run's scope).

| Source | Category | Status | HTTP | Listings Reviewed | Matches | Last Match Date |
|--------|----------|--------|------|-------------------|---------|-----------------|
| Rejigg | General | blocked (verified) | 200 | 0 | 0 | — |
| Flippa | General | blocked (single-attempt) | 200 | 0 | 0 | — |
| Everingham & Kerr | General (email-only broker) | active | 200 | 0 | 0 | — |
| Email channel (email-scan-results) | Inbound | active | n/a | 0 | 0 | — |

Notes:
- **Rejigg** — `/businesses` returned a JS shell with no server-rendered listings; homepage confirms listings are NDA-gated ("Buyers first sign an NDA to view any anonymized businesses"). Two fetch attempts (listings path + homepage), both yielded no listing data. agent-browser fallback unavailable.
- **Flippa** — `BROWSER_AUTOMATION_UNAVAILABLE: Flippa skipped, requires agent-browser install.` SaaS search URL returned JS shell with `{{ listing.* }}` template placeholders, no server-rendered listings. Single WebFetch attempt; fallback (agent-browser) not installed, so marked single-attempt per stop-hook discipline.
- **Everingham & Kerr** — site exposes closed transactions only, no public for-sale listings; deal flow is email-only. Today's E&K blast (Southern NJ landscaping) landed in the 7am email-scan and was morning-processed; no new E&K email after the morning run.
- **Email channel** — re-read of the 7am `email-scan-results-2026-05-29.md`; no afternoon email-intelligence run, so no listings landed after morning.

## Volume Check
- Deals surfaced today (afternoon top-up): 0
- Deals surfaced today (morning + afternoon combined): 0
- Target: 1–3/day — BELOW TARGET
- Note: afternoon top-up is a thin rescan by design; both searchable time-sensitive platforms (Rejigg, Flippa) are gated/JS-shell-blocked without agent-browser. Installing `agent-browser` would unblock Flippa (and BizBuySell, Quiet Light) on future runs — gap surfaced, not silently dropped.
