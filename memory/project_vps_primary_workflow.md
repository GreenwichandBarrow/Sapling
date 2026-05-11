---
name: VPS-primary workflow trial (Kay shifting off Mac Claude)
description: As of 2026-05-10 evening, Kay is trialing VPS (Sapling Linux server) as her primary Claude Code environment instead of Mac Claude. Mac Claude transitions to secondary / sync-only via git pull.
type: project
---

Kay said on 2026-05-10 evening: "I'm going to try to just work from this VPS
going forward."

This is a **trial**, not a confirmed permanent shift — but the direction is
real and follows naturally from the infra work that landed this weekend:

1. **Credential migration complete (2026-05-10 AM):** All 7 production
   secrets on op://, server has full credential parity with Mac.
2. **Tailscale Serve dashboard (2026-05-10 PM):** Command Center reachable
   from anywhere on the tailnet at
   `https://agent-vps-7731c88b.tail868ef9.ts.net/`.
3. **Memory symlink (2026-05-10 evening):** Server's auto-memory directory
   is now a symlink into the in-repo `memory/` dir, so memory writes flow
   into git and are syncable across machines.
4. **Auto-commit hook live (G&B Server author):** Dashboard YAML + MEMORY.md
   edits get committed automatically during the session, so working from
   VPS no longer leaves an uncommitted-changes drag behind.

**Why:** Working from VPS gives Kay (a) durable long-running sessions that
survive Mac sleep/restart, (b) closer proximity to the actual launchd
scheduled jobs and the dashboard, (c) one canonical workspace instead of
the dual-machine reconcile dance she's been doing. The whole point of the
weekend's infra work was to make this trial possible.

**How to apply:**
- **Default to executing on VPS for any new task in this session.** Don't
  ask "are you on Mac or server" — assume server unless context says
  otherwise.
- **Treat Mac Claude as secondary / read-only** during this trial. It can
  still pull from git, but new memory and skill writes happen here.
- **Scheduling is already on systemd (VPS), not launchd.** As of at least
  2026-05-08 (per `project_systemd_env_quoting_fix.md`), all 21 scheduled
  skills run as systemd timers on the VPS — `nightly-tracker-audit`,
  `niche-intelligence`, `deal-aggregator` (+ variants), `email-intelligence`,
  `relationship-manager`, `target-discovery-sunday`, `jj-operations-sunday`,
  `conference-discovery`, `health-monitor`, `calibration-workflow`,
  snapshot refreshers, etc. CLAUDE.md still references "macOS launchd" in
  the scheduled-skills table — that doc is stale and slated for the Monday
  `ai-ops-gnk` trim. Use `systemctl list-timers` for ground truth, not
  CLAUDE.md.
- **Mac launchctl is now empty of `greenwich` jobs** as of 2026-05-10
  ~22:25 ET. Kay unloaded `com.greenwich-barrow.post-call-analyzer.plist`
  and moved it to `LaunchAgents-retired/`. Server's
  `post-call-analyzer-poll.timer` is now the sole processor. **Phase 4.5
  effectively complete**, ahead of the Mon 5/11 target.
- **Known VPS-trial friction points** (capture as you find them):
  - `bd` (Beads CLI) is **not installed on VPS** as of 2026-05-10 evening.
    Beads is the single task system per CLAUDE.md, so this is a material
    gap. Bead intents captured during VPS sessions go to `scratch/{date}-pending-beads.md`
    as a holding pen until either bd is installed server-side or Kay
    beads them from Mac. (See `scratch/2026-05-10-pending-beads.md` for
    the first one — per-service systemd EnvironmentFile audit, P2.)
- **If the trial fails** (Kay reverts to Mac), the symlink + repo memory
  doesn't have to be undone — it works either direction. Just stop
  assuming VPS-primary.
- **Watch for VPS-only friction points** Kay flags during the trial
  (slower keyboard latency over SSH, missing local files, MCP servers
  that only run on Mac) and surface them so she can decide whether to
  build a fix or fall back.

Source: 2026-05-10 evening server session ending with the memory symlink
migration. Kay's signal was casual ("try") not committed — respect that
in how this is communicated forward.
