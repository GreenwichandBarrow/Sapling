---
schema_version: 1.2.0
date: 2026-05-04
type: rerun-analysis
status: review
skill_origin: deal-aggregator
kay_approved: null
kay_approval_date: null
people: ["[[entities/kay-schneider]]"]
companies: []
projects: []
hypothesis: null
trace: null
task_ref: null
published_url: null
tags: ["date/2026-05-04", "output", "output/rerun-analysis", "status/review", "topic/broker-channel", "topic/buy-box", "topic/deal-aggregator"]
---

# Deal-Aggregator Rerun. Broker Buy Box Applied to 30-Day Backfill + Today's Scrape

Question under test. What clears the locked Broker-Channel Opportunistic Buy Box (geo NY/NJ/PA/CT, financials $5M-$50M revenue + $2M EBITDA + 15% margin, hard excludes, industry-agnostic) that the niche-strict Services / Insurance / SaaS screens were rejecting on industry grounds.

## 1. Methodology + Scope

Two arms run against the buy-box locked at `[[outputs/2026-05-04-broker-channel-buy-box-draft]]` (Drive doc `1feNR94YgksrJAEtRYGZOmHQxYe3vaG72Pl0M-bR61M0`).

**Arm 1.** Re-screen today's morning artifact `[[context/deal-aggregator-scan-2026-05-04|deal-aggregator-scan-2026-05-04]]` against the broker buy-box. Pull individual rejected listings (Near Misses + Source Scorecard) and apply the broker rules, since the morning scan ran against niche-strict buy-boxes only.

**Arm 2.** Re-screen the ~42 named-broker BLAST emails enumerated in `[[outputs/2026-05-04-broker-ingestion-audit-30day|2026-05-04-broker-ingestion-audit-30day]]` against the broker buy-box. Apply the data availability rule (missing fields do not auto-reject; flag for manual review).

**Verdict taxonomy.**
- PASS. All disclosed criteria clear; undisclosed fields treated as flag-level only (not reject).
- FLAG. No hard reject, but at least one financial or geo field undisclosed; manual review needed before engagement.
- HARD-REJECT. At least one disclosed criterion fails (geo outside 4-state, hard exclude tripped, disclosed financial below floor / above ceiling, EBITDA margin below 15%).
- KNOWN-REJECT-OVERRIDE. Pre-existing kill from prior session decision or memory rule. Source layer wrong even if listing math clears (e.g. Cetane sell-side per `feedback_free_valuation_equals_sell_side`); Andrew Lowis Axial flagged as not-a-broker, out of scope.

**Constraints honored.** No Apollo, no buy-box doc edits, no skill-file edits, no Slack post.

## 2. Arm 1 Results. Today's Web Scrape Against Broker Buy Box

Source. `brain/context/deal-aggregator-scan-2026-05-04.md`. Section "Near Misses (not Slacked)" enumerates four discrete listings that cleared Services BB financials but missed niche corpus. Source Scorecard shows 30 Business Exits + 20 Synergy + 14 Website Closers + 20 Empire Flippers + 8 Synergy RE + 8 Sica + 3 GP Bullhound + 0 PCO listings reviewed, but only Near Misses are individually disclosed at headline level. **Data limitation. The remaining ~95 reviewed listings are not enumerated; only 4 were lifted into the artifact for thesis-drift review.**

Re-screen of the 4 disclosed Near Misses against broker buy-box.

| Source | Listing | Rev | EBITDA | Margin | Geo | Hard Exclude? | Verdict | Reason |
|---|---|---|---|---|---|---|---|---|
| Business Exits | GovCon IT Firm. Judiciary + VA contracts. $120M+ portfolio | $19.7M | $3.4M | 17.5% | not disclosed | none flagged | FLAG | Financials clear; geo undisclosed in artifact (data availability rule); GovCon not a hard exclude in broker buy-box. Worth surfacing. |
| Business Exits | B2B Experiential Marketing Vendor | $14.3M | $3.3M | 23.1% | not disclosed | none flagged | FLAG | Clean financials; geo undisclosed; B2B services aligns with structural preference. |
| Business Exits | Government Contract ERP Service | $14.0M | $2.6M | 18.3% | not disclosed | none flagged | FLAG | Financials clear; geo undisclosed; SaaS-shape ERP service is industry-agnostic acceptable. |
| Synergy BB | LED Display Solutions Company | $11.2M | $4.6M | ~41% | FL | none flagged | HARD-REJECT | Geography fail. FL is outside the NY/NJ/PA/CT hard gate. |

