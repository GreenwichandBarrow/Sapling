#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
LOG_DIR="$REPO_ROOT/logs/scheduled"
STAMP="$(date +%Y-%m-%d-%H%M)"
LOG_FILE="$LOG_DIR/claude-usage-$STAMP.log"
mkdir -p "$LOG_DIR"

{
  echo "=== refresh-claude-usage.sh @ $(date -u +%Y-%m-%dT%H:%M:%SZ) ==="
  python3 "$REPO_ROOT/scripts/refresh_claude_usage.py"
} >>"$LOG_FILE" 2>&1

find "$LOG_DIR" -name "claude-usage-*.log" -mtime +14 -delete 2>/dev/null || true
