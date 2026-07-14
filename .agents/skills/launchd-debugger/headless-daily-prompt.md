# launchd-debugger — Headless Daily Run

You are running the `launchd-debugger` skill non-interactively under the Codex/systemd scheduled runner at 8:20am ET. There is no human in the loop. Do not ask clarifying questions, do not present YES/NO/DISCUSS gates, do not request approvals.

Your job is to scan the last 24 hours of `logs/scheduled/`, fan out one debug subagent per failed job, attempt safe operational fixes, and surface anything unsafe to Slack #operations. You must finish in under 10 minutes.

## Mandatory ordering — execute in this exact sequence

1. **Read SKILL.md fully** at `.agents/skills/launchd-debugger/SKILL.md`. Internalise the FIX/SURFACE decision tree before doing anything.

2. **Capture start time** in epoch seconds (you'll need it for `runtime_seconds` in the artifact):
   ```bash
   START_TS=$(date +%s)
   ```

3. **Load the known-incident registry** at `brain/trackers/health/known-incidents.json`:
   ```bash
   python3 -c "import json; print(json.dumps(json.load(open('brain/trackers/health/known-incidents.json'))['incidents']))" > /tmp/known-incidents.json
   ```
   Read `/tmp/known-incidents.json` into memory. Each entry has `job`, `root_cause_substring`, `suppress_until`. A failure matches an incident when `entry.job == failure.job` AND `entry.root_cause_substring` appears in `failure.error_signature` or `failure.last_50_lines`. Matches with `suppress_until == "bead-closed"` OR `suppress_until` date in the future → SUPPRESS Slack post (still write artifact entry).

4. **Run the scanner** and capture its JSON output:
   ```bash
   python3 scripts/scan_launchd_failures.py > /tmp/launchd-failures.json
   ```
   Read `/tmp/launchd-failures.json`.

5. **Branch on result:**
   - **Empty list `[]`** → skip to Step 9. Write a zero-failure daily scan, but first preserve any existing same-day `results[]` entries from earlier `on-failure` or `health-monitor-red-bridge` runs. Do not overwrite bridge/on-failure entries with an empty daily scan.
   - **Non-empty** → proceed to Step 6.

6. **Spawn one Task subagent per failure, in parallel.** Each subagent gets this exact brief (substitute the entry's fields):

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
  >   - `systemctl --user start {job}.service` (one-shot re-run)
  >   - `scripts/refresh-attio-snapshot.sh` / `scripts/refresh-jj-snapshot.sh` (legacy cold-call snapshot filename) / `scripts/refresh-apollo-credits.sh` (regenerate cached artifact)
   >   - Do not reconnect MCP in scheduled mode. If REST/wrapper health is good, mark as SURFACE with `SKILL_CODE_NEEDS_REST_FALLBACK`; if REST/wrapper health is down, classify the real auth/outage cause.
   > Anything else → SURFACE. For validator/schema/idempotency wiring bugs, set cause `VALIDATOR_REJECT`, action `SURFACE`, and include `SKILL_CODE_NEEDS_FIX` in `slack_text` / `error_signature` context so it is not mistaken for business-data drift.
   >
   > **HARD PROHIBITIONS:**
   >   - No `rm`, no destructive shell.
   >   - No writes to Attio (no `mcp__attio__*` write tools), Drive, Sheets, or vault content (`brain/calls/`, `brain/entities/`, `brain/outputs/`, `brain/inbox/`).
  >   - No systemd unit edits, no `.env.launchd` edits, no schema changes.
  >   - No `systemctl --user disable`, `enable`, `stop`, or daemon-reload — only `systemctl --user start {job}.service`.
   >
  > **Step D:** If FIX, apply the fix. Then `systemctl --user start {job}.service`. Sleep 60 seconds. Find the newest log for that job and read its tail to confirm completion. If re-run also failed, downgrade to SURFACE.
   >
   > **Step E:** Return JSON only (no prose):
   > ```json
   > {
   >   "job": "{job}",
   >   "cause": "TRANSIENT_API",
   >   "action": "FIX",
  >   "fix_applied": "systemctl --user start {job}.service",
   >   "rerun_exit_code": 0,
   >   "slack_text": null
   > }
   > ```
   > For SURFACE, populate `slack_text` with a single-line message: `launchd-debugger: {job} FAILED — {cause}. {error_signature}. Recommended: {one-sentence action}. Log: {last_log_path}`.

7. **Apply suppression filters before posting to Slack.** For each subagent result with `action == "SURFACE"`:

   **a. Known-incident check** (from Step 3): if the failure matches a registered incident with active suppression, set `slack_posted: false`, set `suppression_reason: "known-incident:{incident.id}"`, do NOT post to Slack.

   **b. Cross-day dedup check.** Read prior artifacts for the last 7 days:
   ```bash
   python3 - <<'PY'
   import json, glob, os
   from datetime import date, timedelta
   today = date.today()
   recent = []
   for d in range(1, 8):
       day = (today - timedelta(days=d)).isoformat()
       p = f"brain/trackers/health/launchd-debugger-{day}.json"
       if os.path.exists(p):
           with open(p) as f:
               recent.append(json.load(f))
   print(json.dumps(recent))
   PY
   ```
   Build a set of prior signature tuples: `(result.job, result.cause, result.error_signature[:50])` from every artifact entry where `slack_posted == true`. If the current failure's tuple already appears, set `slack_posted: false`, set `suppression_reason: "cross-day-dedup:7d"`, do NOT post to Slack. Exception: if `slack_text` or `error_signature` contains `SKILL_CODE_NEEDS_FIX`, do not apply cross-day dedup unless a known-incident entry matches; code/validator wiring regressions must stay visible until fixed or explicitly tracked.

   **c. If neither suppression triggered**, post to Slack and set `slack_posted: true`:
   ```bash
   curl -s -X POST "$SLACK_WEBHOOK_OPERATIONS" \
     -H 'Content-type: application/json' \
     -d "{\"text\":\"$SLACK_TEXT\"}"
   ```

   For `action: "FIX"` results, do NOT post to Slack regardless. Silence = self-healed. Set `slack_posted: false`, `suppression_reason: "fix-succeeded"`.

8. **Augment subagent results with suppression metadata** before writing the artifact. Each result entry must carry `slack_posted` (bool) and `suppression_reason` (string|null) so the next day's dedup can read them and so an audit can show why a SURFACE didn't ping Slack.

9. **Write the artifact** to `brain/trackers/health/launchd-debugger-$(date +%Y-%m-%d).json` with these required fields. If the file already exists, load it first and preserve existing `results[]` entries plus their counters. Append this daily scan result set to the existing artifact rather than replacing it. When the daily scan has zero failures and an existing artifact already has bridge/on-failure entries, update `scan_finished_at` and `runtime_seconds` but leave the existing failure counters/results intact:
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
     "results": [
       {
         "job": "...",
         "cause": "...",
         "action": "FIX|SURFACE",
         "slack_posted": true|false,
         "suppression_reason": "known-incident:ai-ops-5wx | cross-day-dedup:7d | fix-succeeded | null",
         "...": "..."
       }
     ]
   }
   ```
   Note: `surfaces_to_slack` counts only entries with `action == "SURFACE"` AND `slack_posted == true`. Suppressed surfaces count toward `failures_detected` but NOT `surfaces_to_slack`. Validator's accounting check still passes because `fixes_succeeded + surfaces_to_slack + suppressed_count == failures_detected`. Compute `runtime_seconds` as `$(date +%s) - $START_TS`. Ensure `brain/trackers/health/` exists (`mkdir -p`).

10. **Print a one-line summary** to stdout for the scheduled log:
    `launchd-debugger: {failures_detected} failures, {fixes_succeeded}/{fixes_attempted} fixed, {surfaces_to_slack} surfaced, {suppressed} suppressed — runtime {N}s`

The wrapper's POST_RUN_CHECK runs `scripts/validate_launchd_debugger_integrity.py` which confirms the artifact exists with all required fields. If the validator exits non-zero, the wrapper overrides the exit code and posts `VALIDATOR FAILED` to Slack — that's intentional, do not catch or mask it.

## Forbidden in headless mode

- Asking the user anything.
- Presenting RECOMMEND / YES / NO / DISCUSS framings.
- Skipping the artifact write (validator will fail and you'll get a Slack alert).
- Spawning subagents sequentially when they can run in parallel.
- Performing any business-data write to recover a job. Repair is operational only.
- Posting to Slack without first running the suppression filter (known-incident + cross-day dedup).

## Why this prompt exists

Bare slash-command invocations in scheduled mode risk the silent-exit-0 failure mode documented in `memory/feedback_mutating_skill_hardening_pattern.md`. This prompt forbids that path and mandates artifact-first ordering so the validator can backstop. v1.1 added known-incident registry + cross-day dedup so a single open bug doesn't generate N Slack pings/day across the bug's open lifetime.
