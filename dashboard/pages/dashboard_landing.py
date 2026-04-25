"""Dashboard landing page — 5 metric tiles, one per implemented sub-page.

Tech Stack tile retired 2026-04-24 (merged into Infrastructure). Deal Pipeline
renamed to "Active Deal Pipeline" with NDA-forward scope.

Each tile that has a corresponding live page (Active Deal Pipeline,
C-Suite & Skills, Infrastructure) reads its live loader inside a try/except
so any data-source failure falls back to a placeholder rather than crashing
the landing page. M&A Analytics and Deal Aggregator stay placeholder until
their respective live wiring lands.
"""

from __future__ import annotations

from textwrap import dedent

import sys
from pathlib import Path

_DASHBOARD_DIR = Path(__file__).resolve().parent.parent
if str(_DASHBOARD_DIR) not in sys.path:
    sys.path.insert(0, str(_DASHBOARD_DIR))


def _tile(body: str) -> str:
    return dedent(body).strip()


def _tile_deal_aggregator() -> str:
    return _tile("""
    <div class="gb-tile">
    <div class="label">Deal Aggregator</div>
    <div class="primary">3<span class="unit">new leads</span></div>
    <div class="footer">
    <span class="gb-trend up">&uarr; vs. 1 yesterday</span>
    <span class="gb-horizon">TODAY</span>
    </div>
    </div>
    """)


def _tile_deal_pipeline() -> str:
    """Live: count of NDA-forward deals from the Attio snapshot."""
    try:
        from data_sources import load_pipeline
        snapshot = load_pipeline(scope="active")
        if snapshot is None:
            count = 0
            trend = "no snapshot"
        else:
            count = len(snapshot.deals)
            if count == 0:
                trend = "&rarr; nothing in NDA forward"
                trend_class = "flat"
            elif count > 0:
                trend = f"&uarr; {count} active conversation" + ("s" if count != 1 else "")
                trend_class = "up"
    except Exception:
        return _tile("""
        <div class="gb-tile">
        <div class="label">Active Deal Pipeline</div>
        <div class="primary">&mdash;<span class="unit">snapshot unreachable</span></div>
        <div class="footer">
        <span class="gb-trend flat">&rarr; check page</span>
        <span class="gb-horizon">NOW</span>
        </div>
        </div>
        """)
    if count == 0:
        return _tile("""
        <div class="gb-tile">
        <div class="label">Active Deal Pipeline</div>
        <div class="primary">0<span class="unit">NDA forward</span></div>
        <div class="footer">
        <span class="gb-trend flat">&rarr; nothing in NDA stage yet</span>
        <span class="gb-horizon">NOW</span>
        </div>
        </div>
        """)
    return _tile(f"""
    <div class="gb-tile">
    <div class="label">Active Deal Pipeline</div>
    <div class="primary">{count}<span class="unit">active conversations</span></div>
    <div class="footer">
    <span class="gb-trend up">&uarr; NDA forward</span>
    <span class="gb-horizon">NOW</span>
    </div>
    </div>
    """)


