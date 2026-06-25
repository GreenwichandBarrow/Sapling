#!/usr/bin/env bash
set -euo pipefail

# Neutral scheduled skill runner. Phase 1 runtime is Codex.
AGENT_RUNTIME="${AGENT_RUNTIME:-codex}"
SKILL_NAME="${1:-}"
shift || true
SKILL_ARGS="$*"

if [ -z "$SKILL_NAME" ]; then
  echo "Usage: run-agent-skill.sh <skill-name> [args...]" >&2
  exit 64
fi

if [[ -z "$SKILL_ARGS" && "$SKILL_NAME" == *:* ]]; then
  SKILL_ARGS="${SKILL_NAME#*:}"
  SKILL_NAME="${SKILL_NAME%%:*}"
fi

WORKDIR="$(cd "$(dirname "$0")/.." && pwd)"
LOG_DIR="$WORKDIR/logs/scheduled"
LOG_FILE="$LOG_DIR/${LOG_PREFIX:-$SKILL_NAME}-$(date +%Y-%m-%d-%H%M).log"
KILL_SWITCH="${CODEX_SCHEDULED_KILL_SWITCH:-$HOME/.config/sapling/disable-codex-scheduled}"

mkdir -p "$LOG_DIR"
find "$LOG_DIR" -name "*.log" -mtime +14 -delete 2>/dev/null || true

log() {
  printf "%s\n" "$*" | tee -a "$LOG_FILE"
}

post_failure() {
  local message="$1"
  if [ -n "${SLACK_WEBHOOK_OPERATIONS:-}" ]; then
    curl -s -X POST "$SLACK_WEBHOOK_OPERATIONS" \
      -H "Content-type: application/json" \
      -d "{\"text\":\"$message\"}" >/dev/null 2>&1 || true
  fi
}

cd "$WORKDIR"

{
  echo "=== $SKILL_NAME ==="
  echo "Started: $(date)"
  echo "Runner: codex"
  echo "Agent: Codex"
  echo "Runtime: $AGENT_RUNTIME"
  echo "Args: $SKILL_ARGS"
} >> "$LOG_FILE"

if [ "$AGENT_RUNTIME" != "codex" ]; then
  log "ERROR: unsupported AGENT_RUNTIME=$AGENT_RUNTIME"
  exit 64
fi

if [ -e "$KILL_SWITCH" ]; then
  log "DISABLED: Codex scheduled kill switch exists at $KILL_SWITCH"
  exit 0
fi

# Load scheduled Codex settings. Authentication intentionally uses the saved
# Codex CLI ChatGPT/OAuth login instead of a Platform API key.
# shellcheck disable=SC1091
set -a
source "$HOME/.config/op-sa-token.env" >/dev/null 2>&1 || true
set +a
# shellcheck disable=SC1091
source "$WORKDIR/scripts/load-env.sh"
set -a
load_env "$WORKDIR/scripts/.env.codex"
set +a

export GOG_ACCOUNT="${GOG_ACCOUNT:-kay.s@greenwichandbarrow.com}"
TODAY="${TODAY:-$(date +%Y-%m-%d)}"
export TODAY

# Many validators call gog after Codex exits. Codex itself may source op-env.sh
# inside the prompt, but that does not affect this wrapper process.
if [ -f "$WORKDIR/scripts/op-env.sh" ]; then
  # shellcheck disable=SC1091
  source "$WORKDIR/scripts/op-env.sh" >/dev/null 2>&1 || true
fi

# Hard email safety preflight: scheduled jobs may create drafts only through explicit draft paths.
# Scan the active skill plus known email-adjacent trigger scripts; do not scan every
# script for every job, because legacy/fallback scripts can contain unrelated send references.
EMAIL_SCAN_TARGETS=()
[ -d "$WORKDIR/.agents/skills/$SKILL_NAME" ] && EMAIL_SCAN_TARGETS+=("$WORKDIR/.agents/skills/$SKILL_NAME")
case "$SKILL_NAME" in
  email-intelligence|post-call-analyzer|relationship-manager|meeting-brief|outreach-manager)
    [ -e "$WORKDIR/scripts/post_call_analyzer_poll.sh" ] && EMAIL_SCAN_TARGETS+=("$WORKDIR/scripts/post_call_analyzer_poll.sh")
    [ -e "$WORKDIR/scripts/post_call_analyzer_poll.py" ] && EMAIL_SCAN_TARGETS+=("$WORKDIR/scripts/post_call_analyzer_poll.py")
    ;;
