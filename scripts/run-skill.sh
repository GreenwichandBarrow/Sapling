#!/bin/bash
# Shared wrapper for all scheduled Claude skill runs
# Usage: run-skill.sh <skill-name>

SKILL_NAME="$1"
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

# Run Claude in non-interactive mode with retry on transient failures
MAX_ATTEMPTS=3
ATTEMPT=1
EXIT_CODE=1
while [ $ATTEMPT -le $MAX_ATTEMPTS ]; do
  echo "--- attempt $ATTEMPT of $MAX_ATTEMPTS ---" >> "$LOG_FILE"
  echo "/$SKILL_NAME" | \
    "$HOME/.local/bin/claude" \
      -p \
      --dangerously-skip-permissions \
      >> "$LOG_FILE" 2>&1
  EXIT_CODE=$?
  if [ $EXIT_CODE -eq 0 ]; then break; fi
  # Only retry on transient CLI failures, not skill-level errors
  if ! tail -5 "$LOG_FILE" | grep -q "Unexpected\|unknown error\|network\|timeout"; then
    break
  fi
  ATTEMPT=$((ATTEMPT + 1))
  [ $ATTEMPT -le $MAX_ATTEMPTS ] && sleep 30
done
echo "Finished: $(date), exit: $EXIT_CODE (attempts: $ATTEMPT)" >> "$LOG_FILE"

# Notify Slack on failure
if [ $EXIT_CODE -ne 0 ]; then
  curl -s -X POST "$SLACK_WEBHOOK_OPERATIONS" \
    -H 'Content-type: application/json' \
    -d "{\"text\":\"Scheduled skill FAILED: $SKILL_NAME (exit $EXIT_CODE). Check logs/scheduled/\"}"
fi
