---
name: Dashboard-as-source pivot for weekly metrics
description: 2026-04-26 architecture flip — dashboard.snapshot.snapshot_weekly() is the single source of truth for weekly metric definitions. Vault snapshots downstream of dashboard. Sheet downstream of vault.
type: project
originSessionId: 765f2769-0c68-4590-b466-5773bf5b3d4e
---
Phase A-F.1 shipped 2026-04-26 (bead `ai-ops-jrj.5`, plan `~/.claude/plans/linear-wiggling-toast.md`):
- `dashboard/snapshot.py` is single source for weekly metric definitions
- `scripts/snapshot_weekly_to_vault.py` writes `brain/trackers/weekly/{date}-weekly-tracker.md` Friday 22:00 ET (launchd `com.greenwich-barrow.weekly-snapshot`, Weekday 5)
- `scripts/export_weekly_archive_to_sheet.py` writes archive Sheet `1NGGZY...` Saturday 09:00 ET (launchd `com.greenwich-barrow.weekly-archive-export`, Weekday 6)
- Legacy `com.greenwich-barrow.weekly-tracker.plist.disabled` (Thu 22:00) — preserved for emergency rollback until Phase F.2 cleanup on 2026-05-02

**Why:** 4/24 silent-fail (vault wrote, Sheet didn't) showed parallel-write paths drift. Inverting the flow eliminates that failure mode — dashboard is the metric definition, vault is the canonical record, Sheet is downstream archive.

**How to apply:**
- Adding a new weekly metric: edit `dashboard/data_sources.py` (load function) + `dashboard/snapshot.py` (orchestrator) — never edit weekly-tracker SKILL or duplicate the metric in the snapshot script
- Sheet only contains 5 Topline metrics today (Owner Convos, NDAs, Financials, LOIs Submitted, LOIs Signed); Weekly Detail tab's hybrid time-series + per-niche layout deferred (per-niche breakdown lives on dashboard Zone 6 instead)
- Schema 2.0.0 = dashboard-source vault file; schema 1.0.0 = legacy weekly-tracker — Week Archive page (`/week-archive`) shows source pill distinguishing them
- New dashboard helpers added: `OutreachMetrics`, `NewContactsMetric`, `NicheBreakdown` in `dashboard/data_sources.py`
- Phase F.2 cleanup on 2026-05-02: gut SKILL.md to stub, delete `weekly_tracker_validation.py` PreToolUse hook, slim validator to vault-only, rewrite headless prompt, update CLAUDE.md scheduled-skills table
