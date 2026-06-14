"""M&A Analytics page — activity rollups across deal flow + outreach + ops.

Replaces the Weekly Activity Tracker Google Sheet (the spreadsheet Kay used to
maintain manually). Five zones — three live, two DealsX-deferred until that
integration ships:

    Zone 1: Deal Flow Headline       LIVE  — Attio snapshot + brain/calls/
    Zone 2: Outbound Funnel          DEFERRED — pending DealsX integration
    Zone 2.5: AI Response Categories DEFERRED — pending DealsX integration
    Zone 3: Channel Performance      PARTIAL — live rows + DealsX-deferred row
    Zone 4: Trends · 12 weeks        LIVE  — best-effort, pending where no
                                              historical weekly data
    Zone 5: Activity Detail          LIVE  — chip lists per category

All zones tolerate missing data — when a source isn't wired (JJ master sheet,
weekly historical snapshots, conference-engagement output), the zone renders
with "—" or a "Pending" chip rather than crashing the page.
"""

from __future__ import annotations

from html import escape
from textwrap import dedent

import sys
from pathlib import Path

_DASHBOARD_DIR = Path(__file__).resolve().parent.parent
if str(_DASHBOARD_DIR) not in sys.path:
    sys.path.insert(0, str(_DASHBOARD_DIR))

from data_sources import (  # noqa: E402
    ActivityRow,
    ChannelRow,
    KPITile,
    MAAnalytics,
    NicheBreakdown,
    NicheBreakdownRow,
    SourceMixRow,
    TrendPanel,
    WeeklyGoalMetric,
    load_ma_analytics,
    load_pipeline,
)


# -----------------------------------------------------------------------------
# Subtitle + filter bar (visual-only, matches Deal Aggregator pattern)
# -----------------------------------------------------------------------------


def _render_subtitle(ma: MAAnalytics) -> str:
    snap_phrase = (
        "Attio snapshot + vault calls"
        if ma.snapshot_fresh
        else "vault calls only; Attio snapshot unavailable"
    )
    return (
        '<div class="gb-subtitle">'
        f'<span class="highlight">Weekly sourcing goals first.</span> '
        f'Tracks conferences/networking, intermediary and river-guide conversations, owner/seller conversations, then deal-flow outcomes. Live sources: {snap_phrase}.'
        "</div>"
    )


def _render_filter_bar(ma: MAAnalytics) -> str:
    """Static window label. Interactive filters were removed from the default
    view because they were visual-only and made the page feel less operational."""
    date_range = f"{ma.week_start.strftime('%b %-d')} – {ma.week_end.strftime('%b %-d, %Y')}"
    return dedent(
        f"""
        <div class="gb-filter-bar">
        <div class="gb-filter-tabs">
        <button class="gb-filter-tab active">This week</button>
        </div>
        <div style="margin-left: auto; padding: 6px 12px; font-size: 12px;
                    background: var(--panel); border: 1px solid var(--border);
                    border-radius: 6px; color: var(--text-muted);
                    font-variant-numeric: tabular-nums;">
        {escape(date_range)}
        </div>
        </div>
        """
    ).strip()


# -----------------------------------------------------------------------------
# Top Metrics: Kay's current weekly goals
# -----------------------------------------------------------------------------


def _goal_color(goal: WeeklyGoalMetric) -> str:
    if goal.status == "on_track":
        return "green"
    if goal.status == "below":
        return "red"
    return "yellow"


def _goal_sub(goal: WeeklyGoalMetric) -> str:
    target = f"goal {goal.target_min}-{goal.target_max}/week"
    if goal.status == "on_track":
        return f"on track · {target}"
    if goal.status == "below":
        return f"below goal · {target}"
    return f"above target · {target}"


