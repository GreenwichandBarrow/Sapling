---
schema_version: 1.1.0
date: 2026-04-28
type: context
title: "Deal Aggregator Scan — 2026-04-28 (Afternoon Top-Up)"
deals_found: 0
sources_scanned: 4
sources_blocked_verified: 1
sources_blocked_single_attempt: 0
email_deals: 0
buy_box_source: live
morning_artifact_missing: true
tags: [date/2026-04-28, context, output/deal-aggregator-scan, topic/deal-aggregator, status/draft]
---

# Deal Aggregator Scan — 2026-04-28 (Afternoon Top-Up)

Afternoon `--afternoon` run. Lightweight rescan of email channel + time-sensitive platforms (Rejigg, Flippa, Everingham & Kerr). Channel 1 + 3 full sweep skipped per SKILL.md — that is the morning run's job.

**Note for diagnostics:** today's morning artifact (`brain/context/deal-aggregator-scan-2026-04-28.md`) is missing — the morning launchd fire either didn't run or didn't write its artifact. Afternoon run executed regardless. Surface to health-monitor for Friday review.

**Buy-boxes:** all three (Services / Insurance / SaaS) re-read live from Drive at run start. **Active niches:** all 8 re-read live from `WEEKLY REVIEW` (Premium Pest, Private Art Advisory, Estate Mgmt, Specialty Coffee Equipment Service, High-End Commercial Cleaning, Vertical SaaS Luxury, Specialty Insurance Brokerage Art & Collectibles, High-Value Storage). **Email scan:** [[brain/context/email-scan-results-2026-04-28]] — zero CIMs/NDAs/teasers/financials inbound; one BLAST from Helen Guo SMB Deal Hunter (generic, no niche match, skipped per Channel 2 dedup rules).

## Deals Surfaced (sent to Slack individually)

None today.

## Email Inbound Deals

None today. The lone BLAST in today's email-scan-results (Helen Guo SMB Deal Hunter, "Boring business, $700K/yr, 60% seller financed") is generic broker blast content — no specific niche, no industry signal, $700K revenue fails Services Buy Box floor ($10M). Skipped per Channel 2 rules.

## Near Misses (not Slacked)

- **Flippa "$50K/mo (~$450K ARR) subscription app"** — disclosed ARR is $600K, fails SaaS Buy Box floor ($3M). Auto-reject on disclosed-and-failed. Not Slacked.
- **Flippa "Education SaaS $63K ARR"** — disclosed ARR is $63K, fails SaaS Buy Box floor by ~50x. Auto-reject. Not Slacked.
- **Flippa "Real Estate Comparison Platform"** — likely wrong operating layer (lead-gen / comparison marketplace, not B2B services to luxury operators). No revenue/EBITDA disclosed; even on Data Availability Rule, the industry hard-exclude on lead-gen/marketing wrong-layer (per `feedback_startup_vs_mature_layer` style logic) means skip.
- **Flippa "30+ Year Skincare Brand at Luxury Retailers"** — DTC/consumer-retail brand. Services Buy Box hard-exclude on "Consumer retail / DTC". Auto-reject.

## Source Scorecard

| Source | Category | Status | HTTP | Listings Reviewed | Matches | Last Match Date |
|--------|----------|--------|------|-------------------|---------|-----------------|
| Rejigg | General (Time-Sensitive) | blocked (verified) | 404 | 0 | 0 | — |
| Flippa | General (Time-Sensitive) | active | 200 | ~35 | 0 | — |
| Everingham & Kerr | General (Email-Only, Time-Sensitive) | active (email channel) | n/a | 0 | 0 | — |
| Email Inbound (Channel 2) | Email | active | n/a | 1 BLAST | 0 | — |

**Status notes:**
- **Rejigg:** `/listings` and `/marketplace` both 404 (two attempts). Homepage 200 but marketing-only — no public listing data. Platform requires buyer registration; public scrapability verified absent. Pattern matches "registered-buyer-only" classification.
- **Flippa:** 200 with content, ~35 listings on the recently-sold feed. All are DTC/ecom/micro-SaaS in the $50K–$3M revenue band — none pass any G&B buy-box gate. Expected pattern (Flippa is digital-first SMB-focused).
- **Everingham & Kerr:** email-only intermediary per SKILL.md. Channel works via email-intelligence handoff. No Everkerr blasts in today's email-scan-results. Channel healthy, zero blasts ≠ blocked.
- **Email Inbound:** one BLAST classified, zero deal-flow direct inbound. Channel healthy.

## Volume Check

- Deals surfaced today (afternoon): **0**
- Combined morning + afternoon total: **0** (morning artifact missing — full-day total cannot be computed)
- Target: 1–3/day — **BELOW TARGET** (afternoon top-up surfaced no new matches; morning run's volume unknown)
- Fingerprint store at run start: empty (0 bytes) — no dedup conflicts possible
- Fingerprint store at run end: unchanged (no Slack posts → no fingerprint appends)
