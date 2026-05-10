#!/bin/bash
# Shared wrapper for all scheduled Claude skill runs
# Usage: run-skill.sh <skill-name>

SKILL_NAME="$1"
shift
SKILL_ARGS="$*"

# Some plists pass skill+mode as a single colon-joined arg (e.g.
# "jj-operations:sunday-prep") instead of two separate strings. Split it so the
# headless-prompt case statement below matches. Without this, $SKILL_NAME ends
# up as the full "name:mode" string and the case pattern never matches —
# wrapper falls through to bare `claude -p '/name:mode'` which Claude rejects
# as "Unknown command" and exits 0 silently. Confirmed root cause for every
# Sunday jj-operations failure since the plist was created (fix 2026-04-27).
if [[ -z "$SKILL_ARGS" && "$SKILL_NAME" == *:* ]]; then
  SKILL_ARGS="${SKILL_NAME#*:}"
  SKILL_NAME="${SKILL_NAME%%:*}"
fi
WORKDIR="$(cd "$(dirname "$0")/.." && pwd)"
LOG_DIR="$WORKDIR/logs/scheduled"
# LOG_PREFIX env var lets a plist write logs under a name that matches its
# launchd Label when SKILL_NAME alone is ambiguous. Required for skills whose
# plists pass colon-joined args (e.g. jj-operations:sunday-prep) — without
# this, the wrapper writes "jj-operations-{date}.log" and the dashboard
# canary on the launchd-label "jj-operations-sunday" reads as "missed"
# even though the run succeeded. Default = SKILL_NAME (post-colon-split).
LOG_FILE="$LOG_DIR/${LOG_PREFIX:-$SKILL_NAME}-$(date +%Y-%m-%d-%H%M).log"

# Source env (launchd doesn't read .zshrc). load_env helper resolves any
# op:// references via 1Password if op CLI is available; otherwise sources
# the file as-is.
# shellcheck disable=SC1091
source "$WORKDIR/scripts/load-env.sh"
load_env "$WORKDIR/scripts/.env.launchd"

# Export GOG_ACCOUNT for subprocesses that call `gog` without --account
# (notably the POST_RUN_CHECK validators in scripts/validate_*_integrity.py).
# Under launchd's empty env, those calls fail with "missing --account". Not
# kept in .env.launchd because the email is not a secret. Override-friendly:
# if a plist or a future .env.launchd export defines GOG_ACCOUNT, that wins.
export GOG_ACCOUNT="${GOG_ACCOUNT:-kay.s@greenwichandbarrow.com}"

# Raise file descriptor limit (launchd defaults to 256, Claude needs more)
ulimit -n 2147483646 2>/dev/null || ulimit -n 65536 2>/dev/null || true

# Ensure log dir exists, rotate old logs (14 days)
mkdir -p "$LOG_DIR"
find "$LOG_DIR" -name "*.log" -mtime +14 -delete 2>/dev/null

cd "$WORKDIR"

echo "=== $SKILL_NAME ===" >> "$LOG_FILE"
echo "Started: $(date)" >> "$LOG_FILE"

# Preflight: unlock login keychain if a password is provided (prevents 401 on locked keychain)
# Safe because KEYCHAIN_PASSWORD lives only in .env.launchd (not committed)
# Gated on `security` existing — macOS only; silently skipped on Linux.
if [ -n "$KEYCHAIN_PASSWORD" ] && command -v security >/dev/null 2>&1; then
  security unlock-keychain -p "$KEYCHAIN_PASSWORD" "$HOME/Library/Keychains/login.keychain-db" 2>/dev/null || \
    echo "WARN: keychain unlock failed" >> "$LOG_FILE"
fi

# Preflight: verify Claude CLI auth before spending a run on a 401
PREFLIGHT=$(echo "say OK" | "$HOME/.local/bin/claude" -p --dangerously-skip-permissions 2>&1 | head -3)
if echo "$PREFLIGHT" | grep -qE "401|authentication_error|Invalid authentication"; then
  echo "PREFLIGHT FAILED (auth): $PREFLIGHT" >> "$LOG_FILE"
  curl -s -X POST "$SLACK_WEBHOOK_OPERATIONS" \
    -H 'Content-type: application/json' \
    -d "{\"text\":\"PREFLIGHT AUTH FAIL for $SKILL_NAME — Claude CLI 401. Kay must re-auth via \`claude\` command.\"}"
  exit 2
fi

