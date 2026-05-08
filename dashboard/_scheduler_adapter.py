"""Scheduler abstraction layer — macOS launchd vs Linux systemd.

Phase 3 of Linux migration (2026-05-07). Lets dashboard pages render the
same scheduler-introspection data on both platforms without forking
display code.

Strategy: return plist-shaped dicts on both platforms. macOS reads the
real plist; Linux reads the systemd `.timer` unit file and synthesizes a
matching `StartCalendarInterval` list from `OnCalendar` lines. Downstream
code in `dashboard/data_sources.py` consumes the dict the same way on
either backend.

Coverage:
- registered_jobs() — returns set of skill names that have a registered job
- read_job_config(skill) — returns plist-shaped dict, or None if not registered

Exclusions: Linux backend does not support `WatchPaths`-driven jobs (e.g.,
post-call-analyzer). Those stay on macOS as the Granola sidecar.
"""

from __future__ import annotations

import platform
import plistlib
import subprocess
from pathlib import Path

LAUNCHD_LABEL_PREFIX = "com.greenwich-barrow."
LAUNCH_AGENTS_DIR = Path.home() / "Library" / "LaunchAgents"
SYSTEMD_USER_DIR = Path.home() / ".config" / "systemd" / "user"

IS_MACOS = platform.system() == "Darwin"
IS_LINUX = platform.system() == "Linux"


# ─── Public API ──────────────────────────────────────────────────────────


def registered_jobs() -> set[str]:
    """Return set of skill names with a registered scheduler job on this host."""
    if IS_MACOS:
        return _launchd_registered_jobs()
    if IS_LINUX:
        return _systemd_registered_jobs()
    return set()


def read_job_config(skill: str) -> dict | None:
    """Return plist-shaped dict for the named skill, or None if not present.

    On macOS: reads `~/Library/LaunchAgents/com.greenwich-barrow.<skill>.plist`.
    On Linux: parses `~/.config/systemd/user/<skill>.timer` and synthesizes
    a dict with `Label` and `StartCalendarInterval` keys.
    """
    if IS_MACOS:
        return _launchd_plist(skill)
    if IS_LINUX:
        return _systemd_synthesize(skill)
    return None


# ─── macOS backend (launchd) ─────────────────────────────────────────────


def _launchd_registered_jobs() -> set[str]:
    try:
        out = subprocess.run(
            ["launchctl", "list"],
            capture_output=True,
            text=True,
            timeout=5,
        )
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return set()
    if out.returncode != 0:
        return set()
    names: set[str] = set()
    for line in out.stdout.splitlines():
        parts = line.split()
        if len(parts) < 3:
            continue
        label = parts[-1]
        if label.startswith(LAUNCHD_LABEL_PREFIX):
            names.add(label[len(LAUNCHD_LABEL_PREFIX):])
    return names


def _launchd_plist(skill: str) -> dict | None:
    path = LAUNCH_AGENTS_DIR / f"{LAUNCHD_LABEL_PREFIX}{skill}.plist"
    if not path.exists():
        return None
    try:
        with path.open("rb") as f:
            return plistlib.load(f)
    except (OSError, plistlib.InvalidFileException):
        return None


# ─── Linux backend (systemd user timers) ─────────────────────────────────


def _systemd_registered_jobs() -> set[str]:
    try:
        out = subprocess.run(
            [
                "systemctl",
                "--user",
                "list-unit-files",
                "--type=timer",
                "--no-legend",
                "--no-pager",
            ],
            capture_output=True,
            text=True,
            timeout=5,
        )
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return set()
    if out.returncode != 0:
        return set()
    names: set[str] = set()
    for line in out.stdout.splitlines():
        parts = line.split()
        if not parts:
            continue
        unit = parts[0]
        if unit.endswith(".timer"):
            names.add(unit[: -len(".timer")])
    return names


def _systemd_synthesize(skill: str) -> dict | None:
    timer_path = SYSTEMD_USER_DIR / f"{skill}.timer"
    if not timer_path.exists():
        return None
    intervals: list[dict] = []
    try:
        body = timer_path.read_text()
    except OSError:
        return None
    for line in body.splitlines():
        stripped = line.strip()
        if not stripped.startswith("OnCalendar="):
            continue
        spec = stripped.split("=", 1)[1].strip()
        intervals.extend(_parse_oncalendar(spec))
    if not intervals:
        return None
    return {
        "Label": f"{LAUNCHD_LABEL_PREFIX}{skill}",
        "StartCalendarInterval": intervals,
    }


# launchd Weekday integers: 0=Sun, 1=Mon, 2=Tue, 3=Wed, 4=Thu, 5=Fri, 6=Sat
_DAY_NAME_TO_NUM = {
    "Sun": 0, "Mon": 1, "Tue": 2, "Wed": 3, "Thu": 4, "Fri": 5, "Sat": 6,
}


def _parse_oncalendar(spec: str) -> list[dict]:
    """Parse a systemd OnCalendar value into launchd-shaped interval dicts.

    Handles the patterns the generator emits:
    - `Mon..Fri 06:00:00` (range)
    - `Sun 21:00:00` (single day)
    - `Mon,Wed,Fri 12:00:00` (comma list)
    - `*-*-* 23:30:00` (every day)

    Returns [] for unrecognized formats — caller treats as "Multi-cadence"
    or "—" via existing fallback paths in data_sources.py._format_schedule.
    """
    parts = spec.split()
    if len(parts) < 2:
        return []

    day_part = parts[0]
    time_part = parts[-1]

    time_segments = time_part.split(":")
    if len(time_segments) < 2:
        return []
    try:
        hour = int(time_segments[0])
        minute = int(time_segments[1])
    except ValueError:
        return []

    if day_part in ("*-*-*", "*"):
        weekdays = list(range(7))
    elif ".." in day_part:
        try:
            start, end = day_part.split("..")
            start_n = _DAY_NAME_TO_NUM[start]
            end_n = _DAY_NAME_TO_NUM[end]
            if start_n <= end_n:
                weekdays = list(range(start_n, end_n + 1))
            else:
                weekdays = list(range(start_n, 7)) + list(range(0, end_n + 1))
        except (KeyError, ValueError):
            return []
    elif "," in day_part:
        try:
            weekdays = [_DAY_NAME_TO_NUM[d] for d in day_part.split(",")]
        except KeyError:
            return []
    elif day_part in _DAY_NAME_TO_NUM:
        weekdays = [_DAY_NAME_TO_NUM[day_part]]
    else:
        return []

    return [{"Weekday": w, "Hour": hour, "Minute": minute} for w in weekdays]
