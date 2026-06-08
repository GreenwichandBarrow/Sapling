#!/usr/bin/env bash
# Compatibility shim for older references. The active server-side detector is
# post_call_analyzer_poll.codex.sh, which uses the 1Password-backed Granola REST
# wrapper and launches run-agent-skill.sh.

set -euo pipefail

REPO_ROOT="${CODEX_PROJECT_DIR:-/home/ubuntu/projects/Sapling}"
exec /bin/bash "$REPO_ROOT/scripts/post_call_analyzer_poll.codex.sh"
