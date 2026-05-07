---
date: 2026-05-05
deals_found: 0
sources_scanned: 4
sources_blocked_verified: 0
sources_blocked_single_attempt: 0
email_deals: 1
buy_box_source: live
morning_artifact_present: true
notes: "Afternoon top-up. Lightweight rescan of email channel + time-sensitive platforms (Rejigg, Flippa, Everingham & Kerr). Channels 1 + 3 covered by morning run. Email-scan-results-2026-05-05.md present (8.9KB). 1 BLAST listing screened from email channel: B2B Trade Magazine Publisher (E&K) — HARD-REJECT on disclosed-and-failed Services revenue + EBITDA floors. Time-sensitive platforms returned 200 on homepages but actual listings remain auth/JS-gated (Rejigg matches via email-alert, Flippa is JS shell, Everkerr surfaces deals via newsletter blast only — already covered by email channel). No new public listings since 6am morning fire."
tags: [date/2026-05-05, deal-aggregator, scan-artifact, afternoon]
---
# Deal Aggregator Scan — 2026-05-05 (Afternoon Top-Up)

## Deals Surfaced (sent to Slack individually)

None today. 0 listings cleared the buy-box gate AND matched an active-niche corpus across the email channel + time-sensitive platforms scanned this afternoon. Morning artifact (`brain/context/deal-aggregator-scan-2026-05-05.md`) covers full Channels 1 + 3 — see it for today's near-miss roster.

## Email Inbound Deals

1. **B2B Trade Magazine Publisher** — Everingham & Kerr (`admin1@everkerr.com`, gmail msg `19df4c389bb2a227`) | Type: BLAST (single-listing) | Revenue $2.2M / EBITDA ~$1M / ~45% margin / industry: print + digital trade publishing for the meetings industry / NDA via download link in body (not PDF attachment). Screened against Services Buy Box: **HARD-REJECT** — disclosed-and-failed on revenue ($2.2M < $10M floor) AND EBITDA ($1M < $1.5M floor). Industry adjacency note: print/digital trade publishing sits in secular decline; not on the Services Hard-Excludes list explicitly but no thesis fit. No Slack post (HARD-REJECT verdict + disclosed-failure on hard floors).

## Near Misses (not Slacked)

- **B2B Trade Magazine Publisher (E&K)** — see Email Inbound Deals row above. Recategorized as HARD-REJECT not NEAR-MISS because disclosed financials fail TWO hard floors (revenue + EBITDA), not just one. Logged here for visibility on the only afternoon-channel inbound.

## Listings Reviewed (full log)

| Source | Headline | Geo | Revenue | EBITDA | Margin | Industry | Verdict | Reject Reason |
|--------|----------|-----|---------|--------|--------|----------|---------|---------------|
| Everingham & Kerr (email channel) | B2B Trade Magazine Publisher serving the meetings industry — print + digital, "leading industry source," award-winning editorial | undisclosed | $2.2M | ~$1M | ~45% | Trade publishing / media | HARD-REJECT | Revenue $2.2M < $10M Services floor (disclosed) AND EBITDA ~$1M < $1.5M floor (disclosed); print/media adjacency = no active-niche corpus match |

## Source Scorecard

| Source | Category | Status | HTTP | Listings Reviewed | Matches | Last Match Date |
|--------|----------|--------|------|-------------------|---------|-----------------|
| Everingham & Kerr (email channel) | General — Email-only broker | active | 200 | 1 | 0 | — |
| Rejigg | General — Marketplace + Email | active (homepage only; listings auth-gated) | 200 / 404 on /listings | 0 | 0 | — |
| Flippa | General — Marketplace (JS shell) | active (homepage only; listings JS-rendered) | 200 | 0 | 0 | — |
| Everingham & Kerr (web) | General — Email-only broker | active (homepage only; recent-transactions = intel-only tombstones) | 200 / 404 on /current-engagements | 0 | 0 | — |

Notes:
- Rejigg: `https://rejigg.com/` returns 200 with marketing + closed-deal tombstones, no live listing exposure without authenticated buyer profile. Live deal flow comes via Rejigg's email match-alerts (Channel 2). `/listings` returns 404 — confirmed not a public path.
- Flippa: `https://flippa.com/buy` returns 200 but body is a JS shell (no server-rendered listing data). Per SKILL.md, full Flippa scrape requires `agent-browser`; afternoon top-up skipped the heavy scrape (morning run covered it).
- Everingham & Kerr: `https://www.everkerr.com/` returns 200; `/current-engagements/` returns 404. Live engagements surface via email blast (covered by Channel 2 — see Email Inbound Deals row above).

## Volume Check
- Deals surfaced today (afternoon): 0
- Deals surfaced today (morning + afternoon combined): 0
- 7-day rolling average: tracking morning artifact's series; afternoon adds zero new.
- Target: 1-3/day — **BELOW TARGET** (0/3, second consecutive shortfall this week per morning artifact context). Recommend Friday digest review of source productivity per Phase 2.
