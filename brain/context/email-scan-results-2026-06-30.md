---
schema_version: 1.1.0
date: 2026-06-30
type: context
title: "Email Scan Results - 2026-06-30"
status: done
source: email-intelligence
tags: [date/2026-06-30, context, output/email-scan-results, source/email-intelligence, status/done, topic/email-intelligence]
---

# Email Scan Results - 2026-06-30

## 1. Actionable Items Created

None.

System status:
- No CIM, NDA, active-deal document, or bookkeeper Management Report / P&L trigger was detected in `[[context/email-intelligence-input-2026-06-30]]`.
- Granola returned no updated notes since 2026-06-29T00:00:00Z, so no `brain/calls/` files were created.
- The monthly missing-report watchdog ran because 2026-06-30 is the last calendar day of the month. `[[outputs/2026-06-20-budget-report-may-2026]]` exists, so no prior-month Management Report gap was raised.

## 2. Deal Flow Classified

Inbound scan summary from `[[context/email-intelligence-input-2026-06-30]]`:
- DIRECT: 7
- BLAST: 22
- NEWSLETTER: 50

Reviewed sources:
- 79 inbound or deal-label messages in the compact context artifact.
- 0 outbound messages in the compact context artifact.
- 1 Gmail draft in the compact context artifact.
- 46 deal-flow-labeled threads fetched with `--sanitize-content` for targeted broker-listing extraction only.

## 3. Draft Status

- Gmail drafts scanned: 1
- Sent: 0 surfaced in the live Gmail draft list.
- Unsent: 1
- Unsent older than 48 hours: 1

| draft_id | age | to | subject | thread_id | status |
|---|---:|---|---|---|---|
| r-2617485536768457504 | about 7.8 days | [[entities/andrew-saltoun|Andrew Saltoun]] | blank subject | 19ef0337e00067d8 | DRAFT |

Notes:
- The draft snippet begins "Hi Andrew, Hope Japan was wonderful..." and offers Thursday / Friday availability.
- No prior-workday session-decision entry suppressed this stale-draft flag.

## 4. Introductions Detected

None new.

Intro-adjacent personal/network threads were present in metadata, but no explicit new-introduction body signal was exposed in the compact artifact or targeted deal-flow fetches. No entity or inbox item was created from metadata alone.

## 5. Niche Signals

- Broker and marketplace deal flow stayed concentrated in Flippa, Quiet Light, BizQuest, SMB Deal Hunter, Everingham & Kerr, Axial, Transworld, Benchmark International, and Prospect Geni.
- Local services appeared repeatedly: commercial cleaning, septic/liquid waste, water filtration, insulation/weatherization, steel railing fabrication, landscaping, HVAC/plumbing, tree service, solar contracting, signage, telecommunications engineering, and health/wellness clubs.
- Digital and ecommerce inventory remains high-volume but less thesis-aligned: SaaS, content/media assets, Amazon FBA, ecommerce brands, online casino, crypto/media, video hosting, SEO, fragrance, peptides, and YouTube/media channels.
- [[entities/dealsx|DealsX]] / Prospect Geni produced "Lead Interested" notifications. These remain cold-but-live re-engagement signals for the DealsX channel, not Kay-email nudge candidates.
- No StartVirtual monthly Management Report signal appeared, so the `budget-manager monthly` chain did not fire.

### Granola Action Items

None. Granola returned no updated notes in this run.

## 6. In-Person Meetings Today

None confirmed as in-person.

Calendar context did show one external Zoom meeting today: [[entities/megan-lawlor|Megan Lawlor]] <> [[entities/kay-schneider|Kay]], 1:30pm to 2:00pm ET. It is not an in-person meeting.

## 7. Broker BLAST Listings (per-deal extraction)

