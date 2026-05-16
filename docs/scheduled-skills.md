# Scheduled Skills

Reference table for all skills that run on a schedule (launchd on Mac, systemd timers on the Hetzner VPS) independent of active Claude sessions. Authoritative source — `CLAUDE.md` links here rather than duplicating.

Schedule changes happen via systemd unit edits + validator wrapper updates; this table is reference material, not load-bearing process. If you change a schedule, update the corresponding row.

## Schedule

| Skill | Schedule | Purpose |
|-------|----------|---------|
| `deal-aggregator` | Mon-Fri 6am ET | Platform scanning + email screening |
| `email-intelligence` | Mon-Fri 7am ET | Gmail/Superhuman/Granola scanning, email-scan-results artifact |
| `jj-operations` (prep) | Sunday 6pm ET | Creates Mon-Fri Call Log tabs for the week (plist Hour=18). Reads pool artifact from **today's** target-discovery Phase 2 run (3pm fire). Kay reviews tabs Sunday evening before bed. |
| `jj-operations` (harvest) | Manual (no launchd) | Read Call Logs, update master sheet. Triggered by orchestrator or manually after JJ's 2pm shift ends. |
| `target-discovery` | On activation + weekly refill (morning workflow) | Target finding for Active-Outreach niches on initial activation or when weekly dashboard signals refill needed |
| `niche-intelligence` | Tuesday 22:30 ET | Newsletter scrape, niche identification, one-pagers, scorecards. Hardened with POST_RUN_CHECK validator + headless-tuesday-prompt 2026-05-01 (bead ai-ops-5wx closed). |
| `niche-intelligence` (daily) | Nightly | Sprint status tracking, Tabled/Killed processing |
| `target-discovery` (Phase 2) | Sunday 3pm ET | Weekly owner enrichment via Apollo + web research on JJ-Call-Only target sheets. **Moved from 10pm → 3pm 2026-04-26** to ensure pool artifact exists before jj-operations-sunday's 6pm fire (was a logical-ordering bug — prep can't read a pool that hasn't been written yet). 3-hour buffer accommodates enrichment + validator + retry; validator failures hit Slack with enough lead time for Kay to react before 6pm. **Hardened 2026-04-25:** wrapper passes `phase2-sunday` arg → headless prompt loads instead of bare `/target-discovery`; POST_RUN_CHECK runs `scripts/validate_phase2_integrity.py` per active JJ-Call-Only niche; validator failure overrides exit code → Slack alert. Bead `ai-ops-1`. |
| `nightly-tracker-audit` | Daily 23:30 ET | Tabled/Killed processing, WEEKLY REVIEW re-sort, Drive folder moves. **Staggered 2026-04-29 from 23:00 → 23:30** (see niche-intelligence row for parallel-fire incident). |
| `health-monitor` | Friday 12:30 AM ET | System health probes (services, hooks, vault, briefing pipeline) — output ready for Friday morning briefing |
| `calibration-workflow` | Thursday 11pm ET | Friday meta-calibration: rules → stop hooks, memory consolidation, stale-skill refresh |
| `attio-snapshot-refresh` | Hourly Mon-Fri 8am-8pm ET | Refreshes `brain/context/attio-pipeline-snapshot.json` so the Command Center dashboard (landing hero, Active Deal Pipeline, M&A Analytics) stays current as deals advance. Wrapper: `scripts/refresh-attio-snapshot.sh`. |
| `jj-snapshot-refresh` | Mon-Fri 9am, 2:30pm, 6pm ET | Refreshes `brain/context/jj-activity-snapshot.json` from JJ's per-niche target sheets (col T + V dial dates, normalized) so the dashboard's M&A Analytics JJ row + JJ-dials trend panel reflect today's activity. Scans the working tab + every Call Log tab (enumerated via Sheets API metadata using gog's OAuth refresh token). Wrapper: `scripts/refresh-jj-snapshot.sh`. |
| `apollo-credits-refresh` | Hourly Mon-Fri 8am-8pm ET | Refreshes `brain/context/apollo-credits-snapshot.json` so the dashboard's Infrastructure Zone 3 "Apollo credits" tile shows live rate-limit headroom. Apollo's API-key path doesn't expose monthly/daily balances — script captures `x-rate-limit-minute` / `x-minute-usage` / `x-minute-requests-left` headers from a single `/v1/organizations/enrich` call (≤1 credit cost per fire). Wrapper: `scripts/refresh-apollo-credits.sh`. Loader (`load_credit_tiles`) merges live values onto the YAML tile when snapshot ≤6h old, marks grey/stale beyond. |
| `launchd-debugger` | Daily 5am ET | Scans last 24h `logs/scheduled/`, spawns debug agent per failed job, fixes or surfaces to Slack. Hardened with POST_RUN_CHECK validator. Bead pending. |
| `conference-discovery` | Sunday 9pm ET | Weekly conference discovery + auto-archival on the Conference Pipeline sheet. **Hardened 2026-05-04** after 2026-05-03 incident wiped ~70 rows and exited 0 silently. Wrapper passes `sunday` arg → `headless-sunday-prompt.md` mandates a pre-run snapshot to `brain/context/rollback-snapshots/conference-pipeline-pre-run-{TODAY}.json` BEFORE any mutation. POST_RUN_CHECK runs `scripts/validate_conference_discovery_integrity.py` which compares post-run live row count against snapshot row_count and rejects if delta > MAX_ARCHIVAL_DELTA (15). Validator failure overrides exit code → Slack alert. |

