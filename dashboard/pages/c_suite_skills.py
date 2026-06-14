"""C-Suite & Skills page — scheduled-skill canary organized by C-suite agent.

Reads scheduled-job state (`systemd --user` timers on Linux/VPS;
`launchctl` + plist XML on macOS) and `logs/scheduled/*.log` to answer
the page's load-bearing question: did each scheduled skill fire this week?

All data is local — no external auth, no MCP — so this page is the lowest-
risk page in the dashboard build. The C-suite → skill mapping is hardcoded
in `data_sources._SKILL_CATALOG` (validated 2026-04-24); on-demand skills
appear with a dashed status dot and "On-demand" badge.

Health-monitor renders as a red Gap row when migration docs say it should
be Friday-scheduled but no plist is registered — surfacing that exact gap
visually is exactly the kind of silent-failure canary the page exists for.

Weekly Flow grid (added 2026-05-04): each day's tile carries a fired/missed
health indicator that PERSISTS through the rest of the week. Today's column
shows live status; past-day columns show that day's outcome (green ring =
fired ok, red dashed = missed, red ring = failed). The grid resets on
Sunday. The week's per-day status comes from `SkillHealth.week_status_by_day`
in `data_sources` — it scans logs from this week's Sunday through yesterday
and aggregates per scheduled fire-day.
"""

from __future__ import annotations

from datetime import date, datetime
from html import escape
from textwrap import dedent

import sys
from pathlib import Path

_DASHBOARD_DIR = Path(__file__).resolve().parent.parent
if str(_DASHBOARD_DIR) not in sys.path:
    sys.path.insert(0, str(_DASHBOARD_DIR))

from data_sources import (  # noqa: E402
    CSuiteGroup,
    SkillHealth,
    load_email_orchestrator_status,
    load_skill_health,
    skill_health_summary,
)


# Status → (dot CSS class, badge label, badge CSS class)
_STATUS_PRESENTATION = {
    "fired-ok": ("green", "Scheduled", "scheduled"),
    "fired-warn": ("yellow", "Scheduled", "scheduled"),
    "fired-err": ("red", "Scheduled", "scheduled"),
    "scheduled-later": ("grey", "Scheduled", "scheduled"),
    "missed": ("red", "Scheduled", "scheduled"),
    "ondemand": ("ondemand", "On-demand", "ondemand"),
    "gap": ("red", "Gap", "gap"),
}


def _last_run_text(skill: SkillHealth) -> tuple[str, str]:
    """Return (text, css class modifier — '', 'green', 'red', or 'dim')."""
    s = skill.today_status
    if s == "fired-ok":
        return f"Fired {skill.last_run.fired_at.strftime('%-I:%M %p')}", "green"
    if s == "fired-warn":
        return (
            f"Fired {skill.last_run.fired_at.strftime('%-I:%M %p')} · check log",
            "yellow",
        )
    if s == "fired-err":
        return (
            f"Failed {skill.last_run.fired_at.strftime('%-I:%M %p')}",
            "red",
        )
    if s == "missed":
        return "Missed today's window", "red"
    if s == "scheduled-later":
        return (skill.next_fire_text or "Next run pending"), "dim"
    if s == "gap":
        return "No scheduled job registered", "red"
    # On-demand
    if skill.last_run is None:
        return "Never run", "dim"
    delta = datetime.now() - skill.last_run.fired_at
    days = delta.days
    if days <= 0:
        hours = delta.seconds // 3600
        return f"Last run {hours}h ago", ""
    if days == 1:
        return "Last run yesterday", ""
    return f"Last run {days}d ago", ("dim" if days > 6 else "")


def _schedule_or_trigger(skill: SkillHealth) -> tuple[str, bool]:
    """Return (text, is_dim). Scheduled = not dim, on-demand = dim."""
    if skill.is_scheduled:
        return f"⏱ {skill.schedule_text}", False
    if skill.is_gap:
        return "Migration docs say scheduled · no job registered", True
    if skill.trigger_text:
        return skill.trigger_text, True
    return "On-demand", True


