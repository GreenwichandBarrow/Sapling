#!/bin/bash
# Wrapper for export_weekly_archive_to_sheet.py — invoked by launchd Saturday
# 09:00 ET. Runs the morning after the Friday vault snapshot fires, so the
# archive Sheet always reflects the just-written vault file.
# Phase D of the dashboard-as-source pivot.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="${EXPORT_WEEKLY_ARCHIVE_REPO_ROOT:-$(cd "$SCRIPT_DIR/.." && pwd)}"
LOG_DIR="$REPO_ROOT/logs/scheduled"
mkdir -p "$LOG_DIR"

STAMP=$(date +%Y-%m-%d-%H%M)
LOG_FILE="$LOG_DIR/weekly-archive-export-$STAMP.log"

{
  echo "=== export-weekly-archive-to-sheet.sh @ $(date -u +%Y-%m-%dT%H:%M:%SZ) ==="
  # Ensure gog is on PATH for stripped scheduler environments.
  export PATH="/opt/homebrew/bin:/usr/local/bin:$HOME/.local/bin:$PATH"
  "$REPO_ROOT/dashboard/.venv/bin/python" \
    "$REPO_ROOT/scripts/export_weekly_archive_to_sheet.py" --commit
} >> "$LOG_FILE" 2>&1

# Prune logs older than 14 days.
find "$LOG_DIR" -name "weekly-archive-export-*.log" -mtime +14 -delete 2>/dev/null || true
