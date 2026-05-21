---
schema_version: 1.1.0
date: 2026-05-21
type: context
title: Deal Aggregator Scan — 2026-05-21 (Afternoon Top-Up)
deals_found: 0
sources_scanned: 4
sources_blocked_verified: 0
sources_blocked_single_attempt: 1
email_deals: 0
dealsx_replies: 0
buy_box_source: live
morning_artifact_missing: false
tags:
  - date/2026-05-21
  - context
  - source/deal-aggregator
  - status/published
---

# Deal Aggregator Scan — 2026-05-21 (Afternoon)

Headless afternoon top-up run (Thu, 2pm ET). Buy-boxes re-read live from Drive (Services / Insurance / SaaS — unchanged from morning). Active niches re-read from Industry Research Tracker `WEEKLY REVIEW` (8 active rows — unchanged from morning). Morning artifact present at `brain/context/deal-aggregator-scan-2026-05-21.md` (0 deals surfaced). Email-scan-results artifact present at `brain/context/email-scan-results-2026-05-21.md` (7am run — no deal-classified inbound). Per SKILL.md afternoon scope: re-read buy-boxes + niches, rescan email channel + time-sensitive platforms (Rejigg / Flippa / Everingham & Kerr), skip full Channel 1 + 3 sweep, skip Channel 4 (associations).

## Deals Surfaced (sent to Slack individually)

None this run. 0 listings cleared the buy-box + niche-corpus gate across the 4 time-sensitive sources scanned.

## Email Inbound Deals

One new broker single-listing blast landed after the 7am email-intelligence run (Quiet Light, 10:09 ET — Amazon FBA Home Decor Brand). Fails Services buy-box on disclosed financials ($94K SDE far below the $1.5M EBITDA floor and $10M revenue floor) and hits the consumer-retail / DTC industry hard-exclude. Logged in Listings Reviewed below. No Slack post. No CIMs, no new multi-listing broker blasts, no Everingham & Kerr emails today.

## DealsX Proprietary Outreach Replies

None this run. No `Prospect Geni <dealsx.notifaction@gmail.com>` notifications in the inbound window since the morning run.

## Near Misses (not Slacked)

None this run. Every listing reviewed in the afternoon top-up was a HARD-REJECT (sub-buybox financials AND/OR consumer-retail/DTC/lending hard-exclude). No listing cleared buy-box financial gates while sitting outside the active-niche corpus.

## Listings Reviewed (full log)