def _render_skill_row(skill: SkillHealth) -> str:
    dot_class, badge_label, badge_class = _STATUS_PRESENTATION.get(
        skill.today_status, ("grey", "Unknown", "ondemand")
    )
    schedule_text, schedule_dim = _schedule_or_trigger(skill)
    last_run_text, last_run_class = _last_run_text(skill)

    schedule_class = "gb-skill-schedule"
    if schedule_dim:
        schedule_class += " dim"

    last_run_class_full = "gb-skill-last-run"
    if last_run_class:
        last_run_class_full += f" {last_run_class}"

    return dedent(
        f"""
        <div class="gb-skill-row">
        <span class="gb-status-dot {dot_class}"></span>
        <div class="gb-skill-cell">
        <div class="gb-skill-name">{escape(skill.name)}</div>
        <div class="gb-skill-desc">{escape(skill.description)}</div>
        </div>
        <div class="{schedule_class}">{escape(schedule_text)}</div>
        <div class="{last_run_class_full}">{escape(last_run_text)}</div>
        <div class="gb-skill-badge {badge_class}">{escape(badge_label)}</div>
        </div>
        """
    ).strip()


def _render_group_header(group: CSuiteGroup) -> str:
    fired = sum(1 for s in group.skills if s.today_status.startswith("fired"))
    on_deck = sum(1 for s in group.skills if s.today_status == "scheduled-later")
    gaps = sum(1 for s in group.skills if s.today_status == "gap")
    issues = sum(1 for s in group.skills if s.today_status in ("missed", "fired-err", "gap"))

    pills = []
    if fired:
        pills.append(f'<span class="pill">{fired} fired</span>')
    if issues:
        pills.append(f'<span class="pill red">{issues} issues</span>')
    if on_deck:
        pills.append(f'<span class="pill neutral">{on_deck} on-deck</span>')
    if not pills:
        pills.append('<span class="pill neutral">on-demand only</span>')

    return dedent(
        f"""
        <div class="gb-csuite-head">
        <div class="gb-csuite-head-left">
        <div class="gb-csuite-label">{escape(group.label)}</div>
        <div class="gb-csuite-sublabel">{escape(group.short)}</div>
        </div>
        <div class="gb-csuite-meta">
        {len(group.skills)} skills
        {''.join(pills)}
        </div>
        </div>
        """
    ).strip()


def _render_gc_empty() -> str:
    return dedent(
        """
        <div class="gb-csuite-empty">
        No skills assigned yet.
        <span class="candidates">candidates: nda-review · loi-redline · compliance-hard-stop-check</span>
        </div>
        """
    ).strip()


def _render_group(group: CSuiteGroup) -> str:
    head = _render_group_header(group)
    if group.skills:
        body = "".join(_render_skill_row(s) for s in group.skills)
    else:
        body = _render_gc_empty()
    return f'<section class="gb-csuite">{head}{body}</section>'


# ---------------- Weekly Flow (top-of-page tile grid) ----------------

# ISO weekday: Mon=1..Sun=7. Sun-first calendar order:
_SUN_TO_SAT: list[tuple[int, str]] = [
    (7, "Sun"), (1, "Mon"), (2, "Tue"), (3, "Wed"),
    (4, "Thu"), (5, "Fri"), (6, "Sat"),
]

