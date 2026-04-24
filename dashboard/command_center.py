"""G&B Command Center — Streamlit entrypoint.

Session 1: App shell + Dashboard landing page with 6 tiles.
Scope: brain/context/continuation-2026-04-24-dashboard-scope-locked.md
Visual reference: dashboard/mockup-landing.html

Launch:
    dashboard/.venv/bin/streamlit run dashboard/command_center.py
"""

from __future__ import annotations

from datetime import datetime
from html import escape
from textwrap import dedent

import streamlit as st

from theme import GLOBAL_CSS, NAV_ITEMS, REFRESH_SECONDS


st.set_page_config(
    page_title="G&B Command Center",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="expanded",
)


def inject_css() -> None:
    st.markdown(GLOBAL_CSS, unsafe_allow_html=True)


def render_sidebar() -> None:
    items_html = "".join(
        f'<div class="gb-nav-item {"active" if active else "disabled"}">'
        f'<span class="dot"></span>{escape(name)}</div>'
        for name, active in NAV_ITEMS
    )
    st.sidebar.markdown(
        f"""
        <div class="gb-brand">
          <div class="logo">G&amp;B Command Center</div>
          <div class="sub">Greenwich &amp; Barrow</div>
        </div>
        <div class="gb-nav">{items_html}</div>
        """,
        unsafe_allow_html=True,
    )


def render_topbar(title: str) -> None:
    now = datetime.now()
    date_str = now.strftime("%A, %B %-d, %Y")
    updated_str = now.strftime("%H:%M:%S")
    st.markdown(
        f"""
        <div class="gb-topbar">
          <h1>{escape(title)}</h1>
          <div class="meta">
            {escape(date_str)}
            <span class="sep">•</span>
            Refreshing every {REFRESH_SECONDS}s
            <span class="sep">•</span>
            Last updated {escape(updated_str)}
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# -----------------------------------------------------------------------------
# Dashboard landing tiles
# -----------------------------------------------------------------------------
# Session 1 uses placeholder values that match mockup-landing.html exactly.
# Later sessions wire each tile to its source of truth (deal-aggregator artifact,
# Attio MCP, launchd logs, health-monitor output, weekly-tracker, connectivity checks).


def _tile(body: str) -> str:
    return dedent(body).strip()


def tile_deal_aggregator() -> str:
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


def tile_deal_pipeline() -> str:
    return _tile("""
    <div class="gb-tile">
    <div class="label">Deal Pipeline</div>
    <div class="primary">14<span class="unit">active deals</span></div>
    <div class="footer">
    <span class="gb-trend flat">&rarr; no change</span>
    <span class="gb-horizon">NOW</span>
    </div>
    </div>
    """)


def tile_c_suite_skills() -> str:
    return _tile("""
    <div class="gb-tile">
    <div class="label">C-Suite &amp; Skills</div>
    <div class="primary">12<span class="unit">/ 12 fired</span></div>
    <div class="gb-status-row">
    <span class="gb-status-dot green"></span>
    <span class="gb-status-text">all on schedule</span>
    </div>
    <div class="footer">
    <span class="gb-trend flat">&rarr; same as yesterday</span>
    <span class="gb-horizon">TODAY</span>
    </div>
    </div>
    """)


def tile_infrastructure() -> str:
    return _tile("""
    <div class="gb-tile">
    <div class="label">Infrastructure</div>
    <div class="primary">7<span class="unit">/ 7 healthy</span></div>
    <div class="gb-status-row">
    <span class="gb-status-dot green"></span>
    <span class="gb-status-text">all systems nominal</span>
    </div>
    <div class="footer">
    <span class="gb-trend flat">&rarr; stable</span>
    <span class="gb-horizon">NOW</span>
    </div>
    </div>
    """)


def tile_ma_activity() -> str:
    return _tile("""
    <div class="gb-tile">
    <div class="label">M&amp;A Activity</div>
    <div class="gb-ma-list">
    <div class="gb-ma-label">Owner conversations</div><div class="gb-ma-value">3</div>
    <div class="gb-ma-label">NDAs signed</div><div class="gb-ma-value">1</div>
    <div class="gb-ma-label">Financials received</div><div class="gb-ma-value">2</div>
    <div class="gb-ma-label">LOIs submitted</div><div class="gb-ma-value">0</div>
    </div>
    <div class="footer">
    <span class="gb-trend up">&uarr; vs. 4 last week</span>
    <span class="gb-horizon">THIS WEEK</span>
    </div>
    </div>
    """)


def tile_tech_stack() -> str:
    return _tile("""
    <div class="gb-tile">
    <div class="label">Tech Stack</div>
    <div class="primary">9<span class="unit">/ 9 in range</span></div>
    <div class="gb-status-row">
    <span class="gb-status-dot green"></span>
    <span class="gb-status-text">connected, credits healthy</span>
    </div>
    <div class="footer">
    <span class="gb-trend flat">&rarr; stable</span>
    <span class="gb-horizon">NOW</span>
    </div>
    </div>
    """)


def render_landing() -> None:
    tiles = [
        tile_deal_aggregator(),
        tile_deal_pipeline(),
        tile_c_suite_skills(),
        tile_infrastructure(),
        tile_ma_activity(),
        tile_tech_stack(),
    ]
    st.markdown(
        f'<div class="gb-grid">{"".join(tiles)}</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="gb-page-note">Session 1 build — tiles render placeholder values. '
        "Live data wiring ships in Sessions 2-6.</div>",
        unsafe_allow_html=True,
    )


def main() -> None:
    inject_css()
    render_sidebar()
    render_topbar("Dashboard")
    render_landing()


if __name__ == "__main__":
    main()
