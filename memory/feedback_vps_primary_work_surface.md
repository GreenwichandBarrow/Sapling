---
name: VPS is primary work surface — originate all interactive Claude via `vps`
description: From 2026-05-10 forward, Kay originates all interactive Claude work on the Hetzner cpx21 server via cmux's `vps` alias. Local Mac (iMac, MacBook) Claude is fallback only.
type: feedback
---

Every new interactive Claude session originates on the server. Cmux's `vps` alias Tailscale-SSHs into `agent-vps-7731c88b` and auto-launches Claude inside `~/projects/Sapling/`. Local Mac Claude is reserved for offline/local-only work and is no longer the default.

**Why:** Migration goal per Harrison Wells' 2026-04-30 setup guide — *"iMac/MacBook conference-interchangeable. Server = single source of truth for control plane."* Kay committed to the behavioral change on 2026-05-10 after confirming HeyReach add + Jemden Helmsley Spear Gmail-filter add both executed cleanly from server-side Claude. The architecture only delivers on the migration promise if interactive work originates on server, not just scheduled jobs.

**How to apply:**
- When a new conversation starts, default assumption is **server-side Claude**. `DEVICE_LOCATION=server` env var in session-init confirms.
- Do not recommend "do this from local Mac" except for the three known exceptions: (a) Granola Mac app interaction (no Linux client; data syncs via cloud MCP), (b) Excel task tracker writes (OneDrive, iMac by design — server writes to queue file the iMac drains), (c) MCPs not yet migrated server-side.
- Known authenticated server-side as of 2026-05-10: Claude Max OAuth, gh CLI, gog v0.15.1, Granola MCP. **Attio MCP server-side status not yet confirmed** — verify before committing to Attio-touching work on server.
- Memory now lives in repo at `memory/` (moved 2026-05-10) and is symlinked from each device's path-keyed `~/.claude/projects/<sanitized>/memory/`. Both surfaces read the same files. See `memory/README.md` for the symlink scheme.
- If Kay says she's on local Mac for a specific reason, honor that — don't push her back to server. But "where are you running this?" only needs asking when the answer would change recommendation (MCP-availability gap, OneDrive-dependent work, etc.).
