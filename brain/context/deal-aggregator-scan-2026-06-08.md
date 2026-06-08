---
date: 2026-06-08
deals_found: 0
sources_scanned: 17
sources_blocked_verified: 4
sources_blocked_single_attempt: 0
email_deals: 0
dealsx_replies: 0
broker_opportunistic: 5
email_scan_status: missing
---
# Deal Aggregator Scan — 2026-06-08

Morning run (full). Buy-box docs read live from Drive. Active niches loaded from WEEKLY REVIEW. DEALSX keyword corpus loaded and resolved for all 8 active niches. Email-scan-results artifact was missing for 2026-06-08 after the bounded retry, so email-routed sources were scorecarded but no email listings were parsed. Browser fallback was unavailable on JS-shell / 403 sources.

**Niche corpus paths used:**
1. Premium Pest Management → DealsX keywords ("Specialty Pest & Environmental Management Services")
2. Private art advisory firms → WR row enrichment (DealsX Niche blank): art advisory, art advisor, collection strategy, art consulting, private art advisor
3. Estate Management Companies → DealsX keywords ("Estate Management Companies")
4. Specialty Coffee Equipment Service → DealsX keywords ("Specialty Commercial Equipment Services")
5. High-End Commercial Cleaning → DealsX keywords ("High-End Commercial Cleaning")
6. Vertical SaaS for Luxury & High-Value Asset Service Industries → DealsX keywords
7. Specialty Insurance Brokerage (Art & Collectibles) → DealsX keywords ("Specialty Insurance Brokerage")
8. Storage & Related Services for High Value Assets → DealsX keywords ("Specialty Storage & Handling for High-Value Collections")

---

## Deals Surfaced (sent to Slack individually)

None today. No new PASS match cleared fingerprint dedup, so nothing was Slack-posted.

## Email Inbound Deals

None today. `brain/context/email-scan-results-2026-06-08.md` was missing after the bounded retry loop, so email-only broker sources could not be parsed.

## DealsX Proprietary Outreach Replies

None today. Email-scan-results was missing, so no DealsX lead notifications were available to parse.

## Broker Opportunistic Review

Financially plausible broker/platform listings that do not match an active thesis corpus. Artifact-only by default; use this lane for CIO review and corpus/source tuning.
1. **GovCon IT Firm — 120+ Million in Judiciary & VA-Focused Contracts** (Business Exits) — $19.7M revenue, $3.4M EBITDA, 17.5% margin. Clears Services financial gate; no active-niche corpus match.
2. **B2B Experiential Marketing Vendor** (Business Exits) — $14.3M revenue, $3.3M EBITDA, 23.1% margin. Clears Services financial gate; no active-niche corpus match.
3. **Government Contract ERP Service Business** (Business Exits) — $14.0M revenue, $2.6M EBITDA, 18.3% margin. Clears Services financial gate; no active-niche corpus match.
4. **Multi-Service Oilfield Infrastructure & Automation Company** (Business Exits) — $12.9M revenue, $2.0M EBITDA, 15.3% margin. Clears financial gate; no active-niche corpus match; industrial field-services review item.
5. **Growing LED Display Solutions Company** (Synergy Business Brokers) — FL, $11.2M revenue, $4.6M EBITDA, 41.4% margin. Clears Services financial gate; no active-niche corpus match.

## Near Misses (not Slacked)

- Email leg unavailable — `brain/context/email-scan-results-2026-06-08.md` was missing after the bounded retry.
- Browser fallback unavailable — `agent-browser` is not installed, so JS-shell / 403 sources were logged as blocked instead of being silently skipped.

## Listings Reviewed (full log)