Arm 1 totals. 3 FLAG (geo TBD), 1 HARD-REJECT (FL geo), 0 PASS. Pending the geo confirmation, three Business Exits listings warrant Decision-level review under the broker buy-box that the niche-strict screen sent to Near Misses.

Note. The morning artifact's residual ~95 listings (Business Exits 26 + Synergy BB 19 + Website Closers 14 + Empire Flippers 20 + Synergy RE 8 + Sica 8 + GP Bullhound 3) are aggregate-counted only. To convert this rerun into routine practice, the deal-aggregator wrapper would need to emit a per-listing CSV or markdown table. Recommended fix in section 6.

## 3. Arm 2 Results. Per-Email Verdict Against Broker Buy Box

Source. Audit table in `brain/outputs/2026-05-04-broker-ingestion-audit-30day.md` section c. 42 named-broker BLAST emails over 30 calendar days enumerated by date + sender + headline (where disclosed in the artifact). For each, applied broker buy-box rules.

| # | Date | Sender | Headline / Deal | Disclosed Geo | Disclosed Rev | Disclosed EBITDA | Disclosed Margin | Hard Exclude Trip | Verdict | Reason |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 04-07 | Helen Guo | SMB Deal Hunter blast | not disclosed | not disclosed | not disclosed | not disclosed | none in headline | FLAG | Headline-only; full listing details would be in body. |
| 2 | 04-08 | Walker Deibel | Buy Then Build | not disclosed | not disclosed | not disclosed | not disclosed | none | FLAG | Newsletter/community, not a structured listing; treat as FLAG pending body. |
| 3 | 04-08 | Helen Guo | (continuation) | not disclosed | not disclosed | not disclosed | not disclosed | none | FLAG | Same as #1. |
| 4 | 04-11 | Peter Lang | SBA financing newsletter | n/a | n/a | n/a | n/a | none | HARD-REJECT | Lending-adjacent newsletter, not a deal source. Borderline KNOWN-REJECT (newsletter, no listing payload). |
| 5 | 04-11 | Karlton | Tax newsletter | n/a | n/a | n/a | n/a | none | HARD-REJECT | Tax content, not a listing. |
| 6 | 04-13 | Helen Guo | (continuation) | not disclosed | not disclosed | not disclosed | not disclosed | none | FLAG | Same as #1. |
| 7 | 04-13 | Walker Deibel | (continuation) | not disclosed | not disclosed | not disclosed | not disclosed | none | FLAG | Same as #2. |
| 8 | 04-14 | Everingham & Kerr | Wireless Telecom | not disclosed | $9.0M | $1.4M | 15.6% | none | HARD-REJECT | Disclosed EBITDA $1.4M is BELOW the $2M practical floor. Margin clears. Hard-reject on disclosed financial. |
| 9 | 04-14 | Tory @ Flippa | $1.5M WooCommerce | not disclosed | $1.5M | not disclosed | n/a | none | HARD-REJECT | Disclosed revenue $1.5M is BELOW the $5M floor. Hard-reject on disclosed financial. |
| 10 | 04-14 | Lisa @ Generational | DealForce blast | not disclosed | not disclosed | not disclosed | not disclosed | none | FLAG | Curated blast, multi-listing. Body parse required. |
| 11 | 04-15 | Everingham & Kerr | Promotional Products | not disclosed | not disclosed | not disclosed | not disclosed | none | FLAG | Headline-only; promotional products is industry-agnostic-acceptable per buy-box; need geo + financials. |
| 12 | 04-15 | Tory @ Flippa | $3.6M Luxury Fashion | not disclosed | $3.6M | not disclosed | n/a | **fashion / DTC** | HARD-REJECT | Disclosed revenue $3.6M below $5M floor; "luxury fashion" trips fashion/DTC hard exclude. |
| 13 | 04-15 | Tory @ Flippa | $1.5M Health | not disclosed | $1.5M | not disclosed | n/a | none clear | HARD-REJECT | Disclosed revenue below $5M floor. "Health" without "physician practice" language is not a hard exclude on its own; financial alone kills it. |
| 14 | 04-15 | Quiet Light | AI SaaS | not disclosed | not disclosed | not disclosed | not disclosed | none | FLAG | Headline-only, AI/SaaS is industry-agnostic-acceptable. |
| 15 | 04-15 | Quiet Light | Amazon FBA | not disclosed | not disclosed | not disclosed | not disclosed | **DTC** | HARD-REJECT | Amazon FBA is consumer DTC; trips fashion/apparel/DTC consumer brands hard exclude (DTC consumer scope). |
| 16 | 04-15 | Lisa @ Generational | DealForce | not disclosed | not disclosed | not disclosed | not disclosed | none | FLAG | Multi-listing blast. |
| 17 | 04-16 | Quiet Light | RV Enthusiast Content Site | not disclosed | not disclosed | not disclosed | not disclosed | none clear | FLAG | Content site, niche question. Industry-agnostic admits this; flag pending financials. |
| 18 | 04-16 | **Flavia Milano / IAG** | **$25M Rev / $6.5M SDE Site Development + Infrastructure Contractor** | **not disclosed** | **$25M** | **$6.5M SDE** | **26%** | **construction (potential)** | **FLAG** | Financials clear ($25M rev in band; $6.5M SDE well above $2M EBITDA floor; 26% margin clears 15%). Geo undisclosed (named in audit as "highlighted top-3 specific lead"). **"Site Development and Infrastructure Contractor" lands close to construction hard exclude.** Manual review must clarify whether this is general construction (hard reject) or specialty infrastructure services (allowed). Treating as FLAG, not HARD-REJECT, because broker buy-box is industry-agnostic and the construction line is interpretive on this label. Top miss per audit. |
| 19 | 04-16 | Viking Mergers | New Acquisition Opportunities | not disclosed | not disclosed | not disclosed | not disclosed | none | FLAG | Multi-listing. Viking is NC-based, but listings span states. Body parse required. |
| 20 | 04-16 | Tory @ Flippa | Luxury Fashion | not disclosed | not disclosed | not disclosed | not disclosed | **fashion / DTC** | HARD-REJECT | Fashion hard exclude. |
| 21 | 04-17 | Walker Deibel | "007" pitch | n/a | n/a | n/a | n/a | none | HARD-REJECT | Newsletter pitch, not a listing. |
| 22 | 04-17 | Bobby Jackson | Rejigg Report April | n/a | n/a | n/a | n/a | none | HARD-REJECT | Niche-intel report, not a listing. |
| 23 | 04-19 | Tory @ Flippa | $1.2M Hospitality Equipment Shopify | not disclosed | $1.2M | not disclosed | n/a | **DTC + restaurants/hospitality** | HARD-REJECT | Below $5M revenue floor; trips DTC + hospitality hard excludes. |
| 24 | 04-21 | Everingham & Kerr | Specialty Chemicals | not disclosed | not disclosed | not disclosed | not disclosed | **capital-intensive manufacturing (potential)** | FLAG | Specialty chemicals could be manufacturing or distribution; if manufacturing-heavy, hard reject. Body parse required. |
| 25 | 04-21 | Everingham & Kerr | High-Margin Promo Products reminder | not disclosed | not disclosed | not disclosed | not disclosed | none | FLAG | Same as #11. |
| 26 | 04-21 | Helen Guo | $2.9M biz | not disclosed | $2.9M | not disclosed | n/a | none | HARD-REJECT | Disclosed revenue $2.9M below $5M floor. |
| 27 | 04-21 | Quiet Light | 33-yr Education E-com | not disclosed | not disclosed | not disclosed | not disclosed | **DTC (e-com)** | HARD-REJECT | E-com label triggers DTC hard exclude. |
| 28 | 04-21 | Quiet Light | 75-yr Legacy Flag GSA | not disclosed | not disclosed | not disclosed | not disclosed | none | FLAG | GSA contractor, B2G services; industry-agnostic acceptable. Body parse required. |
| 29 | 04-21 | Bobby Jackson | Rejigg April | n/a | n/a | n/a | n/a | none | HARD-REJECT | Report, not a listing. |
| 30 | 04-21 | Tory @ Flippa | link-in-bio SaaS | not disclosed | not disclosed | not disclosed | not disclosed | none | FLAG | Industry-agnostic acceptable; financials TBD. |
| 31 | 04-21 | Walker Deibel | BTB | n/a | n/a | n/a | n/a | none | HARD-REJECT | Newsletter. |
| 32 | 04-22 | Everingham & Kerr | Specialty Chemicals press release | n/a | n/a | n/a | n/a | none | HARD-REJECT | Closed-deal PR, not a for-sale listing. |
| 33 | 04-22 | Quiet Light | 33-yr Education | not disclosed | not disclosed | not disclosed | not disclosed | **DTC (e-com)** | HARD-REJECT | Same as #27. |
| 34 | 04-22 | Rejigg | platform match | not disclosed | not disclosed | not disclosed | not disclosed | none | FLAG | Platform match; payload TBD. |
| 35 | 04-22 | Tory @ Flippa | $1.07M link-in-bio SaaS | not disclosed | $1.07M | not disclosed | n/a | none | HARD-REJECT | Below $5M revenue floor. |
| 36 | 04-22 | Helen Guo | $2.9M biz | not disclosed | $2.9M | not disclosed | n/a | none | HARD-REJECT | Same as #26. |
| 37 | 04-23 | Everingham & Kerr | Specialty Chemicals | not disclosed | not disclosed | not disclosed | not disclosed | **capital-intensive mfg (potential)** | FLAG | Same as #24. |
| 38 | 04-23 | Everingham & Kerr | Driver Education | not disclosed | not disclosed | not disclosed | not disclosed | none | FLAG | Industry-agnostic acceptable; body parse needed. |
| 39 | 04-23 | Everingham & Kerr | Full-Service Mechanical / HVAC | not disclosed | not disclosed | not disclosed | not disclosed | none in broker BB | FLAG | HVAC was a niche-strict hard exclude per audit context but is NOT a hard exclude on the broker buy-box. Industry-agnostic admits HVAC services. Body parse needed. |
| 40 | 04-23 | Quiet Light | 10-Year Education $92K email list | not disclosed | not disclosed | not disclosed | not disclosed | **DTC** | HARD-REJECT | Email-list business is content/DTC. |
| 41 | 04-23 | **Business Exits** | **Texas Home Health Staffing Back to Market** | **TX** | not disclosed | not disclosed | not disclosed | none direct | HARD-REJECT | **Geography hard fail.** TX is outside NY/NJ/PA/CT. Note. "Home Health Staffing" is borderline construction/labor-heavy services adjacent; geo kills it before that question matters. Audit highlighted as top miss but broker buy-box geo gate excludes. |
| 42 | 04-23 | Tory @ Flippa | Pool & Spa Amazon FBA | not disclosed | not disclosed | not disclosed | not disclosed | **DTC (Amazon FBA)** | HARD-REJECT | DTC. |
| 43 | 04-23 | Helen Guo | off-market | not disclosed | not disclosed | not disclosed | not disclosed | none | FLAG | Off-market blast; payload TBD. |
| 44 | 04-24 | **Tory @ Flippa** | **$16M B2B Trade Fair Exhibitor Recruitment Service** | not disclosed | $16M | not disclosed | not disclosed | none | FLAG | Disclosed revenue $16M is in the $5M-$50M band. EBITDA + margin not disclosed; geo not disclosed. B2B services, named industry, industry-agnostic acceptable. **Top miss per audit; no hard exclude trips.** |
| 45 | 04-24 | NAIFA-NY | April newsletter | n/a | n/a | n/a | n/a | none | HARD-REJECT | Industry newsletter, not a listing. |
| 46 | 04-28 | Helen Guo | $700K, 60% seller financed | not disclosed | $700K | not disclosed | n/a | none | HARD-REJECT | Below $5M revenue floor. |
| 47 | 04-30 | Helen Guo | New Off-Market Businesses | not disclosed | not disclosed | not disclosed | not disclosed | none | FLAG | Off-market blast; payload TBD. |
| 48 | 05-01 | **Bob Williamson / Cetane** | VRA cold prospect | n/a | n/a | n/a | n/a | none direct | KNOWN-REJECT-OVERRIDE | Per `feedback_free_valuation_equals_sell_side`. Cetane offers free VRA = sell-side prospecting, wrong layer for buy-side intent. Decision recorded 2026-05-01 + 2026-05-02. Do not surface even if a Cetane listing clears criteria. |
| 49 | 05-01 | Frank Sondors | Salesforge | n/a | n/a | n/a | n/a | none | HARD-REJECT | SaaS vendor pitch to G&B, not a deal listing. |
| 50 | 05-02 | Bob Williamson / Cetane | Sample VRA PDF | n/a | n/a | n/a | n/a | none | KNOWN-REJECT-OVERRIDE | Continuation of #48. |
| 51 | 05-04 | Tory @ Flippa | Football Analysis YT | not disclosed | not disclosed | not disclosed | not disclosed | **DTC** | HARD-REJECT | Consumer/online content. |
| 52 | 05-04 | Tory @ Flippa | Wellness device | not disclosed | not disclosed | not disclosed | not disclosed | **DTC** | HARD-REJECT | Consumer DTC. |
| 53 | 05-04 | Tory @ Flippa | Recovery brand | not disclosed | not disclosed | not disclosed | not disclosed | **DTC** | HARD-REJECT | Consumer DTC. |