| source | headline | geo | revenue | ebitda | margin | industry | flag_reason | gmail_msg_id | listing_ordinal |
|---|---|---|---|---|---|---|---|---|---:|
| Ian Drogin / Quiet Light | EU-Based Amazon FBA Gardening Business / 1x Multiple / 30% Inventory Discount / 84% Gross Profit Margins | undisclosed | $131,770 | undisclosed | 84% gross profit | garden / Amazon FBA | single-listing-blast | 19ef4d05a193c937 | 1 |
| Everingham & Kerr | New Buyer Client Acquisition Search - Landscaping Company | undisclosed | undisclosed | undisclosed | undisclosed | landscaping | single-listing-blast | 19ef54418d301f91 | 1 |
| Helen Guo / SMB Deal Hunter | Absentee-Run Luxury Nail Salon | Arizona | $2,710,783 | $680,868 | undisclosed | nail salon | deal-newsletter-known-sender | 19ef59c77c64dd08 | 1 |
| Helen Guo / SMB Deal Hunter | Commercial Landscape Maintenance Company | Colorado | $1,438,776 | $527,943 | undisclosed | landscaping | deal-newsletter-known-sender | 19ef59c77c64dd08 | 2 |
| Helen Guo / SMB Deal Hunter | Construction Equipment Rental Company | Indiana | $1,205,647 | $418,402 | undisclosed | equipment rental | deal-newsletter-known-sender | 19ef59c77c64dd08 | 4 |
| Helen Guo / SMB Deal Hunter | Electric Motors and Power Transmission Distributor | Florida | $1,036,346 | $402,007 | undisclosed | industrial distribution / repair | deal-newsletter-known-sender | 19ef59c77c64dd08 | 5 |
| Brad Wayland / Quiet Light | RV Enthusiast Content Site | undisclosed | $144,245 | undisclosed | undisclosed | content site / RV | single-listing-blast | 19ef5ac7024e191c | 1 |
| Tory @ Flippa | 1.08M Subs History Channel | undisclosed | undisclosed | undisclosed | undisclosed | media / YouTube | deal-newsletter-known-sender | 19ef5d9121064459 | 1 |
| Tory @ Flippa | $1.3M Crypto Blog | undisclosed | undisclosed | undisclosed | undisclosed | crypto media | deal-newsletter-known-sender | 19ef5d9121064459 | 2 |
| Joe Margle / Benchmark International | Acquisition Opportunity: Multi-Location Health & Wellness Club - BN000060047 | Rocky Mountains, US | $8.4M | $2.5M | undisclosed | health and wellness club | single-listing-blast | 19efa3ecdb74321e | 1 |
| Everingham & Kerr | Manufacturer and Distributor of Licensed & Branded Toy Merchandise | undisclosed | undisclosed | undisclosed | undisclosed | toy merchandise | single-listing-blast | 19efa786d27b7dc9 | 1 |
| Elaine Eason / Quiet Light | SBA Pre-Qualified: 22-Year-Old Music Gear Brand / Significant FBA Upside | undisclosed | $2,757,258 | undisclosed | undisclosed | music gear ecommerce | single-listing-blast | 19efad24c6c6e73f | 1 |
| Helen Guo / SMB Deal Hunter | Semi-Absentee Apparel Decorating Business | Tennessee | $7,000,000 | $1,300,000 | undisclosed | apparel decorating | deal-newsletter-known-sender | 19efaf5a3843537b | 1 |
| Helen Guo / SMB Deal Hunter | Absentee-Run Hay Supply and Delivery Business | Illinois | $1,000,000 | $420,000 | undisclosed | hay supply and delivery | deal-newsletter-known-sender | 19efaf5a3843537b | 2 |
| Helen Guo / SMB Deal Hunter | Commercial Flooring and Concrete Coatings Company | California | $3,600,000 | $550,000 | undisclosed | flooring / coatings | deal-newsletter-known-sender | 19efaf5a3843537b | 3 |
| Helen Guo / SMB Deal Hunter | Heating, Cooling, and Plumbing Company | Iowa | $1,000,000 | $450,000 | undisclosed | HVAC / plumbing | deal-newsletter-known-sender | 19efaf5a3843537b | 4 |
| Helen Guo / SMB Deal Hunter | Tree Service Company | Texas | $850,000 | $460,000 | undisclosed | tree service | deal-newsletter-known-sender | 19efaf5a3843537b | 5 |
| Tory @ Flippa | $17M IT Firm | undisclosed | $17M | undisclosed | undisclosed | IT firm | deal-newsletter-known-sender | 19efb018881e4728 | 1 |
| Tory @ Flippa | 98% Margin Car Wrapping Brand | undisclosed | undisclosed | undisclosed | 98% | car wrapping / ecommerce | deal-newsletter-known-sender | 19efb018881e4728 | 2 |
| Everingham & Kerr | New Acquisition Opportunity - Provider of Renewable Solar Energy Solutions | undisclosed | undisclosed | undisclosed | undisclosed | solar | single-listing-blast | 19efb8c9b612f31d | 1 |
| Everingham & Kerr | Wireless Telecommunications Engineering Firm | undisclosed | undisclosed | undisclosed | undisclosed | telecommunications engineering | single-listing-blast | 19eff1d5745325c2 | 1 |
| Helen Guo / SMB Deal Hunter | Absentee-Run Commercial Cleaning Company | Ohio | $1,730,000 | $462,000 | undisclosed | commercial cleaning | deal-newsletter-known-sender | 19eff9ec60fd2d5f | 1 |
| Helen Guo / SMB Deal Hunter | Septic and Liquid Waste Management Company | Ohio | $1,765,600 | $505,195 | undisclosed | septic / liquid waste | deal-newsletter-known-sender | 19eff9ec60fd2d5f | 2 |
| Helen Guo / SMB Deal Hunter | Premier Insulation and Weatherization Contractor | Massachusetts | $3,618,503 | $419,008 | undisclosed | insulation / weatherization | deal-newsletter-known-sender | 19eff9ec60fd2d5f | 4 |
| Helen Guo / SMB Deal Hunter | High-End Custom Steel Railing Fabricator | Colorado | $1,815,813 | $411,050 | undisclosed | steel railing fabrication | deal-newsletter-known-sender | 19eff9ec60fd2d5f | 5 |
| Ian Drogin / Quiet Light | Amazon FBA Garden Business / Strong Gross Profit Margins / Multiple Expansion Opportunities | undisclosed | $780,513 | undisclosed | undisclosed | garden / Amazon FBA | single-listing-blast | 19efff9e5a7424f9 | 1 |
| Tory @ Flippa | 248K Subs Blanket Brand | undisclosed | undisclosed | undisclosed | undisclosed | ecommerce / media | deal-newsletter-known-sender | 19f002b33dd9e183 | 1 |
| Tory @ Flippa | $1.9M Dating SaaS | undisclosed | $1.9M | undisclosed | undisclosed | SaaS | deal-newsletter-known-sender | 19f002b33dd9e183 | 2 |
| Everingham & Kerr | New Acquisition Opportunity - Geotechnical Engineering Services Company | undisclosed | undisclosed | undisclosed | undisclosed | geotechnical engineering | single-listing-blast | 19f00b55a11762b4 | 1 |
| Samuel Curcio / Transworld | Transworld Business Listings report | New York / Northeast | undisclosed | undisclosed | undisclosed | mixed local businesses | multi-listing | 19f03478a77a58a1 | 1 |
| New Deal via Axial | VPN, Identity, Malware, & Antivirus Protection / Recurring Revenue | undisclosed | undisclosed | undisclosed | undisclosed | cybersecurity / recurring revenue | single-listing-blast | 19f04915cb7a1e7b | 1 |
| Everingham & Kerr | Provider of Renewable Solar Energy Solutions | undisclosed | undisclosed | undisclosed | undisclosed | solar | single-listing-blast | 19f04e2004de337e | 1 |
| New Deal via Axial | Highly Successful Full-Service Architectural Sign Company | undisclosed | undisclosed | undisclosed | undisclosed | sign company | single-listing-blast | 19f0527ed56ade0a | 1 |
| J.R. @ Flippa | $8.2M Peptide Brand | undisclosed | $8.2M | undisclosed | undisclosed | peptide ecommerce | deal-newsletter-known-sender | 19f054f0def06f8f | 1 |
| J.R. @ Flippa | 1.5M Subs Manufacturing Channel | undisclosed | undisclosed | undisclosed | undisclosed | manufacturing media | deal-newsletter-known-sender | 19f054f0def06f8f | 2 |
| J.R. @ Flippa | 30-Yr IT Firm | undisclosed | undisclosed | undisclosed | undisclosed | IT firm | deal-newsletter-known-sender | 19f054f0def06f8f | 3 |
| Everingham & Kerr | Specialty / Niche Monthly International Trade Publication | undisclosed | undisclosed | undisclosed | undisclosed | trade publication | single-listing-blast | 19f05a0138d3536a | 1 |
| Everingham & Kerr | Geotechnical Engineering Services Company | undisclosed | undisclosed | undisclosed | undisclosed | geotechnical engineering | single-listing-blast | 19f0a074c38b84d8 | 1 |
| Tory @ Flippa | $893K Video Hosting SaaS | undisclosed | $893K | undisclosed | undisclosed | SaaS / video hosting | deal-newsletter-known-sender | 19f0a765cbf16d5b | 1 |
| Tory @ Flippa | 89% Margin SEO Platform | undisclosed | undisclosed | undisclosed | 89% | SEO platform | deal-newsletter-known-sender | 19f0a765cbf16d5b | 2 |
| Tory @ Flippa | Recruitment Agency with a 10% repeat customer rate | undisclosed | undisclosed | undisclosed | undisclosed | recruitment agency | deal-newsletter-known-sender | 19f0a765cbf16d5b | 3 |
| Tory @ Flippa | 6-Yr Ecom Growth Agency | undisclosed | undisclosed | undisclosed | undisclosed | ecommerce growth agency | deal-newsletter-known-sender | 19f0fa0533217062 | 1 |
| Tory @ Flippa | $1.07M Accreditation Service | undisclosed | $1.07M | undisclosed | undisclosed | accreditation service | deal-newsletter-known-sender | 19f0fa0533217062 | 2 |
| Tory @ Flippa | Fragrance Brand with a 20% repeat purchase rate | undisclosed | undisclosed | undisclosed | undisclosed | fragrance ecommerce | deal-newsletter-known-sender | 19f0fa0533217062 | 3 |
| BizQuest | New York search agent: 24 new listings | New York | undisclosed | undisclosed | undisclosed | mixed local businesses | deal-newsletter-known-sender | 19f127085b9f12dd | 1 |
| Brad Wayland / Quiet Light | 7-Year-Old Shopify Business Selling Customizable Travel-Themed Jewelry / Fully Outsourced Team / Strong Margins | undisclosed | $10,331,910 | undisclosed | undisclosed | jewelry ecommerce | single-listing-blast | 19f13b77f0f6d10f | 1 |
| Drew Ermenc / Quiet Light | USA-Made Amazon FBA Aquarium Habitat Brand / 55% TTM Revenue Growth / 40K Units Sold & 1.5K Reviews / 1.9X | undisclosed | $554,710 | undisclosed | undisclosed | aquarium ecommerce | single-listing-blast | 19f14931fd3d0834 | 1 |
| Tory @ Flippa | 32-Yr Skincare Brand | undisclosed | undisclosed | undisclosed | undisclosed | skincare ecommerce | deal-newsletter-known-sender | 19f14bfc67d69fb1 | 1 |
| Tory @ Flippa | $2.9M Online Casino | undisclosed | $2.9M | undisclosed | undisclosed | online casino | deal-newsletter-known-sender | 19f14bfc67d69fb1 | 2 |
| Tory @ Flippa | 97% Margin Music Production Business | undisclosed | undisclosed | undisclosed | 97% | music production | deal-newsletter-known-sender | 19f14bfc67d69fb1 | 3 |
| Everingham & Kerr | New Acquisition Opportunity - Residential & Commercial Solar Energy Contractor | undisclosed | undisclosed | undisclosed | undisclosed | solar contractor | single-listing-blast | 19f1533bf50ea88a | 1 |

## 8. Auto-Drafts Created

None.
