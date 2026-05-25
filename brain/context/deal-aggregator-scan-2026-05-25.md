---
schema_version: 1.1.0
date: 2026-05-25
type: context
title: "Deal Aggregator Scan — 2026-05-25 (Memorial Day Monday, morning run)"
deals_found: 0
sources_scanned: 21
sources_blocked_verified: 4
sources_blocked_single_attempt: 0
email_deals: 0
dealsx_replies: 0
buy_box_source: live
tags:
  - date/2026-05-25
  - context
  - topic/deal-aggregator
  - topic/morning-scan
  - status/done
---

# Deal Aggregator Scan — 2026-05-25

US Memorial Day holiday — typical broker-platform activity tempo. Email channel covered Sat-Sun-Mon window via [[brain/context/email-scan-results-2026-05-25]]: 0 broker BLAST per-deal listings, 0 CIMs, 0 introductions, 0 DealsX replies. Web platforms scanned in full per Channel 1; only listings reaching active-niche corpus thresholds are sent to Slack. None today.

**Niche corpus path log (Step 0c stop-hook):**
- Premium Pest Management → DealsX keywords ("Specialty Pest & Environmental Management Services")
- Private art advisory firms → WR row enrichment (Niche Hypothesis + Quick notes — DealsX Niche field blank)
- Estate Management Companies → DealsX keywords ("Estate Management Companies")
- Specialty Coffee Equipment Service → DealsX keywords ("Specialty Commercial Equipment Services")
- High-End Commercial Cleaning → DealsX keywords ("High-End Commercial Cleaning")
- Vertical SaaS for Luxury & High-Value Asset Service Industries → DealsX keywords ("Vertical SaaS for Luxury & High-Value Asset Service Industries")
- Specialty Insurance Brokerage (Art & Collectibles) → DealsX keywords ("Specialty Insurance Brokerage")
- Storage & Related Services for High-Value Assets → DealsX keywords ("Specialty Storage & Handling for High-Value Collections")

## Deals Surfaced (sent to Slack individually)

None today. Zero listings cleared both the buy-box gate AND active-niche corpus match.

## Email Inbound Deals

None. [[brain/context/email-scan-results-2026-05-25]] flagged 0 CIMs, 0 broker BLAST per-deal listings, 0 introductions in the 2026-05-23 → 2026-05-25 window. Flippa Sat/Sun digests were pure consumer ecom — skipped per [[memory/feedback_marketplace_vs_broker_distinction]] + [[memory/feedback_b2b_b2b2c_ok_no_b2c]].

## DealsX Proprietary Outreach Replies

None. No `Lead Interested` notifications from `dealsx.notifaction@gmail.com` in the window per the email-scan-results classification.

## Near Misses (not Slacked)

Listings that cleared the buy-box financial gate but lacked any active-niche corpus match. Tracked for thesis-drift / corpus-tuning calibration, not Slacked.

- **GovCon IT Firm** (Business Exits) — $19.7M revenue / $3.45M EBITDA / ~17.5% margin / location undisclosed. GovCon IT services. Adjacent to no active niche.
- **B2B Experiential Marketing Vendor** (Business Exits) — $14.3M TTM revenue / $3.3M TTM EBITDA / ~23% margin / location undisclosed. Marketing services. Adjacent to no active niche.
- **GovCon ERP Service Business** (Business Exits) — $14M revenue / $2.57M EBITDA / ~18% margin / location undisclosed. GovCon ERP services. Adjacent to no active niche.
- **LED Display Solutions Company** (Synergy BB) — $11.2M revenue / $4.6M EBITDA / ~41% margin / Florida. Tech/distribution, not luxury VSaaS. Adjacent to no active niche.
- **Ed-Tech eLearning Platform** (Website Closers) — asking $7.5M / SDE $1.63M / location undisclosed. EdTech SaaS — not Luxury VSaaS corpus. Adjacent to Workplace Health & Safety Compliance Training (eLearning) but that niche is row 12 New-Pending Review, not Active.
- **Loss Prevention Training Platform** (Website Closers) — asking $3.3M / SDE $793K / location undisclosed. Training SaaS — not Luxury VSaaS corpus.
- **SaaS Infrastructure for Trading Firms** (Website Closers) — asking $28.5M / SDE $3.35M / ARR undisclosed / location undisclosed. FinTech-adjacent SaaS for trading firms — not Luxury VSaaS; SaaS BB hard-exclude check for "balance-sheet-heavy fintech" is ambiguous (trading infrastructure ≠ lending). Flagged for human review, not Slacked.

