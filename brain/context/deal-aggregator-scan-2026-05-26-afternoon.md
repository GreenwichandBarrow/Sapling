---
date: 2026-05-26
type: context
title: "Deal Aggregator Scan — 2026-05-26 (afternoon top-up; 0 PASS, 6 HARD-REJECT email-channel adds, 0 DealsX replies)"
deals_found: 0
sources_scanned: 4
sources_blocked_verified: 0
sources_blocked_single_attempt: 0
email_deals: 0
dealsx_replies: 0
buy_box_source: live
tags:
  - date/2026-05-26
  - context
  - topic/deal-aggregator
  - topic/afternoon-scan
  - status/done
---

# Deal Aggregator Scan — 2026-05-26 (Afternoon)

Afternoon top-up run. Three buy-box docs re-read live (Services 47 lines, Insurance 51 lines, SaaS 46 lines — identical to morning, no Kay edits during day). Active-niche corpus re-resolved from WEEKLY REVIEW + DEALSX tabs (8 active niches, same as morning). Email channel rescan picked up two post-morning sends — David Newell (Quiet Light) at 10:09 ET with one D2C ecommerce listing, Helen Guo (SMB Deal Hunter) at 13:49 ET with five hand-picked SMB listings. All six listings HARD-REJECT on the Services / SaaS buy-box gate (revenue floors, EBITDA floors, operating-history minimum, and industry hard-excludes). Rejigg still login-gated. Everingham & Kerr homepage reachable but no public listings page (email-only broker — no new blast email today). Flippa marketplace silent in afternoon window. Axial newsletter (Kaitlinn Thatcher 11:30 ET) is content/editorial about LOI structuring; no listing extraction. Zero Slack posts (no PASS-grade matches), zero fingerprint additions.

## Deals Surfaced (sent to Slack individually)

None today.

## Email Inbound Deals

None today as PASS-grade matches. Two post-morning broker emails landed and were processed:

- **Quiet Light listing alert** (David Newell, 10:09 ET) — single D2C ecommerce listing (Natural Health brand). HARD-REJECT on three independent criteria (consumer DTC hard-exclude + EBITDA below floor + operating history below 5yr minimum). Logged in Listings Reviewed.
- **SMB Deal Hunter newsletter** (Helen Guo, 13:49 ET) — 5 hand-picked SMB listings (Missouri sign manufacturer, California trucking compliance platform, Utah facility maintenance, North Carolina copper lumber wholesaler, Utah dairy equipment service). All five HARD-REJECT on disclosed-and-failed Services or SaaS criteria. Logged in Listings Reviewed.
- **Axial newsletter** (Kaitlinn Thatcher, 11:30 ET) — editorial content piece *"LOI terms for $45M turnkey electrical contractor"* plus Industrials valuation comps (HVAC 13x, defense 12x, metals <5x). Not a listing; no per-deal extraction. Electrical contractor reference would hit construction hard-exclude regardless.

No CIMs, no broker teasers, no NDA requests inbound this afternoon window. The Project Drone CIM that landed 2026-05-25 remains REJECT-conflict suppressed per `brain/inbox/2026-05-25-project-drone-cim-received-conflict-escalation`.

## DealsX Proprietary Outreach Replies

None today. No `Lead Interested` notifications from `Prospect Geni <dealsx.notifaction@gmail.com>` in the afternoon window.

## Near Misses (not Slacked)

None this run. The 6 new email-channel listings all fail at disclosed-and-failed buy-box criteria (revenue floor, EBITDA floor, operating history minimum, or industry hard-exclude), so they sort to HARD-REJECT rather than NEAR-MISS. The morning artifact already logged 6 NEAR-MISS listings from the broker-platform sweep (Business Exits / Synergy / Website Closers); the afternoon top-up adds none.

## Listings Reviewed (full log)

