#!/bin/bash
# Phase 3.5 foundation check — verifies Hetzner server is ready for Phase 4 rebuild.
#
# Run via vps shell on the server.
# Idempotent and safe to re-run. Read-only except for one optional gog install attempt.
# Output goes to logs/scheduled/phase-3.5-foundation-check-{date}.log so Claude can read findings.
#
# Usage:
#   cd ~/projects/Sapling && git pull && bash scripts/phase-3.5-foundation-check.sh

set -uo pipefail

TODAY=$(date +%Y-%m-%d)
NOW=$(date '+%Y-%m-%d %H:%M:%S %Z')
REPO_ROOT="${HOME}/projects/Sapling"
LOG_DIR="${REPO_ROOT}/logs/scheduled"
LOG_FILE="${LOG_DIR}/phase-3.5-foundation-check-${TODAY}.log"

mkdir -p "$LOG_DIR"
# Tee everything (stdout + stderr) into log file AND console.
exec > >(tee -a "$LOG_FILE") 2>&1

echo "=== Phase 3.5 Foundation Check ==="
echo "Started: ${NOW}"
echo "Host:    $(hostname)"
echo "User:    $(whoami)"
echo "Repo:    ${REPO_ROOT}"
echo

# Track green/red counts for summary
GREEN=0
RED=0

mark_green() { GREEN=$((GREEN+1)); echo "  ✓ $1"; }
mark_red()   { RED=$((RED+1));   echo "  ✗ $1"; }

# ============================================================
# Check 1 — gog CLI installed + credentials present + auth works
# ============================================================
echo "## Check 1: gog CLI"

if command -v gog >/dev/null 2>&1; then
  GOG_PATH=$(command -v gog)
  GOG_VER=$(gog --version 2>&1 | head -1)
  mark_green "gog installed at ${GOG_PATH} (${GOG_VER})"
else
  mark_red "gog NOT installed"
  if [ -x /home/linuxbrew/.linuxbrew/bin/brew ]; then
    echo "    Attempting linuxbrew install..."
    /home/linuxbrew/.linuxbrew/bin/brew install gogcli 2>&1 | tail -8
    if command -v gog >/dev/null 2>&1 || [ -x /home/linuxbrew/.linuxbrew/bin/gog ]; then
      mark_green "gog installed via linuxbrew (re-source ~/.bashrc or restart shell to use)"
    else
      mark_red "linuxbrew install attempt failed — install manually"
    fi
  else
    mark_red "linuxbrew not found — build from source (https://github.com/steipete/gogcli) or apt-install golang-go and 'go build ./cmd/gog'"
  fi
fi

# Credential check — directory existence only, never read contents.
# v0.15+ uses ~/.config/gogcli/ (not ~/.config/gog/).
if [ -d "${HOME}/.config/gogcli" ]; then
  CRED_FILE_COUNT=$(ls -1 "${HOME}/.config/gogcli" 2>/dev/null | wc -l | tr -d ' ')
  mark_green "gog config dir exists (${CRED_FILE_COUNT} files)"
else
  mark_red "gog config dir MISSING at ~/.config/gogcli"
  echo "    ACTION on iMac: scp -r ~/.config/gogcli ubuntu@agent-vps-7731c88b:~/.config/"
fi

# Test gog auth without burning API quota — list configured accounts (v0.15+ syntax: 'gog auth list', not 'gog accounts list').
if command -v gog >/dev/null 2>&1; then
  echo "    gog auth list:"
  gog auth list 2>&1 | head -5 | sed 's/^/      /'
fi

echo

# ============================================================
# Check 2 — Granola MCP reachable from Linux
# ============================================================
echo "## Check 2: Granola MCP reachability"

MCP_URL="https://mcp.granola.ai/mcp"
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" -m 8 "$MCP_URL" 2>&1 || echo "000")
echo "  curl ${MCP_URL} → HTTP ${HTTP_CODE}"

case "$HTTP_CODE" in
  2*|3*|4*) mark_green "MCP server reachable (HTTP ${HTTP_CODE} — auth-handshake-level response, full MCP client test happens in Phase 4)" ;;
  5*)       mark_red "MCP server returned 5xx — vendor-side issue, retry later" ;;
  000)      mark_red "MCP server unreachable — check DNS or network" ;;
  *)        mark_red "MCP server returned unexpected code ${HTTP_CODE}" ;;
