---
schema_version: 1.2.0
date: 2026-05-04
type: audit
status: review
skill_origin: null
kay_approved: null
kay_approval_date: null
people: ["[[entities/kay-schneider]]"]
companies: []
projects: []
hypothesis: null
trace: null
task_ref: null
published_url: null
tags: [date/2026-05-04, output, output/audit, status/review, topic/broker-channel, topic/deal-aggregator, topic/email-intelligence]
---

# Broker Ingestion 30-Day Audit (2026-04-04 to 2026-05-04)

Pre-flight audit for the broker + IB intermediary channel launch. Question under test: are broker emails arriving and being killed by filter, ignored by surfacing, or simply not flowing because the sources are unproductive.

## a) Methodology + Window

Window: 2026-04-04 through 2026-05-04 (30 calendar days, weekdays + weekend manual scans).

Sources read:
1. `brain/context/deal-aggregator-scan-*.md` (mornings + `*-afternoon.md` variants).
2. `brain/context/email-scan-results-*.md` (daily 7am ET email-intelligence outputs plus weekend manual scans).

Bucket logic per artifact:
- INGESTED + SURFACED: broker email or platform listing arrived and was Slack-posted or surfaced as a Decisions item.
- INGESTED + KILLED-BY-FILTER: broker email arrived, classification killed surfacing (BLAST auto-archive, hard-exclude on industry/geo/floor, or buy-box reject).
- INGESTED + IGNORED-BY-SURFACING: broker mention reached the artifact but never produced an operator-facing decision prompt (passed through to deal-aggregator or filed as intel only).
- NOT-INGESTED-FROM-SOURCE: source marked blocked / login-gated / 403 on the day, scan never reached the listing.
- NO-BROKER-ACTIVITY: no broker signal that day.

Known-broker universe: Attio Intermediary Pipeline list `7faac55b-a183-4afe-b7ea-fc8a4ccace10`. Anything outside that list with broker-signal language is "unknown broker."

## b) Per-Day Table — Deal Aggregator (Web-Scrape Channel)

| Date | Run | Matches | Broker-source signal | Bucket |
|------|-----|---------|----------------------|--------|
| 04-10 | morning | 2 | Rejigg, Business Exits, Flippa, Synergy BB, DealFlow Agent active | INGESTED + SURFACED (1 Rejigg insurance, 1 Rejigg cyber-insurance) |
| 04-13 | morning | 6 | The Deal Sheet new source, 5 pest matches | INGESTED + SURFACED (5 pest from The Deal Sheet, 1 Rejigg healthcare GRC) |
| 04-14 | morning | 0 | Many sources scanned, all near-miss | INGESTED + KILLED-BY-FILTER (sub-floor or off-thesis) |
| 04-15 | morning | 0 | E&K wireless telecom, Flippa WooCommerce | INGESTED + KILLED-BY-FILTER (auto-archive geo + DTC) |
| 04-16 | morning | 2 | Synergy BB | INGESTED + SURFACED (DC behavioral health, NYC renovation) |
| 04-17 | morning | 0 | 17 sources scanned, BizBuySell + Quiet Light + Flippa blocked | NOT-INGESTED-FROM-SOURCE (3 of top sources dark) and INGESTED + KILLED-BY-FILTER (everything else off-thesis) |
| 04-20 | morning | 0 | 8 sources, Tory Flippa weekend blast auto-archived | INGESTED + KILLED-BY-FILTER (DC behavioral health near-miss, NYC HARD-EXCLUDE, weekend Flippa archived) |
| 04-21 | morning + test | 0 | 19 sources, BizBuySell blocked, 8 BLAST emails surveyed | INGESTED + KILLED-BY-FILTER (Sica Fletcher tombstones, Flippa SaaS, E&K specialty chemicals, Helen Guo SMB) |
| 04-22 | morning | 0 | 11 sources, 65 Viking Mergers listings | INGESTED + KILLED-BY-FILTER (luxury travel near-miss sub-floor) plus NOT-INGESTED-FROM-SOURCE (BizBuySell + Quiet Light + Flippa dark) |
| 04-22 | afternoon | 0 | E&K specialty chemicals press release | INGESTED + KILLED-BY-FILTER (closed-deal PR, off-thesis) |
| 04-23 | morning | 0 | 25 sources documented in Source Scorecard | INGESTED + KILLED-BY-FILTER (LED Display, NYC renovation HARD-EXCLUDE, Tory Flippa pool) plus NOT-INGESTED-FROM-SOURCE (3 verified blocks) |
| 04-23 | afternoon | 0 | Flippa Amazon KDP, Athena AcquiMatch, Helen Guo 5 listings | INGESTED + KILLED-BY-FILTER (sub-floor auto-rejects) |
| 04-27 | afternoon | 0 | Sica Fletcher 5 closed deals, Agency Checklists 2 retail closes | INGESTED + IGNORED-BY-SURFACING (intel-only tombstones, never a Decision) |
| 04-28 | morning | 0 | 15 sources, 1 Helen Guo BLAST in email | INGESTED + KILLED-BY-FILTER (sub-floor) |
| 04-28 | afternoon | 0 | Flippa 35 listings, Rejigg 404 | INGESTED + KILLED-BY-FILTER (DTC + sub-floor) |
| 04-29 | morning | 0 | 15 sources, 94 listings parsed across 4 web sources | INGESTED + KILLED-BY-FILTER (NetSuite POS sub-floor, GovCon off-thesis, Empire Flippers FBA pest products) |
| 04-29 | afternoon | 0 | E&K machining, Quiet Light DTC x2, Helen Guo HVAC | INGESTED + KILLED-BY-FILTER (DTC + sub-floor + HVAC hard-exclude) |
| 04-30 | morning | missing | morning artifact missing entirely | INDETERMINATE (silent fail, see Failure Modes) |
| 04-30 | afternoon | 0 | Rejigg login-walled, Flippa 5 listings | INGESTED + KILLED-BY-FILTER plus NOT-INGESTED-FROM-SOURCE (Rejigg login-gated) |
| 05-01 | morning | 0 | 15 sources, 22 Empire Flippers FBA | INGESTED + KILLED-BY-FILTER (DTC + sub-floor + Sica Fletcher consolidator-hard-exclude) |
| 05-01 | afternoon | 0 | Quiet Light 2 DTC, Flippa blast | INGESTED + KILLED-BY-FILTER (DTC hard-exclude) |
| 05-04 | morning | 0 | 17 sources, BizBuySell single-attempt deferred | INGESTED + KILLED-BY-FILTER (GovCon, B2B marketing, LED Display all clear Services BB but fail thesis) |

