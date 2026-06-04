#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

status=0

pass() { printf "PASS  %s\n" "$*"; }
warn() { printf "WARN  %s\n" "$*"; }
fail() { printf "FAIL  %s\n" "$*"; status=1; }

check_file() {
  local path="$1"
  if [ -e "$path" ]; then
    pass "$path exists"
  else
    fail "$path is missing"
  fi
}

printf "Codex migration readiness\n"
printf "Project: %s\n\n" "$ROOT"

check_file "AGENTS.md"
check_file ".agents/skills"
check_file ".codex/hooks.json"
check_file ".codex/hooks/run-hook.sh"
check_file "scripts/run-agent-skill.sh"
check_file "scripts/.env.codex"

if bash -n scripts/run-agent-skill.sh; then
  pass "scripts/run-agent-skill.sh syntax"
else
  fail "scripts/run-agent-skill.sh syntax"
fi

if [ -e scripts/post_call_analyzer_poll.codex.sh ]; then
  if bash -n scripts/post_call_analyzer_poll.codex.sh; then
    pass "scripts/post_call_analyzer_poll.codex.sh syntax"
  else
    fail "scripts/post_call_analyzer_poll.codex.sh syntax"
  fi
else
  warn "scripts/post_call_analyzer_poll.codex.sh not present; post-call analyzer cutover is not prepared"
fi

if python3 -m json.tool .codex/hooks.json >/dev/null 2>&1; then
  pass ".codex/hooks.json parses"
else
  fail ".codex/hooks.json parses"
fi

if command -v codex >/dev/null 2>&1; then
  pass "codex CLI installed: $(command -v codex)"
  if codex exec --help 2>/dev/null | grep -q -- "--dangerously-bypass-approvals-and-sandbox"; then
    pass "codex exec supports Phase 1 broad-permission flag"
  else
    fail "codex exec broad-permission flag not found"
  fi
else
  fail "codex CLI is not installed or not on PATH"
fi

if command -v op >/dev/null 2>&1; then
  pass "1Password CLI installed: $(command -v op)"
else
  fail "1Password CLI is not installed or not on PATH"
fi

if [ -f "$HOME/.config/op-sa-token.env" ]; then
  pass "1Password service-account token file exists"
else
  fail "$HOME/.config/op-sa-token.env is missing"
fi

# Resolve only existence/non-placeholder status. Never print the secret value.
set +u
source "$HOME/.config/op-sa-token.env" >/dev/null 2>&1 || true
source "$ROOT/scripts/load-env.sh" >/dev/null 2>&1 || true
set -a
load_env "$ROOT/scripts/.env.codex" >/dev/null 2>&1 || true
set +a
set -u
if [ -n "${CODEX_API_KEY:-}" ] && [[ "${CODEX_API_KEY:-}" != op://* ]]; then
  pass "CODEX_API_KEY resolves through 1Password"
else
  fail "CODEX_API_KEY is missing or unresolved through 1Password"
fi

if [ -e "${CODEX_SCHEDULED_KILL_SWITCH:-$HOME/.config/sapling/disable-codex-scheduled}" ]; then
  warn "Codex scheduled kill switch is currently enabled"
else
  pass "Codex scheduled kill switch is not enabled"
fi

email_payload='{"tool_name":"Bash","tool_input":{"command":"gog gmail send --to test@example.com"}}'
if printf "%s" "$email_payload" | .codex/hooks/run-hook.sh pre_tool_use 2>/dev/null | grep -q '"permissionDecision": "deny"'; then
  pass "email-send hook denies synthetic send command"
else
  fail "email-send hook did not deny synthetic send command"
fi

secret_payload='{"tool_name":"Bash","tool_input":{"command":"cat scripts/.env.launchd"}}'
if printf "%s" "$secret_payload" | .codex/hooks/run-hook.sh pre_tool_use 2>/dev/null | grep -q '"permissionDecision": "deny"'; then
  pass "secret-file hook denies synthetic secret read"
else
  fail "secret-file hook did not deny synthetic secret read"
fi

printf "\n"
if [ "$status" -eq 0 ]; then
  printf "READY: non-live Codex migration checks passed.\n"
else
  printf "NOT READY: fix FAIL items before Codex scheduled validation/cutover.\n"
fi

exit "$status"
