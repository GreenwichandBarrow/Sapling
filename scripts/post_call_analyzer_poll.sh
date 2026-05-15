#!/usr/bin/env bash
# post_call_analyzer_poll.sh — server-side detector for new Granola calls.
# Fires twice daily (1pm + 6pm ET) via systemd timer. Uses ~/.local/bin/granola-api
# wrapper for Granola REST API access (auth via 1Password, no MCP).
#
# Architecture: see .claude/skills/post-call-analyzer/SKILL.md
# Wrapper:      see ~/.local/bin/granola-api

set -uo pipefail

REPO_ROOT="${CLAUDE_PROJECT_DIR:-/home/ubuntu/projects/Sapling}"
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

# Bootstrap 1Password service-account token (granola-api wrapper does the rest)
if [[ -f "$HOME/.config/op-sa-token.env" ]]; then
  set -a; source "$HOME/.config/op-sa-token.env"; set +a
fi

# Determine checkpoint (default: 24h ago on first run)
if [[ -f "$CHECKPOINT_FILE" ]]; then
  SINCE="$(cat "$CHECKPOINT_FILE")"
else
  SINCE="$(date -u -d '24 hours ago' '+%Y-%m-%dT%H:%M:%SZ')"
  log "no prior checkpoint, defaulting to $SINCE"
fi

log "polling for notes updated since $SINCE"

# Ensure processed.json exists with valid shape
if [[ ! -s "$PROCESSED_LEDGER" ]]; then
  echo '{"processed": [], "last_updated": ""}' > "$PROCESSED_LEDGER"
fi

# Call granola-api
NOTES_JSON="$(/home/ubuntu/.local/bin/granola-api since "$SINCE" 2>>"$LOG_FILE")"
RC=$?
if [[ $RC -ne 0 || -z "$NOTES_JSON" ]]; then
  log "granola-api failed (rc=$RC); leaving checkpoint untouched, will retry next fire"
  exit 0
fi

# Filter to unprocessed IDs + write queue files
NEW_COUNT=$(python3 - <<PYEOF
import json, os, sys
notes = json.loads("""$NOTES_JSON""")
ledger = json.load(open("$PROCESSED_LEDGER"))
# processed.json stores a list of dict entries ({"id": ..., ...}); legacy
# history may contain bare-string IDs. Be defensive against both so a future
# format change can't re-crash this with TypeError: unhashable type: 'dict'.
processed = set()
for p in ledger.get("processed", []):
    if isinstance(p, dict):
        pid = p.get("id")
        if pid:
            processed.add(pid)
    elif isinstance(p, str):
        processed.add(p)
queue_dir = "$QUEUE_DIR"
existing = set(f.replace(".json","") for f in os.listdir(queue_dir) if f.endswith(".json") and not f.startswith("."))
new = 0
for n in notes:
    nid = n.get("id")
    if not nid: continue
    if nid in processed: continue
    if nid in existing: continue
    out = os.path.join(queue_dir, f"{nid}.json")
    with open(out, "w") as f:
        json.dump({
            "id": nid,
            "title": n.get("title"),
            "created_at": n.get("created_at"),
            "updated_at": n.get("updated_at"),
            "owner": n.get("owner"),
            "queued_at": "$(date -Is)",
            "detector": "granola-api-rest",
        }, f, indent=2)
    new += 1
print(new)
PYEOF
)
PY_RC=$?

# Silent-crash guard: the root failure on 2026-05-15 was a python TypeError
# swallowed into a blank NEW_COUNT, which made [[ -gt 0 ]] silently false and
# the Claude run never launched. Make a python crash LOUD, not silent.
if [[ $PY_RC -ne 0 ]] || ! [[ "$NEW_COUNT" =~ ^[0-9]+$ ]]; then
  log "ERROR: filter heredoc crashed (py_rc=$PY_RC, NEW_COUNT='$NEW_COUNT') — NOT advancing checkpoint, will retry next fire"
  if command -v op >/dev/null 2>&1 && SLACK_HOOK="$(op read 'op://GB Server/u2shpr72znynqh2s62jue25wzi/password' 2>/dev/null)" && [[ -n "$SLACK_HOOK" ]]; then
    curl -s -o /dev/null -X POST -H 'Content-Type: application/json' \
      -d "{\"text\":\":rotating_light: post-call-analyzer poll FAILED $TODAY — filter heredoc crashed (py_rc=$PY_RC). Calls NOT processed; checkpoint held.\"}" \
      "$SLACK_HOOK" || true
  fi
  exit 1
fi

log "queued $NEW_COUNT new notes"

# Advance checkpoint to NOW (only on success)
date -u '+%Y-%m-%dT%H:%M:%SZ' > "$CHECKPOINT_FILE"

# If anything queued, kick off Claude run via run-skill.sh.
# Use nohup + setsid + </dev/null + & to fully detach from systemd cgroup;
# without this, systemd kills the child when the Type=oneshot parent exits
# (the run-skill.sh wrapper takes minutes; the parent exits in <1s).
if [[ "$NEW_COUNT" -gt 0 ]]; then
  log "invoking post-call-analyzer:on-trigger headless run (detached)"
  setsid nohup bash "$REPO_ROOT/scripts/run-skill.sh" post-call-analyzer:on-trigger \
    </dev/null >>"$LOG_FILE" 2>&1 &
  disown $!
  log "headless run launched (pid $!) — detached from systemd cgroup"
fi

log "poll complete"
exit 0
