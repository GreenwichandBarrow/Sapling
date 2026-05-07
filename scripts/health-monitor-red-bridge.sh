#!/bin/bash
# health-monitor-red-bridge.sh
#
# Reads health-monitor's weekly markdown artifact and auto-fires
# launchd-debugger:on-failure for every RED row in the standard health tables.
#
# Yellow stays informational. Trend table is skipped (it cites historical RED
# states for resolved items).
#
# Recursion guard:
#   - $1 == "health-monitor" (the failing job that triggered this) → exit 0
#   - env FROM_HEALTH_BRIDGE=1 → exit 0
#
# Modes:
#   DRY_RUN=1 → log "WOULD FIRE" lines only, never spawn
#   default   → background-detached spawn of run-skill.sh launchd-debugger:on-failure
#               with FROM_HEALTH_BRIDGE=1 + RED_ITEM_* + HEALTH_ARTIFACT_PATH env
#
# Always exits 0 — never blocks the parent wrapper.

set -u

WORKDIR="$HOME/Documents/AI Operations"
LOG_DIR="$WORKDIR/logs/scheduled"
TODAY=$(date +%Y-%m-%d)
HHMM=$(date +%H%M)
BRIDGE_LOG="$LOG_DIR/health-monitor-red-bridge-${TODAY}-${HHMM}.log"
WRAPPER_PATH="$WORKDIR/scripts/run-skill.sh"

mkdir -p "$LOG_DIR"

log() {
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" >> "$BRIDGE_LOG"
}

log "=== health-monitor-red-bridge start ==="

# Recursion guard 1: arg-form (when run-skill.sh's auto-fire path passes the
# failing job name as $1). Belt-and-suspenders — the wrapper integration we
# write below uses the artifact-path form, but this guards against future
# refactors that pass the skill name positionally.
if [ "${1:-}" = "health-monitor" ]; then
  log "RECURSION GUARD: \$1=health-monitor → exit 0 without firing"
  exit 0
fi

# Recursion guard 2: env-form. If we're already inside a bridge-triggered run,
# bail (prevents launchd-debugger:on-failure → cascading bridge invocation).
if [ "${FROM_HEALTH_BRIDGE:-0}" = "1" ]; then
  log "RECURSION GUARD: FROM_HEALTH_BRIDGE=1 → exit 0 without firing"
  exit 0
fi

# Resolve artifact path. If $1 looks like a path to an .md file, use it.
# Else default to the latest *-health.md in brain/trackers/health/.
ARTIFACT="${1:-}"
if [ -z "$ARTIFACT" ] || [ ! -f "$ARTIFACT" ]; then
  ARTIFACT=$(ls -1t "$WORKDIR/brain/trackers/health/"*-health.md 2>/dev/null | head -1)
  log "Artifact arg empty/missing — defaulting to latest: $ARTIFACT"
fi

if [ -z "$ARTIFACT" ] || [ ! -f "$ARTIFACT" ]; then
  log "FATAL: no health-monitor artifact found at $ARTIFACT — exit 0"
  exit 0
fi

log "Artifact: $ARTIFACT"
log "Mode: ${DRY_RUN:+DRY_RUN}${DRY_RUN:-LIVE}"

# Parse RED rows. Filter:
#   - row pipe-split into 5 fields (NF==5) → standard health table
#       (leading + trailing pipe yields empty $1 + empty $5; data in $2 $3 $4)
#   - $3 (status column) trimmed == "RED"
# This excludes the Trend table (NF==6, format `| Item | 4/24 | 5/1 | Δ |`)
# which can carry RED values in historical columns.
PARSED=$(awk -F'|' '
  NF == 5 {
    s = $3
    gsub(/^[ \t]+|[ \t]+$/, "", s)
    if (s == "RED") {
      lbl = $2; det = $4
      gsub(/^[ \t]+|[ \t]+$/, "", lbl)
      gsub(/^[ \t]+|[ \t]+$/, "", det)
      # Replace literal tabs in the detail text so our \t separator stays clean.
      gsub(/\t/, " ", lbl)
      gsub(/\t/, " ", det)
      print lbl "\t" det
    }
  }
' "$ARTIFACT")

if [ -z "$PARSED" ]; then
  log "No RED rows detected — exit 0"
  exit 0
fi

RED_COUNT=$(echo "$PARSED" | wc -l | tr -d ' ')
log "RED rows detected: $RED_COUNT"

# Slugify helper: lowercase, replace [^a-z0-9]+ with -, trim leading/trailing -
slugify() {
  echo "$1" | tr '[:upper:]' '[:lower:]' \
    | sed -E 's/[^a-z0-9]+/-/g; s/^-+//; s/-+$//'
}

FIRED=0
SKIPPED=0
WOULD_FIRE=0

# Use process substitution so the loop runs in the parent shell — preserves
# counters across iterations.
while IFS=$'\t' read -r LABEL DETAIL; do
  [ -z "$LABEL" ] && continue
  SLUG=$(slugify "$LABEL")
  if [ -z "$SLUG" ]; then
    log "SKIP: label produced empty slug ($LABEL)"
    SKIPPED=$((SKIPPED + 1))
    continue
  fi

  if [ "${DRY_RUN:-0}" = "1" ]; then
    # Dry-run: log only, never spawn. Truncate detail to keep log readable.
    DET_TRUNC=$(echo "$DETAIL" | cut -c1-200)
    log "WOULD FIRE: launchd-debugger:on-failure for RED=$SLUG label=\"$LABEL\" detail=\"$DET_TRUNC\""
    echo "WOULD FIRE: launchd-debugger:on-failure for RED=$SLUG detail=$DET_TRUNC" >&2
    WOULD_FIRE=$((WOULD_FIRE + 1))
    continue
  fi

  # Live mode: background-detached spawn. Each fire gets its own log file with
  # the slug appended so multiple parallel on-failure runs don't collide.
  CHILD_LOG="$LOG_DIR/launchd-debugger-on-failure-${TODAY}-${HHMM}-${SLUG}.log"
  log "FIRE: launchd-debugger:on-failure RED=$SLUG → $CHILD_LOG"

  FROM_HEALTH_BRIDGE=1 \
  RED_ITEM_ID="$SLUG" \
  RED_ITEM_LABEL="$LABEL" \
  RED_ITEM_DETAIL="$DETAIL" \
  HEALTH_ARTIFACT_PATH="$ARTIFACT" \
    nohup "$WRAPPER_PATH" launchd-debugger:on-failure </dev/null >>"$CHILD_LOG" 2>&1 &
  FIRED=$((FIRED + 1))
done <<EOF
$PARSED
EOF

log "Summary: fired=$FIRED skipped=$SKIPPED would_fire=$WOULD_FIRE"
log "=== health-monitor-red-bridge end ==="

exit 0
