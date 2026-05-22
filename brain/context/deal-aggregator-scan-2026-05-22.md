---
schema_version: 1.1.0
date: 2026-05-22
type: output
output_type: deal-aggregator-scan
status: draft
deals_found: 0
sources_scanned: 17
sources_blocked_verified: 0
sources_blocked_single_attempt: 4
email_deals: 0
dealsx_replies: 0
buy_box_source: live
tags:
  - date/2026-05-22
  - output
  - output/deal-aggregator-scan
  - source/deal-aggregator
  - topic/deal-aggregator
  - topic/morning-briefing
---

# Deal Aggregator Scan — 2026-05-22

Morning headless run (Friday). All three buy-box docs (Services / Insurance / SaaS) read live from Drive. Active-niche corpus loaded from Industry Research Tracker WEEKLY REVIEW + DEALSX tabs. Email-scan-results-2026-05-22 read — zero broker BLAST, zero CIM, zero DealsX reply notifications. agent-browser not installed on this VPS (`command not found`) — BizBuySell / Flippa / Quiet Light scraping fell back to single-attempt curl which 403'd or returned a JS shell; surfaced as `blocked (single-attempt)` per `feedback_test_before_concluding_channel_dead`. **BROWSER_AUTOMATION_UNAVAILABLE for BizBuySell, Flippa, Quiet Light — requires `npm i -g agent-browser && agent-browser install` to recover.**

Active-niche corpus path resolution (per Step 0c stop-hook):
- Premium Pest Management → DealsX keywords (DEALSX row "Specialty Pest & Environmental Management Services")
- Private art advisory firms → **WR row enrichment** (Niche Hypothesis + Quick notes — no DealsX equivalent row)
- Estate Management Companies → DealsX keywords (DEALSX "Estate Management Companies")
- Specialty Coffee Equipment Service → DealsX keywords (DEALSX "Specialty Commercial Equipment Services")
- High-End Commercial Cleaning → DealsX keywords (DEALSX "High-End Commercial Cleaning")
- Vertical SaaS for Luxury & High-Value Asset Service Industries → DealsX keywords
- Specialty Insurance Brokerage (Art & Collectibles) → DealsX keywords (DEALSX "Specialty Insurance Brokerage")
- Storage & Related Services for High Value Assets → DealsX keywords (DEALSX "Specialty Storage & Handling for High-Value Collections")

## Deals Surfaced (sent to Slack individually)

None today.

## Email Inbound Deals

None today. Per `brain/context/email-scan-results-2026-05-22.md` §7 Broker BLAST Listings: zero inbound emails in the 2-day window matched broker-signal keywords. Zero CIMs, zero NDA-attached emails, zero broker teasers.

## DealsX Proprietary Outreach Replies

None today. Zero emails from `Prospect Geni <dealsx.notifaction@gmail.com>` in the email-scan-results 2-day window; zero forwards from `@dealsx.io`. Last DealsX reply: 2026-05-19 (Emilio Miti, per fingerprint store).

## Near Misses (not Slacked)

