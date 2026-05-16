#!/bin/bash
# Wrapper for refresh_jj_snapshot.py — invoked by launchd 3x/day Mon-Fri
# (9am, 2:30pm, 6pm ET) so the dashboard's JJ activity stays current
# around JJ's 10am-2pm ET shift.

# NOTE: intentionally NOT using `set -e` because we want to capture the
# refresh-script exit code, run the post-run validator, and propagate the
# worse of the two.

set -uo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
LOG_DIR="$REPO_ROOT/logs/scheduled"
mkdir -p "$LOG_DIR"

STAMP=$(date +%Y-%m-%d-%H%M)
LOG_FILE="$LOG_DIR/jj-snapshot-refresh-$STAMP.log"

REFRESH_EXIT=0
VALIDATOR_EXIT=0

{
  echo "=== refresh-jj-snapshot.sh @ $(date -u +%Y-%m-%dT%H:%M:%SZ) ==="
  set -a
  # Resolve op:// secret references (GOG_KEYRING_PASSWORD etc.) via op inject,
  # same as run-skill.sh. The systemd unit supplies OP_SERVICE_ACCOUNT_TOKEN
  # via EnvironmentFile; sourcing the raw file would leave op:// unresolved.
  # shellcheck source=scripts/load-env.sh
  source "$REPO_ROOT/scripts/load-env.sh"
  load_env "$REPO_ROOT/scripts/.env.launchd"
  set +a
  # gog reads OAuth from the user's keychain; PATH must include the install dir.
  export PATH="$HOME/.local/bin:/usr/local/bin:/opt/homebrew/bin:/home/linuxbrew/.linuxbrew/bin:/usr/bin:/bin"
  "$REPO_ROOT/dashboard/.venv/bin/python3" "$REPO_ROOT/scripts/refresh_jj_snapshot.py"
  REFRESH_EXIT=$?
  echo "--- refresh exit: $REFRESH_EXIT ---"

  echo "=== POST_RUN_CHECK: validate_jj_snapshot_integrity.py ==="
  "$REPO_ROOT/dashboard/.venv/bin/python3" "$REPO_ROOT/scripts/validate_jj_snapshot_integrity.py"
  VALIDATOR_EXIT=$?
  echo "--- validator exit: $VALIDATOR_EXIT ---"
} >> "$LOG_FILE" 2>&1

# 14-day rotation (matches run-skill.sh convention).
find "$LOG_DIR" -name "jj-snapshot-refresh-*.log" -mtime +14 -delete 2>/dev/null || true

# Propagate the worse of refresh / validator exit codes so launchd-debugger
# catches both refresh-side and integrity-side failures.
if [ "$VALIDATOR_EXIT" -ne 0 ]; then
  exit "$VALIDATOR_EXIT"
fi
exit "$REFRESH_EXIT"
