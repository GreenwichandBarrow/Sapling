---
schema_version: 1.1.0
date: 2026-06-29
type: context
title: "Email Scan Results - 2026-06-29"
status: done
source: email-intelligence
tags: [date/2026-06-29, context, output/email-scan-results, source/email-intelligence, status/done, topic/email-intelligence]
---

# Email Scan Results - 2026-06-29

## 1. Actionable Items Created

None.

System status:
- No CIM, NDA, active-deal document, or bookkeeper Management Report / P&L trigger was detected in the compact context artifact.
- Granola returned no updated notes since 2026-06-28T00:00:00Z, so no `brain/calls/` files were created.
- 2026-06-29 is not the last calendar day of the month, so the monthly missing-report watchdog did not run.

## 2. Deal Flow Classified

Inbound scan summary from `[[context/email-intelligence-input-2026-06-29]]`:
- DIRECT: 8
- BLAST: 36
- NEWSLETTER: 11

Reviewed sources:
- 55 inbound or deal-label messages in the compact context artifact.
- 1 outbound message in the compact context artifact.
- 1 Gmail draft in the compact context artifact.

## 3. Draft Status

- Gmail drafts scanned: 1
- Sent: 0 surfaced in the live Gmail draft list.
- Unsent: 1
- Unsent older than 48 hours: 1

| draft_id | age | to | subject | thread_id | status |
|---|---:|---|---|---|---|
| r-2617485536768457504 | about 6.6 days | [[entities/andrew-saltoun|Andrew Saltoun]] | blank subject | 19ef0337e00067d8 | DRAFT |

Notes:
- The draft snippet begins "Hi Andrew, Hope Japan was wonderful..." and offers Thursday / Friday availability.
- `brain/context/session-decisions-2026-06-26.md` was not present, so no prior-workday sent/deleted decision suppressed this stale-draft flag.

## 4. Introductions Detected

None new.

Potential intro-adjacent personal threads from [[entities/albert-kim|Albert Kim]] and [[entities/alex-rejigg|Alex / Rejigg]] were present in metadata, but the compact artifact did not expose an explicit new-introduction body signal. No entity or inbox item was created from metadata alone.

## 5. Niche Signals

- Deal-flow inventory remains dominated by broker/platform digests: Flippa, Quiet Light, BizQuest, BizBuySell, SMB Deal Hunter, Everingham & Kerr, Axial, Transworld, and Prospect Geni.
- Local services appeared repeatedly: towing and repair, RV rental/service, pet retail, commercial cleaning, septic/liquid waste, water filtration, insulation/weatherization, steel railings, HVAC/plumbing, tree service, flooring/concrete coatings, music gear, garden products, and architectural signage.
- Digital and ecommerce inventory stayed high-volume but less thesis-aligned: SaaS, content sites, ecommerce brands, Amazon FBA, crypto/media properties, video hosting, SEO, accreditation, fragrance, peptides, and YouTube/media channels.
- [[entities/dealsx|DealsX]] / Prospect Geni produced three "Lead Interested" notifications in the compact window. These are cold-but-live re-engagement signals for the DealsX channel, not Kay-email nudge candidates.
- No StartVirtual monthly Management Report signal appeared, so the `budget-manager monthly` chain did not fire.

### Granola Action Items

None. Granola returned no updated notes in this run.

## 6. In-Person Meetings Today

None.

Calendar context did show one external Zoom meeting today: [[entities/megan-lawlor|Megan]] <> [[entities/kay-schneider|Kay]], 1:30pm to 2:00pm ET. It is not an in-person meeting.

## 7. Broker BLAST Listings (per-deal extraction)

