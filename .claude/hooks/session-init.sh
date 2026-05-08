#!/bin/bash
# Session initialization hook for Obsidian PKM vault
# Sets up environment variables and ensures daily note exists

# Set vault path (prefer CLAUDE_PROJECT_DIR, fall back to cwd)
VAULT_PATH="${VAULT_PATH:-${CLAUDE_PROJECT_DIR:-$(pwd)}}"

# Date variables for daily operations
TODAY=$(date +%Y-%m-%d)
YESTERDAY=$(date -v-1d +%Y-%m-%d 2>/dev/null || date -d "yesterday" +%Y-%m-%d)
CURRENT_WEEK=$(date +%Y-W%V)

# Device-location detection (Phase 3 server migration). Skills can branch on
# this to behave context-appropriately:
#   imac    — Kay's primary dev Mac (Granola sidecar lives here)
#   macbook — Kay's secondary Mac
#   server  — Hetzner VPS (Linux, runs scheduled jobs as systemd timers)
#   mac     — fallback for unrecognized macOS hosts
#   linux   — fallback for unrecognized Linux hosts
DEVICE_HOSTNAME=$(hostname -s 2>/dev/null || echo "unknown")
case "$(uname)" in
  Darwin)
    case "$DEVICE_HOSTNAME" in
      *[Ii][Mm]ac*) DEVICE_LOCATION="imac" ;;
      *[Mm][Aa][Cc][Bb]ook*) DEVICE_LOCATION="macbook" ;;
      *) DEVICE_LOCATION="mac" ;;
    esac
    ;;
  Linux)
    case "$DEVICE_HOSTNAME" in
      *agent-vps*|*dodo-vps*|*greenwich*|*sapling*|*-vps-*) DEVICE_LOCATION="server" ;;
      *) DEVICE_LOCATION="linux" ;;
    esac
    ;;
  *)
    DEVICE_LOCATION="unknown"
    ;;
esac

# Daily note path
DAILY_NOTE="$VAULT_PATH/brain/notes/daily/$TODAY.md"

# Persist environment variables for all subsequent Bash commands
if [ -n "$CLAUDE_ENV_FILE" ]; then
  cat >> "$CLAUDE_ENV_FILE" << EOF
export VAULT_PATH="$VAULT_PATH"
export TODAY="$TODAY"
export YESTERDAY="$YESTERDAY"
export CURRENT_WEEK="$CURRENT_WEEK"
export DAILY_NOTE="$DAILY_NOTE"
export DEVICE_LOCATION="$DEVICE_LOCATION"
export DEVICE_HOSTNAME="$DEVICE_HOSTNAME"
EOF
fi

# Verify vault structure (check for CLAUDE.md at root)
if [ ! -f "$VAULT_PATH/CLAUDE.md" ]; then
    echo "Note: Not in a SaplingOS directory (no CLAUDE.md found)"
fi

# Output session info
echo ""
echo "Launching your Personal OS"
echo "  Today: $TODAY"
echo "  Device: $DEVICE_LOCATION ($DEVICE_HOSTNAME)"

# Ensure daily note exists (creates from schema if missing)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
python3 "$SCRIPT_DIR/daily-init.py"
