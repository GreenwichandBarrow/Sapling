---
schema_version: 1.1.0
date: 2026-04-20
type: trace
today: "[[notes/daily/2026-04-20]]"
task: "river-guide-builder Phase 3 Network Matches calibration across 8 niches"
output: "[[context/session-decisions-2026-04-20]]"
had_human_override: true
importance: high
target: skill:river-guide-builder
tags: [date/2026-04-20, trace, pattern/instrument-vs-reality, domain/technical, status/pending]
---

# Decision Trace: Phase 3 Calibration Yield Contradicts Kay's Lived Network Knowledge

## Context

Ran river-guide-builder Phase 3 calibration scan across 8 active niches against 492 Apollo-enriched Attio People records. Subagent returned H-strength matches with this distribution:

| Niche | H-count |
|---|---|
| art-storage | 4 |
| estate-management | 1 (FP) |
| premium-pest | 1 (FP) |
| private-art-advisory | 1 |
| high-end-commercial-cleaning | 0 |
| specialty-coffee-equipment | 0 |
| specialty-insurance | 0 |
| vertical-saas-luxury | 0 |

After false-positive filter: 5 legit hits total, all art-world-adjacent. Subagent recommendation: "criterion holds, safe to proceed with writes on the 5 legit hits." Presented results to Kay and offered YES/NO/DISCUSS on writes.

## Decisions

### Whether to write the 5 Network Matches rows or pause for investigation
**AI proposed:** Proceed with writes on 5 art-world hits (Kate Reibel ×2, Britta Nelson, Amanda Lo Iacono, Rick Hiebert). Skip 2 false positives. 6 niches populated with zero — accept thin yield.
**Chosen:** Pause, do not write. Investigate why 6 of 8 niches returned zero when Kay's lived experience says she has network contacts across ALL 8. Resume tomorrow with an investigation pass before any writes.
**Reasoning:** Kay's direct network knowledge is ground truth. Calibration output that contradicts that knowledge is an instrument problem, not a reality problem. Specifically:
- specialty-insurance H=0 doesn't match Kay's known contacts (Christopher Wise at Risk Strategies, Sarah De Blasio at Chartwell, Margot Romano, etc.)
- vertical-saas-luxury H=0 doesn't match her investor base's operator backgrounds
- high-end-commercial-cleaning H=0 is plausible but deserves verification
Accepting the skill's "criterion holds" recommendation would have written a false-bottom-line to the Network Matches tabs and set the Phase 3 baseline at an artificially thin yield.
**Pattern:** #pattern/instrument-vs-reality

## Learnings

- **When skill output contradicts user's direct knowledge, the default prior should be "instrument is broken" not "user is wrong."** Future Phase 3 runs (and Phase 3-analogous network-scan workflows in other skills) should trust the user's lived knowledge as ground truth and treat thin yield as a symptom, not a finding.
- **Investigation vectors identified for tomorrow:** (1) keyword tokenization — short tokens ("sca", "aman", "md") cause substring collisions; need whole-word matching. (2) H-criterion too strict — requiring "senior title + 3yr + keyword" may exclude valid contacts with senior titles at matching firms but <3yr tenure, OR non-senior-titled contacts at matching firms who still have deal-flow proximity. (3) Attio enrichment coverage is 388/1,825 = 21% — the other 79% haven't been scanned at all. (4) Kay's knowledge often lives outside Attio (LinkedIn CSV head-knowledge, Gmail threads, vault entities not yet enriched). Phase 3 should span all 4 data sources per skill spec but the calibration subagent only scanned Attio employment_history.
- **Specific skill defect suspected:** The subagent scanned only `nddl_apollo_employment_history` despite skill spec listing 4 data sources (Attio employment history → LinkedIn CSV → Attio standard fields → vault → Gmail). Prompt may not have been explicit enough about running all 4.
- **Calibration-before-writes pattern validated.** Kay's "10 tops per niche, flag and pause if more" rule caught a problem the skill's internal success criteria would have missed. Opposite-failure mode exists: cap can also mask too-few results. The cap should be a both-sided check: `count > 10` OR `count == 0` where Kay expects signal both trigger pause.

## Why This Trace Matters

Future network-scan agents will face this pattern repeatedly: thin output that passes internal quality checks but contradicts the user's domain knowledge. The default behavior must be "trust the user, diagnose the instrument." Writing five rows and declaring the run complete would have been the wrong answer — and the skill's own recommendation said to do exactly that.
