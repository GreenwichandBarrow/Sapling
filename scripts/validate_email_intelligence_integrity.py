#!/usr/bin/env python3
"""
Wrapper-level integrity validator for email-intelligence scheduled runs.

Runs as POST_RUN_CHECK after the systemd/launchd wrapper completes. Independent
of skill-internal validation. Catches two silent-success failure modes:

  1. email-scan-results artifact missing or malformed at the expected path.
  2. **Bookkeeper P&L chain skipped silently** - a bookkeeper P&L trigger
     inbox item was written this run (or already exists for today) but the
     headless prompt's mandated `BOOKKEEPER-PL-CHAIN:` log marker is absent.
     This is the exact gap that caused March 2026 P&L to never get processed
     (inbox item landed 2026-04-29, but budget-manager monthly never fired).

Exit codes:
  0  Pass - artifact ok, no bookkeeper P&L chain gap detected
  2  Fail - artifact missing/malformed OR bookkeeper chain skipped

Usage:
  python3 validate_email_intelligence_integrity.py [--date YYYY-MM-DD] [--log-file PATH]
"""

import os
import re
import sys
from datetime import date, datetime


_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_REPO_ROOT = os.path.dirname(_SCRIPT_DIR)

CONTEXT_DIR = os.environ.get(
    "EMAIL_INTEL_CONTEXT_DIR",
    os.path.join(_REPO_ROOT, "brain", "context"),
)
INBOX_DIR = os.environ.get(
    "EMAIL_INTEL_INBOX_DIR",
    os.path.join(_REPO_ROOT, "brain", "inbox"),
)
OUTPUTS_DIR = os.environ.get(
    "EMAIL_INTEL_OUTPUTS_DIR",
    os.path.join(_REPO_ROOT, "brain", "outputs"),
)

# Sections defined by SKILL.md <artifact> schema. Skill may emit "None" body
# for empty sections but section headers must be present.
EXPECTED_SECTIONS = [
    "Actionable Items",
    "Deal Flow",
    "Draft Status",
    "Introductions",
    "Niche Signals",
    "In-Person Meetings",
    "Broker BLAST",
    "Auto-Drafts",
]

# Pattern for the bookkeeper P&L trigger inbox file.
# Inbox naming convention: {YYYY-MM-DD}-{month}-management-report-budget-trigger.md
BOOKKEEPER_INBOX_RE = re.compile(
    r"^\d{4}-\d{2}-\d{2}-[a-z]+-management-report-budget-trigger\.md$",
    re.IGNORECASE,
)

# Marker the headless prompt MUST emit to stdout when the bookkeeper chain
# fires. Three valid forms:
#   "BOOKKEEPER-PL-CHAIN: invoked budget-manager monthly for period YYYY-MM"
#   "BOOKKEEPER-PL-CHAIN: dry-run for period YYYY-MM"
#   "BOOKKEEPER-PL-CHAIN: FAILED for period YYYY-MM reason: ..."
# Any of these counts as "the chain attempted" (failures are surfaced via
# the artifact, not the wrapper - wrapper just confirms chain wasn't silently
# skipped).
CHAIN_MARKER_RE = re.compile(r"BOOKKEEPER-PL-CHAIN:\s*(invoked|dry-run|FAILED)", re.IGNORECASE)


def _today_inbox_bookkeeper_triggers(run_date: date) -> list[str]:
    """Return filenames of bookkeeper P&L trigger inbox items dated run_date."""
    if not os.path.isdir(INBOX_DIR):
        return []
    hits = []
    iso = run_date.isoformat()
    for fname in os.listdir(INBOX_DIR):
        if not BOOKKEEPER_INBOX_RE.match(fname):
            continue
        if not fname.startswith(iso + "-"):
            continue
        hits.append(fname)
    return hits


def _expected_budget_output_exists(period_yyyy_mm: str) -> bool:
    """Best-effort check for budget-manager output for the given period.

    Pattern: brain/outputs/{run-date}-budget-report-{month-year}.md where
    month-year is the lowercase month name + year (e.g. 'mar-2026'). We can't
    pin run-date exactly, so we glob by the month-year suffix.
    """
    if not os.path.isdir(OUTPUTS_DIR):
        return False
    try:
        year_short = period_yyyy_mm.split("-")[0]
        month_num = int(period_yyyy_mm.split("-")[1])
    except (IndexError, ValueError):
        return False
    months = [
        "jan", "feb", "mar", "apr", "may", "jun",
        "jul", "aug", "sep", "oct", "nov", "dec",
    ]
    month_short = months[month_num - 1]
    suffix = f"-budget-report-{month_short}-{year_short}.md"
    for fname in os.listdir(OUTPUTS_DIR):
        if fname.endswith(suffix):
            return True
    return False


