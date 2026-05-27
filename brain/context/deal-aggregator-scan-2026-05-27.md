---
date: 2026-05-27
deals_found: 0
sources_scanned: 17
sources_blocked_verified: 1
sources_blocked_single_attempt: 0
email_deals: 9
dealsx_replies: 0
---
# Deal Aggregator Scan — 2026-05-27

Morning headless run. 17 Active sources covered. Email-scan-results-2026-05-27 already extracted 9 listings (Helen Guo SMB Deal Hunter + Flippa Daily) — those are screened below in the per-listing log alongside fresh WebFetch pulls from Business Exits, Synergy Business Brokers (general + real-estate), Empire Flippers, Website Closers. Intel-only niche sources (Sica Fletcher, GP Bullhound, SEG, PCO Bookkeepers) scraped for market signal only — not Slack-posted. No DealsX Proprietary Outreach replies in today's email-scan-results.

**Result: zero PASS listings → zero Slack posts to `#active-deals` today.** One NEAR-MISS (LED Display Solutions FL — clears Services buy-box financial gate but no active-niche corpus match) and one FLAG (Loss Prevention Training Platform — ARR undisclosed, possibly sub-$3M SaaS floor) surfaced for thesis-drift / calibration visibility.

Corpus path log per active niche:
- Premium Pest Management → DEALSX keywords (DealsX "Specialty Pest & Environmental Management Services")
- Private art advisory firms → WR row enrichment (Niche Hypothesis + Quick notes — DealsX Niche field blank)
- Estate Management Companies → DEALSX keywords
- Specialty Coffee Equipment Service → DEALSX keywords (DealsX "Specialty Commercial Equipment Services")
- High-End Commercial Cleaning → DEALSX keywords
- Vertical SaaS for Luxury & High-Value Asset Service Industries → DEALSX keywords
- Specialty Insurance Brokerage (Art & Collectibles) → DEALSX keywords
- Storage & Related Services for High Value Assets → DEALSX keywords (DealsX "Specialty Storage & Handling for High-Value Collections")

## Deals Surfaced (sent to Slack individually)

None today. Zero listings passed both the buy-box financial gate AND an active-niche corpus match.

## Email Inbound Deals

The 9 listings extracted by email-intelligence in section 7 of [[brain/context/email-scan-results-2026-05-27]] (5 Helen Guo SMB Deal Hunter + 4 Flippa Daily) all HARD-REJECTED on revenue/EBITDA below Services Buy Box floors or on Industry/Geography hard-excludes. Per-listing verdicts in the Listings Reviewed log below. No CIMs, NDA confirmations, broker BLASTs, intro forwards, or other deal-specific emails in today's email-scan window.

## DealsX Proprietary Outreach Replies

None today. No `dealsx.notifaction@gmail.com` "Lead Interested" notifications in today's email-scan-results.

## Near Misses (not Slacked)