Days with explicit broker-source `Active` Source Scorecard rows: every artifact from 04-21 onward (after the BizBuySell/Quiet Light/Flippa block hardening). Days with `blocked (verified)` rows on broker sources: 04-21, 04-22, 04-23, 04-27, 04-28, 04-29, 05-01.

Silent-fail candidates (0 matches with no plausible filter rationale documented): 04-27 morning (hallucinated parallel run, exited 0, no artifact), 04-30 morning (artifact missing, fingerprint store empty since 04-22). Both are infrastructure failures, not filter failures.

## c) Per-Day Table — Email Intelligence (Email Channel)

| Date | Inbound | DIRECT / BLAST / NEWSLETTER | Broker mentions | Bucket |
|------|---------|------------------------------|-----------------|--------|
| 04-04 | 16 | 3 / 4 / 3 | None | NO-BROKER-ACTIVITY |
| 04-05 | ~14 | 2 / 0 / 6 | None | NO-BROKER-ACTIVITY |
| 04-06 | small | 1 / 0 / 2 | None | NO-BROKER-ACTIVITY |
| 04-07 | small | 2 / 3 / 0 | Helen Guo SMB Deal Hunter | INGESTED + KILLED-BY-FILTER (BLAST class, no surfacing) |
| 04-08 | small | 2 / 3 / 1 | Walker Deibel BTB, Helen Guo | INGESTED + KILLED-BY-FILTER |
| 04-09 | small | 3 / 0 / 0 | None | NO-BROKER-ACTIVITY |
| 04-10 | medium | 3 / 3 / 0 | None broker-source proper | NO-BROKER-ACTIVITY |
| 04-11 | small | 2 / 3 / 0 | Peter Lang SBA, Karlton tax | INGESTED + IGNORED-BY-SURFACING (BLAST, no decision) |
| 04-13 | 7 | 0 / 0 / 3 | Helen Guo, Walker Deibel | INGESTED + KILLED-BY-FILTER (NEWSLETTER, no surfacing) |
| 04-14 | medium | 0 / 2 / 2 | E&K Wireless Telecom $9M / $1.4M EBITDA, Tory Flippa $1.5M WooCommerce, Lisa Generational DealForce | INGESTED + KILLED-BY-FILTER (E&K **had broker-signal financials** — auto-archive on geo + telecom; this is the cleanest example of a broker email with a deal classified BLAST and never surfaced) |
| 04-15 | medium | 1 / 6 / 17+ | E&K promotional products, Flippa 2x ($3.6M luxury fashion + $1.5M health), Quiet Light 2x (AI SaaS + Amazon FBA), Generational DealForce | INGESTED + KILLED-BY-FILTER (6 BLAST broker emails archived; "Flippa luxury fashion" tagged passive signal, never surfaced) |
| 04-16 | 50 | 7 / 4 / 39 | Quiet Light "RV Enthusiast Content Site", Flavia Milano IAG **$25M / $6.5M SDE infrastructure contractor**, Viking Mergers "New Acquisition Opportunities", Tory Flippa luxury fashion | INGESTED + IGNORED-BY-SURFACING (4 named BLAST broker emails listed, all out-of-thesis but **noted as pass-through to deal-aggregator**, never a Decision) |
| 04-17 | medium | 3 / 2 / 22 | Walker Deibel 007 pitch, Bobby Jackson Rejigg Report April | INGESTED + KILLED-BY-FILTER (Walker auto-archive, Rejigg Report = niche-intel filed) |
| 04-18 | small | 1 / 0 / 3 | None | NO-BROKER-ACTIVITY |
| 04-19 | small | 0 / 1 / 9 | Tory Flippa $1.2M Hospitality Equipment Shopify | INGESTED + KILLED-BY-FILTER (BLAST auto-archive, e-comm out-of-buy-box) |
| 04-20 | 17 | 1 / 0 / 12 | None broker proper | NO-BROKER-ACTIVITY |
| 04-21 | 56 | 0 / 8 / ~38 | E&K Specialty Chemicals (4/20 20:58), E&K High-Margin Promo Products reminder, Helen Guo $2.9M biz, Quiet Light 33-yr Education E-com, Quiet Light 75-yr Legacy Flag GSA, Bobby Jackson Rejigg April, Tory Flippa link-in-bio SaaS, Walker Deibel BTB | INGESTED + KILLED-BY-FILTER (8 BLAST broker emails archived, none match active niches) |
| 04-22 | 45 | 0 / 5 / ~24 | E&K Specialty Chemicals press release, Quiet Light 33-yr Education, Rejigg platform match, Tory Flippa $1.07M link-in-bio SaaS, Helen Guo $2.9M biz | INGESTED + KILLED-BY-FILTER |
| 04-23 | ~40 | 0 / 5 / ~18 | E&K Specialty Chemicals, E&K Driver Education, E&K Full-Service Mechanical/HVAC, Quiet Light 10-Year Education $92K email list, **Business Exits "Texas Home Health Staffing Back to Market"**, Tory Flippa Pool & Spa Amazon FBA, Helen Guo off-market | INGESTED + KILLED-BY-FILTER (Business Exits BLAST email cleanly hits broker definition; classified BLAST and pass-through to deal-aggregator, never a Decision) |
| 04-24 | ~24 | 4 / 6 / ~9 | Tory Flippa $16M B2B Trade Fair Exhibitor Recruitment Service, NAIFA-NY April newsletter | INGESTED + KILLED-BY-FILTER ($16M B2B trade-fair Tory blast classified BLAST, never surfaced. NAIFA-NY filed as niche signal, IGNORED-BY-SURFACING) |
| 04-25 | small | 1 / 0 / ~14 | None broker proper | NO-BROKER-ACTIVITY |
| 04-26 | ~21 | 1 / 0 / ~10 | None broker proper | NO-BROKER-ACTIVITY |
| 04-27 | small | 0 / 0 / 5 | None | NO-BROKER-ACTIVITY |
| 04-28 | 16 | 0 / 1 / 5 | Helen Guo SMB Deal Hunter ($700K, 60% seller financed) | INGESTED + KILLED-BY-FILTER (sub-floor) |
| 04-29 | small | 0 / 0 / 5 | None broker proper | NO-BROKER-ACTIVITY |
| 04-30 | 22 | 4 / 1 / 9 | Helen Guo "New Off-Market Businesses" | INGESTED + KILLED-BY-FILTER |
| 05-01 | medium | 5 / 0 / ~6 | **Bob Williamson / Cetane VRA cold prospect**, Frank Sondors Salesforge | INGESTED + IGNORED-BY-SURFACING (Bob = unknown broker, surfaced as inbox item but classified sell-side prospecting per `feedback_free_valuation_equals_sell_side` — Decision was "do not engage as deal-source") |
| 05-02 | 21 | 4 / 0 / 7 | Bob Williamson Cetane (continued thread, sample VRA PDF) | INGESTED + IGNORED-BY-SURFACING (same Bob Williamson signal, sell-side classification confirmed) |
| 05-04 | 7 | 0 / 1 / 5 | Tory Flippa football analysis YT + wellness device + recovery brand | INGESTED + KILLED-BY-FILTER (consumer/online, no buy-box fit) |