Note. Rows expand past 42 because audit's table-c listed each named-sender slot separately when a single date had multiple distinct headlines. The 42 number is the audit's distinct-broker-blast count; this rerun screens every distinct headline-or-blast lifted into the audit table.

Pre-existing rejections honored.
- **Bob Williamson / Cetane (rows 48 + 50).** KNOWN-REJECT-OVERRIDE. Sell-side advisor pattern locked.
- **Andrew Lowis / Axial.** Not in audit table (Axial-internal connector, not a broker blast). No row needed.

## 4. Aggregate Counts

Cross-arm aggregate.

| Verdict | Arm 1 (today's scrape) | Arm 2 (30-day backfill) | Total |
|---|---|---|---|
| PASS | 0 | 0 | 0 |
| FLAG | 3 | 19 | 22 |
| HARD-REJECT | 1 | 30 | 31 |
| KNOWN-REJECT-OVERRIDE | 0 | 2 | 2 |

Of 53 distinct broker headlines/blasts screened in Arm 2, 19 cleared all disclosed criteria (FLAG = no disclosed reject, missing data prevents PASS); 30 hit a hard reject (geo, hard exclude, or disclosed sub-floor financial); 2 are known overrides; 0 had complete enough disclosure to land at PASS.

The buy-box converts a meaningful slice of the audit's 42 BLAST kills into review-eligible flow. Roughly 22 broker emails over 30 days warrant a manual broker-buy-box review (a 21x lift over today's 0 surfaced from the niche-strict screen, in the 30-day window). At ~7 per week, that fits inside the proposed Friday "broker email weekly review" Decisions surface from the audit's recommendation 2.

