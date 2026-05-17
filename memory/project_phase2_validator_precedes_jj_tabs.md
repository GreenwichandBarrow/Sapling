---
name: project-phase2-validator-precedes-jj-tabs
description: Sunday-night Phase 2 integrity validator structurally cannot pass before jj-operations builds Call Log tabs
metadata:
  type: project
---

The headless Sunday-night JJ Phase 2 job (target-discovery) runs Step 5 = `scripts/validate_phase2_integrity.py`, which checks that every pool company appears on the upcoming-week Mon–Fri "Call Log M.DD.YY" tabs with Col K populated. But those tabs are created by **jj-operations Sunday-prep, a separate launchd job sequenced AFTER this one** (Phase 2 Step 6 explicitly forbids invoking jj-operations from inside the Phase 2 prompt).

Consequence: on every Sunday-night first-of-week run, the validator returns exit 1 with ~5 "could not read 'Call Log X'" + ~199 "pool company not on any tab" failures — purely because the tabs don't exist yet, NOT because the pool is broken. The pool-internal invariants (artifact rows → Full Target List mapping, Col K populated) are checkable independently and were sound on 2026-05-17.

**Why:** The validator is correctly designed to run at the jj-operations boundary (SKILL.md lists jj-operations prep mode as an invoker, and the wrapper runs it as POST_RUN_CHECK). It is NOT satisfiable inside target-discovery Phase 2 before the handoff. The Phase 2 prompt's "validator must pass before exit 0" + "don't run jj-operations" is a spec contradiction for the Sunday slot.

**How to apply:** On the Sunday Phase 2 run, distinguish failure classes. If the ONLY failures are missing-Call-Log-tab + pool-company-not-on-tab (no "drift detected", no "blank Col K"), the pool is sound and the failure is the sequencing gap — exit with the validator's code AND state the diagnosis explicitly so the Slack alert is actionable, not noise. The real fix belongs in the validator/wrapper: gate the pool↔tabs invariant on tab existence, or move the authoritative integrity gate into jj-operations prep (post-tab-build) and have Phase 2 run only the internal-soundness subset (artifact↔Full-Target-List + Col K). See [[feedback-strategic-thresholds-need-grounding]].
