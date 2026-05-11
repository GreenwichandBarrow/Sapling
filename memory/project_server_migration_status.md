---
name: Server migration status (Hetzner cpx21)
description: Current state of iMac launchd → server systemd migration. Updated 2026-05-08 evening.
type: project
originSessionId: d5485724-ca82-4a50-bf98-38302fa9db3d
---
Hetzner server `agent-vps-7731c88b` (cpx21, 4GB RAM, 3 CPU, Ashburn, ~$11/mo). Provisioned 2026-05-07. Tailscale at `100.67.36.25`. Server user `ubuntu`. Repo at `~/projects/Sapling/`. TZ=America/New_York.

**Why:** Migration goal is iMac/MacBook conference-interchangeable starting next week. Server is single source of truth for control plane; Granola input continues from whichever Mac runs the desktop app (Granola has no Linux/web client). Phase architecture per Harrison Wells' 2026-05-07 doc.

**How to apply:** When migrating future timers, check this file for current status before designing migration plan.

## Phase status (as of 2026-05-08 evening)

| Phase | Status | Notes |
|---|---|---|
| Phase 1 (Linux env smoke) | Done 2026-05-07 | Streamlit booted clean on server |
| Phase 3 (systemd port) | Done 2026-05-07 | 19 unit pairs generated + installed |
| Phase 3.5 (selective enablement) | In progress | dashboard.service + 8 timers + post-call-analyzer-poll active |
| Phase 4 (Granola sidecar handoff) | Commissioned 2026-05-08 | Server-side MCP polling active; iMac sidecar shadow-mode |
| Phase 4.5 (iMac sidecar retirement) | Gated on Mon 5/11 first real call validation | |
| Phase 5 (full server-only) | Future | Granola Mac app stays as input device permanently |

## Server timers enabled (10 total as of 2026-05-08)

- `dashboard.service` (persistent Streamlit at `0.0.0.0:8501`, since 2026-05-07)
- `external-services-probe.timer` (since 2026-05-07)
- `attio-snapshot-refresh.timer` (Mon-Fri 8am-8pm hourly)
- `jj-snapshot-refresh.timer` (Mon-Fri 9am, 2:30pm, 6pm)
- `apollo-credits-refresh.timer` (Mon-Fri 8am-8pm hourly)
- `email-intelligence.timer` (Mon-Fri 7am — first auto-fire Mon 5/11)
- `relationship-manager.timer` (Mon-Fri 6:50am — first auto-fire Mon 5/11)
- `deal-aggregator.timer` (Mon-Fri 6am)
- `deal-aggregator-afternoon.timer` (Mon-Fri 2pm)
- `deal-aggregator-friday.timer` (Friday 6am, digest mode)
- `launchd-debugger.timer` (Daily 5am — first server auto-fire Sat 5/9)
- `post-call-analyzer-poll.timer` (every 5 min, server-wide)

## iMac plists retired (3 total)

- `com.greenwich-barrow.attio-snapshot-refresh.plist` (moved to `~/Library/LaunchAgents-retired/`)
- `com.greenwich-barrow.jj-snapshot-refresh.plist` (same)
- `com.greenwich-barrow.apollo-credits-refresh.plist` (same)

## iMac plists still active (shadow-mode + pending migration)

Shadow mode (server timer + iMac plist both active for one auto-fire validation cycle):
- `com.greenwich-barrow.email-intelligence.plist` (cutover after Mon 5/11 7am validation)
- `com.greenwich-barrow.relationship-manager.plist` (cutover after Mon 5/11 6:50am validation)
- `com.greenwich-barrow.deal-aggregator.plist` + afternoon + friday variants
- `com.greenwich-barrow.launchd-debugger.plist`
- `com.greenwich-barrow.post-call-analyzer.plist` (Phase 4.5 cutover gated on Mon 5/11 first real call)

Still-on-iMac (not yet migrated; weekly-cadence so non-urgent):
- `com.greenwich-barrow.nightly-tracker-audit.plist` (deferred Sat 5/9 — Sheets mutation, cutover-only pattern)
- `com.greenwich-barrow.conference-discovery.plist` (Sunday 9pm)
- `com.greenwich-barrow.niche-intelligence.plist` (Tuesday 22:30)
- `com.greenwich-barrow.weekly-tracker.plist` (Friday morning)
- `com.greenwich-barrow.calibration-workflow.plist` (Thursday 11pm)
- `com.greenwich-barrow.jj-operations-sunday.plist` (Sunday 6pm)
- `com.greenwich-barrow.weekly-snapshot.plist` + `weekly-archive-export.plist`

## Architectural invariants (don't refactor blind)

- **Granola sidecar = iMac OR MacBook** (wherever Granola Mac app runs). Server pulls from Granola Cloud via MCP. Granola itself never moves to server (no Linux client exists).
- **Excel task tracker = iMac via OneDrive.** Server-side post-call-analyzer writes Tasks to a queue file (`brain/trackers/post-call-analyzer/task_queue/`); Phase 4.5+ has an iMac drain script consuming the queue (deferred).
- **Mutating skills must use cutover, not shadow.** Read-mostly skills can shadow safely. See `brain/traces/2026-05-08-mutating-skill-shadow-mode-unsafe.md`.
- **Generator (`scripts/generate_systemd_units.py`) MUST quote-escape `Environment=` values with whitespace** (`format_env_line` helper, added 2026-05-08). Don't remove the helper without a unit test verifying POST_RUN_CHECK env vars survive intact.
- **MCP-first / API-second / ask-Kay-third for any new external integration** (per `feedback_integration_priority_mcp_api_local.md`).

## Authentication state

- Granola MCP authenticated on server via interactive same-session PKCE workaround (2026-05-08). Token persists to disk; `claude -p` subprocesses inherit auth.
- gog v0.15.1 on server with `GOG_KEYRING_BACKEND=file` + `GOG_KEYRING_PASSWORD` in `~/.bashrc` + `scripts/.env.launchd`. Live verified via Gmail labels API.
- Claude Max OAuth on server (since 2026-05-07).
- gh CLI auth on server (since 2026-05-07).
- Tailscale SSH ACL active on server (`sudo tailscale set --ssh`); both Macs connect under `kay.s@` identity.

## Known gaps (post-conference cleanup)

- Friday 6am collision (`deal-aggregator` + `deal-aggregator-friday` both fire 6am Fri). Pre-existing iMac pattern. Stagger fix is one plist edit + regenerate.
- Deal-aggregator has no POST_RUN_CHECK validator. Pre-existing gap; in "unhardened skills" bucket per `feedback_mutating_skill_hardening_pattern.md`.
- gog version drift: MacBook 0.12.0 / iMac 0.13.0 / server 0.15.1. `brew upgrade gogcli` on iMac + MacBook to sync.
- claude.ai Google Drive MCP shows "needs authentication" on server (per Phase 4 plumbing check). Not currently used; auth deferred.
