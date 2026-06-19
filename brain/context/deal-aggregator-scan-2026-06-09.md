---
date: 2026-06-09
deals_found: 0
sources_scanned: 17
sources_blocked_verified: 2
sources_blocked_single_attempt: 0
email_deals: 0
dealsx_replies: 0
broker_opportunistic: 4
email_scan_status: live
---
# Deal Aggregator Scan — 2026-06-09

Morning run (full). Buy-box docs read live from Drive. Active niches loaded from WEEKLY REVIEW. DEALSX keyword corpus loaded and resolved for all 8 active niches. Email scan was live today. Browser fallback was unavailable on JS-shell / 403 sources, so those were marked blocked rather than silently skipped.

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

None today. `brain/context/email-scan-results-2026-06-09.md` was live, but no CIMs, teaser blasts, or direct deal emails were classified.

## DealsX Proprietary Outreach Replies

None today. No DealsX lead notifications were present in the email scan artifact.

## Broker Opportunistic Review

Financially plausible broker/platform listings that do not match an active thesis corpus. Artifact-only by default; use this lane for CIO review and corpus/source tuning.
1. **GovCon IT Firm – 120+ Million in Judiciary & VA-Focused Contracts** (Business Exits) — $19.7M revenue, recurring government-contract revenue, long-term agreements. No active-niche corpus match.
2. **California Property Tax Consultants** (Business Exits) — $6.7M revenue, contingency/appeals model, recurring service signal. California soft-exclude only.
3. **California Staffing Firm with Recurring Revenue** (Business Exits) — $7.8M revenue, 80% recurring temporary/contract placements. Financially plausible broker listing; no active-niche corpus match.
4. **Texas Based Non-Emergency Medical Transport** (Business Exits) — $7.7M revenue, diverse payer mix and facility contracts. Critical service, but no active-niche corpus match.

## Near Misses (not Slacked)

- **B2B Experiential Marketing Vendor** (Business Exits) — clearly B2B, but the description reads project-heavy and recurring economics were not disclosed.

## Listings Reviewed (full log)

Every listing scraped or parsed during this run lands here as one row, regardless of verdict. This is the per-listing forensic log that makes future re-screens a fast query instead of an artifact-mining exercise.

| Source | Headline | Geo | Revenue | EBITDA | Margin | Industry | Key Signals | Verdict | Reject Reason |
|--------|----------|-----|---------|--------|--------|----------|-------------|---------|---------------|
| Business Exits | California Property Tax Consultants | California | $6,679,566 | undisclosed | undisclosed | Consulting | recurring/reoccurring revenue | BROKER-OPPORTUNISTIC | California soft-exclude only; financially plausible but off-thesis |
| Business Exits | GovCon IT Firm - 120+ Million in Judiciary & VA-Focused Contracts | undisclosed | $19,700,595 | undisclosed | undisclosed | B2B IT Services / GovCon | recurring/reoccurring revenue | BROKER-OPPORTUNISTIC | Clear recurring-contract signal, but no active niche match |
| Business Exits | California Staffing Firm with Recurring Revenue | California | $7,824,773 | undisclosed | undisclosed | Staffing Services | recurring/reoccurring revenue | BROKER-OPPORTUNISTIC | Financially plausible and recurring, but off-thesis; CA soft-flag only |
| Business Exits | Texas Based Non-Emergency Medical Transport | Texas | $7,743,083 | undisclosed | undisclosed | Healthcare / Transport | service criticality | BROKER-OPPORTUNISTIC | Critical service and recurring payer mix, but no active niche match |
| Business Exits | B2B Experiential Marketing Vendor | undisclosed | $14,277,492 | undisclosed | undisclosed | B2B Marketing Services | not disclosed | NEAR-MISS | B2B, but recurring/retention signals were not disclosed |
| Business Exits | Midwest-Based Multi-Location Wellness Practice with Exceptional Margins | Midwest | $21,313,476 | undisclosed | undisclosed | Healthcare / Wellness | not disclosed | FLAG | Healthcare/wellness provider is too ambiguous against current filters; provider-owned status not disclosed |
| Business Exits | Ireland Construction Business | Ireland | €25,000,000 | undisclosed | undisclosed | Construction | not disclosed | HARD-REJECT | Construction hard-exclude and non-US geography |
| Business Exits | Luxury Wedding Venue | undisclosed | $3,175,872 | undisclosed | undisclosed | Hospitality / Events | not disclosed | HARD-REJECT | Hospitality/event venue hard-exclude |
| Business Exits | Metal Building Supplier with US Manufacturing | undisclosed | $33,694,403 | undisclosed | undisclosed | Construction / Manufacturing | not disclosed | HARD-REJECT | Capital-intensive manufacturing and installation exposure |
| Business Exits | Growing Atlanta Area Residential Plumbing & Septic Company | Georgia | $11,706,308 | undisclosed | undisclosed | Field Services / Plumbing | service criticality | HARD-REJECT | Labor-heavy field services / construction hard-exclude |

## Source Scorecard

Every source scanned this run appears below.

| Source | Category | Status | HTTP | Listings Reviewed | Matches | Last Match Date |
|--------|----------|--------|------|-------------------|---------|-----------------|
| BizBuySell | General | blocked (verified) | 403 | 0 | 0 | — |
| Business Exits | General | active | 200 | 10 | 0 | — |
| DealForce | General | active | 200 | 0 | 0 | — |
| Empire Flippers | General | active | 200 | 0 | 0 | — |
| Everingham & Kerr | General | active | 200 | 0 | 0 | — |
| Flippa | General | active | 200 | 0 | 0 | — |
| IAG M&A Advisors | General | active | 200 | 0 | 0 | — |
| Quiet Light | General | blocked (verified) | 403 | 0 | 0 | — |
| Rejigg | General | active | 200 | 0 | 0 | — |
| SMB Deal Hunter (Helen Guo) | General | active | 200 | 0 | 0 | — |
| Synergy Business Brokers | General | active | 200 | 0 | 0 | — |
| Viking Mergers | General | active | 200 | 0 | 0 | — |
| Website Closers | General | active | 200 | 0 | 2 | 2026-06-05 |
| GP Bullhound | Niche-Specific | active | 200 | 0 | 0 | — |
| PCO Bookkeepers | Niche-Specific | active | 200 | 0 | 0 | — |
| Sica Fletcher | Niche-Specific | active | 200 | 0 | 0 | — |
| Synergy Business Brokers Real Estate | Niche-Specific | active | 200 | 0 | 0 | — |

## Volume Check

- Deals surfaced today: 0
- Broker-opportunistic review items: 4
- 7-day rolling average: 0.29/day
- Target: 1-3/day — BELOW TARGET
- Email leg: live
- Funnel bottleneck: source quality / screening strictness
