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
from datetime import date, datetime, timedelta
from html import escape
from textwrap import dedent

import json
import sys
from pathlib import Path

# Ensure sibling modules import cleanly when Streamlit runs page as a callable.
_DASHBOARD_DIR = Path(__file__).resolve().parent.parent
if str(_DASHBOARD_DIR) not in sys.path:
    sys.path.insert(0, str(_DASHBOARD_DIR))

from data_sources import (  # noqa: E402
    DEAL_AGG_DIR,
    ScanCoverage,
    _parse_frontmatter,
    _section,
    coverage_summary,
    load_recent_scans,
    load_scan,
)


# Default data window. 7 matches the "This week" tab label, but the real
# deal-aggregator surfaces ~0.14 deals/day — a 7-day window is often empty.
# Widening to 14 days lets Kay see actual rows render without waiting for a
# match inside the calendar week. Interactive time-tab filtering will clamp
# this properly in a later session.
WINDOW_DAYS = 14


NEWSLETTER_SOURCE_ROSTER = (
    "BizBuySell",
    "BizQuest",
    "BizScout",
    "Business Exits",
    "Calder Capital",
    "DealForce",
    "Everingham & Kerr",
    "Rejigg",
    "Transworld Business Advisors",
    "Viking Mergers",
    "Axial",
    "Baton",
)

DIRECT_EMAIL_SOURCE_ROSTER = (
    "Benchmark International",
    "Eric Mendelson",
    "Bob Williamson / Cetane",
    "Matt Luczyk / Peapack",
    "Richard / Stone Hill Advisors",
    "Carlos / In3O",
    "IAG M&A Advisors",
    "DealsX replies",
)

