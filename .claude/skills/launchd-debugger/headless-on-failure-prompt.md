# launchd-debugger — Headless On-Failure Run

You are running the `launchd-debugger` skill non-interactively, triggered by the wrapper (`scripts/run-skill.sh`) immediately after another scheduled skill exited non-zero. There is no human in the loop. Do not ask clarifying questions, do not present YES/NO/DISCUSS gates, do not request approvals. You must finish in under 5 minutes — the failure just happened and Kay needs the verdict before the morning briefing.

The wrapper passed you the failed job's log path via the `LOG_FILE` environment variable. Your job is to diagnose THAT specific failure (not enumerate the last 24h), apply a safe operational fix or surface to Slack, and write the artifact entry.

## Mandatory ordering — execute in this exact sequence

1. **Read SKILL.md fully** at `.claude/skills/launchd-debugger/SKILL.md`. Internalise the FIX/SURFACE decision tree before doing anything.

2. **Capture start time** in epoch seconds:
   ```bash
   START_TS=$(date +%s)
   ```

3. **Read the FAILED_LOG_FILE env var** that the triggering wrapper set:
   ```bash
   if [ -z "$FAILED_LOG_FILE" ]; then
     echo "ON-FAILURE FATAL: FAILED_LOG_FILE env var not set by triggering wrapper" >&2
     exit 2
   fi
   echo "On-failure target: $FAILED_LOG_FILE"
   ```
   If `FAILED_LOG_FILE` is empty, exit 2 — this prompt requires the triggering wrapper to set it. (Note: the wrapper sets its OWN `LOG_FILE` for the per-run log path on line ~22, so we use a distinct env var name to avoid collision.)

4. **Load the known-incident registry** at `brain/trackers/health/known-incidents.json`:
   ```bash
   python3 -c "import json; print(json.dumps(json.load(open('brain/trackers/health/known-incidents.json'))['incidents']))" > /tmp/known-incidents.json
   ```
   Read into memory. Match logic: `entry.job == failure.job` AND `entry.root_cause_substring` appears in `failure.error_signature` or `failure.last_50_lines`. Active suppression = `suppress_until == "bead-closed"` OR `suppress_until` date in the future.

