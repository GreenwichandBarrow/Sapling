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

Strategy: if a command references scripts/.env.launchd AND sources/evals it
AND does not also invoke `op inject` (nor go through the sanctioned
scripts/op-env.sh wrapper), BLOCK with the canonical one-liner. False
positives are acceptable; silent auth failure is not.
"""

import re
from typing import Optional

from ..models import Decision, HandlerResult

_ENV_LAUNCHD = re.compile(r"\.env\.launchd")
# Sourcing forms: `source X`, `. X`, or `eval "$(... X)"` style consumption.
_SOURCES_ENV = re.compile(
    r"(^|[\s;&|])(source|\.)\s+[^\s;&|]*\.env\.launchd"
    r"|eval\s+[\"']?\$\([^)]*\.env\.launchd"
)
_HAS_OP_INJECT = re.compile(r"\bop\s+inject\b")
_USES_WRAPPER = re.compile(r"scripts/op-env\.sh")


def enforce_op_first(input_data: dict) -> Optional[HandlerResult]:
    """PreToolUse[Bash]: require op:// resolution before consuming .env.launchd."""
    command = input_data.get("tool_input", {}).get("command", "")
    if not command or not _ENV_LAUNCHD.search(command):
        return None

    # Going through the sanctioned wrapper, or doing op inject inline → fine.
    if _USES_WRAPPER.search(command) or _HAS_OP_INJECT.search(command):
        return None

    # Only the *consumption* (source/eval) is the antipattern. `op inject -i
    # .env.launchd`, `sed -i .env.launchd`, etc. are handled elsewhere or fine.
    if not _SOURCES_ENV.search(command):
        return None

    truncated = command if len(command) <= 200 else command[:200] + "…"
    msg = (
        "BLOCKED — sourcing scripts/.env.launchd raw loads op:// reference "
        "strings, not secret values (this is the gog 'integrity check failed' "
        "trap). 1Password is the first rung of the credential ladder.\n"
        "Use the canonical bootstrap instead:\n"
        "  source scripts/op-env.sh && <your op://-backed command>\n"
        "Or resolve inline: eval \"$(op inject -i scripts/.env.launchd)\" "
        "(after sourcing ~/.config/op-sa-token.env).\n"
        "See memory/feedback_op_env_before_op_backed_cli.md\n"
        f"Command was: {truncated}"
    )
    return HandlerResult(decision=Decision.BLOCK, reason=msg)
