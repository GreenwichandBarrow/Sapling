---
schema_version: 1.1.0
date: 2026-09-14
type: trace
task: Recover explicit budget corrections before Monday planning
had_human_override: true
target: skill:budget-manager
tags: [date/2026-09-14, trace, topic/budget, person/kay-schneider, company/greenwich-and-barrow]
---

# Preserve the approved fund period and cash basis

## Context

[[entities/kay-schneider]] clarified the original [[entities/greenwich-and-barrow]] budget in [[context/session-decisions-2026-09-11]] after the prior reserve correction. The current instructions are recorded in [[context/budget]].

## Decisions

### Use explicit allocations and anniversary dates
**AI proposed:** Explain the fund shortfall using calendar-year prorated expenses and continue the rounded $40K reserve.
**Chosen:** Use February 7, 2025 through February 7, 2027; $42K operating allocation, $38K diligence allocation, zero contingency. Treat calendar comparisons as diagnostics until the full fund-period reconciliation is complete.
**Reasoning:** Calendar-year reports are not the approved anniversary-year budget. An expense category can be under budget while its contingency funding has been consumed by other categories. Calling allocations current bank cash or subtracting reserve/payables twice changes apparent runway without changing funds.

### Keep pre-close cash and closing-funded fees separate
**AI proposed:** Compare total estimated transaction fees directly with the diligence reserve.
**Chosen:** Compare the reserve with amounts actually due before closing and contingent liabilities under the engagement terms; budget total transaction fees separately.
**Reasoning:** A deferred invoice may be funded at closing but remains a liability. Reimbursement after closing does not finance earlier invoices. Discussing release of diligence cash does not authorize its release.

## Learnings

- Current policy and metric references now carry the $38K correction. Historical report snapshots remain historical.
- Follow the newer [[outputs/2026-09-12-budget-runway-followup-aug-2026]] for current dated cash scenarios and invoice corrections; historical conversation amounts do not override newer verified work. Fee payment terms and current bank cash still require verification.
