---
schema_version: 1.1.0
date: 2026-05-07
type: migration-report
status: draft
projects: []
tags:
  - date/2026-05-07
  - output
  - output/migration-report
  - status/draft
  - topic/server-migration
  - topic/dashboard
  - topic/linux-port
---

# Dashboard Linux Migration Report

Spot-checks confirmed the audit. Headline: most of the heavy lifting is already portable (snapshot paths are repo-relative, Streamlit config is `headless = true`), but **three shell wrappers and one launchd dependency** are the load-bearing macOS tie-ins.

---

## 1. What's already Linux-clean

- All three snapshot files (`brain/context/{attio-pipeline,jj-activity,apollo-credits}-snapshot.json`) are computed via `Path(__file__).resolve().parent.parent` in both the dashboard loaders (`dashboard/data_sources.py:23–29`, `:1228`) and the refresh scripts (`scripts/refresh_*.py`). No path changes needed in the Python.
- `dashboard/.streamlit/config.toml` already sets `server.headless = true` and disables usage stats — server-friendly out of the box.
- No `watchdog`/`fsevents`/`kqueue` usage. The dashboard polls JSON files; refresh is push-based via cron-style fires.
- `curl`, `lsof`, `find`, `date` — used in shell wrappers, all standard on Ubuntu.

## 2. Hardcoded macOS paths (must fix)

| File | Line | Offending value |
|---|---|---|
| `scripts/refresh-attio-snapshot.sh` | 13 | `REPO_ROOT="/Users/kaycschneider/Documents/AI Operations"` |
| `scripts/refresh-jj-snapshot.sh` | 12 | same |
| `scripts/refresh-apollo-credits.sh` | 12 | same |
| `scripts/probe-external-services.sh` | 11 | same |
| `scripts/run-skill.sh` | 20 | `$HOME/Documents/AI Operations` |
| `scripts/refresh-jj-snapshot.sh` | 29 | `PATH="...:/opt/homebrew/bin:..."` (Homebrew prefix) |
| `scripts/refresh_jj_snapshot.py` | 37 | gog OAuth credentials at `~/Library/Application Support/gogcli/credentials.json` |
| `scripts/post_call_analyzer_poll.py` | 25–27 | `~/Library/Application Support/Granola/cache-v6.json` + Documents/AI Operations |
| `dashboard/data_sources.py` | 72 | `Path.home() / "Library" / "LaunchAgents"` |

Fix pattern for the shell wrappers: replace the literal with `REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"` so they self-locate from their own path. That's the same idiom the Python scripts already use.

## 3. macOS-only commands

| File | Line | Command | Replacement |
|---|---|---|---|
| `dashboard/data_sources.py` | 828 | `subprocess.run(["launchctl", "list"], …)` | systemd: `systemctl --user list-units --type=timer`, or read crontab; or stub on Linux and rely on a different scheduler-status source |
| `scripts/run-skill.sh` | 48 | `security unlock-keychain` | Drop entirely on Linux — secrets come from `.env.launchd` already |
| `scripts/run-skill.sh` | 53 | `\| say OK` (text-to-speech preflight) | Drop, or replace with `echo` |
| `dashboard/README.md` | 14 | `open http://localhost:8501` | `xdg-open` (doc-only change) |

## 4. launchd surface area

This is the biggest conceptual port. Every scheduled skill in `CLAUDE.md` (10+ jobs) currently runs via `~/Library/LaunchAgents/com.greenwich-barrow.{skill}.plist`. The dashboard reads launchd state directly:

- `dashboard/data_sources.py:72,74` — `LAUNCH_AGENTS_DIR`, `LAUNCHD_LABEL_PREFIX`
- `dashboard/data_sources.py:825–893` — `_registered_skills()`, `_read_plist()`, `_format_schedule()` (parses `StartCalendarInterval`)
- `dashboard/data_sources.py:1242–1368` — `load_system_health()` reports launchd registration
- `dashboard/pages/c_suite_skills.py:1–22, :451` — page docstring + plist references
- `dashboard/pages/infrastructure.py:10–11` — references launchctl/plist count
- `scripts/scan_launchd_failures.py` — scans `logs/scheduled/*.log`

Two viable options on Linux:

