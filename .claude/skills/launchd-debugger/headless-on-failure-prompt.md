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

## When triggered from health-monitor RED bridge

v1.2 adds a second trigger path: `scripts/health-monitor-red-bridge.sh` reads health-monitor's weekly markdown artifact (`brain/trackers/health/{TODAY}-health.md`) and fires this prompt **once per RED row** in the standard health tables. RED-only — yellow rows stay informational. The Trend table is filtered out (it cites historical RED states for resolved items).

When the triggering path is the bridge instead of a direct on-failure spawn, `FAILED_LOG_FILE` is **not** set. Instead, these env vars are populated:

- `FROM_HEALTH_BRIDGE=1` — sentinel that this prompt was bridge-triggered
- `RED_ITEM_ID` — slugified label (e.g. `launchd-niche-intelligence-tue`, `stale-entries`, `missing-vault-entities`, `orphaned-entity-links`)
- `RED_ITEM_LABEL` — the raw label string from column 2 of the markdown table
- `RED_ITEM_DETAIL` — the full detail string from column 4 (may contain a recommended-action sentence, may not)
- `HEALTH_ARTIFACT_PATH` — abs path to the health-monitor `.md` artifact this RED came from

### Decision flow when bridge-triggered

1. **Check `FROM_HEALTH_BRIDGE` first.** If set to `1`, skip the `FAILED_LOG_FILE` validation in step 3. Replace the scanner step (5) with: build a synthetic single-element failure list directly from the env vars:
   ```json
   [{
     "job": "health-monitor-red:{RED_ITEM_ID}",
     "last_log_path": "{HEALTH_ARTIFACT_PATH}",
     "last_log_mtime": "(mtime of HEALTH_ARTIFACT_PATH)",
     "exit_code": null,
     "validator_failed": false,
     "preflight_failed": false,
     "last_50_lines": "(RED_ITEM_DETAIL verbatim)",
     "error_signature": "RED: {RED_ITEM_LABEL} — {first 80 chars of RED_ITEM_DETAIL}"
   }]
   ```
   Do NOT call `scan_launchd_failures.py` — there's no log-file to scan. The RED detail string IS the diagnostic context.

2. **Spawn the same single subagent** (step 6) but with this brief instead:
   > You are diagnosing a health-monitor RED finding (not a launchd job failure). The RED item is:
   >
   > Label: `{RED_ITEM_LABEL}`
   > ID: `{RED_ITEM_ID}`
   > Detail: `{RED_ITEM_DETAIL}`
   > Source artifact: `{HEALTH_ARTIFACT_PATH}`
   >
   > **Step A:** Read the source artifact section that contains this label so you have surrounding context (the RED row sits in one of: Service Connectivity / Infrastructure / Pipeline Hygiene / Data Integrity).
   >
   > **Step B:** Classify the cause using the same enum (AUTH, TRANSIENT_API, MCP_DISCONNECT, VALIDATOR_REJECT, MISSING_ARTIFACT, SCHEMA_VIOLATION, CODE_BUG, EXTERNAL_OUTAGE, UNKNOWN). For pipeline/data-integrity REDs that are not infrastructure failures (e.g. "stale entries", "missing vault entities", "orphaned entity links"), classify as `UNKNOWN` — these need Kay's judgment, not an operational fix.
   >
   > **Step C:** Decision tree. The fix allowlist remains narrow:
   >   - `launchctl start com.greenwich-barrow.{job}` for infrastructure REDs that name a launchd job in the label (`launchd: {name}`).
   >   - Cached-snapshot regen (`scripts/refresh-attio-snapshot.sh` etc.) when label is "{name} snapshot stale".
   >   - **Anything else (pipeline staleness, missing entities, orphan links, drift) → SURFACE.** These are not operational fixes — they are work items for Kay.
   >
   > **HARD PROHIBITIONS** are unchanged from the on-failure brief — no destructive shell, no Attio/Drive/Sheets/vault content writes, no plist edits, no `launchctl unload/load`.
   >
   > **Step D:** If FIX, apply + re-run + verify exit 0 (same protocol). If SURFACE, populate `slack_text` as: `health-monitor RED: {RED_ITEM_LABEL} — {cause}. Detail: {RED_ITEM_DETAIL[:200]}. Recommended: {one-sentence action from the RED detail if present, else "Walk with Kay during Friday meta-calibration."}. Source: {HEALTH_ARTIFACT_PATH}`.
   >
   > **Step E:** Return JSON in the same shape as the on-failure brief, with `job` set to `health-monitor-red:{RED_ITEM_ID}`.

3. **Suppression filters apply unchanged.** Cross-day-dedup keys on `(job, cause, error_signature[:50])` — for bridge-triggered runs, `job` is `health-monitor-red:{RED_ITEM_ID}` so a RED that persists week-over-week (e.g. orphan-entity-links growing 22 → 46 → 89) dedups itself across firings without spamming Slack. Known-incident registry can suppress specific REDs by adding an entry with `job: "health-monitor-red:{slug}"`.

4. **Artifact append.** Same target path (`brain/trackers/health/launchd-debugger-{YYYY-MM-DD}.json`), same append behavior. Each result entry must additionally carry `triggered_by: "health-monitor-red-bridge"` (replaces `"on-failure"` for bridge-triggered runs) so the validator and audit can distinguish three trigger sources: daily-scan / on-failure / health-monitor-red-bridge.

### What the bridge does NOT do

- It does **not** fire for YELLOW rows (informational only).
- It does **not** fire for the Trend table (historical states, not current).
- It does **not** fire when health-monitor itself failed (the v1.1 on-failure auto-fire handles that).
- It does **not** fire when health-monitor's POST_RUN_CHECK validator rejected the artifact (same v1.1 path).
- It does **not** retry on its own. Recursion guard: if `FROM_HEALTH_BRIDGE=1` is set when run-skill.sh evaluates the bridge call, the bridge script exits 0 without firing. If the diagnosing subagent itself fails, the wrapper's existing on-failure auto-fire handles the diagnosis loop — which then sees `SKILL_NAME == "launchd-debugger"` and short-circuits, preventing infinite recursion.