# Bookend-triggered work is not a timer, but it is expected when Kay runs
# /goodmorning or /goodnight. It gets its own calendar view and filter tab.
_BOOKEND_FLOW: dict[int, list[tuple[str, str]]] = {
    1: [
        ("email-intelligence", "good morning"),
        ("relationship-manager", "good morning"),
        ("pipeline-manager", "good morning"),
        ("task-tracker-manager", "good night"),
        ("decision-traces", "good night"),
    ],
    2: [
        ("email-intelligence", "good morning"),
        ("relationship-manager", "good morning"),
        ("pipeline-manager", "good morning"),
        ("task-tracker-manager", "good night"),
        ("decision-traces", "good night"),
    ],
    3: [
        ("email-intelligence", "good morning"),
        ("relationship-manager", "good morning"),
        ("pipeline-manager", "good morning"),
        ("task-tracker-manager", "good night"),
        ("decision-traces", "good night"),
    ],
    4: [
        ("email-intelligence", "good morning"),
        ("relationship-manager", "good morning"),
        ("pipeline-manager", "good morning"),
        ("task-tracker-manager", "good night"),
        ("decision-traces", "good night"),
    ],
    5: [
        ("email-intelligence", "good morning"),
        ("relationship-manager", "good morning"),
        ("pipeline-manager", "good morning"),
        ("weekly-tracker", "good morning"),
        ("health-monitor", "good morning"),
        ("calibration-workflow", "good morning"),
        ("task-tracker-manager", "good night"),
        ("decision-traces", "good night"),
    ],
    6: [],
    7: [
        ("email-intelligence", "good morning"),
        ("relationship-manager", "good morning"),
        ("pipeline-manager", "good morning"),
        ("task-tracker-manager", "good morning"),
        ("task-tracker-manager", "good night"),
        ("decision-traces", "good night"),
    ],
}
_BOOKEND_SKILLS = {name for items in _BOOKEND_FLOW.values() for name, _ in items}
_REPO_ROOT = _DASHBOARD_DIR.parent
_BRAIN_ROOT = _REPO_ROOT / "brain"


def _week_date_for_iso(day_iso: int) -> date:
    today = date.today()
    sunday = today if today.isoweekday() == 7 else today.fromordinal(today.toordinal() - today.isoweekday())
    # Sun-first calendar: Sunday is iso 7, Monday is iso 1.
    offset = 0 if day_iso == 7 else day_iso
    return sunday.fromordinal(sunday.toordinal() + offset)


def _bookend_artifact_exists(name: str, label: str, day_iso: int) -> bool:
    d = _week_date_for_iso(day_iso)
    ds = d.isoformat()
    checks = {
        "email-intelligence": [_BRAIN_ROOT / "context" / f"email-scan-results-{ds}.md"],
        "relationship-manager": [_BRAIN_ROOT / "context" / f"relationship-status-{ds}.md"],
        "weekly-tracker": [_BRAIN_ROOT / "trackers" / "weekly" / f"{ds}-weekly-tracker.md"],
        "health-monitor": [_BRAIN_ROOT / "trackers" / "health" / f"{ds}-health.md"],
        "calibration-workflow": [_BRAIN_ROOT / "outputs" / "calibrations" / f"{ds}-codex-calibration.md"],
        # Good Night always writes session-decisions; use that as the durable
        # proof for carry-forward + trace scan until bookend-run records exist.
        "decision-traces": [_BRAIN_ROOT / "context" / f"session-decisions-{ds}.md"],
        "task-tracker-manager": [_BRAIN_ROOT / "context" / f"session-decisions-{ds}.md"] if label == "good night" else [],
        # Pipeline-manager currently has no durable per-run artifact. Treat the
        # morning's two input artifacts as the best available proxy.
        "pipeline-manager": [
            _BRAIN_ROOT / "context" / f"email-scan-results-{ds}.md",
            _BRAIN_ROOT / "context" / f"relationship-status-{ds}.md",
        ],
    }
    paths = checks.get(name, [])
    if not paths:
        return False
    return all(path.exists() for path in paths)


def _fmt_time_short(h: int, m: int) -> str:
    period = "AM" if h < 12 else "PM"
    h12 = h % 12 or 12
    if m == 0:
        return f"{h12} {period}"
    return f"{h12}:{m:02d} {period}"


