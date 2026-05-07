---
schema_version: 1.1.0
date: 2026-05-06
type: trace
today: "[[notes/daily/2026-05-06]]"
task: Diagnose niche-intelligence + deal-aggregator reported as hung in morning briefing
had_human_override: false
importance: medium
target: skill:pipeline-manager
tags: ["date/2026-05-06", "trace", "topic/launchd-debugger", "topic/pipeline-manager", "pattern/ps-verify-before-orphan-claim"]
---

# Decision Trace: Hung-Jobs False Alarm — Pipeline-Manager Misread Mid-Run Logs

## Context

Morning pipeline-manager scan flagged TWO 🔴 broken-system items:
1. `niche-intelligence` Tuesday-night fire — "failed all 3 attempts, orphan PID 49894 still alive 8h+ later"
2. `deal-aggregator` 6 AM today — "wrapper PID 55943 + claude -p PID 56191 still active, log file shows only the start banner. May be hung or still running."

Both were surfaced as a 🔴 RECOMMEND: Investigate Decision item. Kay approved investigation. launchd-debugger fired.

## Decisions

### Both jobs were FALSE ALARMS — they had succeeded

**AI proposed:** Treat both as legitimate hung-job incidents. Kill orphan PIDs, restart jobs, surface root causes.

**Chosen (debugger findings):** **No-op on both.** Neither job was hung:
- `niche-intelligence` Tuesday: attempts 1+2 hit the known `ai-ops-5wx` "Unexpected" error, but **attempt 3 succeeded at 08:05 with exit 0 + validator PASS.** Full 20 KB sprint report + 3.1 KB sidecar artifacts are on disk. Wrapper retry policy salvaged it.
- `deal-aggregator` 6 AM: **Completed at 06:43 with exit 0 + validator PASS** (32 KB scan artifact present). Pipeline-manager read the log mid-run when it was still 211 bytes; the log is now 1029 bytes.

The 3 "still alive" PIDs the morning scan reported were already dead by the time the debugger looked.

**Reasoning:** Pipeline-manager read the log files at a moment when the job was still mid-execution. It saw "log only contains start banner" and inferred the wrapper was hung. It did not `ps`-verify the PIDs before flagging them as orphans. The 1-hour-or-so delay between pipeline-manager's read and Kay's morning briefing was enough for both jobs to complete cleanly.

**Pattern:** #pattern/ps-verify-before-orphan-claim

## Why This Trace Matters

Future agents (especially pipeline-manager itself) will encounter the same scenario: scheduled job log file is small, last-seen PIDs aren't obviously gone, the job appears stuck. The default reflex is to flag it as broken. **That reflex generates a 🔴 Decision item that wastes Kay's morning attention and triggers a debugger fan-out for nothing.**

The correct sequence:
1. Read the log file
2. **`ps -p <PID> -o pid,etime,command` to verify the wrapper/claude-p PID is actually still alive**
3. If alive AND elapsed time >2 hours → flag as suspect
4. If alive AND elapsed time <2 hours → it's still running, just slow; check back in 30 min, don't flag
5. If dead → check the log AGAIN (it may have grown since the first read); look for exit 0 / validator PASS markers

Today's incident: both PIDs were already dead at scan time (jobs had finished), but pipeline-manager assumed they were alive because the log was small. The fix is to ground the orphan-claim in `ps` output, not log size inference.

## Key Insight

**Log file size is not a liveness signal.** A scheduled skill's wrapper writes the start banner immediately, then sits silent until the child `claude -p` process finishes (which can take 5-30 min). Reading the log mid-run produces a misleading "only start banner" snapshot. `ps`-verification of the PIDs from the log header is the only reliable signal.

This trace argues for a memory rule (`feedback_pipeline_manager_ps_verify_before_orphan_claim.md`) that pipeline-manager must `ps`-verify wrapper/claude-p PIDs before claiming any scheduled job is hung or orphaned.