def _render_goal_tile(goal: WeeklyGoalMetric) -> str:
    color = _goal_color(goal)
    sub = _goal_sub(goal)
    if goal.items:
        items_html = "".join(
            f'<li>{escape(item)}</li>'
            for item in goal.items[: goal.target_max]
        )
        more = len(goal.items) - goal.target_max
        if more > 0:
            items_html += f'<li>+{more} more</li>'
        detail = (
            '<div class="gb-kpi-sub gb-weekly-detail">'
            '<div class="gb-weekly-detail-label">Weekly detail:</div>'
            f'<ol>{items_html}</ol>'
            '</div>'
        )
    else:
        detail = (
            '<div class="gb-kpi-sub gb-weekly-detail">'
            '<div class="gb-weekly-detail-label">Weekly detail:</div>'
            '<div>none captured yet</div>'
            '</div>'
        )
    return dedent(
        f"""
        <div class="gb-kpi-tile {color}">
        <div class="gb-kpi-icon-row">
        <span class="gb-kpi-label">{escape(goal.label)}</span>
        </div>
        <div class="gb-kpi-value">{goal.count} <span style="font-size: 18px; color: var(--text-muted);">/ {goal.target_min}-{goal.target_max}</span></div>
        <div class="gb-kpi-sub">{escape(sub)}</div>
        {detail}
        </div>
        """
    ).strip()


def _render_zone_goals(ma: MAAnalytics) -> str:
    head = dedent(
        """
        <div class="gb-zone-head">
        <div>
        <div class="gb-zone-label">Top Weekly Goals</div>
        <div class="gb-zone-sublabel">Current monthly focus from investor update · each operating goal band is 1-3 per week</div>
        </div>
        <div class="gb-zone-meta">this month focus</div>
        </div>
        """
    ).strip()
    tiles = "".join(_render_goal_tile(g) for g in ma.weekly_goals)
    return f'<section class="gb-zone">{head}<div class="gb-kpi-strip gb-kpi-strip-three">{tiles}</div></section>'


def _render_kpi_tile(t: KPITile) -> str:
    # Sub line wraps the leading ↑/↓/→ in a delta span if present so the
    # green/red/dim coloring matches the mockup.
    sub_html = escape(t.sub)
    if t.sub.startswith("↑"):
        sub_html = f'<span class="delta-up">{escape(t.sub.split(" ")[0])}</span> {escape(" ".join(t.sub.split(" ")[1:]))}'
    elif t.sub.startswith("↓"):
        sub_html = f'<span class="delta-down">{escape(t.sub.split(" ")[0])}</span> {escape(" ".join(t.sub.split(" ")[1:]))}'
    elif t.sub.startswith("→"):
        sub_html = f'<span class="delta-flat">{escape(t.sub.split(" ")[0])}</span> {escape(" ".join(t.sub.split(" ")[1:]))}'
    return dedent(
        f"""
        <div class="gb-kpi-tile {t.color}">
        <div class="gb-kpi-icon-row">
        <span class="gb-kpi-icon">{escape(t.icon)}</span>
        <span class="gb-kpi-label">{escape("Quality conversations" if t.label == "Owner conversations" else t.label)}</span>
        </div>
        <div class="gb-kpi-value">{t.value}</div>
        <div class="gb-kpi-sub">{sub_html}</div>
        </div>
        """
    ).strip()


