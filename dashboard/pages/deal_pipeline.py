"""Deal Pipeline page — Attio replica, Kanban by stage.

Reads `brain/context/attio-pipeline-snapshot.json` — a point-in-time snapshot
of Attio's "Active Deals - Owners" list, written by the harness via the
Attio MCP tools. Streamlit can't call MCP tools directly, so the snapshot
file is the contract between agent (writer) and page (reader).

Six Kanban columns reflect the full pipeline schema (Identified → Signed LOI)
even when a stage has no deals yet; Attio's list today only defines the first
two statuses, and the trailing columns render empty until Kay adds them as
Attio list statuses. Terminal "Closed / Not Proceeding" renders as a compact
strip below the board — closed deals aren't pipeline.
"""

from __future__ import annotations

from datetime import datetime, timezone
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
    footer = f"In stage {days}d" if days is not None else ""
    return dedent(
        f"""
        <a class="gb-kanban-card" href="{escape(deal.attio_url)}"
           target="_blank" rel="noreferrer noopener">
        <div class="company">{escape(deal.company)}</div>
        <div class="meta">{_card_meta(deal)}</div>
        <div class="footer">{escape(footer)}</div>
        </a>
        """
    ).strip()


def _render_column(stage: str, deals: list[PipelineDeal]) -> str:
    if deals:
        cards = "".join(_render_card(d) for d in deals)
    else:
        cards = '<div class="gb-kanban-col-empty">No deals at this stage.</div>'
    return dedent(
        f"""
        <div class="gb-kanban-col">
        <div class="gb-kanban-col-header">
        <span class="gb-kanban-col-name">{escape(stage)}</span>
        <span class="gb-kanban-col-count">{len(deals)}</span>
        </div>
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
    cols = "".join(_render_column(s, by_stage[s]) for s in snapshot.stages)
    return f'<div class="gb-kanban-wrap"><div class="gb-kanban">{cols}</div></div>'


def _render_closed_strip(snapshot: PipelineSnapshot) -> str:
    items = "".join(
        f'<a class="gb-closed-item" href="{escape(c.attio_url)}" '
        f'target="_blank" rel="noreferrer noopener">{escape(c.company)}</a>'
        for c in snapshot.closed_recent
    )
    recent_n = len(snapshot.closed_recent)
    return dedent(
        f"""
        <div class="gb-closed-strip">
        <div class="gb-closed-header">
        <span class="gb-closed-title">{escape(snapshot.terminal_stage)}</span>
        <span class="gb-closed-total">
        <strong>{snapshot.closed_count}</strong> closed lifetime
        &middot; {recent_n} most recent shown
        </span>
        </div>
        <div class="gb-closed-list">{items}</div>
        </div>
        """
    ).strip()


def _render_subtitle(snapshot: PipelineSnapshot) -> str:
    active = len(snapshot.deals)
    fetched = _parse_iso(snapshot.fetched_at)
    fetched_str = (
        fetched.strftime("%b %-d, %H:%M UTC") if fetched else snapshot.fetched_at
    )
    return (
        '<div class="gb-subtitle">'
        'Live Attio replica &mdash; '
        f'<span class="highlight">{escape(snapshot.list_name)}</span>. '
        f"{active} active deals across {len(snapshot.stages)} stages "
        f'&nbsp;&middot;&nbsp; snapshot fetched {escape(fetched_str)}'
        "</div>"
    )


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
    st.markdown(_render_kanban(snapshot), unsafe_allow_html=True)
    st.markdown(_render_closed_strip(snapshot), unsafe_allow_html=True)

    st.markdown(
        '<div class="gb-page-note">Stage vocabulary reflects the 6-stage '
        "pipeline schema. Stages that don’t yet exist as Attio statuses "
        "(NDA, Financials Received, Submitted LOI, Signed LOI) render empty "
        "until added to the Attio list. Snapshot file is rewritten by the "
        "agent via Attio MCP; scheduled refresh lands in a later session."
        "</div>",
        unsafe_allow_html=True,
    )
