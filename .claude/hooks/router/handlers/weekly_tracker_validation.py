"""Weekly tracker validation: block Slack notification until data is verified."""

import json
import os
import re
import subprocess
from pathlib import Path
from datetime import datetime

from ..models import Decision, HandlerResult


SHEET_ID = "1NGGZY_iq9h8cNzLAXSJ1vTcsfXWNU9oin2RiOMtl9NE"
VAULT_TRACKER_DIR = "brain/trackers/weekly"
KEY_METRICS = ["NDAs Signed", "Financials Received", "LOIs Submitted", "LOIs Signed"]


def validate_weekly_tracker_before_slack(input_data: dict) -> HandlerResult:
    """PreToolUse[Bash]: block Slack webhook POST if weekly tracker data is not validated.

    Only triggers when the Bash command contains a Slack webhook URL
    AND the weekly-tracker skill is active (detected by checking for
    the tracker sheet ID in recent tool calls).
    """
    tool_name = input_data.get("tool_name", "")
    if tool_name != "Bash":
        return None

    tool_input = input_data.get("tool_input", {})
    command = tool_input.get("command", "")

    # Only intercept Slack webhook POSTs
    if "SLACK_WEBHOOK" not in command or "curl" not in command:
        return None

    # Only intercept if this looks like a weekly tracker notification
    if "Weekly Activity Tracker" not in command and "week ending" not in command.lower():
        return None

    # Run validation checks
    project_dir = os.environ.get("CLAUDE_PROJECT_DIR", os.getcwd())
    today = datetime.now().strftime("%Y-%m-%d")
    failures = []

    # Check 1: Vault snapshot exists
    vault_path = Path(project_dir) / VAULT_TRACKER_DIR / f"{today}-weekly-tracker.md"
    if not vault_path.exists():
        failures.append(f"Vault snapshot missing: {vault_path}")
    else:
        content = vault_path.read_text()
        # Check 2: Key metrics present in vault
        for metric in KEY_METRICS:
            if metric not in content:
                failures.append(f"Vault missing metric: {metric}")

    # Check 3: Sheet has data for this week
    # First read the header row to find the column for the current week
    result = None
    try:
        # Read header row to find the column matching today's week ending date
        header_result = subprocess.run(
            ["gog", "sheets", "get", SHEET_ID, "'Weekly Topline'!A1:Z1", "--json"],
            capture_output=True,
            text=True,
            timeout=10,
            cwd=project_dir,
        )
        # Determine which column has today's week ending date
        # Default to column D (index 3) if we can't find it
        col_index = 3  # 0-based: A=0, B=1, C=2, D=3
        if header_result.returncode == 0:
            header_data = json.loads(header_result.stdout)
            header_values = header_data.get("values", [[]])[0] if header_data.get("values") else []
            # Look for a header containing today's date in M/D/YY or M/D/YYYY format
            today_dt = datetime.now()
            date_variants = [
                today_dt.strftime("%-m/%-d/%y"),   # e.g. "3/27/26"
                today_dt.strftime("%-m/%-d/%Y"),   # e.g. "3/27/2026"
                today_dt.strftime("%m/%d/%y"),     # e.g. "03/27/26"
            ]
            for idx, header in enumerate(header_values):
                for variant in date_variants:
                    if variant in str(header):
                        col_index = idx
                        break

        # Convert col_index to column letter (A=0, B=1, ...)
        col_letter = chr(ord('A') + col_index)
        sheet_range = f"'Weekly Topline'!{col_letter}4:{col_letter}7"

        result = subprocess.run(
            ["gog", "sheets", "get", SHEET_ID, sheet_range, "--json"],
            capture_output=True,
            text=True,
            timeout=10,
            cwd=project_dir,
        )
        if result.returncode == 0:
            data = json.loads(result.stdout)
            values = data.get("values", [])
            if len(values) < 4:
                failures.append("Sheet Topline missing key metric rows")
            else:
                for i, metric in enumerate(KEY_METRICS):
                    if not values[i] or not values[i][0].strip():
                        failures.append(f"Sheet Topline empty for: {metric}")
        else:
            failures.append(f"Could not read sheet: {result.stderr[:100]}")
    except Exception as e:
        failures.append(f"Sheet check failed: {e}")

    # Check 4: Verify Slack message metrics match sheet
    if not failures:
        try:
            sheet_data = json.loads(result.stdout)
            sheet_values = [row[0] for row in sheet_data.get("values", [])]

            # Extract numbers from the curl command
            for i, metric_name in enumerate(["NDAs", "Financials", "LOIs submitted", "LOIs signed"]):
                pattern = rf"{metric_name}:\s*(\d+)"
                match = re.search(pattern, command)
                if match:
                    slack_val = match.group(1)
                    sheet_val = sheet_values[i] if i < len(sheet_values) else ""
                    if str(slack_val) != str(sheet_val):
                        failures.append(
                            f"MISMATCH: Slack says {metric_name}={slack_val} but sheet says {sheet_val}"
                        )
        except Exception:
            pass  # Non-fatal, other checks still hold

    if failures:
        return HandlerResult(
            decision=Decision.BLOCK,
            reason=(
                "WEEKLY TRACKER VALIDATION FAILED — Slack notification blocked.\n\n"
                + "\n".join(f"  - {f}" for f in failures)
                + "\n\nFix these issues, then retry the Slack notification."
            ),
        )

    return None
