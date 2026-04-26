#!/usr/bin/env python3
"""Weekly snapshot writer — invoked by launchd Friday 22:00 ET (Phase C).

Reads dashboard.snapshot.snapshot_weekly() and writes the canonical
brain/trackers/weekly/{week-ending}-weekly-tracker.md file.

Idempotent: skip if the file already exists, unless --force is passed.
Pure read-only on every source — no Sheet writes, no Slack, no Drive.

Usage:
    python3 scripts/snapshot_weekly_to_vault.py
    python3 scripts/snapshot_weekly_to_vault.py --week-ending 2026-04-24
    python3 scripts/snapshot_weekly_to_vault.py --week-ending 2026-04-24 --force
    python3 scripts/snapshot_weekly_to_vault.py --dry-run
"""

from __future__ import annotations

import argparse
import sys
from datetime import date, timedelta
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "dashboard"))

from snapshot import snapshot_weekly  # noqa: E402

VAULT_TRACKERS_DIR = REPO_ROOT / "brain" / "trackers" / "weekly"


def _last_friday(today: date) -> date:
    """Return the most recent Friday on or before today.
    Friday isoweekday = 5 (Mon=1..Sun=7)."""
    delta = (today.isoweekday() - 5) % 7
    return today - timedelta(days=delta)


def _delta_str(this_val, prior_val) -> str:
    try:
        d = int(this_val) - int(prior_val)
    except (TypeError, ValueError):
        return "—"
    if d > 0:
        return f"+{d}"
    if d < 0:
        return str(d)
    return "0"


