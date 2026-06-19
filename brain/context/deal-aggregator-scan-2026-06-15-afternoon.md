---
schema_version: 1.1.0
date: 2026-06-15
type: output
output_type: deal-aggregator-scan
status: draft
deals_found: 0
sources_scanned: 4
sources_blocked_verified: 0
sources_blocked_single_attempt: 0
email_deals: 0
dealsx_replies: 0
broker_opportunistic: 9
email_scan_status: live
buy_box_source: live
tags: [date/2026-06-15, output, output/deal-aggregator-scan, source/deal-aggregator, topic/deal-aggregator, topic/afternoon-top-up]
---

# Deal Aggregator Scan - 2026-06-15

Afternoon top-up run. Active corpus paths used this run:
- Premium Pest Management -> DealsX keywords + WR row enrichment
- Estate Management Companies -> DealsX keywords + WR row enrichment
- High-End Commercial Cleaning -> DealsX keywords + WR row enrichment
- Specialty Insurance Brokerage -> DealsX keywords + WR row enrichment
- Storage & Related Services for High-Value Collections -> DealsX keywords + WR row enrichment

## Deals Surfaced (sent to Slack individually)
None today.

## Email Inbound Deals
None today.

## DealsX Proprietary Outreach Replies
Inbound owner replies to DealsX cold outreach (Channel 6). Contact handoffs - no financials. Surfaced to Slack, count toward daily volume, do NOT trigger target-discovery.
None today.

## Broker Opportunistic Review
Financially plausible broker/platform listings that do not match an active thesis corpus. Artifact-only by default; use this lane for CIO review and corpus/source tuning.
1. **Real Estate & Property Management Firm** - Rejigg | Revenue $2.7M | EBITDA $659.4K | Property management | Key signals: 1,900 doors, 40-year client relationships, recurring HOA / rental / maintenance revenue | Outside active corpus, but durable recurring cash flow and client stickiness are strong | https://www.rejigg.com/businesses/113576
2. **Trust Property Management Services** - Rejigg | Revenue $2.2M | EBITDA $317.8K | Property management | Key signals: 35+ trust companies, 15+ years, high barriers to entry | Outside active corpus, but the trust-owned-property niche is sticky and referral driven | https://www.rejigg.com/businesses/122169
3. **Telecom Permitting & Zoning Consultancy** - Rejigg | Revenue $864.4K | EBITDA $482.3K | Consulting / permitting | Key signals: multi-year MSAs, 25-state footprint, service-critical workflow for tower owners | Below the current lower bound, but the contract profile is strong | https://www.rejigg.com/businesses/122270
4. **Compliance / Risk Data Services Company** - Rejigg | Revenue $725K | EBITDA $690K | Data services | Key signals: near-100% gross margin, white-label reseller distribution, recurring regulated-workflow usage | Off-corpus but highly recurring and financially efficient | https://www.rejigg.com/businesses/122932
5. **Cloud-Based Back-Office / Marketing Services Firm** - Rejigg | Revenue $517.7K | EBITDA $165.3K | SaaS-adjacent services | Key signals: 80% renewal rates, 20+ years operating history, near-zero churn | Too small for the standard band, but the subscription profile is strong | https://www.rejigg.com/businesses/113461
6. **Insurance Agency** - Rejigg | Revenue $3M | EBITDA $400K | Insurance agency | Key signals: retained book, specialty coverage, renewal-driven revenue | Adjacent to the specialty insurance thesis, but not a direct corpus match | https://www.rejigg.com/businesses/113563
7. **Cleaning Service Business** - Rejigg | Revenue $1.1M | EBITDA $252.7K | Cleaning services | Key signals: 3,200 annual bookings, owner-optional model, no employees | Recurring demand is good, but California soft-exclude keeps it out of pass lanes | https://www.rejigg.com/businesses/111905
8. **Corporate Housing Provider** - Rejigg | Revenue $8M | EBITDA $660K | Corporate housing | Key signals: asset-light recurring demand, competitor exit, established PNW operating history | Durable model, but off-corpus and below the current lower-bound preference | https://www.rejigg.com/businesses/113087
9. **Life Care Management & Patient Advocacy Business** - Rejigg | Revenue $1.3M | EBITDA $281.7K | Patient advocacy / care coordination | Key signals: referral-driven, recession-resistant, aging-population tailwind | Service-critical and recurring, but too small and off-corpus for pass lanes | https://www.rejigg.com/businesses/111178

