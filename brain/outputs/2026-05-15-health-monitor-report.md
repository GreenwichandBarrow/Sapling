---
schema_version: 1.2.0
date: 2026-05-15
type: tracker
status: published
skill_origin: health-monitor
kay_approved: null
kay_approval_date: null
people: []
companies: []
projects: []
hypothesis: null
trace: null
task_ref: null
published_url: null
tags:
  - date/2026-05-15
  - output
  - output/tracker
  - status/published
  - topic/health-monitor
  - source/claude
---

# Health Monitor Report — 2026-05-15 (08:56 ET on-demand)

## Overall: RED (carryover) — 3 RED | 6 YELLOW | 24 GREEN

This is an on-demand probe fired 8h after the scheduled `health-monitor` run at 00:30 ET. Cross-referenced against [[trackers/health/2026-05-15-health]] (the morning's scheduled report). Verdict: **all three RED items from 00:30 persist** (9-week-old Identified cohort, MEMORY.md 531 lines, 91 orphan wiki-links). No new REDs emerged in the 8h window. Today's morning artifacts all landed successfully (email-intelligence, relationship-manager, deal-aggregator-morning, deal-aggregator-friday). One persistent infra finding — `deal-aggregator-friday` and `deal-aggregator` share the same log filename and interleave writes — confirmed at 06:00:44 ET today.

---

## Per-category status

| Category | RED | YELLOW | GREEN | Notes |
|---|---|---|---|---|
| Scheduled jobs (systemd timers) | 0 | 2 | 19 | `launchd-debugger` self-referential regex bug day 4; `weekly-tracker` still iMac-resident |
| MCP / service connectivity | 0 | 0 | 8 | All endpoints GREEN per `external-services-snapshot.json` 08:30 ET; Motion 401 expected (lapses 2027-03-10) |
| Snapshot freshness | 0 | 0 | 3 | attio 56min, apollo 56min, jj 14h (off-hours threshold OK) |
| Vault hygiene | 2 | 1 | 2 | 91 orphan wiki-links (RED), MEMORY.md 531 lines (RED), session-decisions gaps 5/13+5/14 (YELLOW) |
| Briefing pipeline | 0 | 0 | 4 | email-scan + relationship-status + deal-aggregator morning + friday digest all written today |
| Dashboard tile staleness | 0 | 0 | 3 | All three loader snapshots written within business-hour window |

**Totals:** 3 RED | 6 YELLOW | 24 GREEN (unchanged from 00:30 — no degradation, no improvement in 8h)

---

## Scheduled jobs — last 24h

Last-24h fire log (all `exit: 0`, validator PASSED unless noted):

| Job | Last fire | Status |
|---|---|---|
| deal-aggregator (6am ET) | Fri 06:00:44 | GREEN, artifact 21,309 bytes |
| deal-aggregator-friday (digest, 6am ET) | Fri 06:00:44 | GREEN, digest 6,888 bytes — **log filename collision: writes to `deal-aggregator-2026-05-15-0600.log` alongside morning run, interleaved** |
| email-intelligence (7am ET) | Fri 07:00 | GREEN, artifact 10,921 bytes |
| relationship-manager (6:50am ET) | Fri 06:50 | GREEN, artifact 21,987 bytes |
| attio-snapshot-refresh (hourly) | Fri 08:00 | GREEN, 12 deals / 7 stages |
| apollo-credits-refresh (hourly) | Fri 08:00 | GREEN, 999/1000 minute headroom |
| external-services-probe (every 30min) | Fri 08:30 | GREEN, 8 services |
| jj-snapshot-refresh (3x daily) | Thu 18:00 | GREEN (next fire 09:00) |
| post-call-analyzer-poll (5min) | Thu 18:00 | GREEN (next fire 13:00) |
| launchd-debugger (5am ET) | Fri 05:00 | YELLOW — validator PASSED, but self-referential regex bug day 4 means 1 "suppressed failure" per day is its own narrative summary. One-line fix in `scripts/scan_launchd_failures.py`. |
| nightly-tracker-audit (11:30pm ET) | Thu 23:30 | GREEN |
| calibration-workflow (11pm Thu) | Thu 23:00 | GREEN, proposal at `.claude/calibration-proposals/2026-05-14-pending-review.md` |
| health-monitor (12:30am Fri) | Fri 00:30 | GREEN (this delta-check is the on-demand follow-up) |
| **weekly-tracker (Fri 10am ET)** | — | YELLOW — **no server timer**. iMac plist owns it. Today is Friday. If iMac offline, the 10am G&B deliverable misses. Last vault write: `2026-05-08-weekly-tracker.md` (7 days ago). |

**Newly-deployed timers awaiting first auto-fire validation (GREEN-watch):**
- `weekly-snapshot.timer` — first fire tonight Fri 22:00
- `weekly-archive-export.timer` — first fire Sat 09:00
- `deal-aggregator-friday.timer` — fired successfully today 06:00:44 (validation cycle PASSED, but log-collision needs a `LOG_PREFIX` env)

**No iMac launchd plists currently being relied on** except `weekly-tracker` (carried-over migration item).

---

## Silent-failure scan

Last 7 days of `logs/scheduled/` grepped for `exit: [1-9]` and `VALIDATOR FAILED`:

| File | Issue | Status |
|---|---|---|
| `deal-aggregator-2026-05-11-0600.log` | Validator exit: 2 | Single occurrence, not recurring |
| `target-discovery-2026-05-10-1500.log` | Validator exit: 1 | Single occurrence, Sunday weekly job |
| `launchd-debugger-2026-05-12/13/14-0500.log` | "Suppressed failure" entries are the launchd-debugger's OWN prior-day summaries (regex self-match bug) | Day-4 known bug, suppression-routing prevents Slack noise |
| `relationship-manager-2026-05-11-0650.log` | Single non-zero exit, recovered next run | Not recurring |

**No 2+ consecutive failed runs anywhere.** Validator gates held. The `deal-aggregator-friday` + `deal-aggregator` log-collision at 06:00:44 today is a logging defect, not an execution defect — both runs hit exit 0, both validators PASSED, both artifacts landed.

---

## MCP / service connectivity (from `external-services-snapshot.json` 08:30 ET)

| Service | Status | Notes |
|---|---|---|
| Attio | GREEN | API key resolves via `op://GB Server/Attio API Key/password` |
| Apollo | GREEN | 999/1000 minute headroom |
| Gmail (gog) | GREEN | OAuth valid |
| Calendar (gog) | GREEN | |
| Drive (gog) | GREEN | |
| Sheets (gog) | GREEN | |
| Granola | GREEN | REST API via `granola-api`; latest note 2026-05-14 20:36 ET (within 3d threshold) |
| GitHub (gh) | GREEN | |
| Motion | RED-expected | 401 — cancellation in progress per [[memory/project_motion_cancellation_status]], lapses 2027-03-10 |
| Slack webhooks | GREEN | 4 webhooks configured |
| MCP attio-mcp | SKIP | Smithery OAuth re-flow required — superseded by direct-API path per `feedback_all_skills_use_1password` |
| MCP superhuman | SKIP | Sunset 4/29 per `feedback_gmail_only_no_superhuman` |
| Claude API key | SKIP | Not in env (intentional — agents use `op://` resolution) |
| Linkt | SKIP | Browser session required, no API |

The two `external-services-snapshot.json` "error" entries (`launchd: FileNotFoundError`, `mcp-processes: attio-mcp=0 superhuman=0`) are **expected** on a Linux server — there is no `launchd` here, and the MCP processes for attio/superhuman are correctly retired. The probe script needs an OS-aware skip for both. Cosmetic, not blocking.

---

## Snapshot freshness

| Snapshot | Last fetched | Age | Threshold | Status |
|---|---|---|---|---|
| `attio-pipeline-snapshot.json` | Fri 08:00:56 UTC = 04:00 ET? actually `2026-05-15T12:00:56Z` = 08:00 ET | 56min | <4h business hrs | GREEN |
| `apollo-credits-snapshot.json` | Fri 08:00:45 ET | 56min | <6h | GREEN |
| `jj-activity-snapshot.json` | Thu 22:00:45 UTC = Thu 18:00 ET | ~15h | <30h off-hours | GREEN (next fire 09:00 ET) |

All three loader snapshots are within their thresholds. Dashboard tiles will render live data, no grey/stale banners.

---

## Vault hygiene

| Check | Status | Detail |
|---|---|---|
| Schema validation | GREEN | 10/10 recently-modified files pass (sampled at 00:30) |
| Orphan wiki-links | RED (carryover) | 91 orphans across 405 unique entity links (22% orphan rate). Trend 22 → 46 → 89 → 98 → **91** — first non-degrading week since 4/17. Stale `acme-corp` placeholder still leaks. |
| MEMORY.md size | RED (carryover) | 531 lines vs 200 threshold (2.65× over). Truncation banner active in system-prompt context every session. Thursday 11pm calibration-workflow didn't compact it. |
| Session-decisions continuity | YELLOW (carryover) | Missing 2026-05-13 and 2026-05-14 (latest is 2026-05-12). Either evening shutdown skipped or sessions were genuinely off those days. |
| Entity count | INFO | 168 entities, 872 vault markdown files |
| Granola call ingestion | GREEN | Latest: 2026-05-13 (carlos-nieto-dca), within 3d threshold |

---

## Briefing pipeline (today's artifacts)

| Artifact | Path | Size | Status |
|---|---|---|---|
| Email scan results | `brain/context/email-scan-results-2026-05-15.md` | 10,921 bytes | GREEN, written 07:04 ET |
| Relationship status | `brain/context/relationship-status-2026-05-15.md` | 21,987 bytes | GREEN, written 06:58 ET (Friday surfacing day per `feedback_relationship_cadence_friday_only`) |
| Deal aggregator morning | `brain/context/deal-aggregator-scan-2026-05-15.md` | 21,309 bytes | GREEN, 0 PASS / 7 NEAR-MISS / 11 FLAG / 64 HARD-REJECT |
| Deal aggregator Friday digest | `brain/trackers/weekly/2026-05-15-deal-aggregator-digest.md` | 6,888 bytes | GREEN, 1 proposed addition, 0 retirements, 🔴 volume 2nd consecutive week |
| Weekly tracker (Friday 10am deliverable) | — | — | YELLOW — no server timer, last vault write 2026-05-08, depends on iMac being online |

---

## Recommended morning-briefing Decision items (Obama-style)

Three items rise to RECOMMEND level — all carried from the 00:30 scheduled run, none newly emerged:

1. 🟢 [COO] **RECOMMEND: Triage 9-week-old Identified cohort** — Art Ship Co, J.W. Allen Co., Personal Risk Mgmt at 62d Identified, 2 of 3 zero interaction. 50% of "active" pipeline inflation. → YES (close-out) / NO (queue second-touch) / DISCUSS

2. 🟡 [CTO] **RECOMMEND: Schedule MEMORY.md consolidation for next Thursday calibration window** — 531 lines truncates context every session, last night's calibration didn't compact. Owns the systemic fix path. → YES / NO / DISCUSS

3. 🟡 [CTO] **RECOMMEND: Ship `LOG_PREFIX=deal-aggregator-friday` env in friday.service unit** — confirmed today both deal-aggregator runs interleave writes into a single log at 06:00:44. One-line fix to `~/.config/systemd/user/deal-aggregator-friday.service`. → YES / NO / DISCUSS

**Not surfacing as Decision items (already wired up or low-leverage):**
- `weekly-tracker` iMac dependency — already carried as systemic migration item; previously surfaced
- `launchd-debugger` regex bug — already day 4, surfaced in prior briefings, one-line fix queued
- Orphan wiki-links 91 — carryover, weekly trend reversing, not action-today

---

## Trend vs 00:30 scheduled run (8h delta)

- All 3 REDs persist (no degradation, no improvement)
- All 6 YELLOWs persist
- 4 new GREEN data points landed: email-intelligence + relationship-manager + deal-aggregator (morning) + deal-aggregator (friday digest) all wrote artifacts and passed validators
- No new failures, no new validator escalations
- Service connectivity unchanged (8/8 GREEN, Motion 401 expected)
