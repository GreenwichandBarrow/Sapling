"""PreToolUse handler: block superhuman-draft.sh invocations that reference
owner-addressed financials (revenue, EBITDA, headcount, "$XM" quoted back at
the recipient).

Kay's rule (memory/feedback_no_revenue_in_outreach.md): never reference revenue,
employee count, or financials when writing TO an owner. These signal "we looked
you up" in a creepy way.

Carve-out: Kay's own buy-box paragraph mentioning "$2-5M EBITDA" is about HER
acquisition criteria, not the recipient's numbers. Allow that standard framing.
"""

import re
from typing import Optional

from ..models import Decision, HandlerResult

# Patterns that quote the recipient's financials back at them
OWNER_ADDRESSED_FINANCIALS = [
    # "your $5M", "your $40M revenue", "your 500 employees"
    re.compile(r"\byour\s+\$\d+[\d.,]*\s*(m|k|mm|million|billion)?\b", re.IGNORECASE),
    re.compile(r"\byour\s+\d+[\d.,]*\s*(m|k|mm|million|billion)\b", re.IGNORECASE),
    re.compile(r"\byour\s+(revenue|ebitda|arr|mrr|topline|top\s*line|ebit|ebitdar|gross\s*margin|net\s*income|profit)\b", re.IGNORECASE),
    re.compile(r"\byour\s+\d+\+?\s*(employees|ftes|staff|headcount|team\s*members?|people)\b", re.IGNORECASE),
    # "given your $5M revenue"
    re.compile(r"(given|with|at)\s+your\s+\$?\d+", re.IGNORECASE),
]

# Kay's standard buy-box text — allowed even though it contains $ amounts
BUYBOX_CARVEOUT_MARKERS = [
    "i am looking to acquire",  # Kay's first-person buy-box opener
    "looking for a founder-led",
    "currently looking at operationally critical",
    "~$2-5m ebitda",
    "~$2-5 m ebitda",
    "$2-5m ebitda",
]


def no_revenue_in_outreach(input_data: dict) -> Optional[HandlerResult]:
    tool_name = input_data.get("tool_name", "")
    if tool_name != "Bash":
        return None

    command = input_data.get("tool_input", {}).get("command", "") or ""
    if "superhuman-draft.sh" not in command:
        return None

    # Extract --body value from the command
    body = _extract_body(command)
    if not body:
        return None

    body_lower = body.lower()

    # If the body contains Kay's standard buy-box language, the $ amounts there
    # are allowed — but we still check for OTHER violations outside that passage.
    # Simple approach: remove the buy-box sentence, scan what remains.
    scan_text = body
    for marker in BUYBOX_CARVEOUT_MARKERS:
        idx = body_lower.find(marker)
        if idx >= 0:
            # Remove the full sentence containing the marker (rough: period-to-period)
            start = body.rfind(".", 0, idx) + 1
            end = body.find(".", idx + len(marker))
            if end == -1:
                end = len(body)
            scan_text = scan_text[:start] + scan_text[end + 1 :]

    for pattern in OWNER_ADDRESSED_FINANCIALS:
        match = pattern.search(scan_text)
        if match:
            reason = (
                f"Rule violation (no-revenue-in-outreach): draft contains "
                f"'{match.group(0)}' — a recipient-addressed financial reference. "
                "Per memory/feedback_no_revenue_in_outreach, never reference the "
                "owner's revenue, EBITDA, headcount, or financials in outreach; "
                "it signals 'we researched you' in a creepy way. Rewrite the "
                "draft to remove the financial reference and resubmit. Kay's "
                "own buy-box framing ('$2-5M EBITDA') is allowed — but only "
                "when describing her acquisition criteria, not the recipient's."
            )
            return HandlerResult(
                decision=Decision.BLOCK,
                reason=reason,
                exit_code=2,
            )

    return None


def _extract_body(command: str) -> str:
    """Pull the --body argument from a superhuman-draft.sh command line.

    The wrapper uses `--body "..."` or `--body '...'` with shell quoting;
    on a complex command the value may span multiple lines. Use a permissive
    parser that finds --body and grabs everything inside its matching quotes.
    """
    idx = command.find("--body")
    if idx < 0:
        return ""
    # skip --body and whitespace
    i = idx + len("--body")
    while i < len(command) and command[i] in " \t":
        i += 1
    if i >= len(command):
        return ""
    quote = command[i]
    if quote not in ("'", '"'):
        # Unquoted — grab until next flag or end
        end = command.find(" --", i)
        return command[i : end if end > 0 else len(command)]
    # Quoted — find matching close quote, handling escapes minimally
    j = i + 1
    while j < len(command):
        if command[j] == "\\" and j + 1 < len(command):
            j += 2
            continue
        if command[j] == quote:
            return command[i + 1 : j]
        j += 1
    return command[i + 1 :]