## Near Misses (not Slacked)
- Property / HOA Management Company - recurring contracts and proprietary software are interesting, but the profitability profile is too thin / unclear to elevate.
- Real Estate Broker - recurring property-management and storage income is interesting, but this is not a current thesis corpus match.
- Real Estate Media and Photography - repeat bookings and proprietary software, but too small and too adjacent to qualify.
- Facilities and Real Estate Advisory Firm - recurring advisory revenue, but weak fit against active corpora.
- Financial Healthcare Staffing Specialists - revenue quality is decent, but staffing is outside current theses.
- Home Warranty Service Business - recurring homeowner contracts, but the revenue scale is far below the current floor.
- Online Human Resources and Benefits Support Business - recurring platform model, but not an active niche.
- Insurance Adjusting Company - contingency-fee workflow is interesting, but it is not a specialty brokerage.
- Enterprise Risk Management Software - strong SaaS metrics, but generic ERM is outside the active SaaS corpus.
- Carpet Cleaning Business - repeat business and reviews are strong, but the category is too small / too consumer-facing.
- Virtual Assistant Business - recurring retainer revenue, but too small and too service-commodity-heavy.

## Listings Reviewed (full log)

| Source | Headline | Geo | Revenue | EBITDA | Margin | Industry | Key Signals | Verdict | Reject Reason |
|--------|----------|-----|---------|--------|--------|----------|-------------|---------|---------------|
| Rejigg | Real Estate & Property Management Firm | TN | $2.7M | $659.4K SDE | undisclosed | Property management | recurring revenue; 40-year client relationships | BROKER-OPPORTUNISTIC | Outside active corpus; below preferred lower bound |
| Rejigg | Trust Property Management Services | undisclosed | $2.2M | $317.8K SDE | undisclosed | trust property management | recurring revenue; 35+ trust companies; high barriers | BROKER-OPPORTUNISTIC | Outside active corpus; below preferred lower bound |
| Rejigg | Telecom Permitting & Zoning Consultancy | undisclosed | $864.4K | $482.3K SDE | undisclosed | telecom permitting / consulting | multi-year MSAs; service-critical workflow; sticky contracts | BROKER-OPPORTUNISTIC | Below preferred lower bound; preserved because contracts are durable |
| Rejigg | Compliance / Risk Data Services Company | undisclosed | $725K | $690K SDE | near-100% gross margin | risk / compliance data services | recurring data-as-a-service; white-label distribution | BROKER-OPPORTUNISTIC | Off-corpus but financially efficient and recurring |
| Rejigg | Cloud-Based Back-Office / Marketing Services Firm | undisclosed | $517.7K | $165.3K SDE | undisclosed | subscription back-office services | 80% renewal; 20+ years; near-zero churn | BROKER-OPPORTUNISTIC | Too small for current lower bound; off-corpus |
| Rejigg | Insurance Agency | OH | $3M | $400K SDE | undisclosed | insurance agency | retained book; specialty coverage; renewals | BROKER-OPPORTUNISTIC | Adjacent to thesis, but not a specialty brokerage corpus match |
| Rejigg | Cleaning Service Business | CA | $1.1M | $252.7K SDE | 30-35% net margins | cleaning services | 3,200 annual bookings; owner-optional; no employees | BROKER-OPPORTUNISTIC | California soft-exclude and off-corpus |
| Rejigg | Corporate Housing Provider | WA | $8M | $660K SDE | undisclosed | corporate housing | asset-light recurring demand; competitor exit | BROKER-OPPORTUNISTIC | Off-corpus and below preferred lower bound |
| Rejigg | Life Care Management & Patient Advocacy Business | undisclosed | $1.3M | $281.7K EBITDA | undisclosed | care management / advocacy | referral-driven; recession-resistant; service-critical | BROKER-OPPORTUNISTIC | Off-corpus and below preferred lower bound |
| Rejigg | Property / HOA Management Company | undisclosed | $1.95M | $7.2K SDE | undisclosed | HOA management | auto-renewing contracts; proprietary internal software | NEAR-MISS | Profitability profile unclear / thin |
| Rejigg | Real Estate Broker | OR | $235K | $107.7K SDE | nearly 50% SDE margin | real estate brokerage | recurring property-management and storage revenue | NEAR-MISS | Too small and not an active corpus match |
| Rejigg | Real Estate Media and Photography | undisclosed | $700K | $140K EBITDA | undisclosed | real estate media | proprietary booking software; 1099 contractor model | NEAR-MISS | Too small and too adjacent |
| Rejigg | Facilities and Real Estate Advisory Firm | undisclosed | $4M | $411.2K SDE | undisclosed | advisory services | revenue growth; recurring advisory work | NEAR-MISS | Off-corpus and too advisory-driven |
| Rejigg | Financial Healthcare Staffing Specialists | undisclosed | $2.8M | $294.6K SDE | undisclosed | staffing | contract-to-direct-hire mix; established client | NEAR-MISS | Staffing is outside current corpora |
| Rejigg | Home Warranty Service Business | FL | $211.4K | $98.9K SDE | above 45% SDE margin | home warranty | recurring homeowner contracts; remote model | NEAR-MISS | Revenue scale far below the current floor |
| Rejigg | Online Human Resources and Benefits Support Business | undisclosed | $600K | $400K SDE | above 65% SDE margin | HR / benefits support | platform-mediated recurring support | NEAR-MISS | Off-corpus and too small |
| Rejigg | Insurance Adjusting Company | undisclosed | $1.2M | $350K EBITDA | undisclosed | insurance adjusting | contingency-fee model; zero debt; team depth | NEAR-MISS | Not a brokerage corpus match |
| Rejigg | Enterprise Risk Management Software | undisclosed | undisclosed | undisclosed | 85% recurring revenue | SaaS / ERM software | eight-year tenure; 30% ARR growth; no sales team | NEAR-MISS | Generic SaaS outside active niche corpus |
| Rejigg | Carpet Cleaning Business | TX | $142.7K | $139.2K SDE | undisclosed | carpet cleaning | 3,000+ customers; 75-80% repeat business | NEAR-MISS | Too small and consumer-facing |
| Rejigg | Virtual Assistant Business | undisclosed | $201.3K | $15.3K SDE | undisclosed | virtual assistant staffing | retainer-based recurring revenue | NEAR-MISS | Too small and commodity-like |
| Rejigg | Luxury Pool Construction Services | undisclosed | $5.4M | $1.9M EBITDA | undisclosed | pool construction | affluent market; word-of-mouth referrals | HARD-REJECT | Construction / labor-heavy field service |
| Rejigg | Damage Restoration Construction Services | NC | $7.2M | $921.7K SDE | undisclosed | restoration / reconstruction | franchise; roofing division; claims-heavy work | HARD-REJECT | Construction-heavy franchise model |
| Rejigg | Design Build Construction Management Firm | undisclosed | $120M+ throughput | $1.9M SDE | undisclosed | construction management | regulated-facility design-build; very large scale | HARD-REJECT | Construction-heavy and far outside target size |
| Rejigg | Residential Home Construction Company | WI | $3.5M | $400K EBITDA | undisclosed | home construction | backlog into 2027; residential builder/remodeler | HARD-REJECT | Residential construction is outside buy box |
| Rejigg | Healthcare Real Estate Investment Firm | undisclosed | $940.6K | $499.2K SDE | undisclosed | investment / real estate | $370M acquisitions; AUM model | HARD-REJECT | Investment firm, not an operating service business |
| Rejigg | Mushroom Wellness Products Business | undisclosed | $2.1M | $335.9K SDE | undisclosed | consumer wellness products | private label / contract manufacturing | HARD-REJECT | Consumer product business outside target thesis |
| Rejigg | Suburban Auto Repair Franchise | IL | $1.8M | $213.7K SDE | undisclosed | auto repair franchise | lease through 2032; franchise system dissolving | HARD-REJECT | Franchise / auto repair outside current buy box |

## Source Scorecard

| Source | Category | Status | HTTP | Listings Reviewed | Matches | Last Match Date |
|--------|----------|--------|------|-------------------|---------|-----------------|
| Rejigg | Marketplace | active | 200 | 27 | 0 | — |
| Flippa | Marketplace | active | 200 | 0 | 0 | — |
| Everingham & Kerr | Advisory | active | 200 | 0 | 0 | — |
| Email channel | Email | active | 200 | 0 | 0 | — |

## Volume Check
- Deals surfaced today: 0
- Broker-opportunistic review items: 9
- 7-day rolling average: 0.0
- Target: 1-3/day - CRITICAL
- Email leg: live
- Funnel bottleneck: source coverage