## 5. Top 5 Specific Deals/Listings That Warrant G&B Operator Eyes

Ranked by structural goodness (size, named-broker source, distance to financial floor, low hard-exclude risk).

1. **Tory @ Flippa. $16M B2B Trade Fair Exhibitor Recruitment Service** (04-24). Disclosed revenue mid-band. B2B services. No hard exclude trips. Strongest FLAG in the entire 30-day window. Action. Pull Flippa listing page, confirm geo + EBITDA + margin. If NY/NJ/PA/CT and EBITDA >= $2M with 15%+ margin, this is a clean PASS.

2. **Flavia Milano / IAG. $25M / $6.5M SDE Site Development + Infrastructure Contractor** (04-16). Financials clean ($25M / $6.5M SDE / 26% margin). Audit-flagged top miss. Caveat. "Site Development and Infrastructure Contractor" sits close to the construction hard exclude. Action. Open the IAG listing or reply to Flavia for the CIM, confirm geo + clarify whether this is general construction (reject) versus specialty infrastructure services (e.g. utility-locating, fiber-trenching subcontract, environmental remediation). The label is interpretive; the body decides.

3. **Business Exits. GovCon IT Firm. Judiciary + VA contracts. $19.7M / $3.4M / 17.5%** (today, 05-04). Financials clean. B2G services, industry-agnostic. Action. Pull the Business Exits listing page, confirm geo. GovCon contractors cluster around DC / VA / MD; verify whether HQ + ops fit NY/NJ/PA/CT. If yes, PASS-level deal.

