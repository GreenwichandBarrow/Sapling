"""Block Bash commands that would print contents of known-secret files.

Why this exists:
- 2026-04-26: leaked ATTIO_API_KEY by using Read tool on ~/.claude.json.
- 2026-04-27: leaked OpenAI/Salesforge/Motion/Attio/Apollo keys via
  `grep -nE "API_KEY" scripts/.env.launchd` — the value-printing pattern.

PostToolUse `redact_bash_secrets` runs too late (output already streamed; the
warning is advisory, the secrets still landed in transcript). PreToolUse block
is the only durable fix: prevent the value-printing command from executing.

Strategy: positive allowlist of value-suppressing patterns. If the command
references a known-secret path AND isn't on the allowlist, BLOCK. False
positives (blocking a legitimate call) are acceptable; false negatives are not.
"""

import re
import shlex
from typing import Optional

from ..models import Decision, HandlerResult


# Path patterns that always treat as secret-bearing.
# Match against the raw command string (substring search).
SECRET_PATH_PATTERNS = [
    re.compile(r"scripts/\.env\.launchd"),
    re.compile(r"(^|[\s'\"=])(\.env)([.\s'\"]|$)"),  # .env (root)
    re.compile(r"\.env\.[A-Za-z0-9_-]+"),             # .env.local, .env.production etc.
    re.compile(r"\.claude\.json\b"),
    re.compile(r"\.claude/settings(\.local)?\.json\b"),
    re.compile(r"credentials(\.json)?\b"),
    re.compile(r"\bsecrets/"),
    re.compile(r"\.key(\s|$|['\"])"),
    re.compile(r"\.pem(\s|$|['\"])"),
    re.compile(r"/tmp/[A-Za-z0-9_-]*-key\.txt"),
    re.compile(r"/tmp/[A-Za-z0-9_-]*-token\.txt"),
    re.compile(r"/tmp/attio-key"),
    re.compile(r"/tmp/apollo-key"),
]


# Value-printing command basenames. Any of these on a secret-path command
# requires explicit allowlist match below or it gets blocked.
VALUE_PRINTING_CMDS = {
    "grep", "egrep", "fgrep", "rg",
    "cat", "head", "tail", "less", "more", "bat", "view",
    "nl", "od", "xxd", "strings",
    "awk", "sed",
}


def block_secret_file_reads(input_data: dict) -> Optional[HandlerResult]:
    """PreToolUse[Bash]: block value-printing commands targeting secret files."""
    tool_input = input_data.get("tool_input", {})
    command = tool_input.get("command", "")
    if not command:
        return None

    # Fast path: does the command even mention a secret-file path?
    if not _mentions_secret_path(command):
        return None

    # Tokenize. If unparseable, be conservative and block.
    try:
        tokens = shlex.split(command, posix=True)
    except ValueError:
        return _block(command, "could not shlex-parse command (unbalanced quotes)")

    # Walk sub-commands separated by |, &&, ||, ;
    for sub in _split_subcommands(tokens):
        if not sub:
            continue
        cmd = _basename(sub[0])
        if cmd not in VALUE_PRINTING_CMDS:
            continue
        # This sub-command is a value-printer. Does it reference a secret path?
        sub_str = " ".join(sub)
        if not _mentions_secret_path(sub_str):
            continue
        # Apply per-command safety check.
        if _is_safe(cmd, sub):
            continue
        return _block(command, f"{cmd} on secret file without value-suppressing flags")

    return None


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _mentions_secret_path(text: str) -> bool:
    return any(p.search(text) for p in SECRET_PATH_PATTERNS)


def _basename(token: str) -> str:
    return token.rsplit("/", 1)[-1]


# Tokens that act as sub-command boundaries.
_BOUNDARY_TOKENS = {"|", "||", "&&", ";", "&"}


def _split_subcommands(tokens: list[str]) -> list[list[str]]:
    out: list[list[str]] = []
    cur: list[str] = []
    for t in tokens:
        if t in _BOUNDARY_TOKENS:
            if cur:
                out.append(cur)
                cur = []
        else:
            cur.append(t)
    if cur:
        out.append(cur)
    return out


def _expand_grep_flags(tokens: list[str]) -> set[str]:
    """Return short-form grep flags as a set, expanding bundled forms.

    `grep -nE pat` → {-n, -E}; `grep --count` → {--count}.
    """
    flags: set[str] = set()
    for t in tokens:
        if not t.startswith("-") or t == "-" or t == "--":
            continue
        if t.startswith("--"):
            flags.add(t.split("=", 1)[0])
            continue
        # short bundle: -nE → {-n, -E}
        for c in t[1:]:
            flags.add("-" + c)
    return flags


# Suppressing flags for grep family.
_GREP_SUPPRESSING_SHORT = {"-c", "-l", "-L", "-q"}
_GREP_SUPPRESSING_LONG = {
    "--count", "--files-with-matches", "--files-without-match",
    "--quiet", "--silent",
}


def _is_safe(cmd: str, sub: list[str]) -> bool:
    """Per-command allowlist. Returns True iff this invocation is safe to run."""
    if cmd in {"grep", "egrep", "fgrep", "rg"}:
        flags = _expand_grep_flags(sub)
        if flags & _GREP_SUPPRESSING_SHORT:
            return True
        if flags & _GREP_SUPPRESSING_LONG:
            return True
        return False

    if cmd == "sed":
        # sed -i (in-place) doesn't print to stdout — safe.
        flags = _expand_grep_flags(sub)
        return "-i" in flags

    if cmd == "awk":
        # Allow only the explicit name-only pattern: -F= with print $1 (or $1,$2 etc).
        # Reject any awk that prints $0 or whole records.
        joined = " ".join(sub)
        # Must declare a non-default field separator (typical for env-var-name extraction)
        has_F = bool(re.search(r"-F\s*['\"]?[^A-Za-z0-9_]", joined))
        # Body must only print numbered fields, never $0
        prints_only_fields = (
            re.search(r"\{\s*print\s+\$[1-9][0-9]*(\s*,\s*\$[1-9][0-9]*)*\s*\}", joined)
            and not re.search(r"\$0", joined)
            and not re.search(r"print\s+\$0", joined)
        )
        return bool(has_F and prints_only_fields)

    # cat/head/tail/less/more/bat/view/nl/od/xxd/strings → no safe form on secret files.
    return False


def _block(command: str, why: str) -> HandlerResult:
    truncated = command if len(command) <= 200 else command[:200] + "…"
    msg = (
        f"BLOCKED — secret-file content access ({why}).\n"
        f"Use one of:\n"
        f"  grep -c PATTERN <file>          # count only, no value\n"
        f"  grep -l PATTERN <file>          # filename only\n"
        f"  awk -F= '/^export/ {{print $1}}' <file>   # variable names only\n"
        f"  python3 -c \"...\"                # explicit redaction in Python\n"
        f"  sed -i 's/old/new/' <file>      # in-place edit (no stdout)\n"
        f"See memory/feedback_never_read_config_with_secrets.md\n"
        f"Command was: {truncated}"
    )
    return HandlerResult(decision=Decision.BLOCK, reason=msg)
