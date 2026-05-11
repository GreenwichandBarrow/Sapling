---
name: Claude Code caches MCP server configs at session start
description: 2026-04-27 finding — /mcp reconnect rebuilds from session-start snapshot, not current ~/.claude.json. Edits to MCP env blocks require full Cmd+Q + relaunch to take effect.
type: project
originSessionId: e01b0f15-d8be-4bd0-8424-2b86790ca0c8
---
**Architectural finding from 2026-04-27 incident:**

Claude Code reads `~/.claude.json` MCP server configs ONCE at session start and caches them. Subsequent edits to the file are NOT picked up by `/mcp reconnect` — that command rebuilds the MCP subprocess from the cached snapshot, not from disk.

**Why this matters:** Editing an `ATTIO_API_KEY` (or any MCP env value) in `~/.claude.json` mid-session has zero effect on the running MCP server. Even after `pkill -f "npx.*attio-mcp"` to kill the subprocess and `/mcp reconnect` to spawn a fresh one, the new subprocess still inherits env from the cached snapshot.

**How to apply:**

1. **For mid-session credential rotation that needs to take effect immediately**, the only working path is **Cmd+Q + relaunch Claude Code**. Save state via `/savestate` first, write a continuation file, then close+reopen.

2. **For non-urgent rotations**, just update `~/.claude.json` and `scripts/.env.launchd` and let the next session pick it up naturally.

3. **Don't burn rotations on this**: confirmed today across 4 rotations of the same Attio key. Each rotation: edit file → `/mcp reconnect` → fresh `mcp__attio__*` call still uses the session-start key. Pattern is reproducible and consistent.

4. **The `scripts/.env.launchd` layer is separate** — Python scripts read fresh from disk each launch (`source` in `run-skill.sh`), so launchd-scheduled jobs DO pick up new keys without restart.

5. **Workaround for hot-rotation** if a Claude Code restart is genuinely impossible: spawn a separate process with the new key in env, e.g. `ATTIO_API_KEY=<new> npx attio-mcp ...` outside Claude Code. But this is rarely worth the complexity.

**Receipts (this session, 2026-04-27):**

- 4 Attio key rotations (compromised key was `347a6a5d…`).
- Each rotation: write key to `~/.claude.json` via Python → `/mcp reconnect` → `mcp__attio__*` call still 401s with `347a6a5d` in the leaked Authorization header.
- After session close + relaunch (planned, not yet executed when this memory was written), the cache will flush.

**Confirmed NOT a workaround:** `pkill -f "npx.*attio-mcp"` alone. Killing the subprocess works (system reminder confirms tools disappear), but the next `/mcp reconnect` still uses the cached env. The cache is in Claude Code's process memory, not the npx subprocess's.

**Test for the AI consultant:** Whether there's a `/mcp restart` or `/mcp reload-config` command that flushes the session cache short of full restart. As of 2026-04-27 no such command surfaced in `claude --help` or `/help`.
