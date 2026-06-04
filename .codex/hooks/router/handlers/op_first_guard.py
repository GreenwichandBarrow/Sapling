"""Block Bash commands that source/eval scripts/.env.launchd WITHOUT resolving
op:// refs through 1Password first.

Why this exists:
- Recurring failure: `source scripts/.env.launchd` puts the literal op://
  reference strings (not the secret values) into the environment. gog then
  fails with `aes.KeyUnwrap(): integrity check failed`, which looks like a
  corrupted keyring and triggers flailing / spurious credential rotations.
- The credential ladder starts at 1Password. The correct path is
  `source scripts/op-env.sh` (loads the op SA token + `op inject` resolves
  every ref). This guard makes the wrong path impossible, not just discouraged.

Strategy: shlex-tokenize, walk sub-commands. Flag ONLY when an actual
`source` / `.` / `eval` command *consumes* a .env.launchd path — never on mere
substring presence (a `git commit -m "...source .env.launchd..."` message or a
`grep` pattern must not trip it). Allow when `op inject` or the sanctioned
scripts/op-env.sh wrapper appears anywhere in the command.
"""

import re
import shlex
from typing import Optional

from ..models import Decision, HandlerResult

_ENV_LAUNCHD = re.compile(r"\.env\.launchd")
_HAS_OP_INJECT = re.compile(r"\bop\s+inject\b")
_USES_WRAPPER = re.compile(r"op-env\.sh")
_BOUNDARY = {"|", "||", "&&", ";", "&", "(", ")"}
_CONSUMERS = {"source", ".", "eval"}


def _basename(tok: str) -> str:
    return tok.rsplit("/", 1)[-1]


def _split_subcommands(tokens: list[str]) -> list[list[str]]:
    out: list[list[str]] = []
    cur: list[str] = []
    for t in tokens:
        if t in _BOUNDARY:
            if cur:
                out.append(cur)
                cur = []
        else:
            cur.append(t)
    if cur:
        out.append(cur)
    return out


def enforce_op_first(input_data: dict) -> Optional[HandlerResult]:
    """PreToolUse[Bash]: require op:// resolution before consuming .env.launchd."""
    command = input_data.get("tool_input", {}).get("command", "")
    if not command or not _ENV_LAUNCHD.search(command):
        return None

    # Sanctioned wrapper or inline op inject anywhere → fine.
    if _USES_WRAPPER.search(command) or _HAS_OP_INJECT.search(command):
        return None

    try:
        tokens = shlex.split(command, posix=True)
    except ValueError:
        # Unparseable; be conservative only if it plausibly sources the file.
        if re.search(r"(^|[\s;&|])(source|\.)\s+\S*\.env\.launchd", command):
            return _block(command)
        return None

    for sub in _split_subcommands(tokens):
        if not sub:
            continue
        head = _basename(sub[0])
        # `set -a` style prefixes: skip to the real command.
        idx = 0
        while idx < len(sub) and _basename(sub[idx]) in {"set", "-a", "+a"}:
            idx += 1
        head = _basename(sub[idx]) if idx < len(sub) else head
        if head not in _CONSUMERS:
            continue
        # This sub-command is source/./eval. Does an ARGUMENT name .env.launchd?
        if any(_ENV_LAUNCHD.search(arg) for arg in sub[idx + 1:]):
            return _block(command)

    return None


def _block(command: str) -> HandlerResult:
    truncated = command if len(command) <= 200 else command[:200] + "…"
    msg = (
        "BLOCKED — sourcing scripts/.env.launchd raw loads op:// reference "
        "strings, not secret values (the gog 'integrity check failed' trap). "
        "1Password is the first rung of the credential ladder.\n"
        "Use the canonical bootstrap instead:\n"
        "  source scripts/op-env.sh && <your op-backed command>\n"
        "Or resolve inline: eval \"$(op inject -i scripts/.env.launchd)\" "
        "(after sourcing ~/.config/op-sa-token.env).\n"
        "See memory/feedback_op_env_before_op_backed_cli.md\n"
        f"Command was: {truncated}"
    )
    return HandlerResult(decision=Decision.BLOCK, reason=msg)
