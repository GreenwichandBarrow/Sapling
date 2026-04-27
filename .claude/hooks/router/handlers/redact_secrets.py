"""Detect secrets in tool output (Bash + MCP) and inject a redaction warning.

LIMITATION: PostToolUse hooks cannot actually mutate tool output — by the time
this fires, the result has already streamed back into model context. This
handler can only detect secrets and inject an advisory message warning the
agent not to repeat them. Full prevention requires either:
  - PreToolUse blocking (see secret_file_guard.py for the Bash side)
  - A behavioral rule in CLAUDE.md (verify auth via curl before MCP, etc.)

Vector coverage:
  - Bash output (stdout/stderr printed by shell commands)
  - MCP tool error responses (e.g. attio-mcp 401 dumps full Authorization
    header in its error formatter — caught the 2026-04-27 leak after-the-fact)
"""

import json
import re
from typing import Optional

from ..models import HandlerResult


# Pre-compiled patterns for performance
_SECRET_PATTERNS = [
    # API keys with sk- prefix (OpenAI, Anthropic, Stripe, etc.)
    (re.compile(r'\bsk-[A-Za-z0-9_-]{20,}\b'), '[REDACTED]'),
    # Slack tokens
    (re.compile(r'\bxox[bpras]-[A-Za-z0-9-]{10,}\b'), '[REDACTED]'),
    # Bearer tokens — covers MCP error responses with full Authorization headers
    (re.compile(r'(Bearer\s+)[A-Za-z0-9_.~+/=-]{20,}'), r'\1[REDACTED]'),
    # Authorization header in JSON-encoded form (escape-quoted)
    (re.compile(r'(\\?"Authorization\\?"\s*:\s*\\?"Bearer\s+)[A-Za-z0-9_.~+/=-]{20,}'), r'\1[REDACTED]'),
    # Slack webhook URLs
    (re.compile(r'https://hooks\.slack\.com/[A-Za-z0-9/_-]+'), '[REDACTED-WEBHOOK-URL]'),
    # Generic webhook URLs
    (re.compile(r'https://[a-z0-9.-]+/webhook[s]?/[A-Za-z0-9/_-]+'), '[REDACTED-WEBHOOK-URL]'),
    # Key-value pairs: api_key=VALUE, token=VALUE, secret=VALUE, etc.
    (re.compile(
        r'(?i)((?:api[_-]?key|apikey|secret[_-]?key|access[_-]?token|auth[_-]?token'
        r'|refresh[_-]?token|client[_-]?secret|private[_-]?key|password|passwd'
        r'|secret|token)\s*[=:]\s*)["\']?([A-Za-z0-9_.~+/=-]{8,})["\']?'
    ), r'\1[REDACTED]'),
    # URL query params containing secrets
    (re.compile(
        r'(?i)([?&](?:api[_-]?key|token|key|secret|access[_-]?token|auth)=)'
        r'([A-Za-z0-9_.~+/=-]{8,})'
    ), r'\1[REDACTED]'),
    # AWS-style keys (AKIA...)
    (re.compile(r'\bAKIA[A-Z0-9]{16}\b'), '[REDACTED]'),
    # GitHub tokens (ghp_, gho_, ghs_, ghr_)
    (re.compile(r'\bgh[psotr]_[A-Za-z0-9_]{36,}\b'), '[REDACTED]'),
    # Generic long hex strings after = (likely secrets, not paths/hashes in normal output)
    (re.compile(r'(=\s*)["\']?([0-9a-f]{40,})["\']?'), r'\1[REDACTED]'),
]


def redact_bash_secrets(input_data: dict) -> Optional[HandlerResult]:
    """PostToolUse: scan output for secret patterns and warn the agent.

    Runs for ALL tool calls (Bash + MCP). MCP tool error responses can leak
    bearer tokens via upstream API error formatters (e.g. attio-mcp's axios
    error includes the full Authorization header).
    """
    tool_name = input_data.get("tool_name", "")
    if not tool_name:
        return None

    # Collect all candidate output strings from common locations.
    candidates = []
    candidates.append(_stringify(input_data.get("tool_output")))
    candidates.append(_stringify(input_data.get("tool_response")))
    # Some tool error paths nest the message
    output_obj = input_data.get("tool_output") or input_data.get("tool_response") or {}
    if isinstance(output_obj, dict):
        for k in ("stdout", "stderr", "output", "error", "message", "details", "rawError"):
            candidates.append(_stringify(output_obj.get(k)))
    full_text = "\n".join(c for c in candidates if c)
    if not full_text:
        return None

    _, count = _redact(full_text)
    if count == 0:
        return None

    warning = (
        f"\n⚠ SECRET REDACTION: {count} secret pattern(s) detected in {tool_name} output "
        f"(Bearer tokens / API keys / webhook URLs / etc.). The original values are now in "
        f"this conversation transcript and must be considered COMPROMISED. Do NOT echo, "
        f"summarize, or repeat them. Recommend rotation if this is a live credential. "
        f"Source-of-leak likely: upstream error formatter (e.g. axios HTTP error including "
        f"Authorization header). For Attio specifically: verify auth via `curl` with output "
        f"suppression BEFORE calling any MCP tool when a token has just been rotated."
    )

    return HandlerResult(
        additional_context=warning,
        stderr_message=f"[redact-secrets] Detected {count} secret pattern(s) in {tool_name} output — already in transcript, treat as compromised",
    )


def _stringify(obj) -> str:
    if obj is None:
        return ""
    if isinstance(obj, str):
        return obj
    try:
        return json.dumps(obj)
    except (TypeError, ValueError):
        return str(obj)


def _redact(text: str) -> tuple[str, int]:
    """Apply all secret patterns to text. Returns (redacted_text, match_count)."""
    count = 0
    for pattern, replacement in _SECRET_PATTERNS:
        text, n = pattern.subn(replacement, text)
        count += n
    return text, count