| Source | Headline | Geo | Revenue | EBITDA | Margin | Industry | Verdict | Reject Reason |
|--------|----------|-----|---------|--------|--------|----------|---------|---------------|
| SMB Deal Hunter (Helen Guo) | Absentee-Run Commercial Sign Manufacturer | MO | $4.36M | $661K | 15.1% | Manufacturing + Service (sign mfg) | HARD-REJECT | Revenue $4.36M below $10M Services floor (disclosed-and-failed) + capital-intensive manufacturing hard-exclude |
| SMB Deal Hunter (Helen Guo) | Trucking Licensing and Compliance Services Platform | CA (Remote) | $1.04M | $412K | 39.6% | SaaS-adjacent compliance services | HARD-REJECT | ARR $1.04M below $3M SaaS floor (disclosed-and-failed); not luxury vertical; CA soft-flag |
| SMB Deal Hunter (Helen Guo) | Facility Maintenance Contractor (National Grocery Chain) | UT | $4.51M | $838K | 18.6% | Service (facility maintenance) | HARD-REJECT | Revenue $4.51M below $10M Services floor + EBITDA $838K below $1.5M floor (both disclosed-and-failed) |
| SMB Deal Hunter (Helen Guo) | Specialty Copper-Infused Lumber Wholesaler | NC | $4.72M | $698K | 14.8% | Wholesale/Distribution (lumber) | HARD-REJECT | Revenue $4.72M below $10M Services floor + EBITDA $698K below $1.5M floor; no active-niche corpus match |
| SMB Deal Hunter (Helen Guo) | Dairy Equipment Sales, Service, and Installation | UT | $2.5M | $443K | 17.7% | Capital equipment service (dairy) | HARD-REJECT | Revenue $2.5M below $10M Services floor + EBITDA $443K below $1.5M floor + capital-intensive equipment adjacency |
| Quiet Light | Leading Natural Health Ecommerce Brand (30% Repeat-Purchase) | undisclosed (US supply chain) | $6.94M | $927K | 13.4% | Consumer DTC ecommerce | HARD-REJECT | Consumer retail / DTC hard-exclude + EBITDA $927K below $1.5M floor + operating history 4yr (launched 2022) below 5yr structural minimum (three independent disclosed-and-failed criteria) |

## Source Scorecard

| Source | Category | Status | HTTP | Listings Reviewed | Matches | Last Match Date |
|--------|----------|--------|------|-------------------|---------|-----------------|
| Quiet Light | General (email) | active | — | 1 | 0 | — |
| SMB Deal Hunter (Helen Guo) | General (email) | active | — | 5 | 0 | — |
| Rejigg | General | login-gated | 200 | 0 | — | — |
| Everingham & Kerr | General (email) | active | 200 | 0 | 0 | — |
| Flippa | General (email) | active | — | 0 | 0 | — |

**Notes:**
- Rejigg: site reachable (HTTP 200 on root); listings remain NDA/login-gated per morning run. No change in afternoon.
- Everingham & Kerr: homepage HTTP 200; `/listings/` `/for-sale/` `/businesses-for-sale/` `/active-listings/` all return 404 (confirmed email-only broker — no public listings page). No new EK blast email inbound today.
- Flippa: no new Flippa marketplace digest in afternoon window. Morning artifact already noted 2 digests from 5-24 / 5-25 carrying no broker-signal keywords.
- Email channel scope this run = scan Gmail for new inbound since the morning email-intelligence artifact (`email-scan-results-2026-05-26.md`, written 07:07 ET). Two new broker-signal threads (Quiet Light, SMB Deal Hunter) + one editorial content piece (Axial, not extracted).

## Volume Check

- Deals surfaced today (full day, morning + afternoon): 0 PASS
- Listings reviewed today (full day, morning + afternoon): 53 morning + 6 afternoon = 59 listings reviewed across all sources
- 7-day rolling average: 0.3 PASS / day (2 PASS matches surfaced across the prior 30 days per fingerprint store)
- Target: 1-3 / day — **BELOW TARGET**

Notes: zero PASS today is consistent with the post-Memorial-Day inbound thinness already documented in the morning artifact. Afternoon email-channel rescan added meaningful listing volume (6 listings reviewed) but every one of them fails on disclosed-and-failed criteria — none reaches the NEAR-MISS threshold (clears financial+structural gate but no niche match), they all fail the financial+structural gate first. BizBuySell install-gap (agent-browser missing on host) remains the load-bearing dark source from the morning sweep; surface to /evolve calibration. No new dark sources identified in afternoon.