def _fmt_hour(h: int) -> str:
    period = "AM" if h < 12 else "PM"
    h12 = h % 12 or 12
    return f"{h12}{period}"


def _compact_time_label(times: list[tuple[int, int]]) -> str:
    """Compress (hour, minute) fires for ONE skill on ONE day into a label.

    Rules:
      - 1 fire → "6 AM"
      - 2-3 fires → "6 AM, 2 PM"
      - 4+ fires, all on the hour, contiguous → "Hourly 8AM-8PM"
      - otherwise → "{n}× daily"
    """
    if not times:
        return ""
    times = sorted(times)
    if len(times) == 1:
        return _fmt_time_short(*times[0])
    hours = [h for h, _ in times]
    minutes = {m for _, m in times}
    if (
        minutes == {0}
        and hours == list(range(min(hours), max(hours) + 1))
        and len(hours) >= 4
    ):
        return f"Hourly {_fmt_hour(min(hours))}-{_fmt_hour(max(hours))}"
    if len(times) <= 3:
        return ", ".join(_fmt_time_short(h, m) for h, m in times)
    return f"{len(times)}× daily"


def _expand_intervals(intervals: list[dict]) -> dict[int, list[tuple[int, int]]]:
    """Return {iso_weekday: [(hour, minute), ...]} for one skill's plist."""
    by_day: dict[int, list[tuple[int, int]]] = {}
    for d in intervals:
        h = d.get("Hour", 0)
        m = d.get("Minute", 0)
        wd = d.get("Weekday")
        if wd is None:
            for day in range(1, 8):
                by_day.setdefault(day, []).append((h, m))
        else:
            wd_norm = 7 if wd == 0 else wd
            by_day.setdefault(wd_norm, []).append((h, m))
    return {d: sorted(t) for d, t in by_day.items() if t}


def _warning_days_for_skill(skill_status: str, week_status: dict[int, str]) -> int:
    warning_days = sum(1 for s in week_status.values() if s == "fired-warn")
    if skill_status == "fired-warn":
        warning_days += 1
    return warning_days


def _escalated_warning_day(skill_status: str, week_status: dict[int, str]) -> int | None:
    warning_days = [day for day, s in week_status.items() if s == "fired-warn"]
    if skill_status == "fired-warn":
        warning_days.append(datetime.now().isoweekday())
    if len(warning_days) <= 3:
        return None
    return max(warning_days, key=lambda day: 0 if day == 7 else day)


def _bookend_is_due(label: str, day_class: str) -> bool:
    if day_class == "past":
        return True
    if day_class != "today":
        return False
    now = datetime.now()
    if label == "good morning":
        return (now.hour, now.minute) >= (10, 0)
    if label == "good night":
        return (now.hour, now.minute) >= (20, 0)
    return True


