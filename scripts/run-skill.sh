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
WORKDIR="$HOME/Documents/AI Operations"
LOG_DIR="$WORKDIR/logs/scheduled"
LOG_FILE="$LOG_DIR/${SKILL_NAME}-$(date +%Y-%m-%d-%H%M).log"

# Source env (launchd doesn't read .zshrc)
source "$WORKDIR/scripts/.env.launchd"

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
if [ -n "$KEYCHAIN_PASSWORD" ]; then
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
  "deal-aggregator:")
    # Bare `run-skill.sh deal-aggregator` (Mon-Fri 6am morning fire — empty
    # args). Route to the morning headless prompt to forbid operator-question
    # framings and enforce idempotency-gate against double-write. Fix added
    # 2026-04-28 after morning run produced `RECOMMEND: ... → YES/NO/DISCUSS`
    # meta-output instead of executing.
    HEADLESS_PROMPT_FILE="$WORKDIR/.claude/skills/deal-aggregator/headless-morning-prompt.md"
    ;;
  "deal-aggregator:--afternoon")
    # Mon-Fri 2pm afternoon top-up. Lighter scan (Channel 2 + time-sensitive
    # platforms only). Writes separate artifact at
    # brain/context/deal-aggregator-scan-{TODAY}-afternoon.md — never
    # overwrites morning. Hardened 2026-04-28 same incident as morning.
    HEADLESS_PROMPT_FILE="$WORKDIR/.claude/skills/deal-aggregator/headless-afternoon-prompt.md"
    ;;
  "deal-aggregator:--digest-mode")
    # Friday 6am weekly source-productivity digest (Phase 2). Reads 7 days of
    # daily scorecards + 30 days of fingerprints + 7 days of email-scan-results
    # + Sourcing Sheet. Writes brain/trackers/weekly/{TODAY}-deal-aggregator-
    # digest.md. Slack only on ≥1 proposed change OR volume=🔴. Never
    # auto-writes to Sourcing Sheet. Hardened 2026-04-28 same incident.
    HEADLESS_PROMPT_FILE="$WORKDIR/.claude/skills/deal-aggregator/headless-friday-prompt.md"
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
