---
schema_version: 1.1.0
date: 2026-05-26
type: trace
title: "task-tracker-manager: weekly-files architecture chosen over IMPORTRANGE + in-place archive"
tags:
  - date/2026-05-26
  - trace
  - skill/task-tracker-manager
  - verb/APPROVE
  - topic/task-tracker-refactor
  - topic/google-sheets-architecture
---

## Trigger

The in-place `distribute-week --force` model destroyed prior-week day-tab state before next Sunday's `build-week` could read incomplete carryover items from it. Today's belated Sunday ceremony manifested this: I had to manually walk every carryover after the rollover because the prior-week day-tab state had already been wiped. Kay diagnosed: *"The order matters. The week shouldn't be based on the current daily tabs — it should be based on the prior daily tabs. You're deleting those."*

## Decision

**Refactor task-tracker-manager from single-sheet-with-archive-tabs to weekly-Google-Sheets-files architecture.** Each Sunday `build-week` Drive-copies the prior week's file into a new `TO DO M.D.YY` file in the `To Do Archive` Drive folder. Day tabs become the SINGLE edit surface; Week tab cells are in-file formulas (`=Tue!B14` etc.) — live read-only mirror of day tabs. Cross-file carryover-pull at rollover reads PRIOR file's day tabs and writes incompletes to NEW file's day tabs. Prior file is immutable history.

## Alternatives Considered

1. **Keep single-sheet + add archive tab per week (status quo, pre-2026-05-26).** Simplest. Fails because `distribute-week --force` overwrites day tabs before next Sunday's carryover-pull can read them — the original problem.

2. **Add a "carryover" auto-pull step to build-week before distribute-week clears day tabs.** Implemented earlier in the session (`_pull_carryover_to_week`). Solves the read-before-clear problem but Week tab still gets manually maintained → drift between Week tab and day tabs accumulates; Kay correction: *"The Week tab is the Sunday plan-of-record, not a live mirror."*

3. **Make Week tab a live formula mirror of day tabs via IMPORTRANGE (cross-file refs).** Considered. REJECTED because Google Sheets requires a one-time manual browser auth click ("Allow access") per source file — cannot be automated via API. Kay's no-friction principle ruled this out.

4. **Single-sheet + formula Week tab (`=Tue!B14`) + permanent day tabs.** Considered. Solves drift (Week tab = formula mirror). But the prior-week day-tab state is STILL destroyed when distribute-week overwrites day tabs. Doesn't solve the carryover read-before-clear problem.

5. **New Google Sheets file every Sunday + in-file formula Week tab (chosen).** Drive-copy carries full structure + formatting + dropdowns + CF + checkbox validation. Prior file becomes immutable history (read-only by convention). New file's Week tab uses in-file formulas (`=Tue!B14`) — no IMPORTRANGE auth gotcha. Cross-file carryover-pull reads prior file's day tabs once at rollover. distribute-week becomes obsolete (Week tab is auto-mirror, no separate write target).

## Reasoning

Three constraints made option 5 the only fit:

- **Constraint A — carryover read-before-destroy:** Sunday's carryover must read prior-week day-tab state BEFORE that state is destroyed. Options 1, 2, 4 all destroy by overwrite. Option 5 preserves prior state in the immutable prior file.
- **Constraint B — Week tab as plan-of-record:** Kay wants the Week tab to capture the Sunday plan and stay frozen mid-week as a reference. Options 1-2 require manual sync discipline (broke once today). Option 5's formula Week tab is auto-mirror — drift impossible.
- **Constraint C — no manual auth clicks:** Cross-file IMPORTRANGE (option 3) requires one-time browser auth per source file. Each week's new file would trigger the prompt. Violates no-friction principle.

Verified end-to-end in sandbox rehearsal: Drive copy preserved CF + dropdowns + checkbox validation; in-file `=Tue!A14` formulas propagated native checkbox state through to Week tab (tick `Tue!A14` → `Week!F24` evaluates `True`); 0 IMPORTRANGE refs across 140 formula writes.

## Why This Trace Matters

Without this trace, a future agent would either (a) reach for IMPORTRANGE for cross-file refs (the standard pattern), hitting the auth-click trap, or (b) revert to single-sheet thinking on the next refactor. The three constraints above are the load-bearing reasons; future architecture decisions should re-validate against them.

Also encodes: **why `distribute-week` is now functionally redundant** but stays callable (per [[feedback-explicit-review-before-retiring-verbs]]) until usage data justifies retirement.

## Key Insight

**A single-sheet with mutable day tabs CANNOT both preserve prior-week state AND have day tabs as the working surface for a new week.** That contradiction needs file-level separation. The Drive-copy pattern (where new file = full clone with structure intact) makes weekly-file boundaries cheap. The in-file `=Tab!Cell` formula pattern (free, no auth) makes the Week tab a no-cost view.

Implementation plan: [[plans/peppy-leaping-honey]] — 6 phases. Phases 1-4 + 6+ shipped 2026-05-26. Phase 5 (first real rollover) auto-fires Sun 5/31 via `/goodmorning`. Phase 6 distribute-week retirement review deferred until post-5/31 usage data.
