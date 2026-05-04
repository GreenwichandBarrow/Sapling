---
schema_version: 1.2.0
date: 2026-05-04
type: enrichment
status: review
skill_origin: deal-aggregator
kay_approved: null
kay_approval_date: null
people: []
companies: []
projects: []
tags: ["date/2026-05-04", "output", "output/enrichment", "status/review", "topic/broker-channel", "topic/deal-screening", "topic/flippa", "topic/buy-box-application"]
---

# Tory @ Flippa B2B Trade Fair Listing Enrichment, 2026-05-04

Source: deal-aggregator broker buy-box rerun ([[outputs/2026-05-04-deal-aggregator-rerun-broker-buy-box]]) flagged the $16M B2B Trade Fair Exhibitor Recruitment Service from Tory @ Flippa's 2026-04-23 BLAST as the cleanest FLAG candidate. This file applies the locked broker buy-box ([[outputs/2026-05-04-broker-channel-buy-box-draft]]) and renders the verdict.

## Verdict: HARD-REJECT

The listing fails the broker buy-box on the geography hard gate and on a structural mismatch between Flippa's marketplace model and the G&B broker-channel relationship-building thesis. It also fails the implicit "Tory is a real broker" premise the parent rerun assumed.

## Source Email Detail

- **Email date:** 2026-04-23, 13:59 -0500 (Thursday)
- **From:** Tory @ Flippa <marketing@flippa.com>
- **To:** admin@greenwichandbarrow.com
- **Subject:** $16M Annual Rev B2B Trade Fair Exhibitor Recruitment Service
- **Gmail ID:** 19dbbb5b68d54aa1
- **Format:** Multi-listing newsletter BLAST. The B2B Trade Fair listing was the "TODAY'S TOP DEAL" hero card; four additional listings (Logistics SaaS, Sports Shopify, Recipe Binder FBA, Health/Gut Health Shopify) appeared below.

## Listing Detail (from email body)

| Field | Value | Source |
|---|---|---|
| Headline | Established B2B Trade Fair Exhibitor Recruitment Service | Email body |
| Description | "13-year-old B2B platform connecting global exhibitors with international trade fairs. Generates revenue via exhibitor recruitment and participation sales." | Email body |
| Annual revenue | $16M | Email body |
| Profit margin | 30% | Email body |
| YoY growth | 34% | Email body |
| Implied EBITDA | $4.8M (16M x 30%) | Computed |
| Asking price | Not disclosed in email | n/a |
| Business location | Not disclosed in email; description says "global" / "international trade fairs" | Email body |
| Employee count | Not disclosed | n/a |
| Ownership structure | Not disclosed | n/a |
| Industry classification | B2B platform / business-services / event-services exhibitor recruitment | Inferred |

## Broker Detail (CRITICAL CORRECTION)

The parent task assumed Tory @ Flippa was the broker. **He is not.** "Tory @ Flippa" is the bylined sender of Flippa's daily marketing newsletter (`marketing@flippa.com`), curating multiple listings per blast. The B2B Trade Fair listing's actual broker, named in the email body, is:

- **Amber Burke**, Business Broker
- **Location:** Baltimore, Maryland
- **Affiliation:** Listed as broker on Flippa's marketplace; specific brokerage firm not disclosed in email
- **Contact in email:** "Book a Call" link only (Flippa-mediated routing); no direct email or phone surfaced in the BLAST
- **Specialty / prior volume:** Not findable in 2026-05-04 web research (Flippa user / profile pages return 303 / 404; LinkedIn lookup blocked; Google search did not return a public broker bio)

Implication: any outreach to "Tory" would land in `marketing@flippa.com`, the no-reply newsletter inbox. To reach a real human on this listing, contact would have to be Amber Burke via the Flippa "Book a Call" routing, which is the gatekeeper-style competitive funnel G&B's broker-relationship strategy is built to avoid.

## Listing Page Verification (Data Limitation)

Per task constraints, attempted to load the actual Flippa listing page. The newsletter URL is a HubSpot tracking redirect (`l.flippa.com/...`) that returns a redirect-bridge page with no listing content. A direct Flippa marketplace search for "B2B Trade Fair Exhibitor Recruitment" returned zero matches as of 2026-05-04, suggesting the listing has been delisted, sold, or moved off-market in the 11 days since the BLAST. Per task spec, did not attempt to authenticate or scrape around the gating. Documented and stopped.

## Buy-Box Application

