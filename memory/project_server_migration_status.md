---
name: Server migration status (Hetzner cpx21)
description: Current state of Mac → VPS migration. Updated 2026-06-07 to consolidate Granola server setup under the main server setup project.
type: project
originSessionId: d5485724-ca82-4a50-bf98-38302fa9db3d
---
Hetzner server `agent-vps-7731c88b` (cpx21, 4GB RAM, 3 CPU, Ashburn, ~$11/mo). Provisioned 2026-05-07. Tailscale at `100.67.36.25`. Server user `ubuntu`. Repo at `~/projects/Sapling/`. TZ=America/New_York.

**Why:** Migration goal is iMac/MacBook conference-interchangeable starting next week. Server is single source of truth for control plane; Granola input continues from whichever Mac runs the desktop app (Granola has no Linux/web client). Phase architecture per Harrison Wells' 2026-05-07 doc.

**How to apply:** Treat "server setup" as the umbrella project. Do **not**
surface "Granola server setup" as a separate active project/bead unless a new
Granola-specific defect appears. Granola is part of server setup: the Mac app
remains an input device because Granola has no Linux client, while the server
pulls Granola Cloud via MCP and owns post-call processing.

## Phase status (current canonical framing)

| Phase | Status | Notes |
|---|---|---|
| Phase 1 (Linux env smoke) | Done 2026-05-07 | Streamlit booted clean on server |
| Phase 3 (systemd port) | Done 2026-05-07 | 19 unit pairs generated + installed |
| Phase 3.5 (selective enablement) | Done | Scheduled-skill runtime moved to VPS/systemd |
| Phase 4 (Granola Cloud/MCP integration) | Done / archived into server setup | Server-side MCP polling active; Granola is no longer a separate migration project |
| Phase 4.5 (iMac launchd retirement) | Done 2026-05-10 evening | `launchctl list | grep greenwich-barrow` was empty after retiring post-call-analyzer |
| Phase 5 (VPS-primary work surface) | Confirmed 2026-05-18 | Mac + MacBook are thin Tailscale SSH clients into VPS; see `memory/project_vps_primary_workflow.md` |

## Current operating model

- VPS is the single workspace. Start from cmux `vps`, not local Mac Claude.
- Scheduled skills run as systemd timers on VPS. Use `systemctl --user list-timers` for live state.
- Command Center/dashboard is server-hosted and reachable over Tailscale/Magic DNS.
- Memory lives in repo at `memory/` and each node's path-keyed Claude memory dir symlinks into it.
- GitHub remains the durable repo backup, but day-to-day work originates on VPS.

## Granola handling (combined into server setup)

- Granola Mac app remains on whichever Mac records the meeting. This is an
  input-device constraint, not a separate "Granola server setup" project.
- Server pulls Granola Cloud via MCP for post-call processing.
- `post-call-analyzer-poll.timer` is the sole processor; the Mac
  `com.greenwich-barrow.post-call-analyzer.plist` was unloaded/retired on
  2026-05-10 after the server timer was verified healthy.
- Archive/close any duplicate task framed as "Granola server setup" unless it
  names a new concrete defect (auth broken, transcript backlog, MCP outage,
  duplicate processing, etc.). If a concrete defect exists, file it under the
  broader server setup / post-call-analyzer surface.

## Retired local scheduler model

The old Mac launchd/shadow-mode plan is retired. Do not use the May 8
"still-on-iMac" list as current state. If a local Mac plist appears active,
treat it as a regression or stale local artifact and verify against live
`launchctl list`.

## Architectural invariants (don't refactor blind)

- **Granola app input = iMac OR MacBook** (wherever Granola Mac app runs). Server pulls from Granola Cloud via MCP. Granola itself never moves to server (no Linux client exists).
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

## Known gaps / follow-ups

- Use live systemd state, not historical May 8 notes, before diagnosing timers.
- `bd` install on VPS was captured as friction in `memory/project_vps_primary_workflow.md`; verify live before surfacing.
- `ai-ops-t1q` tracks the systemd `EnvironmentFile=` / `op://` audit.
- `ai-ops-jrj` tracks launchd-wrapper hardening coverage.
