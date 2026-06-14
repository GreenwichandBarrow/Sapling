#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SYSTEMD_USER_DIR="${SYSTEMD_USER_DIR:-$HOME/.config/systemd/user}"
OUTPUT_DIR="${OUTPUT_DIR:-$ROOT/docs/migrations/systemd-codex-templates/generated}"
MODE="dry-run"
GROUP="all"

usage() {
  cat <<'EOF'
Usage: prepare-codex-systemd-cutover.sh [--dry-run|--apply] [--group GROUP]

Creates Codex systemd service variants from the live user services.

Modes:
  --dry-run   Write generated service files under docs/migrations; do not touch live units.
  --apply     Update live user services for the selected group after readiness checks.

Groups:
  all, health-monitor, calibration, conference, deal-aggregator,
  email-intelligence, jj-operations, launchd-debugger, niche-intelligence,
  tracker-audit, relationship-manager, target-discovery, post-call-analyzer

Phase 1 policy:
  - Never modifies timers.
  - Never deletes Claude files.
  - Applies only explicitly selected service ExecStart changes.
  - Requires Codex OAuth readiness before --apply.
EOF
}

while [ "$#" -gt 0 ]; do
  case "$1" in
    --dry-run) MODE="dry-run" ;;
    --apply) MODE="apply" ;;
    --group)
      shift
      GROUP="${1:-}"
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "ERROR: unknown argument: $1" >&2
      usage >&2
      exit 64
      ;;
  esac
  shift
done

declare -A SERVICE_GROUPS
declare -A EXECSTARTS

add_service() {
  local group="$1"
  local service="$2"
  local exec_start="$3"
  SERVICE_GROUPS["$service"]="$group"
  EXECSTARTS["$service"]="$exec_start"
}

add_service "calibration" "calibration-workflow.service" "ExecStart=/bin/bash %h/projects/Sapling/scripts/run-agent-skill.sh calibration-workflow"
add_service "conference" "conference-discovery.service" "ExecStart=/bin/bash %h/projects/Sapling/scripts/run-agent-skill.sh conference-discovery sunday"
add_service "deal-aggregator" "deal-aggregator.service" "ExecStart=/bin/bash %h/projects/Sapling/scripts/run-agent-skill.sh deal-aggregator"
add_service "deal-aggregator" "deal-aggregator-afternoon.service" "ExecStart=/bin/bash %h/projects/Sapling/scripts/run-agent-skill.sh deal-aggregator --afternoon"
add_service "deal-aggregator" "deal-aggregator-friday.service" "ExecStart=/bin/bash %h/projects/Sapling/scripts/run-agent-skill.sh deal-aggregator --digest-mode"
add_service "email-intelligence" "email-intelligence.service" "ExecStart=/bin/bash %h/projects/Sapling/scripts/run-agent-skill.sh email-intelligence"
add_service "health-monitor" "health-monitor.service" "ExecStart=/bin/bash %h/projects/Sapling/scripts/run-agent-skill.sh health-monitor"
add_service "jj-operations" "jj-operations-sunday.service" "ExecStart=/bin/bash %h/projects/Sapling/scripts/run-agent-skill.sh jj-operations:sunday-prep"
add_service "launchd-debugger" "launchd-debugger.service" "ExecStart=/bin/bash %h/projects/Sapling/scripts/run-agent-skill.sh launchd-debugger:daily"
add_service "niche-intelligence" "niche-intelligence.service" "ExecStart=/bin/bash %h/projects/Sapling/scripts/run-agent-skill.sh niche-intelligence:tuesday"
add_service "tracker-audit" "nightly-tracker-audit.service" "ExecStart=/bin/bash %h/projects/Sapling/scripts/run-agent-skill.sh nightly-tracker-audit:nightly"
add_service "relationship-manager" "relationship-manager.service" "ExecStart=/bin/bash %h/projects/Sapling/scripts/run-agent-skill.sh relationship-manager:daily"
add_service "target-discovery" "target-discovery-sunday.service" "ExecStart=/bin/bash %h/projects/Sapling/scripts/run-agent-skill.sh target-discovery phase2-sunday"
add_service "post-call-analyzer" "post-call-analyzer-poll.service" "ExecStart=/bin/bash %h/projects/Sapling/scripts/post_call_analyzer_poll.codex.sh"

selected_services=()
for service in "${!EXECSTARTS[@]}"; do
  if [ "$GROUP" = "all" ] || [ "${SERVICE_GROUPS[$service]}" = "$GROUP" ]; then
    selected_services+=("$service")
  fi
done

if [ "${#selected_services[@]}" -eq 0 ]; then
  echo "ERROR: no services matched group '$GROUP'" >&2
  usage >&2
  exit 64
fi

if [ "$MODE" = "apply" ]; then
  if ! "$ROOT/scripts/check-codex-migration-readiness.sh"; then
    echo "ERROR: readiness failed; refusing live systemd cutover." >&2
    exit 1
  fi
fi

mkdir -p "$OUTPUT_DIR/$GROUP"

for service in "${selected_services[@]}"; do
  source_file="$SYSTEMD_USER_DIR/$service"
  if [ ! -f "$source_file" ]; then
    echo "ERROR: live service not found: $source_file" >&2
    exit 1
  fi

  generated="$OUTPUT_DIR/$GROUP/$service"
  awk -v replacement="${EXECSTARTS[$service]}" '
    BEGIN { replaced = 0 }
    /^ExecStart=/ {
      print replacement
      replaced = 1
      next
    }
    { print }
    END {
      if (!replaced) {
        print "ERROR: missing ExecStart" > "/dev/stderr"
        exit 1
      }
    }
  ' "$source_file" > "$generated"
  echo "generated $generated"

  if [ "$MODE" = "apply" ]; then
    cp "$source_file" "$source_file.pre-codex-$(date +%Y%m%d%H%M%S)"
    cp "$generated" "$source_file"
    echo "updated live service $service"
  fi
done

if [ "$MODE" = "apply" ]; then
  systemctl --user daemon-reload
  echo "systemd user manager reloaded"
else
  echo "dry-run complete; live systemd units were not modified"
fi