- **A. systemd user timers** (recommended). One `.timer` + `.service` per skill under `~/.config/systemd/user/`. Translate `StartCalendarInterval` → `OnCalendar=` directives. Replace `launchctl list` with `systemctl --user list-units --type=timer --all`. Replace plist parsing with reading `.timer` files. Logs go to `journalctl --user -u {skill}.service`, not `logs/scheduled/`.
- **B. cron + a shim**. Faster to stand up but loses the structured "registered / next-fire / last-exit" data the dashboard surfaces today. You'd lose the c_suite_skills page or have to fake it.

If you want minimal dashboard surgery, write a thin `_scheduler_adapter.py` that returns the same dataclasses (`ScheduledSkill`, `is_registered`, `next_fire`, `last_log`) regardless of backend. Page code keeps working.

## 5. Native-app integrations to revisit

- **Granola** (`scripts/post_call_analyzer_poll.py`): cache lives at `~/Library/Application Support/Granola/cache-v6.json` on macOS. Granola has no native Linux client — either keep this poller running on the local Mac and ship its output to the server, or move to Granola's API if/when one exists. Listed as Healthy in `dashboard/data/external_services.yaml:65–70`.
- **Superhuman**: already sunset 4/29 per CLAUDE.md, so no action.
- **iMessage / Notes / osascript / pbcopy**: none found in the audited surface.

## 6. Python deps to install

No `requirements.txt` / `pyproject.toml` exists at repo root. Imports across `dashboard/` and the refresh scripts:

- Third-party: `streamlit`, `pandas`, `pyyaml`, `requests`
- Stdlib only: `plistlib`, `pathlib`, `dataclasses`, `subprocess`, `json`, `datetime`, `html`, `re`, `os`, `sys`

Recommend creating a `dashboard/requirements.txt` during the migration so the venv is reproducible. `plistlib` is stdlib on Linux too, so the launchd reader still imports — it's the data source (`~/Library/LaunchAgents/`) that disappears.

## 7. Env vars and external CLIs

Env vars (all read from `scripts/.env.launchd` today): `ATTIO_API_KEY`, `APOLLO_API_KEY`, `ANTHROPIC_API_KEY`, `GOG_ACCOUNT`, `JJ_CALL_NICHES`, `SLACK_WEBHOOK_*`. Drop `KEYCHAIN_PASSWORD` — Linux doesn't need it.

CLI tools the wrappers shell out to: `gog` (Google Workspace CLI — must be on `$PATH`, install separately), `curl`, `lsof`. No `bd`, `gh`, or `jq` dependency in the dashboard surface.

## 8. How it's served today

```
dashboard/.venv/bin/streamlit run dashboard/command_center.py
```

Default port 8501, headless mode already on. The README's `open http://localhost:8501` is the only browser-launch reference (no `webbrowser.open()` in code). On a VPS this becomes "bind and reverse-proxy or SSH-tunnel" — there's no desktop session for `xdg-open` to attach to.

---

## Suggested migration plan

**Phase 1 — Make it boot (1–2 hours).** Create `dashboard/requirements.txt`, build a Linux venv, fix the 5 shell-script `REPO_ROOT` lines to self-locate, drop the `security unlock-keychain` and `say` lines from `run-skill.sh`, run `streamlit run` and confirm pages render. Expect c_suite_skills + infrastructure pages to show "launchctl unavailable" via the existing fallback at `data_sources.py:1357` — that's fine for a smoke test.

**Phase 2 — Decide scheduler (decision needed).** systemd user timers vs cron vs "scheduling stays on the Mac, server is read-only." The third option is real: if the local Mac keeps firing the launchd jobs and pushing snapshots into git or an S3 bucket the VPS pulls from, the server only renders. Cheapest port, but adds a sync hop.

**Phase 3 — Port the scheduler (if Phase 2 picks systemd/cron).** Translate every `com.greenwich-barrow.*.plist` to a `.timer`/`.service` pair. Write `_scheduler_adapter.py` so `data_sources.py` and the c_suite_skills + infrastructure pages keep working unchanged. Translate the launchd POST_RUN_CHECK pattern into systemd's `ExecStartPost=`.

**Phase 4 — Granola.** Either leave the poller on the Mac (simplest) or wait for an API. Don't try to read `~/Library/Application Support/` on Linux.

**Phase 5 — Access.** SSH tunnel for solo use (`ssh -L 8501:localhost:8501`) or nginx + auth + TLS if anyone else needs it. Streamlit's `headless = true` is already correct for either.

**Open question worth pinning before Phase 1:** is this server meant to *replace* the Mac runtime, or *mirror* it? That changes whether Phase 3 is mandatory or optional.
