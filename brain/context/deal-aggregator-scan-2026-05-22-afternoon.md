---
schema_version: 1.1.0
date: 2026-05-22
type: output
output_type: deal-aggregator-scan
status: draft
deals_found: 0
sources_scanned: 4
sources_blocked_verified: 0
sources_blocked_single_attempt: 1
email_deals: 0
dealsx_replies: 0
buy_box_source: live
morning_artifact_missing: false
tags:
  - date/2026-05-22
  - output
  - output/deal-aggregator-scan
  - source/deal-aggregator
  - topic/deal-aggregator
  - topic/morning-briefing
---

# Deal Aggregator Scan — 2026-05-22 (Afternoon Top-Up)

Afternoon headless run (Friday 2pm ET). Lightweight top-up per `--afternoon` mode: re-read buy-boxes + active niches live, rescan time-sensitive platforms only (Rejigg / Flippa / Everingham & Kerr) + email channel. Full Channel 1 + 3 sweep handled by morning run (`deal-aggregator-scan-2026-05-22.md`, 07:38 ET, 0 deals, 54 listings reviewed).

All three buy-box docs (Services / Insurance / SaaS) re-read live from Drive — unchanged from morning run. Active-niche corpus reloaded from Industry Research Tracker WEEKLY REVIEW + DEALSX tabs — 8 Active niches (Premium Pest, Private Art Advisory, Estate Mgmt, Coffee Equipment, High-End Cleaning, Vertical SaaS Luxury, Specialty Insurance Art, Storage for HVA) plus 1 Active-Long Term (Specialty Insurance Art at rank 7). No mid-day edits detected.

Email channel inert this run: `brain/context/email-scan-results-2026-05-22.md` last written 07:04 ET (morning email-intelligence run); email-intelligence has no scheduled midday rerun, so no new email-inbound signals are observable in the artifact since morning. Zero broker BLASTs, zero CIMs, zero DealsX reply notifications captured in today's window (2026-05-20 → 2026-05-22). The DealsX fingerprint store remains at 2 entries (2026-05-18 St. Louis, 2026-05-19 Emilio Miti) — both pre-morning.

agent-browser CLI remains unavailable on this VPS (`command not found`). Flippa's `/search` returned HTTP 200 but as an Angular JS-shell with no server-rendered listings — surfaced as `blocked (single-attempt)` per `feedback_test_before_concluding_channel_dead` (NOT promoted to `blocked (verified)` until a second-tool attempt confirms dark state).

## Deals Surfaced (sent to Slack individually)

None today.

## Email Inbound Deals

None today. `email-scan-results-2026-05-22.md` (last write 07:04 ET) reports zero broker BLAST listings, zero CIMs, zero NDA-attached emails, zero broker teasers in the 2-day window. No midday email-intelligence run to refresh; next email-scan landing is 2026-05-23 ~07:00 ET.

## DealsX Proprietary Outreach Replies

None today. Zero emails from `Prospect Geni <dealsx.notifaction@gmail.com>` or `@dealsx.io` forwards observable in the current email-scan-results window. Last DealsX reply: 2026-05-19 (Emilio Miti, per fingerprint store).

## Near Misses (not Slacked)

- **Email channel afternoon-blank.** Rejigg / Everingham & Kerr / Viking / DealForce / SMB Deal Hunter all flow through Gmail; with no email-intelligence midday run, today's afternoon email-blast window (10am–2pm ET) is effectively invisible to this skill until tomorrow's 07:00 ET email-scan refresh. Logging the gap rather than treating zero-signal as zero-flow.

## Listings Reviewed (full log)

Zero listings scraped or parsed in this afternoon run. Flippa returned a JS-only shell (no server-rendered listings extractable without agent-browser). Email-only sources (Rejigg, E&K) carry no afternoon inbound observable via the morning email-scan artifact. Table header emitted with no data rows per the prompt's "header only when zero listings reviewed" rule.

| Source | Headline | Geo | Revenue | EBITDA | Margin | Industry | Verdict | Reject Reason |
|--------|----------|-----|---------|--------|--------|----------|---------|---------------|

## Source Scorecard

Time-sensitive platforms actually scanned this afternoon run only — per `--afternoon` prompt, the full active-source roster was covered by the morning run scorecard. Four rows below: the three time-sensitive platforms named in SKILL.md "Afternoon Run" + the email channel as a single rolled-up row.

| Source | Category | Status | HTTP | Listings Reviewed | Matches | Last Match Date |
|--------|----------|--------|------|-------------------|---------|-----------------|
| Rejigg | General (email-only) | active (email-only) | n/a | 0 | 0 | — |
| Flippa | General | blocked (single-attempt) | 200 (JS shell, no listings) | 0 | 0 | — |
| Everingham & Kerr | General (email-only) | active (email-only) | n/a | 0 | 0 | — |
| Email channel (CIMs / broker blasts / DealsX replies) | All | active (artifact-driven) | n/a | 0 | 0 | — |

**Status legend:**
- `active (email-only)` — surface via `email-scan-results-{date}.md`; no new inbound observable in this run's window.
- `active (artifact-driven)` — email-scan-results-2026-05-22.md read; zero deal-flow signals.
- `blocked (single-attempt)` — primary curl returned 200 but with a JS-shell payload, no listings parseable. agent-browser unavailable as fallback. NOT promoted to `blocked (verified)` per `feedback_test_before_concluding_channel_dead`.

**Fingerprint store status:** `brain/context/deal-aggregator-fingerprints.jsonl` unchanged this run — 2 entries (both DealsX leads from earlier this week). No new matches to append, no Slack posts to dedup against.

## Volume Check

- Deals surfaced today (combined morning + afternoon): 0
- 7-day rolling weekday average (5/15 / 5/18 / 5/19 / 5/20 / 5/21 / 5/22): (0 + 1 + 0 + 0 + 0 + 0) / 6 = **0.17/day**
- Target: 1–3/day
- Status: **🔴 BELOW TARGET** (sustained — six consecutive weekday zero-result days since 5/19 morning)

The sustained-zero pattern is the same Phase-2-stewardship signal flagged in the morning artifact: scrapable General sources lean toward construction / healthcare / consumer-retail / digital-eCommerce — all hard-excluded by buy-box design. Active-niche corpus matches require either niche-specific advisory output (Sica Fletcher / GP Bullhound / PCO Bookkeepers — silent, JS-rendered, or scraper-blocked today) or email-driven channels which produced nothing in the 2-day window. Friday Source Scout (6 AM digest run, already landed earlier this morning if today's wrapper fired) is the right surface for proposed source additions to widen niche-aligned coverage.

## BROWSER_AUTOMATION_UNAVAILABLE Footnote

agent-browser CLI still not installed on this VPS (`command not found`). Flippa scraping continues to fall back to single-attempt curl, which lands a JS-shell payload without listings. To recover Flippa (and morning-run BizBuySell / Quiet Light) scrapability: `npm i -g agent-browser && agent-browser install`. Surfaced for Friday morning briefing visibility.