# Marketplace sources Kay may need to check manually. SaaS/paywall sources stay
# hidden unless Kay reactivates them.
MANUAL_MARKETPLACE_SOURCE_ROSTER = (
    "DealMatch",
    "Searchfunder",
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


def _source_display_name(source: str) -> str:
    value = (source or "").strip()
    lower = value.lower()
    if not value:
        return ""
    alias_groups = (
        (("transworld",), "Transworld Business Advisors"),
        (("bizbuysell",), "BizBuySell"),
        (("everingham", "everkerr"), "Everingham & Kerr"),
        (("flippa",), "Flippa"),
        (("quiet light", "quietlight"), "Quiet Light"),
        (("website closers", "websiteclosers"), "Website Closers"),
        (("smb deal hunter", "helen guo"), "SMB Deal Hunter (Helen Guo)"),
        (("axial",), "Axial"),
        (("calder",), "Calder Capital"),
        (("benchmark",), "Benchmark International"),
        (("cetane", "bob williamson"), "Bob Williamson / Cetane"),
        (("peapack", "peapackprivate", "matt luczyk", "lisa mcknight", "lmcknight", "raymond radigan", "rradigan"), "Matt Luczyk / Peapack"),
        (("stone hill", "stony hill"), "Richard / Stone Hill Advisors"),
        (("eric mendelson", "mendelson"), "Eric Mendelson"),
        (("bizquest",), "BizQuest"),
        (("bizscout", "dealos"), "BizScout"),
        (("dealmatch", "deal match"), "DealMatch"),
        (("searchfunder", "search funder"), "Searchfunder"),
        (("business exits",), "Business Exits"),
        (("rejigg",), "Rejigg"),
        (("dealforce", "generational"), "DealForce"),
        (("baton",), "Baton"),
        (("prospect geni", "dealsx", "lead interested"), "DealsX replies"),
        (("carlos", "carlo", "in3o"), "Carlos / In3O"),
        (("greenwichandbarrow", "meet-greenwichandbarrow", "txt.voice.google", "google voice"), "Internal / non-source"),
        (("email channel",), "Direct deal email"),
    )
    for needles, display in alias_groups:
        if any(needle in lower for needle in needles):
            return display
    return value


def _safe_int(value: str | None) -> int:
    try:
        return int(str(value or "0").replace(",", "").strip() or "0")
    except ValueError:
        return 0


def _is_paused_source(name: str) -> bool:
    lowered = (name or "").strip().lower()
    return any(paused == lowered or paused in lowered for paused in PAUSED_SOURCE_NAMES)


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
            name = _source_display_name(row.get("Source", ""))
            if name and name.lower() not in sources_by_name:
                row = dict(row)
                row["Source"] = name
                sources_by_name[name.lower()] = row

    inferred_sources: dict[str, dict[str, int]] = {}
    for row in listings:
        name = _source_display_name(row.get("Source", ""))
        if not name:
            continue
        stats = inferred_sources.setdefault(name, {"reviewed": 0, "matches": 0})
        stats["reviewed"] += 1
        if (row.get("Verdict") or "").upper() == "PASS":
            stats["matches"] += 1

    for name, stats in inferred_sources.items():
        key = name.lower()
        existing = sources_by_name.get(key)
        if existing:
            existing["Listings Reviewed"] = str(_safe_int(existing.get("Listings Reviewed")) + stats["reviewed"])
            existing["Matches"] = str(_safe_int(existing.get("Matches")) + stats["matches"])
            if (existing.get("Category") or "").strip().lower() in {"", "general"}:
                existing["Category"] = _source_category(name, "Newsletter")
            if (existing.get("HTTP") or "").strip().lower() in {"", "—", "-", "403", "404"}:
                existing["HTTP"] = "email"
            if "blocked" in (existing.get("Status") or "").lower() and not _is_paused_source(name):
                existing["Status"] = "active"
            continue
        sources_by_name[key] = {
            "Source": name,
            "Category": _source_category(name, "Newsletter"),
            "Status": "active",
            "HTTP": "email",
            "Listings Reviewed": str(stats["reviewed"]),
            "Matches": str(stats["matches"]),
            "Last Match Date": "-",
        }

    for name in NEWSLETTER_SOURCE_ROSTER:
        key = name.lower()
        if key not in sources_by_name:
            sources_by_name[key] = {
                "Source": name,
                "Category": "Newsletter",
                "Status": "active",
                "HTTP": "email",
                "Listings Reviewed": "0",
                "Matches": "0",
                "Last Match Date": "-",
            }

    for name in DIRECT_EMAIL_SOURCE_ROSTER:
        key = name.lower()
        if key not in sources_by_name:
            sources_by_name[key] = {
                "Source": name,
                "Category": "Direct email",
                "Status": "active",
                "HTTP": "email",
                "Listings Reviewed": "0",
                "Matches": "0",
                "Last Match Date": "-",
            }

    for name in MANUAL_MARKETPLACE_SOURCE_ROSTER:
        key = name.lower()
        if key not in sources_by_name:
            sources_by_name[key] = {
                "Source": name,
                "Category": "Marketplace",
                "Status": "manual",
                "Access": "manual",
                "HTTP": "manual",
                "Listings Reviewed": "0",
                "Matches": "0",
                "Last Match Date": "-",
            }

    return listings, list(sources_by_name.values()), summary


def _verdict_groups(listings: list[dict[str, str]]) -> tuple[list[dict[str, str]], list[dict[str, str]], list[dict[str, str]]]:
    surfaced = [r for r in listings if (r.get("Verdict") or "").upper() == "PASS"]
    learning = [r for r in listings if (r.get("Verdict") or "").upper() in {"BROKER-OPPORTUNISTIC", "NEAR-MISS", "FLAG"}]
    rejected = [r for r in listings if (r.get("Verdict") or "").upper() == "HARD-REJECT"]
    return surfaced, learning, rejected


PAUSED_SOURCE_NAMES = {
    "flippa",
    "quiet light",
    "quietlight",
    "website closers",
    "websiteclosers",
    "smb deal hunter (helen guo)",
    "empire flippers",
    "gp bullhound",
    "pco bookkeepers",
    "sica fletcher",
    "synergy business brokers",
    "synergy business brokers real estate",
    # Generic email rows are attribution failures, not source names for Kay.
    "direct deal email",
    "internal / non-source",
    "greenwichandbarrow",
    "meet-greenwichandbarrow",
    "txt.voice.google",
    "google voice",
}


def _is_active_source_for_dashboard(row: dict[str, str]) -> bool:
    name = (row.get("Source") or "").strip().lower()
    status = (row.get("Status") or "").strip().lower()
    if not name:
        return False
    if any(term in status for term in ("dormant", "paused", "paywalled")):
        return False
    if _is_paused_source(name):
        return False
    return True


def _source_channel(source: str, raw_category: str = "") -> str:
    s = source.lower()
    category = raw_category.lower()

    # Direct email = an intermediary/contact/broker email addressed to Kay with
    # a particular deal reference, not a saved-search or bulk newsletter feed.
    direct_email_terms = (
        "benchmark",
        "bob williamson",
        "cetane",
        "carlos",
        "eric mendelson",
        "in3o",
        "matt luczyk",
        "mendelson",
        "peapack",
        "richard / stone hill",
        "iag",
        "stone hill",
        "stony hill",
        "woodbridge",
        "pronova",
        "dealsx replies",
        "direct deal email",
    )
    newsletter_terms = (
        "axial",
        "baton",
        "bizbuysell",
        "bizquest",
        "business exits",
        "calder",
        "dealforce",
        "everingham",
        "everkerr",
        "generational",
        "rejigg",
        "searchfunder",
        "smb deal hunter",
        "transworld",
        "viking",
    )
    profile_backed_newsletter_terms = ("baton", "bizquest", "bizscout")
    if any(term in s for term in profile_backed_newsletter_terms):
        return "newsletter"
    if "marketplace" in category and not any(term in category for term in ("email", "newsletter", "saved search")):
        return "marketplace"
    if "direct email" in category or "email-only" in category or "direct" in category or any(term in s for term in direct_email_terms):
        return "direct_email"
    if "newsletter" in category or "saved search" in category or any(term in s for term in newsletter_terms):
        return "newsletter"
    return "marketplace"

def _source_channel_counts(sources: list[dict[str, str]]) -> Counter[str]:
    counts: Counter[str] = Counter()
    seen: set[str] = set()
    for row in sources:
        if not _is_active_source_for_dashboard(row) or _source_requires_manual_search(row):
            continue
        name = (row.get("Source") or "").strip()
        if not name or name.lower() in seen:
            continue
        seen.add(name.lower())
        counts[_source_channel(name, row.get("Category", ""))] += 1
    return counts


def _artifact_date_from_path(path: Path) -> date | None:
    try:
        return date.fromisoformat(
            path.name.replace("deal-aggregator-scan-", "")
            .replace("-afternoon", "")
            .replace(".md", "")
        )
    except ValueError:
        return None


def _activity_bucket(activity: dict[str, dict[str, int]], name: str) -> dict[str, int]:
    return activity.setdefault(
        name.lower(),
        {
            "week_reviewed": 0,
            "week_matches": 0,
            "month_reviewed": 0,
            "month_matches": 0,
        },
    )


def _bump_activity(
    activity: dict[str, dict[str, int]],
    name: str,
    artifact_date: date,
    week_start: date,
    month_start: date,
    *,
    is_match: bool = False,
) -> None:
    if not name:
        return
    bucket = _activity_bucket(activity, name)
    if artifact_date >= week_start:
        bucket["week_reviewed"] += 1
        if is_match:
            bucket["week_matches"] += 1
    if artifact_date >= month_start:
        bucket["month_reviewed"] += 1
        if is_match:
            bucket["month_matches"] += 1


def _email_input_paths(today: date, days: int) -> list[Path]:
    paths: list[Path] = []
    for offset in range(days):
        d = today.fromordinal(today.toordinal() - offset)
        path = DEAL_AGG_DIR / f"email-intelligence-input-{d.isoformat()}.json"
        if path.exists():
            paths.append(path)
    return paths


def _email_artifact_date(path: Path) -> date | None:
    try:
        return date.fromisoformat(path.name.replace("email-intelligence-input-", "").replace(".json", ""))
    except ValueError:
        return None


def _email_record_text(record: dict) -> str:
    parts: list[str] = []
    for key in ("from", "to", "cc", "bcc", "subject", "snippet", "summary", "text", "body", "labels", "labelIds"):
        value = record.get(key)
        if value is not None:
            parts.append(str(value))
    for msg in record.get("messages", []) if isinstance(record.get("messages"), list) else []:
        if isinstance(msg, dict):
            parts.append(_email_record_text(msg))
    return " ".join(parts)


def _email_records(data: dict) -> list[dict]:
    rows: list[dict] = []
    for section in ("inbound", "outbound", "candidate_threads"):
        for record in data.get(section, []) if isinstance(data.get(section), list) else []:
            if isinstance(record, dict):
                rows.append(record)
    return rows


def _add_direct_email_activity(
    activity: dict[str, dict[str, int]],
    today: date,
    lookback_days: int,
    week_start: date,
    month_start: date,
) -> None:
    seen: set[tuple[str, str, str]] = set()
    direct_names = {name.lower() for name in DIRECT_EMAIL_SOURCE_ROSTER}
    for path in _email_input_paths(today, lookback_days):
        artifact_date = _email_artifact_date(path)
        if artifact_date is None:
            continue
        try:
            data = json.loads(path.read_text())
        except (OSError, json.JSONDecodeError):
            continue
        for record in _email_records(data):
            text = _email_record_text(record)
            name = _source_display_name(text)
            if name.lower() not in direct_names:
                continue
            # Count each source/thread/day once across inbound/outbound mirrors.
            record_id = str(record.get("threadId") or record.get("thread_id") or record.get("id") or record.get("subject") or text[:120])
            key = (path.name, name.lower(), record_id)
            if key in seen:
                continue
            seen.add(key)
            _bump_activity(activity, name, artifact_date, week_start, month_start)


def _source_window_activity(today: date) -> dict[str, dict[str, int]]:
    activity: dict[str, dict[str, int]] = {}
    month_start = today.replace(day=1)
    lookback_days = max((today - month_start).days + 1, 7)
    week_start = today - timedelta(days=6)

    for path in _scan_artifact_paths(today, lookback_days):
        artifact_date = _artifact_date_from_path(path)
        if artifact_date is None:
            continue
        raw = path.read_text()
        _fm, body = _parse_frontmatter(raw)
        for listing in _parse_md_table(_section(body, "Listings Reviewed")):
            name = _source_display_name(listing.get("Source", ""))
            if not name:
                continue
            is_match = (listing.get("Verdict") or "").upper() == "PASS"
            _bump_activity(activity, name, artifact_date, week_start, month_start, is_match=is_match)

    _add_direct_email_activity(activity, today, lookback_days, week_start, month_start)
    return activity


def _apply_source_window_activity(sources: list[dict[str, str]], activity: dict[str, dict[str, int]]) -> None:
    for row in sources:
        name = _source_display_name(row.get("Source", ""))
        stats = activity.get(name.lower(), {})
        row["This Week Reviewed"] = str(stats.get("week_reviewed", 0))
        row["This Week Matches"] = str(stats.get("week_matches", 0))
        row["This Month Reviewed"] = str(stats.get("month_reviewed", 0))
        row["This Month Matches"] = str(stats.get("month_matches", 0))


def _render_run_status(summary: dict[str, str], listings: list[dict[str, str]], sources: list[dict[str, str]], coverage: ScanCoverage) -> str:
    surfaced, learning, rejected = _verdict_groups(listings)
    filtered_count = len(learning) + len(rejected)
    active_sources = [row for row in sources if _is_active_source_for_dashboard(row) and not _source_requires_manual_search(row)]
    source_counts = _source_channel_counts(sources)
    return dedent(f"""
    <div class="gb-deal-status-grid">
      <div><span class="num">{len(surfaced)}</span>matches</div>
      <div><span class="num dim">{filtered_count}</span>filtered out</div>
      <div><span class="num">{len(active_sources)}</span>sources checked<div class="gb-source-detail">{source_counts['marketplace']} marketplaces &middot; {source_counts['newsletter']} newsletters &middot; {source_counts['direct_email']} direct emails</div></div>
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
              <td>{escape(row.get('Source', '—'))}</td>
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
        more = f'<div class="gb-section-footnote">+ {len(rows) - limit} more</div>'
    return dedent(f"""
    <div class="gb-zone gb-zone-plain">
      <div class="gb-zone-head"><div><div class="gb-zone-label">{escape(title)}</div><div class="gb-zone-subtitle">{escape(subtitle)}</div></div><div class="gb-zone-meta">{len(rows)} items</div></div>
      <div class="gb-table-wrap"><table class="gb-table gb-review-table"><thead><tr><th>Source</th><th>Deal</th><th class="gb-num">Revenue</th><th class="gb-num">EBITDA</th><th class="gb-num">Margin</th><th>Why / reason</th><th>Lane</th></tr></thead><tbody>{body}</tbody></table></div>
      {more}
    </div>
    """).strip()



def _source_category(source: str, raw_category: str) -> str:
    channel = _source_channel(source, raw_category)
    if channel == "direct_email":
        return "Direct email"
    if channel == "newsletter":
        return "Newsletter"
    return "Marketplace"


def _source_is_manual_marketplace(row: dict[str, str]) -> bool:
    return _source_channel(row.get("Source", ""), row.get("Category", "")) == "marketplace"

def _source_requires_manual_search(row: dict[str, str]) -> bool:
    status = (row.get("Status") or "").strip().lower()
    access = (row.get("Access") or "").strip().lower()
    source = (row.get("Source") or "").strip().lower()
    if not source or _is_paused_source(source):
        return False
    if any(term in status for term in ("dormant", "paused", "paywalled")):
        return False
    if not _source_is_manual_marketplace(row):
        return False
    manual_terms = (
        "pending",
        "need to register",
        "login-gated",
        "manual",
        "setup",
    )
    return any(term in status for term in manual_terms) or any(term in access for term in manual_terms)

def _source_is_automated_run_coverage(row: dict[str, str]) -> bool:
    return _is_active_source_for_dashboard(row) and not _source_requires_manual_search(row)


def _render_source_rows(rows: list[dict[str, str]]) -> str:
    body = ""
    for row in rows:
        status = row.get("Status", "—")
        status_lower = status.lower()
        cls = "warn" if any(term in status_lower for term in ("blocked", "pending", "login", "manual", "few public", "no public")) else "ok"
        body += dedent(f"""
        <div class="gb-source-row gb-source-row-coverage">
          <div>{escape(row.get('Source', '—'))}<div class="gb-source-detail">{escape(_source_category(row.get('Source', ''), row.get('Category', '')))}</div></div>
          <div><span class="gb-status-dot {cls}"></span>{escape(status)}</div>
          <div><span class="gb-source-detail">this week</span><br>{escape(row.get('This Week Reviewed') or '0')} reviewed &middot; {escape(row.get('This Week Matches') or '0')} matches</div>
          <div><span class="gb-source-detail">this month</span><br>{escape(row.get('This Month Reviewed') or '0')} reviewed &middot; {escape(row.get('This Month Matches') or '0')} matches</div>
        </div>
        """).strip()
    return body


def _render_sources_reviewed(sources: list[dict[str, str]]) -> str:
    eligible_sources = [row for row in sources if _is_active_source_for_dashboard(row)]
    automated_sources = [row for row in eligible_sources if _source_is_automated_run_coverage(row)]
    manual_sources = [row for row in eligible_sources if _source_requires_manual_search(row)]

    automated_grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in automated_sources:
        automated_grouped[_source_category(row.get("Source", ""), row.get("Category", ""))].append(row)

    body = ""
    if automated_sources:
        body += '<div class="gb-source-group"><div class="gb-source-group-title">Automated run coverage</div>'
        for category in ("Marketplace", "Newsletter", "Direct email"):
            rows = automated_grouped.get(category, [])
            if not rows:
                continue
            body += f'<div class="gb-source-group-title gb-source-subgroup-title">{escape(category)}</div>'
            body += _render_source_rows(rows)
        body += "</div>"

    if manual_sources:
        body += '<div class="gb-source-group"><div class="gb-source-group-title">Manual deal sources to aggregate</div>'
        body += _render_source_rows(manual_sources)
        body += "</div>"

    if not body:
        body = '<div class="gb-empty">No source scorecard captured in this window.</div>'
    return dedent(f"""
    <div class="gb-zone gb-zone-plain">
      <div class="gb-zone-head"><div><div class="gb-zone-label">Source Coverage</div><div class="gb-zone-subtitle">Sources the skill reviews when it runs, plus marketplace sources that still require manual aggregation</div></div><div class="gb-zone-meta">{len(automated_sources)} automated · {len(manual_sources)} manual</div></div>
      {body}
    </div>
    """).strip()



# Interactive time filter — maps pill label → window-days lookback.
# "All" uses the full WINDOW_DAYS; smaller windows narrow the row set.
_TIME_FILTER_DAYS = {"Today": 1, "This week": 7, "All": WINDOW_DAYS}
_DEFAULT_TIME_FILTER = "This week"


def render() -> None:
    import streamlit as st

    today = datetime.now().date()
    scans = load_recent_scans(today, WINDOW_DAYS)
    today_scan = load_scan(today)
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
    listings, sources, summary = _load_artifact_tables(today, days)
    _apply_source_window_activity(sources, _source_window_activity(today))
    surfaced, learning, rejected = _verdict_groups(listings)

    st.markdown(_render_run_status(summary, listings, sources, coverage), unsafe_allow_html=True)
    st.markdown(
        _render_review_table(
            "Matches",
            "Deals the skill promoted as worth review now",
            surfaced,
            "No matches in this window. That may be correct.",
        ),
        unsafe_allow_html=True,
    )
    st.markdown(_render_sources_reviewed(sources), unsafe_allow_html=True)

    st.markdown(
        '<div class="gb-page-note">Skill improvement note: if Kay would have reviewed, requested a CIM, or signed an NDA for a filtered deal, that example should become Deal Aggregator calibration input. No emails are sent from this page.</div>',
        unsafe_allow_html=True,
    )
