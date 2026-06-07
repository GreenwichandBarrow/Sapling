#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

status=0
tmp="$(mktemp)"
trap 'rm -f "$tmp"' EXIT

# Search migrated agent docs and operational scripts for executable-looking
# email-send commands. Policy text such as "NEVER call `gog gmail send`" is
# allowed; standalone commands that an agent might copy/run are not.
find .agents/skills scripts -type f \
  \( -name "*.md" -o -name "*.sh" -o -name "*.py" \) \
  ! -path "scripts/run-agent-skill.sh" \
  ! -path "scripts/check-codex-migration-readiness.sh" \
  ! -path "scripts/audit-email-no-send.sh" \
  -print0 |
while IFS= read -r -d '' file; do
  awk -v file="$file" '
    /^[[:space:]]*(gog[[:space:]]+(send([[:space:]]|$)|gmail[[:space:]]+(send|forward|autoreply)([[:space:]]|$)|gmail[[:space:]]+drafts?[[:space:]]+send([[:space:]]|$))|python[0-9.]*[[:space:]].*messages\.send|curl[[:space:]].*messages\.send|.*send_email[[:space:]]*\()/ {
      printf "%s:%d:%s\n", file, FNR, $0
    }
  ' "$file"
done > "$tmp"

if [ -s "$tmp" ]; then
  echo "FAIL: executable-looking email send commands found:"
  cat "$tmp"
  status=1
else
  echo "PASS: no executable-looking email send commands found in migrated skills/scripts"
fi

exit "$status"
