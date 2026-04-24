"""Deal Aggregator page — businesses actively selling.

Reads `brain/context/deal-aggregator-scan-{date}.md` artifacts produced by the
deal-aggregator skill (morning + afternoon runs), flattens them into a single
table view, and renders the mockup-fidelity data-table pattern.

Scope notes:
- Source of truth: latest ~7 days of scan artifacts (plus today if present)
- Status column defaults to "New" — the artifact doesn't yet track review
  status; that wires in when Attio Intermediary Pipeline integration lands
  (Session 3, Deal Pipeline page)
- Filter bar renders for visual fidelity; interactive filtering is a later
  enhancement (kept out of Session 2 to honor the one-page-per-session rule)
"""

from __future__ import annotations

from datetime import date, datetime
from html import escape
from textwrap import dedent

import sys
from pathlib import Path

# Ensure sibling modules import cleanly when Streamlit runs page as a callable.
_DASHBOARD_DIR = Path(__file__).resolve().parent.parent
if str(_DASHBOARD_DIR) not in sys.path:
    sys.path.insert(0, str(_DASHBOARD_DIR))

from data_sources import (  # noqa: E402
    DealRow,
    _source_bucket,
    flatten_rows,
    load_recent_scans,
    load_scan,
)


# Default data window. 7 matches the "This week" tab label, but the real
# deal-aggregator surfaces ~0.14 deals/day — a 7-day window is often empty.
# Widening to 14 days lets Kay see actual rows render without waiting for a
# match inside the calendar week. Interactive time-tab filtering will clamp
# this properly in a later session.
WINDOW_DAYS = 14


def _dash(value: str | None) -> str:
    return escape(value) if value else '<span class="gb-num dim">&mdash;</span>'


def _source_cell(source: str) -> str:
    bucket = _source_bucket(source)
    return (
        f'<span class="gb-source-tag">'
        f'<span class="src-dot {bucket}"></span>{escape(source)}</span>'
    )


def _company_cell(row: DealRow) -> str:
    industry = (
        f'<div class="gb-industry-tag">{escape(row.industry)}</div>'
        if row.industry
        else ""
    )
    return f'<div class="gb-company">{escape(row.company)}</div>{industry}'


def _num_cell(value: str | None) -> str:
    if not value:
        return '<td class="gb-num dim">&mdash;</td>'
    return f'<td class="gb-num">{escape(value)}</td>'


def _status_cell(status: str) -> str:
    slug = status.lower().split()[0] if status else "new"
    return f'<td><span class="gb-status-badge {slug}">{escape(status)}</span></td>'


def _link_cell(link: str | None) -> str:
    if not link:
        return '<td class="gb-link-cell"></td>'
    return (
        f'<td class="gb-link-cell">'
        f'<a class="gb-link-icon" href="{escape(link)}" target="_blank" '
        f'rel="noreferrer noopener">&#x2197;</a></td>'
    )


def _render_row(row: DealRow) -> str:
    return dedent(
        f"""
        <tr>
        <td>{_source_cell(row.source)}</td>
        <td>{_company_cell(row)}</td>
        <td class="gb-owner">{_dash(row.owner)}</td>
        <td class="gb-location">{_dash(row.location)}</td>
        {_num_cell(row.revenue)}
        {_num_cell(row.ebitda)}
        {_num_cell(row.asking)}
        {_status_cell(row.status)}
        {_link_cell(row.link)}
        </tr>
        """
    ).strip()


def _render_empty() -> str:
    return (
        '<tr><td colspan="9">'
        '<div class="gb-empty">No deals surfaced in the last 7 days. '
        "Deal-aggregator scan is running on schedule; zero matches is the honest answer."
        "</div></td></tr>"
    )


def _render_subtitle(latest_run: str | None) -> str:
    suffix = (
        f' &nbsp;&middot;&nbsp; last scan <span class="highlight">{escape(latest_run)}</span>'
        if latest_run
        else ""
    )
    return (
        '<div class="gb-subtitle">'
        "Businesses actively selling &mdash; aggregated from broker platforms, "
        "email inbound, and association boards." + suffix + "</div>"
    )


