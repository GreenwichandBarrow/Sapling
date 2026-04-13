---
name: Superhuman MCP is drafts only — never send
description: CRITICAL — superhuman-cli MCP must only create drafts. Never invoke send. Kay reviews and sends manually from Superhuman.
type: feedback
---

The superhuman-cli MCP tool is DRAFTS ONLY. Never invoke superhuman_send or any send function.

**Why:** Kay explicitly confirmed this. She reviews every email before sending. Automated sending is not authorized.

**CRITICAL — Superhuman drafts do NOT mirror Gmail drafts.** The `superhuman_draft` tool must create drafts directly in Superhuman's native draft system, NOT via the Gmail API. Gmail API drafts do NOT appear in Superhuman. This was a bug caught on 2026-03-23 — the Eric Dreyer draft was created via Gmail API and Kay could not see it in Superhuman.

**How to apply:**
- Use `superhuman_draft` tool BUT verify it creates a Superhuman-native draft, not a Gmail draft
- If the tool creates Gmail drafts, this is broken — need to use the compose/draft flow that goes through Superhuman's UI via CDP
- Never use `superhuman_send` even if it exists in the tool list
- Never schedule sending — Kay does that manually via Superhuman's scheduled send
- If Kay asks to "schedule for Monday" — she means she will schedule it in Superhuman herself
- TEST THIS IN THE NEXT SESSION before drafting any real outreach
