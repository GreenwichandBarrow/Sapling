---
name: HARD RULE — Drafts never wrapped in blockquote bar
description: GOTCHA-level rule. ANY text Kay might copy/paste (email drafts, Slack messages, profile field copy, doc-edit previews, snippets) is rendered as plain text. NEVER `>` blockquote, NEVER leading bar of any kind. Reinforced 2026-04-30 after repeat violations.
type: feedback
originSessionId: 6a2d9cb0-ae3d-480f-bb1e-a106abec3fe3
---
**HARD RULE / GOTCHA:** ANY text Kay might copy and paste — email drafts, Slack messages, profile-field copy (BizBuySell, LinkedIn, etc.), doc-edit previews, vault snippets, intermediary outreach, broker/IB/lender templates, **agent-to-agent paste (e.g. instructions she's relaying to a server claude or another session)**, anything she might lift from chat into a destination — is rendered in **plain text** with no leading bar of any kind.

Specifically forbidden in any draft/copy-paste context:
- Markdown blockquote (`>`)
- Code fences (```)
- Indented code blocks (4-space leading indent)
- Any visual container that produces a vertical bar in the rendered terminal output

Reinforced 2026-04-30 after this rule was violated multiple times in a single session despite being in memory since the original 2025-12 calibration. Reinforced again 2026-05-10 after wrapping agent-to-agent paste content (instructions for server claude) in `>` bars — same paste friction, same rule.

**Why:** Blockquote rendering in the terminal puts a vertical bar on the left margin. When Kay copies the draft to paste into Superhuman or Slack, the bar character (or the surrounding whitespace) comes along and breaks the paste. She manually has to clean each line, which is exactly the friction the draft-review loop is supposed to eliminate.

**How to apply:**
- Drafts go as plain paragraphs separated by blank lines.
- Lists inside drafts can use `-` bullets (those are fine in source text).
- Reserve `>` blockquote for *quoting somebody else's text back* (e.g. quoting Andrew's email when explaining context), never for showing drafts you authored.
- Code fences are fine for non-text artifacts (commands, JSON, calendar event objects) — just not for drafts meant for copy/paste.
- This rule supersedes the prior implicit pattern of using `>` for visual separation. Use whitespace + bold-label headers instead.
