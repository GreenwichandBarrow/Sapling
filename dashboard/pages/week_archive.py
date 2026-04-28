"""Week Archive page — historical weekly view, frozen in time.

Renders the same metric language as M&A Analytics for any prior week-ending
date, sourced from `dashboard.snapshot.snapshot_weekly()`. The dashboard is
the live working surface; this page is the time-machine for capturing
end-of-week views into the G&B Weekly Activity Tracker sheet.
"""

from __future__ import annotations

import re
from datetime import date, timedelta
from html import escape
from pathlib import Path

import sys

_DASHBOARD_DIR = Path(__file__).resolve().parent.parent
if str(_DASHBOARD_DIR) not in sys.path:
    sys.path.insert(0, str(_DASHBOARD_DIR))

from data_sources import WEEKLY_TRACKERS_DIR  # noqa: E402
from snapshot import snapshot_weekly  # noqa: E402

_FILENAME_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})-weekly-tracker\.md$")

_METRIC_DEFAULTS = (
    "owner_conversations", "ndas_signed", "financials_received", "lois_submitted",
    "closed_not_proceeding", "outreach_sends_this_week", "outreach_sends_prior_week",
    "drafts_this_week", "drafts_prior_week", "linkedin_dms_this_week",
    "linkedin_dms_prior_week", "ops_dials_this_week", "ops_dials_prior_week",
    "conferences_attended", "intermediary_meetings", "cims_received",
)


def _list_week_endings() -> list[date]:
    """Available week-ending dates, newest first."""
    if not WEEKLY_TRACKERS_DIR.exists():
        return []
    out: list[date] = []
    for entry in WEEKLY_TRACKERS_DIR.iterdir():
        m = _FILENAME_RE.match(entry.name)
        if not m:
            continue
        try:
            out.append(date.fromisoformat(m.group(1)))
        except ValueError:
            continue
    out.sort(reverse=True)
    return out


# -----------------------------------------------------------------------------
# Small render helpers
# -----------------------------------------------------------------------------


def _delta_sub(this_week: int, prior_week: int) -> str:
    if this_week > prior_week:
        return f'<span class="delta-up">↑ {this_week - prior_week}</span> vs. {prior_week} prior'
    if this_week < prior_week:
        return f'<span class="delta-down">↓ {prior_week - this_week}</span> vs. {prior_week} prior'
    return f'<span class="delta-flat">→</span> same as prior ({prior_week})'


def _kpi_tile(label: str, value: int, sub_html: str, color: str, icon: str) -> str:
    return (
        f'<div class="gb-kpi-tile {color}">'
        f'<div class="gb-kpi-icon-row">'
        f'<span class="gb-kpi-icon">{escape(icon)}</span>'
        f'<span class="gb-kpi-label">{escape(label)}</span>'
        f'</div>'
        f'<div class="gb-kpi-value">{value}</div>'
        f'<div class="gb-kpi-sub">{sub_html}</div>'
        f'</div>'
    )


def _zone_head(label: str, sublabel: str, meta: str = "") -> str:
    meta_html = f'<div class="gb-zone-meta">{escape(meta)}</div>' if meta else ""
    return (
        f'<div class="gb-zone-head">'
        f'<div>'
        f'<div class="gb-zone-label">{escape(label)}</div>'
        f'<div class="gb-zone-sublabel">{escape(sublabel)}</div>'
        f'</div>'
        f'{meta_html}'
        f'</div>'
    )


_NEUTRAL_SUB = '<span class="delta-flat">→</span> snapshot total'


# -----------------------------------------------------------------------------
# Zone renderers
# -----------------------------------------------------------------------------


def _render_subtitle(count: int, selected: date) -> str:
    sel = selected.strftime("%b %-d, %Y")
    return (
        '<div class="gb-subtitle">'
        f"Frozen weekly view · {count} historical snapshot{'s' if count != 1 else ''} · "
        f'<span class="highlight">currently viewing week ending {escape(sel)}</span>. '
        "Activity metrics are window-correct; pipeline-state metrics reflect current Attio."
        "</div>"
    )


def _render_zone_1_deal_flow(metrics: dict) -> str:
    head = _zone_head("Deal Flow · Headline",
                      "Outcomes that move the business · this week", "7-day window")
    tiles = "".join([
        _kpi_tile("Owner conversations", metrics["owner_conversations"], _NEUTRAL_SUB, "blue", "◆"),
        _kpi_tile("NDAs signed", metrics["ndas_signed"], _NEUTRAL_SUB, "purple", "✎"),
        _kpi_tile("Financials received", metrics["financials_received"], _NEUTRAL_SUB, "yellow", "$"),
        _kpi_tile("LOIs submitted", metrics["lois_submitted"], _NEUTRAL_SUB, "green", "↗"),
        _kpi_tile("Closed / Not proceeding", metrics["closed_not_proceeding"], _NEUTRAL_SUB, "red", "×"),
    ])
    return f'<section class="gb-zone">{head}<div class="gb-kpi-strip">{tiles}</div></section>'