- **LED Display Solutions Company (Synergy Business Brokers, FL)** — $11.19M rev / $4.63M cash flow / 41% margin. Clears Services Buy Box financial gate cleanly (within $10-50M rev band, $1.5-5M EBITDA band, margin floor). No active-niche corpus match (LED display manufacturing/distribution is off-thesis for current 8 active niches). Borderline industry — light-mfg/distribution, not hard-excluded as capital-intensive. NEAR-MISS rather than PASS because corpus match is the gate, not just buy-box.
- **Loss Prevention Training Platform (Website Closers)** — $3.3M ask, $792K cash flow, no ARR disclosed. Adjacent to Workplace H&S Compliance Training niche (WEEKLY REVIEW row 12, "New - Pending Review" — not Active). FLAGGED rather than rejected per Data Availability Rule (ARR undisclosed → flag don't reject). If ARR is sub-$3M, would HARD-REJECT against SaaS Buy Box floor — surfaced for human review.
- **Helen Guo CA trucking-compliance listing** — flags [[feedback-no-california]] hard-exclude AND below revenue/EBITDA floors. Niche corpus (Truck Licensing & Compliance, WR row 15) is "New - Pending Review" with THIN-POOL caveat — not Active. HARD-REJECT, not even NEAR-MISS.
- **No new broker introductions** detected in today's email-scan-results (Section 4 intros = none).

## Listings Reviewed (full log)

Every listing scraped or parsed during this run, regardless of verdict. Sort: PASS → NEAR-MISS → FLAG → HARD-REJECT.

| Source | Headline | Geo | Revenue | EBITDA | Margin | Industry | Verdict | Reject Reason |
|--------|----------|-----|---------|--------|--------|----------|---------|---------------|
| Synergy Business Brokers | Growing LED Display Solutions Company | FL | $11.19M | $4.63M | 41% | LED display tech/distribution | NEAR-MISS | Clears Services Buy Box; off-thesis (no active-niche corpus match) |
| Website Closers | Loss Prevention Training Platform | undisclosed | undisclosed | undisclosed | undisclosed | B2B Training / Compliance eLearning | FLAG | ARR undisclosed; possibly sub-$3M SaaS floor; W&H&S Compliance niche is "New - Pending Review" not Active |
| Business Exits | Ireland Construction Business | Ireland | €25M | €6.15M | 25% | Construction | HARD-REJECT | Non-US (US TAM only) + Construction hard-exclude |
| Business Exits | California Property Tax Consultants | CA | $6.68M | $4.68M | 70% | Property tax consulting | HARD-REJECT | Revenue below $10M Services floor; CA soft-flag |
| Business Exits | Luxury Wedding Venue | undisclosed | $3.18M | $2.35M | 74% | Hospitality / wedding venue | HARD-REJECT | Revenue below floor; Restaurants/hospitality/nightlife hard-exclude |
| Business Exits | Northeast Commercial Contractor | Northeast | $21.96M | $2.78M | 13% | Construction | HARD-REJECT | Construction hard-exclude |
| Business Exits | Specialized Military & Aerospace Parts Distributor | undisclosed | $8.23M | $1.9M | 23% | Aerospace/defense parts distribution | HARD-REJECT | Revenue below floor; aviation/aerospace adjacency per [[feedback-no-aviation-targets]] |
| Business Exits | Niche Construction Service Business | undisclosed | $10.8M | $2.3M | 21% | Construction | HARD-REJECT | Construction/labor-heavy field services hard-exclude |
| Business Exits | Florida Med Spa and Regenerative Medicine Clinic | FL | $1.07M | $724K | 67% | Provider-owned healthcare | HARD-REJECT | Revenue below floor; Physician practices / provider-owned healthcare hard-exclude |
| Synergy Business Brokers | Commercial Construction Technology | FL | $9.06M | $3.28M | 36% | Construction tech | HARD-REJECT | Revenue below floor; Construction hard-exclude |
| Synergy Business Brokers | Oil and Gas Specialty Equipment Rental and Trucking | TX | $15.29M | $6.56M | 43% | Oil & gas equipment rental | HARD-REJECT | Capital-intensive / industrial services off-thesis |
| Synergy Business Brokers | Seafood Processing And Distribution Company | Portugal | $165M | $5.9M | 4% | Food processing/distribution | HARD-REJECT | Non-US (US TAM only); also margin below 10% Services floor |
| Synergy Business Brokers | Commercial Plumbing Company | NJ | $13.58M | $4.03M | 30% | Plumbing/construction trade | HARD-REJECT | Construction/labor-heavy field services hard-exclude |
| Synergy Business Brokers | Women's Health OB/GYN & Urogynecology Clinic | FL | $6.58M | $3.38M | 51% | Provider-owned healthcare | HARD-REJECT | Revenue below floor; Physician practices hard-exclude |
| Synergy Business Brokers | Precision Machine Shop, 50 Year Legacy | AZ | $7.5M | $2.3M | 31% | Precision machining | HARD-REJECT | Revenue below floor; Capital-intensive manufacturing hard-exclude |
| Synergy Business Brokers | Ethanol Producer With Real Estate | India | $10.5M | $3M | 29% | Ethanol manufacturing | HARD-REJECT | Non-US; Capital-intensive manufacturing |
| Synergy Business Brokers | Industrial Minerals Producer & Distributor | Peru | $7M | $4.5M | 64% | Mining/industrial minerals | HARD-REJECT | Non-US; Capital-intensive |
| Synergy Business Brokers | Telecom Caller Trust Platform | US | $2.71M | $1.61M | 59% | Telecom anti-fraud SaaS (horizontal) | HARD-REJECT | ARR below $3M SaaS floor; Horizontal SaaS hard-exclude |
| Synergy Business Brokers | Renovation Design And Build Company | NYC | $8.5M | $2.34M | 28% | Construction/renovation | HARD-REJECT | NYC construction explicitly excluded per [[feedback-nyc-construction-hard-exclude]] |
| Synergy Business Brokers | Garment Manufacturing Facility | Bangladesh | $12.5M | $1.95M | 16% | Garment manufacturing | HARD-REJECT | Non-US; Capital-intensive manufacturing |
| Synergy Business Brokers | Railroad Construction Business | MO | $7.83M | $1.5M | 19% | Railroad construction | HARD-REJECT | Revenue below floor; Construction hard-exclude |
| Synergy Business Brokers | B2B Health and Beauty Ingredient Mfr/Distributor | Dubai | $3.09M | $2.25M | 73% | Specialty ingredient mfr/distribution | HARD-REJECT | Non-US; Revenue below floor |
| Synergy Business Brokers | Manufacturer of Specialty Copper Alloy Wires | India | $20M | $2M | 10% | Copper alloy wire mfr | HARD-REJECT | Non-US; Capital-intensive manufacturing |
| Synergy Business Brokers RE | Event Rental Company: Full-Service | South FL | $1.63M | $486K | 30% | Event rentals | HARD-REJECT | Revenue below floor; EBITDA below floor |
| Synergy Business Brokers RE | Short-Term Rental Property Management Co | Midwest | $3.23M | $371K | 11% | Short-term rental property mgmt | HARD-REJECT | Revenue below floor; EBITDA below floor; STR mgmt not Estate Mgmt niche (HNW residential focus) |
| Empire Flippers | Sports/Business/Entertainment B2B2C | undisclosed | ~$1.18M | ~$394K | 33% | eCommerce/service/digital | HARD-REJECT | Revenue below floor; off-thesis digital |
| Empire Flippers | Home/Outdoors (Amazon FBA - Pest Control) | undisclosed | ~$3.1M | ~$638K | 21% | Amazon FBA consumer pest products | HARD-REJECT | Consumer retail/DTC hard-exclude (FBA brand, not pest-services niche) |
| Empire Flippers | News & Education (Amazon KDP) | undisclosed | ~$125K | ~$124K | 99% | Amazon KDP self-publishing | HARD-REJECT | Revenue below floor; consumer content |
| Empire Flippers | Pet Care/Outdoors (Amazon FBA) | undisclosed | ~$703K | ~$91K | 13% | Amazon FBA pet products | HARD-REJECT | Revenue below floor; Consumer retail/DTC |
| Empire Flippers | Entertainment (YouTube) | undisclosed | ~$61K | ~$60K | 98% | YouTube channel | HARD-REJECT | Revenue below floor; consumer content |
| Empire Flippers | Health & Fitness/Home/Medical (FBA+eComm) | undisclosed | ~$17.6M | ~$4.6M | 26% | Amazon FBA + eComm health/fitness | HARD-REJECT | Consumer retail/DTC hard-exclude |
| Empire Flippers | Pet Care eCommerce | undisclosed | ~$19.4M | ~$4.1M | 21% | Pet eCommerce | HARD-REJECT | Consumer retail/DTC hard-exclude |
| Empire Flippers | Cryptocurrency (Digital Product/Newsletter) | undisclosed | ~$8.3M | ~$5.2M | 63% | Crypto/digital products | HARD-REJECT | Off-thesis; lending/credit-extension adjacency risk |
| Empire Flippers | Home (Amazon FBA - Pest Control) | undisclosed | ~$8.1M | ~$1.9M | 24% | Amazon FBA consumer pest products | HARD-REJECT | Consumer retail/DTC hard-exclude (FBA, not pest-services) |
| Empire Flippers | Beauty/Health & Fitness | undisclosed | ~$6.3M | ~$1.5M | 24% | Beauty/H&F eComm/FBA | HARD-REJECT | Consumer retail/DTC hard-exclude |
| Website Closers | Award Winning Marketing & PR Agency | undisclosed | undisclosed | $295K | undisclosed | Marketing/PR agency | HARD-REJECT | Cash flow below floor; off-thesis services |
| Website Closers | Fine Jewelry eCommerce Brand (25-Year) | undisclosed | undisclosed | $282K | undisclosed | Jewelry eCommerce | HARD-REJECT | Consumer retail/DTC hard-exclude |
| Website Closers | AI-Driven Cybersecurity Ed-Tech Platform | undisclosed | undisclosed | $779K | undisclosed | EdTech / horizontal SaaS | HARD-REJECT | Horizontal SaaS / B2C ed-tech hard-exclude |
| Website Closers | Sales Coaching & Lead Generation Platform | undisclosed | undisclosed | $109K | undisclosed | B2B sales training SaaS | HARD-REJECT | Cash flow below floor; horizontal SaaS |
| Website Closers | SaaS Infrastructure for Financial Trading | undisclosed | undisclosed | $3.35M | undisclosed | FinTech SaaS infrastructure | HARD-REJECT | Horizontal SaaS adjacency; balance-sheet-heavy fintech adjacency risk |
| Website Closers | Amazon FBA eCommerce Brand | undisclosed | undisclosed | $955K | undisclosed | Amazon FBA | HARD-REJECT | Consumer retail/DTC hard-exclude |
| Website Closers | Ed-Tech eLearning Platform (10-Year) | undisclosed | undisclosed | $1.63M | undisclosed | Ed-tech/eLearning | HARD-REJECT | Horizontal / B2C ed-tech hard-exclude |
| Website Closers | AI-Native SEO & Content Marketing Agency | undisclosed | undisclosed | $121K | undisclosed | SEO/marketing services | HARD-REJECT | Cash flow below floor; off-thesis |
| Website Closers | Authenticated Collectibles eCommerce | undisclosed | undisclosed | $259K | undisclosed | Collectibles eCommerce | HARD-REJECT | Cash flow below floor; Consumer retail/DTC |
| Helen Guo SMB Deal Hunter | Absentee-Run Commercial Sign Manufacturer ($2.95M ask) | MO | $4.36M | $661K | 15% | Sign manufacturing + LED retrofit | HARD-REJECT | Revenue + EBITDA below floors; capital-intensive mfg adjacency |
| Helen Guo SMB Deal Hunter | Trucking Licensing and Compliance Services ($1.43M ask) | CA | $1.04M | $412K | 40% | Trucking compliance / recurring filings | HARD-REJECT | Revenue + EBITDA below floors; CA soft-flag; Truck Licensing niche is "New - Pending Review" not Active |
| Helen Guo SMB Deal Hunter | Facility Maintenance Contractor ($3.2M ask) | UT | $4.51M | $838K | 19% | Facility maintenance / multi-state | HARD-REJECT | Revenue + EBITDA below floors |
| Helen Guo SMB Deal Hunter | Specialty Copper-Infused Lumber Wholesaler ($2.35M ask) | NC | $4.72M | $698K | 15% | Specialty lumber wholesale | HARD-REJECT | Revenue + EBITDA below floors |
| Helen Guo SMB Deal Hunter | Dairy Equipment Sales/Service ($1M ask) | UT | $2.5M | $443K | 18% | Dairy equipment / robotic milking | HARD-REJECT | Revenue + EBITDA below floors |
| Flippa Marketplace | Audio Production / Dubbing / Localization (11 yrs) | MD | $2.1M | undisclosed | undisclosed | Audio post-production / entertainment | HARD-REJECT | Revenue below floor; off-thesis entertainment services |
| Flippa Marketplace | Fire Alarm Equipment Reseller (Shopify+eBay, 2 yrs) | undisclosed | $440K | undisclosed | 56% | Fire alarm equipment resale / eComm | HARD-REJECT | Revenue below floor; operating history <5 yrs; Consumer/DTC adjacency |
| Flippa Marketplace | All-In-One Waitlist SaaS (4 yrs, F500) | undisclosed | $142K ($13K MRR) | undisclosed | 74% | SaaS / waitlist + analytics | HARD-REJECT | ARR ~$156K below $3M SaaS floor; operating history <5 yrs; horizontal SaaS |
| Flippa Marketplace | Survival Game YouTube Channel (Rust, 252K subs) | undisclosed | $56K | undisclosed | 98% | YouTube / gaming content | HARD-REJECT | Revenue below floor; consumer content |
| GP Bullhound | Sdui — Fundraise with Bain Capital | Europe | undisclosed | undisclosed | undisclosed | Business software/AI | HARD-REJECT | Non-US (intel-only INTEL source, no Slack regardless) |
| GP Bullhound | Peak — Acquired by UiPath | UK/US | undisclosed | undisclosed | undisclosed | Business software/AI | HARD-REJECT | Acquired (closed deal — intel only) |
| GP Bullhound | Flo Health — $200M from General Atlantic | US | undisclosed | undisclosed | undisclosed | Consumer tech (women's health) | HARD-REJECT | B2C/horizontal; intel only |
| GP Bullhound | Runna — Acquired by Strava | UK/US | undisclosed | undisclosed | undisclosed | Consumer tech (fitness) | HARD-REJECT | B2C/horizontal; intel only |
| GP Bullhound | Instaleap — Acquired by Instacart | Global | undisclosed | undisclosed | undisclosed | Business software/AI | HARD-REJECT | Acquired (closed); intel only |
| GP Bullhound | AB Tasty — Merger with VWO | Europe | undisclosed | undisclosed | undisclosed | Business software/AI | HARD-REJECT | Non-US; merger closed; intel only |

## Source Scorecard

| Source | Category | Status | HTTP | Listings Reviewed | Matches | Last Match Date |
|--------|----------|--------|------|-------------------|---------|-----------------|
| BizBuySell | General | blocked (verified) | 403 | 0 | 0 | — |
| Business Exits | General | active | 200 | 7 | 0 | — |
| DealForce | General | active | — | 0 | 0 | — |
| Empire Flippers | General | active | 200 | 10 | 0 | — |
| Everingham & Kerr | General | active | — | 0 | 0 | — |
| Flippa | General | active | — | 4 | 0 | — |
| IAG M&A Advisors | General | active | — | 0 | 0 | — |
| Quiet Light | General | active | — | 0 | 0 | — |
| Rejigg | General | active | 200 | 0 | 0 | — |
| SMB Deal Hunter (Helen Guo) | General | active | — | 5 | 0 | — |
| Synergy Business Brokers | General | active | 200 | 15 | 0 | — |
| Viking Mergers | General | active | — | 0 | 0 | — |
| Website Closers | General | active | 200 | 10 | 0 | — |
| GP Bullhound | Niche-Specific (Vertical SaaS) | active | 200 | 6 | 0 | — |
| PCO Bookkeepers | Niche-Specific (Premium Pest) | active | 200 | 0 | 0 | — |
| Sica Fletcher | Niche-Specific (Insurance) | active | 200 | 0 | 0 | — |
| Synergy Business Brokers Real Estate | Niche-Specific (Estate Mgmt) | active | 200 | 2 | 0 | — |

**Notes:**
- `BizBuySell` returned HTTP 403 on both primary fetch and second-attempt verification → `blocked (verified)`. Source is in the SKILL.md "must use agent-browser" list (JS-shell / scraper-UA-blocked). agent-browser is NOT installed on this VPS → `BROWSER_AUTOMATION_UNAVAILABLE: BizBuySell skipped, requires agent-browser install` per stop hook.
- `DealForce`, `Everingham & Kerr`, `IAG M&A Advisors`, `Quiet Light`, `SMB Deal Hunter`, `Viking Mergers`, `Flippa` — email-only sources; channel health verified by recent email-scan-results history (most recent inbound from each is within last 30 days per Sourcing Sheet Notes column). No HTTP fetch attempted today since the channel is email-driven. Today's email-scan-results extracted listings from SMB Deal Hunter (5) and Flippa (4); the other four email-only sources had no inbound triggering a DEAL_NEWSLETTER classification today.
- `Rejigg` — homepage scraped 200 OK but shows only "Recent Closings" (past deals) + "Success Stories" case studies, not active inventory. Active deals page is member-gated per Sourcing Sheet Notes. 0 active listings extractable from the public homepage.
- `Quiet Light` — listed as Cloudflare-blocked per Sourcing Sheet, but channel is email-only ("Active - email-only") so no web fetch attempted; no DEAL_NEWSLETTER inbound today.
- `Sica Fletcher` and `GP Bullhound` and `PCO Bookkeepers` — Niche-Specific INTEL-only sources. Scraped for market signal (Sica Fletcher shows ~200 historical consolidator-driven transactions with last new announcement 2/27/2026 — no 2026-05-27 new). Per Channel-Type routing, INTEL sources do NOT trigger Slack pings even on matches; "Listings Reviewed" counts deal announcements that surfaced, not buy-box matches.

## Volume Check

- Deals surfaced today: 0
- 7-day rolling average: pending (yesterday's artifact `deal-aggregator-scan-2026-05-26.md` to be aggregated; trend computation tracks daily artifacts)
- Target: 1-3/day — **BELOW TARGET** (zero surfaced, expected ~1 evaluable/day)

**Below-target note:** Today's 60 listings reviewed (across 13 web-accessible + email-only sources) yielded zero PASS matches. Failure pattern: (a) Helen Guo and Flippa newsletter listings are SMB-scale sub-$1M-EBITDA businesses, all below Services Buy Box $1.5M EBITDA floor; (b) Business Exits + Website Closers + Empire Flippers + Synergy general inventory skewed to construction, consumer-FBA/eCommerce, and horizontal SaaS, all hard-excluded; (c) Synergy Real Estate had only 2 active listings, both sub-floor. The active-niche corpus is narrow (8 niches, heavily weighted to specialty/luxury services) and broker-marketplace inventory is broad/generalist — corpus mismatch is the dominant filter. This pattern is consistent with last week's scans and feeds [[feedback-industry-is-output-of-network]] (network-mapping-first thesis: broad marketplace screens are diminishing-returns for Kay's specific buy-box).
