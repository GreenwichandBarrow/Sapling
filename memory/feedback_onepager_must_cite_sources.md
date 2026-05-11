---
name: Niche one-pagers must cite every source with live hyperlinks
description: Niche-intelligence one-pager .pptx must include a Sources section citing every source used (external URLs, vault paths, chatroom traces, CRM pulls), each with a live python-pptx hyperlink. Added as Section 10 on 2026-04-24.
type: feedback
originSessionId: 3d944631-1e1f-43d0-88c1-6fdd795901fd
---
Every .pptx one-pager produced by the niche-intelligence skill must include **Section 10: Sources** — a complete citation list of every source file, web page, newsletter, report, vault note, chatroom trace, Attio/Apollo pull, or sheet lookup that informed the content. Each entry carries a live hyperlink.

**Why:** Kay reviews one-pagers before scoring and tracker updates. When a fact is noteworthy she wants to click through to the source directly — to verify, to pull more context, or to share with advisors. Without source links, the one-pager is a black box: the analyst can't audit how conclusions were drawn, and Kay can't reuse the research trail elsewhere. Rule added 2026-04-24 after Kay's explicit ask during weekly-tracker debugging session.

**How to apply:**
- Add Section 10 "Sources" to every one-pager, either as the final row in the main table or as a second slide titled "Sources" in the same .pptx file. Never truncate.
- Each entry format: `{Short title} — {one-line description} — {live URL or vault/Drive path}`.
- Group entries in this order: (1) Gathering-sub-agent findings (chatroom traces at `brain/traces/agents/{date}-niche-intelligence.md`), (2) External research & industry reports (web URLs, newsletter links, trade publications), (3) Internal vault references (call notes, prior one-pagers, session decisions), (4) CRM / data pulls (Attio queries, Apollo searches, sheet lookups).
- Implement hyperlinks in python-pptx: `run.hyperlink.address = url` with `run.font.color.rgb = RGBColor(0x0B, 0x5C, 0xAB)` for the standard hyperlink blue.
- Validation: a one-pager without Section 10 fails the skill's completion checklist (`.claude/skills/niche-intelligence/SKILL.md` Completion Criteria). Re-run the one-pager agent rather than shipping incomplete.
- Companion files updated 2026-04-24: `references/one-pager-template.md` (Sections list + Implementation block), `references/sub-agents.md` (§3 niche-intel-onepager section list), `SKILL.md` (Completion checklist line).
