"""Dashboard landing page — 6 metric tiles, one per sub-page.

Session 1 seeded this with placeholders. Later sessions wire each tile to
live data from its respective sub-page's data source.
"""

from __future__ import annotations

from textwrap import dedent


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


def _tile_c_suite_skills() -> str:
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


def _tile_infrastructure() -> str:
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


def _tile_ma_activity() -> str:
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


def _tile_tech_stack() -> str:
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


def render() -> None:
    import streamlit as st

    tiles = [
        _tile_deal_aggregator(),
        _tile_deal_pipeline(),
        _tile_c_suite_skills(),
        _tile_infrastructure(),
        _tile_ma_activity(),
        _tile_tech_stack(),
    ]
    st.markdown(
        f'<div class="gb-grid">{"".join(tiles)}</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="gb-page-note">Landing tiles render placeholder values. '
        "Live data wiring ships alongside each sub-page.</div>",
        unsafe_allow_html=True,
    )