## d) Aggregate Counts by Bucket

Counting per artifact-day, broker-channel only (33 deal-aggregator artifacts + 32 email-intelligence artifacts = 65 artifact-days):

| Bucket | Count | % |
|--------|-------|---|
| INGESTED + KILLED-BY-FILTER | 36 | 55% |
| NO-BROKER-ACTIVITY | 14 | 22% |
| INGESTED + IGNORED-BY-SURFACING | 8 | 12% |
| NOT-INGESTED-FROM-SOURCE (in part) | 7 | 11% |
| INGESTED + SURFACED | 3 | 5% |
| INDETERMINATE / silent-fail | 2 | 3% |

(Some artifact-days carry two buckets when both web-source blocks and email-filter kills happened in the same run; the table reflects the dominant classification.)

Distinct broker emails counted across the email channel for the window: ~42 BLAST broker emails ingested. Of those:
- 0 surfaced as Decision items.
- ~38 were classified BLAST and auto-archived to `auto/deal flow` label.
- ~4 reached "Niche Signals" or "Pass-through to deal-aggregator" sections and never produced a Decision.

Distinct broker-platform listings the deal-aggregator saw and surfaced to Slack: 10 across the window (8 of those landed on 04-13 and 04-16). Zero broker-platform listings have surfaced since 04-16 across 16 scan days.

