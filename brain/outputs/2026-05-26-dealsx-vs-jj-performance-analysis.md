---
schema_version: 1.1.0
date: 2026-05-26
type: analysis
status: draft
title: "DealsX vs JJ — Channel Performance Analysis Pre-Wind-Down (2026-05-26)"
tags:
  - date/2026-05-26
  - output
  - output/analysis
  - topic/dealsx
  - topic/jj-operations
  - topic/channel-performance
  - topic/windown-decision
  - status/draft
---

# DealsX vs JJ — Channel Performance Analysis Pre-Wind-Down

**Framing.** This is an analysis tool for the G&B principal's call, not a verdict. The 2026-05-20 wind-down decision was thesis-driven (network-mapping-first, women-led purpose throughline). This document asks the orthogonal question: *what does the channel performance data alone say?* See [[memory/project-dealsx-jj-windown-by-summer]] for the original convergence rationale, [[memory/user-kay-women-led-purpose-throughline]] for the thesis lens, and [[memory/feedback-industry-is-output-of-network]] for the structural reframe.

---

## A. Headline

**Both channels show zero meaningful conversion downstream of top-of-funnel activity, and neither has produced an NDA, financials, or LOI across the full ramp.** DealsX out-performs JJ on every yield metric where comparison is possible (positive replies > owner conversations, replies > "Connected" outcomes, faster pace at lower marginal cost per unit of activity). JJ's top-of-funnel signal is dominated by gatekeeper deflection ("Customer Service" = 64% of all logged 1st-call statuses), which suggests structural mismatch between the channel and the target population, not a JJ-execution problem. DealsX is younger (active ~2 weeks of measured data; launched 2026-05-06), but its early reply-rate window (2.5-3.5%) is within the band that justifies continued evaluation. **The data does not contradict wind-down; it does suggest DealsX deserves more runway than JJ if forced to pick one.**

---

## B. DealsX — Weekly Metrics

DealsX launched 2026-05-06. Two operational weeks of measured data exist in the canonical snapshot.

| Week ending | Sent | Replied | Positive | Bounced | Reply rate | Positive-of-replied |
|---|---|---|---|---|---|---|
| 2026-05-15 | 436 | 11 | 5 | 12 | 2.52% | 45.5% |
| 2026-05-22 | 200 | 7 | 1 | 0 | 3.50% | 14.3% |
| **Total** | **636** | **18** | **6** | **12** | **2.83%** | **33.3%** |
| Avg / week | 318 | 9 | 3 | 6 | — | — |

**Funnel downstream of positive replies:** 0 NDAs, 0 financials, 0 LOIs attributable to DealsX in the canonical Active Deals pipeline (snapshot 2026-05-26: 10 active deals, all Identified/Contacted; closed_post_nda lifetime = 2, neither sourced from DealsX based on stage_since dating). Note: source attribution is not stored on the Attio snapshot, so this is inferred from pipeline composition and weekly-tracker NDA/financials/LOI rows (all 0 since launch).

**Bounce note:** Week 1 bounce rate 2.75%, Week 2 bounce rate 0% — sender reputation acceptable, no deliverability red flag.

---

## C. JJ — Weekly Metrics

JJ has been operational since ~early February 2026. Below is the comparable window (last ~7 trackable weeks; earlier weeks had JJ on different niches or onboarding).

| Week ending | Dials (window-corrected) | "Connected" / owner conv. | Voicemail | Customer Service (gatekeeper) | Owner sentiment captured |
|---|---|---|---|---|---|
| 2026-04-10 | ~36 | 1 | 17 | 0 (pre-migration) | 0 |
| 2026-04-17 | 0 | 0 | — | — | 0 |
| 2026-04-24 | ~49 | 0 | 8 | 27 | 0 |
| 2026-05-01 | 91 | 0 | 49 | 111 | 0 |
| 2026-05-08 | 0 | 0 | 60 | 104 | 0 |
| 2026-05-15 | 133 | 2 | 18 | 72 | 0 |
| 2026-05-22 | 40 | 0 | 24 | 94 | 0 |
| **Total** | **~349** | **3** | **176** | **408** | **0** |
| Avg / week | ~50 | 0.43 | 25 | 58 | 0 |