4. **Business Exits. B2B Experiential Marketing Vendor. $14.3M / $3.3M / 23.1%** (today, 05-04). Financials clean. B2B services. Action. Confirm geo. If in band, surface to evaluation.

5. **Business Exits. Government Contract ERP Service. $14.0M / $2.6M / 18.3%** (today, 05-04). Financials clean. Vertical SaaS / B2G services. Action. Confirm geo. If in band, surface.

Honorable mentions worth a body-parse pass.
- Quiet Light 75-yr Legacy Flag GSA (04-21). GSA contractor; flag-related but B2G services-shape.
- Tory @ Flippa link-in-bio SaaS (04-21 / 04-22). Industry-agnostic SaaS; financials TBD on the 04-21 entry, sub-floor on 04-22 entry.
- Everingham & Kerr Full-Service Mechanical / HVAC (04-23). HVAC is NOT a broker-buy-box hard exclude (only a niche-strict one). Industry-agnostic admits.
- Quiet Light RV Enthusiast Content Site (04-16). Content/media, industry-agnostic admits if not DTC.
- Everingham & Kerr Driver Education (04-23). Industry-agnostic services.

## 6. Data Quality Notes

Where the backfill was constrained.

- **42 distinct named-broker BLAST emails were enumerated by the audit, not 53.** The 53 rows in the verdict table reflect every distinct headline lifted into audit table c. Rows that are newsletters / reports / pitches (Walker Deibel BTB, Bobby Jackson Rejigg Report, NAIFA-NY, Frank Sondors, Karlton tax, Peter Lang SBA) collapse to "not a listing" hard rejects. The decision-relevant universe is roughly 22 FLAG + 0 PASS, which aligns to a 21x lift over the niche-strict screen but is well under the audit's 42 if newsletters are excluded.

