---
name: launchd-debugger
description: "Daily 5am ET scan of overnight launchd job logs. Spawns a debug subagent per failed job to diagnose, attempt safe fixes (re-run, restart, retry transient), or surface to Slack #operations. Catches silent failures before the morning briefing."
user_invocable: true
trigger: "Scheduled daily 5:00am ET via launchd (com.greenwich-barrow.launchd-debugger). Runs after overnight jobs complete and before goodmorning workflow at 7am."
schedule: "Daily 5:00am ET"
context_budget:
  skill_md: 1200
  max_references: 0
  sub_agent_limit: 2000
---

<objective>
Health-monitor catches silent overnight failures *post hoc* — it observes, it does not repair. Every Friday it surfaces a list of REDs that have already cost a morning. This skill is the agents-all-the-way-down repair layer Harrison Wells recommended: a daily cron that detects every failed scheduled job in the last 24h, spawns a debug subagent per failure, and either applies a safe operational fix and re-runs the job OR posts a diagnosis to Slack #operations with a recommended action.

The skill never touches business data. Fixes are operational only — re-run, regenerate cached artifact, restart MCP server, retry transient API. Anything else is escalated as a SURFACE, not a FIX.
</objective>

<scope>
## What this skill OWNS

- Detection: scan `logs/scheduled/*.log` for files modified in last 24h with non-zero exit, `VALIDATOR FAILED`, `PREFLIGHT FAILED`, or `STOP:` markers.
- Per-failure diagnosis via Task subagent.
- Safe operational fix attempts (whitelist below).
- Re-run via `launchctl start com.greenwich-barrow.{skill}` after a fix.
- Slack #operations notification when fix is unsafe or fails.
- Daily artifact at `brain/trackers/health/launchd-debugger-{YYYY-MM-DD}.json` for validator + audit trail.

## What this skill does NOT do