**Calibration signal:** GovCon services repeat across Business Exits (3 listings in window). Not a thesis-shape candidate for Kay (no women-led network access per [[memory/feedback_industry_is_output_of_network]]), but worth noting as a recurring buy-box-clean shape that the corpus doesn't capture.

## Listings Reviewed (full log)

Every listing scraped or parsed during this run, regardless of verdict. Sorted PASS → NEAR-MISS → FLAG → HARD-REJECT.

| Source | Headline | Geo | Revenue | EBITDA | Margin | Industry | Verdict | Reject Reason |
|--------|----------|-----|---------|--------|--------|----------|---------|---------------|
| Business Exits | GovCon IT Firm | undisclosed | $19.7M | $3.45M | ~17.5% | GovCon IT services | NEAR-MISS | No active-niche corpus match |
| Business Exits | B2B Experiential Marketing Vendor | undisclosed | $14.3M | $3.3M | ~23% | Marketing services | NEAR-MISS | No active-niche corpus match |
| Business Exits | Government Contract ERP Service Business | undisclosed | $14M | $2.57M | ~18% | GovCon ERP services | NEAR-MISS | No active-niche corpus match |
| Synergy BB | Growing LED Display Solutions Company | FL | $11.2M | $4.6M | ~41% | LED display tech/distribution | NEAR-MISS | No active-niche corpus match |
| Website Closers | Ed-Tech eLearning Platform | undisclosed | undisclosed | $1.63M (SDE) | undisclosed | EdTech SaaS | NEAR-MISS | EdTech, not Luxury VSaaS corpus |
| Website Closers | Loss Prevention Training Platform | undisclosed | undisclosed | $793K (SDE) | undisclosed | Training SaaS | NEAR-MISS | Training SaaS, not Luxury VSaaS corpus |
| Website Closers | SaaS Infrastructure for Trading Firms | undisclosed | undisclosed | $3.35M (SDE) | undisclosed | FinTech-adjacent SaaS | FLAG | ARR undisclosed + ambiguous balance-sheet-fintech exclude |
| Business Exits | Midwest Multi-Location Wellness Practice | Midwest | $21.3M | $12.9M | ~61% | Healthcare/wellness | HARD-REJECT | Physician/provider healthcare excluded |
| Business Exits | Ireland Construction Business | Ireland | €25M | €6.15M | ~25% | Construction | HARD-REJECT | Geography (non-US) + construction excluded |
| Business Exits | California Property Tax Consultants | CA | $6.68M | $4.68M | ~70% | Marketing/consulting | HARD-REJECT | Revenue below $10M floor (disclosed-fails); CA soft-flag |
| Business Exits | Luxury Wedding Venue | undisclosed | $3.18M | $2.35M | ~74% | Hospitality | HARD-REJECT | Hospitality excluded |
| Business Exits | Metal Building Supplier with US Manufacturing | US | $33.7M | $3.97M | ~12% | Construction/manufacturing | HARD-REJECT | Capital-intensive manufacturing |
| Business Exits | California Staffing Firm with Recurring Revenue | CA | $7.82M | $3.2M | ~41% | Staffing services | HARD-REJECT | Revenue below $10M floor (disclosed-fails) |
| Business Exits | Texas Non-Emergency Medical Transport | TX | $7.74M | $2.87M | ~37% | Healthcare/transport | HARD-REJECT | Revenue below $10M floor (disclosed-fails) |
| Business Exits | Northeast Commercial Contractor | Northeast | $22M | $2.78M | ~13% | Construction | HARD-REJECT | Construction excluded |
| Business Exits | Atlanta Area Residential Plumbing & Septic | GA | $11.7M | $2.41M | ~21% | Construction/field services | HARD-REJECT | Labor-heavy field services excluded |
| Business Exits | Design & Build Studio for Themed Props | undisclosed | $10M | $3.06M | ~31% | Construction/manufacturing | HARD-REJECT | Construction + manufacturing excluded |
| Business Exits | Texas HVAC—Residential New Construction | TX | $22M | $2.28M | ~10% | Construction/HVAC | HARD-REJECT | Construction excluded |
| Business Exits | Cell Phone Tower Installation & Repair | undisclosed | $8.93M | $1.95M | ~22% | Construction services | HARD-REJECT | Revenue below $10M floor (disclosed-fails) |
| Business Exits | Specialized Military/Aerospace Parts Distributor | undisclosed | $8.23M | $1.9M | ~23% | Aerospace distribution | HARD-REJECT | Aviation/aerospace hard-exclude per [[memory/feedback_no_aviation_targets]] |
| Business Exits | Niche Construction Service Business | undisclosed | $10.8M | $2.3M | ~21% | Construction | HARD-REJECT | Construction excluded |
| Business Exits | Category Defining Window Manufacturer | undisclosed | $4.9M | $1.54M | ~31% | Manufacturing/retail | HARD-REJECT | Revenue below $10M + capital-intensive mfg |
| Business Exits | Southeast Electrical Contractor | Southeast | $5.28M | $1.91M | ~36% | Construction | HARD-REJECT | Revenue below $10M + construction |
| Business Exits | Safe Pet Travel Products Distribution | undisclosed | $1.67M | $1.03M | ~62% | B2C product distribution | HARD-REJECT | Revenue below $10M + B2C consumer retail |
| Business Exits | Government Contracted Military Promotional Products | US (remote) | $8.18M | $788K | ~10% | Retail/services | HARD-REJECT | Revenue below $10M + EBITDA below $1.5M |
| Business Exits | Nevada Commercial Fireproofing Contractor | NV | $3.06M | $932K | ~30% | Construction | HARD-REJECT | Revenue/EBITDA below floor + construction |
| Business Exits | Specialized Canadian Recruitment Agency | Canada | $2.28M CAD | $764K CAD | ~34% | Staffing | HARD-REJECT | Geography (non-US) |
| Business Exits | Florida Med Spa and Regenerative Medicine | FL | $1.07M | $724K | ~68% | Healthcare | HARD-REJECT | Healthcare/provider + below floor |
| Business Exits | Landscape Architecture Business | undisclosed | $5.5M | $1.8M | ~33% | Construction | HARD-REJECT | Revenue below $10M + construction |
| Business Exits | Restaurant and Juice Bar Franchise | undisclosed | $4.14M TTM | $714K TTM | ~17% | Restaurant/franchise | HARD-REJECT | Restaurant + franchise excluded |
| Business Exits | Colorado Regenerative & Functional Medicine | CO | $895K | $494K | ~55% | Healthcare | HARD-REJECT | Healthcare + below floor |
| Business Exits | Bay Area Residential Roofing Company | CA | $2.5M | $470K | ~19% | Construction | HARD-REJECT | Construction + CA soft-flag + below floor |
| Business Exits | Texas Home Health Staffing Firm | TX | $2.49M | $337K | ~14% | Healthcare/staffing | HARD-REJECT | Below floor + healthcare-adjacent |
| Business Exits | New Jersey HVAC-R and Lead Remediation | NJ | $3.37M | $373K | ~11% | Construction | HARD-REJECT | Construction + below floor |
| Empire Flippers | Medical Language Learning App (#94091) | undisclosed | ~$108K | undisclosed | undisclosed | Healthcare/EdTech SaaS | HARD-REJECT | ARR below $3M floor (disclosed-fails) |
| Empire Flippers | Crypto News Platform (#90682) | undisclosed | ~$5.2M | $5.2M | ~100% (content) | Crypto/news/content | HARD-REJECT | Not vertical SaaS; B2C content; crypto-adjacent |
| Empire Flippers | Shopify Store Service Business (#84831) | undisclosed | ~$1.7M | $1.7M | undisclosed | Shopify services | HARD-REJECT | Revenue below $10M floor |
| Empire Flippers | B2B2C Entertainment Business (#94296) | undisclosed | ~$394K | $394K | undisclosed | Entertainment/hospitality | HARD-REJECT | Below floor + hospitality |
| Synergy BB | Commercial Construction Technology FL | FL | $9.06M | $3.28M | ~36% | Construction tech | HARD-REJECT | Construction excluded |
| Synergy BB | Oil and Gas Specialty Equipment Rental TX | TX | $15.3M | $6.56M | ~43% | Capital-intensive services | HARD-REJECT | Capital-intensive mfg-adjacent |
| Synergy BB | Seafood Processing Portugal | Portugal | $165M | $5.9M | ~3.6% | Manufacturing | HARD-REJECT | Geography (non-US) + mfg + margin below floor |
| Synergy BB | Commercial Plumbing NJ | NJ | $13.6M | $4.03M | ~30% | Construction | HARD-REJECT | Construction excluded |
| Synergy BB | Women's Health OB/GYN FL | FL | $6.58M | $3.38M | ~51% | Healthcare | HARD-REJECT | Physician practice excluded |
| Synergy BB | Precision Machine Shop AZ | AZ | $7.5M | $2.3M | ~31% | Manufacturing | HARD-REJECT | Capital-intensive mfg + below floor |
| Synergy BB | Telecom Caller Trust Platform | US | $2.71M | $1.61M | ~59% | Telecom SaaS | HARD-REJECT | ARR below $3M floor (disclosed-fails) |
| Synergy BB | Ethanol Producer India | India | $10.5M | $3M | ~29% | Manufacturing | HARD-REJECT | Geography (non-US) + capital-intensive mfg |
| Synergy BB | Industrial Minerals Peru | Peru | $7M | $4.5M | ~64% | Manufacturing/distribution | HARD-REJECT | Geography (non-US) + capital-intensive mfg |
| Synergy BB | Renovation Design and Build NY | NY | $8.5M | $2.34M | ~28% | Construction | HARD-REJECT | Construction excluded |
| Synergy BB | Garment Manufacturing Bangladesh | Bangladesh | $12.5M | $1.95M | ~16% | Manufacturing | HARD-REJECT | Geography (non-US) + capital-intensive mfg |
| Synergy BB | Railroad Construction MO | MO | $7.83M | $1.5M | ~19% | Construction/transport | HARD-REJECT | Construction excluded |
| Synergy BB | B2B Health & Beauty Ingredient Mfr Dubai | UAE | $3.09M | $2.25M | ~73% | Manufacturing | HARD-REJECT | Geography (non-US) + capital-intensive mfg |
| Synergy BB | Specialty Copper Alloy Wires India | India | $20M | $2M | ~10% | Manufacturing | HARD-REJECT | Geography (non-US) + capital-intensive mfg |
| Synergy BB | Travel and Tourism Saudi Arabia | Saudi Arabia | $7.94M | $2.95M | ~37% | Travel services | HARD-REJECT | Geography (non-US) + below floor |
| Synergy BB | Admissions Consulting US Remote | US (remote) | $2M | $1.3M | ~65% | Education consulting | HARD-REJECT | Revenue below $10M floor |
| Synergy BB | Pediatric Practice NY | NY | $5.83M | $1.65M | ~28% | Healthcare | HARD-REJECT | Physician practice excluded |
| Synergy BB | Utility Support Construction NY | NY | $12M | $2M | ~17% | Construction | HARD-REJECT | Construction excluded |
| Synergy BB | Midwest Trucking & Transportation Brokerage | Midwest | $9M | $1.65M | ~18% | Transportation/brokerage | HARD-REJECT | Revenue below $10M floor |
| Synergy BB Real Estate | Event Rental Company FL | FL | $1.63M | $486K | ~30% | Event rental services | HARD-REJECT | Revenue below $10M floor + EBITDA below floor |
| Synergy BB Real Estate | Short-Term Rental Property Mgmt Midwest | Midwest | $3.23M | $371K | ~11% | STR property mgmt | HARD-REJECT | Revenue below floor + STR not on Estate Mgmt corpus |
| Website Closers | Award Winning Marketing & PR Agency | undisclosed | undisclosed | $295K (SDE) | undisclosed | Marketing services | HARD-REJECT | SDE below $1.5M EBITDA floor |
| Website Closers | Fine Jewelry eCommerce Brand | undisclosed | undisclosed | $282K (SDE) | undisclosed | B2C ecommerce | HARD-REJECT | Consumer retail/DTC excluded + below floor |
| Website Closers | AI-Driven Cybersecurity Ed-Tech Platform | undisclosed | undisclosed | $779K (SDE) | undisclosed | Cybersecurity EdTech SaaS | HARD-REJECT | SDE/EBITDA below floor |
| Website Closers | Sales Coaching & Lead Generation Platform | undisclosed | undisclosed | $109K (SDE) | undisclosed | Training SaaS | HARD-REJECT | SDE below floor |
| Website Closers | Amazon FBA eCommerce Brand | undisclosed | undisclosed | $955K (SDE) | undisclosed | B2C ecommerce | HARD-REJECT | Consumer retail/DTC excluded + below floor |
| Website Closers | AI-Native SEO & Content Marketing Agency | undisclosed | undisclosed | $121K (SDE) | undisclosed | Marketing services | HARD-REJECT | SDE below floor |
| Website Closers | Authenticated Collectibles eCommerce | undisclosed | undisclosed | $259K (SDE) | undisclosed | B2C ecommerce | HARD-REJECT | Consumer retail/DTC excluded |
| Website Closers | Lead Gen & Performance Marketing Agency | undisclosed | undisclosed | $847K (SDE) | undisclosed | Marketing services | HARD-REJECT | SDE below floor |
| Website Closers | Shopify Business Brokerage | undisclosed | undisclosed | $2.4M (SDE) | undisclosed | Brokerage services | HARD-REJECT | Service brokerage, no thesis fit |

## Source Scorecard

One row per Active or Weak (web-scannable) source on the Sourcing Sheet. Intel-only sources scanned for tombstone signal are also rowed.

| Source | Category | Status | HTTP | Listings Reviewed | Matches | Last Match Date |
|--------|----------|--------|------|-------------------|---------|-----------------|
| BizBuySell | General | blocked (verified) | 403 | 0 | 0 | — |
| Business Exits | General | active | 200 | 30 | 0 | — |
| DealForce | General (email-only) | active (email-only) | n/a | 0 | 0 | — |
| Empire Flippers | General | active | 200 | 4 (B2B-relevant); 21 consumer-ecom listings skipped per [[memory/feedback_b2b_b2b2c_ok_no_b2c]] | 0 | — |
| Everingham & Kerr | General (email-only) | active (email-only — 0 per-deal extractions in window) | n/a | 0 | 0 | — |
| Flippa | General (email-only) | blocked (verified) — web JS-shell; email digests consumer-only this window | 403 (web) / n/a (email) | 0 | 0 | — |
| IAG M&A Advisors | General (email-only) | active (email-only — 0 new in window) | n/a | 0 | 0 | — |
| Quiet Light | General (email-only) | blocked (verified) — Cloudflare; email digest 0 new in window | 403 | 0 | 0 | — |
| Rejigg | General (email-only) | active (email-only — 0 new in window) | n/a | 0 | 0 | — |
| SMB Deal Hunter (Helen Guo) | General (email-only) | active (email-only — 0 new in window) | n/a | 0 | 0 | — |
| Synergy Business Brokers | General | active | 200 | 20 | 0 | — |
| Viking Mergers | General (email-only) | active (email-only — 0 new in window) | n/a | 0 | 0 | — |
| Website Closers | General | active | 200 | 12 | 0 | — |
| GP Bullhound | Niche-Specific (Vertical SaaS) | active (intel — tombstones only) | 200 | 0 active listings (6 tombstones reviewed; no SaaS deal flow surfacing for Luxury VSaaS corpus) | 0 | — |
| PCO Bookkeepers | Niche-Specific (Pest) | active (intel — no deal content on home/newsletter today) | 200 | 0 | 0 | — |
| Sica Fletcher | Niche-Specific (Insurance) | active (intel — 5 tombstones reviewed; all sold to consolidators, no active listings to surface) | 200 | 0 active listings | 0 | — |
| Software Equity Group | Niche-Specific (Vertical SaaS) | active (intel — completed transactions only, no public marketplace) | 200 | 0 active listings | 0 | — |
| Synergy BB Real Estate | Niche-Specific (Estate Mgmt) | active | 200 | 2 | 0 | — |
| Tyton Partners | Niche-Specific (Vertical SaaS) | weak (intel — 3 EdTech tombstones; not Luxury VSaaS corpus) | 200 | 0 active listings | 0 | — |
| Exit Strategies Group | Niche-Specific (Estate Mgmt) | weak — no listings displayed; advisor-only | 200 | 0 | 0 | — |
| Cetane | Niche-Specific (Pest) | blocked (verified) — Cloudflare-gated to scraper | 403 | 0 | 0 | — |
| MidCap Advisors | Niche-Specific (Art Storage) | intel-only (scanned for tombstone signal; no recent dated releases) | 200 | 0 | 0 | — |
| Agency Checklists | Niche-Specific (Insurance) | intel-only (scanned for signal; 3 May 2026 NE acquisitions to consolidators) | 200 | 0 | 0 | — |
| Calder Capital | Niche-Specific (Cleaning) | not yet scanning | n/a | 0 | 0 | — |
| Green Bridge Advisors | Niche-Specific (Cleaning) | not yet scanning | n/a | 0 | 0 | — |
| Keystone Business Advisors | Niche-Specific (Pest) | pending decision | n/a | 0 | 0 | — |
| Union Square Advisors | Niche-Specific (Vertical SaaS) | not yet scanning | n/a | 0 | 0 | — |
| Anticimex US | Niche-Specific (Pest) | intel-only (strategic acquirer; blacklist signal not source) | n/a | 0 | 0 | — |
| CMM Online | Niche-Specific (Cleaning) | intel-only (industry publication) | n/a | 0 | 0 | — |
| IA Magazine | Niche-Specific (Insurance) | intel-only (trade publication) | n/a | 0 | 0 | — |
| Inside Self-Storage | Niche-Specific (Art Storage) | intel-only (trade publication) | n/a | 0 | 0 | — |
| MarshBerry | Niche-Specific (Insurance) | intel-only (relationship-gated) | n/a | 0 | 0 | — |
| Reagan Consulting | Niche-Specific (Insurance) | intel-only (relationship-gated) | n/a | 0 | 0 | — |
| Acquire.com (Gen + Niche SaaS) | Marketplace | pending G&B registration | n/a | 0 | 0 | — |
| Axial | Marketplace | pending G&B registration | n/a | 0 | 0 | — |
| Benchmark International | General (email newsletter) | registered-dormant | n/a | 0 | 0 | — |
| BizScout (DealOS) | Marketplace | pending G&B registration | n/a | 0 | 0 | — |
| FE International (Gen + Niche SaaS) | Marketplace | pending G&B registration | n/a | 0 | 0 | — |
| Kumo | Marketplace | pending G&B registration | n/a | 0 | 0 | — |
| Paine Pacific | General (direct relationships) | few public listings | n/a | 0 | 0 | — |
| Searchfunder | General (email newsletter) | pending alerts enablement | n/a | 0 | 0 | — |
| Woodbridge / Mariner | General (direct relationships) | no public listings | n/a | 0 | 0 | — |
| Private Art Advisory | Niche-Specific GAP | structural gap — no M&A-intermediated source exists | n/a | 0 | 0 | — |
| Specialty Coffee Equipment Service | Niche-Specific GAP | structural gap — no specialty advisor exists | n/a | 0 | 0 | — |

**Browser automation note:** `agent-browser` not installed on this VPS as of this run. Cloudflare/JS-shell sources (BizBuySell, Quiet Light, Cetane, USAdvisors, Flippa web) cannot be fallback-scraped. Status confirms sheet-noted "Web blocked" labels. BROWSER_AUTOMATION_UNAVAILABLE applied to these sources per Channel 1 stop hook.

## Volume Check

- Deals surfaced today: 0
- 7-day rolling average: estimated 0–0.5/day (5/18 + 5/19 DealsX leads in fingerprint store; no platform matches in recent windows)
- Target: 1–3/day — **BELOW TARGET**

US Memorial Day Monday — partial soft-explanation for the empty platform side; broker-tombstone sources don't produce active listings on holidays. Email channel cleanly empty per [[brain/context/email-scan-results-2026-05-25]]. The structural finding stands: even on a non-holiday, GP Bullhound / SEG / Tyton / MidCap / Sica Fletcher are tombstone-publishers, not active-listing sources — they do not feed daily flow. The "1–3/day" target requires more public listings from BizBuySell/Quiet Light (currently blocked, need agent-browser) OR more inbound from Searchfunder (alerts not enabled) and Acquire/Axial/BizScout (registrations pending). This run does not propose changes — daily scan only; source-stewardship proposals belong in Friday digest.