def _build_weekly_flow(groups: list[CSuiteGroup], view: str = "Scheduled") -> dict[int, list[dict]]:
    """Return {iso_weekday: [{name, time_label, today_status, sort_minutes, day_count}, ...]}.

    Tiles within each day are sorted by frequency band first (everyday -> most-
    days -> day-unique), then by first-fire time, then by name. Frequency is the
    raw day_count across the 7-day week, sorted descending: a 7-day skill
    floats to the top of every column, a 5-day Mon-Fri skill sits in the middle,
    a 1-day skill drops to the bottom.
    """
    # First pass: count how many days each skill fires across the week.
    day_count: dict[str, int] = {}
    skill_intervals: dict[str, dict[int, list[tuple[int, int]]]] = {}
    skill_status: dict[str, str] = {}
    skill_week_status: dict[str, dict[int, str]] = {}
    skill_escalated_warning: dict[str, int | None] = {}
    for group in groups:
        for skill in group.skills:
            if not skill.is_scheduled or not skill.intervals:
                continue
            by_day = _expand_intervals(skill.intervals)
            day_count[skill.name] = len(by_day)
            skill_intervals[skill.name] = by_day
            skill_status[skill.name] = skill.today_status
            skill_week_status[skill.name] = skill.week_status_by_day
            skill_escalated_warning[skill.name] = _escalated_warning_day(
                skill.today_status, skill.week_status_by_day
            )

    flow: dict[int, list[dict]] = {d: [] for d in range(1, 8)}
    if view in ("Scheduled", "All", "Issues only"):
        for name, by_day in skill_intervals.items():
            for day, times in by_day.items():
                day_status = skill_week_status[name].get(day, "")
                escalated_warning_day = skill_escalated_warning.get(name)
                issue_on_this_day = day_status in ("missed", "fired-err") or (
                    day == datetime.now().isoweekday() and skill_status[name] in ("missed", "fired-err")
                )
                if escalated_warning_day == day:
                    issue_on_this_day = True
                if view == "Issues only" and not issue_on_this_day:
                    continue
                flow[day].append({
                    "name": name,
                    "time_label": _compact_time_label(times),
                    "today_status": skill_status[name],
                    "day_status": day_status,
                    "sort_minutes": times[0][0] * 60 + times[0][1],
                    "day_count": day_count[name],
                    "kind": "scheduled",
                    "escalated_warning_day": escalated_warning_day,
                })
    if view in ("Bookend-triggered", "All"):
        for day, items in _BOOKEND_FLOW.items():
            for name, label in items:
                flow[day].append({
                    "name": name,
                    "time_label": label,
                    "today_status": "workflow",
                    "day_status": "workflow",
                    "sort_minutes": (8 if label == "good morning" else 18) * 60,
                    "day_count": 7 if name in {"pipeline-manager", "email-intelligence", "relationship-manager", "task-tracker-manager", "decision-traces"} else 1,
                    "kind": "workflow",
                })
    # Sort: descending day_count (everyday first), then ascending time, then name.
    for day in flow:
        flow[day].sort(key=lambda t: (-t["day_count"], t["sort_minutes"], t["name"]))
    return flow


def _render_weekly_flow(groups: list[CSuiteGroup], view: str = "Scheduled") -> str:
    flow = _build_weekly_flow(groups, view)
    today_iso = datetime.now().isoweekday()

    # Skip Saturday only if zero scheduled skills fire on Sat.
    week = list(_SUN_TO_SAT)
    if not flow.get(6):
        week = [(d, n) for d, n in week if d != 6]

    today_idx = next((i for i, (d, _) in enumerate(week) if d == today_iso), None)

    cols: list[str] = []
    for i, (day_iso, day_name) in enumerate(week):
        tiles = flow.get(day_iso, [])
        if today_idx is None:
            day_class = "future"
        elif i < today_idx:
            day_class = "past"
        elif i == today_idx:
            day_class = "today"
        else:
            day_class = "future"

        tile_html: list[str] = []
        for tile in tiles:
            cls_extra = ""
            if tile.get("kind") == "workflow" and _bookend_is_due(tile["time_label"], day_class):
                cls_extra = " fired-ok" if _bookend_artifact_exists(
                    tile["name"], tile["time_label"], day_iso
                ) else " missed"
            elif tile.get("kind") != "workflow" and day_class == "today":
                s = tile["today_status"]
                if tile.get("escalated_warning_day") == day_iso and s == "fired-warn":
                    cls_extra = " missed"
                elif s in ("fired-ok", "fired-warn"):
                    cls_extra = " fired-ok"
                elif s in ("fired-err", "missed"):
                    cls_extra = f" {s}"
            elif tile.get("kind") != "workflow" and day_class == "past":
                s = tile.get("day_status", "")
                if tile.get("escalated_warning_day") == day_iso and s == "fired-warn":
                    cls_extra = " missed"
                elif s in ("fired-ok", "fired-warn"):
                    cls_extra = " fired-ok"
                elif s in ("fired-err", "missed"):
                    cls_extra = f" {s}"
            tile_html.append(
                f'<div class="gb-flow-tile{cls_extra}">'
                f'<div class="gb-flow-tile-name">{escape(tile["name"])}</div>'
                f'<div class="gb-flow-tile-time">{escape(tile["time_label"])}</div>'
                f'</div>'
            )
        body = "".join(tile_html) if tile_html else '<div class="gb-flow-day-empty">—</div>'
        cols.append(
            f'<div class="gb-flow-day {day_class}">'
            f'<div class="gb-flow-day-head">'
            f'<span class="gb-flow-day-name">{day_name}</span>'
            f'<span class="gb-flow-day-count">{len(tiles)}</span>'
            f'</div>'
            f'{body}'
            f'</div>'
        )

    return (
        '<section class="gb-weekly-flow">'
        '<div class="gb-weekly-flow-head">'
        '<span class="gb-weekly-flow-label">WEEKLY FLOW</span>'
        '<span class="gb-weekly-flow-sub">scheduled skills by day · today highlighted</span>'
        '</div>'
        f'<div class="gb-weekly-flow-grid">{"".join(cols)}</div>'
        '</section>'
    )