esac

echo

# ============================================================
# Check 3 — Vault git-sync server-side
# ============================================================
echo "## Check 3: Vault git-sync"

if [ -d "${REPO_ROOT}/.git" ]; then
  cd "${REPO_ROOT}"
  CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD 2>&1)
  LAST_COMMIT=$(git log -1 --format='%h %s (%ar)' 2>&1)
  mark_green "repo at ${REPO_ROOT} (branch: ${CURRENT_BRANCH})"
  echo "    Last commit: ${LAST_COMMIT}"

  # Dry-run pull to see if we're behind origin without actually pulling
  echo "    git fetch + status vs origin:"
  git fetch --quiet 2>&1 || echo "      fetch failed"
  AHEAD=$(git rev-list --count HEAD..@{u} 2>/dev/null || echo "?")
  BEHIND=$(git rev-list --count @{u}..HEAD 2>/dev/null || echo "?")
  echo "      remote-ahead: ${AHEAD}, local-ahead: ${BEHIND}"

  # brain/ writeable?
  if [ -w "${REPO_ROOT}/brain" ]; then
    mark_green "brain/ directory writeable"
  else
    mark_red "brain/ NOT writeable"
  fi

  # Working tree clean check (don't surface filenames if dirty — could leak)
  DIRTY_COUNT=$(git status --porcelain 2>/dev/null | wc -l | tr -d ' ')
  if [ "$DIRTY_COUNT" -eq 0 ]; then
    mark_green "working tree clean"
  else
    echo "  ⚠ working tree has ${DIRTY_COUNT} uncommitted changes (server should be clean — investigate)"
    RED=$((RED+1))
  fi
else
  mark_red "no git repo at ${REPO_ROOT}"
fi

echo

# ============================================================
# Check 4 — Slack webhook env var loads (don't echo value)
# ============================================================
echo "## Check 4: Slack webhook env var"

ENV_FILE="${REPO_ROOT}/scripts/.env.launchd"
if [ -f "$ENV_FILE" ]; then
  # grep -c is value-suppressing per CLAUDE.md secrets rule
  COUNT=$(grep -c '^export SLACK_WEBHOOK_OPERATIONS=' "$ENV_FILE" 2>/dev/null || echo 0)
  if [ "$COUNT" -gt 0 ]; then
    mark_green "SLACK_WEBHOOK_OPERATIONS line present in .env.launchd (count: ${COUNT})"
    # Test it actually loads into a shell — without echoing value
    if ( set +u; source "$ENV_FILE" >/dev/null 2>&1; [ -n "${SLACK_WEBHOOK_OPERATIONS:-}" ] ); then
      mark_green "SLACK_WEBHOOK_OPERATIONS loads into shell"
    else
      mark_red "SLACK_WEBHOOK_OPERATIONS line present but fails to load (syntax issue?)"
    fi
  else
    mark_red "SLACK_WEBHOOK_OPERATIONS not found in .env.launchd"
  fi
else
  mark_red ".env.launchd missing at ${ENV_FILE} — re-run 5/7 scp transfer"
fi

echo

# ============================================================
# Check 5 — Python runtime + deps for poller
# ============================================================
echo "## Check 5: Python runtime"

if command -v python3 >/dev/null 2>&1; then
  PY_VER=$(python3 --version 2>&1)
  mark_green "python3 ${PY_VER}"
  for mod in requests yaml json; do
    if python3 -c "import ${mod}" >/dev/null 2>&1; then
      mark_green "python module: ${mod}"
    else
      mark_red "python module: ${mod} MISSING (pip3 install ${mod})"
    fi
  done
else
  mark_red "python3 not installed"
fi

echo

# ============================================================
# Summary
# ============================================================
echo "## Summary"
echo "Finished: $(date '+%Y-%m-%d %H:%M:%S %Z')"
echo "Green: ${GREEN}"
echo "Red:   ${RED}"
echo "Log:   ${LOG_FILE}"

if [ "$RED" -gt 0 ]; then
  echo
  echo "ACTION REQUIRED — see RED rows above. Resolve, then re-run."
  exit 1
else
  echo
  echo "All foundations green. Ready for Phase 4 rebuild."
  exit 0
fi
