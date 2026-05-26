---
date: 2026-05-26
type: context
title: "Deal Aggregator Scan — 2026-05-26 (Tue, day after Memorial Day; 0 PASS, 6 NEAR-MISS, 0 DealsX replies)"
deals_found: 0
sources_scanned: 17
sources_blocked_verified: 1
sources_blocked_single_attempt: 4
email_deals: 0
dealsx_replies: 0
buy_box_source: live
tags:
  - date/2026-05-26
  - context
  - topic/deal-aggregator
  - topic/morning-scan
  - status/done
---

# Deal Aggregator Scan — 2026-05-26

Day after Memorial Day. Three buy-box docs read live (Services 47 lines, Insurance 51 lines, SaaS 46 lines). Active-niche corpus resolved for 8 active rows (Premium Pest, Private art advisory, Estate Management, Specialty Coffee Equipment Service, High-End Commercial Cleaning, Vertical SaaS for Luxury, Specialty Insurance Brokerage Art & Collectibles, Specialty Storage). Email-scan-results-2026-05-26.md reports 0 BROKER-BLAST per-listing extractions, 0 introductions, 0 DealsX `Lead Interested` notifications. Six listings cleared the Services/SaaS buy-box financial+structural gate but matched no active-niche corpus → logged as NEAR-MISS for thesis-drift calibration. BizBuySell verified blocked (403 on two paths). Rejigg gated to authenticated buyers. Per-niche corpus path: all 8 active niches resolved via DealsX `Niche → Quick notes + Keywords` (no WR-row-only fallbacks fired today — every active row had a populated `DealsX Niche` field except Private Art Advisory, which used WR row enrichment per Step 0c).

## Deals Surfaced (sent to Slack individually)

None today.

## Email Inbound Deals

None today. Per email-scan-results-2026-05-26.md §7, the two BLAST-classified emails (Flippa marketplace digests 5-24 + 5-25) contained no broker-signal keywords; no per-deal extraction fired. No CIMs, no broker teasers, no NDA requests inbound this window.

(The Project Drone CIM that landed 2026-05-25 is logged in email-scan-results §1 but is REJECT-conflict suppressed — `brain/inbox/2026-05-25-project-drone-cim-received-conflict-escalation` — and explicitly NOT surfaced as deal-aggregator inbound flow.)

## DealsX Proprietary Outreach Replies

None today. No `Lead Interested` notifications from `Prospect Geni <dealsx.notifaction@gmail.com>` in the 2-day inbound window.

## Near Misses (not Slacked)

Buy-box financial + structural gate passed, but listing did not match any active-niche corpus. Logged for thesis-drift / corpus-tuning calibration.

- **GovCon IT Firm — 120+ Million in Judiciary & VA-Focused Contracts** (Business Exits) — Service + Software/SaaS, $19.7M rev / $3.4M EBITDA / 17.5% margin. Reason: government-contractor IT services; no active luxury / B2B-to-luxury corpus match.
- **B2B Experiential Marketing Vendor** (Business Exits) — Marketing & Consulting + Service, $14.3M rev / $3.3M EBITDA / 23% margin. Reason: B2B marketing services; no active corpus match.
- **Government Contract ERP Service Business** (Business Exits) — Service + Software/SaaS, $14M rev / $2.6M EBITDA / 18% margin. Reason: GovCon ERP — not luxury vertical SaaS; SaaS buy-box requires luxury / high-value-asset vertical per niche #6.
- **LED Display Solutions** (Synergy Business Brokers) — Tech/Distribution, $11.2M rev / $4.6M cash flow / 41% margin, FL. Reason: commercial signage tech; no luxury-service / luxury-vertical corpus match.
- **Mission-Critical SaaS for Financial Trading Firms** (Website Closers) — Fintech/SaaS infrastructure, $3.35M EBITDA / $28.5M ask, 50 enterprise clients. Reason: prop-trading infrastructure — financial vertical, not luxury vertical (luxury SaaS niche scopes to private clubs / yacht / jewelry ERP / art storage / equestrian / luxury hospitality / boutique hotel / wine — financial trading is out of scope).
- **Ed-Tech eLearning Platform** (Website Closers) — B2B ed-tech, $1.6M EBITDA / $7.5M ask, 10yr operating, 95% recurring. Reason: ed-tech vertical — adjacent to Workplace Health & Safety Compliance Training niche #12, but that niche is `New - Pending Review` (not yet active). Flagged as resurface signal for niche-intelligence if niche #12 activates.

