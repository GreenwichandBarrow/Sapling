---
schema_version: 1.1.0
date: 2026-09-11
type: trace
task: Correct automatic deal-reserve escalation
output: "[[outputs/2026-09-11-budget-report-aug-2026]]"
had_human_override: true
target: skill:budget-manager
tags: [date/2026-09-11, trace, topic/budget, person/kay-schneider, company/greenwich-and-barrow]
---

# Decision Trace: Keep the confirmed deal reserve fixed

## Context

The monthly workflow applied an old40K-to80K LOI rule to a Submitted LOI status. [[entities/kay-schneider]] challenged the resulting [[entities/greenwich-and-barrow]] runway: "when it was always40K." The reviewed repo policy and agent memory recorded escalation, but direct approval was not found.

## Decisions

### Keep40K until the user explicitly changes it

**AI proposed:** Treat the CRM stage as authority to double the protected reserve.
**Chosen:** Use the user-confirmed40K; stage transitions do not change it.
**Reasoning:** A recorded policy assumption and a submitted LOI do not establish consent to withhold another40K from operations. The escalation understated available operating cash by40K without any new expenditure. Preserve source cash and recompute only dependent reserve/runway figures.

## Learnings

- Budget-manager: apply the current explicit reserve decision to future runs; present any alternative reserve as an unapproved scenario, never silently replace the base case.
- Source: [[context/session-decisions-2026-09-11]].