**Funnel downstream of dials:** 0 NDAs, 0 financials, 0 LOIs, 0 owner sentiments recorded. Aggregate 1st-call status distribution across the window: **Customer Service 408 (~64%), Voicemail 176 (~28%), No Answer 52 (~8%), "Connected" 1, "Callback Requested" 1.** 2nd-attempt calls (36 attempted in trailing 4 weeks) all hit gatekeeper or voicemail again.

**Pace note:** Lifetime dials = 667 at 2026-05-22 snapshot. Wide week-to-week variance (0 to 133) — pace is unreliable. Wed/Thu no-shows recurred (4/22-4/23, others).

---

## D. Side-by-Side Funnel (Normalized)

| Stage | DealsX (2 weeks measured) | JJ (7 trackable weeks) |
|---|---|---|
| Top-of-funnel volume | 636 sends | ~349 dials |
| Avg / week | 318 | 50 |
| Engagement signal | 18 replies (2.83%) | 1 "Connected" + 1 callback = 2 (0.57%) |
| Positive engagement | 6 positive replies (0.94% of sent) | 0 owner-sentiment entries |
| Stage advance (NDA) | 0 | 0 |
| Financials | 0 | 0 |
| LOI | 0 | 0 |

**Top-of-funnel signal (per the dashboard note in 2026-05-22 tracker, DealsX has no open-tracking — reply rate is the only viable proxy):**
- DealsX positive-reply rate per send = 0.94% (6 / 636)
- JJ "Connected" rate per dial = 0.29% (1 / 349)

