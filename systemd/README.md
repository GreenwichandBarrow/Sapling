# Systemd unit templates (Phase 3 Linux migration)

Generated 2026-05-07 by `scripts/generate_systemd_units.py`. 16 unit pairs (32 files).

Do not edit by hand. To regenerate: re-run the generator script on the iMac (the only host with the source plists).

## Generated units

- `calibration-workflow.service` + `calibration-workflow.timer`
- `conference-discovery.service` + `conference-discovery.timer`
- `deal-aggregator.service` + `deal-aggregator.timer`
- `email-intelligence.service` + `email-intelligence.timer`
- `external-services-probe.service` + `external-services-probe.timer`
- `health-monitor.service` + `health-monitor.timer`
- `jj-operations-sunday.service` + `jj-operations-sunday.timer` — legacy installed alias for Cold Call Operations Sunday prep; intentionally on-demand/disabled as of 2026-07-17
- `launchd-debugger.service` + `launchd-debugger.timer`
- `niche-intelligence.service` + `niche-intelligence.timer`
- `nightly-tracker-audit.service` + `nightly-tracker-audit.timer`
- `relationship-manager.service` + `relationship-manager.timer`
- `target-discovery-sunday.service` + `target-discovery-sunday.timer`
- `weekly-archive-export.service` + `weekly-archive-export.timer`
- `weekly-snapshot.service` + `weekly-snapshot.timer`

## Excluded plists

- `post-call-analyzer` — WatchPaths-driven or no schedule (excluded)

## Install on server

Run `bash scripts/install_systemd_units.sh` on the server.
Units are installed but **not enabled** — enable selectively per skill.

Current operating status: Cold Call Operations Sunday prep and Phase 2 target discovery are intentionally on-demand as of 2026-07-17. Legacy `jj-operations-sunday.timer`, canonical `cold-call-operations-sunday.timer`, and `target-discovery-sunday.timer` may remain installed and disabled without being treated as health failures.

