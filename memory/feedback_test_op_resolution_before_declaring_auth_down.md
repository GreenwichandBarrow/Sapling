---
name: feedback-test-op-resolution-before-declaring-auth-down
description: Reproduce gog/op/1Password failures through the scheduled resolution path before escalating an auth outage
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7b223302-fb2c-4eb1-b17a-bf9f0dcd0466
---

A failing `op whoami` / `gog` call in the **interactive shell** is the expected state on this VPS, not an incident. The interactive shell does NOT source `~/.config/op-sa-token.env`; scheduled jobs DO, via systemd `EnvironmentFile=%h/.config/op-sa-token.env`.

**Why:** On 2026-05-16 a bare-shell `op whoami` (0 accounts) led to a ~12-minute false 🔴 escalation declaring gog/Gmail/Calendar/Sheets and all 7 op:// secrets down and proposing a new service account. The SA token was valid the whole time; only one wrapper (`export-weekly-archive-to-sheet.sh`) had a real bug.

**How to apply:** Before declaring gog/op/1Password down, reproduce through the scheduled path:
`. ~/.config/op-sa-token.env; source scripts/load-env.sh; load_env scripts/.env.launchd` then test `op inject` + a value-suppressed `gog calendar`. If those exit 0, there is no outage — look for a single wrapper that bypasses `run-skill.sh`/`load-env.sh`. Related: [[reference-gog-interactive-unlock-recipe]], [[reference-vps-broken-pipe-use-agent-tmux]], [[traces/2026-05-16-gog-false-alarm-test-resolution-path]]
