#!/bin/bash
# Wrapper for refresh_attio_snapshot.py — invoked by launchd hourly during
# business hours. Sources the env file (ATTIO_API_KEY) and runs via the
# dashboard venv's Python so `requests` is available.

# NOTE: intentionally NOT using `set -e` because we want to capture the
# refresh-script exit code, run the post-run validator, and propagate the
# worse of the two. The plist wrapper convention is "silent-success failure
# is the bug we are guarding against," so the validator must always run.

set -uo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
LOG_DIR="$REPO_ROOT/logs/scheduled"
mkdir -p "$LOG_DIR"

STAMP=$(date +%Y-%m-%d-%H%M)
LOG_FILE="$LOG_DIR/attio-snapshot-refresh-$STAMP.log"

REFRESH_EXIT=0
VALIDATOR_EXIT=0

{
  echo "=== refresh-attio-snapshot.sh @ $(date -u +%Y-%m-%dT%H:%M:%SZ) ==="
  set -a
  # shellcheck disable=SC1091
  source "$REPO_ROOT/scripts/load-env.sh"
  load_env "$REPO_ROOT/scripts/.env.launchd"
  set +a
  "$REPO_ROOT/dashboard/.venv/bin/python" "$REPO_ROOT/scripts/refresh_attio_snapshot.py"
  REFRESH_EXIT=$?
  echo "--- refresh exit: $REFRESH_EXIT ---"

  echo "=== POST_RUN_CHECK: validate_attio_snapshot_integrity.py ==="
  "$REPO_ROOT/dashboard/.venv/bin/python" "$REPO_ROOT/scripts/validate_attio_snapshot_integrity.py"
  VALIDATOR_EXIT=$?
  echo "--- validator exit: $VALIDATOR_EXIT ---"
} >> "$LOG_FILE" 2>&1

# Prune logs older than 14 days (matches the convention in run-skill.sh).
find "$LOG_DIR" -name "attio-snapshot-refresh-*.log" -mtime +14 -delete 2>/dev/null || true

# Propagate the worse of refresh / validator exit codes so launchd-debugger
# catches both refresh-side and integrity-side failures.
if [ "$VALIDATOR_EXIT" -ne 0 ]; then
  exit "$VALIDATOR_EXIT"
fi
exit "$REFRESH_EXIT"
