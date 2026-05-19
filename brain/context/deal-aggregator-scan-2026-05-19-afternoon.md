---
date: 2026-05-19
deals_found: 0
sources_scanned: 4
sources_blocked_verified: 0
sources_blocked_single_attempt: 3
email_deals: 0
dealsx_replies: 0
morning_artifact_missing: false
buy_box_source: live
---
# Deal Aggregator Scan — 2026-05-19 (Afternoon Top-Up)

Afternoon (`--afternoon`) lightweight top-up. Buy-boxes re-read live from Drive this run (Services 1453B / Insurance 1782B / SaaS 1463B — unchanged vs morning). Active niches re-read from WEEKLY REVIEW: rows 1–8 Active (Premium Pest, Private Art Advisory, Estate Management, Specialty Coffee Equipment Service, High-End Commercial Cleaning, Vertical SaaS Luxury, Specialty Insurance Brokerage Art & Collectibles, Storage & Handling High-Value) — no Kay toggles since the 7:30am run; rows 9–15 still New–Pending Review. Scope per SKILL.md afternoon path: email channel + time-sensitive platforms (Rejigg / Flippa / Everingham & Kerr) only. Full Channel 1 + 3 + 4 sweep skipped (morning run covered those). agent-browser still NOT installed — JS-shell/Cloudflare fallback unavailable; affected web frontends logged single-attempt.

## Deals Surfaced (sent to Slack individually)
None today. No new (non-fingerprinted) matches surfaced in the afternoon top-up. 0 listings cleared the buy-box gate this run (0 listings parsed — all time-sensitive web sources returned no server-rendered listings).

## Email Inbound Deals
None today. `email-scan-results-2026-05-19.md` is the single 7am ET email-intelligence artifact (one run/day — no afternoon re-fire). Section 7: zero broker BLAST listings extracted this window (only inbound was Helen Guo / SMB Deal Hunter product-launch announcement — no broker-signal keywords, no embedded listings). No CIM / NDA / teaser / blind-profile email landed after the morning run.

## DealsX Proprietary Outreach Replies
None new. Emilio Mitidieri (emiliomiti.com) was already surfaced, Slack-posted to #active-deals, and fingerprinted (`149e3b2c…`) in the 2026-05-19 morning run; Greg Bruyere fingerprinted 2026-05-18. Both present in `deal-aggregator-fingerprints.jsonl` → dedup DUP → Slack skipped (idempotent, no double-post). No new DealsX "Lead Interested" notification after the morning run.

## Near Misses (not Slacked)
- None this run. No listings were parsed in the afternoon top-up (all time-sensitive web sources dark; email channel produced zero broker listings). Morning run's near-miss set stands in `deal-aggregator-scan-2026-05-19.md`.

## Listings Reviewed (full log)

Zero listings were scraped or parsed this run — every time-sensitive web source returned no server-rendered listings and the email channel produced no broker-blast listings. Header emitted with no data rows per the Results File spec.

| Source | Headline | Geo | Revenue | EBITDA | Margin | Industry | Verdict | Reject Reason |
|--------|----------|-----|---------|--------|--------|----------|---------|---------------|

## Source Scorecard

One row per time-sensitive source actually scanned this afternoon run (not the full source universe — that was the morning run's scorecard).

| Source | Category | Status | HTTP | Listings Reviewed | Matches | Last Match Date |
|--------|----------|--------|------|-------------------|---------|-----------------|
| Rejigg | General (time-sensitive) | blocked (single-attempt) | 200 (JS shell) | 0 | 0 | — |
| Flippa | General (time-sensitive) | blocked (single-attempt) | 200 (JS shell) | 0 | 0 | — |
| Everingham & Kerr | General (time-sensitive) | active (no public listings) | 200 | 0 | 0 | — |
| Email channel (email-scan-results) | Email Inbound | active | — | 0 | 0 | — |

**Notes:**
- `Rejigg` — `rejigg.com/businesses` returned a JS shell with no server-rendered listings. Primary path is email-routed deal-match emails (covered by email-intelligence — zero this window). agent-browser fallback NOT installed (`BROWSER_AUTOMATION_UNAVAILABLE: Rejigg web scrape skipped, requires agent-browser install`). Marked single-attempt (fallback could not be attempted).
- `Flippa` — `flippa.com/search` returned "No matches found" / JS template; digital-online-only inventory anyway. agent-browser fallback NOT installed. Marked single-attempt. Primary path email-routed (zero this window).
- `Everingham & Kerr` — `/listings/` and `/businesses-for-sale/` both 404; homepage shows completed transactions only, no current-deal portal (email-only broker per SKILL.md). No afternoon email blast in this window. Active, no public listings to parse.
- Email channel — `email-scan-results-2026-05-19.md` is the 7am artifact; email-intelligence does not re-run in the afternoon. Re-read this run: no new broker blasts, CIMs, teasers, or DealsX replies after the morning scan.
- `Matches`/`Last Match Date` from `deal-aggregator-fingerprints.jsonl` — only DealsX-channel entries present (Greg 5/18, Emilio 5/19); no scanned-source matches in the 30-day window.

## Volume Check
- Deals surfaced today (afternoon top-up): 0 new. Day total stands at 1 (Emilio Mitidieri DealsX reply, counted + Slacked in the morning run — not double-counted here).
- 7-day rolling average: ~1/day (fingerprint history: Greg 2026-05-18, Emilio 2026-05-19; limited prior-artifact history for full 7-day window).
- Target: 1–3/day — **ON TRACK** (low end; afternoon top-up added no incremental volume — time-sensitive web sources dark and email channel quiet post-morning. Watch: if scanning channels stay at 0 PASS for 7+ consecutive days, expand source coverage / install agent-browser to unblock Rejigg + Flippa web scrapes / revisit corpus tuning for the 7 active niches at 0 matches.)