| Criterion | Threshold | Listing | Pass? |
|---|---|---|---|
| Geography hard gate | NY, NJ, PA, CT only | Unknown business location; description is "global" / "international." Broker is Baltimore, MD. | **NO (FAIL)** |
| Revenue | $5M to $50M | $16M | YES |
| EBITDA | $2M practical floor | $4.8M (implied) | YES |
| Margin | 15%+ | 30% | YES |
| Hard exclude (CA, lending, carve-out, fashion, franchise, restaurant, capital-intensive mfg, physician practice, construction, PE roll-up) | None hit | None of the listed excludes apply on the surface, but business model risk discussed below | YES on the literal list |

Geography fails outright. Even if the operating entity is US-domiciled, the business itself is described as "connecting global exhibitors with international trade fairs," which means revenue, customers, and operations are not concentrated in NY / NJ / PA / CT. The G&B broker-channel buy-box is a HARD GATE on geography per `feedback_broker_channel_opportunistic_floor`; the gate fails.

## Structural Concerns Beyond the Buy-Box

1. **Flippa marketplace model is the wrong layer for G&B broker-channel relationship building.** Flippa is a digital-first marketplace for primarily online businesses (SaaS, ecommerce, content sites, FBA brands). Listings are exposed to a high-volume buyer pool, exactly the 3000+ buyer cattle-call pattern `feedback_broker_competition` warned against. Brokers on Flippa are mostly transaction-execution intermediaries on a single deal, not relationship-channel partners worth a 3-touch G&B cadence. The broker-channel build in `vivid-booping-starfish` was scoped for traditional NY-tristate Main Street brokers (Transworld, Sunbelt, Murphy, etc.), not Flippa marketplace listing agents.

2. **34% YoY growth and 30% margin will get bid up fast on Flippa.** Listings with these metrics in this revenue range typically draw heavy bidder action within weeks. Even if every other gate cleared, G&B's odds against the broader Flippa buyer pool are low, consistent with `feedback_broker_competition`.

3. **"Connecting global exhibitors with international trade fairs" reads as a digital marketplace / lead-gen platform, not a service business.** Operationally this looks closer to an online matchmaking platform for trade fair participation than a hands-on B2B service. Without more detail (ownership of fairs, recurring contracts vs transactional placements, customer concentration, churn), this is materially harder to underwrite than a typical Main Street services target.

4. **The listing may already be off-market.** The Flippa marketplace search returned zero matches on 2026-05-04. If the listing was withdrawn or sold inside the 11-day window, any outreach is moot.

## Industry Translation: What "B2B Trade Fair Exhibitor Recruitment Service" Means Operationally

A platform that helps exhibitors (companies that pay to set up booths at trade fairs) find and book participation in trade fairs run by third-party fair organizers. Revenue mechanics typically: commission on booked exhibitor placements, subscription fees from exhibitors for premium listing visibility on the platform, or a combo. Customer base: B2B companies in industries that exhibit at international trade shows (manufacturing, industrial, medical devices, food, etc.). Closest comparable in G&B's framing: an online marketplace / lead-gen middleman for the global trade fair industry, not an operationally-critical B2B service provider in a single niche.

## Recommendation

**Kill, do not outreach to Amber Burke or Tory.** Reasons in priority order:

1. Geography hard gate fails. Business is global / international, broker is in Baltimore.
2. Flippa marketplace listings are wrong layer for G&B broker-channel relationship building.
3. Listing may already be off-market.
4. Operating model (online marketplace platform) does not match the operationally-critical-services thesis.

This finding also surfaces a calibration signal for the parent rerun: the deal-aggregator broker buy-box rerun should treat Flippa newsletter blasts as a **separate channel** from traditional broker BLASTs and not flag Flippa listings into the broker-channel funnel without first checking (a) whether Flippa even surfaces a real broker (about half of Flippa listings are owner-self-listed) and (b) whether the underlying business has US-tristate operations.

## No Day 0 Email Drafted

Per task spec, Day 0 outreach is drafted only when verdict is PASS or FLAG-with-soft-data-gap. HARD-REJECT skips the draft. The 60-80 word slot remains unused.

## Related Files

- [[outputs/2026-05-04-deal-aggregator-rerun-broker-buy-box]] (parent rerun that flagged this listing)
- [[outputs/2026-05-04-broker-channel-buy-box-draft]] (locked buy-box criteria applied here)
- [[outputs/2026-05-04-broker-outreach-templates]] (Day 0 / 5 / 12 templates, not used)

## Related Memories

- `feedback_broker_channel_opportunistic_floor` (broker-channel geography hard gate)
- `feedback_broker_competition` (3000+ buyer broker pool, G&B rarely wins)
- `feedback_broker_emails` (concise broker outreach pattern, not used here)
- `feedback_no_search_fund_language_intermediaries`
- `feedback_strategic_thresholds_need_grounding`

## Outcome

- **Published:** null
- **Engagement:** null
- **Hypothesis result:** pending