# Headless-prompt resolution. If SKILL_ARGS names a mode that has a
# headless prompt file, pipe its contents to Claude as a self-contained
# user prompt instead of bare /skill-name. Avoids the "interactive
# clarifying question → exit 0" silent-failure pattern that hit
# target-discovery Phase 2 on 2026-04-19.
HEADLESS_PROMPT_FILE=""
case "$SKILL_NAME:$SKILL_ARGS" in
  "target-discovery:phase2-sunday")
    HEADLESS_PROMPT_FILE="$WORKDIR/.claude/skills/target-discovery/headless-phase2-prompt.md"
    ;;
  "weekly-tracker:friday")
    HEADLESS_PROMPT_FILE="$WORKDIR/.claude/skills/weekly-tracker/headless-friday-prompt.md"
    ;;
  "nightly-tracker-audit:nightly")
    HEADLESS_PROMPT_FILE="$WORKDIR/.claude/skills/nightly-tracker-audit/headless-nightly-prompt.md"
    ;;
  "relationship-manager:daily")
    HEADLESS_PROMPT_FILE="$WORKDIR/.claude/skills/relationship-manager/headless-daily-prompt.md"
    ;;
  "jj-operations:sunday-prep")
    HEADLESS_PROMPT_FILE="$WORKDIR/.claude/skills/jj-operations/headless-sunday-prep-prompt.md"
    ;;
  "launchd-debugger:daily")
    HEADLESS_PROMPT_FILE="$WORKDIR/.claude/skills/launchd-debugger/headless-daily-prompt.md"
    ;;
  "launchd-debugger:on-failure")
    # On-failure mode triggered by the failure-trigger block at the bottom of
    # this wrapper. The triggering wrapper sets LOG_FILE env var pointing at
    # the just-failed log; the on-failure prompt reads it and runs scan with
    # --log-file instead of --lookback-hours. Single-failure-focused (<5min).
    HEADLESS_PROMPT_FILE="$WORKDIR/.claude/skills/launchd-debugger/headless-on-failure-prompt.md"
    ;;
  "niche-intelligence:tuesday")
    # Tuesday 22:30 ET fire. Agent B is building the niche-intelligence
    # hardening files in parallel (headless-tuesday-prompt.md + validator).
    # This case routes the wrapper correctly so when their plist update
    # lands, the headless prompt loads instead of the bare /niche-intelligence
    # invocation that has failed every Tuesday with "An unknown error
    # occurred (Unexpected)" (bead ai-ops-5wx).
    HEADLESS_PROMPT_FILE="$WORKDIR/.claude/skills/niche-intelligence/headless-tuesday-prompt.md"
    POST_RUN_CHECK="${POST_RUN_CHECK:-python3 \"$WORKDIR/scripts/validate_niche_intelligence_integrity.py\"}"
    ;;
  "deal-aggregator:")
    # Bare `run-skill.sh deal-aggregator` (Mon-Fri 6am morning fire — empty
    # args). Route to the morning headless prompt to forbid operator-question
    # framings and enforce idempotency-gate against double-write. Fix added
    # 2026-04-28 after morning run produced `RECOMMEND: ... → YES/NO/DISCUSS`
    # meta-output instead of executing.
    #
    # 2026-04-30 experimental fingerprint-comparison variant retired — date
    # gate already past, file remains on disk (dead code, harmless).
    HEADLESS_PROMPT_FILE="$WORKDIR/.claude/skills/deal-aggregator/headless-morning-prompt.md"
    # POST_RUN_CHECK added 2026-05-02 (launchd-debugger investigation).
    # Catches the silent-success failure mode: 4/27 + 4/30 morning runs
    # exited 0 but no artifact landed because Claude emitted operator-
    # question framings instead of executing. Validator non-zero → wrapper
    # overrides exit code → Slack alert fires. Pattern: `feedback_mutating
    # _skill_hardening_pattern.md`.
    POST_RUN_CHECK="${POST_RUN_CHECK:-python3 \"$WORKDIR/scripts/validate_deal_aggregator_integrity.py\" --mode morning --date \$TODAY}"
    ;;
  "deal-aggregator:--afternoon")
    # Mon-Fri 2pm afternoon top-up. Lighter scan (Channel 2 + time-sensitive
    # platforms only). Writes separate artifact at
    # brain/context/deal-aggregator-scan-{TODAY}-afternoon.md — never
    # overwrites morning. Hardened 2026-04-28 same incident as morning.
    HEADLESS_PROMPT_FILE="$WORKDIR/.claude/skills/deal-aggregator/headless-afternoon-prompt.md"
    POST_RUN_CHECK="${POST_RUN_CHECK:-python3 \"$WORKDIR/scripts/validate_deal_aggregator_integrity.py\" --mode afternoon --date \$TODAY}"
    ;;
  "conference-discovery:sunday")
    # Sunday 21:00 ET weekly conference discovery + auto-archival cycle.
    # Hardened 2026-05-04 after the 2026-05-03 incident where the archival
    # subagent wiped ~70 rows from the Pipeline tab and exited 0 silently.
    # Headless prompt mandates pre-run snapshot to brain/context/rollback-
    # snapshots/conference-pipeline-pre-run-{TODAY}.json BEFORE any Pipeline
    # mutation. Validator compares post-run live row count against snapshot
    # row_count; rejects if delta exceeds MAX_ARCHIVAL_DELTA (15).
    HEADLESS_PROMPT_FILE="$WORKDIR/.claude/skills/conference-discovery/headless-sunday-prompt.md"
    POST_RUN_CHECK="${POST_RUN_CHECK:-python3 \"$WORKDIR/scripts/validate_conference_discovery_integrity.py\" --date \$TODAY}"
    ;;
  "post-call-analyzer:on-trigger")
    # Triggered by scripts/post_call_analyzer_poll.py when new Granola docs
    # land in brain/trackers/post-call-analyzer/queue/. Headless prompt drains
    # the queue, writes vault call notes, routes action items to task-tracker
    # + Gmail drafts, posts ONE Slack message per call. NEVER sends email.
    HEADLESS_PROMPT_FILE="$WORKDIR/.claude/skills/post-call-analyzer/headless-on-trigger-prompt.md"
    POST_RUN_CHECK="${POST_RUN_CHECK:-python3 \"$WORKDIR/scripts/validate_post_call_analyzer_integrity.py\"}"
    ;;
  "deal-aggregator:--digest-mode")
    # Friday 6am weekly source-productivity digest (Phase 2). Reads 7 days of
    # daily scorecards + 30 days of fingerprints + 7 days of email-scan-results
    # + Sourcing Sheet. Writes brain/trackers/weekly/{TODAY}-deal-aggregator-
    # digest.md. Slack only on ≥1 proposed change OR volume=🔴. Never
    # auto-writes to Sourcing Sheet. Hardened 2026-04-28 same incident.
    HEADLESS_PROMPT_FILE="$WORKDIR/.claude/skills/deal-aggregator/headless-friday-prompt.md"
    POST_RUN_CHECK="${POST_RUN_CHECK:-python3 \"$WORKDIR/scripts/validate_deal_aggregator_integrity.py\" --mode digest --date \$TODAY}"
    ;;