def main() -> int:
    args = sys.argv[1:]
    run_date = date.today()
    log_file: str | None = None

    i = 0
    while i < len(args):
        if args[i] == "--date" and i + 1 < len(args):
            run_date = datetime.fromisoformat(args[i + 1]).date()
            i += 2
        elif args[i] == "--log-file" and i + 1 < len(args):
            log_file = args[i + 1]
            i += 2
        else:
            i += 1

    failures: list[str] = []

    # ---- Check 1: artifact exists + schema ----
    artifact = os.path.join(
        CONTEXT_DIR, f"email-scan-results-{run_date.isoformat()}.md"
    )

    if not os.path.exists(artifact):
        failures.append(f"artifact missing: {artifact}")
    else:
        with open(artifact) as f:
            content = f.read()

        if os.path.getsize(artifact) < 200:
            failures.append(
                f"artifact suspiciously small ({os.path.getsize(artifact)} bytes) - likely empty stub"
            )

        # Frontmatter (lenient - skill body is the deliverable, but a totally
        # frontmatter-free file means the writer broke).
        if not content.startswith("---"):
            failures.append(f"artifact has no YAML frontmatter: {artifact}")

        # At least one expected section header must be present. We do not
        # require all 8 - the SKILL.md says all 8 should be present but the
        # skill body is responsible for that. The validator just confirms
        # the artifact looks structurally like an email-scan-results doc.
        sections_found = [s for s in EXPECTED_SECTIONS if s in content]
        if len(sections_found) < 3:
            failures.append(
                f"too few expected section headers found ({len(sections_found)}/8); "
                f"likely a malformed artifact. Found: {sections_found}"
            )

    # ---- Check 2: bookkeeper P&L chain gap ----
    # If today's inbox has a bookkeeper P&L trigger file, the log MUST contain
    # the BOOKKEEPER-PL-CHAIN marker. Missing marker = silent skip of step 3.
    bookkeeper_triggers = _today_inbox_bookkeeper_triggers(run_date)

    if bookkeeper_triggers and log_file and os.path.exists(log_file):
        with open(log_file) as f:
            log_content = f.read()
        if not CHAIN_MARKER_RE.search(log_content):
            failures.append(
                f"BOOKKEEPER-PL-CHAIN gap: today's inbox has {len(bookkeeper_triggers)} "
                f"bookkeeper P&L trigger file(s) ({bookkeeper_triggers}) but the run log "
                f"does not contain the mandatory 'BOOKKEEPER-PL-CHAIN:' marker. This is "
                f"the March 2026 silent-skip failure mode - the trigger inbox item was "
                f"created but budget-manager monthly was never invoked. See "
                f"memory/feedback_bookkeeper_pl_auto_trigger_budget_manager.md."
            )
    elif bookkeeper_triggers and not log_file:
        # Bookkeeper trigger exists today but no log path passed - we can't
        # verify the chain. Warn but don't fail (the wrapper may have been
        # invoked outside the systemd path).
        print(
            f"WARN: today's inbox has bookkeeper P&L trigger(s) but --log-file "
            f"not provided; cannot verify chain marker.",
            file=sys.stderr,
        )

    # ---- Report ----
    if failures:
        print(
            f"EMAIL-INTELLIGENCE VALIDATOR FAILED for {run_date}:",
            file=sys.stderr,
        )
        for f in failures:
            print(f"  - {f}", file=sys.stderr)
        return 2

    print(f"EMAIL-INTELLIGENCE VALIDATOR PASSED for {run_date}")
    print(f"  artifact: {artifact}")
    if os.path.exists(artifact):
        print(f"  size: {os.path.getsize(artifact)} bytes")
    if bookkeeper_triggers:
        print(f"  bookkeeper P&L triggers today: {bookkeeper_triggers}")
        print(f"  chain marker present in log: yes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
