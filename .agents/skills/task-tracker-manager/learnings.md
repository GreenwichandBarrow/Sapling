# Task Tracker Manager Learnings

## 2026-09-10 — Detect approved daily task boundaries

- Firing case: the September 7 approved expanded habit frame moved daily task headers from row 20 to row 22. The fixed-row guard blocked September 8–10 completion sync, carryforward, and reporting, leaving earlier-day work stranded.
- Daily maintenance now detects the supported exact header per tab and stops at the unique visible NOTES boundary, including overflow beyond row 80. Completion sync, carryforward, reporting, and source packing must use the same bounds.
- Preserve fail-closed behavior for missing, unsupported, or ambiguous headers and NOTES boundaries. Never rebuild an approved weekly layout merely to satisfy stale row constants.
- Focused regression coverage belongs in tests/test_task_tracker_daily_layout.py; keep habits, focus, free notes, future-day tasks, and recurring backend templates protected.

## 2026-09-10 — Remaining receipt and report cleanup

- The successful completion sync still emitted a mechanical receipt into brain/traces. The closeout removed only this run's receipt and retained verb-log/rollback evidence, following decision-traces. Candidate: route the emitter to execution logs in a separately reviewed cleanup; do not create receipt traces.
- Legacy report wording says individual carry moves require approval, despite the approved routine Good Morning sweep. Automatic approval review rejected changing that wording as weakening a safeguard. It remains unchanged; use explicit session authorization and the current skill contract, and keep the wording correction separate from the verified boundary repair.
