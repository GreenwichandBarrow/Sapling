---
name: Dashboard green status can lie when wrapper exits 0 on graceful self-stop
description: A launchd job exiting 0 doesn't mean it succeeded — it can mean it gracefully detected its own destructive failure and stopped before the rewrite. Validate with POST_RUN_CHECK.
type: feedback
originSessionId: 6c3fb9cc-7515-4990-9b86-f88efbc0a62e
---
A launchd job exit code of 0 doesn't mean the job did the right thing. It can mean the skill self-detected a problem (e.g., wiped a sheet by accident), saved a memory rule, surfaced to Kay, and stopped gracefully. Wrapper sees exit 0 → tile goes green → dashboard claims "fired this week, healthy."

**Why:** May 3 conference-discovery wiped the Conference Pipeline (~70 rows), self-detected, surfaced to Kay, exited 0. Dashboard's C-Suite & Skills weekly-flow tile showed green for the Sunday fire as of May 4 evening — Kay caught the gap visually. This is the failure mode POST_RUN_CHECK validators are designed to catch.

**How to apply:** Every launchd-scheduled skill needs a POST_RUN_CHECK validator that checks the actual artifact (sheet rows, snapshot file freshness, vault file content), not just exit code. As of 2026-05-04 the doctrine is universal — read-only skills get lighter validators (artifact-landed checks), no exemptions. Hardened: 8 skills. Outstanding: 5-6 (email-intelligence, calibration-workflow, external-services-probe, weekly-archive-export, weekly-snapshot, health-monitor).
