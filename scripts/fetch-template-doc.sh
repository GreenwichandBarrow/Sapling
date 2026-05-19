#!/usr/bin/env bash
# Fetch a canonical Google Doc (templates etc.) as plain text — LIVE, not a
# vault snapshot. Resolves creds through 1Password automatically.
#
#   scripts/fetch-template-doc.sh                 # default: Intermediary templates
#   scripts/fetch-template-doc.sh <google_doc_id> # any doc
#
# Why this exists: drafting from the stale brain/outputs/*-templates.md
# snapshot instead of the live Drive doc is a recurring failure. The live doc
# is canonical (CLAUDE.md source-of-truth: Drive owns living documents). This
# makes pulling it the path of least resistance. See
# memory/feedback_op_env_before_op_backed_cli.md and
# feedback_no_intermediary_drafts_outside_template.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")/.." && pwd)"

# Canonical doc IDs (extend as needed).
DOC_ID="${1:-1gTQoCbaX8IyrTDli4Xd6IBtCqCT-DwciOUnNmgv0_J4}"  # G&B Intermediary Email Templates

# shellcheck disable=SC1091
source "${REPO_ROOT}/scripts/op-env.sh"

gog docs export "$DOC_ID" --format txt \
  --account "${GOG_ACCOUNT:-kay.s@greenwichandbarrow.com}" >/dev/null 2>&1

# gog writes to ~/.config/gogcli/drive-downloads/<id>_<title>.txt — find newest match.
OUT="$(ls -t "$HOME/.config/gogcli/drive-downloads/${DOC_ID}"_*.txt 2>/dev/null | head -1)"
if [[ -z "${OUT}" || ! -f "${OUT}" ]]; then
  echo "FETCH FAILED for doc ${DOC_ID} — check op-env.sh / gog auth (source scripts/op-env.sh && gog --no-input auth list)" >&2
  exit 1
fi

echo "# LIVE canonical doc ${DOC_ID} (Drive — authoritative; do NOT draft from vault snapshots)"
echo "# source: ${OUT}"
echo "---"
cat "${OUT}"
