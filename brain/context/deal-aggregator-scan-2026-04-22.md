---
date: 2026-04-22
deals_found: 0
platforms_scanned: 11
email_deals: 0
---
# Deal Aggregator Scan — 2026-04-22

## Active Theses (from WEEKLY REVIEW — 8 active)
1. Premium Pest Management (Luxury Hospitality) — Services
2. Private Art Advisory Firms — Services
3. Estate Management Companies — Services
4. Specialty Coffee Equipment Service — Services
5. Vertical SaaS for Luxury & High-Value Asset Service Industries — SaaS
6. High-End Commercial Cleaning — Services
7. Specialty Insurance Brokerage (Art & Collectibles) — Insurance
8. Storage & Related Services for High Value Assets — Services

## Deals Surfaced (sent to Slack individually)
Zero matches. No listing across 11 accessible sources passed a buy-box gate AND matched any of the 8 active niche keyword corpora. No buy-box-clean outliers worth routing to niche-intelligence.

## Email Inbound Deals (Channel 2)
Pending — email-scan-results-2026-04-22.md not yet written at scan time (email-intelligence 7am ET launchd job).

## Near Misses (not Slacked)

### Business Exits (30 listings reviewed)
In-band by size but off-thesis: wellness practice, construction/HVAC/plumbing/electrical, GovCon IT & ERP, aerospace parts, staffing firms, med spa, themed-props studio, commercial contractor, recruitment agency. Two California listings (property-tax consultants $6.7M rev; staffing $7.8M rev) soft-filter. Nearest-miss: "Luxury Wedding Venue" — operating hospitality = hard exclude (serving luxury hospitality is fine; operating it is not).

### Synergy BB general (20) + real estate (8)
Closest to active niche: property management cluster (VT $1.56M rev, NYC $600K rev, Ulster County $888K rev, PA $2.37M rev). All below $10M services floor. All are vacation/residential property management shops, not UHNW estate management firms (household staffing, multi-estate ops). NYC high-end renovation explicitly excluded per nyc_construction_hard_exclude memory. Short-term rental portfolio (Midwest, $3.2M rev) also below floor and wrong segment.

### Viking Mergers (65 listings)
- #1982 Luxury Travel & Lifestyle Services ($5.7M rev / $1.9M EBITDA, Remote) — closest-read to estate/concierge niche but is a travel agency, not household ops. Disclosed revenue below $10M services floor → fail.
- #1966 Yacht Brokerage ($4.8M rev) — yacht sales, not yacht-insurance brokerage; not storage. Below floor.
- #1965 Privileged Access Management SaaS ($651K rev) — horizontal security SaaS, not vertical luxury. Well below $3M ARR.
- #1987 Dumpster franchise — franchise hard-exclude.
- Everything else: construction, HVAC, medical, staffing, manufacturing, auto — off-thesis.

### Empire Flippers (3 surfaced)
All annual revenues well below $3M floor ($1.8M / $3.75M service-mix / $180K). SaaS niche mismatch (conversion-recovery ecom plugin is horizontal, not luxury-vertical).

### WebsiteClosers (14)
One hard-exclude worth naming: #9 Digital Marketing Agency — Insurance Lead Generation ($9.7M ask / $2.15M cash flow) — explicit insurance-lead-gen hard-exclude in the insurance buy-box. Remainder: ecommerce/Amazon FBA/consumer brands/construction — off-thesis.

### Sica Fletcher / Agency Checklists (intel only)
No current-year specialty-brokerage deals in art/collectibles/jewelry/wine/marine/equine/UHNW personal lines segments. Two small MA agency tombstones (Cushman→Bergeron Jan 26; MountainOne→Morey Jan 12) — neither specialty. Sica historical: Atlass yacht (2016 → Risk Strategies) and Surety Bonds LLC (Feb 2026 → Hilb) — sold, not available.

## Platform Status
- Business Exits — accessible (30 listings parsed)
- Synergy Business Brokers (general) — accessible (20 listings parsed)
- Synergy Real Estate tab — accessible (8 listings parsed, including sold)
- Viking Mergers — accessible (65 listings parsed)
- Empire Flippers — accessible (3 SaaS-filtered listings parsed)
- WebsiteClosers — accessible (14 listings parsed, page 1 of 221)
- Keystone Business Advisors — login wall, no public listings
- Exit Strategies Group (property mgmt) — marketing page only, no listings
- BizBuySell — 403 Forbidden via WebFetch; agent-browser CLI not installed on this host → logged as blocked, no fallback available this run
- Quiet Light — 403 Forbidden via WebFetch; same (no agent-browser)
- Flippa — 404 via WebFetch; same
- Sica Fletcher — accessible (intel only, no active deals)
- Agency Checklists — accessible (intel only)

## Corpus Path Used Per Niche
- Premium Pest Management — DealsX keywords
- Private Art Advisory — WR row enrichment (DealsX ref blank)
- Estate Management — DealsX keywords
- Specialty Coffee Equipment Service — DealsX keywords
- Vertical SaaS (luxury) — DealsX keywords
- High-End Commercial Cleaning — DealsX keywords
- Specialty Insurance Brokerage (Art) — DealsX keywords
- Storage for High Value Assets — DealsX keywords

## Volume Check
- Deals surfaced today: 0
- 7-day rolling average (4/16-4/22): 0.29/day (4/16=2, 4/17=0, 4/18=weekend, 4/19=weekend, 4/20=0, 4/21=0, 4/22=0)
- Target: 1-3/day — BELOW TARGET
- Diagnostic: BizBuySell + Quiet Light + Flippa (three highest-flow-sources) all blocked this run by WebFetch 403/404 and agent-browser fallback is unavailable on this host. Prior runs on 4/16 where BizBuySell WAS reachable yielded the only recent passes. Structural infrastructure gap — the three general-marketplace sources that drive 80%+ of deal flow are not currently scrapeable in this environment. Recommend: either install agent-browser CLI, or add alternate source (DealStream, MergerNetwork, Axial public boards).

## Infrastructure Notes
- agent-browser CLI not found on PATH. All JS-rendered/Cloudflare-gated sources (BizBuySell, Quiet Light, Flippa) are effectively dark without it.
- Fingerprint store: no writes today (zero passes). Store untouched.
- Slack: no webhook calls made today (zero passes). SLACK_WEBHOOK_ACTIVE_DEALS not exercised.
