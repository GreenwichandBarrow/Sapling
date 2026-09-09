#!/usr/bin/env bash
# Codex post-call analyzer detector. Live systemd timer polls Granola through
# the 1Password-backed granola-api REST wrapper.

set -uo pipefail

REPO_ROOT="${CODEX_PROJECT_DIR:-/home/ubuntu/projects/Sapling}"
CACHE_DIR="$HOME/.cache/post-call-analyzer"
CHECKPOINT_FILE="$CACHE_DIR/last-checkpoint.txt"
QUEUE_DIR="$REPO_ROOT/brain/trackers/post-call-analyzer/queue"
PROCESSED_LEDGER="$REPO_ROOT/brain/trackers/post-call-analyzer/processed.json"
LOG_DIR="$REPO_ROOT/logs/scheduled"
TODAY="$(date '+%Y-%m-%d')"
LOG_FILE="$LOG_DIR/post-call-analyzer-poll-$TODAY.log"

mkdir -p "$CACHE_DIR" "$QUEUE_DIR" "$LOG_DIR"
mkdir -p "$(dirname "$PROCESSED_LEDGER")"

log() { echo "$(date -Is) [poll] $*" | tee -a "$LOG_FILE"; }

if [[ -f "$HOME/.config/op-sa-token.env" ]]; then
  set -a; source "$HOME/.config/op-sa-token.env"; set +a
fi

if [[ -f "$CHECKPOINT_FILE" ]]; then
  SINCE="$(cat "$CHECKPOINT_FILE")"
else
  SINCE="$(date -u -d '24 hours ago' '+%Y-%m-%dT%H:%M:%SZ')"
  log "no prior checkpoint, defaulting to $SINCE"
fi

log "polling for notes updated since $SINCE"

if [[ ! -s "$PROCESSED_LEDGER" ]]; then
  echo '{"processed": [], "last_updated": ""}' > "$PROCESSED_LEDGER"
fi

NOTES_JSON="$("$HOME/.local/bin/granola-api" since "$SINCE" 2>>"$LOG_FILE")"
RC=$?
if [[ $RC -ne 0 || -z "$NOTES_JSON" ]]; then
  log "granola-api failed (rc=$RC); leaving checkpoint untouched, will retry next fire"
  exit 0
fi

COUNTS=$(python3 - "$PROCESSED_LEDGER" "$QUEUE_DIR" "$(date -Is)" 3<<<"$NOTES_JSON" <<'PYEOF'
import json, os, sys
# Keep API data out of Python source (titles can contain quotes/backslashes).
notes = json.load(os.fdopen(3))
ledger = json.load(open(sys.argv[1]))
processed = set()
for p in ledger.get("processed", []):
    if isinstance(p, dict):
        pid = p.get("id")
        if pid:
            processed.add(pid)
    elif isinstance(p, str):
        processed.add(p)
queue_dir = sys.argv[2]
existing = set(f.replace(".json","") for f in os.listdir(queue_dir) if f.endswith(".json") and not f.startswith("."))
new = 0
for n in notes:
    nid = n.get("id")
    if not nid:
        continue
    if nid in processed:
        continue
    if nid in existing:
        continue
    out = os.path.join(queue_dir, f"{nid}.json")
    with open(out, "w") as f:
        json.dump({
            "id": nid,
            "title": n.get("title"),
            "created_at": n.get("created_at"),
            "updated_at": n.get("updated_at"),
            "owner": n.get("owner"),
            "queued_at": sys.argv[3],
            "detector": "granola-api-rest",
        }, f, indent=2)
    new += 1
# A failed worker leaves existing queue entries even when the next poll is empty.
pending = {f[:-5] for f in os.listdir(queue_dir)
           if f.endswith(".json") and not f.startswith(".")} - processed
print(new, len(pending))
PYEOF
)
PY_RC=$?

if [[ $PY_RC -ne 0 ]] || ! [[ "$COUNTS" =~ ^[0-9]+\ [0-9]+$ ]]; then
  log "ERROR: queue filter failed (py_rc=$PY_RC) - NOT advancing checkpoint, will retry next fire"
  if [[ "${SAPLING_NO_NOTIFICATIONS:-0}" != "1" ]] && command -v op >/dev/null 2>&1 && SLACK_HOOK="$(op read 'op://GB Server/u2shpr72znynqh2s62jue25wzi/password' 2>/dev/null)" && [[ -n "$SLACK_HOOK" ]]; then
    curl -s -o /dev/null -X POST -H 'Content-Type: application/json' \
      -d "{\"text\":\":rotating_light: post-call-analyzer poll FAILED $TODAY - filter heredoc crashed (py_rc=$PY_RC). Calls NOT processed; checkpoint held.\"}" \
      "$SLACK_HOOK" || true
  fi
  exit 1
fi

read -r NEW_COUNT PENDING_COUNT <<< "$COUNTS"
log "queued $NEW_COUNT new notes"
log "$PENDING_COUNT unprocessed notes pending"

date -u '+%Y-%m-%dT%H:%M:%SZ' > "$CHECKPOINT_FILE"

if [[ "$PENDING_COUNT" -gt 0 ]]; then
  log "invoking post-call-analyzer:on-trigger Codex headless run (detached)"
  setsid nohup bash "$REPO_ROOT/scripts/run-agent-skill.sh" post-call-analyzer:on-trigger \
    </dev/null >>"$LOG_FILE" 2>&1 &
  disown $!
  log "Codex headless run launched (pid $!) - detached from systemd cgroup"
fi

log "poll complete"
exit 0