| Source | Headline | Geo | Revenue | EBITDA | Margin | Industry | Verdict | Reject Reason |
|--------|----------|-----|---------|--------|--------|----------|---------|---------------|
| Quiet Light (email) | 10-Year-Old Amazon FBA Home Decor Brand | undisclosed | undisclosed | $94K SDE | undisclosed | Amazon FBA / DTC home decor | HARD-REJECT | SDE far below Services $1.5M EBITDA floor; consumer-retail/DTC hard-exclude |
| Flippa (marketplace) | Premium Fashion / 47% Europe / $3.7M Pro Forma Rev | undisclosed | $3.7M (pro forma) | undisclosed | undisclosed | Fashion / DTC | HARD-REJECT | Rev below $10M Services floor; consumer-retail/DTC hard-exclude |
| Flippa (marketplace) | Education + Software Reviews Content Site Portfolio | undisclosed | undisclosed | undisclosed | undisclosed | Digital media / content site | HARD-REJECT | Asking $331K — sub-buybox; ad-revenue content sites wrong shape |
| Flippa (marketplace) | SEO Shopify Baby Float Niche Site (7yr) | undisclosed | undisclosed | undisclosed | undisclosed | Shopify / DTC baby | HARD-REJECT | Asking $98K — sub-buybox; consumer-retail/DTC hard-exclude |
| Flippa (marketplace) | Amazon FBA Baby Brand (€2.62M TTM) | undisclosed | €2.62M | undisclosed | undisclosed | Amazon FBA / DTC baby | HARD-REJECT | Rev below $10M floor; consumer-retail/DTC hard-exclude |
| Flippa (marketplace) | Mauritius-Licensed Regulated Trading Platform (~15% mgn) | Mauritius | undisclosed | undisclosed | ~15% | Regulated trading / fintech | HARD-REJECT | Non-US (offshore); lending/balance-sheet financial product hard-exclude |
| Flippa (marketplace) | AI Tools Platform + Newsletter (10K+ tools) | undisclosed | undisclosed | undisclosed | undisclosed | AI tools directory / newsletter | HARD-REJECT | Asking $195K — sub-buybox; ad/affiliate revenue model |
| Flippa (marketplace) | Amazon KDP Business ($13K rev) | undisclosed | $13K | undisclosed | undisclosed | Amazon KDP | HARD-REJECT | Sub-buybox; consumer-retail/DTC hard-exclude |
| Flippa (marketplace) | Strollers + Children's Furniture Online Shop | undisclosed | undisclosed | undisclosed | undisclosed | Ecom / DTC kids | HARD-REJECT | Asking $116K — sub-buybox; consumer-retail/DTC hard-exclude |
| Flippa (marketplace) | Dog Breeder ↔ Buyer Marketplace | undisclosed | undisclosed | undisclosed | undisclosed | Two-sided marketplace / consumer | HARD-REJECT | Asking $118K — sub-buybox; consumer-marketplace wrong shape |
| Flippa (marketplace) | Elite 2014 FBA/WFS Health & Beauty Brand | undisclosed | undisclosed | undisclosed | undisclosed | Amazon FBA / DTC health & beauty | HARD-REJECT | Asking $335K — sub-buybox; consumer-retail/DTC hard-exclude |
| Flippa (marketplace) | SleepBamboo (20-yr legacy ecom) | undisclosed | undisclosed | undisclosed | undisclosed | Ecom / DTC bedding | HARD-REJECT | Asking $57K — sub-buybox; consumer-retail/DTC hard-exclude |
| Flippa (marketplace) | 2013 Ecom Electronics Brand ($67K rev / 30% mgn) | undisclosed | $67K | undisclosed | ~30% | Ecom electronics / DTC | HARD-REJECT | Sub-buybox; consumer-retail/DTC hard-exclude |
| Flippa (marketplace) | Branded Site | undisclosed | undisclosed | undisclosed | undisclosed | Digital / branded site | HARD-REJECT | Asking $17K — sub-buybox |
| Flippa (marketplace) | Practical Amazon Business | undisclosed | undisclosed | undisclosed | undisclosed | Amazon FBA / DTC | HARD-REJECT | Asking $25K — sub-buybox; consumer-retail/DTC hard-exclude |

## Source Scorecard

Time-sensitive sources scanned this afternoon top-up (per SKILL.md afternoon scope — full Channel 1 + 3 sweep was the morning run's job):

| Source | Category | Status | HTTP | Listings Reviewed | Matches | Last Match Date |
|--------|----------|--------|------|-------------------|---------|-----------------|
| Email Channel (Gmail since 7am — Quiet Light, Flippa-mkt, Everingham & Kerr senders) | Email Inbound | active | 200 | 1 | 0 | — |
| Rejigg | General Marketplace | blocked (single-attempt) | 404 | 0 | — | — |
| Flippa | General Marketplace | active | 200 | 14 | 0 | — |
| Everingham & Kerr | Email-only Broker | active | — | 0 | 0 | — |

Notes:
- Rejigg `/listings` returned 404 (login-gated marketplace; homepage `/` renders case-study tiles for acquired deals, not live listings). Single-attempt block — surface for manual retry / login next run.
- Flippa scanned via public marketplace; 14 surfaced tiles all sub-buybox or DTC/consumer-retail hard-excluded. Marketplace classification per `feedback_marketplace_vs_broker_distinction` — listings flagged for log only, not Slacked.
- Everingham & Kerr is email-only; no new emails since the 7am email-intelligence scan window.
- Email Channel "1 listing reviewed" = the Quiet Light 10:09 broker-blast single-listing email.

## Volume Check

- Deals surfaced today (afternoon contribution): 0
- Deals surfaced today (combined morning + afternoon): 0
- 7-day rolling average: 0/day
- Target: 1-3/day — **BELOW TARGET** (Tue–Thu this week have all produced 0 deals; Friday digest will surface the volume gap with proposed source additions / retirements per Phase 2 weekly digest spec).
