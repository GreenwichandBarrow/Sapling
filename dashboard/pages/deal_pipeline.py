"""Active Deal Pipeline page — NDA-forward conversations only.

Reads `brain/context/attio-pipeline-snapshot.json` — a point-in-time snapshot
of Attio's "Active Deals - Owners" list — and filters to NDA-forward stages
(NDA, Financials Received, Submitted LOI, Signed LOI). Identified + Contacted
moved to M&A Analytics on 2026-04-24 because DealsX-driven cold outreach will
push those columns into the thousands and turn the page into a funnel report.

Cards now carry:
- Category color chip (insurance/fine-art/shipping/consulting/other)
- Stage-age severity dot (green <14d / yellow 14–30d / red >30d)
- Last-touch days

Each column header carries a thin proportion bar showing what share of the
active pipeline lives at that stage — instant read on bottlenecks.

Closed strip below renders the terminal Attio stage. Pre-NDA outreach
attrition is intermixed in `closed_count` until the snapshot writer is
enhanced to split post-NDA failures separately.
"""

from __future__ import annotations

from datetime import date, datetime, timedelta, timezone
from html import escape
from textwrap import dedent

import sys
from pathlib import Path

_DASHBOARD_DIR = Path(__file__).resolve().parent.parent
if str(_DASHBOARD_DIR) not in sys.path:
    sys.path.insert(0, str(_DASHBOARD_DIR))

from data_sources import (  # noqa: E402
    ClosedDealStub,
    PipelineDeal,
    PipelineSnapshot,
    load_pipeline,
)


def _parse_iso(ts: str | None) -> datetime | None:
    if not ts:
        return None
    # Python <3.11 chokes on trailing Z; normalize to +00:00 offset.
    s = ts.replace("Z", "+00:00")
    try:
        return datetime.fromisoformat(s)
    except ValueError:
        return None


def _days_since(ts: str | None) -> int | None:
    dt = _parse_iso(ts)
    if not dt:
        return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return (datetime.now(timezone.utc) - dt).days


# Category → CSS modifier on .gb-cat. Chips color-coded so the board scans
# as "where are my insurance deals?" at a glance.
_CATEGORY_BUCKETS = {
    "insurance": "insurance",
    "fine art": "fineart",
    "shipping": "shipping",
    "logistics": "shipping",
    "consulting": "consulting",
    "professional services": "consulting",
}


def _category_bucket(category: str | None) -> str:
    if not category:
        return "other"
    low = category.lower()
    for needle, bucket in _CATEGORY_BUCKETS.items():
        if needle in low:
            return bucket
    return "other"


def _age_severity(days: int | None) -> str:
    """green <14d, yellow 14–30d, red >30d (matches mockup heuristic)."""
    if days is None:
        return "grey"
    if days < 14:
        return "green"
    if days <= 30:
        return "yellow"
    return "red"


def _last_touch_text(deal: PipelineDeal) -> str:
    days = _days_since(deal.last_interaction)
    if days is None:
        return "no contact yet"
    if days <= 0:
        return "last touch today"
    if days == 1:
        return "last touch 1d"
    return f"last touch {days}d"


def _card_meta(deal: PipelineDeal) -> str:
    parts: list[str] = []
    if deal.location:
        parts.append(escape(deal.location))
    if deal.employee_range:
        parts.append(f"{escape(deal.employee_range)} emp")
    if deal.arr_bucket:
        parts.append(escape(deal.arr_bucket))
    return '<span class="sep">&middot;</span>'.join(parts)


def _render_card(deal: PipelineDeal) -> str:
    days = _days_since(deal.stage_since)
    age = _age_severity(days)
    stage_text = f"In stage {days}d" if days is not None else ""
    cat_bucket = _category_bucket(deal.category)
    cat_chip = (
        f'<span class="gb-cat {cat_bucket}">{escape(deal.category)}</span>'
        if deal.category
        else ""
    )
    return dedent(
        f"""
        <a class="gb-kanban-card" href="{escape(deal.attio_url)}"
           target="_blank" rel="noreferrer noopener">
        <div class="company">{escape(deal.company)}</div>
        {cat_chip}
        <div class="meta">{_card_meta(deal)}</div>
        <div class="footer">
        <span class="age"><span class="age-dot {age}"></span>{escape(stage_text)}</span>
        <span class="last-touch">{escape(_last_touch_text(deal))}</span>
        </div>
        </a>
        """
    ).strip()


