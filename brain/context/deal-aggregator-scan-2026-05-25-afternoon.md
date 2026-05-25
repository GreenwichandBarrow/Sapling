---
schema_version: 1.1.0
date: 2026-05-25
type: context
title: "Deal Aggregator Scan — 2026-05-25 (Memorial Day Monday, afternoon top-up)"
deals_found: 0
sources_scanned: 4
sources_blocked_verified: 3
sources_blocked_single_attempt: 0
email_deals: 0
dealsx_replies: 0
buy_box_source: live
morning_artifact_missing: false
tags:
  - date/2026-05-25
  - context
  - topic/deal-aggregator
  - topic/afternoon-scan
  - status/done
---

# Deal Aggregator Scan — 2026-05-25 (Afternoon)

Afternoon top-up scan. US Memorial Day holiday — no broker afternoon blasts landed and no new platform listings cleared corpus thresholds. Morning artifact ([[brain/context/deal-aggregator-scan-2026-05-25]]) covered Channel 1 + 3 + 4 in full; this run rescans only the email channel + time-sensitive platforms (Rejigg, Flippa, Everingham & Kerr) per the `--afternoon` spec.

**Buy-box source:** live re-read of Services / Insurance / SaaS docs from Drive — no Kay edits since morning run.

**Active niches re-read:** Industry Research Tracker WEEKLY REVIEW tab returned 8 Active rows (rows 1-8), same set as morning. No status toggles since 07:38 ET morning artifact write.

**Niche corpus path log (unchanged from morning):**
- Premium Pest Management → DealsX keywords ("Specialty Pest & Environmental Management Services")
- Private art advisory firms → WR row enrichment (Niche Hypothesis + Quick notes — DealsX Niche field blank)
- Estate Management Companies → DealsX keywords ("Estate Management Companies")
- Specialty Coffee Equipment Service → DealsX keywords ("Specialty Commercial Equipment Services")
- High-End Commercial Cleaning → DealsX keywords ("High-End Commercial Cleaning")
- Vertical SaaS for Luxury & High-Value Asset Service Industries → DealsX keywords
- Specialty Insurance Brokerage (Art & Collectibles) → DealsX keywords ("Specialty Insurance Brokerage")
- Storage & Related Services for High-Value Assets → DealsX keywords ("Specialty Storage & Handling for High-Value Collections")

## Deals Surfaced (sent to Slack individually)

None today. Zero new listings since morning run; fingerprint store unchanged.

## Email Inbound Deals

None. [[brain/context/email-scan-results-2026-05-25]] flagged 0 CIMs, 0 broker BLAST per-deal listings, 0 introductions. Afternoon Gmail recheck (post-07:38 morning artifact) returned zero new threads from Rejigg, Flippa, Everingham & Kerr, DealsX notification alias, or any `Lead Interested` / `new listing` keyword senders.

## DealsX Proprietary Outreach Replies

None. No `Lead Interested` notifications from `dealsx.notifaction@gmail.com` since morning run. Most recent Channel-6 fingerprint is from 2026-05-19 (emiliomiti.com) — 6 days dark.

## Near Misses (not Slacked)

None this run. Time-sensitive platforms all blocked (see Source Scorecard); email channel produced zero borderline listings.

## Listings Reviewed (full log)

Zero listings reviewed this run — all three time-sensitive platforms blocked at fetch time and email channel returned no per-listing extractions. Table header emitted per spec.

| Source | Headline | Geo | Revenue | EBITDA | Margin | Industry | Verdict | Reject Reason |
|--------|----------|-----|---------|--------|--------|----------|---------|---------------|

## Source Scorecard

Rows = the four time-sensitive sources scanned in this afternoon run (not the full Sourcing-Sheet sweep — that was morning's job).

| Source | Category | Status | HTTP | Listings Reviewed | Matches | Last Match Date |
|--------|----------|--------|------|-------------------|---------|-----------------|
| Rejigg | General | blocked (verified) | 404 (`/listings`) → 200 empty (`/`) → 200 gated (`/businesses`) | 0 | 0 | — |
| Flippa | General (AI marketplace) | blocked (verified) | 200 (JS shell, no server-rendered listings); agent-browser not installed (BROWSER_AUTOMATION_UNAVAILABLE) | 0 | 0 | — |
| Everingham & Kerr | General (email-only broker) | blocked (verified) | 404 (`/listings`) + 200 (`/` = transaction archive only); 0 afternoon Gmail blasts | 0 | 0 | — |
| Email Channel (Channel 2 + 6) | Email | active | 200 (Gmail) | 0 | 0 | — |

**Notes:**
- Rejigg `/businesses` requires login; Kay has no buyer account yet. Surface to Kay for one-time registration if afternoon scans should produce listings from this source. Until registered, this source is structurally dark in afternoon mode.
- Flippa is on the known JS-shell / agent-browser-required list (SKILL.md scraper routing). `agent-browser` CLI is not installed on this VPS (`command not found`). Per Stop Hook: surface the gap rather than silently drop the source. Morning run also blocked here.
- Everingham & Kerr is email-only by design; no afternoon blast email today (no Gmail thread from `everkerr.com` after 07:38).

## Volume Check

- Deals surfaced today (morning + afternoon combined): 0
- 7-day rolling average: ~0.1/day (1 surfaced match in trailing 7 days — both fingerprints in store are >5 days old)
- Target: 1-3/day — **BELOW TARGET**

Memorial Day holiday explains today's zero; the rolling-average gap is the persistent signal — most-active broker channels are blocked-or-empty and Channel 6 (DealsX replies) is the main inbound recently. Calibration belongs in the Friday digest, not in this artifact.
