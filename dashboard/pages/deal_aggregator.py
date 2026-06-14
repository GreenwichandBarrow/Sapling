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

from collections import Counter, defaultdict
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
    DEAL_AGG_DIR,
    DealRow,
    ScanCoverage,
    _parse_frontmatter,
    _section,
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




# Markdown-table rows parsed from the deal-aggregator artifact. These are the
# skill's own review lanes, so the dashboard can help tune the skill without
# inventing a second classification system.

def _scan_artifact_paths(today: date, days: int) -> list[Path]:
    paths: list[Path] = []
    for offset in range(days):
        d = today.fromordinal(today.toordinal() - offset)
        for suffix in (".md", "-afternoon.md"):
            path = DEAL_AGG_DIR / f"deal-aggregator-scan-{d.isoformat()}{suffix}"
            if path.exists():
                paths.append(path)
    return paths


def _parse_md_table(section: str) -> list[dict[str, str]]:
    lines = [ln.strip() for ln in section.splitlines() if ln.strip().startswith("|")]
    if len(lines) < 2:
        return []
    headers = [h.strip() for h in lines[0].strip("|").split("|")]
    rows: list[dict[str, str]] = []
    for line in lines[2:]:
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < len(headers):
            cells += [""] * (len(headers) - len(cells))
        row = dict(zip(headers, cells[: len(headers)]))
        if any(row.values()):
            rows.append(row)
    return rows


def _strip_md_links(value: str) -> tuple[str, str | None]:
    m = __import__('re').search(r"\[([^\]]+)\]\(([^)]+)\)", value or "")
    if not m:
        return value or "", None
    return m.group(1), m.group(2)


def _load_artifact_tables(today: date, days: int) -> tuple[list[dict[str, str]], list[dict[str, str]], dict[str, str]]:
    listings: list[dict[str, str]] = []
    sources_by_name: dict[str, dict[str, str]] = {}
    summary: dict[str, str] = {}
    for path in _scan_artifact_paths(today, days):
        raw = path.read_text()
        fm, body = _parse_frontmatter(raw)
        for key in (
            "email_scan_status",
            "sources_scanned",
            "sources_blocked_verified",
            "sources_blocked_single_attempt",
            "deals_found",
            "broker_opportunistic",
        ):
            if key in fm and key not in summary:
                summary[key] = str(fm.get(key))
        listings.extend(_parse_md_table(_section(body, "Listings Reviewed")))
        for row in _parse_md_table(_section(body, "Source Scorecard")):
            name = row.get("Source", "").strip()
            if name and name not in sources_by_name:
                sources_by_name[name] = row
    return listings, list(sources_by_name.values()), summary


def _verdict_groups(listings: list[dict[str, str]]) -> tuple[list[dict[str, str]], list[dict[str, str]], list[dict[str, str]]]:
    surfaced = [r for r in listings if (r.get("Verdict") or "").upper() == "PASS"]
    learning = [r for r in listings if (r.get("Verdict") or "").upper() in {"BROKER-OPPORTUNISTIC", "NEAR-MISS", "FLAG"}]
    rejected = [r for r in listings if (r.get("Verdict") or "").upper() == "HARD-REJECT"]
    return surfaced, learning, rejected


def _render_run_status(summary: dict[str, str], listings: list[dict[str, str]], sources: list[dict[str, str]], coverage: ScanCoverage) -> str:
    surfaced, learning, rejected = _verdict_groups(listings)
    email_status = summary.get("email_scan_status", "unknown")
    blocked = sum(1 for s in sources if "blocked" in (s.get("Status", "").lower()))
    return dedent(f"""
    <div class="gb-deal-status-grid">
      <div><span class="num">{len(surfaced)}</span>surfaced matches</div>
      <div><span class="num" style="color: var(--yellow);">{len(learning)}</span>borderline / learning</div>
      <div><span class="num dim">{len(rejected)}</span>filtered out</div>
      <div><span class="num">{len(sources)}</span>sources reviewed</div>
      <div><span class="num {'green' if email_status == 'live' else ''}">{escape(email_status)}</span>email leg</div>
      <div><span class="num {'red' if blocked else 'dim'}">{blocked}</span>blocked sources</div>
    </div>
    """).strip()


