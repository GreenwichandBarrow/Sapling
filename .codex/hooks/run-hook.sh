#!/usr/bin/env bash
set -euo pipefail

event="${1:?hook event required}"
project_dir="$(git rev-parse --show-toplevel)"

export CODEX_PROJECT_DIR="$project_dir"
# Compatibility alias for migrated hook scripts that still read the old name
# during the one-week monitoring window.
export CLAUDE_PROJECT_DIR="$project_dir"

case "$event" in
  session_start) script="$project_dir/.codex/hooks/router/session_start.py" ;;
  pre_tool_use) script="$project_dir/.codex/hooks/router/pre_tool_use.py" ;;
  post_tool_use) script="$project_dir/.codex/hooks/router/post_tool_use.py" ;;
  stop) script="$project_dir/.codex/hooks/router/stop.py" ;;
  pre_compact) script="$project_dir/.codex/hooks/router/pre_compact.py" ;;
  user_prompt_submit) script="$project_dir/.codex/hooks/router/user_prompt_submit.py" ;;
  *) echo "Unknown hook event: $event" >&2; exit 2 ;;
esac

exec python3 "$script"
