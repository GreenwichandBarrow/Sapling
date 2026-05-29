---
schema_version: "1.0.0"
date: 2026-05-29
type: tracker
title: "Deal Aggregator Weekly Digest — 2026-05-29"
window_start: 2026-05-22
window_end: 2026-05-29
volume_7d_avg: 0.0
volume_prior_week_avg: 0.29
volume_status: "🔴 Critical"
proposed_additions: 0
proposed_retirements: 0
opportunistic_count: 0
sourcing_sheet_source: live
fingerprint_store_status: sparse
tags:
  - date/2026-05-29
  - tracker
  - topic/deal-aggregator
  - topic/weekly-digest
  - status/draft
---

# Deal Aggregator Weekly Digest — 2026-05-29

Window: **2026-05-22 → 2026-05-29** (5 weekday scans read: Thu 05-22, Mon 05-25, Tue 05-26, Wed 05-27, Thu 05-28. Fri 05-29 morning daily-scan fires on a separate plist and isn't read by this digest. Weekend gaps 05-23/05-24 are expected — no scheduled scan.)

## 1. Source Productivity (Last 7 Days)

| Source | Category | 7d Matches | 7d Listings Reviewed | Last Match | Trend |
|---|---|---:|---:|---|:---:|
| Business Exits | General | 0 | 127 | — | → |
| Synergy Business Brokers | General | 0 | 55 | — | → |
| Empire Flippers | General | 0 | 44 | — | → |
| Website Closers | General | 0 | 38 | — | → |
| Synergy BB Real Estate | Niche / Estate Mgmt | 0 | 16 | — | ↓ |
| SMB Deal Hunter (Helen Guo) | General | 0 | 10 | — | ↑ |
| Flippa | General | 0 | 8 | — | ↑ |
| GP Bullhound | Niche / Vertical SaaS | 0 | 6 | — | → |
| Sica Fletcher | Niche / Specialty Insurance | 0 | 6 | — | ↓ |
| Quiet Light | General | 0 | 1 | — | → |
| BizBuySell | General | 0 | 0 | — | → |
| DealForce | General | 0 | 0 | — | → |
| Everingham & Kerr | General | 0 | 0 | — | → |
| IAG M&A Advisors | General | 0 | 0 | — | → |
| PCO Bookkeepers | Niche / Premium Pest | 0 | 0 | — | → |
| Rejigg | General | 0 | 0 | — | → |
| Viking Mergers | General | 0 | 0 | — | → |

- Source rows = 17 (all sheet-Active sources: 13 General + 4 Niche-Specific). Matches current Sourcing Sheet Active roster, live-read this run.
- Total listings reviewed across the week: **311** — concentrated on Business Exits / Synergy / Empire Flippers / Website Closers (general-platform horsepower, ~84% of all listings reviewed). Throughput down vs prior week (444 → 311, -30%) on a thinner listing window across the general platforms.
- Total buy-box matches across the week: **0** from scanned sources. (DealsX-channel inbound = 0 this window — no `Lead Interested` notifications landed; the 2 historical DealsX leads in the fingerprint store predate this window.)
- Email-only broker blasts (SMB Deal Hunter, Flippa, Quiet Light) produced 9 listings 05-27 + 10 listings 05-28, **all HARD-REJECTED** on sub-floor revenue/EBITDA or industry/geography hard-excludes. Those listings are counted in the source rows above (SMB Deal Hunter 10, Flippa 8, Quiet Light 1); none surfaced as evaluable deals.
- **Trend column:** matches are 0/0 for every source both weeks, so a strict match-count trend is undefined. Per the prior-digest convention, the arrow proxies on **listings-reviewed** week-over-week vs the 2026-05-22 digest (window 05-15 → 05-22): `↑` ≥ +50%, `↓` ≤ -50%, `→` within ±50%. Synergy BB Real Estate ↓ (33 → 16, -52%) and Sica Fletcher ↓ (27 → 6, -78%, thinner tombstone window). SMB Deal Hunter ↑ (0 → 10) and Flippa ↑ (0 → 8) as their email blasts resumed mid-week. All others → (within ±50%, or 0 → 0).
- **`fingerprint_store_status: sparse`** — `brain/context/deal-aggregator-fingerprints.jsonl` holds 2 records (both DealsX-channel leads, 05-18 / 05-19). Zero platform-source matches have ever been written. "Last Match" reads `—` for every source: the instrument exists, scanned channels have not produced a PASS to write. Fourth consecutive week with no platform-source fingerprint.

## 2. Volume Check

- 7-day rolling average: **0.0/day** (0 evaluable deals surfaced + 0 DealsX-channel inbound ÷ 7 days)
- Target: 1–3/day
- Status: **🔴 Critical**
- Prior-week average (05-15 → 05-22): 0.29/day → **-0.29 week-over-week** (the prior week's 2 DealsX-channel leads were not repeated this window; platform-source contribution remains 0).
- Read: 311 listings reviewed across 5 weekday scans is healthy scan throughput; the gap is at the buy-box gate, not at scan coverage. **Fourth consecutive 🔴 week** on platform-source volume (04-25→05-02, 05-08→05-15, 05-15→05-22, 05-22→05-29). The 19 email-broker listings on 05-27/05-28 all cleared scan but failed the financial gate (sub-floor) or a hard-exclude — consistent with the standing hypothesis that the general-platform inventory sits structurally below the $2M-EBITDA practical floor, and the active niche corpora aren't converting general scan volume. Calibration item carried to Section 5.

## 3. Proposed Additions

None this week.

- Source Scout enumerated all inbox sender domains across the 6 email-scan-results files in the window (05-22, 05-25, 05-26, 05-27, 05-28, 05-29), cross-referenced against the live Sourcing Sheet roster, and web-verified every candidate. **Zero genuinely new deal-source domains surfaced.** Every new sender classified out by category — searcher peers (libreequity.com, pacificlake.com), women's-network / warm-intro contacts (planprofessionals.com, thecorpcoach.com, gripcommunications), PE / search-fund investors (plexuscap.com [HTTP 200, confirmed PE not broker — exit/intel channel per `feedback_pe_rollup_relationship_is_exit_channel_not_dealflow`], Anacapa Partners), law/accounting firms (norris-law.com, schulmanlobel.com), or vendor solicitations (inzotechnologies, salesforge, corpnet.com).
- Newsletter-body scan for AI-marketplace launches and named niche-broker mentions (NPMA/PestWorld, IA Magazine, IREM, CMM Online, Agency Checklists, Axial Middle Market Review, Acquiring Minds): no new web-verifiable deal-source platform surfaced. The one AI-marketplace mention — Acquiring Minds' "ETA Database" — is a searcher database, not a broker deal-listing source.
- **Carryover awaiting Kay's decision (proposed 2026-05-22, not yet actioned):**
  - **Digital Capital Advisors (DCA)** — https://www.digitalcapitaladvisors.com — reappeared this window (Project Drone thread, Carlos Nieto). Still `Active - email-only` candidate for General Sources.
  - **Transworld Business Advisors (NY)** — https://www.tworld.com — reappeared 05-29 as a ~20-listing blast (Sam Curcio). Still `Active - relationship + marketplace` candidate for General Sources.
  - These are NOT re-counted in `proposed_additions` (no new proposal this week) but remain open from the 05-22 digest. See Section 5.

## 4. Proposed Retirements

None this week.

- Per SKILL.md `<weekly_digest>` retirement-side spec, a proposed retirement requires (a) 30+ days no fingerprint-attributed match AND (b) 3 live-checks performed (URL resolves, domain registered, email-channel status). The fingerprint store has 2 records total (both DealsX-channel, since 05-18); **zero platform-source matches have ever been written**, so signal (a) is undefined for every scanned source.
- Per `feedback_test_before_concluding_channel_dead` (Sica Fletcher was mis-labeled 404 for days in April): never retire on absent data. Silence from an instrument that has never recorded a hit for *any* platform source is not silence from any *individual* source. No retirement is defensible until the fingerprint path has demonstrably recorded at least one platform PASS. Fourth consecutive week carrying this reasoning.

## 5. Recommended Actions (Kay's Review Bucket)

1. **Volume = 🔴 fourth consecutive week** (0 platform-source deals/day, 0.0/day total — the prior week's DealsX inbound did not repeat). 311 listings reviewed → 0 PASS; the 19 email-broker listings on 05-27/05-28 all HARD-REJECTED on sub-floor financials or hard-excludes. RECOMMEND: schedule a corpus-tuning pass on the active niches' DEALSX keyword sets + WR-row enrichment terms alongside next Tuesday's niche-intelligence, AND confirm whether the general-platform inventory structurally sits below the $2M-EBITDA practical floor (if so, re-weight scan effort toward niche-specific advisory sources) — carried from 05-15 and 05-22 digests, not yet executed → YES / NO / DISCUSS
2. **Carryover: Digital Capital Advisors → add to General Sources (`Active - email-only`)** — proposed 05-22, still awaiting decision; reappeared this window (Project Drone) → YES / NO / DISCUSS
3. **Carryover: Transworld Business Advisors (NY) → add to General Sources (`Active - relationship + marketplace`)** — proposed 05-22, still awaiting decision; reappeared 05-29 (~20-listing blast) → YES / NO / DISCUSS
4. **Fingerprint store still empty for platform sources** (2 records total, both DealsX-channel, none since 05-19). The `scripts/deal-aggregator-fingerprint.sh add` path has never fired from a scanned-source PASS in 14+ weekday scans — consistent with 0 platform PASS verdicts, so likely "no matches" not "silent helper failure," but the morning-run exit-code instrumentation request from the 05-15 / 05-22 digests is still unimplemented. RECOMMEND: have the next morning scan log the fingerprint-helper exit code for any PASS attempt (or an explicit "no PASS to fingerprint" line if 0) → YES / NO / DISCUSS

---

### Sources read

- Daily scans (5): `brain/context/deal-aggregator-scan-{2026-05-22,25,26,27,28}.md`
- Email-scan results (6): `brain/context/email-scan-results-{2026-05-22,25,26,27,28,29}.md`
- Fingerprint store: `brain/context/deal-aggregator-fingerprints.jsonl` (2 records, both DealsX-channel; 0 platform-source matches)
- Sourcing Sheet: `1z8o2obq2mOG9drQ0umCmBk31K3OS2afMNGpVAlbLljw` — General Sources + Niche-Specific Sources, live-read this run (17 Active sources)
- Prior digest for trend comparison: `brain/trackers/weekly/2026-05-22-deal-aggregator-digest.md`
