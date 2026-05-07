---
date: 2026-04-29
deals_found: 0
sources_scanned: 15
sources_blocked_verified: 1
sources_blocked_single_attempt: 0
email_deals: 0
buy_box_source: live
---
# Deal Aggregator Scan — 2026-04-29

Morning run (full). 15 active sources scanned (12 general + 3 niche-specific). Email-only channels resolved through `email-scan-results-2026-04-29.md`, which classified zero broker blasts and zero CIMs in today's window. Web-scrape sources returned 94 listings combined (Business Exits 30, Empire Flippers 26, Synergy 20, Website Closers 13, Synergy Real Estate 5) plus Sica Fletcher's 10 completed-transaction announcements; none cleared the buy-box gate against an active niche.

## Niche Corpus Resolution

| # | Niche | Corpus path |
|---|---|---|
| 1 | Premium Pest Management | DealsX keywords (Specialty Pest & Environmental Mgmt Services) |
| 2 | Private art advisory firms | WR row enrichment (Niche Hypothesis + Quick notes — DealsX blank) |
| 3 | Estate Management Companies | DealsX keywords (Estate Management Companies) |
| 4 | Specialty Coffee Equipment Service | DealsX keywords (Specialty Commercial Equipment Services) |
| 5 | High-End Commercial Cleaning | DealsX keywords (High-End Commercial Cleaning) |
| 6 | Vertical SaaS for Luxury | DealsX keywords (Vertical SaaS for Luxury) |
| 7 | Specialty Insurance Brokerage (Art) | DealsX keywords (Specialty Insurance Brokerage) |
| 8 | Storage for High-Value Collections | DealsX keywords (Specialty Storage & Handling) |

## Deals Surfaced (sent to Slack individually)

None today.

## Email Inbound Deals

None today. Per `brain/context/email-scan-results-2026-04-29.md`: 0 CIMs, 0 NDAs, 0 LOIs, 0 broker blasts caught the filter, 0 introductions detected.

## Near Misses (not Slacked)

- **NetSuite Native POS Software** (Synergy Business Brokers, $7.1M ask, $1.6M revenue, $1.17M EBITDA, AU/global) — vertical SaaS with mission-critical recurring revenue and embedded customers. Right structural shape for SaaS thesis. Disclosed-and-fails on ARR floor ($1.6M < $3M minimum). Worth re-scanning in 12-18 months if they re-list at higher ARR.
- **GovCon IT Firm** (Business Exits, $19.7M revenue, $3.4M EBITDA, 17% margin) — passes Services financial bands but GovCon vertical is outside the luxury thesis envelope. Buy-box pass without thesis match → not a new-niche signal worth routing to niche-intelligence (GovCon is structurally non-luxury and has heavy concentration risk).
- **Empire Flippers Listing #19 "Home (Pest Control)"** ($7.2M ask, Amazon FBA pest control products eCommerce) — keyword "pest control" hit but it's a consumer DTC eCommerce store selling pest products, not a pest service business. Hard-exclude (consumer retail/DTC).
- **Synergy Real Estate listings** — 5 listings; 3 marked Sold, 2 below $10M revenue floor (event rental $1.6M, STR property mgmt $3.2M). Estate Management niche received zero in-band flow today.

## Source Scorecard

| Source | Category | Status | HTTP | Listings Reviewed | Matches | Last Match Date |
|--------|----------|--------|------|-------------------|---------|-----------------|
| DealForce | General (Email) | active | n/a | 0 | 0 | — |
| IAG M&A Advisors | General (Email) | active | n/a | 0 | 0 | — |
| Rejigg | General (Email) | active | n/a | 0 | 0 | — |
| Everingham & Kerr | General (Email) | active | n/a | 0 | 0 | — |
| Flippa | General (Email) | active | n/a | 0 | 0 | — |
| Quiet Light | General (Email) | active | n/a | 0 | 0 | — |
| Viking Mergers | General (Email) | active | n/a | 0 | 0 | — |
| BizBuySell | General (Web) | blocked (verified) | 403 | 0 | — | — |
| Business Exits | General (Web) | active | 200 | 30 | 0 | — |
| Empire Flippers | General (Web) | active | 200 | 26 | 0 | — |
| Synergy Business Brokers | General (Web) | active | 200 | 20 | 0 | — |
| Website Closers | General (Web) | active | 200 | 13 | 0 | — |
| PCO Bookkeepers | Niche (Pest) | active | 200 | 0 | 0 | — |
| Sica Fletcher | Niche (Insurance) | active | 200 | 10 | 0 | — |
| Synergy Business Brokers Real Estate | Niche (Estate Mgmt) | active | 200 | 5 | 0 | — |

**Status notes:**
- BizBuySell `blocked (verified)` — Akamai/Edge "Access Denied" on WebFetch (403) AND on agent-browser snapshot (Reference #18.d7fd117.1777461971.2a98ad33). Two-attempt rule satisfied. Source is genuinely dark to scrapers; remains active via registered email alerts (saved-search emails).
- Email-channel sources — "Listings Reviewed" measured at the broker-blast level by email-intelligence; today's scan classified zero broker blasts as deal-bearing (BLAST=0, DIRECT=0). Each of these channels had no qualifying deal traffic in today's window — not a fetch failure.
- PCO Bookkeepers — `transactions/` page returned successfully (HTTP 200) but tombstones are image-only and not parseable by WebFetch. Zero listings extractable; manual review required for transaction details.
- Sica Fletcher — page healthy with 10 recent announcements. All 10 are completed transactions (consolidator roll-ups: ALKEME ×6, Hilb ×1, World Insurance ×1, Keystone Agency Partners ×1, Gavnat ×1) — intel signal, not deal flow. None disclose specialty in art/jewelry/marine/aviation lines required for the Art & Collectibles thesis.

## Volume Check

- Deals surfaced today: 0
- 7-day rolling average: ~0/day (4/22 fingerprint store empty since launch; no Slack matches recorded)
- Target: 1-3/day — **BELOW TARGET**

Phase 2 source-stewardship implications: web-scrape channels are returning healthy listing volume (94 listings parsed today across 4 general sources) but zero buy-box-thesis intersection. Listing populations skew construction / manufacturing / healthcare / DTC eCommerce — orthogonal to G&B's luxury-services / vertical-SaaS / specialty-insurance theses. The funnel gap is structural to the channels, not a fetch problem. Friday digest should weigh whether to retire generalist scrape sources in favor of more niche-specific advisor monitors (e.g., advance Calder Capital + Green Bridge from "Not yet scanning" → "Active" for cleaning thesis; revisit MidCap monitor cadence for storage thesis).
