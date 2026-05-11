---
created: 2026-05-10
purpose: Hold bead intents captured on VPS while bd CLI is not yet installed there
target: Bead these from Mac (or after bd is installed on VPS) on Mon 2026-05-11
---

# Pending Beads — Captured 2026-05-10 evening

## 1. Per-service systemd EnvironmentFile audit (op:// resolution)

- **Priority:** 2
- **Assignee:** agent
- **Issue type:** task
- **Target batch:** Monday 2026-05-11 infra batch (alongside `ai-ops-gnk` CLAUDE.md trim)

**Description:**

Every `*.service` in `~/.config/systemd/user/` that references
`scripts/.env.launchd` via `EnvironmentFile=` currently emits ~7
`Ignoring invalid environment assignment 'export VAR=op://...'`
warnings on every fire. Root cause: systemd's `EnvironmentFile=`
doesn't support `export VAR=...` shell syntax or resolve `op://` URIs —
only `KEY=value` literal pairs.

On `post-call-analyzer-poll.service` alone (5-min cadence) this is
~2K warning lines/day in journal, drowning real errors. Other services
likely emit the same warnings on their respective cadences.

**Approach: per-service audit, NOT a blanket fix.**

For each `*.service`:

1. Identify which env vars the `ExecStart` binary/script actually reads
   at process start. Grep the target script for `os.environ.get` /
   `getenv` / `$VAR` references.
2. If the script reads **zero** of those vars (e.g.
   `post_call_analyzer_mcp_poll.py` — only does Granola MCP detection
   via `claude -p`, doesn't touch ATTIO/SLACK/APOLLO/GOG creds at
   process start) → safe to **REMOVE** the `EnvironmentFile=
   scripts/.env.launchd` line entirely.
3. If the script needs those vars at process start → either
   (a) drop-in resolver that op-injects values into a runtime
   .env file systemd can parse, or (b) wrap `ExecStart` in a shell
   that sources `load-env.sh` and exports resolved values before exec.
4. Reload daemon + verify no journal warnings on next fire.

**Why not blanket-strip:** Some services legitimately need
`ATTIO_API_KEY` / `SLACK_WEBHOOK_*` / `GOG_KEYRING_PASSWORD` at process
start and would silently break if we strip `EnvironmentFile=` without
checking. The journal warnings hide real failures, so a blanket fix
could mask the very class of bug we want to surface.

**Precipitating context:** 2026-05-10 evening diagnostic on
`post-call-analyzer-poll.timer` — calls landing in vault, timer healthy,
but journal is drowning in env-load warnings.

---

## VPS-trial blocker: install `bd` CLI

While capturing this bead from the VPS, discovered `bd` is not installed
on the server. Without it, Kay can't create or update beads from server
Claude during the VPS-primary trial. Options:

- `go install github.com/<beads-repo>` (canonical install path TBC — Kay
  knows or check Mac's `~/.go/bin/bd` provenance)
- Or download a release binary if beads ships one

This is a material gap for the VPS-primary trial since beads is the
single task system per CLAUDE.md.
