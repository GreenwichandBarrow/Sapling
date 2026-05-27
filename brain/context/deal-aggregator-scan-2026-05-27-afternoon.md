---
date: 2026-05-27
run: afternoon
deals_found: 0
sources_scanned: 4
sources_blocked_verified: 1
sources_blocked_single_attempt: 1
email_deals: 0
dealsx_replies: 0
morning_artifact_present: true
---
# Deal Aggregator Scan — 2026-05-27 (Afternoon Top-Up)

Afternoon (`--afternoon`) headless run. Lightweight top-up over the morning artifact (`deal-aggregator-scan-2026-05-27.md`). Per SKILL.md, scope = email channel + time-sensitive platforms only (Rejigg, Flippa, Everingham & Kerr). Channel 1 full broker-platform sweep + Channel 3 industry-specific scan + Channel 4 association deal boards = morning's job, skipped here.

Buy-boxes re-pulled fresh from Drive (Services 47 lines / Insurance 51 lines / SaaS 46 lines). Active niches re-pulled from Industry Research Tracker WEEKLY REVIEW. No changes since 7am.

**Result: zero new listings since morning → zero new Slack posts to `#active-deals`.** Email-scan midday refresh (1:19pm ET) confirmed no new BLAST or DEAL_NEWSLETTER deal-listing emails since 7am (Section 7 row count unchanged at 9, all already screened in morning artifact). No DealsX Proprietary Outreach replies. Time-sensitive broker platforms returned no scrapable listings this run.

## Deals Surfaced (sent to Slack individually)

None today (afternoon). Morning run also surfaced zero PASS listings.

## Email Inbound Deals

None new since morning. Email-scan-results-2026-05-27 midday refresh at 1:19pm ET explicitly confirmed "No new BLAST or DEAL_NEWSLETTER deal-listing emails since 7am — Section 7 row count unchanged at 9 listings." The 9 listings (5 Helen Guo SMB Deal Hunter + 4 Flippa Daily) were screened and HARD-REJECTED in the morning artifact. No CIMs, NDA confirmations, broker BLASTs, intro forwards, or other deal-specific emails landed in the afternoon window.

## DealsX Proprietary Outreach Replies

None today. No `dealsx.notifaction@gmail.com` "Lead Interested" notifications in today's email-scan-results (morning or midday refresh).

## Near Misses (not Slacked)

None new this run. Morning artifact carries the two day-level entries (LED Display Solutions Company / Loss Prevention Training Platform); not duplicated here.

## Listings Reviewed (full log)

Zero new listings scraped or parsed this run. Rejigg `/listings` returned 404 (two-attempt verified blocked). Rejigg homepage marketing-only, no live listings. Flippa returned JS shell with no server-rendered listings (agent-browser not installed → cannot render). Everingham & Kerr homepage shows historical closed transactions only (email-only intermediary, no public listings — email channel covered via email-scan-results, no new blasts since 7am). Email channel produced no new deal-flow emails after the morning sweep.

| Source | Headline | Geo | Revenue | EBITDA | Margin | Industry | Verdict | Reject Reason |
|--------|----------|-----|---------|--------|--------|----------|---------|---------------|

## Source Scorecard

| Source | Category | Status | HTTP | Listings Reviewed | Matches | Last Match Date |
|--------|----------|--------|------|-------------------|---------|-----------------|
| Rejigg | General (Time-Sensitive) | blocked (verified) | 404 / 200 | 0 | 0 | — |
| Flippa | General (Time-Sensitive) | blocked (single-attempt) | JS-shell | 0 | 0 | — |
| Everingham & Kerr | General (Email-Only Broker) | active | 200 | 0 | 0 | — |
| email-scan-results (Channel 2) | Email Inbound | active | n/a | 0 | 0 | — |

**Status notes:**
- **Rejigg** — `/listings` path returned HTTP 404 (canonical listings URL moved or auth-gated). Homepage fetch returned 200 but shows only marketing content + "Recent Closings" (completed deals, not active marketplace). Two attempts = `blocked (verified)`.
- **Flippa** — JS shell with template syntax (`{{ listing.basic_info.name }}`), server-rendered HTML contains no listings. Per SKILL.md routing, this source requires agent-browser; `agent-browser` not installed on this VPS. Marked `blocked (single-attempt)` per the SKILL.md guidance: "if agent-browser is not installed, log BROWSER_AUTOMATION_UNAVAILABLE." Surfacing here so the gap is visible.
- **Everingham & Kerr** — homepage 200, but per SKILL.md classification this is an email-only broker with no searchable platform. Email-scan-results midday refresh confirmed no new Everingham & Kerr blasts since 7am. Source "active" = covered correctly via email channel.
- **email-scan-results (Channel 2)** — email-intelligence midday refresh (1:19pm ET) ran cleanly; 0 new deal-flow emails (BLAST / DEAL_NEWSLETTER / CIM / NDA / intro forward) after the 7am baseline.

## Volume Check

- Deals surfaced today (morning + afternoon combined): **0**
- Afternoon-only delta: 0
- 7-day rolling average: tracking morning artifact's view (0/day current week)
- Target: 1-3/day — **BELOW TARGET**

Volume continues to track BELOW the 1-3/day target. The Friday digest (next: 2026-05-29) is the canonical surface for source-productivity retirement / addition proposals. Two observations from this afternoon's blocks that the Friday digest should weigh: (1) Rejigg `/listings` 404 is new behavior — needs verify-still-alive check before retirement; (2) Flippa as a deal source is permanently dark without `agent-browser` install — either install agent-browser on the VPS or formally remove Flippa from the platform list. Surfacing here for visibility, not actioning in headless mode.
