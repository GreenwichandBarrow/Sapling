"""C-Suite & Skills page — scheduled-skill canary organized by C-suite agent.

Reads `launchctl list`, plist XML, and `logs/scheduled/*.log` to answer
the page's load-bearing question: did each scheduled skill fire today?

All data is local — no external auth, no MCP — so this page is the lowest-
risk page in the dashboard build. The C-suite → skill mapping is hardcoded
in `data_sources._SKILL_CATALOG` (validated 2026-04-24); on-demand skills
appear with a dashed status dot and "On-demand" badge.

Health-monitor renders as a red Gap row because CLAUDE.md says it should
be Friday-scheduled but no plist is registered — surfacing that exact gap
visually is exactly the kind of silent-failure canary the page exists for.
"""

from __future__ import annotations

from datetime import datetime
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
        return "No plist registered", "red"
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
        return "CLAUDE.md says scheduled · no plist", True
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
    missed = sum(1 for s in group.skills if s.today_status == "missed")

    pills = []
    if fired:
        pills.append(f'<span class="pill">{fired} fired</span>')
    if missed:
        pills.append(f'<span class="pill red">{missed} missed</span>')
    if gaps:
        pills.append(f'<span class="pill red">{gaps} gap</span>')
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


def _build_weekly_flow(groups: list[CSuiteGroup]) -> dict[int, list[dict]]:
    """Return {iso_weekday: [{name, time_label, today_status, sort_minutes, day_count}, ...]}.

    Tiles within each day are sorted by frequency band first (everyday → most-
    days → day-unique), then by first-fire time, then by name. Frequency is the
    raw day_count across the 7-day week, sorted descending — a 7-day skill
    floats to the top of every column, a 5-day Mon-Fri skill sits in the middle,
    a 1-day skill drops to the bottom.
    """
    # First pass: count how many days each skill fires across the week.
    day_count: dict[str, int] = {}
    skill_intervals: dict[str, dict[int, list[tuple[int, int]]]] = {}
    skill_status: dict[str, str] = {}
    for group in groups:
        for skill in group.skills:
            if not skill.is_scheduled or not skill.intervals:
                continue
            by_day = _expand_intervals(skill.intervals)
            day_count[skill.name] = len(by_day)
            skill_intervals[skill.name] = by_day
            skill_status[skill.name] = skill.today_status

    flow: dict[int, list[dict]] = {d: [] for d in range(1, 8)}
    for name, by_day in skill_intervals.items():
        for day, times in by_day.items():
            flow[day].append({
                "name": name,
                "time_label": _compact_time_label(times),
                "today_status": skill_status[name],
                "sort_minutes": times[0][0] * 60 + times[0][1],
                "day_count": day_count[name],
            })
    # Sort: descending day_count (everyday first), then ascending time, then name.
    for day in flow:
        flow[day].sort(key=lambda t: (-t["day_count"], t["sort_minutes"], t["name"]))
    return flow


def _render_weekly_flow(groups: list[CSuiteGroup]) -> str:
    flow = _build_weekly_flow(groups)
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
            if day_class == "today":
                s = tile["today_status"]
                if s in ("fired-ok", "fired-warn", "fired-err", "missed"):
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
        <span class="highlight">Green = fired today · red = should have fired but didn't · grey = scheduled later · dashed = on-demand.</span>
        </div>
        """
    ).strip()


def _render_summary(summary: dict[str, int]) -> str:
    """Match mockup-c-suite-skills.html: always show the 5 pills (skills,
    fired today, scheduled later, scheduling gap, on-demand) so the strip
    layout is stable even on weekends. Color the number pills directly:
    green for fired, red for gap/missed when >0, dim when 0."""
    fired = summary["fired_today"]
    gaps = summary["gaps"]
    missed = summary["missed"]
    fired_color = "var(--green)" if fired else "var(--text-dim)"
    gap_color = "var(--red)" if gaps else "var(--text-dim)"

    parts = [
        f'<div><span class="num">{summary["total"]}</span>skills</div>',
        f'<div><span class="num" style="color:{fired_color};">{fired}</span>fired today</div>',
        f'<div><span class="num">{summary["on_deck"]}</span>scheduled later this week</div>',
        f'<div><span class="num" style="color:{gap_color};">{gaps}</span>scheduling gap</div>',
    ]
    if missed:
        parts.append(
            f'<div><span class="num" style="color:var(--red);">{missed}</span>missed today\'s window</div>'
        )
    parts.append(f'<div><span class="num">{summary["ondemand"]}</span>on-demand</div>')
    return f'<div class="gb-summary">{"".join(parts)}</div>'


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
            kept = [s for s in g.skills if not s.is_scheduled and not s.is_gap]
        elif pill == "Gaps only":
            kept = [s for s in g.skills if s.is_gap or s.today_status == "missed"]
        else:
            kept = list(g.skills)
        out.append(CSuiteGroup(short=g.short, label=g.label, skills=kept))
    return out


def render() -> None:
    import streamlit as st

    groups = load_skill_health()
    summary = skill_health_summary(groups)

    st.markdown(_render_subtitle(), unsafe_allow_html=True)
    st.markdown(_render_summary(summary), unsafe_allow_html=True)
    st.markdown(_render_weekly_flow(groups), unsafe_allow_html=True)

    pill = st.segmented_control(
        "Skill filter",
        options=["All", "Scheduled", "On-demand", "Gaps only"],
        default="All",
        key="csuite_filter",
        label_visibility="collapsed",
    ) or "All"
    filtered = _filter_groups_by_pill(groups, pill)

    st.markdown(_render_filter_bar_stubs(), unsafe_allow_html=True)
    sections = "".join(_render_group(g) for g in filtered)
    st.markdown(sections, unsafe_allow_html=True)

    st.markdown(
        '<div class="gb-page-note">Reads <code>launchctl list</code>, '
        "<code>~/Library/LaunchAgents/com.greenwich-barrow.*.plist</code>, "
        "and <code>logs/scheduled/*.log</code>. C-suite → skill mapping "
        "validated 2026-04-24."
        "</div>",
        unsafe_allow_html=True,
    )