`weekly-tracker` runs on Fridays but is triggered by the orchestrator during the morning workflow (not launchd). Kay needs results by 10am ET.

## Infrastructure

- Wrapper: `scripts/run-skill.sh` (shared by all jobs)
- Env: `scripts/.env.launchd` (secrets for headless runs, not committed)
- Logs: `logs/scheduled/{skill}-{date}.log` (14-day rotation)
- Plists: `~/Library/LaunchAgents/com.greenwich-barrow.{skill}.plist` (Mac), systemd units in `systemd/` (VPS)

## Wrapper Hardening Pattern (2026-04-25, bead ai-ops-1; doctrine broadened 2026-05-04)

- **POST_RUN_CHECK env var** in plist runs an artifact-integrity validator after Claude exits 0. Non-zero validator → wrapper overrides EXIT_CODE → Slack alert with "VALIDATOR FAILED" prefix. `$TODAY` placeholder in the env var is substituted with current YYYY-MM-DD.
- **Headless prompts** for skills that misbehave under `claude -p` with bare `/skill-name`. Wrapper detects `skill:args` pair and pipes `.claude/skills/{skill}/headless-{mode}-prompt.md` content as Claude's user prompt instead of `/skill-name`. Prompt file forbids clarifying questions and mandates artifact-first ordering.
- **Universal POST_RUN_CHECK doctrine (2026-05-04):** Every launchd-scheduled skill needs a validator — no exemptions. Precipitating incident: 2026-05-03 `conference-discovery` Sunday-night run wiped ~70 rows on the Conference Pipeline tab and exited 0 silently; the dashboard reported it healthy because no validator gated the exit code. Read-only skills (deal-aggregator, email-intelligence) get **lighter validators** that check "did the expected artifact land at the expected path?" but are NOT exempt from the post-run check entirely. Mutating skills get artifact + integrity validators (row-count delta, schema, header presence) per the existing pattern. **Hardened mutating skills (now 6):** `target-discovery` Phase 2, `jj-operations-sunday`, `nightly-tracker-audit`, `weekly-tracker`, `relationship-manager`, `conference-discovery`. Each has its own `scripts/validate_{skill}_integrity.py` validator + `headless-{mode}-prompt.md` headless prompt. Wrapper case-statement in `scripts/run-skill.sh` routes `skill:mode` args to the corresponding prompt file. Remaining unhardened skills (read-only + snapshot refreshers + weekly export jobs) are follow-up work — see audit table in any 2026-05-04 hardening session.

## Operations

- **Status check:** `launchctl list | grep greenwich` (Mac) / `systemctl --user list-timers` (VPS)
- **Manual trigger:** `launchctl start com.greenwich-barrow.{skill}` (Mac) / `systemctl --user start {skill}.service` (VPS)
- **Mac must be in sleep mode (not shut down) for scheduled runs to fire.** VPS runs 24/7.