esac

# Run Claude in non-interactive mode with retry on transient failures
MAX_ATTEMPTS=3
ATTEMPT=1
EXIT_CODE=1
VALIDATOR_FAILED=""
while [ $ATTEMPT -le $MAX_ATTEMPTS ]; do
  echo "--- attempt $ATTEMPT of $MAX_ATTEMPTS ---" >> "$LOG_FILE"
  if [ -n "$HEADLESS_PROMPT_FILE" ] && [ -f "$HEADLESS_PROMPT_FILE" ]; then
    echo "Using headless prompt: $HEADLESS_PROMPT_FILE" >> "$LOG_FILE"
    "$HOME/.local/bin/claude" \
      -p \
      --dangerously-skip-permissions \
      < "$HEADLESS_PROMPT_FILE" \
      >> "$LOG_FILE" 2>&1
  else
    if [ -n "$HEADLESS_PROMPT_FILE" ]; then
      echo "WARN: headless prompt expected but missing: $HEADLESS_PROMPT_FILE" >> "$LOG_FILE"
    fi
    INVOKE="/$SKILL_NAME"
    if [ -n "$SKILL_ARGS" ]; then INVOKE="$INVOKE $SKILL_ARGS"; fi
    echo "$INVOKE" | \
      "$HOME/.local/bin/claude" \
        -p \
        --dangerously-skip-permissions \
        >> "$LOG_FILE" 2>&1
  fi
  EXIT_CODE=$?
  if [ $EXIT_CODE -eq 0 ]; then break; fi
  # Only retry on transient CLI failures, not skill-level errors
  if ! tail -10 "$LOG_FILE" | grep -qE "Unexpected|unknown error|network|timeout|401|authentication_error|Invalid authentication"; then
    break
  fi
  ATTEMPT=$((ATTEMPT + 1))
  [ $ATTEMPT -le $MAX_ATTEMPTS ] && sleep 30
done
echo "Finished claude run: $(date), exit: $EXIT_CODE (attempts: $ATTEMPT)" >> "$LOG_FILE"