esac
if [ "${#EMAIL_SCAN_TARGETS[@]}" -gt 0 ]; then
  EMAIL_MATCH_FILE="$(mktemp)"
  if grep -RInE "gog[[:space:]]+(send|gmail[[:space:]]+(send|forward|autoreply|drafts?[[:space:]]+send))|messages\.send|send_email|smtp|superhuman.*send|Superhuman.*send" "${EMAIL_SCAN_TARGETS[@]}" > "$EMAIL_MATCH_FILE" 2>/dev/null; then
    # Ignore explicit prohibition/policy prose such as "NEVER call gog gmail send".
    # Real executable-looking send paths still block below.
    if grep -viE "never|do not|don't|forbidden|draft-only|no-send|blocked" "$EMAIL_MATCH_FILE" >> "$LOG_FILE"; then
      rm -f "$EMAIL_MATCH_FILE"
      log "BLOCKED: potential email-send path found for $SKILL_NAME. Never send email."
      post_failure "BLOCKED: Codex scheduled job $SKILL_NAME found a potential email-send path. Review required."
      exit 3
    fi
  fi
  rm -f "$EMAIL_MATCH_FILE"
fi

HEADLESS_PROMPT_FILE=""
case "$SKILL_NAME:$SKILL_ARGS" in
  "calibration-workflow:"|"calibration-workflow:weekly")
    HEADLESS_PROMPT_FILE="$WORKDIR/.agents/skills/calibration-workflow/headless-weekly-prompt.md"
    POST_RUN_CHECK="${POST_RUN_CHECK:-python3 \"$WORKDIR/scripts/validate_calibration_workflow_integrity.py\" --date \"$TODAY\"}" ;;
  "target-discovery:phase2-sunday")
    HEADLESS_PROMPT_FILE="$WORKDIR/.agents/skills/target-discovery/headless-phase2-prompt.md"
    POST_RUN_CHECK="${POST_RUN_CHECK:-python3 \"$WORKDIR/scripts/validate_phase2_integrity.py\" --date \"$TODAY\"}" ;;
  "weekly-tracker:friday")
    HEADLESS_PROMPT_FILE="$WORKDIR/.agents/skills/weekly-tracker/headless-friday-prompt.md"
    POST_RUN_CHECK="${POST_RUN_CHECK:-python3 \"$WORKDIR/scripts/validate_weekly_tracker_integrity.py\"}" ;;
  "nightly-tracker-audit:nightly")
    HEADLESS_PROMPT_FILE="$WORKDIR/.agents/skills/nightly-tracker-audit/headless-nightly-prompt.md"
    POST_RUN_CHECK="${POST_RUN_CHECK:-python3 \"$WORKDIR/scripts/validate_nightly_tracker_audit_integrity.py\"}" ;;
  "relationship-manager:daily")
    HEADLESS_PROMPT_FILE="$WORKDIR/.agents/skills/relationship-manager/headless-daily-prompt.md"
    POST_RUN_CHECK="${POST_RUN_CHECK:-python3 \"$WORKDIR/scripts/validate_relationship_manager_integrity.py\"}" ;;
  "jj-operations:sunday-prep")
    HEADLESS_PROMPT_FILE="$WORKDIR/.agents/skills/jj-operations/headless-sunday-prep-prompt.md"
    POST_RUN_CHECK="${POST_RUN_CHECK:-python3 \"$WORKDIR/scripts/validate_jj_operations_integrity.py\"}" ;;
  "launchd-debugger:daily")
    HEADLESS_PROMPT_FILE="$WORKDIR/.agents/skills/launchd-debugger/headless-daily-prompt.md"
    POST_RUN_CHECK="${POST_RUN_CHECK:-python3 \"$WORKDIR/scripts/validate_launchd_debugger_integrity.py\"}" ;;
  "launchd-debugger:on-failure")
    HEADLESS_PROMPT_FILE="$WORKDIR/.agents/skills/launchd-debugger/headless-on-failure-prompt.md" ;;
  "niche-intelligence:tuesday")
    HEADLESS_PROMPT_FILE="$WORKDIR/.agents/skills/niche-intelligence/headless-tuesday-prompt.md"
    POST_RUN_CHECK="${POST_RUN_CHECK:-python3 \"$WORKDIR/scripts/validate_niche_intelligence_integrity.py\" --date \"$TODAY\"}" ;;
  "email-intelligence:")
    HEADLESS_PROMPT_FILE="$WORKDIR/.agents/skills/email-intelligence/headless-weekday-prompt.md"
    POST_RUN_CHECK="${POST_RUN_CHECK:-python3 \"$WORKDIR/scripts/validate_email_intelligence_integrity.py\" --date \"$TODAY\" --log-file \"$LOG_FILE\"}" ;;
  "deal-aggregator:")
    HEADLESS_PROMPT_FILE="$WORKDIR/.agents/skills/deal-aggregator/headless-morning-prompt.md"
    POST_RUN_CHECK="${POST_RUN_CHECK:-python3 \"$WORKDIR/scripts/validate_deal_aggregator_integrity.py\" --mode morning --date \"$TODAY\"}" ;;
  "deal-aggregator:--afternoon")
    HEADLESS_PROMPT_FILE="$WORKDIR/.agents/skills/deal-aggregator/headless-afternoon-prompt.md"
    POST_RUN_CHECK="${POST_RUN_CHECK:-python3 \"$WORKDIR/scripts/validate_deal_aggregator_integrity.py\" --mode afternoon --date \"$TODAY\"}" ;;
  "conference-discovery:sunday")
    HEADLESS_PROMPT_FILE="$WORKDIR/.agents/skills/conference-discovery/headless-sunday-prompt.md"
    POST_RUN_CHECK="${POST_RUN_CHECK:-python3 \"$WORKDIR/scripts/validate_conference_discovery_integrity.py\" --date \"$TODAY\"}" ;;
  "post-call-analyzer:on-trigger")
    HEADLESS_PROMPT_FILE="$WORKDIR/.agents/skills/post-call-analyzer/headless-on-trigger-prompt.md"
    POST_RUN_CHECK="${POST_RUN_CHECK:-python3 \"$WORKDIR/scripts/validate_post_call_analyzer_integrity.py\"}" ;;
  "deal-aggregator:--digest-mode")
    HEADLESS_PROMPT_FILE="$WORKDIR/.agents/skills/deal-aggregator/headless-friday-prompt.md"
    POST_RUN_CHECK="${POST_RUN_CHECK:-python3 \"$WORKDIR/scripts/validate_deal_aggregator_integrity.py\" --mode digest --date \"$TODAY\"}" ;;