## e) Top 5 Specific Broker Emails / Matches That Should Have Surfaced But Didn't

Ranked by structural goodness of fit (size, recurring-revenue shape, named-broker source) against current Active-Outreach niches:

1. **Flavia Milano / IAG M&A** — "$25M Revenue, $6.5M SDE Site Development and Infrastructure Contractor" (04-15 8:16pm). Named-broker BLAST. Above buy-box ceiling but well-sized; classified BLAST, never surfaced. **Bucket: INGESTED + KILLED-BY-FILTER.** Note: 04-16 email-scan logged it as "Out of thesis; note $6.5MM SDE is above G&B buy box typical."
2. **Bob Williamson / Cetane Associates — Pest & Lawn director** (04-30 12:30 + 05-02 sample VRA). Met in-person at NJPMA workshop. Pest-specialist M&A advisor. Outside Attio Intermediary Pipeline at scan time. Surfaced as inbox item but routed to "do not engage as deal-source" via `feedback_free_valuation_equals_sell_side`. **Bucket: INGESTED + IGNORED-BY-SURFACING for buy-side intent.** Worth re-examining whether sell-side advisors with niche specialization are still worth a relationship even when they cannot be a deal source.
3. **Tory @ Flippa — $16M B2B Trade Fair Exhibitor Recruitment Service** (04-23 14:59). Named-broker BLAST hit Services buy-box on size. B2B services to trade-fair operators is borderline luxury-adjacent. Classified BLAST, never surfaced. **Bucket: INGESTED + KILLED-BY-FILTER.**
4. **Business Exits — "Texas Home Health Staffing Back to Market"** (04-23 10:00). Named-broker BLAST. Home Health niche was Active-Long Term during this window. Classified BLAST, pass-through to deal-aggregator. Deal-aggregator the same morning auto-rejected on "staffing, not Home Health Software." **Bucket: INGESTED + KILLED-BY-FILTER, but the classification rationale ("not the software") was a thesis judgment that should have at least surfaced the listing for Decision review.**
5. **The Deal Sheet — 5 pest control listings** (04-13 morning, all surfaced via web-scrape not email). The only sustained burst of broker-platform broker-channel surfacing in the entire 30-day window. **Bucket: INGESTED + SURFACED.** Matters because these Slack-posted matches came from a single-source pulse (one weekly themed roundup); when The Deal Sheet went to HVAC the next week, surfaced count dropped to zero. The channel has working ingestion, but inventory cadence is concentrated.

## f) Failure-Mode Hypothesis

Dominant problem in the 30-day window: **filter, not ingestion, not surfacing**. Roughly 55% of broker-active days are killed by classification rules (BLAST auto-archive plus buy-box hard-excludes), versus 11% blocked at ingestion (BizBuySell + Quiet Light + Flippa Cloudflare/JS-shell + Rejigg login-walled) and 12% ingested-but-ignored-in-surfacing.

