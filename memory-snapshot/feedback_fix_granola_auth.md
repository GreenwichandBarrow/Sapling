---
name: Fix Granola MCP Auth + No Transcript Pasting
description: Kay doesn't want to paste transcripts into chat — feels less private. Fix Granola MCP auth so transcripts flow silently.
type: feedback
originSessionId: 478b30c8-a8cc-4964-a389-9b94e349abc9
---
Kay does not want to paste full meeting transcripts into the conversation. It feels less private and clutters context.

**Why:** Transcripts contain personal conversations (Camilla's apartment, family details, candid opinions about contacts). Pasting them into chat makes Kay uncomfortable.

**How to apply:** Fix Granola MCP auth at the start of the next session (try fresh auth flow immediately on session start when the localhost listener is active). Once working, pull transcripts silently via MCP — read them in a subagent, extract key points, never surface raw transcript text in conversation.
