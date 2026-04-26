#!/bin/bash
# Wrapper for refresh_apollo_credits.py — invoked by launchd hourly during
# business hours. Sources the env file (APOLLO_API_KEY) and runs via the
# dashboard venv's Python so `requests` is available.

set -euo pipefail

REPO_ROOT="/Users/kaycschneider/Documents/AI Operations"
LOG_DIR="$REPO_ROOT/logs/scheduled"
mkdir -p "$LOG_DIR"

STAMP=$(date +%Y-%m-%d-%H%M)
LOG_FILE="$LOG_DIR/apollo-credits-$STAMP.log"

{
  echo "=== refresh-apollo-credits.sh @ $(date -u +%Y-%m-%dT%H:%M:%SZ) ==="
  set -a
  # shellcheck disable=SC1091
  source "$REPO_ROOT/scripts/.env.launchd"
  set +a
  "$REPO_ROOT/dashboard/.venv/bin/python" "$REPO_ROOT/scripts/refresh_apollo_credits.py"
} >> "$LOG_FILE" 2>&1

# Prune logs older than 14 days (matches the convention in run-skill.sh).
find "$LOG_DIR" -name "apollo-credits-*.log" -mtime +14 -delete 2>/dev/null || true
