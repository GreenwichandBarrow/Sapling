#!/bin/bash
# Wrapper for snapshot_weekly_to_vault.py — invoked by launchd Friday 22:00 ET.
# Phase C of the dashboard-as-source pivot. No secrets needed (reads vault
# files locally). Uses dashboard venv for yaml dependency.

set -euo pipefail

REPO_ROOT="/Users/kaycschneider/Documents/AI Operations"
LOG_DIR="$REPO_ROOT/logs/scheduled"
mkdir -p "$LOG_DIR"

STAMP=$(date +%Y-%m-%d-%H%M)
LOG_FILE="$LOG_DIR/weekly-snapshot-$STAMP.log"

{
  echo "=== snapshot-weekly-to-vault.sh @ $(date -u +%Y-%m-%dT%H:%M:%SZ) ==="
  "$REPO_ROOT/dashboard/.venv/bin/python" "$REPO_ROOT/scripts/snapshot_weekly_to_vault.py"
} >> "$LOG_FILE" 2>&1

# Prune logs older than 14 days (matches refresh-attio-snapshot pattern).
find "$LOG_DIR" -name "weekly-snapshot-*.log" -mtime +14 -delete 2>/dev/null || true