esac

if [ -n "$HEADLESS_PROMPT_FILE" ] && [ ! -f "$HEADLESS_PROMPT_FILE" ]; then
  log "BLOCKED: headless prompt missing: $HEADLESS_PROMPT_FILE"
  post_failure "BLOCKED: Codex scheduled job $SKILL_NAME missing headless prompt."
  exit 4
fi

if [ -z "${CODEX_MODEL:-}" ]; then
  case "$SKILL_NAME:$SKILL_ARGS" in
    "calibration-workflow:"|"calibration-workflow:weekly"|\
    "conference-discovery:sunday"|\
    "jj-operations:sunday-prep"|\
    "niche-intelligence:tuesday"|\
    "target-discovery:phase2-sunday")
      CODEX_MODEL="${CODEX_HEAVY_MODEL:-gpt-5.5}" ;;
    *)
      CODEX_MODEL="${CODEX_ROUTINE_MODEL:-gpt-5.4-mini}" ;;
  esac
fi
log "Model: $CODEX_MODEL"

# Idempotency guard for mutating daily relationship syncs. If a valid artifact
# already exists for today, do not re-run Codex and risk duplicate Attio/vault writes.
# Set RELATIONSHIP_MANAGER_ALLOW_RERUN=1 only for an intentional supervised rerun.
if [ "$SKILL_NAME:$SKILL_ARGS" = "relationship-manager:daily" ] && [ -z "${RELATIONSHIP_MANAGER_ALLOW_RERUN:-}" ]; then
  RELATIONSHIP_ARTIFACT="$WORKDIR/brain/context/relationship-status-$TODAY.md"
  if [ -f "$RELATIONSHIP_ARTIFACT" ]; then
    log "Idempotency check: existing relationship artifact found for $TODAY; validating before skip."
    set +e
    python3 "$WORKDIR/scripts/validate_relationship_manager_integrity.py" --date "$TODAY" >> "$LOG_FILE" 2>&1
    existing_status=$?
    set -e
    if [ "$existing_status" -eq 0 ]; then
      log "SKIPPED: relationship-manager already has a valid artifact for $TODAY. Set RELATIONSHIP_MANAGER_ALLOW_RERUN=1 for a supervised rerun."
      exit 0
    fi
    log "Existing relationship artifact failed validation; proceeding with Codex run."
  fi
