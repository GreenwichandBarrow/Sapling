---
name: Superhuman CLI setup
description: superhuman-cli installation, MCP config, LaunchAgent, and token refresh for native Superhuman draft creation
type: reference
---

## Setup (completed 2026-03-18)

**Problem:** Superhuman's official remote MCP server (`mcp.mail.superhuman.com` via `mcp-remote`) OAuth auth was failing. Root cause: Superhuman doesn't use Gmail's draft system — they have a proprietary draft service. Gmail API drafts (via gog) never appear in Superhuman.

**Solution:** Community `superhuman-cli` by edwinhu. Connects to Superhuman desktop app via Chrome DevTools Protocol (CDP). Creates native Superhuman drafts.

## Components

- **CLI:** `/Users/kaycschneider/.local/share/superhuman-cli/` (cloned from github.com/edwinhu/superhuman-cli)
- **Runtime:** `bun` (installed via Homebrew, v1.3.11)
- **MCP config:** `~/.claude/.mcp.json` — server name `superhuman`, runs via `bun src/index.ts --mcp`
- **LaunchAgent:** `~/Library/LaunchAgents/com.superhuman.debug.plist` — auto-starts Superhuman with `--remote-debugging-port=9400` on login
- **Safety script:** `~/.local/bin/ensure-superhuman-debug.sh` — relaunches Superhuman with debug flag if opened without it
- **Draft wrapper:** `~/.local/bin/superhuman-draft.sh` — single entry point for all draft creation. Handles launch, token refresh, retry. ALL skills must use this, never the raw CLI.
- **Token cache:** `~/.config/superhuman-cli/tokens.json` — valid ~1 hour (wrapper auto-refreshes)

## Accounts (all 6 extracted)

1. kay.s@greenwichandbarrow.com (primary for G&B work)
2. kaycfofana@gmail.com
3. kcs211@stern.nyu.edu
4. myselfrenewed@gmail.com
5. pantheragreyholdings@gmail.com
6. kaigreyventures@gmail.com

## Token refresh

```bash
# Superhuman must be running with debug port
CDP_PORT=9400 bun run /Users/kaycschneider/.local/share/superhuman-cli/src/cli.ts account auth
```

## MCP tools available

Draft: `superhuman_draft`, `superhuman_send`, `superhuman_reply`, `superhuman_reply_all`, `superhuman_forward`
Read: `superhuman_inbox`, `superhuman_search`, `superhuman_read`
Manage: `superhuman_archive`, `superhuman_delete`, `superhuman_mark_read`, `superhuman_mark_unread`
Organize: `superhuman_labels`, `superhuman_add_label`, `superhuman_remove_label`, `superhuman_star`, `superhuman_snooze`
Other: `superhuman_attachments`, `superhuman_snippets`, `superhuman_accounts`, `superhuman_ask_ai`, `superhuman_calendar_*`