def _render_zone_1(ma: MAAnalytics) -> str:
    head = dedent(
        """
        <div class="gb-zone-head">
        <div>
        <div class="gb-zone-label">Deal Flow Outcomes</div>
        <div class="gb-zone-sublabel">Pipeline movement created by the sourcing work · this week and lifetime</div>
        </div>
        <div class="gb-zone-meta">weekly + LTD</div>
        </div>
        """
    ).strip()
    labels = ["Quality conversations" if t.label == "Owner conversations" else t.label for t in ma.deal_flow_tiles]
    week_values = [str(t.value) for t in ma.deal_flow_tiles]

    snapshot = load_pipeline(scope="full")
    ltd_values = ["—", "—", "—", "—", "—"]
    if snapshot is not None and ltd_values:
        # True LTD stage-history is a plumbing task. Closed post-NDA is the one
        # durable LTD outcome currently present in the snapshot contract.
        ltd_values[-1] = str(snapshot.closed_count_post_nda)

    header_cells = "".join(f'<th class="right">{escape(label)}</th>' for label in labels)
    week_cells = "".join(f'<td class="right">{escape(v)}</td>' for v in week_values)
    ltd_cells = "".join(f'<td class="right">{escape(v)}</td>' for v in ltd_values)
    table = dedent(
        f"""
        <table class="gb-ch-table gb-outcomes-table">
        <thead>
        <tr>
        <th>Window</th>
        {header_cells}
        </tr>
        </thead>
        <tbody>
        <tr><td><div class="gb-ch-name">This week</div></td>{week_cells}</tr>
        <tr><td><div class="gb-ch-name">LTD</div><div class="gb-ch-desc">stage-history backfill pending</div></td>{ltd_cells}</tr>
        </tbody>
        </table>
        """
    ).strip()
    return f'<section class="gb-zone">{head}{table}</section>'


# -----------------------------------------------------------------------------
# Pipeline Snapshot
# -----------------------------------------------------------------------------


def _pipeline_stage_label(stage: str) -> str:
    return {
        "Contacted": "Warmed / teaser",
        "Financials Received": "Financials",
        "Closed / Not Proceeding": "Closed / not proceeding",
    }.get(stage, stage)


def _stage_age_text(stage_deals: list) -> str:
    if not stage_deals:
        return "—"
    from datetime import date, datetime
    oldest = None
    oldest_deal = None
    for deal in stage_deals:
        try:
            ts = datetime.fromisoformat(deal.stage_since.replace("Z", "+00:00"))
        except (ValueError, AttributeError):
            continue
        if oldest is None or ts < oldest:
            oldest = ts
            oldest_deal = deal
    if oldest is None or oldest_deal is None:
        return "—"
    age = (date.today() - oldest.date()).days
    return f"oldest {age}d · {oldest_deal.company}"


def _render_pipeline_snapshot() -> str:
    snapshot = load_pipeline(scope="full")
    head = dedent(
        """
        <div class="gb-zone-head">
        <div>
        <div class="gb-zone-label">Active Pipeline Snapshot</div>
        <div class="gb-zone-sublabel">Current engaged pipeline · company references, not another metric board</div>
        </div>
        <div class="gb-zone-meta">current state</div>
        </div>
        """
    ).strip()
    if snapshot is None:
        return f'<section class="gb-zone">{head}<div class="gb-zone-empty">Attio snapshot unavailable</div></section>'

    # Dashboard pipeline starts once there has been engagement. Raw Identified
    # records remain in Attio, but this operating view should not show them
    # until a direct or intermediary-routed response moves them forward.
    stages = [stage for stage in snapshot.stages if stage != "Identified"]
    cells = []
    for stage in stages:
        deals = [d for d in snapshot.deals if d.stage == stage]
        count = len(deals)
        if deals:
            items = "".join(
                f'<li><a href="{escape(d.attio_url)}" target="_blank">{escape(d.company)}</a></li>'
                for d in deals[:5]
            )
            if len(deals) > 5:
                items += f'<li class="dim">+{len(deals) - 5} more</li>'
        else:
            items = '<li class="dim">None</li>'
        meta = _stage_age_text(deals)
        cell_class = "active" if count else "empty"
        cells.append(
            '<div class="gb-pipe-cell {cell_class}">'
            '<div class="gb-pipe-top"><span class="gb-pipe-label">{stage}</span><span class="gb-pipe-badge">{count}</span></div>'
            '<ol class="gb-pipe-list">{items}</ol>'
            '<div class="gb-pipe-meta">{meta}</div>'
            '</div>'.format(
                cell_class=escape(cell_class),
                stage=escape(_pipeline_stage_label(stage)),
                count=count,
                items=items,
                meta=escape(meta),
            )
        )
    return f'<section class="gb-zone">{head}<div class="gb-pipe-strip">{"".join(cells)}</div></section>'


