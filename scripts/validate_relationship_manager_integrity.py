#!/usr/bin/env python3
"""
Wrapper-level integrity validator for relationship-manager scheduled runs.

Runs as POST_RUN_CHECK after launchd wrapper completes. Independent of skill-internal
validation. Catches silent-success failures where Claude exits 0 but no artifact
landed at brain/context/relationship-status-{date}.md.

Note: Does NOT gate on Attio writes succeeding. Attio MCP can be down (as of
2026-04-26), and we still want a graceful artifact recording the fact in
"System Status Alerts" rather than the wrapper hard-failing.

Exit codes:
  0  Pass — artifact exists, has frontmatter, has at least one expected section header
  2  Fail — artifact missing or malformed

Usage:
  python3 validate_relationship_manager_integrity.py [--date YYYY-MM-DD]
"""

import os
import re
import sys
from datetime import date, datetime


_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_REPO_ROOT = os.path.dirname(_SCRIPT_DIR)
VAULT_DIR = os.environ.get(
    "RELATIONSHIP_MANAGER_VAULT_DIR",
    os.path.join(_REPO_ROOT, "brain", "context"),
)

# Sections defined by SKILL.md "Output Artifact" template.
# At least one of these must appear (skill may legitimately omit empty sections).
EXPECTED_SECTIONS = [
    "## Overdue Contacts",
    "## Auto-Resolved",
    "## Pending Intros",
    "## Warm Intro Opportunities",
    "## Vault → Attio Syncs",
    "## Attio Dedup Needed",
    "## System Status Alerts",
]


def main() -> int:
    args = sys.argv[1:]
    if "--date" in args:
        idx = args.index("--date")
        run_date = datetime.fromisoformat(args[idx + 1]).date()
    else:
        run_date = date.today()

    artifact = os.path.join(VAULT_DIR, f"relationship-status-{run_date.isoformat()}.md")

    failures = []

    if not os.path.exists(artifact):
        failures.append(f"artifact missing: {artifact}")
    else:
        with open(artifact) as f:
            content = f.read()

        # Frontmatter check
        if not content.startswith("---"):
            failures.append(f"artifact has no YAML frontmatter (must start with '---'): {artifact}")
        else:
            fm_match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
            if not fm_match:
                failures.append(f"frontmatter unterminated: {artifact}")
            else:
                fm = fm_match.group(1)
                if "type: relationship-status" not in fm:
                    failures.append(f"frontmatter missing 'type: relationship-status'")
                if f"date: {run_date.isoformat()}" not in fm:
                    failures.append(f"frontmatter date does not match run date {run_date}")

        # At least one expected section must be present
        sections_found = [s for s in EXPECTED_SECTIONS if s in content]
        if not sections_found:
            failures.append(
                f"no expected sections found; expected at least one of: {EXPECTED_SECTIONS}"
            )

        # Sanity: artifact should be > 200 bytes — empty stubs are not real outputs
        if os.path.getsize(artifact) < 200:
            failures.append(
                f"artifact suspiciously small ({os.path.getsize(artifact)} bytes) — likely empty stub"
            )

    if failures:
        print(
            f"RELATIONSHIP-MANAGER VALIDATOR FAILED for {run_date}:",
            file=sys.stderr,
        )
        for f in failures:
            print(f"  - {f}", file=sys.stderr)
        return 2

    print(f"RELATIONSHIP-MANAGER VALIDATOR PASSED for {run_date}")
    print(f"  artifact: {artifact}")
    print(f"  size: {os.path.getsize(artifact)} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
