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

scheduled_coverage=(
  "target-discovery:phase2-sunday|.agents/skills/target-discovery/headless-phase2-prompt.md|scripts/validate_phase2_integrity.py"
  "weekly-tracker:friday|.agents/skills/weekly-tracker/headless-friday-prompt.md|scripts/validate_weekly_tracker_integrity.py"
  "nightly-tracker-audit:nightly|.agents/skills/nightly-tracker-audit/headless-nightly-prompt.md|scripts/validate_nightly_tracker_audit_integrity.py"
  "relationship-manager:daily|.agents/skills/relationship-manager/headless-daily-prompt.md|scripts/validate_relationship_manager_integrity.py"
  "jj-operations:sunday-prep|.agents/skills/jj-operations/headless-sunday-prep-prompt.md|scripts/validate_jj_operations_integrity.py"
  "launchd-debugger:daily|.agents/skills/launchd-debugger/headless-daily-prompt.md|scripts/validate_launchd_debugger_integrity.py"
  "niche-intelligence:tuesday|.agents/skills/niche-intelligence/headless-tuesday-prompt.md|scripts/validate_niche_intelligence_integrity.py"
  "email-intelligence:|.agents/skills/email-intelligence/headless-weekday-prompt.md|scripts/validate_email_intelligence_integrity.py"
  "deal-aggregator:|.agents/skills/deal-aggregator/headless-morning-prompt.md|scripts/validate_deal_aggregator_integrity.py"
  "deal-aggregator:--afternoon|.agents/skills/deal-aggregator/headless-afternoon-prompt.md|scripts/validate_deal_aggregator_integrity.py"
  "deal-aggregator:--digest-mode|.agents/skills/deal-aggregator/headless-friday-prompt.md|scripts/validate_deal_aggregator_integrity.py"
  "conference-discovery:sunday|.agents/skills/conference-discovery/headless-sunday-prompt.md|scripts/validate_conference_discovery_integrity.py"
  "post-call-analyzer:on-trigger|.agents/skills/post-call-analyzer/headless-on-trigger-prompt.md|scripts/validate_post_call_analyzer_integrity.py"
)

for row in "${scheduled_coverage[@]}"; do
  IFS='|' read -r workflow prompt validator <<< "$row"
  if [ -f "$prompt" ]; then
    pass "$workflow headless prompt exists"
  else
    fail "$workflow headless prompt is missing: $prompt"
  fi
  if [ -f "$validator" ]; then
    pass "$workflow validator exists"
  else
    fail "$workflow validator is missing: $validator"
  fi
done

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

if [ -e scripts/audit-email-no-send.sh ]; then
  if bash -n scripts/audit-email-no-send.sh; then
    pass "scripts/audit-email-no-send.sh syntax"
  else
    fail "scripts/audit-email-no-send.sh syntax"
  fi
  if scripts/audit-email-no-send.sh >/dev/null 2>&1; then
    pass "email no-send audit"
  else
    fail "email no-send audit"
  fi
else
  warn "scripts/audit-email-no-send.sh not present"
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
set -a
source "$HOME/.config/op-sa-token.env" >/dev/null 2>&1 || true
set +a
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
