---
name: Pipeline-manager — ps-verify before claiming a job is hung or orphaned
description: Pipeline-manager must `ps -p <PID>` verify wrapper/claude-p PIDs from a scheduled-job log header BEFORE flagging the job as hung, orphan, or stuck. Log file size is not a liveness signal.
type: feedback
originSessionId: 326c69dd-5175-4205-89f6-eb4a9ec64ab8
---
**Rule:** When pipeline-manager scans `logs/scheduled/*.log` and considers flagging a scheduled job as hung/orphaned, it MUST `ps -p <PID> -o pid,etime,command` verify the wrapper and `claude -p` PIDs are actually still alive **before** surfacing the job as broken.

**Forbidden pattern:** Flagging a scheduled job as hung based on log file size (e.g., "log only contains start banner") or last-modified-time without ps-verifying the PIDs from the log header.

**Why:** Wrappers write a start banner immediately, then sit silent until the child `claude -p` finishes (which can take 5-30 min). Reading the log mid-run produces a misleading "only start banner" snapshot. On 2026-05-06 morning, pipeline-manager flagged TWO 🔴 broken-system items (niche-intelligence Tuesday, deal-aggregator 6 AM). Neither was hung — both jobs had already succeeded with exit 0 + validator PASS. The "still alive" PIDs the morning scan reported were already dead by the time launchd-debugger looked. False alarm cost a 🔴 Decision item slot on Kay's morning briefing AND triggered a debugger fan-out.

**How to apply:**
- Before any "hung job" / "orphan PID" / "stuck job" claim in a briefing, run:
  ```bash
  ps -p <wrapper_PID> -o pid,etime,command 2>/dev/null
  ps -p <claude_p_PID> -o pid,etime,command 2>/dev/null
  ```
- Decision tree:
  - PID alive AND elapsed time >2h → suspect, flag.
  - PID alive AND elapsed time <2h → still running, just slow. Don't flag. Re-check in 30 min.
  - PID dead → re-read the log file (it may have grown since the first read) and look for `exit 0` + `validator PASS` markers. If found, the job succeeded. Don't flag.
- Apply the same check to `health-monitor`'s scheduled-job rows. If health-monitor uses log-size heuristics, the same correction applies there.

**Source:** 2026-05-06 morning briefing false alarm. Trace at `brain/traces/2026-05-06-hung-jobs-false-alarm-stale-snapshot.md`. Pattern tag: `pattern/ps-verify-before-orphan-claim`.