def _render_zone_2_outbound(metrics: dict) -> str:
    head = _zone_head("Outbound Activity",
                      "Sends, drafts, LinkedIn, dials · this week vs. prior", "7-day window")
    tiles = "".join([
        _kpi_tile("Outreach sends", metrics["outreach_sends_this_week"],
                  _delta_sub(metrics["outreach_sends_this_week"], metrics["outreach_sends_prior_week"]),
                  "blue", "✉"),
        _kpi_tile("Drafts", metrics["drafts_this_week"],
                  _delta_sub(metrics["drafts_this_week"], metrics["drafts_prior_week"]),
                  "purple", "✎"),
        _kpi_tile("LinkedIn DMs", metrics["linkedin_dms_this_week"],
                  _delta_sub(metrics["linkedin_dms_this_week"], metrics["linkedin_dms_prior_week"]),
                  "yellow", "in"),
        _kpi_tile("Operations dials", metrics["ops_dials_this_week"],
                  _delta_sub(metrics["ops_dials_this_week"], metrics["ops_dials_prior_week"]),
                  "green", "☎"),
    ])
    return f'<section class="gb-zone">{head}<div class="gb-kpi-strip">{tiles}</div></section>'


def _render_zone_3_channels(channels: list[dict]) -> str:
    head = _zone_head("Channel Performance",
                      "Outbound activity by channel · frozen for this week",
                      f"{len(channels)} channels" if channels else "")
    if not channels:
        return (f'<section class="gb-zone">{head}'
                '<div class="gb-zone-empty">No channel data captured for this week.</div></section>')

    rows = []
    for ch in channels:
        deferred = bool(ch.get("deferred"))
        if deferred:
            sent = reply = positive = "—"
            to_nda_html = "—"
            rate_cell = '<span class="gb-ch-pill">pending</span>'
            tr_class = ' class="deferred"'
        else:
            sent = str(ch.get("sent", "—"))
            reply = str(ch.get("reply", "—"))
            positive = str(ch.get("positive", "—"))
            to_nda_html = f"<strong>{escape(str(ch.get('to_nda', '—')))}</strong>"
            rate_cell = escape(str(ch.get("reply_rate", "—")))
            tr_class = ""
        rows.append(
            f'<tr{tr_class}>'
            f'<td><div class="gb-ch-name">{escape(str(ch.get("channel", "—")))}</div></td>'
            f'<td class="right">{escape(sent)}</td>'
            f'<td class="right">{escape(reply)}</td>'
            f'<td class="right">{escape(positive)}</td>'
            f'<td class="right">{to_nda_html}</td>'
            f'<td class="right">{rate_cell}</td>'
            f'</tr>'
        )

    table = (
        '<table class="gb-ch-table"><thead><tr>'
        '<th>Channel</th><th class="right">Sent / Dialed</th>'
        '<th class="right">Reply / Conv</th><th class="right">Positive</th>'
        '<th class="right">→ NDA</th><th class="right">Reply rate</th>'
        f'</tr></thead><tbody>{"".join(rows)}</tbody></table>'
    )
    return f'<section class="gb-zone">{head}{table}</section>'


def _render_zone_4_niches(per_niche: list[dict]) -> str:
    active_count = sum(1 for r in per_niche if r.get("active"))
    meta = (f"{active_count} of {len(per_niche)} niches active"
            if per_niche else "no niche data")
    head = _zone_head("Per-Niche Breakdown",
                      "Operations dial activity by niche · lifetime totals", meta)
    if not per_niche:
        return (f'<section class="gb-zone">{head}'
                '<div class="gb-zone-empty">No per-niche data captured for this week.</div></section>')

    rows = []
    for r in per_niche:
        active = bool(r.get("active"))
        cell = "✓ active" if active else "—"
        color = "var(--green)" if active else "var(--text-dim)"
        rows.append(
            f'<tr>'
            f'<td><div class="gb-ch-name">{escape(str(r.get("niche", "—")))}</div></td>'
            f'<td class="right" style="color: {color};">{escape(cell)}</td>'
            f'<td class="right">{int(r.get("ops_dials_lifetime", 0))}</td>'
            f'</tr>'
        )

    table = (
        '<table class="gb-ch-table"><thead><tr>'
        '<th>Niche</th><th class="right">Active</th>'
        '<th class="right">Operations dials (lifetime)</th>'
        f'</tr></thead><tbody>{"".join(rows)}</tbody></table>'
    )
    return f'<section class="gb-zone">{head}{table}</section>'


