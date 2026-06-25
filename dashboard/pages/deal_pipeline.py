"""Pipeline page — active Attio pipeline snapshot.

This page owns the dashboard's Active Pipeline Snapshot tile. It intentionally
shows the current engaged pipeline by company reference, while M&A Activity owns
weekly sourcing goals and source/outcome analytics.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime, timedelta
from html import escape
from textwrap import dedent

import sys
from pathlib import Path

_DASHBOARD_DIR = Path(__file__).resolve().parent.parent
if str(_DASHBOARD_DIR) not in sys.path:
    sys.path.insert(0, str(_DASHBOARD_DIR))

from data_sources import load_pipeline, load_pipeline_source_map  # noqa: E402


# -----------------------------------------------------------------------------
# Active Pipeline Snapshot
# -----------------------------------------------------------------------------


@dataclass(frozen=True)
class _ClosedPipelineItem:
    company: str
    closed_date: date
    attio_url: str | None = None


def _pipeline_stage_label(stage: str) -> str:
    return {
        "Contacted": "Teaser",
        "Financials Received": "Financials",
        "Closed / Not Proceeding": "Closed / not proceeding",
    }.get(stage, stage)


def _teaser_items() -> list[_ClosedPipelineItem]:
    source_map = load_pipeline_source_map()
    if source_map is None:
        return []
    items = []
    for record in source_map.records:
        if (record.current_stage or "").casefold().strip() != "teaser":
            continue
        items.append(_ClosedPipelineItem(company=record.company, closed_date=date.today()))
    return sorted(items, key=lambda item: item.company.casefold())


def _stage_age_text(stage_deals: list) -> str:
    if not stage_deals:
        return "—"
    oldest = None
    oldest_deal = None
    for deal in stage_deals:
        try:
            ts = datetime.fromisoformat(deal.stage_since.replace("Z", "+00:00"))
        except (ValueError, AttributeError):
            continue
        if oldest is None or ts < oldest:
            oldest = ts
            oldest_deal = deal
    if oldest is None or oldest_deal is None:
        return "—"
    age = (date.today() - oldest.date()).days
    return f"oldest {age}d · {oldest_deal.company}"


def _recent_closed_deals(closed_deals: list) -> list[_ClosedPipelineItem]:
    cutoff = date.today() - timedelta(days=30)
    by_company: dict[str, _ClosedPipelineItem] = {}

    def add_item(item: _ClosedPipelineItem) -> None:
        if item.closed_date < cutoff:
            return
        key = item.company.casefold().strip()
        existing = by_company.get(key)
        if existing is None or item.closed_date > existing.closed_date:
            by_company[key] = item

    for deal in closed_deals:
        try:
            closed_at = datetime.fromisoformat(deal.stage_since.replace("Z", "+00:00")).date()
        except (ValueError, AttributeError):
            continue
        add_item(_ClosedPipelineItem(company=deal.company, closed_date=closed_at, attio_url=deal.attio_url))

    source_map = load_pipeline_source_map()
    if source_map is not None:
        for record in source_map.records:
            if record.current_stage != "Closed / Not Proceeding" or record.closed_not_proceeding_date is None:
                continue
            add_item(_ClosedPipelineItem(company=record.company, closed_date=record.closed_not_proceeding_date))

    return sorted(by_company.values(), key=lambda item: item.closed_date, reverse=True)


def _closed_age_text(closed_deals: list[_ClosedPipelineItem]) -> str:
    if not closed_deals:
        return "last 30d"
    age = (date.today() - closed_deals[0].closed_date).days
    return f"latest {age}d ago · last 30d"


def _render_pipeline_snapshot() -> str:
    snapshot = load_pipeline(scope="engaged")
    head = dedent(
        """
        <div class="gb-zone-head">
        <div>
        <div class="gb-zone-label">Active Pipeline Snapshot</div>
        <div class="gb-zone-sublabel">Current engaged pipeline · company references, not another metric board</div>
        </div>
        <div class="gb-zone-meta">current state</div>
        </div>
        """
    ).strip()
    if snapshot is None:
        return f'<section class="gb-zone">{head}<div class="gb-zone-empty">Attio snapshot unavailable</div></section>'

    # Shared loader owns the NDA-forward stages. The first display column
    # remains the Attio Contacted position, but dashboard semantics are now
    # stricter: only explicitly mapped broker teasers belong there. Stale
    # proprietary/contacted rows stay out until financials arrive.
    stages = snapshot.stages
    cells = []
    for stage in stages:
        if stage == "Contacted":
            teaser_items = _teaser_items()
            count = len(teaser_items)
            if teaser_items:
                items = "".join(f'<li>{escape(d.company)}</li>' for d in teaser_items[:5])
                if len(teaser_items) > 5:
                    items += f'<li class="dim">+{len(teaser_items) - 5} more</li>'
            else:
                items = '<li class="dim">None</li>'
            meta = "broker teasers only"
            deals = []
        else:
            deals = [d for d in snapshot.deals if d.stage == stage]
            count = len(deals)
            if deals:
                items = "".join(
                    f'<li><a href="{escape(d.attio_url)}" target="_blank">{escape(d.company)}</a></li>'
                    for d in deals[:5]
                )
                if len(deals) > 5:
                    items += f'<li class="dim">+{len(deals) - 5} more</li>'
            else:
                items = '<li class="dim">None</li>'
            meta = _stage_age_text(deals)
        cell_class = "active" if count else "empty"
        cells.append(
            '<div class="gb-pipe-cell {cell_class}">'
            '<div class="gb-pipe-top"><span class="gb-pipe-label">{stage}</span><span class="gb-pipe-badge">{count}</span></div>'
            '<ol class="gb-pipe-list">{items}</ol>'
            '<div class="gb-pipe-meta">{meta}</div>'
            '</div>'.format(
                cell_class=escape(cell_class),
                stage=escape(_pipeline_stage_label(stage)),
                count=count,
                items=items,
                meta=escape(meta),
            )
        )

    closed_deals = _recent_closed_deals(snapshot.closed_recent)
    if closed_deals:
        closed_items = "".join(
            f'<li><a href="{escape(d.attio_url)}" target="_blank">{escape(d.company)}</a></li>'
            if d.attio_url else f'<li>{escape(d.company)}</li>'
            for d in closed_deals[:5]
        )
        if len(closed_deals) > 5:
            closed_items += f'<li class="dim">+{len(closed_deals) - 5} more</li>'
    else:
        closed_items = '<li class="dim">None in last 30d</li>'
    cells.append(
        '<div class="gb-pipe-cell closed">'
        '<div class="gb-pipe-top"><span class="gb-pipe-label">Closed / not proceeding</span><span class="gb-pipe-badge">{count}</span></div>'
        '<ol class="gb-pipe-list">{items}</ol>'
        '<div class="gb-pipe-meta">{meta}</div>'
        '</div>'.format(
            count=len(closed_deals),
            items=closed_items,
            meta=escape(_closed_age_text(closed_deals)),
        )
    )
    return f'<section class="gb-zone">{head}<div class="gb-pipe-strip gb-pipe-strip-with-closed">{"".join(cells)}</div></section>'


def render() -> None:
    import streamlit as st

    st.markdown(_render_pipeline_snapshot(), unsafe_allow_html=True)
    st.markdown(
        '<div class="gb-page-note">Pipeline source: Attio Active Deals snapshot. Good Morning should reconcile Kay-confirmed changes, update Attio, then refresh this snapshot.</div>',
        unsafe_allow_html=True,
    )