def _render_column(stage: str, deals: list[PipelineDeal], total: int) -> str:
    """`total` = total deals across all active stages — used for proportion bar."""
    if deals:
        cards = "".join(_render_card(d) for d in deals)
    else:
        cards = '<div class="gb-kanban-col-empty">No deals at this stage.</div>'

    if total > 0:
        pct = round(100 * len(deals) / total)
    else:
        pct = 0
    fill_class = "gb-kanban-bar-fill"
    if pct == 0:
        fill_class += " empty"
    dot_class = "green" if deals else "grey"

    return dedent(
        f"""
        <div class="gb-kanban-col">
        <div class="gb-kanban-col-header">
        <span class="gb-kanban-col-name">{escape(stage)}</span>
        <span class="gb-kanban-col-count">
        <span class="gb-kanban-col-dot {dot_class}"></span>
        <span class="n">{len(deals)}</span>
        </span>
        </div>
        <div class="gb-kanban-bar"><div class="{fill_class}" style="width: {pct}%"></div></div>
        <div class="gb-kanban-cards">{cards}</div>
        </div>
        """
    ).strip()


def _render_kanban(snapshot: PipelineSnapshot) -> str:
    by_stage: dict[str, list[PipelineDeal]] = {s: [] for s in snapshot.stages}
    for deal in snapshot.deals:
        if deal.stage in by_stage:
            by_stage[deal.stage].append(deal)
    # Sort each column most-recently-moved first; freshest deals surface at the
    # top of their column instead of oldest-first.
    for stage in by_stage:
        by_stage[stage].sort(key=lambda d: d.stage_since, reverse=True)
    total = sum(len(v) for v in by_stage.values())
    cols = "".join(_render_column(s, by_stage[s], total) for s in snapshot.stages)
    return f'<div class="gb-kanban-wrap"><div class="gb-kanban">{cols}</div></div>'


def _render_closed_strip(snapshot: PipelineSnapshot) -> str:
    """Show post-NDA failures (deals with engagement signal: notes or
    meaningful_conversation). Pre-NDA outreach attrition counted separately
    in the header so the strip stays focused on meaningful losses."""
    items = "".join(
        f'<a class="gb-closed-item" href="{escape(c.attio_url)}" '
        f'target="_blank" rel="noreferrer noopener">{escape(c.company)}</a>'
        for c in snapshot.closed_recent
    )
    post_nda = snapshot.closed_count_post_nda
    pre_nda = snapshot.closed_count_pre_nda
    recent_n = len(snapshot.closed_recent)

    if post_nda == 0:
        body = (
            '<div class="gb-empty" style="padding: 12px 0;">'
            "No post-NDA closures yet — every loss to date is pre-NDA "
            "outreach attrition (cold email + LinkedIn DM nonresponse)."
            "</div>"
        )
    else:
        body = f'<div class="gb-closed-list">{items}</div>'

    return dedent(
        f"""
        <div class="gb-closed-strip">
        <div class="gb-closed-header">
        <span class="gb-closed-title">{escape(snapshot.terminal_stage)} &middot; Post-NDA</span>
        <span class="gb-closed-total">
        <strong>{post_nda}</strong> post-NDA failures
        &middot; {pre_nda} pre-NDA outreach attrition (excluded)
        &middot; {recent_n} of {post_nda} shown
        </span>
        </div>
        {body}
        </div>
        """
    ).strip()


def _advanced_this_week(snapshot: PipelineSnapshot, today: date) -> int:
    """Count deals whose stage_since landed in the last 7 days."""
    week_start = today - timedelta(days=6)
    n = 0
    for d in snapshot.deals:
        ts = _parse_iso(d.stage_since)
        if not ts:
            continue
        if week_start <= ts.date() <= today:
            n += 1
    return n


def _stalled_count(snapshot: PipelineSnapshot, today: date) -> int:
    """Deals that have sat in their current stage for >30 days."""
    threshold = today - timedelta(days=30)
    n = 0
    for d in snapshot.deals:
        ts = _parse_iso(d.stage_since)
        if not ts:
            continue
        if ts.date() < threshold:
            n += 1
    return n


def _render_subtitle(snapshot: PipelineSnapshot) -> str:
    return (
        '<div class="gb-subtitle">'
        'Active conversations &mdash; <span class="highlight">NDA signed forward</span>. '
        "Cold outreach &amp; identified targets aggregate on M&amp;A Analytics, not here."
        "</div>"
    )