def _deal_name_link(row: dict[str, str]) -> str:
    name, link = _strip_md_links(row.get("Headline", ""))
    if link:
        return f'<a class="gb-inline-link" href="{escape(link)}" target="_blank" rel="noreferrer noopener">{escape(name)}</a>'
    return escape(name or "—")


def _render_review_table(title: str, subtitle: str, rows: list[dict[str, str]], empty: str, limit: int | None = None) -> str:
    visible = rows[:limit] if limit else rows
    body = ""
    if visible:
        for row in visible:
            verdict = escape(row.get("Verdict", ""))
            why = row.get("Key Signals") or row.get("Reject Reason") or "—"
            body += dedent(f"""
            <tr>
              <td>{_source_cell(row.get('Source', '—'))}</td>
              <td><div class="gb-company compact">{_deal_name_link(row)}</div><div class="gb-industry-tag">{escape(row.get('Industry') or '—')}</div></td>
              <td class="gb-num">{escape(row.get('Revenue') or '—')}</td>
              <td class="gb-num">{escape(row.get('EBITDA') or '—')}</td>
              <td class="gb-num">{escape(row.get('Margin') or '—')}</td>
              <td>{escape(why)}</td>
              <td><span class="gb-status-badge {escape(verdict.lower().replace('-', ''))}">{verdict or '—'}</span></td>
            </tr>
            """).strip()
    else:
        body = f'<tr><td colspan="7"><div class="gb-empty">{escape(empty)}</div></td></tr>'
    more = ""
    if limit and len(rows) > limit:
        more = f'<div class="gb-section-footnote">+ {len(rows) - limit} more in raw intake archive</div>'
    return dedent(f"""
    <div class="gb-zone gb-zone-plain">
      <div class="gb-zone-head"><div><div class="gb-zone-label">{escape(title)}</div><div class="gb-zone-subtitle">{escape(subtitle)}</div></div><div class="gb-zone-meta">{len(rows)} items</div></div>
      <div class="gb-table-wrap"><table class="gb-table gb-review-table"><thead><tr><th>Source</th><th>Deal</th><th class="gb-num">Revenue</th><th class="gb-num">EBITDA</th><th class="gb-num">Margin</th><th>Why / reason</th><th>Lane</th></tr></thead><tbody>{body}</tbody></table></div>
      {more}
    </div>
    """).strip()


def _render_filtered_summary(rejected: list[dict[str, str]]) -> str:
    reasons = Counter((r.get("Reject Reason") or "Unspecified").strip() for r in rejected)
    industries = Counter((r.get("Industry") or "Unspecified").strip() for r in rejected)
    reason_html = "".join(f'<div><span class="num dim">{count}</span>{escape(reason)}</div>' for reason, count in reasons.most_common(4))
    industry_html = "".join(f'<span class="gb-chip">{escape(name)} <span>{count}</span></span>' for name, count in industries.most_common(8))
    if not rejected:
        reason_html = '<div class="gb-empty">No hard rejects captured in this window.</div>'
        industry_html = ""
    return dedent(f"""
    <div class="gb-zone gb-zone-plain">
      <div class="gb-zone-head"><div><div class="gb-zone-label">Filtered Out Summary</div><div class="gb-zone-subtitle">Default view shows rejection patterns, not every rejected listing</div></div><div class="gb-zone-meta">{len(rejected)} filtered</div></div>
      <div class="gb-reject-summary"><div>{reason_html}</div><div class="gb-chip-row">{industry_html}</div></div>
    </div>
    """).strip()


def _to_int(value: str | None) -> int:
    if not value:
        return 0
    digits = "".join(ch for ch in value if ch.isdigit())
    return int(digits or 0)


