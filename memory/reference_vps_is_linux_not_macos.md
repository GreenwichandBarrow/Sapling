---
name: The control-plane VPS is Linux/systemd, NOT macOS — scripts must be cross-platform
description: All scheduled jobs, credential resolution, and dashboard feeds run on a Hetzner Ubuntu/systemd VPS. macOS assumptions (launchd/launchctl, ~/Library, LaunchAgents, Keychain) silently break here. Default to cross-platform paths.
type: reference
---

**Rule:** The control plane runs on `agent-vps-7731c88b` — Ubuntu 24.04, **systemd**, user `ubuntu`, repo `~/projects/Sapling/`. Any script, scheduled skill, validator, or dashboard feed MUST be written cross-platform (or Linux-first). macOS-isms are silent failures here:

| macOS assumption | Linux/systemd reality | Correct pattern |
|---|---|---|
| `launchd` / `launchctl` / LaunchAgents `.plist` | `systemd` timers + units | `systemctl --user list-timers`, `*.timer`/`*.service` |
| `~/Library/Application Support/...` | `~/.config/...` / `~/.local/...` | XDG base dirs; resolve via `$HOME` + platform check |
| macOS Keychain / `security` CLI | file-based creds (`~/.config/gogcli/credentials.json`) | platform-aware resolver, never a hardcoded mac path |
| `pbcopy` / `osascript` / `open` | not present | guard or use Linux equivalents |
| Granola desktop app local files | no Linux client | data flows via cloud MCP, not local file reads |

**Why:** On 2026-05-17 three distinct things broke from the same root cause class — all macOS-on-Linux assumptions on the systemd VPS:
1. **JJ credentials** — `refresh_jj_snapshot.py` resolved a macOS credential path; fixed with a cross-platform resolver landing on `/home/ubuntu/.config/gogcli/credentials.json`.
2. **Dashboard C-Suite page** — fed by a job assuming launchd/mac paths.
3. **Dashboard Infrastructure page** — same class.

This is a recurring ≥3x pattern in a single session, not a one-off. The system was originally built on Kay's iMac (launchd) and migrated to Hetzner systemd (Phase 3+, see `project_server_migration_status.md`). Migrated-but-not-ported code carries mac assumptions that fail silently — no crash, just zero rows or stale panels, which is exactly the failure mode loud validators are meant to catch.

**How to apply:**
- When writing or editing any script/scheduled job/feed: assume Linux/systemd. Never hardcode `~/Library`, `launchctl`, LaunchAgents, Keychain, `pbcopy`, `osascript`.
- Credential/path resolution: use a platform check or XDG dirs; resolve from `$HOME`, don't assume a macOS layout.
- Scheduling: it's `systemd` timers, verified via `systemctl --user list-timers`. "Did it fire?" is a systemd question, not a `launchctl` one.
- Reviewing a stale dashboard panel or empty snapshot: suspect a macOS-ism in the producing script BEFORE assuming the source is genuinely empty.
- Known Mac-only exceptions (data via cloud, not local): Granola desktop app input; OneDrive/Excel task-tracker writes on the iMac. Everything else is server-side Linux.

**Source:** 2026-05-17 evening — JJ cred fix + C-Suite + Infrastructure page diagnosis all root-caused to macOS-on-Linux assumptions. Keystone follow-up = task 13 (sweep scripts/dashboard for macOS-isms → systemd/cross-platform).