**DealsX is ~3.2x more efficient at producing a meaningful positive top-of-funnel response per unit of activity, AND requires zero G&B internal calendar time to operate (Sam's team runs it). JJ requires JJ's full 10am-2pm ET shift + Claude-side Monday ops review + occasional G&B-side debugging.**

---

## E. Cost Analysis (Best-Effort)

| Cost line | DealsX | JJ |
|---|---|---|
| Monthly recurring | $1,500/mo (Sam Singh retainer; KeyReach bundled) | $1,040/mo (StartVirtual VA invoice per [[memory/project-session-april-1]]) |
| Success fee | $25K flat per close | N/A |
| Apollo / list-builder | Shared $64/mo Apollo | Shared $64/mo Apollo |
| Total monthly variable | $1,500 | $1,040 |

**Cost per top-of-funnel unit (using full-period averages):**
- DealsX: $1,500/mo divided by ~1,272 sends/mo (extrapolated from 318/wk x 4) = **~$1.18 per send**
- JJ: $1,040/mo divided by ~200 dials/mo (50/wk x 4) = **~$5.20 per dial**

**Cost per positive top-of-funnel response:**
- DealsX: $1,500 divided by ~12 positives/mo (3/wk x 4) = **~$125 per positive reply**
- JJ: $1,040 divided by ~1.7 connects/mo (0.43/wk x 4) = **~$612 per connected call**

**Cost per NDA / financials / LOI:** undefined (denominator = 0 for both channels across the ramp).

**Caveat:** DealsX cost-per-positive looks attractive, but the success-fee structure ($25K per close) flips the economics on actual outcome. JJ has no equivalent success fee — JJ's marginal cost is fixed.

---

## F. Conviction-Builder Fit (2026-05-20 Thesis Convergence)

Per [[memory/feedback-industry-is-output-of-network]] and [[memory/user-kay-women-led-purpose-throughline]], the post-2026-05-20 operating model is **3 buckets x 10 women-owned NY firms, network-mapping-first**. Industry is the output of network access, not the input.

- **DealsX structural fit:** misaligned. DealsX is industry-agnostic mass cold email tuned by Sam's team. Its operating mode is *volume from list*, not *named-owner from network*. The current verticals (SaaS Enterprise / Specialty Healthcare / Female-Led SaaS) are charter-aligned on paper but DealsX has no mechanism to QC against "is this a woman-owned NY firm with a G&B relationship-path." **Strategic fit: low.**
- **JJ structural fit:** misaligned. JJ is blue-collar phone-cold outreach to Premium Pest Management owners. Pest is one of the staple-female-skew industries G&B's new methodology targets, but the JJ approach is *cold dial random pest companies* not *map the women-led pest network in NY*. Gatekeeper rate of 64% is exactly the signal the women-led-network model is designed to bypass — warm intros don't hit gatekeepers. **Strategic fit: low.**

Both channels are structurally orthogonal to the 2026-05-20 model. Neither generates the network-graph artifacts the new model requires.

---

## G. Wind-Down Recommendation (Data-Driven)

**DealsX:** Wind-down decision **STANDS, but with measured runway.** Performance metrics (2.83% reply rate, 0.94% positive-of-sent, $125 cost per positive) are within early-stage tolerance, but with 0 NDAs across the ramp the middle-of-funnel is not converting. The strategic-fit gap (industry-agnostic vs. network-mapped) is the binding constraint, not the throughput. Recommend honoring the 30-day notice timing.
- **Threshold that flips the verdict:** if DealsX delivers >=1 NDA-stage advance from a positive reply before notice-end, *AND* the source is a woman-owned NY firm, reopen the conversation. Both conditions are needed — NDA alone is not sufficient because the strategic fit is the gating issue.

**JJ:** Wind-down decision **STANDS, and the data argues for slight acceleration.** 349 dials, 1 "Connected" outcome, 0 owner conversations, 0 captured owner sentiments across 7 weeks of measured activity. Gatekeeper rate of 64% indicates structural failure of the cold-dial approach against this target population — not a JJ execution problem. The $1,040/mo is freeing slower than DealsX's $1,500/mo but the marginal yield is lower.
- **Threshold that flips the verdict:** if JJ produces >=1 owner conversation per week with captured sentiment (any sentiment, even "not selling") for 2 consecutive weeks before notice-end, the channel is viable enough to reconsider. Current rate is ~0 owner conversations/week.

**Sequencing recommendation:** Wind down both in the planned window. JJ's structural mismatch is more acute and warrants the longstanding-team-member careful exit message per [[memory/feedback-jj-team-member]]. DealsX should be the first test of the AI drafting skill ([[memory/project-dealsx-jj-windown-by-summer]]) for the business-communication side of the wind-down.

---

## H. Caveats

1. **DealsX has no open-tracking** (per 2026-05-22 tracker footnote — UI quirk). Reply rate is the top-of-funnel signal but undercounts engagement.
2. **DealsX measured window is small** (n=2 weeks, 636 sends). Two-week reply-rate noise is significant; the 14.3% positive-of-replied in week 2 vs. 45.5% in week 1 could reflect either list quality decay or sample noise.
3. **JJ "Customer Service" status is ambiguous** — could mean gatekeeper deflected to general line, or could mean "JJ talked to customer service rep, not owner." Either reading is a non-owner outcome; the distinction doesn't change the analysis.
4. **JJ owner-sentiment column has zero entries across the ramp.** Either no owners were reached, or JJ is not populating the column. Either way the data does not show owner-side signal.
5. **Source attribution on Attio is not in the snapshot.** NDA/financial/LOI counts are inferred from weekly trackers and pipeline composition, not direct join. The two post-NDA deals in the lifetime pipeline (per snapshot) are not attributable to DealsX or JJ from this data — they predate or are sourced from intermediary/conference channels.
6. **Spend data is point-estimate.** $1,500/mo DealsX and $1,040/mo JJ are documented in memory files but not reconciled against actual QBO line items in this analysis. Budget-manager skill would be the authoritative cross-check.
7. **Tab-name vs. call-date drift on JJ data** ([[memory/feedback-jj-call-date-from-field-not-tab]]) means per-week dial counts above may be off by ~1 day at the boundaries. Aggregate totals are not affected.
8. **The wind-down decision was thesis-driven, not performance-driven.** Even if both channels were performing well, the structural-fit gap with the 2026-05-20 model is independently load-bearing. This analysis confirms performance does not contradict the decision; it does not establish performance as the reason.
