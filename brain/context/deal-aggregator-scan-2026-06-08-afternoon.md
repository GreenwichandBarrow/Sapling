---
schema_version: 1.1.0
date: 2026-06-08
deals_found: 1
sources_scanned: 4
sources_blocked_verified: 0
sources_blocked_single_attempt: 0
email_deals: 8
dealsx_replies: 1
broker_opportunistic: 1
email_scan_status: late_recovered
tags: [date/2026-06-08, context, output/deal-aggregator-scan, source/deal-aggregator, status/done, topic/deal-aggregator]
title: "Deal Aggregator Scan - 2026-06-08 Afternoon"
---
# Deal Aggregator Scan — 2026-06-08 Afternoon

## Deals Surfaced (sent to Slack individually)
1. **DealsX reply — owner responded to outreach** — [[entities/dealsx|DealsX]] | not disclosed | not disclosed | inbound contact handoff | thread `19ea2db0e9a5f672`

## Email Inbound Deals
1. **Adult Classifieds Platform** — Flippa | $2.1M annual revenue | undisclosed EBITDA | online classifieds platform | Denmark | no active thesis match
2. **Health Shopify Brand** — Flippa | $2.1M annual revenue | undisclosed EBITDA | DTC health & beauty / Shopify | undisclosed | no active thesis match
3. **Festival-Wear Shopify Brand** — Flippa | $277K annual revenue | undisclosed EBITDA | festival-wear ecommerce | NYC showroom / New York City | no active thesis match
4. **WordPress Theme Shop** — Flippa | $40K annual revenue | undisclosed EBITDA | WordPress themes and templates | undisclosed | no active thesis match
5. **High-Growth Golf SaaS / Golfpay** — Flippa | $344,418 TTM revenue | TTM profit $136,055 | AI SaaS for golf courses | Arizona | no active thesis match
6. **Baby Amazon FBA** — Flippa | $6.7M annual revenue | undisclosed EBITDA | Amazon FBA / ecommerce | undisclosed | no active thesis match
7. **Luxury Fashion Ecommerce** — Flippa | $8.2M annual revenue | undisclosed EBITDA | luxury fashion ecommerce | undisclosed | no active thesis match
8. **14mm Ask! Waterfront Beach Club & Event Venue - 36+ Years Established** — BizBuySell | asking price $13.6M | undisclosed EBITDA | beach club / event venue | Mamaroneck, NY | hospitality / nightlife

## DealsX Proprietary Outreach Replies
Inbound owner replies to [[entities/dealsx|DealsX]] cold outreach. Contact handoffs only.
1. **Lead notification** — thread `19ea2db0e9a5f672` | lead details not disclosed in scan artifact | surfaced to Slack

## Broker Opportunistic Review
Financially plausible broker/platform listings that do not match an active thesis corpus.
1. **Insurance Agency** — Rejigg | $3M annual revenue | $400K SDE | insurance brokerage | Key signals: recurring commissions, renewals | Financially plausible broker listing outside current corpus; preserve for CIO review | https://www.rejigg.com/for-sale/insurance

## Near Misses
- [[entities/everingham-kerr|Everingham & Kerr]] buyer client - Landscaping Company — buy-side search letter, not a sell-side deal
- Insurance Consulting Business — Rejigg | recurring commissions, but revenue/scale below current buy-box floor
- Cleaning Service Business — Rejigg | service business with no disclosed evidence of current buy-box scale
- Janitorial Services Business — Rejigg | recurring contract services, but too small for current buy-box
- Exterior Residential & Commercial Cleaning Services — Rejigg | recurring service profile, but below floor
- Commercial Window Cleaning Service — Rejigg | recurring commercial service, but below floor
- Insurance Adjusting Company — Rejigg | wrong operating layer for the insurance brokerage buy box

## Listings Reviewed (full log)