- **Boutique Property Management Company w/ Available Real Estate** (Synergy Real Estate) — $1.56M revenue / $299K cash flow. Property mgmt sector is adjacent to Estate Management niche (#3), but revenue is well below Services Buy Box floor ($10M – $50M) and property mgmt firms generally serve broad multi-tenant residential portfolios, not the HNW single-family / multi-estate operations the Estate Management thesis targets. HARD-REJECT, but logged as a corpus signal — if multiple sub-$5M property-mgmt firms continue appearing without matching the HNW-estate thesis, the Estate Management corpus may need tightening to keep generic property-mgmt firms out of future near-miss noise.
- **GP Bullhound `/transactions/` 404 + `/news/` 404, root 200** — niche-specific source for Vertical SaaS is structurally alive at root but no public listings path resolves. Same condition as Software Equity Group `/recent-transactions/` 404 vs `/` 200. Both are Tech / SaaS advisory firms whose deal flow is relationship-gated; the "Active" status on the Sourcing Sheet is misleading for these and should be reviewed at Friday Source Scout.

## Listings Reviewed (full log)

54 listings scraped or parsed across 4 accessible scrapable sources (Business Exits 30 / Synergy Real Estate 8 / Empire Flippers 15 / Website Closers 1). Zero PASS, zero NEAR-MISS at the buy-box gate (one corpus-adjacent NEAR-MISS noted above, but HARD-REJECT on revenue floor), 54 HARD-REJECT.

| Source | Headline | Geo | Revenue | EBITDA | Margin | Industry | Verdict | Reject Reason |
|--------|----------|-----|---------|--------|--------|----------|---------|---------------|
| Business Exits | Midwest Multilocation Wellness Practice | undisclosed | $21.3M | undisclosed | undisclosed | Wellness / healthcare | HARD-REJECT | Healthcare hard-exclude (physician practices / provider-owned) |
| Business Exits | Ireland Construction Co | Ireland | $6.7M | undisclosed | undisclosed | Construction | HARD-REJECT | Construction hard-exclude + non-US (US-only buy-box) |
| Business Exits | CA Property Tax Consultants | California | $6.7M | undisclosed | undisclosed | Property tax services | HARD-REJECT | Not on active niche list (Property Tax Appeal is rank-11 New-Pending Review, not Active); CA soft-flag |
| Business Exits | Luxury Wedding Venue | undisclosed | $3.2M | undisclosed | undisclosed | Hospitality / events | HARD-REJECT | Restaurants/hospitality/nightlife hard-exclude |
| Business Exits | Metal Building US Manufacturing | undisclosed | $19.7M | undisclosed | undisclosed | Manufacturing | HARD-REJECT | Capital-intensive manufacturing hard-exclude |
| Business Exits | GovCon IT Judiciary VA Contracts | undisclosed | $19.7M | undisclosed | undisclosed | Government IT | HARD-REJECT | No active-niche corpus match |
| Business Exits | B2B Experiential Marketing | undisclosed | $14.3M | undisclosed | undisclosed | Marketing services | HARD-REJECT | No active-niche corpus match |
| Business Exits | Non-Emergency Medical Transport | undisclosed | $7.7M | undisclosed | undisclosed | Medical transport | HARD-REJECT | Healthcare hard-exclude (provider-owned) |
| Business Exits | CA Staffing Firm Recurring Revenue | California | $7.8M | undisclosed | undisclosed | Staffing | HARD-REJECT | No active-niche corpus match; CA soft-flag |
| Business Exits | NE Commercial Contractor (Healthcare/Financial) | undisclosed | $22.0M | undisclosed | undisclosed | Construction | HARD-REJECT | Construction hard-exclude |
| Business Exits | Atlanta Area Plumbing & Septic Co | Atlanta, GA | $11.7M | undisclosed | undisclosed | Plumbing services | HARD-REJECT | No active-niche corpus match |
| Business Exits | Government Contract ERP | undisclosed | $14.0M | undisclosed | undisclosed | Vertical SaaS (govt) | HARD-REJECT | Vertical SaaS but govt vertical ≠ Luxury & High-Value Asset Service Industries thesis |
| Business Exits | Design-Build Studio (Interactive Experiential) | undisclosed | $10.0M | undisclosed | undisclosed | Design/build | HARD-REJECT | Construction hard-exclude |
| Business Exits | Texas HVAC RNC | Texas | $22.0M | undisclosed | undisclosed | HVAC | HARD-REJECT | No active-niche corpus match |
| Business Exits | Cell Phone Tower Install | undisclosed | $8.9M | undisclosed | undisclosed | Telecom construction | HARD-REJECT | Construction hard-exclude |
| Business Exits | Niche Construction Service Business | undisclosed | $10.8M | undisclosed | undisclosed | Construction | HARD-REJECT | Construction hard-exclude |
| Business Exits | Military Aerospace Parts Distributor | undisclosed | $8.2M | undisclosed | undisclosed | Aerospace distribution | HARD-REJECT | Aviation/aerospace hard-exclude per `feedback_no_aviation_targets` |
| Business Exits | Category-Defining Window Manufacturing | undisclosed | $4.9M | undisclosed | undisclosed | Manufacturing | HARD-REJECT | Capital-intensive manufacturing hard-exclude |
| Business Exits | Southeast Electrical Contractor | Southeast US | $5.3M | undisclosed | undisclosed | Electrical contractor | HARD-REJECT | Construction hard-exclude |
| Business Exits | AZ Addiction Treatment | Arizona | $4.4M | undisclosed | undisclosed | Addiction treatment | HARD-REJECT | Healthcare hard-exclude |
| Business Exits | Pet Safety Manufacturing | undisclosed | $1.7M | undisclosed | undisclosed | Manufacturing | HARD-REJECT | Capital-intensive manufacturing + below Services floor ($10M) |
| Business Exits | Nevada Fireproofing Contractor | Nevada | $3.1M | undisclosed | undisclosed | Construction | HARD-REJECT | Construction hard-exclude |
| Business Exits | Government-Contracted Promotional Products | undisclosed | $8.2M | undisclosed | undisclosed | Promotional products | HARD-REJECT | No active-niche corpus match |
| Business Exits | Recruitment Agency | undisclosed | $2.3M | undisclosed | undisclosed | Staffing | HARD-REJECT | No active-niche corpus match + below floor |
| Business Exits | Med Spa Clinic | undisclosed | $1.1M | undisclosed | undisclosed | Healthcare / med spa | HARD-REJECT | Healthcare hard-exclude + below floor |
| Business Exits | "Detx" (presumed detox) | undisclosed | $5.5M | undisclosed | undisclosed | Healthcare (presumed) | HARD-REJECT | Healthcare hard-exclude (presumed) |
| Business Exits | Restaurant Juice Bar Franchise | undisclosed | $4.1M | undisclosed | undisclosed | Franchise restaurant | HARD-REJECT | Restaurants + Franchises both hard-excluded |
| Business Exits | CO Regenerative Medicine | Colorado | $0.9M | undisclosed | undisclosed | Healthcare | HARD-REJECT | Healthcare hard-exclude + below floor |
| Business Exits | Bay Area Roofing Co | California (Bay Area) | $2.5M | undisclosed | undisclosed | Construction (roofing) | HARD-REJECT | Construction hard-exclude + CA soft-flag |
| Business Exits | TX Home Health Staffing | Texas | $2.5M | undisclosed | undisclosed | Healthcare staffing | HARD-REJECT | Healthcare hard-exclude |
| Synergy Real Estate | Event Rental Company (Full-Service) | Florida | $1.6M | $486K (CF) | ~30% | Event rental / hospitality | HARD-REJECT | Below Services floor + hospitality-adjacent |
| Synergy Real Estate | Midwest Short-Term Rental Portfolio | Midwest | $3.2M | $371K (CF) | ~11% | Real estate (STR) | HARD-REJECT | No active-niche corpus match (B2C STR) |
| Synergy Real Estate | Established Groundwater Treatment Solutions | Florida | $3.5M | $1.3M (CF) | ~37% | Environmental services | HARD-REJECT | No active-niche corpus match |
| Synergy Real Estate | Long-Established Niche Music Service Co | New Jersey | $2.3M | $284K (CF) | ~12% | Music services | HARD-REJECT | No active-niche corpus match |
| Synergy Real Estate | Boutique Property Management Co w/ RE | undisclosed | $1.6M | $299K (CF) | ~19% | Property management | HARD-REJECT | Below Services floor ($10M); property mgmt ≠ Estate Management niche (HNW single/multi-estate) |
| Synergy Real Estate | Real Estate Investment Co (Semi-Absentee) | undisclosed | $2.4M | $395K (CF) | ~17% | Real estate investment | HARD-REJECT | No active-niche corpus match |
| Synergy Real Estate | Property Management Firm For Sale (Highly Regarded) | undisclosed | $0.6M | $300K (CF) | ~50% | Property management | HARD-REJECT | Below Services floor + property mgmt ≠ Estate Mgmt niche |
| Synergy Real Estate | Real Estate Property Management Office | undisclosed | $0.9M | undisclosed | undisclosed | Property management | HARD-REJECT | Below Services floor + property mgmt ≠ Estate Mgmt niche |
| Empire Flippers | Medical News / Education Newsletter (94124) | undisclosed | $43K/mo | undisclosed | undisclosed | Digital media / newsletter | HARD-REJECT | Not vertical SaaS for luxury; B2C content business |
| Empire Flippers | Medical Subscription App (94091) | undisclosed | $30K/mo | undisclosed | undisclosed | Subscription app | HARD-REJECT | Not vertical SaaS for luxury |
| Empire Flippers | Generic SaaS Subscription (91852) | undisclosed | $26K/mo | undisclosed | undisclosed | Generic SaaS | HARD-REJECT | Horizontal/below ARR floor; not vertical luxury |
| Empire Flippers | Music YouTube Channel (94250) | undisclosed | $9K/mo | undisclosed | undisclosed | YouTube content | HARD-REJECT | B2C / not vertical SaaS |
| Empire Flippers | Sports/Entertainment YouTube (94498) | undisclosed | $2.7K/mo | undisclosed | undisclosed | YouTube content | HARD-REJECT | B2C / not vertical SaaS + below floor |
| Empire Flippers | Pet Care eCommerce (94115) | undisclosed | $1.6M/mo | $342K/mo | ~21% | Consumer retail / eCommerce | HARD-REJECT | Consumer retail / DTC hard-exclude |
| Empire Flippers | Cryptocurrency Content (90682) | undisclosed | undisclosed | undisclosed | undisclosed | Crypto content + display | HARD-REJECT | Not vertical SaaS; lending/finance-adjacent |
| Empire Flippers | Amazon FBA Pest Control Products (88177) | undisclosed | undisclosed | undisclosed | undisclosed | B2C consumer goods (pest) | HARD-REJECT | Consumer retail / DTC; not premium B2B pest mgmt thesis |
| Empire Flippers | Supplements/Beauty eCommerce (88296) | undisclosed | undisclosed | undisclosed | undisclosed | Consumer retail | HARD-REJECT | Consumer retail / DTC hard-exclude |
| Empire Flippers | Business/Digital Media (84831) | undisclosed | undisclosed | undisclosed | undisclosed | Digital media | HARD-REJECT | Not vertical SaaS; B2C content |
| Empire Flippers | Home/Romance eCommerce Amazon (83512) | undisclosed | $122K/mo | undisclosed | undisclosed | Consumer retail | HARD-REJECT | Consumer retail / DTC hard-exclude |
| Empire Flippers | Hobbies/Gaming eCommerce Amazon (91643) | undisclosed | $110K/mo | undisclosed | undisclosed | Consumer retail | HARD-REJECT | Consumer retail / DTC hard-exclude |
| Empire Flippers | Bedding Accessories Amazon FBA (87832) | undisclosed | undisclosed | undisclosed | undisclosed | Consumer retail | HARD-REJECT | Consumer retail / DTC hard-exclude |
| Empire Flippers | Listing 94170 (unclear) | undisclosed | undisclosed | undisclosed | undisclosed | undisclosed | HARD-REJECT | No active-niche corpus match in scraped fragment |
| Empire Flippers | Listing 94312 (marked sold) | undisclosed | undisclosed | undisclosed | undisclosed | undisclosed | HARD-REJECT | Already sold per listing markup |
| Website Closers | SBA Pre-Qualified Luxury RV Coach Marketplace (28-yr) | undisclosed | undisclosed | undisclosed | undisclosed | B2C marketplace (luxury RV) | HARD-REJECT | B2C marketplace; not active niche (luxury RV ≠ vertical SaaS for luxury) |

## Source Scorecard

Every source with `Status: Active` on the Sourcing Sheet (General + Niche-Specific tabs) appears below. 17 active sources surveyed.

| Source | Category | Status | HTTP | Listings Reviewed | Matches | Last Match Date |
|--------|----------|--------|------|-------------------|---------|-----------------|
| BizBuySell | General | blocked (single-attempt) | 403 | 0 | 0 | — |
| Business Exits | General | active | 200 | 30 | 0 | — |
| DealForce | General | active (email-only) | n/a | 0 | 0 | — |
| Empire Flippers | General | active | 200 | 15 | 0 | — |
| Everingham & Kerr | General | active (email-only) | n/a | 0 | 0 | — |
| Flippa | General | blocked (single-attempt) | 404 (JS shell) | 0 | 0 | — |
| IAG M&A Advisors | General | active (email-only) | n/a | 0 | 0 | — |
| Quiet Light | General | blocked (single-attempt) | 403 | 0 | 0 | — |
| Rejigg | General | active (email-only) | n/a | 0 | 0 | — |
| SMB Deal Hunter (Helen Guo) | General | active (email-only) | n/a | 0 | 0 | — |
| Synergy Business Brokers | General | active | 200 | 0 (categorical landing only) | 0 | — |
| Viking Mergers | General | active (email-only) | n/a | 0 | 0 | — |
| Website Closers | General | active | 200 | 1 | 0 | — |
| GP Bullhound | Niche-Specific (Vertical SaaS) | active (root only) | 200 root, 404 /transactions/ /news/ | 0 | 0 | — |
| PCO Bookkeepers | Niche-Specific (Premium Pest) | blocked (single-attempt) | 403 (scraper) — value is via email newsletter | 0 | 0 | — |
| Sica Fletcher | Niche-Specific (Specialty Insurance) | active | 200 | 0 (announcements page only, no current listings) | 0 | — |
| Synergy Business Brokers Real Estate | Niche-Specific (Estate Mgmt) | active | 200 | 8 | 0 | — |

**Status legend:**
- `active` — fetched successfully, listings parsed (or `0 (categorical landing only)` if the page is navigation-only).
- `active (email-only)` — surface via `email-scan-results-{date}.md`; nothing inbound today.
- `active (root only)` — homepage 200 but listings/transactions sub-path 404. Source structurally alive but no listings path; not a "blocked" verdict.
- `blocked (single-attempt)` — primary fetch failed AND fallback (agent-browser) unavailable in this environment. Per `feedback_test_before_concluding_channel_dead`, NOT promoted to `blocked (verified)` until a successful second-tool attempt confirms the dark state.

**Fingerprint store status:** `brain/context/deal-aggregator-fingerprints.jsonl` contains 2 entries (2026-05-18 DealsX St. Louis MO, 2026-05-19 DealsX Emilio Miti). No platform-source matches recorded yet — Last Match Date is `—` across the board because no listings have ever cleared the buy-box gate via these scrapable channels in the fingerprint window.

## Volume Check

- Deals surfaced today: 0
- 7-day rolling average (5/15 / 5/18 / 5/19 / 5/20 / 5/21 / 5/22 weekdays): (0 + 1 + 0 + 0 + 0 + 0) / 6 = **0.17/day**
- Target: 1–3/day
- Status: **🔴 BELOW TARGET** (sustained — five consecutive weekday zero-result morning runs since 5/19)

Below-target driver pattern: the scrapable General sources (Business Exits / Synergy / Empire Flippers / Website Closers) lean construction / healthcare / consumer-retail / digital-eCommerce — categories the buy-box hard-excludes by design. Active-niche corpus matches require either (a) niche-specific advisory output (Sica Fletcher / GP Bullhound / PCO Bookkeepers — currently silent, JS-rendered, or scraper-blocked) or (b) email-driven channels (DealForce / Rejigg / E&K / Viking) which produced nothing in the 2-day window. **Friday Source Scout (6 AM digest run) should be examined for proposed additions to widen niche-aligned coverage; sustained zero-result morning runs are the exact signal Phase 2 stewardship is built to act on.**

## BROWSER_AUTOMATION_UNAVAILABLE Footnote

agent-browser CLI not installed on this VPS (`command not found`). JS-shell and Cloudflare-gated sources (BizBuySell, Flippa, Quiet Light) fell back to single-attempt curl and surfaced as `blocked (single-attempt)`. To recover scrapability on these three sources: `npm i -g agent-browser && agent-browser install`. Until that is in place, daily scans will continue to miss the BizBuySell long tail (largest LMM broker platform) and Flippa/Quiet Light digital-niche flow.
