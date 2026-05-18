---
name: launchd-debugger-blind-to-exit0
description: launchd-debugger's scan_launchd_failures.py only catches non-zero exits / validator failures. An empty scan ([]) does NOT mean "system healthy" — silent exit-0 logic failures (empty source list, schedule-order starvation, over-tight screening) are invisible to it.
metadata:
  type: feedback
---

When investigating a reported "silent failure," do NOT treat an empty `scan_launchd_failures.py` result (`[]`) as evidence the system is healthy. The scanner only sees non-zero exits, `VALIDATOR FAILED`, `PREFLIGHT FAILED`, or `STOP:` markers. A skill that exits 0 while producing zero useful output is invisible to it by design — launchd-debugger's scope explicitly excludes output-correctness.

**Why:** 2026-05-15 — deal-aggregator had produced zero broker matches for weeks. launchd-debugger scan returned `[]`. The real cause was a schedule-order bug (morning run fired 6am, before email-intelligence's 7am artifact landed → 8 broker-email sources blocked every morning) plus a niche-corpus/source-inventory mismatch. Both exit 0 cleanly; neither is a crash.

**How to apply:** For any silent-failure report, after the launchd scan comes back empty, spawn a focused root-cause subagent that reads the skill's recent run logs + output artifacts + its data-source dependencies (buy-box reads, niche corpus, upstream artifact timing). Empty scan = "not a crash," never "not a problem." Related: [[feedback_silent_failures_are_the_core_concern]], [[feedback_dashboard_green_can_lie]].
