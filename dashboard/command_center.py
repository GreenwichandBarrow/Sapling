"""G&B Command Center — Streamlit entrypoint.

Session 1: App shell + Dashboard landing (6 tiles).
Session 2: Deal Aggregator page + st.navigation router.
Session 3: Deal Pipeline page (Kanban, Attio snapshot).

Scope: brain/context/continuation-2026-04-24-dashboard-scope-locked.md

Launch:
    dashboard/.venv/bin/streamlit run dashboard/command_center.py
"""

from __future__ import annotations

from datetime import datetime
from html import escape
from pathlib import Path
import sys

import streamlit as st

# Make sibling modules importable when Streamlit runs this script.
_DASHBOARD_DIR = Path(__file__).resolve().parent
if str(_DASHBOARD_DIR) not in sys.path:
    sys.path.insert(0, str(_DASHBOARD_DIR))

from theme import GLOBAL_CSS, NAV_ITEMS, REFRESH_SECONDS  # noqa: E402
from data_sources import check_dashboard_staleness  # noqa: E402
from pages import (  # noqa: E402
    c_suite_skills,
    dashboard_landing,
    deal_aggregator,
    deal_pipeline,
    infrastructure,
    ma_analytics,
)


st.set_page_config(
    page_title="G&B Command Center",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="expanded",
)


def _inject_css() -> None:
    st.markdown(GLOBAL_CSS, unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# Page registry
# -----------------------------------------------------------------------------
# Callable targets keep each page's render function in its own module and
# avoid triggering Streamlit's auto-discovery of files under pages/.

_PAGE_RENDERERS = {
    "dashboard": (dashboard_landing.render, "Dashboard"),
    "deal-aggregator": (deal_aggregator.render, "Deal Aggregator"),
    "deal-pipeline": (deal_pipeline.render, "Active Deal Pipeline"),
    "ma-analytics": (ma_analytics.render, "M&A Analytics"),
    "c-suite-skills": (c_suite_skills.render, "C-Suite & Skills"),
    "infrastructure": (infrastructure.render, "Infrastructure"),
}


def _build_pages() -> tuple[list[st.Page], dict[str, st.Page]]:
    pages: list[st.Page] = []
    by_url: dict[str, st.Page] = {}
    for label, url_path, implemented in NAV_ITEMS:
        if not implemented:
            continue
        fn, _ = _PAGE_RENDERERS[url_path]
        page = st.Page(
            fn,
            title=label,
            url_path=url_path,
            default=(url_path == "dashboard"),
        )
        pages.append(page)
        by_url[url_path] = page  # our own map — st.Page normalizes
                                 # default pages to url_path="", so we can't
                                 # round-trip via page.url_path.
    return pages, by_url


# -----------------------------------------------------------------------------
# Topbar  (sidebar removed 2026-05-10 — Dashboard tiles are the nav surface;
#          sub-pages render a "← Greenwich & Barrow Dashboard" back-link below.)
# -----------------------------------------------------------------------------


def _render_back_home() -> None:
    st.markdown(
        '<a class="gb-back-home" href="/" target="_self">'
        '<span class="arrow">&larr;</span> Greenwich &amp; Barrow Dashboard</a>',
        unsafe_allow_html=True,
    )


def _render_topbar(title: str) -> None:
    now = datetime.now()
    date_str = now.strftime("%A, %B %-d, %Y")
    updated_str = now.strftime("%H:%M:%S")
    st.markdown(
        f"""
        <div class="gb-topbar">
          <h1>{escape(title)}</h1>
          <div class="meta">
            {escape(date_str)}
            <span class="sep">&middot;</span>
            Refreshing every {REFRESH_SECONDS}s
            <span class="sep">&middot;</span>
            Last updated {escape(updated_str)}
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def _render_staleness_banner() -> None:
    """Show a yellow banner above every page if any data snapshot is stale."""
    stale = check_dashboard_staleness()
    if not stale:
        return
    items = " &middot; ".join(
        f'<strong>{escape(c.label)}</strong> {c.age_hours:.1f}h old (threshold {c.threshold_hours}h)'
        for c in stale
    )
    st.markdown(
        f'<div class="gb-stale-banner">⚠ Stale data: {items}. '
        "Live snapshot refresh job may be down — check launchctl + recent logs."
        "</div>",
        unsafe_allow_html=True,
    )


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------


def main() -> None:
    _inject_css()

    pages, pages_by_url = _build_pages()

    # `position="hidden"` keeps Streamlit's built-in nav widget out of the
    # (removed) sidebar; the multipage router still works for path-based
    # navigation triggered by tile click-throughs and the back-home link.
    nav = st.navigation(pages, position="hidden")

    is_dashboard = nav is pages_by_url["dashboard"]
    if not is_dashboard:
        _render_back_home()
    _render_topbar(nav.title)
    _render_staleness_banner()

    nav.run()


if __name__ == "__main__":
    main()