def _source_effectiveness(
    sources: list[dict[str, str]],
    listings: list[dict[str, str]],
) -> list[dict[str, str | int | float]]:
    rows: dict[str, dict[str, str | int | float]] = {}
    for source in sources:
        name = (source.get("Source") or "Unknown").strip()
        rows[name] = {
            "Source": name,
            "Category": source.get("Category") or "—",
            "Status": source.get("Status") or "—",
            "Reviewed": _to_int(source.get("Listings Reviewed")),
            "Surfaced": _to_int(source.get("Matches")),
            "Learning": 0,
            "Rejected": 0,
            "Last Match Date": source.get("Last Match Date") or "—",
        }

    for listing in listings:
        name = (listing.get("Source") or "Unknown").strip()
        row = rows.setdefault(
            name,
            {
                "Source": name,
                "Category": "—",
                "Status": "captured in listings",
                "Reviewed": 0,
                "Surfaced": 0,
                "Learning": 0,
                "Rejected": 0,
                "Last Match Date": "—",
            },
        )
        row["Reviewed"] = int(row["Reviewed"]) + 1
        verdict = (listing.get("Verdict") or "").upper()
        if verdict == "PASS":
            row["Surfaced"] = int(row["Surfaced"]) + 1
        elif verdict == "HARD-REJECT":
            row["Rejected"] = int(row["Rejected"]) + 1
        elif verdict in {"BROKER-OPPORTUNISTIC", "NEAR-MISS", "FLAG"}:
            row["Learning"] = int(row["Learning"]) + 1

    for row in rows.values():
        reviewed = int(row["Reviewed"])
        useful = int(row["Surfaced"]) + int(row["Learning"])
        row["Useful"] = useful
        row["Useful Rate"] = (useful / reviewed) if reviewed else 0.0

    return sorted(
        rows.values(),
        key=lambda r: (float(r["Useful Rate"]), int(r["Useful"]), int(r["Reviewed"])),
        reverse=True,
    )


def _render_source_effectiveness(sources: list[dict[str, str]], listings: list[dict[str, str]]) -> str:
    rows = _source_effectiveness(sources, listings)
    if not rows:
        body = '<tr><td colspan="8"><div class="gb-empty">No source effectiveness data captured in this window.</div></td></tr>'
    else:
        body = ""
        for row in rows:
            reviewed = int(row["Reviewed"])
            useful_rate = float(row["Useful Rate"])
            rate_text = f"{round(useful_rate * 100)}%" if reviewed else "—"
            if reviewed == 0:
                rate_class = "dim"
            elif useful_rate >= 0.20:
                rate_class = "green"
            elif useful_rate > 0:
                rate_class = "yellow"
            else:
                rate_class = "dim"
            body += dedent(
                f"""
                <tr>
                  <td>{_source_cell(str(row['Source']))}<div class="gb-source-detail">{escape(str(row['Category']))}</div></td>
                  <td>{escape(str(row['Status']))}</td>
                  <td class="gb-num">{reviewed}</td>
                  <td class="gb-num" style="color: var(--green);">{int(row['Surfaced'])}</td>
                  <td class="gb-num" style="color: var(--yellow);">{int(row['Learning'])}</td>
                  <td class="gb-num dim">{int(row['Rejected'])}</td>
                  <td class="gb-num {rate_class}">{rate_text}</td>
                  <td class="gb-source-detail">{escape(str(row['Last Match Date']))}</td>
                </tr>
                """
            ).strip()

    return dedent(
        f"""
        <div class="gb-zone gb-zone-plain">
          <div class="gb-zone-head">
            <div>
              <div class="gb-zone-label">Source Effectiveness</div>
              <div class="gb-zone-subtitle">Assesses whether each source is creating surfaced matches or useful learning, not just scan volume</div>
            </div>
            <div class="gb-zone-meta">{len(rows)} sources</div>
          </div>
          <div class="gb-table-wrap">
            <table class="gb-table gb-review-table">
              <thead><tr><th>Source</th><th>Status</th><th class="gb-num">Reviewed</th><th class="gb-num">Surfaced</th><th class="gb-num">Learning</th><th class="gb-num">Rejected</th><th class="gb-num">Useful rate</th><th>Last match</th></tr></thead>
              <tbody>{body}</tbody>
            </table>
          </div>
        </div>
        """
    ).strip()


