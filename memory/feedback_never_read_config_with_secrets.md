---
name: Never use Read tool on config files containing secrets
description: Read tool dumps file content into conversation transcript. Use Bash + grep + cut/awk for secret-containing configs. Self-leak 2026-04-26.
type: feedback
originSessionId: 8cc9b9eb-89cd-43ea-8e11-34566c18e476
---
When inspecting any config file that may contain API keys, tokens, or credentials (`~/.claude.json`, `.env`, `credentials.json`, MCP server configs, `~/.config/`, etc.), NEVER use the Read tool — it dumps file content into conversation context including any secret values, which leaks them into the transcript.

**Why:** 2026-04-26 Sunday morning, while diagnosing Attio MCP credential issue, I used Read on `~/.claude.json` lines 495-525 to inspect the Attio MCP server entry. The `env` block contained `ATTIO_API_KEY` with the literal value. The key is now in this session transcript. Kay had to rotate the key Monday AM as a result.

## Known secret-containing files (NEVER print contents)
- `scripts/.env.launchd` — all G&B service API keys (Attio, Apollo, OpenAI, Anthropic, Slack webhooks, etc.)
- `~/.claude.json` — MCP server env blocks
- `~/.claude/settings.json`, `.claude/settings.local.json` — env values
- `.env`, `.env.*`, `credentials.json`, `secrets/*` (any path), `*.key`, `*.pem`, OAuth token files
- `/tmp/*-key.txt`, `/tmp/*-token.txt` (transient secret-transfer files)

## Safe grep idioms — all suppress values
- Confirm a key exists: `grep -c '^export ATTIO_API_KEY=' file` → returns count only
- Confirm filename matches: `grep -l 'API_KEY' file` → returns filename only
- List variable NAMES (no values): `awk -F= '/^export / {print $1}' file`
- Test syntactic structure: `python3 -c "import json; c=json.load(open('/path')); print(sorted(c.keys()))"` → keys only

## UNSAFE patterns that LEAK — DO NOT USE on secret files
- `grep -nE "PATTERN" file` — `-n` adds line numbers but DOES NOT suppress content; matched lines print verbatim including values. **This is the exact pattern that caused the 2026-04-27 5-key leak.**
- `grep "API_KEY" file` — same problem, prints whole matching line
- `cat`, `head`, `tail`, `less`, `more`, `Read tool` — all dump content
- `sed -n '/PATTERN/p' file` — prints the line including value

## Hard rule
**If the file is plausibly secret-containing, default to `-c` / `-l` / `awk-strip-RHS` patterns. Never use a value-printing pattern. If the diagnostic genuinely needs the value (e.g., comparing to expected), pipe it through redaction (`| cut -c1-8` for first 8 chars) or use `python3` with explicit `print('SET' if k else 'UNSET')`.**

Treat any secret that has appeared in a conversation transcript as compromised — flag rotation immediately.

## Incidents (so the lesson sticks)
- **2026-04-26:** Read tool on `~/.claude.json` → leaked `ATTIO_API_KEY`. Kay rotated.
- **2026-04-27:** `grep -nE "ATTIO|attio.*api.*key|API_KEY" scripts/.env.launchd` → leaked **5 keys** (OpenAI, Salesforge, Motion, Attio, Apollo). Salesforge + Motion accounts being closed; Attio + Apollo + OpenAI rotation pending. Even though I had this memory loaded, I reached for `grep -nE` (value-printing) instead of `awk -F=` (name-only). The lesson: **the pattern matters more than knowing the rule. Always reach for `-c`, `-l`, or `awk-strip-RHS` first; never `grep PATTERN file` on a secret file.**