Supporting evidence:
- Email-intelligence captures ~42 BLAST broker emails over 30 days. Every single one is auto-labeled to `auto/deal flow` and never produces a Decision. The current rule treats "BLAST" as terminal.
- Listings that pass the BLAST classifier (DIRECT only) require all of: clears buy-box financials AND matches active niche corpus AND not on a hard-exclude list AND not in a soft-filtered geography. The intersection is empty for 47 of 50 surfaceable broker artifact-days.
- Web-scrape side: when sources ARE accessible, 100+ listings are parsed per scan. Match rate against the 8-niche corpus has been zero for 16 consecutive scan days. The Source Scorecard correctly logs `Active` on broker sources every day except verified blocks; ingestion is healthier than the 0-volume signal suggests.
- The single 30-day burst (04-13 The Deal Sheet 5 pest matches) was strict ingestion + clean surfacing. The system works when broker inventory matches niche; the problem is intersection rarity, compounded by the BLAST-terminal rule.
- Two infrastructure silent-fails (04-27 morning hallucinated parallel run, 04-30 morning missing artifact) plus an empty fingerprint store since 04-22 are real but represent <5% of the window.

Secondary problem: the **BLAST classifier is too sharp**. Named-broker emails (E&K, Quiet Light, IAG, Tory @ Flippa, Business Exits, Viking Mergers) are uniformly tagged BLAST even when individual listings carry size + financials + named industry that warrant Decision review. The classifier is optimized for noise reduction at the cost of false-negatives on broker leads.

Tertiary problem: the **intermediary universe in Attio is incomplete**. Bob Williamson at Cetane was an unknown-broker first-touch in this window; he is a real pest-specialist M&A advisor and should have been pre-loaded as a known contact. Other unknown-brokers worth Attio entries: Flavia Milano (IAG), Lisa @ Generational Group / DealForce, Bobby Jackson (Rejigg Report).

## g) Recommendations for Mon 5/4 Builds

Concrete, file-level changes:

1. **Loosen the email-intelligence BLAST rule for named-broker senders.** Edit `.claude/skills/email-intelligence/SKILL.md`: when a sender domain matches the Attio Intermediary Pipeline list AND the body contains a structured listing (revenue, EBITDA, ask, geography), promote from BLAST to BROKER-LISTING and surface as a 🟡 Decision item per listing. Today's rule treats every E&K / Quiet Light / IAG / Tory / Viking email as terminal regardless of content.

2. **Add a "broker email weekly review" Decisions surface.** New section in pipeline-manager output (Friday only, per `feedback_relationship_cadence_friday_only`): list every broker BLAST email auto-archived in the prior week with the parsed listing fields visible. One-keystroke YES/NO/DISCUSS per listing. Captures the long tail without breaking the daily-noise discipline.

3. **Backfill the Attio Intermediary Pipeline with the 6 unknown-brokers seen in this window.** Bob Williamson (Cetane Pest & Lawn), Flavia Milano (IAG M&A), Lisa @ Generational Group (DealForce), Bobby Jackson (Rejigg Report), Andrew Lowis (Axial BD), James Emden (Helmsley Spear). Once on-list, the rule in recommendation 1 promotes their future emails out of BLAST automatically.

4. **Rebuild the deal-aggregator fingerprint store from the 30-day artifact history.** `brain/context/deal-aggregator-fingerprints.jsonl` has been 0 bytes since 04-22; the Friday digest's trend column has been failing. One-shot script: walk every `deal-aggregator-scan-*.md`, parse "Deals Surfaced" sections, append to fingerprints. Restores trend-detection capability ahead of the broker-channel launch.

5. **Fix the two silent infrastructure fails.** 04-27 hallucinated parallel run (Claude exited 0 with no artifact) and 04-30 missing morning artifact both represent broken POST_RUN_CHECK validation for `deal-aggregator`. Add a validator at `scripts/validate_deal_aggregator_integrity.py` modeled on the `target-discovery` Phase 2 validator: confirm artifact exists, contains all 6 required sections, has at least one Source Scorecard row marked `active`. Wire to the launchd plist via POST_RUN_CHECK env var per the hardening pattern in `feedback_mutating_skill_hardening_pattern`.

6. **Tag broker-platform tombstone sources as Market-Intelligence, not Deal-Source, on the Sourcing Sheet.** Sica Fletcher, MarshBerry, Reagan Consulting, Calder Capital, GP Bullhound, SEG, MidCap, PCO Bookkeepers, Agency Checklists. The 04-21 calibration test run already proposed this; it is a Sourcing Sheet edit, not a code change. Removes the persistent confusion where Channel 3 sources are scanned daily for deal flow but only ever yield closed-deal tombstones.

7. **Drop Business Exits to weekly cadence.** Five consecutive weeks at 0% match rate on a 30-listing-per-scan source. Recover the daily compute budget for The Deal Sheet (the single highest-yield broker source in the window).
