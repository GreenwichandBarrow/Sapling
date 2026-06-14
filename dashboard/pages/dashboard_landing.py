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
from html import escape
from textwrap import dedent

import sys
from pathlib import Path

_DASHBOARD_DIR = Path(__file__).resolve().parent.parent
if str(_DASHBOARD_DIR) not in sys.path:
    sys.path.insert(0, str(_DASHBOARD_DIR))


def _tile(body: str) -> str:
    return dedent(body).strip()


def _status_dot(status: str) -> str:
    if status in {"ok", "green"}:
        return "green"
    if status in {"warn", "yellow"}:
        return "yellow"
    if status in {"alert", "red"}:
        return "red"
    return "grey"


def _command_item(title: str, value: str, detail: str, status: str, href: str) -> str:
    return dedent(
        f"""
        <a class="gb-command-item" href="{href}" target="_self">
          <div class="gb-command-item-head">
            <span class="gb-status-dot {_status_dot(status)}"></span>
            <span>{escape(title)}</span>
          </div>
          <div class="gb-command-value">{escape(value)}</div>
          <div class="gb-command-detail">{escape(detail)}</div>
        </a>
        """
    ).strip()


def _command_center_strip() -> str:
    """Top-level operating cockpit: what ran, what needs review, and freshness."""
    items: list[str] = []

    try:
        from data_sources import load_skill_health, skill_health_summary
        from pages.c_suite_skills import _bookend_summary

        groups = load_skill_health()
        summary = skill_health_summary(groups)
        bookend = _bookend_summary()
        scheduled_issues = summary["daily_issue"] + summary["gaps"]
        scheduled_status = "alert" if scheduled_issues else "ok"
        items.append(_command_item(
            "Scheduled Work",
            f"{summary['daily_completed']} / {summary['daily_total']} due-by-now",
            f"{scheduled_issues} issues, {summary['daily_remaining']} later today",
            scheduled_status,
            "/c-suite-skills",
        ))
        bookend_issues = bookend["daily_issues"]
        bookend_status = "alert" if bookend_issues else ("warn" if bookend["daily_fired"] < bookend["daily_total"] else "ok")
        items.append(_command_item(
            "Bookends",
            f"{bookend['daily_fired']} / {bookend['daily_total']} complete",
            f"{bookend_issues} issues in Good Morning / Good Night flow",
            bookend_status,
            "/c-suite-skills",
        ))
    except Exception:
        items.append(_command_item(
            "Scheduled Work",
            "unavailable",
            "skill-health loader failed",
            "alert",
            "/c-suite-skills",
        ))

    try:
        from data_sources import check_dashboard_staleness

        stale = check_dashboard_staleness()
        if stale:
            first = stale[0]
            items.append(_command_item(
                "Freshness",
                f"{len(stale)} stale source{'s' if len(stale) != 1 else ''}",
                f"{first.label} {first.age_hours:.1f}h old",
                "warn",
                "/infrastructure",
            ))
        else:
            items.append(_command_item(
                "Freshness",
                "current",
                "all dashboard snapshots within thresholds",
                "ok",
                "/infrastructure",
            ))
    except Exception:
        items.append(_command_item(
            "Freshness",
            "unavailable",
            "staleness check failed",
            "alert",
            "/infrastructure",
        ))

    try:
        from pages.deal_aggregator import _load_artifact_tables, _verdict_groups

        listings, _sources, _summary = _load_artifact_tables(date.today(), 1)
        surfaced, learning, rejected = _verdict_groups(listings)
        status = "ok" if surfaced else ("warn" if learning else "warn")
        items.append(_command_item(
            "Deal Intake",
            f"{len(surfaced)} surfaced",
            f"{len(learning)} borderline, {len(rejected)} filtered today",
            status,
            "/deal-aggregator",
        ))
    except Exception:
        items.append(_command_item(
            "Deal Intake",
            "unavailable",
            "deal-aggregator artifact read failed",
            "alert",
            "/deal-aggregator",
        ))

    try:
        from data_sources import load_credit_tiles, load_system_health, system_health_summary

        health = load_system_health()
        health_summary = system_health_summary(health)
        credits = load_credit_tiles()
        review = [t for t in health if t.status in ("alert", "warn")]
        if health_summary["alert"]:
            status = "alert"
        elif health_summary["warn"]:
            status = "warn"
        else:
            status = "ok"
        if review:
            detail = f"{review[0].label}: {review[0].detail}"
        else:
            live_credits = sum(1 for c in credits if c.runway_color == "green")
            detail = f"{live_credits} / {len(credits)} usage meters live" if credits else "usage meters unavailable"
        items.append(_command_item(
            "System",
            f"{health_summary['healthy']} healthy",
            detail,
            status,
            "/infrastructure",
        ))
    except Exception:
        items.append(_command_item(
            "System",
            "unavailable",
            "infrastructure loader failed",
            "alert",
            "/infrastructure",
        ))

    return _tile(f"""
    <section class="gb-command-strip">
      <div class="gb-command-head">
        <div>
          <div class="gb-command-eyebrow">Command Center</div>
          <div class="gb-command-title">Today&apos;s operating status</div>
        </div>
        <div class="gb-command-meta">Live local checks · no email sending</div>
      </div>
      <div class="gb-command-grid">
        {''.join(items)}
      </div>
    </section>
    """)


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
        <a class="gb-tile hero" href="/ma-analytics" target="_self">
        <div class="label">Active Pipeline Snapshot</div>
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
        headline_unit = "NDA-forward deals"
    elif total == 1:
        headline_unit = "NDA-forward deal"
    else:
        headline_unit = "NDA-forward deals"

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
    <a class="gb-tile hero" href="/ma-analytics" target="_self">
    <div class="label">Active Pipeline Snapshot</div>
    <div class="gb-hero-row">
    <div class="gb-hero-headline">
    <div class="gb-hero-num">{total}<span class="unit">{headline_unit}</span></div>
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
    """Main dashboard tile for today's Deal Aggregator review lanes."""
    try:
        from pages.deal_aggregator import _load_artifact_tables, _verdict_groups

        today = date.today()
        listings, _sources, _summary = _load_artifact_tables(today, 1)
        surfaced, learning, rejected = _verdict_groups(listings)

        surfaced_n = len(surfaced)
        learning_n = len(learning)
        rejected_n = len(rejected)

        status_class = "up" if surfaced_n else ("flat" if learning_n else "")
        footer_text = "review intake" if surfaced_n or learning_n else "scan complete"

        return _tile(f"""
        <a class="gb-tile" href="/deal-aggregator" target="_self">
        <div class="label">Deal Aggregator</div>
        <div class="gb-deal-agg-tile-lines">
          <div><span class="num">{surfaced_n}</span> surfaced today</div>
          <div><span class="num">{learning_n}</span> borderline</div>
          <div><span class="num dim">{rejected_n}</span> filtered</div>
        </div>
        <div class="footer">
        <span class="gb-trend {status_class}">&rarr; {escape(footer_text)}</span>
        <span class="gb-horizon">TODAY</span>
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

def _tile_email_orchestration() -> str:
    """Main dashboard tile for email-derived operating signals."""
    try:
        from data_sources import load_email_orchestrator_status

        email = load_email_orchestrator_status()
        if email.send_blockers:
            primary = str(email.send_blockers)
            unit = "send blockers"
            dot = "red"
            footer = "review before action"
        elif email.review_count:
            primary = str(email.review_count)
            unit = "review items"
            dot = "yellow"
            footer = "review routing"
        else:
            primary = "Clear"
            unit = "email routing"
            dot = "green"
            footer = "no review items"
        detail = (
            f"{email.drafts_pending} drafts pending · {email.deal_items} deal · "
            f"{email.pipeline_items} pipeline · {email.relationship_items} relationship"
        )
        return _tile(f"""
        <a class="gb-tile" href="/email-orchestration" target="_self">
        <div class="label">Email Orchestration</div>
        <div class="primary" style="font-size: 2.1em;">{escape(primary)}<span class="unit">{escape(unit)}</span></div>
        <div class="gb-status-row">
        <span class="gb-status-dot {dot}"></span>
        <span class="gb-status-text">{escape(detail)}</span>
        </div>
        <div class="footer">
        <span class="gb-trend flat">&rarr; {escape(footer)}</span>
        <span class="gb-horizon">TODAY</span>
        </div>
        </a>
        """)
    except Exception:
        return _tile("""
        <a class="gb-tile" href="/email-orchestration" target="_self">
        <div class="label">Email Orchestration</div>
        <div class="primary">&mdash;<span class="unit">status unavailable</span></div>
        <div class="footer">
        <span class="gb-trend flat">&rarr; check page</span>
        <span class="gb-horizon">TODAY</span>
        </div>
        </a>
        """)


def _tile_ma_analytics() -> str:
    """Main dashboard tile for Kay's current weekly sourcing goals."""
    goals = []
    try:
        from data_sources import load_ma_analytics

        ma = load_ma_analytics(today=date.today())
        goals = ma.weekly_goals
    except Exception:
        goals = []

    if not goals:
        goal_rows = """
        <div class="gb-ma-label">Conferences / networking</div><div class="gb-ma-value">&mdash;</div>
        <div class="gb-ma-label">Intermediary / river-guide</div><div class="gb-ma-value">&mdash;</div>
        <div class="gb-ma-label">Owner / seller</div><div class="gb-ma-value">&mdash;</div>
        """
        footer_text = "source check needed"
    else:
        def _dot(status: str) -> str:
            if status == "on_track":
                return "green"
            if status == "below":
                return "red"
            return "yellow"

        def _short(label: str) -> str:
            return {
                "Conferences / networking": "Conferences / networking",
                "Intermediary / river-guide": "Intermediary / river-guide",
                "Owner / seller": "Owner / seller",
            }.get(label, label)

        goal_rows = "".join(
            f'<div class="gb-ma-label"><span class="gb-status-dot {_dot(g.status)}" '
            f'style="width:7px;height:7px;display:inline-block;margin-right:7px;"></span>{escape(_short(g.label))}</div>'
            f'<div class="gb-ma-value">{g.count} / {g.target_min}-{g.target_max}</div>'
            for g in goals
        )
        below = sum(1 for g in goals if g.status == "below")
        above = sum(1 for g in goals if g.status == "above")
        if below:
            footer_text = f"{below} below goal"
        elif above:
            footer_text = f"{above} above target"
        else:
            footer_text = "all on track"

    return _tile(f"""
    <a class="gb-tile" href="/ma-analytics" target="_self">
    <div class="label">M&amp;A Analytics</div>
    <div style="font-size: 0.78em; color: #888; margin-bottom: 12px; letter-spacing: 0.16em; text-transform: uppercase;">This Month's Weekly Goals</div>
    <div class="gb-ma-list">
    {goal_rows}
    </div>
    <div class="footer">
    <span class="gb-trend flat">&rarr; {escape(footer_text)}</span>
    <span class="gb-horizon">THIS WEEK</span>
    </div>
    </a>
    """)

def _tile_c_suite_skills() -> str:
    """Live: daily scheduled + bookend-triggered skill status."""
    try:
        from data_sources import load_skill_health, skill_health_summary
        from pages.c_suite_skills import _bookend_summary

        groups = load_skill_health()
        summary = skill_health_summary(groups)
        bookend = _bookend_summary()
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

    scheduled_completed = summary["daily_completed"]
    scheduled_total = summary["daily_total"]
    scheduled_issues = summary["daily_issue"] + summary["gaps"]
    bookend_completed = bookend["daily_fired"]
    bookend_total = bookend["daily_total"]
    bookend_issues = bookend["daily_issues"]
    return _tile(f"""
    <a class="gb-tile" href="/c-suite-skills" target="_self">
    <div class="label">C-Suite &amp; Skills</div>
    <div style="font-size: 0.78em; color: #888; margin-bottom: 12px; letter-spacing: 0.16em; text-transform: uppercase;">Daily</div>
    <div style="font-size: 0.82em; color: #6f7788; letter-spacing: 0.12em; text-transform: uppercase; margin-bottom: 6px;">Scheduled</div>
    <div class="primary" style="font-size: 1.72em; line-height: 1.05; margin-bottom: 6px;">{scheduled_completed}<span class="unit">/ {scheduled_total} completed</span></div>
    <div class="gb-status-row" style="margin-top: 0;">
    <span class="gb-status-dot {'red' if scheduled_issues else 'green'}"></span>
    <span class="gb-status-text">{scheduled_issues} {'issue' if scheduled_issues == 1 else 'issues'}</span>
    </div>
    <div style="font-size: 0.82em; color: #6f7788; letter-spacing: 0.12em; text-transform: uppercase; margin: 16px 0 6px;">Bookend Triggered</div>
    <div style="font-size: 0.9em; color: #cfd3dc; font-variant-numeric: tabular-nums; margin-bottom: 6px;">{bookend_completed} / {bookend_total} completed</div>
    <div class="gb-status-row" style="margin-top: 0;">
    <span class="gb-status-dot {'red' if bookend_issues else 'green'}"></span>
    <span class="gb-status-text">{bookend_issues} {'issue' if bookend_issues == 1 else 'issues'}</span>
    </div>
    <div class="footer">
    <span class="gb-trend flat">&rarr; {summary["ondemand"]} on-demand skills</span>
    <span class="gb-horizon">TODAY</span>
    </div>
    </a>
    """)


def _tile_infrastructure() -> str:
    """Live: infrastructure operating status for the landing page."""
    try:
        from data_sources import load_credit_tiles, load_system_health, system_health_summary
        tiles = load_system_health()
        credits = load_credit_tiles()
        summary = system_health_summary(tiles)
    except Exception:
        return _tile("""
        <a class="gb-tile" href="/infrastructure" target="_self">
        <div class="label">System Health &amp; Infrastructure</div>
        <div class="primary">&mdash;<span class="unit">probes unreachable</span></div>
        <div class="footer">
        <span class="gb-trend flat">&rarr; check page</span>
        <span class="gb-horizon">NOW</span>
        </div>
        </a>
        """)

    problem_tiles = [t for t in tiles if t.status in ("alert", "warn")]
    problem_tiles.sort(key=lambda t: 0 if t.status == "alert" else 1)
    if problem_tiles:
        issue = problem_tiles[0]
        issue_dot = "red" if issue.status == "alert" else "yellow"
        issue_text = f'{escape(issue.label)} needs review'
        issue_detail = escape(issue.detail)
    else:
        issue_dot = "green"
        issue_text = "No infrastructure issues"
        issue_detail = ""

    usage_live = sum(1 for t in credits if t.runway_color == "green")
    usage_total = len(credits)
    usage_dot = "green" if usage_total and usage_live == usage_total else "yellow"
    usage_text = f'{usage_live} / {usage_total} usage meters live' if usage_total else "Usage meters unavailable"

    if summary["alert"]:
        primary = "Issue"
        primary_unit = "needs review"
    elif summary["warn"]:
        primary = "Running"
        primary_unit = "with review item"
    else:
        primary = "Running"
        primary_unit = "all clear"

    issue_detail_html = f'<div style="font-size: 0.78em; color: #7f8798; margin-top: 3px; line-height: 1.25;">{issue_detail}</div>' if issue_detail else ""

    return _tile(f"""
    <a class="gb-tile" href="/infrastructure" target="_self">
    <div class="label">System Health &amp; Infrastructure</div>
    <div class="primary" style="font-size: 2.1em;">{primary}<span class="unit">{primary_unit}</span></div>
    <div class="gb-status-row">
    <span class="gb-status-dot green"></span>
    <span class="gb-status-text">Core systems running</span>
    </div>
    <div class="gb-status-row" style="margin-top: 7px;">
    <span class="gb-status-dot {issue_dot}"></span>
    <span class="gb-status-text">{issue_text}</span>
    </div>
    {issue_detail_html}
    <div class="gb-status-row" style="margin-top: 7px;">
    <span class="gb-status-dot {usage_dot}"></span>
    <span class="gb-status-text">{usage_text}</span>
    </div>
    <div class="footer">
    <span class="gb-trend flat">&rarr; live probes</span>
    <span class="gb-horizon">NOW</span>
    </div>
    </a>
    """)


def render() -> None:
    import streamlit as st

    command_strip = _command_center_strip()
    hero = _hero_active_deal_pipeline()
    small_tiles = [
        _tile_deal_aggregator(),
        _tile_email_orchestration(),
        _tile_ma_analytics(),
        _tile_c_suite_skills(),
        _tile_infrastructure(),
    ]
    st.markdown(
        f'{command_strip}<div class="gb-grid">{hero}{"".join(small_tiles)}</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="gb-page-note">All tiles read live data &mdash; Active '
        "Deal Pipeline, Deal Aggregator, M&amp;A Analytics, C-Suite &amp; "
        "Skills, and Infrastructure."
        "</div>",
        unsafe_allow_html=True,
    )