def _render_subtitle() -> str:
    return dedent(
        """
        <div class="gb-subtitle">
        Scheduled-skill canary organized by C-suite agent.
        </div>
        """
    ).strip()


def _render_legend() -> str:
    return dedent(
        """
        <div class="gb-flow-legend">
        <span class="gb-flow-legend-pill fired-ok">fired on schedule</span>
        <span class="gb-flow-legend-pill missed">skill issue</span>
        </div>
        """
    ).strip()


def _bookend_counts_for_day(day_iso: int, day_class: str) -> dict[str, int]:
    counts = {"total": 0, "fired": 0, "issues": 0, "remaining": 0}
    for name, label in _BOOKEND_FLOW.get(day_iso, []):
        counts["total"] += 1
        if _bookend_artifact_exists(name, label, day_iso):
            counts["fired"] += 1
        elif _bookend_is_due(label, day_class):
            counts["issues"] += 1
        else:
            counts["remaining"] += 1
    return counts


def _bookend_summary() -> dict[str, int]:
    today_iso = datetime.now().isoweekday()
    week = list(_SUN_TO_SAT)
    today_idx = next((i for i, (d, _) in enumerate(week) if d == today_iso), None)

    today_counts = {"total": 0, "fired": 0, "issues": 0, "remaining": 0}
    weekly_counts = {"total": 0, "fired": 0, "issues": 0, "remaining": 0}
    for i, (day_iso, _) in enumerate(week):
        if today_idx is None:
            day_class = "future"
        elif i < today_idx:
            day_class = "past"
        elif i == today_idx:
            day_class = "today"
        else:
            day_class = "future"
        day_counts = _bookend_counts_for_day(day_iso, day_class)
        for key, value in day_counts.items():
            weekly_counts[key] += value
        if day_iso == today_iso:
            today_counts = day_counts

    return {
        "daily_total": today_counts["total"],
        "daily_fired": today_counts["fired"],
        "daily_issues": today_counts["issues"],
        "daily_remaining": today_counts["remaining"],
        "weekly_total": weekly_counts["total"],
        "weekly_fired": weekly_counts["fired"],
        "weekly_issues": weekly_counts["issues"],
        "weekly_remaining": weekly_counts["remaining"],
    }


