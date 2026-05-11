---
name: Email drafts via Gmail only — Superhuman sunset
description: Kay no longer uses Superhuman. All email drafts created in Gmail directly (gog gmail draft / Gmail compose UI). Supersedes all prior Superhuman draft memories.
type: feedback
originSessionId: e26dda1b-d8f3-41ea-b671-19271a6fed00
---
**Rule: Kay no longer uses Superhuman as of 2026-04-29. All drafts are created in Gmail directly. Never propose Superhuman drafts, never use the Bash superhuman-draft.sh wrapper, never reference Superhuman MCP tools as a draft surface.**

**Why:** Kay sunset Superhuman after the cancellation/refund flow on 2026-04-28. Superhuman's value vs cost (Mimestream / Apple Mail + Gmail filters) didn't pan out. Workflow is now Gmail-native.

**How to apply:**

1. **Drafting:** Use `gog gmail draft` or have Kay compose in Gmail UI. The previous `~/.local/bin/superhuman-draft.sh` wrapper is deprecated — do not call it.

2. **CLAUDE.md and skill files** that reference Superhuman as the draft surface need to be updated when next encountered. Don't bulk-rewrite — update inline as each skill is touched.

3. **The following memory files are now SUPERSEDED by this one** (stale, can be deleted in next calibration sweep):
   - `feedback_drafts_superhuman.md`
   - `feedback_drafts_in_superhuman_not_cursor.md`
   - `feedback_superhuman_drafts_only.md`
   - `feedback_superhuman_down_suppress_drafts.md`
   - `feedback_superhuman_token_fallback.md`
   - `reference_superhuman_cli.md`

4. **Signature:** Kay's Gmail signature handles the full block (name, title, email, website, confidentiality). Drafts should sign off `Very best,\nKay` only — same convention as before, just routed through Gmail now.

5. **MCP tools to ignore:** all `mcp__superhuman__*` tools — both the read tools (search, inbox) and the draft tools — are no longer the workflow. If they're listed in deferred tools, don't pick them up.

**Source:** Kay 2026-04-29 conversation: "FYI we are not using superhuman anymore, just gmail."
