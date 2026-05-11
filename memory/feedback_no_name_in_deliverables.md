---
name: Never use Kay's first name in any artifact that lives outside a private conversation
description: Any Google Sheet, Google Doc, PPTX, scorecard, one-pager, brief, meeting doc, operational list, or Drive artifact — internal or external — must use "G&B" or "Greenwich & Barrow", never "Kay". Applies regardless of audience or formality.
type: feedback
originSessionId: 848374e5-1268-4868-935b-ca7f12026b58
---
Never use "Kay" in any artifact that lives outside a private conversation with her. This includes — but is not limited to — Google Sheets (operational trackers, sourcing lists, target lists, status sheets), Google Docs (one-pagers, scorecards, buy-boxes, thesis docs, meeting briefs), PPTX decks (investor, analyst, external), markdown files in Drive, and anything shared with the analyst or any team member.

"Pending Kay registration," "Kay likely has account," "Kay has annual membership" — all violations, even in an internal operational sheet. The rule is not about audience or formality; it's about any written artifact that persists beyond a live conversation.

**Correct framings:**
- "Pending G&B registration"
- "G&B likely has account — verify saved searches"
- "G&B member account"
- "G&B network includes..."
- "G&B luxury background"

**Why:** 2026-03-26 — Kay first codified the rule around professional deliverables. 2026-04-21 — I violated it in the Deal Aggregator Sourcing List sheet (12 cells used "Kay"). Kay corrected: "please update in your system." The original memory was scoped to "professional deliverables" which let me rationalize an operational discussion sheet as different. It is not different. Any written artifact gets G&B framing, period.

**How to apply:** Before writing ANY cell, field, note, or line into a sheet, doc, deck, or file, scan for "Kay" and replace with "G&B" or "Greenwich & Barrow" — regardless of whether the artifact is formal or informal, internal or external, draft or final. No exceptions except when Kay explicitly authorizes personal naming (e.g., personal email signature blocks).

**Enforcement (added 2026-04-24):** graduated to PostToolUse hook `.claude/hooks/router/handlers/no_kay_in_deliverables.py` (registered in `post_tool_use.py`, matcher `Write|Edit`). Hook fires on Write/Edit calls with `file_path` matching `brain/outputs/`, `brain/briefs/`, `brain/library/client-facing/`, or staged `/tmp/*-(onepager|scorecard|brief).md` paths. Scans the incoming content for "Kay" as a bounded token (`\bKay('?s)?\b` — "Kayak", "Kayla" don't trigger). Exempts frontmatter and wiki-links (`[[entities/kay-schneider]]` is metadata, not prose). Blocks the write and returns a rewrite prompt. Known gap: pptx/xlsx deliverables are not scanned (would require unzipping the XML); those remain governed by the niche-intelligence sub-agent prompts.