fi

PROMPT_FILE="${HEADLESS_PROMPT_FILE:-}"
if [ -n "$HEADLESS_PROMPT_FILE" ] && [ "$SKILL_NAME" = "calibration-workflow" ]; then
  PROMPT_FILE="$(mktemp)"
  sed "s/{YYYY-MM-DD}/$TODAY/g" "$HEADLESS_PROMPT_FILE" > "$PROMPT_FILE"
  printf "\n\nScheduled date: %s\nUse this scheduled date for every report date, frontmatter date, tag date, title date, heading date, and validation path.\n" "$TODAY" >> "$PROMPT_FILE"
elif [ -z "$PROMPT_FILE" ]; then
  PROMPT_FILE="$(mktemp)"
  printf "Use the $%s skill. Arguments: %s\n\nRun this scheduled workflow faithfully in Sapling. NEVER send email. Drafts only where explicitly supported. Validate outputs and summarize results." "$SKILL_NAME" "$SKILL_ARGS" > "$PROMPT_FILE"
fi

CODEX_CMD=(codex exec --cd "$WORKDIR" --dangerously-bypass-approvals-and-sandbox --json --output-last-message "$LOG_FILE.final")
if [ -n "${CODEX_MODEL:-}" ]; then
  CODEX_CMD+=(--model "$CODEX_MODEL")
fi

log "Codex command: ${CODEX_CMD[*]} < prompt"
set +e
env -u CODEX_API_KEY "${CODEX_CMD[@]}" - < "$PROMPT_FILE" >> "$LOG_FILE" 2>&1
status=$?
set -e

if [ "$status" -ne 0 ]; then
  if grep -q "Selected model is at capacity" "$LOG_FILE" && [ -z "${CODEX_MODEL_FALLBACK_ATTEMPTED:-}" ]; then
    FALLBACK_MODEL="${CODEX_FALLBACK_MODEL:-gpt-5.5}"
    log "RETRY: codex exec hit model capacity on $CODEX_MODEL; retrying once with $FALLBACK_MODEL"
    CODEX_MODEL_FALLBACK_ATTEMPTED=1
    CODEX_CMD=(codex exec --cd "$WORKDIR" --dangerously-bypass-approvals-and-sandbox --json --output-last-message "$LOG_FILE.final" --model "$FALLBACK_MODEL")
    set +e
    env -u CODEX_API_KEY "${CODEX_CMD[@]}" - < "$PROMPT_FILE" >> "$LOG_FILE" 2>&1
    status=$?
    set -e
  fi
fi

if [ "$status" -ne 0 ]; then
  log "FAILED: codex exec exited $status"
  post_failure "FAILED: Codex scheduled job $SKILL_NAME exited $status."
  exit "$status"
fi

if [ -n "${POST_RUN_CHECK:-}" ]; then
  log "Post-run check: $POST_RUN_CHECK"
  set +e
  bash -lc "$POST_RUN_CHECK" >> "$LOG_FILE" 2>&1
  check_status=$?
  set -e
  if [ "$check_status" -ne 0 ]; then
    log "FAILED: post-run check exited $check_status"
    post_failure "FAILED: Codex scheduled job $SKILL_NAME post-run validation failed."
    exit "$check_status"
  fi
fi

# Health-monitor RED bridge: when health-monitor exits clean and its artifact
# landed at the expected path, fan out one launchd-debugger:on-failure spawn per
# RED row in the markdown artifact. The bridge is background-detached so the
# parent wrapper exits immediately.
if [ "$SKILL_NAME" = "health-monitor" ]; then
  HEALTH_ARTIFACT="$WORKDIR/brain/trackers/health/$(date +%Y-%m-%d)-health.md"
  if [ -f "$HEALTH_ARTIFACT" ]; then
    log "Firing health-monitor RED bridge against $HEALTH_ARTIFACT"
    bash "$WORKDIR/scripts/health-monitor-red-bridge.sh" "$HEALTH_ARTIFACT" >> "$LOG_FILE" 2>&1 || true
  else
    log "health-monitor RED bridge skipped — artifact not found at $HEALTH_ARTIFACT"
  fi
fi

log "Completed: $(date)"