| Source | Headline | Geo | Revenue | EBITDA | Margin | Industry | Verdict | Reject Reason |
|--------|----------|-----|---------|--------|--------|----------|---------|---------------|
| Website Closers | Lead Generation Marketplace for Local Service Pros | undisclosed | $9,583,684 | $2,366,900 cash flow | undisclosed | Lead generation marketplace / local services SaaS | PASS | |
| Business Exits | GovCon IT Firm – 120+ Million in Judiciary & VA-Focused Contracts | undisclosed | $19,700,595 | $3,446,340 | 17.5% | B2B IT Services / GovCon | BROKER-OPPORTUNISTIC | Financially plausible broker listing; off-thesis but recurring contract revenue |
| Business Exits | B2B Experiential Marketing Vendor | undisclosed | $14,277,492 | $3,297,944 | 23.1% | B2B Marketing Services | BROKER-OPPORTUNISTIC | Financially plausible broker listing; no active niche corpus match |
| Business Exits | Government Contract ERP Service Business | undisclosed | $14,046,972 | $2,572,171 | 18.3% | B2B ERP / GovCon | BROKER-OPPORTUNISTIC | Financially plausible broker listing; no active niche corpus match |
| Business Exits | Multi-Service Oilfield Infrastructure & Automation Company | undisclosed | $12,897,728 | $1,967,502 | 15.3% | B2B Oilfield Services | BROKER-OPPORTUNISTIC | Financially plausible broker listing; strong recurring customer relationships; off-thesis |
| Synergy Business Brokers | Growing LED Display Solutions Company | Florida | $11,193,625 | $4,634,729 | 41.4% | B2B Technology / Distribution | BROKER-OPPORTUNISTIC | Financially plausible broker listing; no active niche corpus match |
| Business Exits | Midwest-Based Multi-Location Wellness Practice with Exceptional Margins | Midwest | $21,313,476 | $12,974,692 | 60.9% | Healthcare | HARD-REJECT | Physician/provider-owned healthcare hard-exclude; EBITDA above Services ceiling |
| Business Exits | Ireland Construction Business | Ireland | €25,000,000 | €6,150,000 | 24.6% | Construction | HARD-REJECT | Non-US; construction hard-exclude |
| Business Exits | California Property Tax Consultants | California | $6,679,566 | $4,676,542 | 70.0% | Consulting | HARD-REJECT | Revenue below $10M Services floor; California soft-flag |
| Business Exits | Luxury Wedding Venue | undisclosed | $3,175,872 | $2,347,000 | 73.9% | Hospitality / Events | HARD-REJECT | Revenue below floor; hospitality hard-exclude |
| Business Exits | Metal Building Supplier with US Manufacturing | undisclosed | $33,694,403 | $3,973,506 | 11.8% | Construction / Manufacturing | HARD-REJECT | Construction and capital-intensive manufacturing hard-excludes |
| Business Exits | California Staffing Firm with Recurring Revenue | California | $7,824,773 | $3,196,529 | 40.9% | Staffing Services | HARD-REJECT | Revenue below $10M floor; California soft-flag |
| Business Exits | Texas Based Non-Emergency Medical Transport | Texas | $7,743,083 | $2,874,318 | 37.1% | Healthcare / Transport | HARD-REJECT | Revenue below floor; healthcare-adjacent |
| Business Exits | Growing Atlanta Area Residential Plumbing & Septic Company | Georgia | $11,706,308 | $2,406,695 | 20.6% | Field Services / Plumbing | HARD-REJECT | Labor-heavy field services / construction hard-exclude |
| Business Exits | Northeast Commercial Contractor Serving Healthcare and Financial Clients | Northeast | $21,959,113 | $2,784,735 | 12.7% | Construction | HARD-REJECT | Construction hard-exclude |
| Business Exits | Design & Build Studio for Themed Props, Structures, & Interactive Experiences | undisclosed | $10,022,434 | $3,057,730 | 30.5% | Construction / Manufacturing | HARD-REJECT | Construction and manufacturing hard-excludes |
| Business Exits | Thriving Texas HVAC Company Specializing in Residential New Construction | Texas | $21,986,180 | $2,284,289 | 10.4% | HVAC / Field Services | HARD-REJECT | Labor-heavy field services / construction hard-exclude |
| Business Exits | Cell Phone Tower Installation & Repair | undisclosed | $8,927,055 | $1,946,908 | 21.8% | Telecom Field Services | HARD-REJECT | Revenue below floor; field-services construction exposure |
| Business Exits | Niche Construction Service Business | undisclosed | $10,800,000 | $2,300,000 | 21.3% | Construction | HARD-REJECT | Construction hard-exclude |
| Business Exits | Specialized Military and Aerospace Parts Distributor | undisclosed | $8,231,459 | $1,903,206 | 23.1% | Wholesale / Distribution | HARD-REJECT | Revenue below floor |
| Business Exits | Category Defining Window Manufacturer | undisclosed | $4,895,568 | $1,539,977 | 31.5% | Manufacturing / Retail | HARD-REJECT | Revenue below floor; manufacturing hard-exclude |
| Business Exits | Southeast Electrical Contractor | Southeast | $5,280,585 | $1,910,497 | 36.2% | Construction | HARD-REJECT | Revenue below floor; construction hard-exclude |
| Business Exits | Safe Pet Travel Products Distribution Company | undisclosed | $1,666,584 | $1,032,490 | 61.9% | B2C Distribution | HARD-REJECT | Revenue below floor; consumer retail/DTC hard-exclude |
| Business Exits | Nevada Commercial Fireproofing Contractor | Nevada | $3,057,340 | $931,994 | 30.5% | Construction | HARD-REJECT | Revenue and EBITDA below floors; construction hard-exclude |
| Business Exits | Specialized Canadian Recruitment Agency | Canada | $2,283,323 CAD | $763,741 CAD | 33.5% | Staffing | HARD-REJECT | Non-US; revenue below floor |
| Business Exits | Florida Med Spa and Regenerative Medicine Clinic | Florida | $1,074,754 | $723,910 | 67.4% | Healthcare | HARD-REJECT | Revenue below floor; physician/provider healthcare hard-exclude |
| Business Exits | Landscape Architecture Business – SBA Eligible | undisclosed | $5,500,000 | $1,800,000 | 32.7% | Construction-adjacent | HARD-REJECT | Revenue below floor; construction-adjacent |
| Business Exits | Colorado Based Regenerative & Functional Medicine Practice | Colorado | $894,910 | $494,099 | 55.2% | Healthcare | HARD-REJECT | Revenue below floor; physician/provider healthcare hard-exclude |
| Business Exits | Restaurant and Juice Bar Franchise | undisclosed | $4,144,975 | $714,160 | 17.2% | Restaurant / Franchise | HARD-REJECT | Franchise and restaurant hard-excludes |
| Business Exits | Bay Area Residential Roofing Company | California | $2,500,254 | $469,568 | 18.8% | Construction | HARD-REJECT | Revenue below floor; construction hard-exclude; California soft-flag |
| Business Exits | Automotive Quality Inspection & Workforce Solutions Provider | undisclosed | $4,734,092 | $387,292 | 8.2% | B2B Services | HARD-REJECT | Revenue, EBITDA, and margin below floors |
| Business Exits | Texas Home Health Staffing Firm | Texas | $2,494,220 | $337,193 | 13.5% | Healthcare Staffing | HARD-REJECT | Revenue and EBITDA below floors |
| Empire Flippers | #95105 — Beauty, Supplements eCommerce | undisclosed | $33.2M annualized | $1.4M annualized | 4.3% | eCommerce / DTC | HARD-REJECT | Consumer retail/DTC hard-exclude; under 5-year operating history |
| Empire Flippers | #93773 — Entertainment / Electronics / Technology Amazon FBA | undisclosed | $2.7M annualized | $0.8M annualized | 29.0% | Amazon FBA / Consumer | HARD-REJECT | B2C consumer retail hard-exclude; below floors |
| Empire Flippers | #94522 — Business / Electronics / Technology FBA + eCommerce + SaaS | undisclosed | $1.1M annualized | $0.2M annualized | 16.3% | eCommerce / SaaS hybrid | HARD-REJECT | Below SaaS ARR floor; eCommerce/DTC exposure |
| Empire Flippers | #93686 — Automotive / Sports / Hobbies eCommerce | New Jersey | $0.6M annualized | $0.2M annualized | 31.3% | eCommerce / DTC | HARD-REJECT | B2C consumer retail; below floors |
| Empire Flippers | #94607 — Business / Information Display Ads | undisclosed | $0.2M annualized | $0.2M annualized | 85.4% | Digital Media | HARD-REJECT | B2C content; below floors |
| Empire Flippers | #94707 — Home / Art / Design Affiliate | undisclosed | $0.1M annualized | $0.1M annualized | 96.2% | Affiliate / Display Ads | HARD-REJECT | B2C content; below floors |
| Empire Flippers | #94911 — Hobbies / Art Digital Product | undisclosed | $0.3M annualized | $0.1M annualized | 24.0% | Digital Product / DTC | HARD-REJECT | Consumer digital product; below floors |
| Empire Flippers | #90998 — Children / Books Amazon KDP | undisclosed | $0.1M annualized | $0.05M annualized | 41.0% | Amazon KDP / Consumer | HARD-REJECT | Consumer publishing; below floors |
| Empire Flippers | #94170 — Health & Fitness / Home / Medical Amazon FBA | undisclosed | $17.6M annualized | $4.6M annualized | 26.2% | Amazon FBA / Consumer | HARD-REJECT | Consumer retail/DTC hard-exclude |
| Empire Flippers | #94115 — Pet Care eCommerce | undisclosed | $19.4M annualized | $4.1M annualized | 21.2% | eCommerce / DTC | HARD-REJECT | Consumer retail/DTC hard-exclude |
| Empire Flippers | #90682 — Cryptocurrency Digital Product / Newsletter | undisclosed | $8.3M annualized | $5.2M annualized | 62.6% | Crypto / Digital Media | HARD-REJECT | B2C digital media; not vertical SaaS |
| Empire Flippers | #88177 — Home Amazon FBA | undisclosed | $8.1M annualized | $1.9M annualized | 23.6% | Amazon FBA / Consumer | HARD-REJECT | Consumer retail/DTC hard-exclude; revenue below Services floor |
| Empire Flippers | #94312 — Beauty / Health & Fitness eCommerce + FBA | undisclosed | $6.3M annualized | $1.5M annualized | 24.2% | eCommerce / DTC | HARD-REJECT | Consumer retail/DTC hard-exclude |
| Empire Flippers | #84831 — Business / Digital Media Service + Digital Product | undisclosed | $4.1M annualized | $1.8M annualized | 44.1% | Digital Media / Service | HARD-REJECT | Below Services revenue floor; digital/eCommerce exposure |
| Empire Flippers | #88296 — Supplements / Health & Fitness / Beauty eCommerce | undisclosed | $3.3M annualized | $1.4M annualized | 41.9% | eCommerce / DTC | HARD-REJECT | Consumer retail/DTC hard-exclude; pending sold |
| Empire Flippers | #83512 — Home / Romance Amazon FBA + eCommerce | undisclosed | $5.8M annualized | $1.5M annualized | 25.1% | Amazon FBA / Consumer | HARD-REJECT | Consumer retail/DTC hard-exclude |
| Empire Flippers | #91643 — Hobbies / Gaming Amazon FBA + eCommerce | undisclosed | $4.4M annualized | $1.3M annualized | 30.1% | Amazon FBA / Consumer | HARD-REJECT | Consumer retail/DTC hard-exclude; pending sold |
| Empire Flippers | #87832 — Bed & Bath Amazon FBA | undisclosed | $6.6M annualized | $1.3M annualized | 19.5% | Amazon FBA / Consumer | HARD-REJECT | Consumer retail/DTC hard-exclude; pending sold |
| Synergy Business Brokers | Commercial Construction Technology — Revenue +176% YoY | Florida | $9,059,000 | $3,275,000 | 36.2% | Construction / Technology | HARD-REJECT | Revenue below floor; construction hard-exclude |
| Synergy Business Brokers | Oil and Gas Specialty: Equipment Rental and Trucking Solutions | Texas | $15,293,339 | $6,563,296 | 42.9% | Oilfield Services | HARD-REJECT | EBITDA above Services ceiling; oilfield field services |
| Synergy Business Brokers | Seafood Processing And Distribution Company | Portugal | $165,000,000 | $5,900,000 | 3.6% | Food Processing / Distribution | HARD-REJECT | Non-US; manufacturing; margin below floor |
| Synergy Business Brokers | Commercial Plumbing Company, Strong Client Base | New Jersey | $13,575,714 | $4,034,348 | 29.7% | Construction / Plumbing | HARD-REJECT | Labor-heavy field services / construction hard-exclude |
| Synergy Business Brokers | Women’s Health Practice – Multi-Physician OB/GYN and Urogynecology Clinic | Florida | $6,578,488 | $3,376,803 | 51.3% | Healthcare / Physician Practice | HARD-REJECT | Revenue below floor; physician/provider healthcare hard-exclude |
| Synergy Business Brokers | Renovation Design And Build Company – Over 100% growth | New York | $8,500,000 | $2,344,000 | 27.6% | Construction / NYC | HARD-REJECT | Revenue below floor; NYC construction hard-exclude |
| Synergy Business Brokers | Logistics Business – Nationwide Niche | Illinois | $12,061,000 | $1,189,000 | 9.9% | Transportation / Logistics | HARD-REJECT | EBITDA and margin below floors |
| Synergy Business Brokers | Railroad Construction Business with $11.5M in Contracts | Missouri | $7,833,546 | $1,498,641 | 19.1% | Construction / Transportation | HARD-REJECT | Revenue below floor; construction hard-exclude |
| Synergy Business Brokers | B2B Health and Beauty: Proprietary Ingredient Manufacturer and Distributor | Dubai | $3,087,523 | $2,245,335 | 72.7% | Manufacturing / Distribution | HARD-REJECT | Non-US; revenue below floor |
| Synergy Business Brokers | Manufacturer of Specialty Copper Alloy Wires | India | $20,000,000 | $2,000,000 | 10.0% | Manufacturing | HARD-REJECT | Non-US; manufacturing hard-exclude |
| Synergy Business Brokers | Admissions Consulting Practice, Global, Fully Remote | United States | $2,000,000 | $1,300,000 | 65.0% | Consulting / Education | HARD-REJECT | Revenue and EBITDA below floors |
| Synergy Business Brokers | Prominent 40-Year Pediatric Practice, Real Estate Available | New York | $5,830,000 | $1,650,000 | 28.3% | Healthcare / Physician Practice | HARD-REJECT | Revenue below floor; physician/provider healthcare hard-exclude |
| Synergy Business Brokers | Growing Midwestern Trucking and Transportation Brokerage | Midwest | $9,000,000 | $1,650,000 | 18.3% | Transportation | HARD-REJECT | Revenue below floor |
| Synergy BB Real Estate | Event Rental Company: Full-Service | South Florida | $1,633,413 | $486,182 | 29.8% | Event Rental | HARD-REJECT | Revenue and EBITDA below floors |
| Synergy BB Real Estate | Short-Term Rental Property Management Company: 80+ Prime Locations | Midwest | $3,233,807 | $370,885 | 11.5% | Short-Term Rental Mgmt | HARD-REJECT | Revenue and EBITDA below floors; not estate management niche at scale |
| Synergy BB Real Estate | Groundwater Treatment Equipment Rental and Solutions Company – Sold | Florida | $3,500,000 | $1,300,000 | 37.1% | Equipment Rental | HARD-REJECT | Sold/inactive listing |
| Synergy BB Real Estate | Musical Instrument Rental & Repair Company – Sold | New Jersey | $2,348,039 | $283,822 | 12.1% | Rental / Repair | HARD-REJECT | Sold/inactive listing |
| Synergy BB Real Estate | Property Management Company with Available Real Estate: Sold | Vermont | $1,561,699 | $298,990 | 19.1% | Property Management | HARD-REJECT | Sold/inactive listing |
| Synergy BB Real Estate | Real Estate Investment Company, Semi-Absentee Owner – Sold | Pennsylvania | $2,371,950 | $394,752 | 16.6% | Real Estate | HARD-REJECT | Sold/inactive listing |
| Synergy BB Real Estate | Property Management firm – Sold | New York | $600,000 | $300,000 | 50.0% | Property Management | HARD-REJECT | Sold/inactive listing |
| Synergy BB Real Estate | Real Estate Property Management Office – Sold | New York | $888,397 | undisclosed | undisclosed | Property Management | HARD-REJECT | Sold/inactive listing |
| Website Closers | SBA Pre-Qualified Digital Marketing Agency — Interior Design / Architecture / Home Sectors | undisclosed | $612,498 | $176,929 cash flow | undisclosed | Digital Marketing | HARD-REJECT | Revenue and EBITDA below floors |
| Website Closers | SBA Pre-Qualified Media, Publishing & Digital Marketing Agency | undisclosed | $1,376,520 | $292,164 cash flow | undisclosed | Media / Marketing | HARD-REJECT | Revenue and EBITDA below floors |
| Website Closers | SBA Pre-Qualified Military Advertising Network & Digital Marketing Platform | undisclosed | $703,779 | $482,376 cash flow | undisclosed | Advertising / Digital | HARD-REJECT | Revenue and EBITDA below floors |
| Website Closers | Digital Media and Faith-Based Content Brand | undisclosed | $117,650 | $109,169 cash flow | undisclosed | Digital Media / B2C | HARD-REJECT | Revenue and EBITDA below floors; B2C content |
| Website Closers | SBA Pre-Qualified Web Design & Website Management Agency | undisclosed | $1,041,011 | $522,076 cash flow | undisclosed | Web Design / Services | HARD-REJECT | Revenue and EBITDA below floors |
| Website Closers | SBA Pre-Qualified Shark Tank CPG Brand | undisclosed | $2,109,255 | $536,619 cash flow | undisclosed | Consumer Products / CPG | HARD-REJECT | Consumer retail/DTC hard-exclude; below floors |
| Website Closers | 13-Year Women’s Apparel eCommerce Brand | undisclosed | $5,271,936 | $372,951 cash flow | 18% | eCommerce / Apparel | HARD-REJECT | Consumer retail/DTC hard-exclude; EBITDA below floor |
| Website Closers | AI News Intelligence & Data Platform | undisclosed | $863,838 | $572,554 cash flow | undisclosed | AI / Data Platform | HARD-REJECT | Revenue and EBITDA below floors; not active luxury SaaS thesis |
| Website Closers | Award Winning, SBA Pre-Qualified Marketing & PR Agency | undisclosed | $1,462,056 | $294,991 cash flow | undisclosed | Marketing / PR | HARD-REJECT | Revenue and EBITDA below floors |