# -----------------------------------------------------------------------------
# Zone 2 + 2.5: Deferred placeholders
# -----------------------------------------------------------------------------


def _render_zone_placeholder(label: str, sublabel: str, body: str) -> str:
    return dedent(
        f"""
        <section class="gb-zone gb-zone-pending">
        <div class="gb-zone-head">
        <div>
        <div class="gb-zone-label">{escape(label)}</div>
        <div class="gb-zone-sublabel">{escape(sublabel)}</div>
        </div>
        <div class="gb-zone-meta"><span class="pill yellow">DealsX pending</span></div>
        </div>
        <div class="gb-zone-empty">{escape(body)}</div>
        </section>
        """
    ).strip()


# -----------------------------------------------------------------------------
# Zone 3: Channel Performance
# -----------------------------------------------------------------------------


def _render_channel_row(ch: ChannelRow) -> str:
    tr_class = ' class="deferred"' if ch.deferred else ""
    if ch.deferred:
        rate_cell = '<span class="gb-ch-pill">DealsX pending</span>'
        sent = reply = positive = to_nda = "—"
    else:
        sent = ch.sent
        reply = ch.reply
        positive = ch.positive
        to_nda = f"<strong>{escape(ch.to_nda)}</strong>"
        bar_color_class = f" {ch.bar_color}" if ch.bar_color else ""
        bar_html = (
            f'<span class="gb-ch-bar"><span class="gb-ch-bar-fill{bar_color_class}" '
            f'style="width:{ch.bar_pct}%"></span></span>'
        )
        rate_cell = f"{escape(ch.reply_rate)} {bar_html}"

    return dedent(
        f"""
        <tr{tr_class}>
        <td>
        <div class="gb-ch-name"><span class="gb-ch-dot {escape(ch.dot_class)}"></span>{escape(ch.name)}</div>
        <div class="gb-ch-desc">{escape(ch.description)}</div>
        </td>
        <td class="right">{escape(sent)}</td>
        <td class="right">{escape(reply)}</td>
        <td class="right">{escape(positive)}</td>
        <td class="right">{to_nda}</td>
        <td class="right">{rate_cell}</td>
        </tr>
        """
    ).strip()


def _render_zone_3(ma: MAAnalytics) -> str:
    live_channels = [c for c in ma.channels if not c.deferred]
    deferred = sum(1 for c in ma.channels if c.deferred)
    head = dedent(
        f"""
        <div class="gb-zone-head">
        <div>
        <div class="gb-zone-label">Channel Performance</div>
        <div class="gb-zone-sublabel">Live weekly channel activity · DealsX email + LinkedIn volume pending</div>
        </div>
        <div class="gb-zone-meta">{len(live_channels)} live channels · {deferred} pending</div>
        </div>
        """
    ).strip()
    rows = "".join(_render_channel_row(c) for c in live_channels)
    pending_row = dedent(
        """
        <tr class="deferred">
        <td><div class="gb-ch-name"><span class="gb-ch-dot dealsx"></span>DealsX email + LinkedIn</div><div class="gb-ch-desc">High-volume outbound volume, replies, positive replies, and reply rate will appear here once the integration is wired.</div></td>
        <td class="right">—</td><td class="right">—</td><td class="right">—</td><td class="right">—</td><td class="right"><span class="gb-ch-pill">Pending</span></td>
        </tr>
        """
    ).strip()
    table = dedent(
        f"""
        <table class="gb-ch-table">
        <thead>
        <tr>
        <th>Channel</th>
        <th class="right">Sent / Dialed</th>
        <th class="right">Reply / Conv</th>
        <th class="right">Positive</th>
        <th class="right">→ NDA</th>
        <th class="right">Reply rate</th>
        </tr>
        </thead>
        <tbody>{rows}{pending_row}</tbody>
        </table>
        """
    ).strip()
    return f'<section class="gb-zone">{head}{table}</section>'