def _render_summary(summary: dict[str, int]) -> str:
    """Three operating rows: scheduled, bookend-triggered, and on-demand."""
    daily_issue = summary["daily_issue"] + summary["gaps"]
    weekly_issues = summary["weekly_issues"] + summary["gaps"]
    bookend = _bookend_summary()
    rows = [
        (
            '<span class="gb-summary-label">Scheduled</span>'
            f'<span><span class="num">{summary["daily_total"]}</span>skills today</span>'
            f'<span><span class="num" style="color:var(--green);">{summary["daily_completed"]}</span>fired</span>'
            f'<span><span class="num" style="color:var(--red);">{daily_issue}</span>issues</span>'
            f'<span><span class="num">{summary["daily_remaining"]}</span>remaining</span>'
            f'<span><span class="num">{summary["weekly_expected"]}</span>skills weekly</span>'
            f'<span><span class="num" style="color:var(--green);">{summary["weekly_completed"]}</span>fired</span>'
            f'<span><span class="num" style="color:var(--red);">{weekly_issues}</span>issues</span>'
            f'<span><span class="num">{summary["weekly_remaining"]}</span>remaining</span>'
        ),
        (
            '<span class="gb-summary-label">Bookend-triggered</span>'
            f'<span><span class="num">{bookend["daily_total"]}</span>skills today</span>'
            f'<span><span class="num" style="color:var(--green);">{bookend["daily_fired"]}</span>fired</span>'
            f'<span><span class="num" style="color:var(--red);">{bookend["daily_issues"]}</span>issues</span>'
            f'<span><span class="num">{bookend["daily_remaining"]}</span>remaining</span>'
            f'<span><span class="num">{bookend["weekly_total"]}</span>skills weekly</span>'
            f'<span><span class="num" style="color:var(--green);">{bookend["weekly_fired"]}</span>fired</span>'
            f'<span><span class="num" style="color:var(--red);">{bookend["weekly_issues"]}</span>issues</span>'
            f'<span><span class="num">{bookend["weekly_remaining"]}</span>remaining</span>'
        ),
        (
            '<span class="gb-summary-label">On-demand</span>'
            f'<span><span class="num">{summary["ondemand"]}</span>skills</span>'
        ),
    ]
    return '<div class="gb-summary gb-summary-rows">' + ''.join(
        f'<div class="gb-summary-row">{row}</div>' for row in rows
    ) + '</div>'


def _render_email_orchestration_panel() -> str:
    """Render the email routing surface without exposing raw email content."""
    email = load_email_orchestrator_status()
    status_label = {
        "ok": "Ready",
        "warn": "Needs review",
        "alert": "Blocked",
    }.get(email.status, "Unknown")
    status_class = {
        "ok": "green",
        "warn": "yellow",
        "alert": "red",
    }.get(email.status, "grey")
    fetched = email.fetched_at or "not fetched"
    source = email.source_artifact or "no source artifact"
    review_items = email.review_count

    needs = email.needs_kay[:3]
    blocked = email.blocked[:3]
    queue_rows = []
    for label, items, css in (
        ("Needs Kay", needs, "yellow"),
        ("Blocked", blocked, "red"),
    ):
        if items:
            body = "".join(f"<li>{escape(item)}</li>" for item in items)
        else:
            body = "<li>None</li>"
            css = "green"
        queue_rows.append(
            f'<div class="gb-email-queue"><div class="gb-source-group-title">'
            f'<span class="gb-status-dot {css}"></span>{label}</div><ul>{body}</ul></div>'
        )

    return dedent(
        f"""
        <div class="gb-zone gb-zone-plain">
          <div class="gb-zone-head">
            <div>
              <div class="gb-zone-label">Email Orchestration</div>
              <div class="gb-zone-subtitle">Routes email-derived signals into deal flow, relationships, tasks, and Good Morning without sending email</div>
            </div>
            <div class="gb-zone-meta"><span class="gb-status-dot {status_class}"></span>{escape(status_label)}</div>
          </div>
          <div class="gb-deal-status-grid">
            <div><span class="num">{escape(email.source_status)}</span>source</div>
            <div><span class="num">{email.drafts_pending}</span>drafts pending</div>
            <div><span class="num {'red' if email.send_blockers else 'dim'}">{email.send_blockers}</span>send blockers</div>
            <div><span class="num">{email.deal_items}</span>deal items</div>
            <div><span class="num">{email.pipeline_items}</span>pipeline items</div>
            <div><span class="num">{email.relationship_items}</span>relationship items</div>
            <div><span class="num">{email.task_candidates}</span>task candidates</div>
            <div><span class="num {'yellow' if review_items else 'green'}">{review_items}</span>review items</div>
          </div>
          <div class="gb-source-detail" style="margin: 10px 0 14px;">Source: {escape(source)} · fetched {escape(fetched)}</div>
          <div class="gb-email-queues">{''.join(queue_rows)}</div>
        </div>
        """
    ).strip()


