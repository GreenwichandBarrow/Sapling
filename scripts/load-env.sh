#!/bin/bash
# Source-able helper that loads scripts/.env.launchd into the current shell.
# If the env file contains op:// references AND the 1Password CLI is
# available, resolves the references via `op inject` so the actual secret
# values are exported. Otherwise sources the file as-is.
#
# Usage from a wrapper script:
#   source "$REPO_ROOT/scripts/load-env.sh"
#   load_env "$REPO_ROOT/scripts/.env.launchd"
#
# Caller is responsible for `set -a` / `set +a` if they need automatic
# export of every variable (most existing wrappers do this).

load_env() {
  local f="$1"
  if [ -z "$f" ]; then
    echo "load_env: missing env-file path" >&2
    return 1
  fi
  if command -v op >/dev/null 2>&1 && grep -q 'op://' "$f" 2>/dev/null; then
    # op inject reads the env file, substitutes op:// references with the
    # resolved secret values, and writes the result to stdout. Sourcing
    # via process substitution avoids touching disk with secrets.
    # shellcheck disable=SC1090
    source <(op inject -i "$f" 2>/dev/null)
  else
    # shellcheck disable=SC1090,SC1091
    source "$f"
  fi
}
