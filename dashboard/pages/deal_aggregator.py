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
    ScanCoverage,
    _source_bucket,
    coverage_summary,
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


def _render_empty(coverage: ScanCoverage | None = None) -> str:
    """Empty state that explains *why* it's empty.

    Three cases:
      1. No coverage object → fall back to the legacy single-line message.
      2. Some scans read, no missing slots → genuinely-zero-deals (honest scan).
      3. Scans read but slots missing → coverage gap, surface which slots.
    """
    if coverage is None:
        body = (
            "No deals surfaced in the last 7 days. Deal-aggregator scan is "
            "running on schedule; zero matches is the honest answer."
        )
    else:
        lines: list[str] = []
        # Lead line — match-count framing.
        lines.append(
            f"<strong>0 deals</strong> across "
            f"<strong>{coverage.scans_read} scan{'s' if coverage.scans_read != 1 else ''}</strong> "
            f"in the last 7 days."
        )
        if coverage.last_successful:
            lines.append(
                f"Last successful scan: <span class='highlight'>{escape(coverage.last_successful)}</span>."
            )
        # Coverage gaps — only surface if any.
        if coverage.missing_slots:
            missed = ", ".join(escape(s) for s in coverage.missing_slots)
            lines.append(
                f"Missing slots: <span style='color: var(--yellow);'>{missed}</span>."
            )
            lines.append(
                "Weekend mornings don't run by design (Mon-Fri 6am + 2pm only). "
                "Weekday gaps are scheduled-skill misfires — separate fix from the dashboard."
            )
        else:
            lines.append(
                "All weekday slots covered. Zero matches is the honest answer — "
                "luxury-service niches flow through specialty channels and proprietary "
                "outbound, not general broker platforms."
            )
        body = "<br/>".join(lines)
    return (
        '<tr><td colspan="9">'
        f'<div class="gb-empty">{body}</div>'
        "</td></tr>"
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
    """Match mockup-deal-aggregator.html number colors:
    - new today: green when >0, dim when 0
    - this week: default text
    - pursuing: yellow when >0, dim when 0
    - awaiting CIM: yellow when >0, dim when 0
    """
    today_color = "var(--green)" if today_count else "var(--text-dim)"
    pursuing_color = "var(--yellow)" if pursuing_count else "var(--text-dim)"
    cim_color = "var(--yellow)" if awaiting_cim_count else "var(--text-dim)"
    return dedent(
        f"""
        <div class="gb-summary">
        <div><span class="num" style="color:{today_color};">{today_count}</span>new today</div>
        <div><span class="num">{week_count}</span>this week</div>
        <div><span class="num" style="color:{pursuing_color};">{pursuing_count}</span>pursuing</div>
        <div><span class="num" style="color:{cim_color};">{awaiting_cim_count}</span>awaiting CIM</div>
        </div>
        """
    ).strip()


# Visual stub — dropdowns + search render but don't filter. Time tabs are
# now interactive via st.segmented_control above this row (see render()).
def _render_filter_bar_stubs() -> str:
    return dedent(
        """
        <div class="gb-filter-bar" style="border-bottom: none; padding-bottom: 0; margin-bottom: 16px;">
        <select class="gb-filter-select"><option>All sources</option></select>
        <select class="gb-filter-select"><option>All industries</option></select>
        <select class="gb-filter-select"><option>All statuses</option></select>
        <input class="gb-filter-search" type="text" placeholder="Search company, owner, industry..." />
        </div>
        """
    ).strip()


# Original visual-only filter bar — kept for reference. Replaced by
# segmented_control + _render_filter_bar_stubs.
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


def _render_table(rows: list[DealRow], coverage: ScanCoverage | None = None) -> str:
    body = (
        "".join(_render_row(r) for r in rows) if rows else _render_empty(coverage)
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


# Interactive time filter — maps pill label → window-days lookback.
# "All" uses the full WINDOW_DAYS; smaller windows narrow the row set.
_TIME_FILTER_DAYS = {"Today": 1, "This week": 7, "All": WINDOW_DAYS}
_DEFAULT_TIME_FILTER = "This week"


def render() -> None:
    import streamlit as st

    today = datetime.now().date()
    # Always load the full window so filter pills can narrow without re-fetch.
    scans = load_recent_scans(today, WINDOW_DAYS)
    all_rows = flatten_rows(scans)
    today_scan = load_scan(today)
    today_rows = today_scan.rows if today_scan else []
    week_rows = [r for r in all_rows if (today - r.scan_date).days < 7]
    latest_run = today_scan.last_run if today_scan else (
        scans[0].last_run if scans else None
    )
    # 7-day coverage summary — used to explain empty states honestly.
    coverage = coverage_summary(today, days=7)

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

    # Interactive time filter via segmented_control. Label hidden via
    # label_visibility so the row reads as a clean pill bar matching mockup.
    selected = st.segmented_control(
        "Time window",
        options=list(_TIME_FILTER_DAYS.keys()),
        default=_DEFAULT_TIME_FILTER,
        key="deal_agg_time_filter",
        label_visibility="collapsed",
    ) or _DEFAULT_TIME_FILTER
    days = _TIME_FILTER_DAYS[selected]
    filtered_rows = [r for r in all_rows if (today - r.scan_date).days < days]

    st.markdown(_render_filter_bar_stubs(), unsafe_allow_html=True)
    st.markdown(_render_table(filtered_rows, coverage), unsafe_allow_html=True)

    st.markdown(
        '<div class="gb-page-note">Scan source: morning + afternoon '
        "broker-platform sweeps (Mon-Fri 6am + 2pm), email inbound, and "
        "association deal boards. Time filter interactive (Today / This week / "
        "All); source / industry / status dropdowns + search are visual stubs "
        "pending interactive build."
        "</div>",
        unsafe_allow_html=True,
    )
