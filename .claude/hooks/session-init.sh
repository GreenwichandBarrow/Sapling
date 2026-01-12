#!/bin/bash
# Session initialization hook for Obsidian PKM vault
# Sets up environment variables and ensures daily note exists

# Set vault path (defaults to current directory)
VAULT_PATH="${VAULT_PATH:-$(pwd)}"

# Date variables for daily operations
TODAY=$(date +%Y-%m-%d)
YESTERDAY=$(date -v-1d +%Y-%m-%d 2>/dev/null || date -d "yesterday" +%Y-%m-%d)
CURRENT_WEEK=$(date +%Y-W%V)

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

# Ensure daily note exists (creates from schema if missing)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
python3 "$SCRIPT_DIR/daily-init.py"
