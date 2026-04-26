"""Weekly snapshot orchestrator — single source of truth for the metrics
that the legacy weekly-tracker skill used to produce.

Phase B of the dashboard-as-source pivot (`~/.claude/plans/linear-wiggling-toast.md`).
Pure read-only: reuses dashboard.data_sources helpers + JJ snapshot to
return one dict that scripts/snapshot_weekly_to_vault.py renders into
the canonical `brain/trackers/weekly/{week_ending}-weekly-tracker.md`.

Narrative fields (Key Relationships, Surprising Findings, Blocker, Next-Week
Watchlist) are returned as None — out of scope per the plan. Operator can
append manually after the metrics-snapshot lands.

Usage:
    from dashboard.snapshot import snapshot_weekly
    from datetime import date
    snap = snapshot_weekly(date(2026, 4, 24))
    print(snap["metrics"]["outreach_sends_this_week"])  # 6

CLI verification:
    python3 -m dashboard.snapshot 2026-04-24
"""

from __future__ import annotations

from datetime import date, timedelta
from pathlib import Path
import sys

_DASHBOARD_DIR = Path(__file__).resolve().parent
if str(_DASHBOARD_DIR) not in sys.path:
    sys.path.insert(0, str(_DASHBOARD_DIR))

from data_sources import (  # noqa: E402
    load_ma_analytics,
    load_jj_activity,
    load_pipeline,
    load_weekly_tracker_history,
)


def _activity_count(rows, category: str) -> int:
    for r in rows:
        if r.category == category:
            return r.count
    return 0


def _kpi_value(tiles, label: str) -> int:
    for t in tiles:
        if t.label == label:
            return int(t.value)
    return 0


def snapshot_weekly(week_ending: date) -> dict:
    """Aggregate all weekly metrics for the given Friday week-end date.

    Returns a dict matching the vault snapshot template. Run-time metrics
    (call counts, verb-tag counts) honor the [week_ending - 6, week_ending]
    7-day window — the same definition the dashboard renders. Operations
    dials reconstruct from JJ snapshot's by_day dict for historical accuracy.
    Snapshot-driven metrics (Attio companies count) reflect current state,
    not state-as-of-week_ending — historical Attio snapshots aren't kept.
    """
    week_start = week_ending - timedelta(days=6)
    prior_end = week_start - timedelta(days=1)
    prior_start = prior_end - timedelta(days=6)

    ma = load_ma_analytics(today=week_ending)
    jj = load_jj_activity()
    history = load_weekly_tracker_history()
    pipeline_full = load_pipeline(scope="full")

    # Window-corrected operations dials (jj.dials_this_week is fetch-time-relative).
    if jj is not None:
        ops_dials_this = jj.dials_in_window(week_start, week_ending)
        ops_dials_prior = jj.dials_in_window(prior_start, prior_end)
    else:
        ops_dials_this = ops_dials_prior = 0

    # Active niches list — read off the existing ActivityRow rather than
    # importing the private constant, so this stays decoupled.
    active_niches: list[str] = []
    for r in ma.activity_rows:
        if r.category == "Active Niches":
            active_niches = list(r.chips)
            break

    # Outreach + new-contacts come straight off the MA analytics object
    # (already populated by load_ma_analytics).
    om = ma.outreach_metrics
    nc = ma.new_contacts
    nb = ma.niche_breakdown

    metrics = {
        # Headline outcomes (matches Zone 1 deal-flow tiles)
        "owner_conversations": _kpi_value(ma.deal_flow_tiles, "Owner conversations"),
        "ndas_signed": _kpi_value(ma.deal_flow_tiles, "NDAs signed"),
        "financials_received": _kpi_value(ma.deal_flow_tiles, "Financials received"),
        "lois_submitted": _kpi_value(ma.deal_flow_tiles, "LOIs submitted"),
        "closed_not_proceeding": _kpi_value(ma.deal_flow_tiles, "Closed / Not proceeding"),
        # Outreach activity (Phase A.1 — verb-tag aggregation)
        "outreach_sends_this_week": om.sends_this_week if om else 0,
        "outreach_sends_prior_week": om.sends_last_week if om else 0,
        "drafts_this_week": om.drafts_this_week if om else 0,
        "drafts_prior_week": om.drafts_last_week if om else 0,
        "linkedin_dms_this_week": om.linkedin_dms_this_week if om else 0,
        "linkedin_dms_prior_week": om.linkedin_dms_last_week if om else 0,
        # Operations dials (window-corrected from JJ snapshot by_day)
        "ops_dials_this_week": ops_dials_this,
        "ops_dials_prior_week": ops_dials_prior,
        "ops_dials_lifetime": jj.dials_lifetime if jj else 0,
        # Activity rollups (Zone 5)
        "conferences_attended": _activity_count(ma.activity_rows, "Conferences attended"),
        "intermediary_meetings": _activity_count(ma.activity_rows, "Intermediary meetings"),
        "cims_received": _activity_count(ma.activity_rows, "CIMs received"),
        # New contacts (Phase A.3 — pending historical Attio snapshots for delta)
        "new_contacts_attio_count": nc.snapshot_count if nc else 0,
        # Niche state
        "active_niches": active_niches,
        "active_niche_count": len(active_niches),
    }

    channel_performance = [
        {
            "channel": c.name,
            "sent": c.sent,
            "reply": c.reply,
            "positive": c.positive,
            "to_nda": c.to_nda,
            "reply_rate": c.reply_rate,
            "deferred": c.deferred,
        }
        for c in ma.channels
    ]

    per_niche_breakdown = (
        [
            {
                "niche": r.niche,
                "ops_dials_lifetime": r.jj_dials_lifetime,
                "active": r.jj_active,
            }
            for r in nb.rows
        ]
        if nb is not None
        else []
    )

    # Prior-week historical comparison (best-effort from prior weekly tracker file)
    prior_snapshot = history.get(prior_end)

    return {
        "schema_version": "2.0.0",  # Phase B — dashboard-as-source
        "week_ending": week_ending.isoformat(),
        "week_start": week_start.isoformat(),
        "prior_week_start": prior_start.isoformat(),
        "prior_week_ending": prior_end.isoformat(),
        "metrics": metrics,
        "channel_performance": channel_performance,
        "per_niche_breakdown": per_niche_breakdown,
        "data_sources": {
            "attio_snapshot_fresh": ma.snapshot_fresh,
            "attio_snapshot_fetched_at": nc.fetched_at if nc else None,
            "ops_snapshot_fetched_at": jj.fetched_at if jj else None,
            "pipeline_full_deal_count": (
                len(pipeline_full.deals) + pipeline_full.closed_count
                if pipeline_full is not None else 0
            ),
            "prior_week_tracker_present": prior_snapshot is not None,
        },
        "narrative": {
            "key_relationships_advanced": None,
            "surprising_findings": None,
            "blocker": None,
            "next_week_watchlist": None,
        },
    }


if __name__ == "__main__":
    import json
    if len(sys.argv) < 2:
        print("Usage: python3 -m dashboard.snapshot YYYY-MM-DD", file=sys.stderr)
        sys.exit(1)
    week_ending = date.fromisoformat(sys.argv[1])
    out = snapshot_weekly(week_ending)
    print(json.dumps(out, indent=2, default=str))
