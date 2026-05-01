---
date: 2026-05-01
deals_found: 0
sources_scanned: 15
sources_blocked_verified: 2
sources_blocked_single_attempt: 0
email_deals: 0
buy_box_source: live
email_scan_results_status: missing
---

# Deal Aggregator Scan — 2026-05-01

## Deals Surfaced (sent to Slack individually)

None today.

## Email Inbound Deals

None today. `brain/context/email-scan-results-2026-05-01.md` not yet written at scan time (email-intelligence runs at 7am ET, deal-aggregator at 6am ET — Channel 2 will be re-read on the 2pm afternoon top-up run if scheduled).

## Near Misses (not Slacked)

- **Business Exits #6 — GovCon IT Firm (Judiciary & VA Contracts)** | $19.7M revenue / $3.4M EBITDA / Service+SaaS → Passes Services buy-box financials, but GovCon vertical is not on G&B active thesis list AND carries contract-concentration risk that conflicts with the recurring-revenue moat criterion. Logged as new-niche signal; not promoted given thesis distance.
- **Business Exits #7 — B2B Experiential Marketing Vendor** | $14.3M revenue / $3.3M EBITDA / Service → Passes Services buy-box financials. Marketing-services is event/project-cycle revenue (not recurring service contracts) and not luxury-aligned. Not promoted.
- **Business Exits #12 — Government Contract ERP Service Business** | $14.0M revenue / $2.6M EBITDA / Service+SaaS → Same GovCon concentration concern as #6.
- **Business Exits #3 — California Property Tax Consultants** | $6.7M rev / $4.7M EBITDA → Below $10M revenue floor + California soft flag. Strong margins but fails revenue gate.
- **Business Exits — broad rejection cluster** | 18 of 30 listings hit Services hard-excludes (construction/labor-heavy: 8; healthcare provider-owned: 4; franchise: 2; restaurants/hospitality: 2; capital-intensive manufacturing: 2). 6 below revenue floor.
- **Empire Flippers — full marketplace (22 listings reviewed)** | All Amazon FBA / DTC eCommerce / digital media — Services hard-exclude (consumer retail/DTC). One AI-content SaaS at $50K MRR ($600K ARR) fails SaaS $3M ARR floor.
- **Synergy Real Estate (8 listings)** | 6 of 8 marked SOLD. Active 2: Florida event rental ($1.6M rev, hospitality-adjacent) + Midwest STR property mgmt ($3.2M rev, vacation-rental ops not HNW estate management). Both below revenue floor and outside Estate Management thesis (HNW/UHNW recurring retainer model).
- **Website Closers (13 listings)** | All eCommerce / digital / horizontal SaaS / hospitality — hard-excludes or thesis miss.
- **Sica Fletcher** | 5 announced deals from Feb 2026 (ALKEME ×3, Hilb Group ×1, World Insurance Associates ×1) — all consolidator-acquired insurance brokers (PE-consolidator hard-exclude). Market-intel signal (consolidator activity in MA/FL/GA/MD/NY), not for-sale deal flow.
- **Flippa marketplace** | Web-fetched via agent-browser — overwhelmingly DTC/digital. Single SaaS surfaced ($60K ARR India education) below buy-box floor.

## Source Scorecard

| Source | Category | Status | HTTP | Listings Reviewed | Matches | Last Match Date |
|--------|----------|--------|------|-------------------|---------|-----------------|
| Business Exits | General | active | 200 | 30 | 0 | — |
| Empire Flippers | General | active | 200 | 22 | 0 | — |
| Synergy Business Brokers | General | active | 200 | 0 | 0 | — |
| Website Closers | General | active | 200 | 13 | 0 | — |
| BizBuySell | General | blocked (verified) | 403 | 0 | — | — |
| Flippa | General | active | 200 | 22 | 0 | — |
| Quiet Light | General | blocked (verified) | 403 | 0 | — | — |
| DealForce | General (email-alerts) | active | — | 0 | 0 | — |
| IAG M&A Advisors | General (email-alerts) | active | — | 0 | 0 | — |
| Rejigg | General (email-alerts) | active | — | 0 | 0 | — |
| Everingham & Kerr | General (email-only) | active | — | 0 | 0 | — |
| Viking Mergers | General (email-only) | active | — | 0 | 0 | — |
| PCO Bookkeepers | Niche-Specific (Pest) | active | 200 | 0 | 0 | — |
| Sica Fletcher | Niche-Specific (Insurance) | active | 200 | 5 (announcements) | 0 | — |
| Synergy Real Estate | Niche-Specific (Estate Mgmt) | active | 200 | 8 | 0 | — |

**Notes on this run:**
- Email-channel sources (DealForce, IAG, Rejigg, Everingham & Kerr, Viking Mergers) show `Listings Reviewed: 0` because `email-scan-results-2026-05-01.md` did not exist at 6am ET scan time. email-intelligence's 7am ET fire will write today's artifact — Channel 2 inbound will land on the next pass (afternoon run or tomorrow morning).
- BizBuySell verified blocked via two `agent-browser` fetch attempts, both returning "Access Denied" page (Akamai/Cloudflare bot mitigation on `/businesses-for-sale/?industry=cleaning-business` and bare `/businesses-for-sale/`).
- Quiet Light verified blocked — agent-browser fetch returned Cloudflare "Performing security verification" challenge page; consistent with Sourcing Sheet status "Web blocked (Cloudflare)".

**Niche corpus path used (per `feedback_no_search_fund_language_intermediaries` calibration trail and Step 0c stop-hook requirement):**
- Premium Pest Mgmt → DEALSX keywords (`Specialty Pest & Environmental Management Services` row)
- Private Art Advisory → WR row enrichment (Niche Hypothesis + Quick notes — DEALSX blank, structural-gap niche)
- Estate Mgmt → DEALSX keywords (`Estate Management Companies` row)
- Specialty Coffee Equipment Service → DEALSX keywords (`Specialty Commercial Equipment Services` row)
- High-End Commercial Cleaning → DEALSX keywords (`High-End Commercial Cleaning` row)
- Vertical SaaS for Luxury → DEALSX keywords (matching row)
- Specialty Insurance Brokerage (Art) → DEALSX keywords (`Specialty Insurance Brokerage` row)
- Storage for High-Value Assets → DEALSX keywords (`Specialty Storage & Handling for High-Value Collections` row)

## Volume Check

- Deals surfaced today: 0
- 7-day rolling average: 0.0/day (artifacts present for 4/28, 4/29 only — both 0; 4/24-4/27 + 4/30 missing, treated as 0 for divisor)
- Target: 1-3/day — **BELOW TARGET**

Persistent zero-volume pattern: 5 consecutive scan days (across the 4/22 fingerprint-store creation through 5/1) with zero matches surfaced. Friday digest (`com.greenwich-barrow.deal-aggregator-friday.plist`) will surface this for retirement/source-coverage-expansion review.
