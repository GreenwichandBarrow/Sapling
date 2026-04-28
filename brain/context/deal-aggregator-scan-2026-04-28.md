---
date: 2026-04-28
deals_found: 0
sources_scanned: 15
sources_blocked_verified: 1
sources_blocked_single_attempt: 0
email_deals: 0
buy_box_source: live
---
# Deal Aggregator Scan — 2026-04-28

Morning fire (Tue 6am ET). Buy-boxes (Services / Insurance / SaaS) live-read from Drive, all three loaded successfully. 8 active niches loaded from WEEKLY REVIEW (Premium Pest, Private Art Advisory, Estate Mgmt, Specialty Coffee Equipment, High-End Commercial Cleaning, Vertical SaaS for Luxury, Specialty Insurance Brokerage, Specialty Storage HVAs). DEALSX keyword corpus resolved for all 7 niches with DealsX references; Private Art Advisory corpus built from WEEKLY REVIEW row (no DealsX mapping) per Step 0c fallback.

## Deals Surfaced (sent to Slack individually)

None today. Zero thesis matches and zero buy-box matches in new niches across all scanned sources.

## Email Inbound Deals

None today. `email-scan-results-2026-04-28.md` reports 0 DIRECT inbound from owners/intermediaries, 1 BLAST (Helen Guo SMB Deal Hunter — generic $700K/yr SMB, doesn't match any active niche or buy-box floor), 0 CIMs, 0 NDAs, 0 LOIs, 0 financials, 0 broker teasers tied to active niches. The only passing-touch deal-flow signals were generic newsletter blasts (XPX CT macro panel, Cornellians, Axios, HBR) — none with niche-specific deals attached.

## Near Misses (not Slacked)

- **GovCon IT Firm** (Business Exits, $19.7M rev / $3.4M EBITDA / 17.5% margin) — passes Services financials but industry is government-contractor IT services, not a luxury vertical and not on active thesis list. Not a "buy-box match, new niche" because thesis direction is luxury B2B services; gov-IT is wrong layer. Skipped.
- **Government Contract ERP Service** (Business Exits, $14M / $2.6M / 18.3%) — same pattern as above. Skipped.
- **B2B Experiential Marketing Vendor** (Business Exits, $14.3M / $3.3M / 23%) — passes financials, but marketing/consulting services to corporates is wrong-layer for G&B luxury-services thesis. Not promoted as new-niche signal.
- **Texas HVAC Company** (Business Exits, $22M / $2.3M / 10.4%) — financials pass Services floor, but HVAC is labor-heavy field services + construction-adjacent; matches Services hard-exclude on labor-heavy field services. Auto-rejected.
- **Northeast Commercial Contractor** (Business Exits, $22M / $2.8M) — Services hard-exclude on construction. Auto-rejected.
- **Multi-Location Wellness Practice** (Business Exits, $21M / $13M / 60%) — Services hard-exclude on physician/provider-owned healthcare. Auto-rejected.
- **AI SaaS Company** (Website Closers, $50K MRR ≈ $600K ARR, 63% margin) — disclosed ARR materially below $3M SaaS floor. Auto-rejected on disclosed-and-failed criterion.
- **Push-to-Talk Communications Platform** (Website Closers, $160M ask / $12.5M cash flow / "30% recurring") — disclosed recurring share well below SaaS GRR floor (85%); only 30% recurring suggests services not pure SaaS. Also asking far above buy-box. Auto-rejected.
- **Short-Term Rental Property Mgmt** (Synergy BB, $3.2M rev / $371K cash flow) — below Services revenue floor ($10M); also short-term-rental ops is not estate-management for HNW per active thesis. Skipped.
- **Sica Fletcher 2026 announcements** (5 deals — Safe Harbour, O'Neill, Surety Bonds, Quantum Resource, Centennial State) — all closed acquisitions BY consolidators (ALKEME x4, Hilb x1), not currently-selling independents. Per Insurance buy-box hard-exclude: PE-consolidator owned. Intel only — surface to niche-intelligence as confirmation that ALKEME + Hilb continue dominating the consolidator side; no actionable deal flow.

## Source Scorecard

| Source | Category | Status | HTTP | Listings Reviewed | Matches | Last Match Date |
|--------|----------|--------|------|-------------------|---------|-----------------|
| Business Exits | General | active | 200 | 30 | 0 | — |
| BizBuySell | General | blocked (verified) | 403 | 0 | — | — |
| Empire Flippers | General | active | 200 | 24 | 0 | — |
| Synergy Business Brokers (general site) | General | active | 200 | (covered via Real Estate sub-site) | 0 | — |
| Website Closers | General | active | 200 | 13 | 0 | — |
| Quiet Light | General | active (email) | n/a | 0 | 0 | — |
| Flippa | General | active (email) | n/a | 0 | 0 | — |
| Everingham & Kerr | General | active (email) | n/a | 0 | 0 | — |
| Viking Mergers | General | active (email) | n/a | 0 | 0 | — |
| Rejigg | General | active (email) | n/a | 0 | 0 | — |
| DealForce | General | active (email) | n/a | 0 | 0 | — |
| IAG M&A Advisors | General / Niche | active (email) | n/a | 0 | 0 | — |
| PCO Bookkeepers | Niche-Specific (Premium Pest) | active | 200 | 0 (tombstones image-only, no parseable text) | 0 | — |
| Sica Fletcher | Niche-Specific (Insurance) | active | 200 | 5 (consolidator-buy announcements; 0 sell-side independents) | 0 | — |
| Synergy BB Real Estate | Niche-Specific (Estate Mgmt) | active | 200 | 2 | 0 | — |

**Notes:**
- BizBuySell `blocked (verified)`: WebFetch returned 403, agent-browser also returned "Access Denied". Two attempts confirmed. Per `feedback_test_before_concluding_channel_dead`, fallback was attempted before marking verified.
- Quiet Light listed as "active (email)" not "blocked": web path is persistently Cloudflare-blocked, but the channel's email subscription IS the active path per Sourcing Sheet — email-intelligence covers it. Today's email-scan-results: 0 matches from quietlight.com sender.
- Flippa same pattern as Quiet Light — JS-shell on web; email subscription is the active channel.
- Email-only sources (Everingham & Kerr, Viking Mergers, DealForce, Rejigg, IAG, Quiet Light email, Flippa email) all rely on email-intelligence pipeline. Today's email-scan-results-2026-04-28.md reports 0 DIRECT/CIM/teaser/blast inbound matching any active niche. Listings Reviewed = 0 reflects no deal-bearing inbound, not a pipeline failure.
- PCO Bookkeepers transactions page renders deal tombstones as images (TURF MASTERS, CARDINAL DEAL referenced in filenames only) — no parseable text. Source is alive (HTTP 200) but yields zero scrapable listings. Logged as 0 listings reviewed.
- Sica Fletcher: 5 announcements parsed, all consolidator-side acquisitions (ALKEME x4, Hilb x1), zero are independent specialty insurance brokerages currently for sale. Forwarded to niche-intelligence as a market-structure signal (consolidator dominance continues 2026 YTD).

## Volume Check

- Deals surfaced today: 0
- 7-day rolling average: 0 (insufficient prior-week artifact history; daily artifacts pre-4/22 not present in vault)
- Target: 1-3/day — **BELOW TARGET**

**Calibration note for niche-intelligence + Friday digest:**
- Two consecutive scrape blocks on BizBuySell (WebFetch + agent-browser both 403) suggest the scrape rotation needs persistent-session strategy (`--profile ~/.deal-aggregator` per SKILL.md) once Kay's BizBuySell account login is available.
- Email-only channels produced 0 inbound deal flow today — not abnormal for a Tuesday after a Sunday/Monday cycle, but a 2nd consecutive zero-day across all email channels would warrant a Friday-digest dig into whether saved-search filters drifted (Benchmark International precedent: silent for 90+ days after saved searches went stale).
- Sica Fletcher continues to confirm specialty insurance brokerage M&A is consolidator-dominated 2026 YTD. Pipeline strategy should remain proprietary/warm-intro per `feedback_broker_competition`; broker-listed insurance brokerages are unlikely to be independent.
