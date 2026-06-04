"""Block `gog sheets update` Bash calls that pass a positional value containing
`|` or `,` characters — those are gog's cell-delim and row-delim respectively
and silently corrupt the write.

Why this exists:
- 2026-05-01: Notes-column writes via `gog sheets update ... "user prose, with
  commas, and pipes|like|this"` got parsed as multi-row + multi-cell payloads,
  scrambling adjacent data. See `memory/feedback_gog_sheets_value_delimiters.md`.

Strategy: detect the unsafe call shape at PreToolUse and BLOCK before execution.
Safe path is `--values-json` (explicit JSON payload bypasses delim parsing) or
direct Sheets API.

The hook only fires when ALL of:
  1. command contains `gog sheets update` (substring)
  2. command does NOT contain `--values-json`
  3. some positional value (i.e. a token after the command/flags) contains
     `|` or `,`

False positives (blocking a legit positional value with a comma) are acceptable
— Kay would rather see a block than scramble a sheet. Override path: switch to
`--values-json` with explicit JSON.
"""

import re
import shlex
from typing import Optional

from ..models import Decision, HandlerResult


# Match the gog sheets update invocation. Tolerate any leading wrapper
# (env vars, sudo, etc.) by using a substring search.
_GOG_SHEETS_UPDATE = re.compile(r"\bgog\s+sheets\s+update\b")

# Flags that take an argument — we skip the next token when seeing these.
_ARG_TAKING_FLAGS = {
    "--sheet-id", "--sheet", "--spreadsheet", "--spreadsheet-id",
    "--tab", "--tab-name", "--range", "--cell",
    "--account", "--credentials", "--token", "--profile",
    "--major-dimension", "--input-option", "--value-input-option",
    "--output", "-o", "--format",
}


def block_gog_sheets_delimiter_writes(input_data: dict) -> Optional[HandlerResult]:
    """PreToolUse[Bash]: block `gog sheets update` with risky positional value."""
    tool_input = input_data.get("tool_input", {})
    command = tool_input.get("command", "")
    if not command:
        return None

    # Fast path
    if "gog" not in command or "sheets" not in command or "update" not in command:
        return None
    if not _GOG_SHEETS_UPDATE.search(command):
        return None

    # Safe path: --values-json present
    if "--values-json" in command:
        return None

    # Also tolerate the explicit `--values` flag-equals form if user redirects
    # to a file (no inline string risk). Hard to verify cleanly, so we allow
    # `--values @file` shape here.
    if re.search(r"--values\s+@\S+", command):
        return None

    # Tokenize. If unparseable, be conservative and let it through (parse
    # failures shouldn't manifest as false-block on a different tool).
    try:
        tokens = shlex.split(command, posix=True)
    except ValueError:
        return None

    # Walk tokens after the `update` subcommand looking for a positional value.
    # Skip flags (--foo or --foo=bar) and known arg-taking flags' next token.
    seen_update = False
    skip_next = False
    for tok in tokens:
        if skip_next:
            skip_next = False
            continue
        if not seen_update:
            if tok == "update":
                seen_update = True
            continue
        # We're past `update`. Now scanning for a positional value.
        if tok.startswith("--") or tok.startswith("-"):
            base = tok.split("=", 1)[0]
            if "=" in tok:
                # Inline value form — check it for delim risk
                _, val = tok.split("=", 1)
                if _has_risky_delim(val):
                    return _block(command, f"flag value {base}=... contains | or ,")
                continue
            if base in _ARG_TAKING_FLAGS:
                skip_next = True
            continue
        # Positional token. This is the suspected value payload.
        if _has_risky_delim(tok):
            return _block(command, "positional value contains | or ,")
        # If first positional doesn't have risky chars, we still keep scanning
        # in case the value is later (some gog forms put the value last).

    return None


def _has_risky_delim(value: str) -> bool:
    return ("|" in value) or ("," in value)


def _block(command: str, why: str) -> HandlerResult:
    truncated = command if len(command) <= 200 else command[:200] + "…"
    msg = (
        f"BLOCKED — `gog sheets update` with positional value containing | or , ({why}).\n"
        f"`gog sheets update` parses `|` as cell-delim and `,` as row-delim — your\n"
        f"value will be silently split across cells/rows.\n"
        f"\n"
        f"Use one of:\n"
        f"  gog sheets update ... --values-json '[[\"your, prose | here\"]]'\n"
        f"  # or call Sheets API directly via python\n"
        f"\n"
        f"See memory/feedback_gog_sheets_value_delimiters.md\n"
        f"Command was: {truncated}"
    )
    return HandlerResult(decision=Decision.BLOCK, reason=msg)
