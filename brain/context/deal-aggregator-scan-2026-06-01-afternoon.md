---
date: 2026-06-01
deals_found: 0
sources_scanned: 4
sources_blocked_verified: 0
sources_blocked_single_attempt: 2
email_deals: 0
dealsx_replies: 0
buy_box_source: live
morning_artifact_missing: false
niche_corpus_note: "8 active niches re-loaded. Private art advisory firms built from WR row (no DealsX equivalent); all others used DealsX keyword corpus. No niche status changes detected since morning run."
---
# Deal Aggregator Scan — 2026-06-01 (Afternoon Top-Up)

## Deals Surfaced (sent to Slack individually)

None today.

## Email Inbound Deals

None. email-scan-results-2026-06-01.md (morning artifact) confirms: 0 broker BLASTs, 0 deal newsletters, 0 CIM/NDA/teaser emails in the 2-day Gmail window. No Everingham & Kerr, Viking Mergers, DealForce, Rejigg, SMB Deal Hunter, or other deal-source emails detected. No new deal emails landed in the afternoon window (email-scan artifact re-read; no updates since morning).

## DealsX Proprietary Outreach Replies

Inbound owner replies to DealsX cold outreach (Channel 6). Contact handoffs — no financials. Surfaced to Slack, count toward daily volume, do NOT trigger target-discovery.

None today. No Prospect Geni notifications in email-scan-results-2026-06-01.md.

## Near Misses (not Slacked)

None. All afternoon sources were blocked or returned zero accessible listings — no listings reached the buy-box screening stage.

## Listings Reviewed (full log)

| Source | Headline | Geo | Revenue | EBITDA | Margin | Industry | Verdict | Reject Reason |
|--------|----------|-----|---------|--------|--------|----------|---------|---------------|

*(Zero listings parsed this run — all afternoon sources blocked or email-only with empty window. Table header retained per spec.)*

## Source Scorecard

| Source | Category | Status | HTTP | Listings Reviewed | Matches | Last Match Date |
|--------|----------|--------|------|-------------------|---------|-----------------|
| Rejigg | General | login-gated | 200 | 0 | — | — |
| Flippa | General | blocked (single-attempt) | JS-shell | 0 | — | — |
| Everingham & Kerr | Email-only broker | active (email-only) | N/A | 0 | — | — |
| Email channel | Channel 2 | active | N/A | 0 | 0 | — |

**Rejigg:** Homepage and /businesses page fetch succeeded (HTTP 200), but all individual listings are behind NDA/account creation gate — no listing content extractable without buyer account. Status: login-gated.

**Flippa:** JS-rendered marketplace; all search paths return JS shell or 404. `agent-browser` is NOT installed (`which agent-browser` → NOT_INSTALLED). BROWSER_AUTOMATION_UNAVAILABLE: Flippa skipped, requires agent-browser install. Status: blocked (single-attempt) — only one fetch attempt possible without browser automation.

**Everingham & Kerr:** Email-only broker. No public listing page (E&K website shows completed transactions only, no live listings). Deal flow arrives via email blast. No E&K emails in today's 2-day Gmail window per email-scan-results-2026-06-01.md.

**Email channel:** email-scan-results-2026-06-01.md re-read. No new deal-related emails since morning run. 8 total emails in window; 0 classified as BLAST, DEAL_NEWSLETTER, or CIM-bearing.

## Volume Check

- Deals surfaced today (morning + afternoon combined): 0
- 7-day rolling average (May 26 – Jun 1, weekdays only): 0.0/day
- Target: 1-3/day — **BELOW TARGET**

*Note: Persistent 0-deal run streak (5 consecutive weekdays). Primary access blockers: Rejigg login-gated, Flippa requires agent-browser (not installed). Everingham & Kerr email cadence has been silent. Consider: (1) install agent-browser for Flippa automation, (2) register buyer account on Rejigg, (3) verify E&K email list subscription is active. Morning artifact (2026-06-01) scanned 17 sources; afternoon top-up adds 4 time-sensitive checks — all blocked or empty today.*