5. **Run the scanner against ONLY this log**:
   ```bash
   python3 scripts/scan_launchd_failures.py --log-file "$FAILED_LOG_FILE" > /tmp/launchd-failures.json
   ```
   Read `/tmp/launchd-failures.json`. Expected: a single-element list. If empty `[]`, the scanner did not detect a failure in this log — write a 0-failure artifact entry and exit clean (the wrapper's exit-non-zero may have been a false positive, e.g. a transient that did not write a failure marker). If list has more than one element, something is wrong — log a warning and process the first entry only.

6. **Spawn ONE Task subagent** for the single failure. Use the same brief as the daily prompt's Step 6 (FIX/SURFACE decision tree, hard prohibitions, JSON return shape):

   > You are debugging a SINGLE failed scheduled job. You have ONE job: read the log, identify root cause, and decide FIX or SURFACE.
   >
   > Job: `{job}`
   > Log path: `{last_log_path}`
   > Last mtime: `{last_log_mtime}`
   > Wrapper exit code: `{exit_code}`
   > Validator failed: `{validator_failed}`
   > Preflight failed: `{preflight_failed}`
   > Error signature: `{error_signature}`
   >
   > **Step A:** Read the full log at `{last_log_path}`. Also read the prior 1-2 logs for the same job (`ls logs/scheduled/{job}-*.log | tail -3`) to see if this is a first failure or a pattern.
   >
   > **Step B:** Classify the cause as ONE of: `AUTH`, `TRANSIENT_API`, `MCP_DISCONNECT`, `VALIDATOR_REJECT`, `MISSING_ARTIFACT`, `SCHEMA_VIOLATION`, `CODE_BUG`, `EXTERNAL_OUTAGE`, `UNKNOWN`.
   >
   > **Step C:** Decide FIX or SURFACE per the SKILL.md decision tree. The allowlist of fixes is narrow:
   >   - `launchctl start com.greenwich-barrow.{job}` (re-run)
   >   - `scripts/refresh-attio-snapshot.sh` / `scripts/refresh-jj-snapshot.sh` / `scripts/refresh-apollo-credits.sh` (regenerate cached artifact)
   >   - Restart MCP server: only via `claude mcp restart` if available; otherwise mark as SURFACE.
   > Anything else → SURFACE.
   >
   > **HARD PROHIBITIONS:**
   >   - No `rm`, no destructive shell.
   >   - No writes to Attio (no `mcp__attio__*` write tools), Drive, Sheets, or vault content (`brain/calls/`, `brain/entities/`, `brain/outputs/`, `brain/inbox/`).
   >   - No plist edits, no `.env.launchd` edits, no schema changes.
   >   - No `launchctl unload`/`launchctl load` — only `launchctl start`.
   >
   > **Step D:** If FIX, apply the fix. Then `launchctl start com.greenwich-barrow.{job}`. Sleep 60 seconds. Find the newest log for that job and read its tail to confirm `exit: 0`. If re-run also failed, downgrade to SURFACE.
   >
   > **Step E:** Return JSON only (no prose):
   > ```json
   > {
   >   "job": "{job}",
   >   "cause": "TRANSIENT_API",
   >   "action": "FIX",
   >   "fix_applied": "launchctl start com.greenwich-barrow.{job}",
   >   "rerun_exit_code": 0,
   >   "slack_text": null
   > }
   > ```
   > For SURFACE, populate `slack_text`: `launchd-debugger (on-failure): {job} FAILED — {cause}. {error_signature}. Recommended: {one-sentence action}. Log: {last_log_path}`.

7. **Apply suppression filters** (identical contract to daily prompt's Step 7):

   **a. Known-incident check** — if matched against an actively-suppressed incident, set `slack_posted: false`, `suppression_reason: "known-incident:{incident.id}"`, do NOT post.

   **b. Cross-day dedup check** — read prior 7 days of `brain/trackers/health/launchd-debugger-*.json`, build set of `(job, cause, error_signature[:50])` tuples where `slack_posted == true`. If current tuple matches, set `slack_posted: false`, `suppression_reason: "cross-day-dedup:7d"`, do NOT post. **Important:** include today's daily-mode artifact if it already exists — the on-failure run can fire after the 5am daily run on the same date.

   **c. Otherwise** post to Slack and set `slack_posted: true`.

   For `action: "FIX"` results, never post to Slack. Set `slack_posted: false`, `suppression_reason: "fix-succeeded"`.

8. **Write the artifact**. On-failure runs append to today's daily artifact if it exists, otherwise create a new one. Path: `brain/trackers/health/launchd-debugger-$(date +%Y-%m-%d).json`. Required schema (same as daily):
   ```json
   {
     "date": "YYYY-MM-DD",
     "scan_started_at": "ISO8601",
     "scan_finished_at": "ISO8601",
     "failures_detected": <int>,
     "fixes_attempted": <int>,
     "fixes_succeeded": <int>,
     "surfaces_to_slack": <int>,
     "runtime_seconds": <int>,
     "results": [...]
   }
   ```
   **Append behavior:** if the file exists, load it, append this run's result(s) to `results[]`, increment counters, update `scan_finished_at` to now, leave `scan_started_at` unchanged (it captures the daily run's start). If the file does not exist, create it fresh with this run's data — `scan_started_at` = the on-failure START_TS, `scan_finished_at` = now.

   Each result entry must carry `slack_posted` (bool), `suppression_reason` (string|null), AND `triggered_by: "on-failure"` so audits can distinguish daily-scan results from on-failure-trigger results.

9. **Print a one-line summary** to stdout:
   `launchd-debugger (on-failure): {job} → {action} ({cause}), slack_posted={true|false}, suppression={reason or none} — runtime {N}s`

The wrapper's POST_RUN_CHECK runs `scripts/validate_launchd_debugger_integrity.py` against the artifact (same validator as the daily run). If it fails, the wrapper overrides exit code and posts `VALIDATOR FAILED` to Slack — that's intentional, do not mask it.

## Forbidden in headless on-failure mode

- Scanning the full 24-hour window. Use `--log-file` only. The trigger already told you which log failed; enumerating others is wasted token spend.
- Asking the user anything.
- Self-triggering. The wrapper has a recursion guard (`SKILL_ARG != "launchd-debugger:on-failure"` check), but if you somehow find yourself debugging a launchd-debugger log, exit immediately with a stderr warning — do not attempt diagnosis.
- Posting to Slack without first running the suppression filter (known-incident + cross-day dedup).

## Why this prompt exists

The daily 5am scan catches everything that failed overnight, but a job that fails at 23:30 ET has 5.5 hours of staleness before the daily run picks it up — long enough that Kay's morning briefing reads stale state. v1.1 added auto-fire-on-failure so failures get diagnosed immediately, and this prompt is the single-failure-focused variant that runs in <5min instead of the daily's <10min budget.
