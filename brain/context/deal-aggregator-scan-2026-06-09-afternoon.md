---
date: 2026-06-09
deals_found: 0
sources_scanned: 4
sources_blocked_verified: 0
sources_blocked_single_attempt: 1
email_deals: 0
dealsx_replies: 0
broker_opportunistic: 0
email_scan_status: live
buy_box_source: live
morning_artifact_missing: false
---
# Deal Aggregator Scan — 2026-06-09 (Afternoon Top-Up)

Afternoon `--afternoon` run. Live buy-boxes re-read from Drive, live active niches re-read from WEEKLY REVIEW, today's `email-scan-results-2026-06-09.md` re-read, and time-sensitive platforms rescanned (Rejigg, Flippa, Everingham & Kerr). Morning artifact (`brain/context/deal-aggregator-scan-2026-06-09.md`) was present and left untouched.

**Result: 0 new evaluable deals this afternoon.** Rejigg exposed 10 visible listings in embedded JSON; all 10 were hard-rejects. Flippa remained a JS shell and could not be fully parsed without browser automation, which is unavailable on this host. Everingham & Kerr published only closed transactions on the website and the email channel produced no new deal-classified inbound after the morning scan.

## Deals Surfaced (sent to Slack individually)
None today.

## Email Inbound Deals
None today. `email-scan-results-2026-06-09.md` was present and read live, but it contained no CIMs, broker blasts, or direct deal threads that qualified as inbound deal flow after the morning run.

## DealsX Proprietary Outreach Replies
None today.

## Broker Opportunistic Review
None today.

## Near Misses (not Slacked)
None today.

## Listings Reviewed (full log)

| Source | Headline | Geo | Revenue | EBITDA | Margin | Industry | Key Signals | Verdict | Reject Reason |
|--------|----------|-----|---------|--------|--------|----------|-------------|---------|---------------|
| Rejigg | Wound Treatment Device Manufacturer | MN | $11.3M | $3.35M | 29.6% | Medical device manufacturing | recurring disposable components | HARD-REJECT | Capital-intensive manufacturing hard-exclude |
| Rejigg | Supply Chain SaaS Platform | NC | $898K | -$1.90M | -211.1% | Horizontal SaaS / supply chain software | service criticality | HARD-REJECT | Horizontal SaaS hard-exclude + negative EBITDA |
| Rejigg | Marketing Analytics Platform Provider | TX | $1.21M | $294K | 24.2% | Marketing analytics / SaaS-services hybrid | service criticality | HARD-REJECT | Horizontal SaaS / software-services mix + revenue below floor |
| Rejigg | Faculty Credentialing & Management EdTech Business | VA | $973K | $235K | 24.2% | EdTech software | service criticality | HARD-REJECT | Revenue below SaaS floor; not clearly vertical SaaS for active thesis |
| Rejigg | Roofing Business | IL | $2.0M | $137K | 6.9% | Roofing / construction services | not disclosed | HARD-REJECT | Construction hard-exclude + EBITDA margin below 10% floor |
| Rejigg | Vendor Management Company | FL | $1.04M | $173K | 16.7% | Vendor management services | recurring invoice/contract review | HARD-REJECT | Revenue and EBITDA below Services floor |
| Rejigg | Data Discovery Platform | WA | $2.58M | $1.77M | 68.7% | Data aggregation / horizontal software | service criticality | HARD-REJECT | Horizontal data platform hard-exclude + revenue below SaaS floor |
| Rejigg | Paper Products Business | PA | $2.04M | $267K | 13.1% | Paper products / production and distribution | not disclosed | HARD-REJECT | Revenue and EBITDA below Services floor; manufacturing/distribution profile |
| Rejigg | Water Filtration E-Commerce Business | undisclosed | $3.0M | $1.19M | 40.2% | DTC e-commerce / water filtration | recurring filter sales | HARD-REJECT | Consumer retail / DTC hard-exclude + revenue below Services floor |
| Rejigg | Critical Infrastructure & Thermal Management Systems Integrator | LA | $11.8M | $81K | 0.7% | Infrastructure equipment integration / distribution | service criticality | HARD-REJECT | EBITDA margin below 10% floor |

## Source Scorecard

| Source | Category | Status | HTTP | Listings Reviewed | Matches | Last Match Date |
|--------|----------|--------|------|-------------------|---------|-----------------|
| Rejigg | General | active | 200 | 10 | 0 | — |
| Flippa | General | blocked (single-attempt) | 200 (JS shell) | 0 | 0 | — |
| Everingham & Kerr | Email-only broker (time-sensitive) | active | 200 | 0 | 0 | — |
| Email channel (email-scan-results) | Inbound | active | n/a | 0 | 0 | — |

Notes:
- **Rejigg** — `/businesses` exposed 10 visible listings in embedded JSON; all 10 were reviewed and hard-rejected on disclosed criteria or hard-excludes. No active-niche corpus match.
- **Flippa** — search page loaded as a JS shell. Browser automation is unavailable on this host, so the source was marked `blocked (single-attempt)` rather than silently skipped.
- **Everingham & Kerr** — website exposes closed transactions only; no active for-sale listings. Today's email-scan had no new E&K deal blast after the morning run.
- **Email channel** — `email-scan-results-2026-06-09.md` was present and live, but contained no actionable inbound deal email.

## Volume Check
- Deals surfaced today: 0
- Broker-opportunistic review items: 0
- 7-day rolling average: 0.29/day
- Target: 1-3/day — BELOW TARGET
- Email leg: live
- Funnel bottleneck: source quality