# Post-run validator. If the skill exited 0 AND the plist set
# POST_RUN_CHECK, execute it. If the validator fails, override
# EXIT_CODE so the Slack alert below fires. Catches the "skill exited 0
# but did no work" silent-success failure mode (2026-04-19 incident).
# $TODAY in POST_RUN_CHECK is substituted with today's YYYY-MM-DD.
if [ $EXIT_CODE -eq 0 ] && [ -n "$POST_RUN_CHECK" ]; then
  echo "--- post-run validator ---" >> "$LOG_FILE"
  CHECK_CMD="${POST_RUN_CHECK//\$TODAY/$(date +%Y-%m-%d)}"
  echo "Running: $CHECK_CMD" >> "$LOG_FILE"
  eval "$CHECK_CMD" >> "$LOG_FILE" 2>&1
  CHECK_CODE=$?
  echo "Validator exit: $CHECK_CODE" >> "$LOG_FILE"
  if [ $CHECK_CODE -ne 0 ]; then
    EXIT_CODE=$CHECK_CODE
    VALIDATOR_FAILED=1
    echo "VALIDATOR FAILED — overriding skill exit code" >> "$LOG_FILE"
  fi
fi

# Notify Slack on failure (skill failure OR validator failure)
if [ $EXIT_CODE -ne 0 ]; then
  if [ -n "$VALIDATOR_FAILED" ]; then
    SLACK_TEXT="Scheduled skill VALIDATOR FAILED: $SKILL_NAME (validator exit $EXIT_CODE). Skill ran clean but post-run integrity check rejected output. Check logs/scheduled/"
  else
    SLACK_TEXT="Scheduled skill FAILED: $SKILL_NAME (exit $EXIT_CODE). Check logs/scheduled/"
  fi
  curl -s -X POST "$SLACK_WEBHOOK_OPERATIONS" \
    -H 'Content-type: application/json' \
    -d "{\"text\":\"$SLACK_TEXT\"}"
fi

# v1.1 Failure-trigger: auto-fire launchd-debugger on any non-zero exit so the
# debug subagent diagnoses immediately instead of waiting for the 5am daily
# scan. Recursion guard: skip if THIS run is already launchd-debugger (any
# mode) — if launchd-debugger fails it must NOT trigger itself.
#
# Background-detached (nohup + &) so the parent skill exit isn't held up by
# the on-failure run (~3min). The wrapper exits immediately; the on-failure
# child wrapper has its own LOG_FILE/POST_RUN_CHECK lifecycle and writes its
# own log at logs/scheduled/launchd-debugger-{date}-{HHMM}.log.
#
# FAILED_LOG_FILE (not LOG_FILE) is exported so it survives the child
# wrapper's reassignment of LOG_FILE on its line ~22. The on-failure prompt
# reads $FAILED_LOG_FILE and feeds it to scan_launchd_failures.py --log-file.
if [ "$EXIT_CODE" != "0" ] && [ "$SKILL_NAME" != "launchd-debugger" ]; then
  WRAPPER_PATH="$WORKDIR/scripts/run-skill.sh"
  echo "Auto-firing launchd-debugger on-failure (LOG_FILE=$LOG_FILE)" >> "$LOG_FILE"
  FAILED_LOG_FILE="$LOG_FILE" nohup "$WRAPPER_PATH" launchd-debugger on-failure </dev/null >/dev/null 2>&1 &
fi

# v1.2 health-monitor RED bridge: when health-monitor exits clean AND its
# artifact landed at the expected path, fan out one launchd-debugger:on-failure
# spawn per RED row in the markdown artifact. Yellow stays informational.
# Skipped on validator failure (the v1.1 on-failure auto-fire above already
# fires for that case). Background-detached so the wrapper exits immediately.
# Recursion-guarded inside the bridge script too (FROM_HEALTH_BRIDGE env +
# arg-form check on $1).
if [ "$EXIT_CODE" = "0" ] \
   && [ -z "$VALIDATOR_FAILED" ] \
   && [ "$SKILL_NAME" = "health-monitor" ]; then
  HEALTH_ARTIFACT="$WORKDIR/brain/trackers/health/$(date +%Y-%m-%d)-health.md"
  if [ -f "$HEALTH_ARTIFACT" ]; then
    echo "Firing health-monitor RED bridge against $HEALTH_ARTIFACT" >> "$LOG_FILE"
    nohup bash "$WORKDIR/scripts/health-monitor-red-bridge.sh" "$HEALTH_ARTIFACT" </dev/null >/dev/null 2>&1 &
  else
    echo "health-monitor RED bridge skipped — artifact not found at $HEALTH_ARTIFACT" >> "$LOG_FILE"
  fi
fi
