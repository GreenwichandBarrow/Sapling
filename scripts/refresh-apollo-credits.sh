#!/bin/bash
# Wrapper for refresh_apollo_credits.py — invoked by launchd hourly during
# business hours. Sources the env file (APOLLO_API_KEY) and runs via the
# dashboard venv's Python so `requests` is available.

# NOTE: intentionally NOT using `set -e` because we want to capture the
# refresh-script exit code, run the post-run validator, and propagate the
# worse of the two.

set -uo pipefail

REPO_ROOT="/Users/kaycschneider/Documents/AI Operations"
LOG_DIR="$REPO_ROOT/logs/scheduled"
mkdir -p "$LOG_DIR"

STAMP=$(date +%Y-%m-%d-%H%M)
LOG_FILE="$LOG_DIR/apollo-credits-$STAMP.log"

REFRESH_EXIT=0
VALIDATOR_EXIT=0

{
  echo "=== refresh-apollo-credits.sh @ $(date -u +%Y-%m-%dT%H:%M:%SZ) ==="
  set -a
  # shellcheck disable=SC1091
  source "$REPO_ROOT/scripts/.env.launchd"
  set +a
  "$REPO_ROOT/dashboard/.venv/bin/python" "$REPO_ROOT/scripts/refresh_apollo_credits.py"
  REFRESH_EXIT=$?
  echo "--- refresh exit: $REFRESH_EXIT ---"

  echo "=== POST_RUN_CHECK: validate_apollo_credits_integrity.py ==="
  "$REPO_ROOT/dashboard/.venv/bin/python" "$REPO_ROOT/scripts/validate_apollo_credits_integrity.py"
  VALIDATOR_EXIT=$?
  echo "--- validator exit: $VALIDATOR_EXIT ---"
} >> "$LOG_FILE" 2>&1

# Prune logs older than 14 days (matches the convention in run-skill.sh).
find "$LOG_DIR" -name "apollo-credits-*.log" -mtime +14 -delete 2>/dev/null || true

# Propagate the worse of refresh / validator exit codes so launchd-debugger
# catches both refresh-side and integrity-side failures.
if [ "$VALIDATOR_EXIT" -ne 0 ]; then
  exit "$VALIDATOR_EXIT"
fi
exit "$REFRESH_EXIT"
