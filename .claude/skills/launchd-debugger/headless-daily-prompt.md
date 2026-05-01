# launchd-debugger — Headless Daily Run

You are running the `launchd-debugger` skill non-interactively under launchd at 5am ET. There is no human in the loop. Do not ask clarifying questions, do not present YES/NO/DISCUSS gates, do not request approvals.

Your job is to scan the last 24 hours of `logs/scheduled/`, fan out one debug subagent per failed job, attempt safe operational fixes, and surface anything unsafe to Slack #operations. You must finish in under 10 minutes.

## Mandatory ordering — execute in this exact sequence

1. **Read SKILL.md fully** at `.claude/skills/launchd-debugger/SKILL.md`. Internalise the FIX/SURFACE decision tree before doing anything.

2. **Capture start time** in epoch seconds (you'll need it for `runtime_seconds` in the artifact):
   ```bash
   START_TS=$(date +%s)
   ```

3. **Run the scanner** and capture its JSON output:
   ```bash
   python3 scripts/scan_launchd_failures.py > /tmp/launchd-failures.json
   ```
   Read `/tmp/launchd-failures.json`.

4. **Branch on result:**
   - **Empty list `[]`** → skip to Step 7 (write artifact with `failures_detected: 0`, exit clean, no Slack).
   - **Non-empty** → proceed to Step 5.

5. **Spawn one Task subagent per failure, in parallel.** Each subagent gets this exact brief (substitute the entry's fields):

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
   > For SURFACE, populate `slack_text` with a single-line message: `launchd-debugger: {job} FAILED — {cause}. {error_signature}. Recommended: {one-sentence action}. Log: {last_log_path}`.

6. **Collect subagent results.** For every result with `action: "SURFACE"` and a non-null `slack_text`, post to Slack:
   ```bash
   curl -s -X POST "$SLACK_WEBHOOK_OPERATIONS" \
     -H 'Content-type: application/json' \
     -d "{\"text\":\"$SLACK_TEXT\"}"
   ```
   For `action: "FIX"` results, do NOT post to Slack. Silence = self-healed.

7. **Write the artifact** to `brain/trackers/health/launchd-debugger-$(date +%Y-%m-%d).json` with these required fields:
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
     "results": [...subagent JSON results...]
   }
   ```
   Compute `runtime_seconds` as `$(date +%s) - $START_TS`. Ensure `brain/trackers/health/` exists (`mkdir -p`).

8. **Print a one-line summary** to stdout for the launchd log:
   `launchd-debugger: {failures_detected} failures, {fixes_succeeded}/{fixes_attempted} fixed, {surfaces_to_slack} surfaced — runtime {N}s`

The wrapper's POST_RUN_CHECK runs `scripts/validate_launchd_debugger_integrity.py` which confirms the artifact exists with all required fields. If the validator exits non-zero, the wrapper overrides the exit code and posts `VALIDATOR FAILED` to Slack — that's intentional, do not catch or mask it.

## Forbidden in headless mode

- Asking the user anything.
- Presenting RECOMMEND / YES / NO / DISCUSS framings.
- Skipping the artifact write (validator will fail and you'll get a Slack alert).
- Spawning subagents sequentially when they can run in parallel.
- Performing any business-data write to recover a job. Repair is operational only.

## Why this prompt exists

Bare `claude -p '/launchd-debugger'` invocations under launchd risk the silent-exit-0 failure mode documented in `memory/feedback_mutating_skill_hardening_pattern.md`. This prompt forbids that path and mandates artifact-first ordering so the validator can backstop.