# -----------------------------------------------------------------------------
# Zone 4: Trends · 12 weeks
# -----------------------------------------------------------------------------


def _render_trend_panel(panel: TrendPanel, x_labels: tuple[str, str, str]) -> str:
    cell_class = "gb-trend-cell pending" if panel.pending else "gb-trend-cell"
    bars = "".join(
        f'<div class="gb-trend-bar {panel.bar_color}" style="height: {h}%"></div>'
        for h in panel.bars
    )
    return dedent(
        f"""
        <div class="{cell_class}">
        <div class="gb-trend-label">{escape(panel.label)}</div>
        <div class="gb-trend-value-row">
        <span class="gb-trend-value">{escape(panel.value)}</span>
        <span class="gb-trend-delta {panel.delta_class}">{escape(panel.delta)}</span>
        </div>
        <div class="gb-trend-bars">{bars}</div>
        <div class="gb-trend-x-labels">
        <span>{escape(x_labels[0])}</span>
        <span>{escape(x_labels[1])}</span>
        <span>{escape(x_labels[2])}</span>
        </div>
        </div>
        """
    ).strip()


def _render_zone_4(ma: MAAnalytics) -> str:
    pending = sum(1 for p in ma.trends if p.pending)
    head = dedent(
        f"""
        <div class="gb-zone-head">
        <div>
        <div class="gb-zone-label">Trends · Last 12 Weeks</div>
        <div class="gb-zone-sublabel">Weekly buckets · NDAs, reply rate, owner conversations, operations dials{' · ' + str(pending) + ' panels pending data history' if pending else ''}</div>
        </div>
        <div class="gb-zone-meta">{escape(ma.trend_x_labels[0])} – {escape(ma.trend_x_labels[2])}, 2026</div>
        </div>
        """
    ).strip()
    panels = "".join(_render_trend_panel(p, ma.trend_x_labels) for p in ma.trends)
    return f'<section class="gb-zone">{head}<div class="gb-trend-grid">{panels}</div></section>'


# -----------------------------------------------------------------------------
# Zone 5: Activity Detail
# -----------------------------------------------------------------------------


def _render_activity_row(row: ActivityRow) -> str:
    if row.chips:
        chips_html = "".join(
            f'<span class="gb-act-chip">{escape(c)}</span>' for c in row.chips
        )
        content = f'<div class="gb-act-content">{chips_html}</div>'
    else:
        empty_text = row.empty_text or "—"
        content = f'<div class="gb-act-content empty">{escape(empty_text)}</div>'
    return dedent(
        f"""
        <div class="gb-act-row">
        <div class="gb-act-cat">{escape(row.category)}</div>
        {content}
        <div class="gb-act-num">{row.count}</div>
        </div>
        """
    ).strip()


def _render_zone_5(ma: MAAnalytics) -> str:
    head = dedent(
        """
        <div class="gb-zone-head">
        <div>
        <div class="gb-zone-label">Weekly Activity Detail</div>
        <div class="gb-zone-sublabel">Conferences/networking, intermediary touchpoints, owner/seller touchpoints, CIMs, and other sourcing inputs</div>
        </div>
        <div class="gb-zone-meta">7-day window</div>
        </div>
        """
    ).strip()
    rows = "".join(_render_activity_row(r) for r in ma.activity_rows)
    return f'<section class="gb-zone">{head}<div>{rows}</div></section>'


# -----------------------------------------------------------------------------
# Zone 6: Per-niche outreach breakdown (Phase A.4)
# -----------------------------------------------------------------------------


def _render_niche_row(row: NicheBreakdownRow) -> str:
    activity_cell = "✓ active" if row.jj_active else "—"
    activity_class = "active" if row.jj_active else "dim"
    kay_cell = str(row.kay_emails_this_week) if row.kay_emails_this_week else "—"
    kay_class = "active" if row.kay_emails_this_week else "dim"
    return dedent(
        f"""
        <tr>
        <td>
        <div class="gb-ch-name">{escape(row.niche)}</div>
        </td>
        <td class="right">{row.jj_dials_lifetime}</td>
        <td class="right"><span class="gb-niche-{activity_class}">{escape(activity_cell)}</span></td>
        <td class="right"><span class="gb-niche-{kay_class}">{kay_cell}</span></td>
        <td class="right"><span class="gb-ch-pill">DealsX pending</span></td>
        </tr>
        """
    ).strip()


