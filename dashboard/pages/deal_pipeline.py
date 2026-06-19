"""Pipeline page — active Attio pipeline snapshot.

This page owns the dashboard's Active Pipeline Snapshot tile. It intentionally
shows the current engaged pipeline by company reference, while M&A Activity owns
weekly sourcing goals and source/outcome analytics.
"""

from __future__ import annotations

from datetime import date, datetime
from html import escape
from textwrap import dedent

import sys
from pathlib import Path

_DASHBOARD_DIR = Path(__file__).resolve().parent.parent
if str(_DASHBOARD_DIR) not in sys.path:
    sys.path.insert(0, str(_DASHBOARD_DIR))

from data_sources import load_pipeline  # noqa: E402


# -----------------------------------------------------------------------------
# Active Pipeline Snapshot
# -----------------------------------------------------------------------------


def _pipeline_stage_label(stage: str) -> str:
    return {
        "Contacted": "Warmed / teaser",
        "Financials Received": "Financials",
        "Closed / Not Proceeding": "Closed / not proceeding",
    }.get(stage, stage)


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


def _render_pipeline_snapshot() -> str:
    snapshot = load_pipeline(scope="full")
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

    # Dashboard pipeline starts once there has been engagement. Raw Identified
    # records remain in Attio, but this operating view should not show them
    # until a direct or intermediary-routed response moves them forward.
    stages = [stage for stage in snapshot.stages if stage not in {"Identified", "Closed / Not Proceeding"}]
    cells = []
    for stage in stages:
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
    return f'<section class="gb-zone">{head}<div class="gb-pipe-strip">{"".join(cells)}</div></section>'


def render() -> None:
    import streamlit as st

    st.markdown(_render_pipeline_snapshot(), unsafe_allow_html=True)
    st.markdown(
        '<div class="gb-page-note">Pipeline source: Attio Active Deals snapshot. Good Morning should reconcile Kay-confirmed changes, update Attio, then refresh this snapshot.</div>',
        unsafe_allow_html=True,
    )