def _source_category(source: str, raw_category: str) -> str:
    s = source.lower()
    if any(x in s for x in ("everingham", "benchmark", "viking", "searchfunder", "iag", "rejigg", "dealforce", "smb deal hunter")):
        return "Email newsletters / broker blasts"
    if any(x in s for x in ("bizbuysell", "business exits", "flippa", "quiet light", "website closers", "empire", "synergy")):
        return "Broker marketplaces"
    if raw_category.lower().startswith("niche") or any(x in s for x in ("sica", "pco", "marshberry", "agency")):
        return "Association / niche boards"
    return "Other sources"


def _render_sources_reviewed(sources: list[dict[str, str]]) -> str:
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in sources:
        grouped[_source_category(row.get("Source", ""), row.get("Category", ""))].append(row)
    body = ""
    for category in ("Email newsletters / broker blasts", "Broker marketplaces", "Association / niche boards", "Other sources"):
        rows = grouped.get(category, [])
        if not rows:
            continue
        body += f'<div class="gb-source-group"><div class="gb-source-group-title">{escape(category)}</div>'
        for row in rows:
            status = row.get("Status", "—")
            cls = "warn" if "blocked" in status.lower() else "ok"
            body += dedent(f"""
            <div class="gb-source-row">
              <div>{_source_cell(row.get('Source', '—'))}<div class="gb-source-detail">{escape(row.get('Category') or '—')}</div></div>
              <div><span class="gb-status-dot {cls}"></span>{escape(status)}</div>
              <div>{escape(row.get('Listings Reviewed') or '0')} reviewed</div>
              <div>{escape(row.get('Matches') or '0')} matches</div>
              <div class="gb-source-detail">last match {escape(row.get('Last Match Date') or '—')}</div>
            </div>
            """).strip()
        body += "</div>"
    if not body:
        body = '<div class="gb-empty">No source scorecard captured in this window.</div>'
    return dedent(f"""
    <div class="gb-zone gb-zone-plain">
      <div class="gb-zone-head"><div><div class="gb-zone-label">Sources Reviewed</div><div class="gb-zone-subtitle">Source coverage and source quality, grouped for skill improvement</div></div><div class="gb-zone-meta">{len(sources)} sources</div></div>
      {body}
    </div>
    """).strip()


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
    listings, sources, summary = _load_artifact_tables(today, days)
    surfaced, learning, rejected = _verdict_groups(listings)

    st.markdown(_render_run_status(summary, listings, sources, coverage), unsafe_allow_html=True)
    st.markdown(
        _render_review_table(
            "Surfaced Matches",
            "Deals the skill promoted as worth review now",
            surfaced,
            "No surfaced matches in this window. That may be correct, but the learning queue below is where we tune misses.",
        ),
        unsafe_allow_html=True,
    )
    st.markdown(
        _render_review_table(
            "Borderline / Learning Queue",
            "Promising, ambiguous, or off-thesis deals retained for calibration",
            learning,
            "No borderline deals captured in this window.",
            limit=12,
        ),
        unsafe_allow_html=True,
    )
    st.markdown(_render_filtered_summary(rejected), unsafe_allow_html=True)
    st.markdown(_render_source_effectiveness(sources, listings), unsafe_allow_html=True)
    st.markdown(_render_sources_reviewed(sources), unsafe_allow_html=True)

    n = len(filtered_rows)
    deal_word = "deal" if n == 1 else "deals"
    st.markdown(
        f'<div class="gb-zone gb-zone-plain gb-raw-archive">'
        f'<div class="gb-zone-head"><div><div class="gb-zone-label">Raw Intake Archive</div>'
        f'<div class="gb-zone-subtitle">Email inbound and parsed scan rows for audit, not the default work queue</div></div>'
        f'<div class="gb-zone-meta">{selected} · {n} {deal_word}</div></div>'
        f'{_render_table(filtered_rows, coverage)}'
        f'</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="gb-page-note">Skill improvement note: if Kay would have reviewed, requested a CIM, or signed an NDA for a borderline or filtered deal, that example should become Deal Aggregator calibration input. No emails are sent from this page.</div>',
        unsafe_allow_html=True,
    )