def _render_stat_pills(snapshot: PipelineSnapshot) -> str:
    today = date.today()
    active = len(snapshot.deals)
    advanced = _advanced_this_week(snapshot, today)
    stalled = _stalled_count(snapshot, today)
    fetched = _parse_iso(snapshot.fetched_at)
    fetched_str = (
        fetched.strftime("%b %-d, %H:%M UTC") if fetched else snapshot.fetched_at
    )
    deal_word = "deal" if active == 1 else "deals"
    return dedent(
        f"""
        <div class="gb-stat-pills">
        <span class="gb-stat-pill"><strong>{active}</strong> active {deal_word}</span>
        <span class="gb-stat-pill green"><strong>{advanced}</strong> advanced this week</span>
        <span class="gb-stat-pill {'red' if stalled else ''}"><strong>{stalled}</strong> stalled &gt;30d</span>
        <span class="gb-stat-pill"><strong>{snapshot.closed_count}</strong> closed lifetime</span>
        <a class="gb-stat-link" href="/ma-analytics" target="_self">Outreach funnel stats &rarr; M&amp;A Analytics</a>
        <span class="gb-stat-meta">snapshot {escape(fetched_str)}</span>
        </div>
        """
    ).strip()


# Visual stubs only — filter pills are interactive via st.segmented_control
# in render(); dropdowns + search render but don't mutate state.
def _render_filter_bar_stubs() -> str:
    return dedent(
        """
        <div class="gb-filter-bar" style="border-bottom: none; padding-bottom: 0; margin-bottom: 16px;">
        <select class="gb-filter-select"><option>All categories</option></select>
        <select class="gb-filter-select"><option>All locations</option></select>
        <input class="gb-filter-search" type="text" placeholder="Search company, owner..." />
        </div>
        """
    ).strip()


def _filter_deals_by_pill(snapshot: PipelineSnapshot, pill: str) -> PipelineSnapshot:
    """Apply pill filter to snapshot deals. Returns a new snapshot with the
    deals list filtered; counts and closed strip stay the same."""
    if pill == "All" or pill is None:
        return snapshot
    today = date.today()
    if pill == "Recent <14d":
        kept = [
            d for d in snapshot.deals
            if d.stage_since and (
                today - _parse_iso(d.stage_since).date()
                if _parse_iso(d.stage_since) else timedelta(days=999)
            ).days < 14
        ]
    elif pill == "Stalled":
        threshold = today - timedelta(days=30)
        kept = [
            d for d in snapshot.deals
            if d.stage_since and _parse_iso(d.stage_since) and _parse_iso(d.stage_since).date() < threshold
        ]
    else:
        kept = list(snapshot.deals)
    # Construct a shallow-copied snapshot with the filtered deals
    from dataclasses import replace
    return replace(snapshot, deals=kept)


def _render_empty_state() -> str:
    return (
        '<div class="gb-empty" style="background: var(--panel); '
        'border: 1px solid var(--border); border-radius: 10px;">'
        "No pipeline snapshot found at "
        "<code>brain/context/attio-pipeline-snapshot.json</code>. "
        "The agent must write the snapshot via Attio MCP before this page "
        "has data."
        "</div>"
    )


def render() -> None:
    import streamlit as st

    snapshot = load_pipeline()
    if snapshot is None:
        st.markdown(_render_empty_state(), unsafe_allow_html=True)
        return

    st.markdown(_render_subtitle(snapshot), unsafe_allow_html=True)
    st.markdown(_render_stat_pills(snapshot), unsafe_allow_html=True)

    pill = st.segmented_control(
        "Pipeline filter",
        options=["All", "Recent <14d", "Stalled"],
        default="All",
        key="deal_pipeline_filter",
        label_visibility="collapsed",
    ) or "All"
    filtered_snapshot = _filter_deals_by_pill(snapshot, pill)

    st.markdown(_render_filter_bar_stubs(), unsafe_allow_html=True)
    st.markdown(_render_kanban(filtered_snapshot), unsafe_allow_html=True)
    st.markdown(_render_closed_strip(snapshot), unsafe_allow_html=True)

    st.markdown(
        '<div class="gb-page-note">Page filters to <strong>NDA-forward</strong> '
        "stages (NDA, Financials Received, Submitted LOI, Signed LOI). Identified + "
        "Contacted moved to M&amp;A Analytics on 2026-04-24. Snapshot file rewritten "
        "by the agent via Attio MCP; scheduled refresh lands in a later session."
        "</div>",
        unsafe_allow_html=True,
    )
