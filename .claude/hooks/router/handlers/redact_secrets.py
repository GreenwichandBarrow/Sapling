"""Redact secrets from Bash tool output before they appear in conversation."""

import re
from typing import Optional

from ..models import HandlerResult


# Pre-compiled patterns for performance
_SECRET_PATTERNS = [
    # API keys with sk- prefix (OpenAI, Anthropic, Stripe, etc.)
    (re.compile(r'\bsk-[A-Za-z0-9_-]{20,}\b'), '[REDACTED]'),
    # Slack tokens
    (re.compile(r'\bxox[bpras]-[A-Za-z0-9-]{10,}\b'), '[REDACTED]'),
    # Bearer tokens
    (re.compile(r'(Bearer\s+)[A-Za-z0-9_.~+/=-]{20,}'), r'\1[REDACTED]'),
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
    """PostToolUse[Bash]: scan output for secrets and inject redaction warning."""
    tool_name = input_data.get("tool_name", "")

    if tool_name != "Bash":
        return None

    tool_output = input_data.get("tool_output", "")
    if not tool_output or not isinstance(tool_output, str):
        # Try nested structure
        output_obj = input_data.get("tool_output", {})
        if isinstance(output_obj, dict):
            tool_output = output_obj.get("stdout", "") or output_obj.get("output", "")
        if not tool_output:
            return None

    redacted_output, count = _redact(tool_output)

    if count == 0:
        return None

    warning = (
        f"\n⚠ SECRET REDACTION: {count} secret pattern(s) detected and redacted from Bash output. "
        f"Do NOT attempt to retrieve or display the original values. "
        f"If you need these values, read them silently via Bash without echoing."
    )

    return HandlerResult(
        additional_context=warning,
        stderr_message=f"[redact-secrets] Redacted {count} secret(s) from Bash output",
    )


def _redact(text: str) -> tuple[str, int]:
    """Apply all secret patterns to text. Returns (redacted_text, match_count)."""
    count = 0
    for pattern, replacement in _SECRET_PATTERNS:
        text, n = pattern.subn(replacement, text)
        count += n
    return text, count
