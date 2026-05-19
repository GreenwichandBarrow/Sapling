# shellcheck shell=bash
# Canonical interactive credential bootstrap for op://-backed CLIs.
#
# ALWAYS source this before gog / attio / apollo / any CLI whose secrets live
# as op:// refs in scripts/.env.launchd. It (a) loads the 1Password service-
# account token the systemd units inject, (b) resolves every op:// ref via
# `op inject`, (c) exports the real values into the current shell. Secrets
# never touch stdout or the transcript.
#
#   Usage:  source scripts/op-env.sh && gog docs export <id> --format txt
#
# Why this exists: repeatedly sourced .env.launchd raw (op:// strings, not
# values) -> gog "aes.KeyUnwrap(): integrity check failed" -> flailing /
# spurious credential rotations. The credential ladder starts at 1Password;
# this file is that first rung made trivial. See
# memory/feedback_op_env_before_op_backed_cli.md.

_OPENV_DIR="$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")"

set -a
# 1Password service-account token (systemd supplies this; interactive shells must source it).
# shellcheck disable=SC1091
source "$HOME/.config/op-sa-token.env" >/dev/null 2>&1
# Resolve op:// refs to real values. NEVER `source .env.launchd` raw.
eval "$(op inject -i "${_OPENV_DIR}/.env.launchd" 2>/dev/null)"
set +a

unset _OPENV_DIR
