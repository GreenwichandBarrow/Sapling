#!/bin/bash
# Wrapper for refresh_attio_snapshot.py — invoked by launchd hourly during
# business hours. Sources the env file (ATTIO_API_KEY) and runs via the
# dashboard venv's Python so `requests` is available.

set -euo pipefail

REPO_ROOT="/Users/kaycschneider/Documents/AI Operations"
LOG_DIR="$REPO_ROOT/logs/scheduled"
mkdir -p "$LOG_DIR"

STAMP=$(date +%Y-%m-%d-%H%M)
LOG_FILE="$LOG_DIR/attio-snapshot-refresh-$STAMP.log"

{
  echo "=== refresh-attio-snapshot.sh @ $(date -u +%Y-%m-%dT%H:%M:%SZ) ==="
  set -a
  # shellcheck disable=SC1091
  source "$REPO_ROOT/scripts/.env.launchd"
  set +a
  "$REPO_ROOT/dashboard/.venv/bin/python" "$REPO_ROOT/scripts/refresh_attio_snapshot.py"
} >> "$LOG_FILE" 2>&1

# Prune logs older than 14 days (matches the convention in run-skill.sh).
find "$LOG_DIR" -name "attio-snapshot-refresh-*.log" -mtime +14 -delete 2>/dev/null || true