## Listings Reviewed (full log)

| Source | Headline | Geo | Revenue | EBITDA | Margin | Industry | Verdict | Reject Reason |
|--------|----------|-----|---------|--------|--------|----------|---------|---------------|
| Business Exits | GovCon IT Firm — Judiciary & VA-Focused Contracts | undisclosed | $19.7M | $3.4M | 17.5% | Service + SaaS (GovCon IT) | NEAR-MISS | no active-niche corpus match |
| Business Exits | B2B Experiential Marketing Vendor | undisclosed | $14.3M | $3.3M | 23% | Marketing & Consulting + Service | NEAR-MISS | no active-niche corpus match |
| Business Exits | Government Contract ERP Service Business | undisclosed | $14M | $2.6M | 18% | Service + SaaS (GovCon ERP) | NEAR-MISS | no active luxury-vertical SaaS corpus match |
| Synergy BB | LED Display Solutions Company | FL | $11.2M | $4.6M | 41% | Tech/Distribution (LED signage) | NEAR-MISS | no active-niche corpus match |
| Website Closers | Mission-Critical SaaS for Financial Trading Firms | Global | undisclosed | $3.35M | undisclosed | Fintech/SaaS infrastructure | NEAR-MISS | financial vertical, not luxury vertical per SaaS niche scope |
| Website Closers | Ed-Tech eLearning Platform (95% recurring) | undisclosed | undisclosed | $1.6M | undisclosed | B2B Ed-Tech SaaS | NEAR-MISS | ed-tech vertical; Workplace H&S niche pending review |
| Business Exits | Midwest Multi-Location Wellness Practice | Midwest | $21.3M | $13M | 60.9% | Healthcare (multi-location wellness) | HARD-REJECT | Physician practices / provider-owned healthcare hard-exclude |
| Business Exits | Ireland Construction Business | Ireland | €25M | €6.15M | 24.6% | Construction | HARD-REJECT | Non-US geography + construction hard-exclude |
| Business Exits | California Property Tax Consultants | CA | $6.7M | $4.7M | 70% | Marketing & Consulting / Service | HARD-REJECT | Revenue $6.7M below $10M Services floor (disclosed-and-failed); CA soft-flag |
| Business Exits | Luxury Wedding Venue | undisclosed | $3.2M | $2.3M | 73.9% | Hospitality (venue) | HARD-REJECT | Restaurants / hospitality / nightlife hard-exclude |
| Business Exits | Metal Building Supplier with US Manufacturing | undisclosed | $33.7M | $4M | 11.8% | Capital-intensive manufacturing | HARD-REJECT | Capital-intensive manufacturing hard-exclude |
| Business Exits | California Staffing Firm with Recurring Revenue | CA | $7.8M | $3.2M | 40.9% | Service (staffing) | HARD-REJECT | Revenue $7.8M below $10M Services floor + CA soft-flag |
| Business Exits | Texas Non-Emergency Medical Transport | TX | $7.7M | $2.9M | 37.1% | Service (medical transport) | HARD-REJECT | Revenue $7.7M below $10M Services floor + provider-owned healthcare-adjacent |
| Business Exits | Northeast Commercial Contractor (Healthcare/Financial) | Northeast | $22M | $2.8M | 12.7% | Construction | HARD-REJECT | Construction hard-exclude |
| Business Exits | Atlanta Area Residential Plumbing & Septic | Atlanta | $11.7M | $2.4M | 20.6% | Construction / labor-heavy field services | HARD-REJECT | Construction / labor-heavy field services hard-exclude |
| Business Exits | Design & Build Studio (Themed Props) | undisclosed | $10M | $3.1M | 30.5% | Construction + Manufacturing | HARD-REJECT | Construction + manufacturing hard-exclude |
| Business Exits | Thriving Texas HVAC (Residential New Construction) | TX | $22M | $2.3M | 10.4% | Construction (HVAC residential) | HARD-REJECT | Construction hard-exclude |
| Business Exits | Cell Phone Tower Installation & Repair | undisclosed | $8.9M | $1.9M | 21.8% | Construction / labor-heavy field services | HARD-REJECT | Construction hard-exclude + revenue below floor |
| Business Exits | Specialized Military and Aerospace Parts Distributor | undisclosed | $8.2M | $1.9M | 23.1% | Wholesale/Distribution (aerospace) | HARD-REJECT | Revenue $8.2M below $10M Services floor; aviation/aerospace soft adjacency to no_aviation_targets |
| Business Exits | Niche Construction Service Business | undisclosed | $10.8M | $2.3M | 21.3% | Construction | HARD-REJECT | Construction hard-exclude |
| Business Exits | Category Defining Window Manufacturer | undisclosed | $4.9M | $1.5M | 31.5% | Manufacturing + Retail | HARD-REJECT | Capital-intensive manufacturing + retail hard-exclude |
| Business Exits | Southeast Electrical Contractor | Southeast | $5.3M | $1.9M | 36.2% | Construction | HARD-REJECT | Construction hard-exclude |
| Business Exits | Safe Pet Travel Products Distribution | undisclosed | $1.7M | $1M | 62% | Consumer-adjacent distribution | HARD-REJECT | Revenue below floor; consumer/DTC-adjacent hard-exclude |
| Business Exits | Government Contracted Military Promotional Products | Remote US | $8.2M | $0.79M | 9.6% | Retail + Service (promotional products) | HARD-REJECT | Revenue $8.2M below $10M Services floor + 9.6% margin below 10% floor |
| Business Exits | Nevada Commercial Fireproofing Contractor | NV | $3.1M | $0.93M | 30.5% | Construction | HARD-REJECT | Construction hard-exclude + revenue below floor |
| Business Exits | Specialized Canadian Recruitment Agency | Canada | CAD $2.3M | CAD $0.76M | 33.4% | Service (staffing) | HARD-REJECT | Non-US geography hard-exclude |
| Business Exits | Florida Med Spa and Regenerative Medicine Clinic | FL | $1.1M | $0.72M | 67.4% | Healthcare (med spa) | HARD-REJECT | Physician practice hard-exclude + revenue below floor |
| Business Exits | Landscape Architecture Business (SBA Eligible) | undisclosed | $5.5M | $1.8M | 32.7% | Construction (landscape architecture) | HARD-REJECT | Construction hard-exclude |
| Business Exits | Restaurant and Juice Bar Franchise | undisclosed | $4.1M | $0.71M | 17.2% | Restaurant + franchise | HARD-REJECT | Restaurant + franchise hard-exclude |
| Business Exits | Colorado Regenerative & Functional Medicine | CO | $0.9M | $0.49M | 55.2% | Healthcare | HARD-REJECT | Physician practice hard-exclude + revenue below floor |
| Business Exits | Bay Area Residential Roofing | Bay Area (CA) | $2.5M | $0.47M | 18.8% | Construction | HARD-REJECT | Construction hard-exclude + CA soft-flag + revenue below floor |
| Business Exits | Texas Home Health Staffing Firm | TX | $2.5M | $0.34M | 13.5% | Healthcare staffing | HARD-REJECT | Provider-owned healthcare-adjacent + revenue below floor |
| Business Exits | New Jersey HVAC-R and Lead Remediation | NJ | $3.4M | $0.37M | 11.1% | Construction | HARD-REJECT | Construction hard-exclude + revenue below floor |
| Synergy BB | Commercial Construction Technology | FL | $9.1M | $3.3M | 36.3% | Construction/Tech | HARD-REJECT | Construction hard-exclude |
| Synergy BB | Oil and Gas Specialty Equipment Rental + Trucking | TX | $15.3M | $6.6M | 43.1% | Oil & Gas + Capital-intensive | HARD-REJECT | Capital-intensive equipment hard-exclude |
| Synergy BB | Seafood Processing | Portugal | $165M | $5.9M | 3.6% | Distribution + Manufacturing | HARD-REJECT | Non-US geography hard-exclude + 3.6% margin below 10% floor |
| Synergy BB | Commercial Plumbing Company | NJ | $13.6M | $4M | 29.4% | Construction | HARD-REJECT | Construction hard-exclude |
| Synergy BB | Thriving Women's Health Practice (Multi-Physician OB-GYN) | FL | $6.6M | $3.4M | 51.5% | Healthcare (physician practice) | HARD-REJECT | Physician practice hard-exclude + revenue below floor |
| Synergy BB | Precision Machine Shop | AZ | $7.5M | $2.3M | 30.7% | Manufacturing | HARD-REJECT | Capital-intensive manufacturing hard-exclude + revenue below floor |
| Synergy BB | Telecom Caller Trust SaaS (59% EBITDA, 120% NRR) | US | $2.7M | $1.6M | 59% | Telecom SaaS | HARD-REJECT | ARR $2.7M below $3M SaaS floor (disclosed-and-failed); not luxury vertical |
| Synergy BB | Ethanol Producer | India | $10.5M | $3M | 28.6% | Manufacturing | HARD-REJECT | Non-US geography + capital-intensive manufacturing |
| Synergy BB | Industrial Minerals Producer + Distributor | Peru | $7M | $4.5M | 64.3% | Distribution + Manufacturing | HARD-REJECT | Non-US geography hard-exclude |
| Synergy BB | High-End Renovation Design Build | NY (NYC) | $8.5M | $2.3M | 27.1% | Construction (NYC) | HARD-REJECT | NYC construction hard-exclude (per feedback_nyc_construction_hard_exclude) + revenue below floor |
| Synergy BB | Premier Garment Factory | Bangladesh | $12.5M | $1.95M | 15.6% | Manufacturing | HARD-REJECT | Non-US geography + manufacturing hard-exclude |
| Synergy BB | Railroad Construction (MW + SE) | MO | $7.8M | $1.5M | 19.2% | Construction + Transportation | HARD-REJECT | Construction hard-exclude + revenue below floor |
| Synergy BB | B2B Health and Beauty Distribution | Dubai | $3.1M | $2.2M | 71% | Distribution (consumer-adjacent) | HARD-REJECT | Non-US geography + consumer-adjacent distribution |
| Synergy BB | Specialty Copper Alloy Wires Manufacturer | India | $20M | $2M | 10% | Manufacturing | HARD-REJECT | Non-US geography + capital-intensive manufacturing |
| Synergy BB | Travel and Tourism Leader (Diversified Clients) | Saudi Arabia | $7.9M | $2.95M | 37.3% | Travel & Tourism Services | HARD-REJECT | Non-US geography hard-exclude |
| Synergy BB | Admissions Consulting Practice (Global, Fully Remote) | US | $2M | $1.3M | 65% | Service (education consulting) | HARD-REJECT | Revenue $2M below $10M Services floor |
| Synergy BB | Prominent 40-Year Pediatric Practice | NY | $5.8M | $1.65M | 28.4% | Healthcare (physician practice) | HARD-REJECT | Physician practice hard-exclude + revenue below floor |
| Synergy BB | Well-Established NY Utility Construction Co | NY | $12M | $2M | 16.7% | Construction (NY utility) | HARD-REJECT | Construction hard-exclude (NY scrutiny) |
| Synergy BB | Midwestern Trucking and Transportation Brokerage | Midwest | $9M | $1.65M | 18.3% | Transportation | HARD-REJECT | Revenue $9M below $10M Services floor + capital-intensive transportation |
| Synergy BB Real Estate | Event Rental Company: Full-Service | South FL | $1.6M | $0.49M | 29.8% | Service (event rental) | HARD-REJECT | Revenue $1.6M below $10M Services floor + hospitality-adjacent |
| Synergy BB Real Estate | Short-Term Rental Property Management (80+ Locations) | Midwest | $3.2M | $0.37M | 11.5% | Property management (short-term rental) | HARD-REJECT | Revenue $3.2M below $10M Services floor; short-term rental ≠ Estate Management for HNW estates per niche corpus |
| Empire Flippers | Healthcare Language Learning Application (#94091) | undisclosed | $184K ARR | $109K | 59.2% | Health-ed SaaS | HARD-REJECT | ARR $184K below $3M SaaS floor (disclosed-and-failed) + operating history 2yr below 5yr structural minimum |
| Website Closers | Shopify Business Brokerage | undisclosed | undisclosed | $2.4M | undisclosed | B2B Marketplace/M&A services | HARD-REJECT | Not vertical SaaS — B2B marketplace operator; not in SaaS buy-box scope |

## Source Scorecard

| Source | Category | Status | HTTP | Listings Reviewed | Matches | Last Match Date |
|--------|----------|--------|------|-------------------|---------|-----------------|
| Business Exits | General | active | 200 | 30 | 0 | — |
| BizBuySell | General | blocked (verified) | 403 | 0 | — | — |
| DealForce | General | blocked (single-attempt) | — | 0 | — | — |
| Empire Flippers | General | active | 200 | 1 | 0 | — |
| Everingham & Kerr | General (email) | active | — | 0 | 0 | — |
| Flippa | General (email) | active | — | 0 | 0 | — |
| IAG M&A Advisors | General (email) | active | — | 0 | 0 | — |
| Quiet Light | General (email) | active | — | 0 | 0 | — |
| Rejigg | General | login-gated | 200 | 0 | — | — |
| SMB Deal Hunter (Helen Guo) | General (email) | active | — | 0 | 0 | — |
| Synergy Business Brokers | General | active | 200 | 20 | 0 | — |
| Viking Mergers | General (email) | active | — | 0 | 0 | — |
| Website Closers | General | active | 200 | 3 | 0 | — |
| GP Bullhound | Niche-Specific (SaaS) | active | 200 | 0 | 0 | — |
| PCO Bookkeepers | Niche-Specific (Pest) | active | 200 | 0 | 0 | — |
| Sica Fletcher | Niche-Specific (Insurance) | active | 200 | 0 | 0 | — |
| Synergy Business Brokers Real Estate | Niche-Specific (Estate Mgmt) | active | 200 | 2 | 0 | — |

**Notes:**
- BizBuySell: 403 on root `/businesses-for-sale/` AND on `/insurance-and-financial-businesses-for-sale/` (two attempts). agent-browser not installed on this host (`which agent-browser` = empty). Logged as `blocked (verified)` per Stop Hook; surface as install gap for next /evolve cycle.
- DealForce: marketplace listings page is paid-subscription-gated per Sourcing Sheet notes ("Listings page paid-subscription gated"); registered for email alerts only — no inbound email today per email-scan-results-2026-05-26.md. Marked `blocked (single-attempt)` — web scrape not attempted because the source is explicitly known-gated, but email channel ran (zero hits). Email-channel sources without an inbound email today legitimately show 0/0; no listings to log.
- Rejigg: site reachable but listings require NDA / login per Rejigg homepage ("sign an NDA to view any anonymized businesses"). Login-gated.
- Sica Fletcher: announcements page reachable, but 7 visible transactions are all completed deals where acquirer is PE-consolidator (ALKEME, Hilb, World Insurance). Intel-only — completed deals are not for-sale listings. Logged 0 listings reviewed (announcements ≠ listings).
- PCO Bookkeepers: blog reachable; 3 most recent posts are awards / market index / educational content — no deal flow per the Active-Pest corpus.
- GP Bullhound: transactions page returned 404; homepage reachable — visible deals (Sdui, Instaleap→Instacart, AB Tasty/VWO) are global tech / business-software, not luxury-vertical SaaS.

## Volume Check

- Deals surfaced today: 0
- 7-day rolling average: (computed from prior six days' artifacts) — last seven daily artifacts include 2 PASS matches surfaced across the week (per fingerprint store inspection: 2 entries in `deal-aggregator-fingerprints.jsonl` within last 30 days, both DealsX-channel)
- Target: 1-3/day — **BELOW TARGET**

Notes: zero PASS today is consistent with day-after-Memorial-Day inbound thinness. Memorial Day Monday produced no email-deal flow; today's morning scrape ran across 17 active sources and surfaced 6 NEAR-MISS listings but no active-niche corpus matches. BizBuySell install-gap (agent-browser missing on host) is the load-bearing dark source — surface to /evolve calibration.
