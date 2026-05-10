# Server Cutover Runbook — fully on server-Claude by Monday

**Created:** 2026-05-09 12:30 EDT
**Status:** Ready to execute when Kay returns to Mac
**Goal:** All scheduled work running on Hetzner server by Monday morning briefing. Post-call-analyzer = Phase 4.5 Monday cutover (eyes-on, separate runbook).

**Prereq:** Tailscale SSH re-auth — visit URL printed on first SSH attempt. ~30 sec.

## Inventory (verified 2026-05-09 12:30 EDT, all 16 unit pairs present in `systemd/`, all validators present in `scripts/`)

| Group | Skill | Schedule | Validator | iMac action |
|---|---|---|---|---|
| A — fresh enable | nightly-tracker-audit | daily 23:30 | yes | retire |
| A | conference-discovery | Sun 21:00 | yes | retire |
| A | niche-intelligence | Tue 22:30 | yes | retire |
| A | calibration-workflow | Thu 23:00 | none | retire |
| A | jj-operations-sunday | Sun 18:00 | yes | retire |
| A | target-discovery-sunday | Sun 15:00 | yes | retire |
| A | weekly-snapshot | Fri 22:00 | none | retire |
| A | weekly-archive-export | Sat 09:00 | none | retire |
| A | external-services-probe | Mon-Fri 8am-8:30pm (×26) | none | retire |
| A | health-monitor | Fri 00:30 | none | retire |
| B — already on server | deal-aggregator | Mon-Fri 06:00 | yes | retire |
| B | deal-aggregator-afternoon | Mon-Fri 14:00 | yes | retire |
| B | deal-aggregator-friday | Fri 06:00 | yes | retire |
| B | email-intelligence | Mon-Fri 07:00 | none | retire |
| B | relationship-manager | Mon-Fri 06:50 | yes | retire |
| B | launchd-debugger | daily 05:00 | yes | retire |
| C — Phase 4.5 Mon | post-call-analyzer | WatchPaths | yes | KEEP — retire Mon after first call validates |

## Execution

### Step 1 — Local: confirm clean git state

```bash
cd "/Users/kaycschneider/Documents/AI Operations"
git status systemd/ scripts/
# expected: clean. push if not.
```

### Step 2 — Server: pull + install all unit pairs (one SSH, idempotent)

```bash
ssh ubuntu@100.67.36.25 'cd ~/projects/Sapling && git pull && bash scripts/install_systemd_units.sh && systemctl --user daemon-reload'
```

Idempotent — copies `systemd/*.timer` + `*.service` into `~/.config/systemd/user/`, sets timezone, runs `daemon-reload`. Already-installed units get overwritten.

### Step 3 — Server: enable + start Group A timers (10 timers)

```bash
ssh ubuntu@100.67.36.25 'for t in nightly-tracker-audit conference-discovery niche-intelligence calibration-workflow jj-operations-sunday target-discovery-sunday weekly-snapshot weekly-archive-export external-services-probe health-monitor; do
  systemctl --user enable --now "${t}.timer" && echo "ENABLED ${t}.timer"
done'
```

### Step 4 — Server: verify 16 timers loaded

```bash
ssh ubuntu@100.67.36.25 'systemctl --user list-timers --all | grep -c greenwich-barrow'
# expected: 16
ssh ubuntu@100.67.36.25 'systemctl --user list-timers --all | grep greenwich-barrow'
# inspect: every NEXT column should be a sane future timestamp
```

### Step 5 — Local: retire 16 iMac plists in batch

```bash
RETIRE=(
  calibration-workflow conference-discovery jj-operations-sunday niche-intelligence
  nightly-tracker-audit target-discovery-sunday weekly-snapshot weekly-archive-export
  external-services-probe health-monitor
  deal-aggregator deal-aggregator-afternoon deal-aggregator-friday
  email-intelligence relationship-manager launchd-debugger
)
RETIRED_DIR=~/Library/LaunchAgents-retired
mkdir -p "$RETIRED_DIR"
for n in "${RETIRE[@]}"; do
  P=~/Library/LaunchAgents/com.greenwich-barrow.${n}.plist
  if [ -f "$P" ]; then
    launchctl unload "$P" 2>&1 && mv "$P" "$RETIRED_DIR/" && echo "RETIRED ${n}"
  else
    echo "SKIP ${n} — already retired"
  fi
done
```

### Step 6 — Local: verify iMac launchd empty (only post-call-analyzer remains)

```bash
launchctl list | grep greenwich-barrow
# expected: only com.greenwich-barrow.post-call-analyzer
```

### Step 7 — Tonight's validation (23:30 EDT, hands-off)

`nightly-tracker-audit` fires on server. If clean: artifact landed at expected path, launchd-debugger Sun 5am scans no failure, Slack quiet.

If it fails: iMac plist file at `~/Library/LaunchAgents-retired/com.greenwich-barrow.nightly-tracker-audit.plist` — 1-command revert: `mv` back + `launchctl load`.

## Post-cutover Monday morning sequence

1. **Mon 06:00 — `deal-aggregator`** first server-side weekday-morning fire. Watch Slack for Sapling-deals webhook ping.
2. **Mon 06:50 — `relationship-manager`** first server-side fire. Artifact at `brain/context/relationship-status-2026-05-11.md`.
3. **Mon 07:00 — `email-intelligence`** first server-side fire. Artifact at `brain/context/email-scan-results-2026-05-11.md`.
4. **Mon 07:30 — Kay says good morning** — pipeline-manager reads server-written artifacts (transparent — should look identical to iMac runs).
5. **Mon (after first real call processes)** — Phase 4.5 cutover for post-call-analyzer: stop iMac sidecar, retire iMac plist, delete `scripts/post_call_analyzer_poll.py`.

## Rollback

If any step 1-6 fails:
- Server: `systemctl --user disable --now <timer>.timer`
- iMac: `mv ~/Library/LaunchAgents-retired/com.greenwich-barrow.<name>.plist ~/Library/LaunchAgents/ && launchctl load ~/Library/LaunchAgents/com.greenwich-barrow.<name>.plist`

No data-loss surface in steps 1-4 (read-only on server). Steps 5-6 reversible via the retire-dir mv.

## Risk callouts

- **Weekly timers won't validate on schedule before Monday.** niche-intelligence (Tue), calibration-workflow (Thu), conference-discovery (Sun), weekly-snapshot/archive-export (Fri/Sat) all fire on their own cadence. First failures show mid-week. Mitigation: cold-backup plists in `LaunchAgents-retired/` for 1-line revert.
- **Group B "already enabled"** means the server timer is loaded, but the iMac plist has been firing in shadow-mode. Retiring iMac de-shadows; if the server timer has a config defect (e.g., env var not propagated), next fire fails with no iMac fallback. Cold-backup mitigates.
- **`external-services-probe` fires 26× per weekday.** First weekday post-cutover (Mon) is the highest-volume validation surface. If it loops or spams, easy to spot.
- **Tailscale SSH session timeout.** Re-auth must be re-done if the cutover spans hours. Run all SSH steps in one window if possible.