| source | headline | geo | revenue | ebitda | margin | industry | flag_reason | gmail_msg_id | listing_ordinal |
|---|---|---|---|---|---|---|---|---|---:|
| BizQuest | Automotive Tow & Repair Business Operating 24/7 | Bronx, NY | asking price $4.1M | undisclosed | undisclosed | towing / auto repair | deal-newsletter-known-sender | 19f127085b9f12dd | 1 |
| BizQuest | RV and Camper Rental Business for Sale | New York | asking price $109K | undisclosed | undisclosed | RV rental | deal-newsletter-known-sender | 19f127085b9f12dd | 2 |
| BizQuest | Thriving Specialty Metals and On Demand Industrial Supply Business | Astoria, NY | asking price $539,999 | undisclosed | undisclosed | specialty metals / industrial supply | deal-newsletter-known-sender | 19f127085b9f12dd | 3 |
| Tory @ Flippa | 6-year-old ecommerce growth agency | undisclosed | undisclosed | undisclosed | undisclosed | ecommerce growth agency | deal-newsletter-known-sender | 19f0fa0533217062 | 1 |
| Tory @ Flippa | Accreditation training service | undisclosed | $1.07M annual revenue | undisclosed | undisclosed | training / accreditation | deal-newsletter-known-sender | 19f0fa0533217062 | 2 |
| Tory @ Flippa | Fragrance brand with 20% repeat purchase rate | undisclosed | undisclosed | undisclosed | undisclosed | ecommerce / fragrance | deal-newsletter-known-sender | 19f0fa0533217062 | 3 |
| Tory @ Flippa | Video file hosting SaaS | undisclosed | $893K annual revenue | undisclosed | 64% profit margin | SaaS / video hosting | deal-newsletter-known-sender | 19f0a765cbf16d5b | 1 |
| Tory @ Flippa | SEO fulfillment platform | undisclosed | undisclosed | undisclosed | 89% margin from subject | SEO / digital marketing | deal-newsletter-known-sender | 19f0a765cbf16d5b | 2 |
| Tory @ Flippa | Recruitment agency with 10% repeat customer rate | undisclosed | undisclosed | undisclosed | undisclosed | recruiting services | deal-newsletter-known-sender | 19f0a765cbf16d5b | 3 |
| J.R. @ Flippa | Single-brand RUO peptide ecommerce platform | undisclosed | $8.2M annual revenue | undisclosed | 55% profit margin | ecommerce / peptides | deal-newsletter-known-sender | 19f054f0def06f8f | 1 |
| J.R. @ Flippa | IT consulting firm | undisclosed | $17M annual revenue | undisclosed | 31% profit margin | IT consulting / cybersecurity / telecom | deal-newsletter-known-sender | 19f054f0def06f8f | 2 |
| J.R. @ Flippa | Manufacturing YouTube channel | undisclosed | undisclosed | undisclosed | undisclosed | media / manufacturing | deal-newsletter-known-sender | 19f054f0def06f8f | 3 |
| Samuel Curcio, Transworld Business Advisors NY | Beloved pet store turn-key opportunity | Dutchess County, NY | price $49K | $0 SDE | undisclosed | pet retail | multi-listing | 19f03478a77a58a1 | 1 |
| Samuel Curcio, Transworld Business Advisors NY | Profitable virtual corporate events and gifting business | United States | price $1.3M | $458,863 SDE | undisclosed | virtual events / gifting | multi-listing | 19f03478a77a58a1 | 2 |
| Samuel Curcio, Transworld Business Advisors NY | Queens neighborhood bar and grill | Queens County, NY | price $700K | $0 SDE | undisclosed | restaurant / bar | multi-listing | 19f03478a77a58a1 | 3 |
| Samuel Curcio, Transworld Business Advisors NY | High-end Midtown med skincare spa | New York County, NY | price $400K | $0 SDE | undisclosed | med spa / skincare | multi-listing | 19f03478a77a58a1 | 4 |
| Samuel Curcio, Transworld Business Advisors NY | Absentee-run recording studio established 20 years | Kings County, NY | price $325K | $134,988 SDE | undisclosed | recording studio | multi-listing | 19f03478a77a58a1 | 5 |
| Ian Drogin, Quiet Light | Amazon FBA Garden Business | undisclosed | $780,513 | $123,865 earnings | 74.5% gross margin | Amazon FBA / garden products | deal-newsletter-known-sender | 19efff9e5a7424f9 | 1 |
| Elaine Eason, Quiet Light | 22-year-old music gear brand | undisclosed | $2,757,258 | $790,269 earnings | undisclosed | ecommerce / music gear | deal-newsletter-known-sender | 19efad24c6c6e73f | 1 |
| Brad Wayland, Quiet Light | RV enthusiast content site | undisclosed | $144,245 | $137,057 earnings | undisclosed | content site / RV | deal-newsletter-known-sender | 19ef5ac7024e191c | 1 |
| Ian Drogin, Quiet Light | EU-based Amazon FBA gardening business | EU | $131,770 | $31,144 earnings | 84% gross margin | Amazon FBA / gardening | deal-newsletter-known-sender | 19ef4d05a193c937 | 1 |
| Brad Wayland, Quiet Light | Personal finance site for physicians | undisclosed | undisclosed | undisclosed | undisclosed | content site / personal finance | deal-newsletter-known-sender | 19eefaa97403ee54 | 1 |
| Helen Guo, SMB Deal Hunter | Absentee-run commercial cleaning company | OH | undisclosed | $462K EBITDA | undisclosed | commercial cleaning | deal-newsletter-known-sender | 19eff9ec60fd2d5f | 1 |
| Helen Guo, SMB Deal Hunter | Septic and liquid waste company | OH | undisclosed | $505K EBITDA | undisclosed | septic / liquid waste | deal-newsletter-known-sender | 19eff9ec60fd2d5f | 2 |
| Helen Guo, SMB Deal Hunter | Medical-grade water filtration manufacturer | undisclosed | undisclosed | $870K EBITDA | undisclosed | water filtration manufacturing | deal-newsletter-known-sender | 19eff9ec60fd2d5f | 3 |
| Helen Guo, SMB Deal Hunter | Insulation and weatherization contractor | MA | undisclosed | $419K EBITDA | undisclosed | insulation / weatherization | deal-newsletter-known-sender | 19eff9ec60fd2d5f | 4 |
| Helen Guo, SMB Deal Hunter | Custom steel railing fabricator | CO | undisclosed | $411K EBITDA | undisclosed | steel fabrication | deal-newsletter-known-sender | 19eff9ec60fd2d5f | 5 |
| Helen Guo, SMB Deal Hunter | Semi-absentee apparel decorating business | TN | undisclosed | $1.3M EBITDA | undisclosed | apparel decorating | deal-newsletter-known-sender | 19efaf5a3843537b | 1 |
| Helen Guo, SMB Deal Hunter | Absentee-run hay supply and delivery business | IL | undisclosed | $420K EBITDA | undisclosed | hay supply / delivery | deal-newsletter-known-sender | 19efaf5a3843537b | 2 |
| Helen Guo, SMB Deal Hunter | Commercial flooring and concrete coatings company | Los Angeles, CA | undisclosed | $550K EBITDA | undisclosed | flooring / concrete coatings | deal-newsletter-known-sender | 19efaf5a3843537b | 3 |
| Helen Guo, SMB Deal Hunter | Heating, cooling, and plumbing company | IA | undisclosed | $450K EBITDA | undisclosed | HVAC / plumbing | deal-newsletter-known-sender | 19efaf5a3843537b | 4 |
| Helen Guo, SMB Deal Hunter | Tree service company | Dallas, TX | undisclosed | $460K EBITDA | undisclosed | tree service | deal-newsletter-known-sender | 19efaf5a3843537b | 5 |
| Everingham & Kerr | Geotechnical engineering services company | undisclosed | undisclosed | undisclosed | undisclosed | engineering services | single-listing-blast | 19f0a074c38b84d8 | 1 |
| Everingham & Kerr | Specialty / niche monthly international trade publication | undisclosed | undisclosed | undisclosed | undisclosed | trade publication | single-listing-blast | 19f05a0138d3536a | 1 |
| Everingham & Kerr | Provider of renewable solar energy solutions | undisclosed | undisclosed | undisclosed | undisclosed | renewable solar energy | single-listing-blast | 19f04e2004de337e | 1 |
| Everingham & Kerr | Wireless telecommunications engineering firm | undisclosed | undisclosed | undisclosed | undisclosed | telecom engineering | single-listing-blast | 19eff1d5745325c2 | 1 |
| Everingham & Kerr | Manufacturer and distributor of licensed and branded toy merchandise | undisclosed | undisclosed | undisclosed | undisclosed | toy manufacturing / distribution | single-listing-blast | 19efa786d27b7dc9 | 1 |
| Benchmark International | Multi-location health and wellness club | undisclosed | undisclosed | undisclosed | undisclosed | health and wellness club | single-listing-blast | 19efa3ecdb74321e | 1 |
| Axial | Full-service architectural sign company | undisclosed | undisclosed | undisclosed | undisclosed | signage / architectural signs | single-listing-blast | 19f0527ed56ade0a | 1 |
| Axial | VPN, identity, malware, and antivirus protection | undisclosed | undisclosed | undisclosed | undisclosed | cybersecurity / recurring revenue | single-listing-blast | 19f04915cb7a1e7b | 1 |
| BizBuySell | June top 7 listings digest | undisclosed | undisclosed | undisclosed | undisclosed | mixed business-for-sale digest | deal-newsletter-known-sender | 19ef05df8c872613 | 1 |

## 8. Auto-Drafts Created

None.
