"""M&A Analytics page — activity rollups across deal flow + outreach + ops.

Replaces the Weekly Activity Tracker Google Sheet (the spreadsheet Kay used to
maintain manually). Five zones — three live, two DealsX-deferred until May 7:

    Zone 1: Deal Flow Headline      LIVE  — Attio snapshot + brain/calls/
    Zone 2: Outbound Funnel         DEFERRED — DealsX live May 7
    Zone 2.5: AI Response Categories DEFERRED — DealsX live May 7
    Zone 3: Channel Performance     PARTIAL — 4 of 6 rows (DealsX deferred)
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
    TrendPanel,
    load_ma_analytics,
)


# -----------------------------------------------------------------------------
# Subtitle + filter bar (visual-only, matches Deal Aggregator pattern)
# -----------------------------------------------------------------------------


def _render_subtitle(ma: MAAnalytics) -> str:
    snap_phrase = (
        "from Attio snapshot + vault calls"
        if ma.snapshot_fresh
        else "from vault calls (Attio snapshot unavailable)"
    )
    return (
        '<div class="gb-subtitle">'
        f'Replaces the Weekly Activity Tracker. '
        f'<span class="highlight">Deal-flow outcomes up top, outbound funnel + channel performance below.</span> '
        f'7-day window {snap_phrase}.'
        "</div>"
    )


def _render_filter_bar(ma: MAAnalytics) -> str:
    """Visual-only — interactivity deferred. M&A Analytics has 5 zones with
    different time scopes (Zone 1=7d window vs prior; Zone 4=12 weekly buckets
    always); window-driving needs load_ma_analytics() refactor first."""
    date_range = (
        f"{ma.week_start.strftime('%b %-d')} – {ma.week_end.strftime('%b %-d, %Y')}"
    )
    return dedent(
        f"""
        <div class="gb-filter-bar">
        <div class="gb-filter-tabs">
        <button class="gb-filter-tab">Daily</button>
        <button class="gb-filter-tab active">This Week</button>
        <button class="gb-filter-tab">This Quarter</button>
        <button class="gb-filter-tab">LTD</button>
        </div>
        <select class="gb-filter-select"><option>All channels</option></select>
        <select class="gb-filter-select"><option>All niches</option></select>
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
# Zone 1: Deal Flow Headline
# -----------------------------------------------------------------------------


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
        <span class="gb-kpi-label">{escape(t.label)}</span>
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
        <div class="gb-zone-label">Deal Flow · Headline</div>
        <div class="gb-zone-sublabel">Outcomes that move the business · this week vs. prior</div>
        </div>
        <div class="gb-zone-meta">7-day window</div>
        </div>
        """
    ).strip()
    tiles = "".join(_render_kpi_tile(t) for t in ma.deal_flow_tiles)
    return f'<section class="gb-zone">{head}<div class="gb-kpi-strip">{tiles}</div></section>'


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
        <div class="gb-zone-meta"><span class="pill yellow">Live May 7</span></div>
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
        rate_cell = '<span class="gb-ch-pill">live May 7</span>'
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
    live = sum(1 for c in ma.channels if not c.deferred)
    deferred = sum(1 for c in ma.channels if c.deferred)
    head = dedent(
        f"""
        <div class="gb-zone-head">
        <div>
        <div class="gb-zone-label">Channel Performance</div>
        <div class="gb-zone-sublabel">Outbound activity by channel · {live} live · {deferred} pending DealsX (May 7)</div>
        </div>
        <div class="gb-zone-meta">{len(ma.channels)} channels · this week</div>
        </div>
        """
    ).strip()
    rows = "".join(_render_channel_row(c) for c in ma.channels)
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
        <tbody>{rows}</tbody>
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
        <div class="gb-zone-sublabel">Weekly buckets · NDAs, reply rate, owner conversations, JJ dials{' · ' + str(pending) + ' panels pending data history' if pending else ''}</div>
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
        <div class="gb-zone-label">Activity Detail · This Week</div>
        <div class="gb-zone-sublabel">Niche pipeline state, conferences, intermediary touchpoints</div>
        </div>
        <div class="gb-zone-meta">7-day window</div>
        </div>
        """
    ).strip()
    rows = "".join(_render_activity_row(r) for r in ma.activity_rows)
    return f'<section class="gb-zone">{head}<div>{rows}</div></section>'


# -----------------------------------------------------------------------------
# Page entry
# -----------------------------------------------------------------------------


def render() -> None:
    import streamlit as st

    ma = load_ma_analytics()

    st.markdown(_render_subtitle(ma), unsafe_allow_html=True)
    st.markdown(_render_filter_bar(ma), unsafe_allow_html=True)
    st.markdown(_render_zone_1(ma), unsafe_allow_html=True)
    st.markdown(
        _render_zone_placeholder(
            "Outbound Funnel",
            "Email volume, opens, replies, positive replies, bounces · all channels combined",
            "Live May 7 · DealsX integration unlocks email + LinkedIn DM volume, "
            "opens, replies, positive replies, and bounce rate.",
        ),
        unsafe_allow_html=True,
    )
    st.markdown(
        _render_zone_placeholder(
            "Response Categorization · AI-Classified",
            "DealsX AI tags every reply by intent · sentiment breakdown",
            "Live May 7 · DealsX AI categorizes replies as Interested / "
            "Meeting Request / Information Request / Wrong Person / Not Interested "
            "/ Uncategorizable, plus sentiment (positive / neutral / negative).",
        ),
        unsafe_allow_html=True,
    )
    st.markdown(_render_zone_3(ma), unsafe_allow_html=True)
    st.markdown(_render_zone_4(ma), unsafe_allow_html=True)
    st.markdown(_render_zone_5(ma), unsafe_allow_html=True)

    st.markdown(
        '<div class="gb-page-note">Data sources: Attio snapshot (deal-flow KPIs), '
        "<code>brain/calls/</code> (owner conversations + intermediary + conferences), "
        "<code>brain/context/email-scan-results-*</code> (CIM detection). "
        "<strong style=\"color:var(--text-muted);\">DealsX zones live May 7, 2026.</strong>"
        "</div>",
        unsafe_allow_html=True,
    )