def _render_summary(
    today_count: int, week_count: int, pursuing_count: int, awaiting_cim_count: int
) -> str:
    return dedent(
        f"""
        <div class="gb-summary">
        <div><span class="num">{today_count}</span>new today</div>
        <div><span class="num">{week_count}</span>this week</div>
        <div><span class="num">{pursuing_count}</span>pursuing</div>
        <div><span class="num">{awaiting_cim_count}</span>awaiting CIM</div>
        </div>
        """
    ).strip()


# Filter bar is visual-only in Session 2. Controls render identically to the
# mockup but do not mutate state — interactive filtering ships later.
def _render_filter_bar() -> str:
    return dedent(
        """
        <div class="gb-filter-bar">
        <div class="gb-filter-tabs">
        <button class="gb-filter-tab">Today</button>
        <button class="gb-filter-tab active">This week</button>
        <button class="gb-filter-tab">All</button>
        </div>
        <select class="gb-filter-select">
        <option>All sources</option>
        <option>BizBuySell</option>
        <option>Axial</option>
        <option>Email</option>
        <option>Association</option>
        <option>DealsX</option>
        </select>
        <select class="gb-filter-select">
        <option>All industries</option>
        <option>Insurance</option>
        <option>HVAC</option>
        <option>Art Storage</option>
        <option>MSP</option>
        <option>Equipment</option>
        </select>
        <select class="gb-filter-select">
        <option>All statuses</option>
        <option>New</option>
        <option>Reviewed</option>
        <option>Pursuing</option>
        <option>Passed</option>
        </select>
        <input class="gb-filter-search" type="text"
               placeholder="Search company, owner, industry..." />
        </div>
        """
    ).strip()


def _render_table(rows: list[DealRow]) -> str:
    body = (
        "".join(_render_row(r) for r in rows) if rows else _render_empty()
    )
    return dedent(
        f"""
        <div class="gb-table-wrap">
        <table class="gb-table">
        <thead>
        <tr>
        <th>Source</th>
        <th>Company</th>
        <th>Owner</th>
        <th>Location</th>
        <th class="gb-num">Revenue</th>
        <th class="gb-num">EBITDA</th>
        <th class="gb-num">Asking</th>
        <th>Status</th>
        <th class="gb-link-cell"></th>
        </tr>
        </thead>
        <tbody>{body}</tbody>
        </table>
        </div>
        """
    ).strip()


def render() -> None:
    import streamlit as st

    today = datetime.now().date()
    scans = load_recent_scans(today, WINDOW_DAYS)
    week_rows = flatten_rows(scans)
    today_scan = load_scan(today)
    today_rows = today_scan.rows if today_scan else []
    latest_run = today_scan.last_run if today_scan else (
        scans[0].last_run if scans else None
    )

    # Summary-strip rollups. "Pursuing" and "Awaiting CIM" aren't tracked in
    # the scan artifact — those fields land once Deal Pipeline (Session 3)
    # wires in Attio. Show 0 with an em-dash-style placeholder for now.
    st.markdown(_render_subtitle(latest_run), unsafe_allow_html=True)
    st.markdown(
        _render_summary(
            today_count=len(today_rows),
            week_count=len(week_rows),
            pursuing_count=0,
            awaiting_cim_count=0,
        ),
        unsafe_allow_html=True,
    )
    st.markdown(_render_filter_bar(), unsafe_allow_html=True)
    st.markdown(_render_table(week_rows), unsafe_allow_html=True)

    st.markdown(
        '<div class="gb-page-note">Rows parsed from '
        f"<code>brain/context/deal-aggregator-scan-*.md</code> across the last "
        f"{WINDOW_DAYS} days (wider than the \"this week\" tab so real rows "
        "render given the current 0.14/day volume). Filter controls are "
        "visual-only in Session 2. Pursuing / Awaiting-CIM counts wire in "
        "once Deal Pipeline (Session 3) reads Attio.</div>",
        unsafe_allow_html=True,
    )