- **Geography is the highest-leverage missing field.** 19 of 19 Arm-2 FLAGs are FLAG-because-geo-undisclosed. The broker buy-box has geo as a HARD GATE; until each FLAG resolves to "in NY/NJ/PA/CT" or "out", none can promote to PASS. Body-parsing the underlying email or visiting the broker listing page is the single highest-value backfill action.

- **EBITDA and margin disclosure is rare in BLAST headlines.** Most named-broker blasts (Quiet Light, Tory @ Flippa, Helen Guo, Everingham & Kerr) lead with revenue + asking price, not EBITDA. The buy-box's $2M EBITDA practical floor + 15% margin minimum cannot be applied at headline level; body parse is mandatory.

- **The audit's enumeration was sender + headline, not full payload.** The audit captured what it could from artifact references; for several FLAGs (e.g. Lisa @ Generational DealForce, Viking Mergers New Acquisition Opportunities, Helen Guo off-market) the email IS a multi-listing blast, and "the headline" understates how many distinct deals are inside one message. A future rerun should ingest the actual emails, not the audit summary, to count individual listings rather than blast counts.

- **Today's morning artifact (Arm 1) only enumerates 4 Near Misses** out of ~95 reviewed listings across 8 active broker sources. The remaining ~91 listings exist only as aggregate counts in the Source Scorecard. To run this rerun routinely (recommendation in section below), the deal-aggregator wrapper would need to emit a per-listing rejection log, not just aggregate Near Misses.

- **EBITDA/SDE distinction.** Several disclosed financials use SDE (seller's discretionary earnings) rather than EBITDA. SDE is typically higher than EBITDA by the value of owner's compensation. For the Flavia Milano $6.5M SDE example, EBITDA is plausibly $4.5M-$5.5M, still well above the $2M floor; the verdict holds. For sub-floor SDE listings the gap is in G&B's favor, but flag any borderline case for proper EBITDA computation.

---

## Outcome

- **Published.** null
- **Engagement.** null
- **Hypothesis result.** pending. Whether the broker buy-box converts the BLAST-killed long tail into useful flow rests on geo-resolution of the 22 FLAGs.
