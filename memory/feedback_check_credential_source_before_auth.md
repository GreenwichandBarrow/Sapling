---
name: check-credential-source-before-auth
description: "Before invoking ANY interactive auth flow (OAuth, MCP authenticate, login prompt), exhaust the cached-credential ladder first. 1Password → cached MCP tokens → /mcp reconnect → only then OAuth."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7dc0f575-9c45-4aad-9c1c-4d9782371a2c
---

# Check the credential source ladder BEFORE any interactive auth flow

When a tool reports unauthenticated state (`mcp__*__authenticate` surfaced, 401 response, "needs auth" message), DO NOT immediately invoke the interactive OAuth/login flow. Walk this ladder first:

## The ladder (top-down — only fall through when each step fails)

1. **1Password GB Server vault.** Run `op item list --vault "GB Server" --format=json | python3 -c "import json,sys; items=json.load(sys.stdin); [print(i['title']) for i in items if 'SERVICE' in i.get('title','').lower()]"` — substitute the service name. If a credential exists → use it via `op read 'op://GB Server/<title>/<field>'`. Done.

2. **Cached MCP tokens (Claude Code internal).** Check `~/.claude/mcp-needs-auth-cache.json` — if the service is NOT listed there, Claude Code already has valid tokens cached server-side; the session just hasn't picked them up. Action: ask Kay to run `/mcp` to reconnect, OR (if mid-session-rotation) note that a quit+relaunch is needed per `project_claude_code_config_cache`.

3. **Recent MCP log activity.** `ls -t ~/.cache/claude-cli-nodejs/-home-ubuntu-projects-Sapling/mcp-logs-{service}/` — if recent logs (today/yesterday) exist, the service worked recently → tokens almost certainly valid; treat as step 2.

4. **Only after 1–3 all fail → interactive OAuth.** Even then, AFTER successful auth, ask Kay if the resulting credential should be stashed in 1Password for next time.

## Why this rule

Precipitating incident — 2026-05-13, this session. User asked to pull a Granola transcript. I jumped directly to `mcp__granola__authenticate`, generated an OAuth URL, and asked Kay to do the browser dance. She caught it: *"use 1Password always."* On checking AFTER the fact: `mcp-needs-auth-cache.json` did NOT list Granola → tokens were already cached → just needed `/mcp` reconnect. The interactive OAuth was avoidable.

This is the second time in one session I bypassed 1Password. The first was implicit (I read the Attio API key correctly via op://, but only because the bootstrap pattern was muscle-memory — not from running the ladder check).

## How to apply

Whenever you encounter ANY of these signals — fire the ladder before doing anything else:
- A deferred tool shows up as `mcp__*__authenticate`
- A curl/HTTP call returns 401
- A CLI prompts for login or token
- A skill or script errors with "credentials not configured"

The discipline: **never propose Kay perform an interactive auth step until you've shown her the ladder result and at least step 1 (1Password) has been confirmed empty.**

## Linked rules

- [[feedback_all_skills_use_1password]] — the universal policy this complements
- [[project_claude_code_config_cache]] — why /mcp reconnect works vs why relaunch is sometimes needed
- [[feedback_credential_extraction_clean_terminal]] — where to extract secrets when needed