def _render_zone_5_rollups(metrics: dict) -> str:
    head = _zone_head("Activity Rollups",
                      "Conferences, intermediary meetings, CIMs · plus active niches",
                      "7-day window")
    tiles = "".join([
        _kpi_tile("Conferences attended", metrics["conferences_attended"],
                  _NEUTRAL_SUB, "purple", "◇"),
        _kpi_tile("Intermediary meetings", metrics["intermediary_meetings"],
                  _NEUTRAL_SUB, "blue", "⇆"),
        _kpi_tile("CIMs received", metrics["cims_received"],
                  _NEUTRAL_SUB, "yellow", "📄"),
    ])
    active_niches = metrics.get("active_niches") or []
    if active_niches:
        chips = "".join(f'<span class="gb-act-chip">{escape(n)}</span>' for n in active_niches)
        chip_block = (
            '<div class="gb-act-row">'
            '<div class="gb-act-cat">Active Niches</div>'
            f'<div class="gb-act-content">{chips}</div>'
            f'<div class="gb-act-num">{len(active_niches)}</div>'
            '</div>'
        )
    else:
        chip_block = (
            '<div class="gb-act-row">'
            '<div class="gb-act-cat">Active Niches</div>'
            '<div class="gb-act-content empty">— no active niches captured</div>'
            '<div class="gb-act-num">0</div>'
            '</div>'
        )
    return (f'<section class="gb-zone">{head}'
            f'<div class="gb-kpi-strip">{tiles}</div>'
            f'<div>{chip_block}</div></section>')


def _render_footer(week_start: date, week_ending: date) -> str:
    return (
        '<div class="gb-page-note">'
        f"Window: {week_start.strftime('%b %-d, %Y')} → "
        f"{week_ending.strftime('%b %-d, %Y')}. "
        "End-of-week capture flow → G&amp;B Weekly Activity Tracker sheet."
        "</div>"
    )


# -----------------------------------------------------------------------------
# Page entry
# -----------------------------------------------------------------------------


def render() -> None:
    import streamlit as st

    week_endings = _list_week_endings()

    if not week_endings:
        st.markdown(
            '<div class="gb-subtitle">'
            "No historical weekly snapshots available yet. The first frozen view "
            "will land here at end of week."
            "</div>",
            unsafe_allow_html=True,
        )
        return

    with st.sidebar:
        st.markdown(
            '<div style="font-size: 11px; letter-spacing: 0.08em; '
            "text-transform: uppercase; color: var(--text-muted); "
            'margin: 12px 0 6px;">Week archive</div>',
            unsafe_allow_html=True,
        )
        selected = st.selectbox(
            "Select week",
            options=week_endings,
            format_func=lambda d: d.strftime("Week ending %b %-d, %Y"),
            label_visibility="collapsed",
            key="week_archive_select",
        )

    week_ending = selected
    week_start = week_ending - timedelta(days=6)

    st.markdown(_render_subtitle(len(week_endings), week_ending), unsafe_allow_html=True)

    try:
        snap = snapshot_weekly(week_ending)
    except Exception as exc:  # noqa: BLE001
        st.markdown(
            f'<section class="gb-zone gb-zone-pending">'
            f'{_zone_head("Snapshot unavailable", "Unable to assemble metrics for this week")}'
            f'<div class="gb-zone-empty">{escape(str(exc))}</div>'
            "</section>",
            unsafe_allow_html=True,
        )
        return

    metrics = snap.get("metrics", {}) or {}
    for k in _METRIC_DEFAULTS:
        metrics.setdefault(k, 0)
    channels = snap.get("channel_performance", []) or []
    per_niche = snap.get("per_niche_breakdown", []) or []

    st.markdown(_render_zone_1_deal_flow(metrics), unsafe_allow_html=True)
    st.markdown(_render_zone_2_outbound(metrics), unsafe_allow_html=True)
    st.markdown(_render_zone_3_channels(channels), unsafe_allow_html=True)
    st.markdown(_render_zone_4_niches(per_niche), unsafe_allow_html=True)
    st.markdown(_render_zone_5_rollups(metrics), unsafe_allow_html=True)
    st.markdown(_render_footer(week_start, week_ending), unsafe_allow_html=True)
