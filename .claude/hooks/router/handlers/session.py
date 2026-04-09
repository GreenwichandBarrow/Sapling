"""Session handlers: init, daily note, dedup cleanup."""

import os
import subprocess
import sys
from pathlib import Path

from ..models import HandlerResult


def session_init(input_data: dict) -> HandlerResult:
    """SessionStart: run session-init.sh (sets env, creates daily note)."""
    project_dir = os.environ.get("CLAUDE_PROJECT_DIR", os.getcwd())
    script_path = os.path.join(project_dir, ".claude", "hooks", "session-init.sh")

    if not os.path.exists(script_path):
        return None

    try:
        result = subprocess.run(
            ["bash", script_path],
            capture_output=True,
            text=True,
            timeout=10,
            cwd=project_dir,
            env={**os.environ, "CLAUDE_PROJECT_DIR": project_dir},
        )

        out = HandlerResult()
        if result.stdout.strip():
            out.additional_context = result.stdout.strip()
        if result.stderr.strip():
            out.stderr_message = result.stderr.strip()
        return out

    except subprocess.TimeoutExpired:
        return HandlerResult(stderr_message="[session] session-init.sh timed out")
    except Exception as e:
        return HandlerResult(stderr_message=f"[session] session-init.sh error: {e}")


def calendar_check(input_data: dict) -> HandlerResult:
    """SessionStart: fetch today's + tomorrow's calendar and inject as context."""
    import shutil
    from datetime import datetime, timedelta

    if not shutil.which("gog"):
        return HandlerResult(stderr_message="[session] gog not found, skipping calendar check")

    today = datetime.now()
    tomorrow = today + timedelta(days=1)
    today_str = today.strftime("%Y-%m-%d")
    tomorrow_str = tomorrow.strftime("%Y-%m-%d")
    today_day = today.strftime("%A")
    tomorrow_day = tomorrow.strftime("%A")

    account = os.environ.get("GOG_ACCOUNT", "kay.s@greenwichandbarrow.com")
    lines = [f"📅 Calendar — {today_day}, {today.strftime('%B %d, %Y')}"]

    for label, date_str, day_name in [
        ("Today", today_str, today_day),
        ("Tomorrow", tomorrow_str, tomorrow_day),
    ]:
        try:
            result = subprocess.run(
                ["gog", "cal", "list", "--from", date_str, "--to", date_str,
                 "-a", account, "-p"],
                capture_output=True, text=True, timeout=10,
            )
            output = result.stdout.strip()
            # Skip header line (ID\tSTART\tEND\tSUMMARY)
            events = [l for l in output.split("\n")[1:] if l.strip()]
            if events:
                lines.append(f"\n{label} ({day_name} {date_str}):")
                for ev in events:
                    parts = ev.split("\t")
                    if len(parts) >= 4:
                        start = parts[1]
                        summary = parts[3]
                        # Extract time from ISO format
                        try:
                            t = datetime.fromisoformat(start)
                            time_str = t.strftime("%-I:%M%p").lower()
                        except (ValueError, IndexError):
                            time_str = start
                        lines.append(f"  • {time_str} — {summary}")
                    else:
                        lines.append(f"  • {ev}")
            else:
                lines.append(f"\n{label} ({day_name} {date_str}): No events")
        except subprocess.TimeoutExpired:
            lines.append(f"\n{label}: (calendar fetch timed out)")
        except Exception as e:
            lines.append(f"\n{label}: (calendar error: {e})")

    return HandlerResult(additional_context="\n".join(lines))


def dedup_cleanup(input_data: dict) -> HandlerResult:
    """SessionStart[startup]: clean up memory dedup state files."""
    project_dir = os.environ.get("CLAUDE_PROJECT_DIR", os.getcwd())
    dedup_dir = Path(project_dir) / ".claude" / "state" / "memory-dedup"

    if dedup_dir.exists():
        for log_file in dedup_dir.glob("*.log"):
            try:
                log_file.unlink()
            except Exception:
                pass

    return None
