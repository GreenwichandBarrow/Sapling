# Scheduled Skills

Reference table for all skills that run on a schedule (launchd on Mac, systemd timers on the Hetzner VPS) independent of active Claude sessions. Authoritative source — `CLAUDE.md` links here rather than duplicating.

Schedule changes happen via systemd unit edits + validator wrapper updates; this table is reference material, not load-bearing process. If you change a schedule, update the corresponding row.

## Schedule

| Skill | Schedule | Purpose |
|-------|----------|---------|
| `deal-aggregator` | Mon-Fri 7:00am ET | Single morning platform scan + email screening after the 6:30am email-intelligence artifact lands; timed for summer Good Morning readiness by ~7:45am ET. Duplicate afternoon runs retired 2026-06-19 to prevent dashboard/status mismatches |
| `email-intelligence` | Mon-Fri 6:30am ET | Gmail/Granola scanning, email-scan-results artifact |
| Cold Call Operations (Sunday prep) | On-demand / intentionally paused | Creates Mon-Fri Call Log tabs when Kay reactivates cold-call operations. Sunday timer disabled by design as of 2026-07-17; do not treat disabled `cold-call-operations-sunday` or legacy installed alias `jj-operations-sunday` as a scheduler failure. |
| Cold Call Operations (harvest) | Manual | Read Call Logs and update the master sheet. Triggered by orchestrator or manually after the cold-call block ends. |
| `target-discovery` | On activation + weekly refill (morning workflow) | Target finding for Active-Outreach niches on initial activation or when weekly dashboard signals refill needed |
| `niche-intelligence` | Monday 22:30 ET | Full thesis-development run: newsletters/web/calls/email/research, niche identification, one-pagers, scorecards, tracker update. Feeds Tuesday Good Morning CEO thesis decisions. Hardened with POST_RUN_CHECK validator. |
| `niche-intelligence` signal scan | Thursday 22:30 ET | Light thesis signal scan: PE/news, email/call/inbox/conference changes. Feeds Friday Good Morning with urgent/queue/park/no-signal status only. |
| `niche-intelligence` (daily) | Nightly | Sprint status tracking, Tabled/Killed processing |
| `target-discovery` (Phase 2) | On-demand / intentionally paused | Owner enrichment via Apollo + web research on Cold-Call-Only target sheets when Kay reactivates cold-call operations or asks for a Phase 2 refill. Sunday timer disabled by design as of 2026-07-17; do not treat disabled `target-discovery-sunday` as a scheduler failure. Historical notes: moved from 10pm to 3pm on 2026-04-26 when it fed Cold Call Operations; hardened 2026-04-25 with `phase2-sunday` headless prompt and `scripts/validate_phase2_integrity.py`; scoped pool-only on 2026-05-31. |
| `nightly-tracker-audit` | Daily 23:30 ET | Tabled/Killed processing, WEEKLY REVIEW re-sort, Drive folder moves. **Staggered 2026-04-29 from 23:00 → 23:30** (see niche-intelligence row for parallel-fire incident). |
| `health-monitor` | Friday 12:30 AM ET | System health probes (services, hooks, vault, briefing pipeline) — output ready for Friday morning briefing |
| `calibration-workflow` | Thursday 11pm ET | Friday meta-calibration: rules → stop hooks, memory consolidation, stale-skill refresh |
| `attio-snapshot-refresh` | Hourly Mon-Fri 8am-8pm ET | Refreshes `brain/context/attio-pipeline-snapshot.json` so the Command Center dashboard (landing hero, Active Deal Pipeline, M&A Analytics) stays current as deals advance. Wrapper: `scripts/refresh-attio-snapshot.sh`. |
| Cold Call Snapshot Refresh (`jj-snapshot-refresh` legacy id) | Mon-Fri 9am, 2:30pm, 6pm ET | Refreshes `brain/context/jj-activity-snapshot.json` from cold-call target sheets by resolving dial-date fields by header name, so the dashboard's M&A Analytics cold-call row and dial trend panel reflect today's activity. Scans the working tab + every Call Log tab (enumerated via Sheets API metadata using gog's OAuth refresh token). Wrapper: `scripts/refresh-jj-snapshot.sh`. |
| `apollo-credits-refresh` | Hourly Mon-Fri 8am-8pm ET | Refreshes `brain/context/apollo-credits-snapshot.json` so the dashboard's Infrastructure Zone 3 "Apollo credits" tile shows live rate-limit headroom. Apollo's API-key path doesn't expose monthly/daily balances — script captures `x-rate-limit-minute` / `x-minute-usage` / `x-minute-requests-left` headers from a single `/v1/organizations/enrich` call (≤1 credit cost per fire). Wrapper: `scripts/refresh-apollo-credits.sh`. Loader (`load_credit_tiles`) merges live values onto the YAML tile when snapshot ≤6h old, marks grey/stale beyond. |
| `launchd-debugger` | Daily 7:20am ET + on-failure | Runs after 6:30am email-intelligence and 7:00am deal-aggregator as the final pre-brief double-check; also auto-fires on non-zero scheduled-skill exits. Hardened with POST_RUN_CHECK validator. |
| `conference-discovery` | Sunday 9pm ET | Weekly conference discovery + auto-archival on the Conference Pipeline sheet. **Hardened 2026-05-04** after 2026-05-03 incident wiped ~70 rows and exited 0 silently. Wrapper passes `sunday` arg → `headless-sunday-prompt.md` mandates a pre-run snapshot to `brain/context/rollback-snapshots/conference-pipeline-pre-run-{TODAY}.json` BEFORE any mutation. POST_RUN_CHECK runs `scripts/validate_conference_discovery_integrity.py` which compares post-run live row count against snapshot row_count and rejects if delta > MAX_ARCHIVAL_DELTA (15). Validator failure overrides exit code → Slack alert. |

`weekly-tracker` runs on Fridays but is triggered by the orchestrator during the morning workflow (not launchd). Summer target: ready by ~7:30am ET so the Friday Good Morning can launch around 8:00-8:30am.

## Infrastructure

- Wrapper: `scripts/run-skill.sh` (shared by all jobs)
- Env: `scripts/.env.launchd` (secrets for headless runs, not committed)
- Logs: `logs/scheduled/{skill}-{date}.log` (14-day rotation)
- Plists: `~/Library/LaunchAgents/com.greenwich-barrow.{skill}.plist` (Mac), systemd units in `systemd/` (VPS)

## Model Routing (2026-05-30)

Effective **2026-06-15**, Anthropic moves programmatic Claude usage (`claude -p` non-interactive, Agent SDK, GitHub Actions) off the standard subscription onto a separate metered credit pool ($200/mo on Max 20x), billed at full API rates. Interactive terminal use is unaffected. A 30-day transcript analysis (2026-04-29 → 05-29) measured the scheduled fleet at **~$5,000/mo API-equivalent**, ~99% on Opus, because the wrapper passed no `--model` and every fire (plus every subagent it spawns) inherited the Opus default.

**Policy:** scheduled jobs default to **Sonnet**. Only genuinely reasoning-heavy jobs run on **Opus**. Subagents inherit the parent model, so `run-skill.sh` is the single chokepoint — it routes the whole fan-out. The per-fire auth preflight runs on **Haiku** (auth is account-level; model is irrelevant to what the check validates, so use the cheapest).

- **Opus list** (`OPUS_SKILLS` in `run-skill.sh`): `calibration-workflow`, `niche-intelligence`. These make non-obvious judgment calls (rules → stop-hook graduation; niche scoring against the G&B scorecard). Add a skill here only with a cited reason.
- **Everything else → Sonnet**: data-gathering, scanning, classification, sheet-population, tab creation, discovery, debugging. Kay is the judgment layer on these outputs; Sonnet is sufficient.
- **Per-unit override:** export `SKILL_MODEL` in a systemd unit (e.g. `Environment=SKILL_MODEL=opus`) to pin one job regardless of the default. Empty/unset → routing logic decides.
- **Watch-and-promote:** if a Sonnet-routed job's output quality visibly drops (e.g. `launchd-debugger` fix quality, `deal-aggregator` screening precision), promote it back to Opus via `SKILL_MODEL` or by adding it to `OPUS_SKILLS` — don't suffer silent degradation to save tokens.

Expected effect: ~5x reduction on the programmatic bucket (~$5k → ~$1k/mo), before any frequency/consolidation work. Re-measure against the same 30-day transcript method before 2026-06-15 to confirm the landing spot.

## Wrapper Hardening Pattern (2026-04-25, bead ai-ops-1; doctrine broadened 2026-05-04)

- **POST_RUN_CHECK env var** in plist runs an artifact-integrity validator after Claude exits 0. Non-zero validator → wrapper overrides EXIT_CODE → Slack alert with "VALIDATOR FAILED" prefix. `$TODAY` placeholder in the env var is substituted with current YYYY-MM-DD.
- **Headless prompts** for skills that misbehave under `claude -p` with bare `/skill-name`. Wrapper detects `skill:args` pair and pipes `.claude/skills/{skill}/headless-{mode}-prompt.md` content as Claude's user prompt instead of `/skill-name`. Prompt file forbids clarifying questions and mandates artifact-first ordering.
- **Universal POST_RUN_CHECK doctrine (2026-05-04):** Every scheduled skill needs a validator — no exemptions. Precipitating incident: 2026-05-03 `conference-discovery` Sunday-night run wiped ~70 rows on the Conference Pipeline tab and exited 0 silently; the dashboard reported it healthy because no validator gated the exit code. Read-only skills (deal-aggregator, email-intelligence) get **lighter validators** that check "did the expected artifact land at the expected path?" but are NOT exempt from the post-run check entirely. Mutating skills get artifact + integrity validators (row-count delta, schema, header presence) per the existing pattern. **Hardened mutating skills (now 6):** `target-discovery` Phase 2, Cold Call Operations, `nightly-tracker-audit`, `weekly-tracker`, `relationship-manager`, `conference-discovery`. Each has its own `scripts/validate_{skill}_integrity.py` validator + `headless-{mode}-prompt.md` headless prompt. Wrapper case-statement in `scripts/run-skill.sh` routes `skill:mode` args to the corresponding prompt file. Remaining unhardened skills (read-only + snapshot refreshers + weekly export jobs) are follow-up work — see audit table in any 2026-05-04 hardening session.

## Operations

- **Status check:** `launchctl list | grep greenwich` (Mac) / `systemctl --user list-timers` (VPS)
- **Manual trigger:** `launchctl start com.greenwich-barrow.{skill}` (Mac) / `systemctl --user start {skill}.service` (VPS)
- **Mac must be in sleep mode (not shut down) for scheduled runs to fire.** VPS runs 24/7.