## Source Scorecard

| Source | Category | Status | HTTP | Listings Reviewed | Matches | Last Match Date |
|--------|----------|--------|------|-------------------|---------|-----------------|
| BizBuySell | General | blocked (verified) | 403 | 0 | 0 | — |
| Business Exits | General | active | 200 | 30 | 0 | — |
| DealForce | General | active (email-routed; email artifact missing) | n/a | 0 | 0 | — |
| Empire Flippers | General | active | 200 | 18 | 0 | — |
| Everingham & Kerr | General | active (email-routed; email artifact missing) | n/a | 0 | 0 | — |
| Flippa | General | blocked (verified) | 200 | 0 | 0 | — |
| IAG M&A Advisors | General | active (email-routed; email artifact missing) | n/a | 0 | 0 | — |
| Quiet Light | General | blocked (verified) | 403 | 0 | 0 | — |
| Rejigg | General | active (email-routed; email artifact missing) | n/a | 0 | 0 | — |
| SMB Deal Hunter (Helen Guo) | General | active (email-routed; email artifact missing) | n/a | 0 | 0 | — |
| Synergy Business Brokers | General | active | 200 | 14 | 0 | — |
| Viking Mergers | General | blocked (verified) | 403 | 0 | 0 | — |
| Website Closers | General | active | 200 | 10 | 2 | 2026-06-05 |
| GP Bullhound | Niche-Specific (Vertical SaaS) | active — direct relationship/intel only | 200 | 0 | 0 | — |
| PCO Bookkeepers | Niche-Specific (Premium Pest) | active — image tombstones, not parseable | 200 | 0 | 0 | — |
| Sica Fletcher | Niche-Specific (Specialty Insurance) | active — intel-only completed transactions | 200 | 0 | 0 | — |
| Synergy BB Real Estate | Niche-Specific (Estate Management) | active | 200 | 8 | 0 | — |

**Notes:**
- BizBuySell, Quiet Light, Viking Mergers, and Flippa were blocked on live fetch / JS-shell fallback checks. `agent-browser` is not installed on this host, so browser fallback was unavailable.
- Email-routed active sources remained scorecarded, but `brain/context/email-scan-results-2026-06-08.md` was missing after the bounded retry, so no inbox-deal rows were available to parse.
- Website Closers: the lead-generation marketplace match remains fingerprinted in the dedup store; it was observed again today but not Slack-posted because the fingerprint already exists.

## Volume Check

- Deals surfaced today: 0
- Broker-opportunistic review items: 5
- 7-day rolling average: 0.29 deals/day
- Target: 1-3/day — BELOW TARGET
- Email leg: missing
- Funnel bottleneck: email leg / blocked browser fallback