def _format_markdown(snap: dict) -> str:
    week_ending = snap["week_ending"]
    week_start = snap["week_start"]
    prior_end = snap["prior_week_ending"]
    metrics = snap["metrics"]

    lines: list[str] = [
        "---",
        'schema_version: "2.0.0"',
        f"date: {week_ending}",
        "type: tracker",
        f'title: "Weekly Activity Tracker — Week Ending {week_ending}"',
        "tags:",
        f"  - date/{week_ending}",
        "  - output",
        "  - output/tracker",
        "  - status/published",
        "  - topic/weekly-tracker",
        "  - source/dashboard-snapshot",
        "---",
        "",
        f"# Weekly Activity Tracker — Week Ending {week_ending}",
        "",
        f"**Window:** {week_start} → {week_ending} (prior week = week ending {prior_end}).",
        "**Source:** `dashboard.snapshot.snapshot_weekly()` — single source of truth for metric definitions.",
        "",
        "## Key Metrics",
        "",
        "| Metric | This Week | Prior Week | Delta |",
        "|--------|-----------|------------|-------|",
        f"| Outreach sends (SENT verb-tag bullets) | {metrics['outreach_sends_this_week']} | {metrics['outreach_sends_prior_week']} | {_delta_str(metrics['outreach_sends_this_week'], metrics['outreach_sends_prior_week'])} |",
        f"| Drafts created (DRAFTED bullets) | {metrics['drafts_this_week']} | {metrics['drafts_prior_week']} | {_delta_str(metrics['drafts_this_week'], metrics['drafts_prior_week'])} |",
        f"| CEO LinkedIn DMs | {metrics['linkedin_dms_this_week']} | {metrics['linkedin_dms_prior_week']} | {_delta_str(metrics['linkedin_dms_this_week'], metrics['linkedin_dms_prior_week'])} |",
        f"| Operations dials (window-corrected) | {metrics['ops_dials_this_week']} | {metrics['ops_dials_prior_week']} | {_delta_str(metrics['ops_dials_this_week'], metrics['ops_dials_prior_week'])} |",
        f"| Owner conversations | {metrics['owner_conversations']} | — | — |",
        f"| NDAs signed | {metrics['ndas_signed']} | — | — |",
        f"| Financials received | {metrics['financials_received']} | — | — |",
        f"| LOIs submitted | {metrics['lois_submitted']} | — | — |",
        f"| Closed / Not proceeding | {metrics['closed_not_proceeding']} | — | — |",
        f"| Conferences attended | {metrics['conferences_attended']} | — | — |",
        f"| Intermediary meetings | {metrics['intermediary_meetings']} | — | — |",
        f"| CIMs received | {metrics['cims_received']} | — | — |",
        "",
    ]

    if metrics["active_niches"]:
        lines.append(
            f"**Active niches** ({metrics['active_niche_count']}): "
            + ", ".join(metrics["active_niches"])
        )
    else:
        lines.append("**Active niches:** none")
    lines.append(
        f"**New contacts (Attio total):** {metrics['new_contacts_attio_count']} "
        "(WoW delta pending historical snapshots)"
    )
    lines.append(f"**Operations dials lifetime:** {metrics['ops_dials_lifetime']}")
    lines.extend([
        "",
        "## Channel Performance",
        "",
        "| Channel | Sent | Reply | Positive | → NDA | Reply rate |",
        "|---------|------|-------|----------|-------|-----------|",
    ])
    for c in snap["channel_performance"]:
        deferred = " (deferred)" if c["deferred"] else ""
        lines.append(
            f"| {c['channel']}{deferred} | {c['sent']} | {c['reply']} | "
            f"{c['positive']} | {c['to_nda']} | {c['reply_rate']} |"
        )

    lines.extend([
        "",
        "## Per-Niche Breakdown",
        "",
        "| Niche | Operations dials lifetime | Active |",
        "|-------|---------------------------|--------|",
    ])
    for r in snap["per_niche_breakdown"]:
        active = "✓" if r["active"] else "—"
        lines.append(f"| {r['niche']} | {r['ops_dials_lifetime']} | {active} |")

    lines.extend([
        "",
        "## Data Sources",
        "",
        f"- Attio snapshot fresh: {snap['data_sources']['attio_snapshot_fresh']}",
        f"- Attio snapshot fetched: {snap['data_sources']['attio_snapshot_fetched_at']}",
        f"- Operations snapshot fetched: {snap['data_sources']['ops_snapshot_fetched_at']}",
        f"- Pipeline total deal count: {snap['data_sources']['pipeline_full_deal_count']}",
        f"- Prior week tracker present: {snap['data_sources']['prior_week_tracker_present']}",
        "",
        "## Narrative (optional manual additions)",
        "",
        "_Key Relationships Advanced, Surprising Findings, Blocker, and Next-Week Watchlist_",
        "_remain optional manual additions per the dashboard-as-source plan._",
        "_Append below this line with operator commentary if desired._",
        "",
    ])

    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Write canonical weekly tracker snapshot to vault."
    )
    parser.add_argument("--week-ending", help="ISO date YYYY-MM-DD (defaults to most recent Friday).")
    parser.add_argument("--force", action="store_true", help="Overwrite existing file.")
    parser.add_argument("--dry-run", action="store_true", help="Print path + preview, no write.")
    args = parser.parse_args()

    if args.week_ending:
        week_ending = date.fromisoformat(args.week_ending)
    else:
        week_ending = _last_friday(date.today())

    out_path = VAULT_TRACKERS_DIR / f"{week_ending.isoformat()}-weekly-tracker.md"

    if out_path.exists() and not args.force and not args.dry_run:
        print(f"Already exists: {out_path}")
        print("Pass --force to overwrite.")
        return 0

    snap = snapshot_weekly(week_ending)
    text = _format_markdown(snap)

    if args.dry_run:
        print(f"[dry-run] Would write to: {out_path}")
        print("--- preview (first 50 lines) ---")
        print("\n".join(text.splitlines()[:50]))
        return 0

    VAULT_TRACKERS_DIR.mkdir(parents=True, exist_ok=True)
    out_path.write_text(text)
    print(f"Wrote {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
