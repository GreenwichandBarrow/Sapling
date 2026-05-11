---
name: Morning briefing always includes clickable dashboard link
description: The header line of every morning briefing must include the Command Center URL as a clickable markdown link, not bare text. Kay wants one-click open every morning.
type: feedback
originSessionId: f8be9c15-9637-4853-b0f6-7cf93e164c94
---
Every morning briefing's header line must render the Command Center URL as a **clickable markdown link**, not as bare text.

**Right:** `System status + pipeline + outreach metrics live at [http://localhost:8501](http://localhost:8501).`

**Wrong:** `... live at localhost:8501.` (bare text — not clickable in terminal)

**Why:** Kay opens the briefing in terminal every morning and wants to click through to the dashboard immediately for the full context. Bare-text URLs require copy/paste, which adds a step.

**How to apply:**
- Every `/goodmorning` briefing header line includes `[http://localhost:8501](http://localhost:8501)` as a clickable link.
- The dashboard skill auto-launches the dashboard if it's not already running. If it IS running, just include the link.
- This applies to the header line specifically — not every mention of the dashboard in conversation needs to be a link.
- CLAUDE.md "Morning Workflow" Step 9 codifies this. If the briefing template ever moves out of CLAUDE.md, the rule moves with it.

**Precedent:** 2026-04-28 morning briefing — Kay asked "can you always include the link for the morning briefing" after seeing the bare-text version.
