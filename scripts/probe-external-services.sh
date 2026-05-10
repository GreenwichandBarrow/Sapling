#!/bin/bash
# Wrapper for probe_external_services.py — invoked by launchd every 30 min
# during business hours. Sources scripts/.env.launchd so the probe can read
# APOLLO_API_KEY / SLACK_WEBHOOK_* / etc., then runs via the dashboard venv's
# Python so `requests` and any other deps are available.
#
# Mirrors scripts/refresh-attio-snapshot.sh structure.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
LOG_DIR="$REPO_ROOT/logs/scheduled"
mkdir -p "$LOG_DIR"

STAMP=$(date +%Y-%m-%d-%H%M)
LOG_FILE="$LOG_DIR/external-services-$STAMP.log"

{
  echo "=== probe-external-services.sh @ $(date -u +%Y-%m-%dT%H:%M:%SZ) ==="
  set -a
  # shellcheck disable=SC1091
  source "$REPO_ROOT/scripts/load-env.sh"
  load_env "$REPO_ROOT/scripts/.env.launchd"
  set +a
  "$REPO_ROOT/dashboard/.venv/bin/python" "$REPO_ROOT/scripts/probe_external_services.py"
} >> "$LOG_FILE" 2>&1

# Prune logs older than 14 days (matches refresh-attio-snapshot + run-skill convention).
find "$LOG_DIR" -name "external-services-*.log" -mtime +14 -delete 2>/dev/null || true