def _tile_c_suite_skills() -> str:
    """Live: count of scheduled skills that fired today + alert state."""
    try:
        from data_sources import load_skill_health, skill_health_summary
        groups = load_skill_health()
        summary = skill_health_summary(groups)
    except Exception:
        return _tile("""
        <div class="gb-tile">
        <div class="label">C-Suite &amp; Skills</div>
        <div class="primary">&mdash;<span class="unit">loader unreachable</span></div>
        <div class="footer">
        <span class="gb-trend flat">&rarr; check page</span>
        <span class="gb-horizon">TODAY</span>
        </div>
        </div>
        """)
    fired = summary["fired_today"]
    on_deck = summary["on_deck"]
    missed = summary["missed"]
    gaps = summary["gaps"]
    scheduled_total = fired + on_deck + missed + gaps  # all that *should* fire today or are scheduled at all
    if gaps > 0 or missed > 0:
        dot = "red"
        bits = []
        if gaps:
            bits.append(f"{gaps} gap")
        if missed:
            bits.append(f"{missed} missed")
        status_text = " &middot; ".join(bits)
    elif on_deck > 0:
        dot = "yellow"
        status_text = f"{on_deck} on deck"
    else:
        dot = "green"
        status_text = "all on schedule"
    return _tile(f"""
    <div class="gb-tile">
    <div class="label">C-Suite &amp; Skills</div>
    <div class="primary">{fired}<span class="unit">/ {scheduled_total} fired today</span></div>
    <div class="gb-status-row">
    <span class="gb-status-dot {dot}"></span>
    <span class="gb-status-text">{status_text}</span>
    </div>
    <div class="footer">
    <span class="gb-trend flat">&rarr; {summary["ondemand"]} on-demand</span>
    <span class="gb-horizon">TODAY</span>
    </div>
    </div>
    """)


def _tile_infrastructure() -> str:
    """Live: System Health tile counts + alert state."""
    try:
        from data_sources import load_system_health, system_health_summary
        tiles = load_system_health()
        summary = system_health_summary(tiles)
    except Exception:
        return _tile("""
        <div class="gb-tile">
        <div class="label">Infrastructure</div>
        <div class="primary">&mdash;<span class="unit">probes unreachable</span></div>
        <div class="footer">
        <span class="gb-trend flat">&rarr; check page</span>
        <span class="gb-horizon">NOW</span>
        </div>
        </div>
        """)
    healthy = summary["healthy"]
    total = sum(summary.values())
    if summary["alert"] > 0:
        dot = "red"
        status_text = f'{summary["alert"]} alert &middot; {summary["warn"]} warn' if summary["warn"] else f'{summary["alert"]} alert'
    elif summary["warn"] > 0:
        dot = "yellow"
        status_text = f'{summary["warn"]} warn'
    else:
        dot = "green"
        status_text = "all systems nominal"
    return _tile(f"""
    <div class="gb-tile">
    <div class="label">Infrastructure</div>
    <div class="primary">{healthy}<span class="unit">/ {total} healthy</span></div>
    <div class="gb-status-row">
    <span class="gb-status-dot {dot}"></span>
    <span class="gb-status-text">{status_text}</span>
    </div>
    <div class="footer">
    <span class="gb-trend flat">&rarr; live probes</span>
    <span class="gb-horizon">NOW</span>
    </div>
    </div>
    """)


def _tile_ma_activity() -> str:
    return _tile("""
    <div class="gb-tile">
    <div class="label">M&amp;A Analytics</div>
    <div class="gb-ma-list">
    <div class="gb-ma-label">Owner conversations</div><div class="gb-ma-value">3</div>
    <div class="gb-ma-label">NDAs signed</div><div class="gb-ma-value">1</div>
    <div class="gb-ma-label">Outbound contacted</div><div class="gb-ma-value">1,539</div>
    <div class="gb-ma-label">Reply rate</div><div class="gb-ma-value">4.3%</div>
    </div>
    <div class="footer">
    <span class="gb-trend up">&uarr; vs. 4 last week</span>
    <span class="gb-horizon">THIS WEEK</span>
    </div>
    </div>
    """)


def render() -> None:
    import streamlit as st

    tiles = [
        _tile_deal_aggregator(),
        _tile_deal_pipeline(),
        _tile_c_suite_skills(),
        _tile_infrastructure(),
        _tile_ma_activity(),
    ]
    st.markdown(
        f'<div class="gb-grid">{"".join(tiles)}</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="gb-page-note">Active Deal Pipeline, C-Suite &amp; Skills, '
        "and Infrastructure tiles read live data. Deal Aggregator and M&amp;A "
        "Analytics tiles still show placeholders pending wire-up."
        "</div>",
        unsafe_allow_html=True,
    )