- Cannot rewrite plists or change schedules (that's Kay).
- Cannot touch Attio, Drive, vault content (calls/entities/outputs), or Sheets.
- Does not duplicate health-monitor's broader checks (service connectivity, pipeline hygiene, data freshness). Health-monitor still owns those — this skill targets the narrow "did the cron run successfully" question.
- Does not evaluate whether a skill's *output* was correct. The POST_RUN_CHECK validators on each mutating skill own that — this skill only fans out on validator-flagged failures.
</scope>

<workflow>
## Step 1 — Scan for failures

```bash
python3 scripts/scan_launchd_failures.py
```

Returns JSON list. Empty = clean run; write the artifact, exit 0, no Slack.

Each failure entry has:
- `job` — skill name (e.g. `nightly-tracker-audit`)
- `last_log_path` — abs path to most recent failed log
- `last_log_mtime` — ISO timestamp
- `exit_code` — wrapper's final exit (after POST_RUN_CHECK override)
- `validator_failed` — true if POST_RUN_CHECK rejected
- `preflight_failed` — true if Claude CLI 401
- `last_50_lines` — log tail for context
- `error_signature` — one-line diagnostic

## Step 2 — Spawn one debug subagent per failure

For each failure, launch a Task subagent with this brief:

> You are debugging a single failed scheduled job. You have ONE job: read the full log, identify root cause, and decide FIX or SURFACE.
>
> Job: `{job}`
> Log path: `{last_log_path}`
> Error signature: `{error_signature}`
>
> Step 1: Read the full log file.
> Step 2: Classify the cause into one of: AUTH, TRANSIENT_API, MCP_DISCONNECT, VALIDATOR_REJECT, MISSING_ARTIFACT, SCHEMA_VIOLATION, CODE_BUG, EXTERNAL_OUTAGE, UNKNOWN.
> Step 3: Decide FIX vs SURFACE per the decision tree below.
> Step 4: If FIX, apply the fix, then `launchctl start com.greenwich-barrow.{job}` to re-run. Wait 60s. Re-scan that one log file to verify success.
> Step 5: Return JSON: `{job, cause, action: "FIX"|"SURFACE", fix_applied?, rerun_exit_code?, slack_text?}`

Run subagents in parallel — they share no state.

## Step 3 — Decision tree (FIX vs SURFACE)

| Cause | Action | Allowed fix |
|-------|--------|-------------|
| AUTH (Claude CLI 401, OAuth token expired) | SURFACE | none — Kay must re-auth |
| TRANSIENT_API (5xx, network timeout, rate-limited 429) | FIX | re-run via `launchctl start` |
| MCP_DISCONNECT (mcp__attio, mcp__granola, mcp__superhuman returns "not connected") | FIX | reconnect via `claude mcp restart` (if available) OR mark for manual `/mcp` reconnect, then re-run |
| VALIDATOR_REJECT (POST_RUN_CHECK said skill output was wrong) | SURFACE | never auto-fix sheet/Attio drift — Kay reviews |
| MISSING_ARTIFACT (cached snapshot didn't refresh) | FIX | regenerate via `scripts/refresh-{name}.sh`, then re-run |
| SCHEMA_VIOLATION (vault write rejected by validate-edits.py) | SURFACE | code change required |
| CODE_BUG (Python traceback, undefined var, etc.) | SURFACE | code change required |
| EXTERNAL_OUTAGE (vendor down — Apollo/Anthropic/Google) | SURFACE | wait for vendor |
| UNKNOWN | SURFACE | always |

**Hard prohibitions (any violation = SURFACE):**
- No `rm`, no `git reset --hard`, no destructive shell ops.
- No writes to Attio (no MCP `mcp__attio__update_record` etc.).
- No writes to vault content (`brain/calls/`, `brain/entities/`, `brain/outputs/`, `brain/inbox/`).
- No writes to Google Sheets, Drive, or Docs.
- No schema changes, no plist edits, no `.env.launchd` edits.
- No `launchctl unload` or `launchctl load` — only `launchctl start` (one-shot re-run).

## Step 4 — Aggregate + write artifact

Write `brain/trackers/health/launchd-debugger-{YYYY-MM-DD}.json`:

```json
{
  "date": "2026-05-01",
  "scan_started_at": "2026-05-01T05:00:00-04:00",
  "scan_finished_at": "2026-05-01T05:04:23-04:00",
  "failures_detected": 2,
  "fixes_attempted": 1,
  "fixes_succeeded": 1,
  "surfaces_to_slack": 1,
  "runtime_seconds": 263,
  "results": [
    {
      "job": "nightly-tracker-audit",
      "cause": "VALIDATOR_REJECT",
      "action": "SURFACE",
      "slack_text": "..."
    },
    {
      "job": "attio-snapshot-refresh",
      "cause": "TRANSIENT_API",
      "action": "FIX",
      "fix_applied": "launchctl start com.greenwich-barrow.attio-snapshot-refresh",
      "rerun_exit_code": 0
    }
  ]
}
```

## Step 5 — Slack notify

For every SURFACE, post one message to `$SLACK_WEBHOOK_OPERATIONS`:

```
launchd-debugger: {job} FAILED — {cause}
Signature: {error_signature}
Recommended action: {one sentence}
Log: {last_log_path}
```

For successful FIXes, no Slack — silence = self-healed. The artifact records the fix.

If the scan returned zero failures, no Slack at all.
</workflow>

<integration>
## Integration with existing infra

- **Logs:** Reads `logs/scheduled/*.log` produced by `scripts/run-skill.sh`. Writes its own log to `logs/scheduled/launchd-debugger-{date}-{HHMM}.log` via the same wrapper.
- **Wrapper:** Invoked via `scripts/run-skill.sh launchd-debugger:daily` — wrapper case routes to `headless-daily-prompt.md`.
- **POST_RUN_CHECK:** `scripts/validate_launchd_debugger_integrity.py` confirms the artifact exists with required fields. Per `feedback_mutating_skill_hardening_pattern.md`, this skill is treated as mutating because it can `launchctl start` other jobs.
- **Slack:** `$SLACK_WEBHOOK_OPERATIONS` from `scripts/.env.launchd`.
- **Health-monitor relationship:** Health-monitor still runs Friday 12:30am — it still detects silent failures across the *whole system*. This skill is the *narrow daily* layer that catches launchd failures specifically and tries to self-heal before the morning briefing.
</integration>

<success_criteria>
- [ ] `scan_launchd_failures.py` ran without script-level error.
- [ ] Every detected failure spawned a debug subagent that returned a verdict.
- [ ] Every FIX action either succeeded (re-run exit 0) or was downgraded to SURFACE on retry failure.
- [ ] Every SURFACE has a Slack message posted to #operations.
- [ ] Artifact written to `brain/trackers/health/launchd-debugger-{date}.json` with all required fields.
- [ ] No write to Attio / Drive / Sheets / vault content.
- [ ] Validator (`validate_launchd_debugger_integrity.py`) exits 0.
</success_criteria>
