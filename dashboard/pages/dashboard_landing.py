"""Dashboard landing page — hero Active Deal Pipeline tile + 4 small tiles.

Layout matches `dashboard/mockup-landing.html` (locked Session 4 PM):
  Row 1: HERO Active Deal Pipeline (full-width, 56px / weight-200 headline,
         4 stage breakdown cells, accent-blue gradient)
  Row 2: Deal Aggregator · M&A Analytics · C-Suite & Skills · Infrastructure

Each tile that has a corresponding live page reads its loader inside a
try/except so a data-source failure falls back to a placeholder rather than
crashing the page.
"""

from __future__ import annotations

from datetime import date, datetime, timedelta, timezone
from textwrap import dedent

import sys
from pathlib import Path

_DASHBOARD_DIR = Path(__file__).resolve().parent.parent
if str(_DASHBOARD_DIR) not in sys.path:
    sys.path.insert(0, str(_DASHBOARD_DIR))


def _tile(body: str) -> str:
    return dedent(body).strip()


# -----------------------------------------------------------------------------
# Hero tile — Active Deal Pipeline (NDA-forward)
# -----------------------------------------------------------------------------


_NDA_FORWARD_STAGES = ("NDA", "Financials Received", "Submitted LOI", "Signed LOI")


def _stage_age_days(deals: list, stage: str, today: date) -> tuple[int, str]:
    """Return (count, avg-age-text) for deals currently in `stage`."""
    in_stage = [d for d in deals if d.stage == stage]
    if not in_stage:
        return 0, "—"
    ages = []
    for d in in_stage:
        try:
            ts = datetime.fromisoformat(d.stage_since.replace("Z", "+00:00"))
        except (ValueError, AttributeError):
            continue
        ages.append((today - ts.date()).days)
    if not ages:
        return len(in_stage), "—"
    avg = round(sum(ages) / len(ages))
    if len(in_stage) == 1:
        return 1, f"{avg}d in stage"
    return len(in_stage), f"avg {avg}d in stage"


def _advanced_this_week(deals: list, today: date) -> int:
    """Count NDA-forward deals whose stage_since landed in the last 7 days."""
    week_start = today - timedelta(days=6)
    n = 0
    for d in deals:
        if d.stage not in _NDA_FORWARD_STAGES:
            continue
        try:
            ts = datetime.fromisoformat(d.stage_since.replace("Z", "+00:00"))
        except (ValueError, AttributeError):
            continue
        if week_start <= ts.date() <= today:
            n += 1
    return n


def _stalled_count(deals: list, today: date) -> int:
    """Deals that have sat in their current NDA-forward stage >30 days."""
    threshold = today - timedelta(days=30)
    n = 0
    for d in deals:
        if d.stage not in _NDA_FORWARD_STAGES:
            continue
        try:
            ts = datetime.fromisoformat(d.stage_since.replace("Z", "+00:00"))
        except (ValueError, AttributeError):
            continue
        if ts.date() < threshold:
            n += 1
    return n