| Source | Headline | Geo | Revenue | EBITDA | Margin | Industry | Key Signals | Verdict | Reject Reason |
|--------|----------|-----|---------|--------|--------|----------|-------------|---------|---------------|
| Rejigg | Insurance Agency | OH | $3M annual revenue | undisclosed | undisclosed | Insurance brokerage | recurring commissions, renewals | BROKER-OPPORTUNISTIC | No active-niche corpus match; keep for CIO review |
| Rejigg | Insurance Consulting Business | undisclosed | $750K annual revenue | undisclosed | undisclosed | Insurance consulting | recurring commissions | NEAR-MISS | Scale below current floor |
| Rejigg | Cleaning Service Business | undisclosed | $1.1M annual revenue | undisclosed | undisclosed | Cleaning / referral agency | not disclosed | NEAR-MISS | Too small for current floor and no active thesis match |
| Rejigg | Janitorial Services Business | undisclosed | $700K annual revenue | undisclosed | undisclosed | Janitorial / commercial cleaning | recurring contract services | NEAR-MISS | Below floor |
| Rejigg | Exterior Residential & Commercial Cleaning Services | undisclosed | $1.9M annual revenue | $350K SDE | undisclosed | Exterior cleaning | recurring service | NEAR-MISS | Below floor |
| Rejigg | Commercial Window Cleaning Service | undisclosed | $1M annual revenue | undisclosed | undisclosed | Commercial window cleaning | recurring commercial service | NEAR-MISS | Below floor |
| Rejigg | Insurance Adjusting Company | undisclosed | undisclosed | undisclosed | undisclosed | Claims / adjusting | not disclosed | HARD-REJECT | Wrong operating layer for the insurance brokerage buy box |
| Flippa | Adult Classifieds Platform | undisclosed | $2.1M annual revenue | undisclosed | 92% | Online classifieds platform | recurring listing products | HARD-REJECT | Consumer/digital classifieds; no active thesis match |
| Flippa | Health Shopify Brand | undisclosed | $2.1M annual revenue | undisclosed | 67% | DTC health & beauty | not disclosed | HARD-REJECT | Consumer retail / DTC |
| Flippa | Festival-Wear Shopify Brand | NY | $277K annual revenue | undisclosed | undisclosed | Festival-wear ecommerce | not disclosed | HARD-REJECT | Consumer retail / DTC |
| Flippa | WordPress Theme Shop | undisclosed | $40K annual revenue | undisclosed | 88% | Digital templates | not disclosed | HARD-REJECT | Horizontal digital product; below floor |
| Flippa | High-Growth Golf SaaS / Golfpay | AZ | $344,418 TTM revenue | $136,055 TTM profit | undisclosed | SaaS for golf courses | repeat usage, but too small | HARD-REJECT | ARR/revenue far below SaaS floor |
| Flippa | Baby Amazon FBA | undisclosed | $6.7M annual revenue | undisclosed | undisclosed | Amazon FBA / ecommerce | not disclosed | HARD-REJECT | Consumer ecommerce / retail |
| Flippa | Luxury Fashion Ecommerce | undisclosed | $8.2M annual revenue | undisclosed | undisclosed | Luxury fashion ecommerce | not disclosed | HARD-REJECT | Consumer retail / DTC |
| BizBuySell | Waterfront Beach Club & Event Venue - 36+ Years Established | NY | $13.6M asking price | undisclosed | undisclosed | Beach club / event venue | not disclosed | HARD-REJECT | Hospitality / nightlife hard no |
| Everingham & Kerr | Buyer Client - Landscaping Company | undisclosed | undisclosed | undisclosed | undisclosed | Buy-side search letter | buy-side, not sell-side | HARD-REJECT | Buyer-side search, not a sell-side deal |

## Source Scorecard

| Source | Category | Status | HTTP | Listings Reviewed | Matches | Last Match Date |
|--------|----------|--------|------|-------------------|---------|-----------------|
| Rejigg | General (time-sensitive) | active | 200 | 7 | 0 | — |
| Flippa | General (email-driven) | active (email) | n/a | 8 | 0 | — |
| Everingham & Kerr | General (email-only, time-sensitive) | active (email) | n/a | 1 | 0 | — |
| email channel | Email inbound | late_recovered | n/a | 9 | 0 | — |

## Volume Check
- Deals surfaced today: 1
- Broker-opportunistic review items: 1
- 7-day rolling average: 0.33
- Target: 1-3/day — BELOW TARGET
- Email leg: late_recovered
- Funnel bottleneck: source quality
