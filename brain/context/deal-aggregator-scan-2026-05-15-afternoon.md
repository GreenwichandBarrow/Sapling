---
date: 2026-05-15
deals_found: 0
sources_scanned: 4
sources_blocked_verified: 2
sources_blocked_single_attempt: 0
email_deals: 0
buy_box_source: live
morning_artifact_present: true
---
# Deal Aggregator Scan — 2026-05-15 (Afternoon)

Afternoon top-up run (`--afternoon`). Lightweight rescan of email channel + time-sensitive platforms only (Rejigg, Flippa, Everingham & Kerr). Channels 1 (full broker-platform sweep) and 4 (association deal boards) skipped — morning run handled them.

Buy-box docs re-read live from Drive (Services / Insurance / SaaS, all 2026-04-21 versions, unchanged since morning). Active-niche list re-read from Industry Research Tracker WEEKLY REVIEW (8 active rows: Premium Pest, Private Art Advisory, Estate Mgmt, Specialty Coffee Equipment, High-End Commercial Cleaning, Vertical SaaS Luxury, Specialty Insurance Brokerage, Storage High-Value). DealsX keyword corpus re-read for the 7 niches with a populated `DealsX Niche` field; Private Art Advisory uses WR-row enrichment (DealsX Niche blank).

Email-scan-results-2026-05-15.md is now PRESENT on disk (was missing during 6am morning run; produced by email-intelligence 7am ET). Section 7 of that artifact lists 11 broker-BLAST listings extracted from today's inbox — all 11 processed below, fingerprint-checked (empty store → all NEW), and screened against the live buy-boxes + active-niche corpora. Zero PASSes.

Fingerprint store (`brain/context/deal-aggregator-fingerprints.jsonl`) remains empty (0 records). No cross-day dedup hits possible. Florida Med Spa appears in both morning artifact (Business Exits web scrape) and Section 7 of email-scan-results (Business Exits BLAST) — same underlying listing; logged once below with a dedup note, no Slack (HARD-REJECT regardless).

## Deals Surfaced (sent to Slack individually)

None this afternoon. 0 listings cleared both the financial gate and the industry hard-excludes with an active-niche corpus match. No Slack posts to `#active-deals`.

## Email Inbound Deals

None matching buy-box + active-niche corpus. The 11 broker-BLAST listings in email-scan-results-2026-05-15.md Section 7 were all processed (see Listings Reviewed log below). All 11 were HARD-REJECTed on industry hard-excludes (manufacturing / construction / consumer retail / DTC / B2C SaaS / healthcare / hospitality) or sub-floor financials. Zero CIM attachments today (per email-intelligence artifact). Zero NDA attachments. Zero introductions detected.

## Near Misses (not Slacked)

None this afternoon. No listing this run cleared the financial gate AND industry hard-excludes without a niche corpus match. Every listing failed on either a disclosed-and-failed financial criterion or a hard-excluded industry — i.e. all rejections were HARD-REJECT, not NEAR-MISS.

## Listings Reviewed (full log)

15 listings reviewed this afternoon: 11 from email-scan-results Section 7 (broker BLASTs that morning could not parse) + 4 surfaced on Flippa's public homepage. Sorted PASS → NEAR-MISS → FLAG → HARD-REJECT (all rows are HARD-REJECT this run).