def _hero_active_deal_pipeline() -> str:
    """Live: Active Deal Pipeline hero — 4 stage cells + headline + trend."""
    try:
        from data_sources import load_pipeline
        snapshot = load_pipeline(scope="active")
    except Exception:
        snapshot = None

    if snapshot is None:
        return _tile("""
        <a class="gb-tile hero" href="/deal-pipeline" target="_self">
        <div class="label">Active Deal Pipeline · NDA Forward</div>
        <div class="gb-hero-row">
        <div class="gb-hero-headline">
        <div class="gb-hero-num">&mdash;<span class="unit">snapshot unreachable</span></div>
        <div class="gb-hero-trend">Run the agent's snapshot refresh to populate.</div>
        <div class="gb-hero-cta">View pipeline &rarr;</div>
        </div>
        <div class="gb-stage-bar">
        <div class="gb-stage-cell"><div class="gb-stage-label">NDA</div><div class="gb-stage-num zero">&mdash;</div></div>
        <div class="gb-stage-cell"><div class="gb-stage-label">Financials</div><div class="gb-stage-num zero">&mdash;</div></div>
        <div class="gb-stage-cell"><div class="gb-stage-label">Submitted LOI</div><div class="gb-stage-num zero">&mdash;</div></div>
        <div class="gb-stage-cell"><div class="gb-stage-label">Signed LOI</div><div class="gb-stage-num zero">&mdash;</div></div>
        </div>
        </div>
        </a>
        """)

    today = date.today()
    deals = snapshot.deals

    nda_n, nda_meta = _stage_age_days(deals, "NDA", today)
    fin_n, fin_meta = _stage_age_days(deals, "Financials Received", today)
    loi_n, loi_meta = _stage_age_days(deals, "Submitted LOI", today)
    sloi_n, sloi_meta = _stage_age_days(deals, "Signed LOI", today)

    total = nda_n + fin_n + loi_n + sloi_n
    advanced = _advanced_this_week(deals, today)
    stalled = _stalled_count(deals, today)
    # Hero is NDA-forward scoped, so show post-NDA closures only — pre-NDA
    # outreach attrition lives on Deal Aggregator / M&A Analytics, not here.
    closed_post_nda = getattr(snapshot, "closed_count_post_nda", 0)

    if total == 0:
        headline_unit = "NDA forward"
    elif total == 1:
        headline_unit = "active conversation"
    else:
        headline_unit = "active conversations"

    advanced_html = (
        f'<span class="green">&uarr; {advanced} advanced this week</span>'
        if advanced
        else '<span>0 advanced this week</span>'
    )
    stalled_html = (
        f'<span class="red">{stalled} stalled &gt;30d</span>'
        if stalled
        else '<span>0 stalled &gt;30d</span>'
    )

    def _cell(label: str, n: int, meta: str) -> str:
        zero = " zero" if n == 0 else ""
        return (
            f'<div class="gb-stage-cell">'
            f'<div class="gb-stage-label">{label}</div>'
            f'<div class="gb-stage-num{zero}">{n}</div>'
            f'<div class="gb-stage-meta">{meta}</div>'
            f"</div>"
        )

    return _tile(f"""
    <a class="gb-tile hero" href="/deal-pipeline" target="_self">
    <div class="label">Active Deal Pipeline &middot; NDA Forward</div>
    <div class="gb-hero-row">
    <div class="gb-hero-headline">
    <div class="gb-hero-num">{total}<span class="unit">{headline_unit}</span></div>
    <div class="gb-hero-trend">
    {advanced_html}
    &nbsp;&middot;&nbsp;
    {stalled_html}
    &nbsp;&middot;&nbsp;
    <span>{closed_post_nda} closed post-NDA lifetime</span>
    </div>
    <div class="gb-hero-cta">View pipeline &rarr;</div>
    </div>
    <div class="gb-stage-bar">
    {_cell("NDA", nda_n, nda_meta)}
    {_cell("Financials", fin_n, fin_meta)}
    {_cell("Submitted LOI", loi_n, loi_meta)}
    {_cell("Signed LOI", sloi_n, sloi_meta)}
    </div>
    </div>
    </a>
    """)


# -----------------------------------------------------------------------------
# Small tiles — row below the hero
# -----------------------------------------------------------------------------


def _tile_deal_aggregator() -> str:
    """Today's count + delta vs prior scan day. Falls back to placeholder on read failure."""
    try:
        from data_sources import load_scan
        today = date.today()
        today_scan = load_scan(today)
        today_count = today_scan.deals_found if today_scan else None

        # Walk back up to 7 days to find the most recent prior scan (skips weekends).
        prior_count = None
        prior_date = None
        for offset in range(1, 8):
            d = today - timedelta(days=offset)
            scan = load_scan(d)
            if scan is not None:
                prior_count = scan.deals_found
                prior_date = d
                break

        if today_count is None and prior_count is None:
            primary = '<span class="primary">&mdash;<span class="unit">no recent scan</span></span>'
            footer = '<span class="gb-horizon">TODAY</span>'
        else:
            display_count = today_count if today_count is not None else prior_count
            display_label = "new leads" if today_count is not None else f"on {prior_date.strftime('%-m/%-d')}"
            primary = f'<div class="primary">{display_count}<span class="unit">{display_label}</span></div>'

            if today_count is not None and prior_count is not None and prior_date is not None:
                delta = today_count - prior_count
                prior_label = prior_date.strftime("%-m/%-d")
                if delta > 0:
                    trend = f'<span class="gb-trend up">&uarr; vs. {prior_count} on {prior_label}</span>'
                elif delta < 0:
                    trend = f'<span class="gb-trend down">&darr; vs. {prior_count} on {prior_label}</span>'
                else:
                    trend = f'<span class="gb-trend">flat vs. {prior_label}</span>'
                horizon = "TODAY"
            else:
                # Today's scan not yet run (weekend, or before 6am Mon-Fri fire). Show the
                # prior-day count without a fake delta and label the horizon clearly.
                trend = '<span class="gb-trend">awaiting next scan</span>'
                horizon = "LAST SCAN"
            footer = f'{trend}<span class="gb-horizon">{horizon}</span>'

        return _tile(f"""
        <a class="gb-tile" href="/deal-aggregator" target="_self">
        <div class="label">Deal Aggregator</div>
        {primary}
        <div class="footer">
        {footer}
        </div>
        </a>
        """)
    except Exception:
        return _tile("""
        <a class="gb-tile" href="/deal-aggregator" target="_self">
        <div class="label">Deal Aggregator</div>
        <div class="primary">&mdash;<span class="unit">read failed</span></div>
        <div class="footer">
        <span class="gb-trend">check logs</span>
        <span class="gb-horizon">TODAY</span>
        </div>
        </a>
        """)