def _render_zone_6(ma: MAAnalytics) -> str:
    breakdown = ma.niche_breakdown
    if breakdown is None:
        return ""
    active_count = sum(1 for r in breakdown.rows if r.jj_active)
    head = dedent(
        f"""
        <div class="gb-zone-head">
        <div>
        <div class="gb-zone-label">Per-niche Outreach</div>
        <div class="gb-zone-sublabel">Operations dial coverage by niche · email/LinkedIn attribution pending DealsX</div>
        </div>
        <div class="gb-zone-meta">{active_count} of {len(breakdown.rows)} niches active</div>
        </div>
        """
    ).strip()
    rows = "".join(_render_niche_row(r) for r in breakdown.rows)
    table = dedent(
        f"""
        <table class="gb-ch-table">
        <thead>
        <tr>
        <th>Niche</th>
        <th class="right">Operations dials (lifetime)</th>
        <th class="right">Ops activity</th>
        <th class="right">CEO emails (7d)</th>
        <th class="right">DealsX + LinkedIn</th>
        </tr>
        </thead>
        <tbody>{rows}</tbody>
        </table>
        """
    ).strip()
    return f'<section class="gb-zone">{head}{table}</section>'



# -----------------------------------------------------------------------------
# Lifetime Source Mix
# -----------------------------------------------------------------------------


def _render_source_row(row: SourceMixRow) -> str:
    pill = '<span class="gb-ch-pill">Pending</span>' if row.status == "pending" else escape(row.financials_received)
    return dedent(
        f"""
        <tr>
        <td>
        <div class="gb-ch-name">{escape(row.source)}</div>
        <div class="gb-ch-desc">{escape(row.note)}</div>
        </td>
        <td class="right">{escape(row.ltd_activity)}</td>
        <td class="right">{pill}</td>
        </tr>
        """
    ).strip()


def _render_source_mix(ma: MAAnalytics) -> str:
    head = dedent(
        """
        <div class="gb-zone-head">
        <div>
        <div class="gb-zone-label">Lead Source Mix · LTD</div>
        <div class="gb-zone-sublabel">Where real deal starts are coming from over the life of the search · financials are the key conversion point</div>
        </div>
        <div class="gb-zone-meta">source attribution</div>
        </div>
        """
    ).strip()
    rows = "".join(_render_source_row(r) for r in ma.source_rows)
    table = dedent(
        f"""
        <table class="gb-ch-table">
        <thead>
        <tr>
        <th>Source</th>
        <th class="right">LTD</th>
        <th class="right">Financials received</th>
        </tr>
        </thead>
        <tbody>{rows}</tbody>
        </table>
        """
    ).strip()
    return f'<section class="gb-zone">{head}{table}</section>'


# -----------------------------------------------------------------------------
# Page entry
# -----------------------------------------------------------------------------


def render() -> None:
    import streamlit as st

    ma = load_ma_analytics()

    st.markdown(_render_filter_bar(ma), unsafe_allow_html=True)
    st.markdown(_render_zone_goals(ma), unsafe_allow_html=True)
    st.markdown(_render_pipeline_snapshot(), unsafe_allow_html=True)
    st.markdown(_render_zone_1(ma), unsafe_allow_html=True)
    st.markdown(_render_source_mix(ma), unsafe_allow_html=True)

    st.markdown(
        '<div class="gb-page-note">Industry focus stays in the Industry Research Tracker. Financials-by-source will become live once lead-source attribution is added to the Attio snapshot or maintained as a source map.</div>',
        unsafe_allow_html=True,
    )