# Visual stubs only — pill row is interactive via st.segmented_control
# in render(); dropdowns + search render but don't mutate state.
def _render_filter_bar_stubs() -> str:
    return dedent(
        """
        <div class="gb-filter-bar" style="border-bottom: none; padding-bottom: 0; margin-bottom: 16px;">
        <select class="gb-filter-select"><option>All C-suites</option></select>
        <select class="gb-filter-select"><option>All statuses</option></select>
        <input class="gb-filter-search" type="text" placeholder="Search skill..." />
        </div>
        """
    ).strip()


def _filter_groups_by_pill(groups: list[CSuiteGroup], pill: str) -> list[CSuiteGroup]:
    """Filter each group's skills based on the selected pill. Returns new
    CSuiteGroup objects (not mutating the input). Empty groups stay so the
    C-suite header still renders even when filtered to zero skills."""
    if pill in (None, "All"):
        return groups
    out: list[CSuiteGroup] = []
    for g in groups:
        if pill == "Scheduled":
            kept = [s for s in g.skills if s.is_scheduled and not s.is_gap]
        elif pill == "On-demand":
            kept = [s for s in g.skills if not s.is_scheduled and not s.is_gap and s.name not in _BOOKEND_SKILLS]
        elif pill == "Bookend-triggered":
            kept = [s for s in g.skills if s.name in _BOOKEND_SKILLS]
        elif pill == "Issues only":
            kept = [s for s in g.skills if s.is_gap or s.today_status in ("missed", "fired-err")]
        else:
            kept = list(g.skills)
        out.append(CSuiteGroup(short=g.short, label=g.label, skills=kept))
    return out


def render() -> None:
    import streamlit as st

    groups = load_skill_health()
    summary = skill_health_summary(groups)

    st.markdown(_render_subtitle(), unsafe_allow_html=True)
    st.markdown(_render_legend(), unsafe_allow_html=True)
    st.markdown(_render_summary(summary), unsafe_allow_html=True)
    st.markdown(_render_email_orchestration_panel(), unsafe_allow_html=True)

    current_view = st.session_state.get("csuite_filter", "Scheduled")
    st.markdown(_render_weekly_flow(groups, current_view), unsafe_allow_html=True)

    pill = st.segmented_control(
        "Skill filter",
        options=["Scheduled", "Bookend-triggered", "Issues only", "On-demand"],
        default="Scheduled",
        key="csuite_filter",
        label_visibility="collapsed",
    ) or "Scheduled"
    filtered = _filter_groups_by_pill(groups, pill)

    st.markdown(_render_filter_bar_stubs(), unsafe_allow_html=True)
    sections = "".join(_render_group(g) for g in filtered)
    st.markdown(sections, unsafe_allow_html=True)

    st.markdown(
        '<div class="gb-page-note">Reads scheduled-job state '
        "(<code>systemd --user</code> timers on this host; "
        "<code>launchctl</code> + plist on macOS) and "
        "<code>logs/scheduled/*.log</code>. Source / status dropdowns + "
        "search are visual stubs pending interactive build. C-suite → "
        "skill mapping validated 2026-04-24."
        "</div>",
        unsafe_allow_html=True,
    )