def _tile_ma_analytics() -> str:
    """Stacked metric list per locked mockup — live wiring lands separately."""
    try:
        from data_sources import load_ma_analytics
        ma = load_ma_analytics()
        # Pull what we have live; fall back gracefully where data isn't wired.
        owner_now = ma.deal_flow_tiles[0].value if ma.deal_flow_tiles else 0
        ndas_now = ma.deal_flow_tiles[1].value if len(ma.deal_flow_tiles) > 1 else 0
    except Exception:
        owner_now = 0
        ndas_now = 0
    return _tile(f"""
    <a class="gb-tile" href="/ma-analytics" target="_self">
    <div class="label">M&amp;A Analytics</div>
    <div class="gb-ma-list">
    <div class="gb-ma-label">Owner conversations</div><div class="gb-ma-value">{owner_now}</div>
    <div class="gb-ma-label">NDAs signed</div><div class="gb-ma-value">{ndas_now}</div>
    <div class="gb-ma-label">Outbound contacted</div><div class="gb-ma-value">&mdash;</div>
    <div class="gb-ma-label">Reply rate</div><div class="gb-ma-value">&mdash;</div>
    </div>
    <div class="footer">
    <span class="gb-trend flat">&rarr; DealsX wires May 7</span>
    <span class="gb-horizon">THIS WEEK</span>
    </div>
    </a>
    """)


def _tile_c_suite_skills() -> str:
    """Live: count of scheduled skills that fired today + alert state."""
    try:
        from data_sources import load_skill_health, skill_health_summary
        groups = load_skill_health()
        summary = skill_health_summary(groups)
    except Exception:
        return _tile("""
        <a class="gb-tile" href="/c-suite-skills" target="_self">
        <div class="label">C-Suite &amp; Skills</div>
        <div class="primary">&mdash;<span class="unit">loader unreachable</span></div>
        <div class="footer">
        <span class="gb-trend flat">&rarr; check page</span>
        <span class="gb-horizon">TODAY</span>
        </div>
        </a>
        """)
    fired = summary["fired_today"]
    on_deck = summary["on_deck"]
    missed = summary["missed"]
    gaps = summary["gaps"]
    scheduled_total = fired + on_deck + missed + gaps
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
    <a class="gb-tile" href="/c-suite-skills" target="_self">
    <div class="label">C-Suite &amp; Skills</div>
    <div class="primary">{fired}<span class="unit">/ {scheduled_total} fired</span></div>
    <div class="gb-status-row">
    <span class="gb-status-dot {dot}"></span>
    <span class="gb-status-text">{status_text}</span>
    </div>
    <div class="footer">
    <span class="gb-trend flat">&rarr; {summary["ondemand"]} on-demand</span>
    <span class="gb-horizon">TODAY</span>
    </div>
    </a>
    """)


def _tile_infrastructure() -> str:
    """Live: System Health tile counts + alert state."""
    try:
        from data_sources import load_system_health, system_health_summary
        tiles = load_system_health()
        summary = system_health_summary(tiles)
    except Exception:
        return _tile("""
        <a class="gb-tile" href="/infrastructure" target="_self">
        <div class="label">Infrastructure</div>
        <div class="primary">&mdash;<span class="unit">probes unreachable</span></div>
        <div class="footer">
        <span class="gb-trend flat">&rarr; check page</span>
        <span class="gb-horizon">NOW</span>
        </div>
        </a>
        """)
    healthy = summary["healthy"]
    total = sum(summary.values())
    if summary["alert"] > 0:
        dot = "red"
        status_text = (
            f'{summary["alert"]} alert &middot; {summary["warn"]} warn'
            if summary["warn"] else f'{summary["alert"]} alert'
        )
    elif summary["warn"] > 0:
        dot = "yellow"
        status_text = f'{summary["warn"]} warn'
    else:
        dot = "green"
        status_text = "all systems nominal"
    return _tile(f"""
    <a class="gb-tile" href="/infrastructure" target="_self">
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
    </a>
    """)


def render() -> None:
    import streamlit as st

    hero = _hero_active_deal_pipeline()
    small_tiles = [
        _tile_deal_aggregator(),
        _tile_ma_analytics(),
        _tile_c_suite_skills(),
        _tile_infrastructure(),
    ]
    st.markdown(
        f'<div class="gb-grid">{hero}{"".join(small_tiles)}</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="gb-page-note">Active Deal Pipeline, M&amp;A Analytics, '
        "C-Suite &amp; Skills, and Infrastructure read live data. Deal "
        "Aggregator placeholder pending wire-up."
        "</div>",
        unsafe_allow_html=True,
    )