| Source | Headline | Geo | Revenue | EBITDA | Margin | Industry | Verdict | Reject Reason |
|--------|----------|-----|---------|--------|--------|----------|---------|---------------|
| Everingham & Kerr (BLAST) | Provider of Metal Manufacturing; Precision Machining, Stamping & Tool & Die | Mid-Atlantic (state undisclosed) | $20M+ | $4.2M | ~21% | Metal Manufacturing / Precision Machining | HARD-REJECT | Industry hard-exclude (capital-intensive manufacturing); financials clear Services BB |
| Helen Guo SMB Deal Hunter (BLAST) | Commercial Glass and Glazing Contractor (asking $7.9M) | AL | $7.03M | $1.34M | ~19% | Commercial Glass & Glazing | HARD-REJECT | Below $10M Services BB rev floor (disclosed-and-failed); construction/labor-heavy field service hard-exclude |
| Helen Guo SMB Deal Hunter (BLAST) | Cabinetry Fabrication and Installation Company | AZ | undisclosed | $515K | undisclosed | Cabinetry / Building Products | HARD-REJECT | Below $1.5M Services BB EBITDA floor (disclosed-and-failed); construction/building-products hard-exclude |
| Helen Guo SMB Deal Hunter (BLAST) | Residential HVAC Service Company w/ 400+ Active Service Agreements | LA | undisclosed | $434K | undisclosed | Residential HVAC | HARD-REJECT | Below EBITDA floor; B2C residential outside B2B/B2B2C structural requirement |
| Helen Guo SMB Deal Hunter (BLAST) | Gas Station with Triple-Net McDonald's Lease | WI | undisclosed | $512K | undisclosed | Gas Station / Convenience Retail | HARD-REJECT | Below EBITDA floor; consumer retail + franchise hard-exclude |
| Helen Guo SMB Deal Hunter (BLAST) | Fully Staffed High-Volume Convenience Store | MD | undisclosed | $500K | undisclosed | Convenience Retail | HARD-REJECT | Below EBITDA floor; consumer retail hard-exclude |
| Tory @ Flippa (BLAST) | $3.5M Annual Revenue Hair Styling Brand | undisclosed | $3.5M | undisclosed | undisclosed | DTC Consumer Brand | HARD-REJECT | Below $10M Services BB rev floor; consumer retail/DTC hard-exclude |
| Tory @ Flippa (BLAST) | 96% Margin Automated Trading SaaS (10K active subscribers) | undisclosed | undisclosed | undisclosed | 96% | SaaS (consumer trading) | HARD-REJECT | B2C/prosumer SaaS hard-exclude (10K consumer subscribers); horizontal not luxury-vertical SaaS corpus |
| Tory @ Flippa (BLAST) | Video to Blog SaaS (462 active subscribers, 12K MRR) | undisclosed | $144K ARR | undisclosed | undisclosed | SaaS (horizontal content) | HARD-REJECT | Below SaaS BB ARR floor ($3M); horizontal productivity SaaS hard-exclude |
| Chuck Mullins, Quiet Light (BLAST) | 20-Year-Old Women's Health Authority Website (DR60, 15K forum posts) | undisclosed | undisclosed | undisclosed | undisclosed | Content / Media (B2C) | HARD-REJECT | Consumer retail/DTC adjacency (content site); not vertical-SaaS or services corpus |
| Jon Hainstock, Quiet Light (BLAST) | Customizable Plant Kit Brand (Q1 rev +179% YoY, 4 sales channels) | undisclosed | undisclosed | undisclosed | undisclosed | DTC Consumer Brand | HARD-REJECT | Consumer retail/DTC hard-exclude |
| Business Exits (BLAST) | Florida Med Spa and Regenerative Medicine Clinic | FL | $1.1M | undisclosed | undisclosed | Healthcare / Med Spa | HARD-REJECT | Healthcare provider hard-exclude + below floor. DEDUP: same listing logged in morning artifact (Business Exits web scrape row); no double-Slack risk (both runs HARD-REJECT, neither posted) |
| Flippa (web — homepage) | smashhaus.com (Editor's Choice, partial sale 90% equity, $298K ask) | undisclosed | $155K | $107K (~$8.9K/mo) | ~69% | SaaS / Entertainment (B2C) | HARD-REJECT | Below SaaS BB ARR floor ($3M); B2C entertainment hard-exclude |
| Flippa (web — homepage) | Subscription-based AI study platform (managed by Flippa, $165K ask) | undisclosed | undisclosed | $37.7K (~$3.1K/mo) | undisclosed | SaaS / Education (B2C) | HARD-REJECT | Below SaaS BB ARR floor; B2C/education-consumer hard-exclude |
| Flippa (web — homepage) | Soolo (Shopify App, early-stage AI product, $11K ask) | undisclosed | undisclosed | undisclosed | undisclosed | SaaS / Shopify app | HARD-REJECT | Sub-floor (asking $11K); horizontal/prosumer Shopify-app hard-exclude; operating history likely <5yr |
| Flippa (web — homepage) | 3 Gaming Websites (content/hobbies, current bid $305) | undisclosed | undisclosed | $84 ($7/mo) | undisclosed | Content / Gaming (B2C) | HARD-REJECT | Sub-floor; B2C content/hobby hard-exclude |

**Niche corpus path used (per Step 0c, re-resolved this afternoon):**
- Premium Pest Management → DealsX keywords (Specialty Pest & Environmental Management Services row)
- Private art advisory firms → WR row enrichment (DealsX Niche blank; Niche Hypothesis + Quick notes corpus)
- Estate Management Companies → DealsX keywords
- Specialty Coffee Equipment Service → DealsX keywords (Specialty Commercial Equipment Services row)
- High-End Commercial Cleaning → DealsX keywords
- Vertical SaaS for Luxury & High-Value Asset Service Industries → DealsX keywords
- Specialty Insurance Brokerage (Art & Collectibles) → DealsX keywords (Specialty Insurance Brokerage row)
- Storage & Related Services for High Value Assets → DealsX keywords (Specialty Storage & Handling for High-Value Collections row)

## Source Scorecard

Afternoon scorecard reports only the time-sensitive sources actually scanned this run (not the full source list — that was the morning run's job). Email channel = email-scan-results Section 7 parse.

| Source | Category | Status | HTTP | Listings Reviewed | Matches | Last Match Date |
|--------|----------|--------|------|-------------------|---------|-----------------|
| Email channel (email-scan-results-2026-05-15.md Section 7) | General (email) | active | — | 11 | 0 | — |
| Rejigg | General (email + searchable) | blocked (verified) | 200 + 404 | 0 | 0 | — |
| Flippa (web) | General (searchable) | active | 200 | 4 | 0 | — |
| Everingham & Kerr (web) | General (relationship/email) | blocked (verified) | 200 | 0 | 0 | — |

**Notes on blocked status:**
- **Rejigg** — `rejigg.com` returns 200 but is a gated marketplace (NDA + buyer-account required to view anonymized listings); `rejigg.com/listings` returns 404. Two attempts, both attempts confirmed gated/dark from a public-fetch posture. `blocked (verified)`. Already known per SKILL.md ("automated deal match emails + searchable" — searchable side requires buyer-tier access this VPS does not hold). Email-side carried by email-scan-results when Rejigg sends a digest; none surfaced today.
- **Everingham & Kerr** — `everkerr.com` returns 200 but homepage shows only closed-deal tombstones and a contact form; no public listings page. Email-channel BLAST already captured today's E&K listing (Metal Manufacturing, Mid-Atlantic) via email-scan-results; logged above. `blocked (verified)` for the web side, `active` via the email side (same source, two surfaces, both attempted).
- **Flippa (web)** — Public homepage IS server-rendered today (not the JS-shell pattern documented in SKILL.md). Surfaced 4 listings, all sub-floor consumer/B2C → 0 matches. Email-side BLAST (Tory @ Flippa) separately captured 3 listings via email-scan-results (counted in the 11-listing email-channel total).
- **Email channel** — Recovered the 11-listing parse that the 6am morning run could not perform (email-scan-results artifact was missing then; produced at 7am by email-intelligence). All 11 logged above. Zero PASSes — today's BLAST volume skews construction / consumer retail / DTC / B2C SaaS / healthcare-provider, all hard-excluded.
- **Last Match Date** column shows `—` because the fingerprint store remains empty (0 records ever).

## Volume Check

- Deals surfaced this afternoon: 0
- Deals surfaced today (morning + afternoon combined): 0
- 7-day rolling average: 0 (fingerprint store empty)
- Target: 1-3/day — BELOW TARGET

Drivers (afternoon-specific):
1. Today's broker-BLAST inbox composition (E&K, Helen Guo, Tory @ Flippa, Quiet Light × 2, Business Exits) is dominated by manufacturing / construction / consumer-retail / DTC / B2C-SaaS / healthcare-provider listings — all sit on the Services / SaaS BB hard-exclude lists. None of the 11 BLAST listings hit an active-niche corpus.
2. Time-sensitive web platforms: Rejigg (gated) and E&K (no public listings) remain dark from a public-fetch posture; Flippa (web) is open but its inventory is consumer/B2C-SaaS sub-floor.
3. No CIM, no NDA, no introductions in today's inbox per email-intelligence artifact.
4. Combined day yields 0 PASS / 0 NEAR-MISS across morning + afternoon — calibration signal: when the BLAST distribution skews consumer/construction/healthcare on a given day, the 1-3/day target is structurally unreachable from the public + email surface alone. Niche-Specific channels (Channel 3) and Channel 4 association boards remain the volume gap; afternoon spec correctly excludes them, but the morning run's Channel 3 coverage today (Sica Fletcher, GP Bullhound, Synergy BB Real Estate) yielded only intel-tombstones.
