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
    parts = [
        f'<div><span class="num">{summary["total"]}</span>skills</div>',
        f'<div><span class="num green">{summary["fired_today"]}</span>fired today</div>',
        f'<div><span class="num">{summary["on_deck"]}</span>scheduled later this week</div>',
    ]
    if summary["missed"]:
        parts.append(
            f'<div><span class="num red">{summary["missed"]}</span>missed today\'s window</div>'
        )
    if summary["gaps"]:
        parts.append(
            f'<div><span class="num red">{summary["gaps"]}</span>scheduling gap</div>'
        )
    parts.append(f'<div><span class="num">{summary["ondemand"]}</span>on-demand</div>')
    return f'<div class="gb-summary">{"".join(parts)}</div>'


def render() -> None:
    import streamlit as st

    groups = load_skill_health()
    summary = skill_health_summary(groups)

    st.markdown(_render_subtitle(), unsafe_allow_html=True)
    st.markdown(_render_summary(summary), unsafe_allow_html=True)

    sections = "".join(_render_group(g) for g in groups)
    st.markdown(sections, unsafe_allow_html=True)

    st.markdown(
        '<div class="gb-page-note">Reads <code>launchctl list</code>, '
        "<code>~/Library/LaunchAgents/com.greenwich-barrow.*.plist</code>, "
        "and <code>logs/scheduled/*.log</code>. C-suite → skill mapping "
        "validated 2026-04-24."
        "</div>",
        unsafe_allow_html=True,
    )
