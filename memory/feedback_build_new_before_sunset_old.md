---
name: Build new functionality up and running BEFORE sunsetting the old
description: Never sunset old functionality (format, skill, workflow) before the replacement is built and working. Ship sequence is: build new → verify running → then retire old. Kay 2026-04-24 precedent.
type: feedback
originSessionId: 3d944631-1e1f-43d0-88c1-6fdd795901fd
---
When replacing a system component (briefing format, skill, workflow, tool, artifact), always build the new version to operational state FIRST, then sunset the old. Never sunset first and create a gap where the old is broken and the new doesn't exist yet.

**Why:** On 2026-04-24 Claude edited CLAUDE.md + goodmorning.md + pipeline-manager/SKILL.md to switch the morning briefing from 4-bucket to Decisions-only BEFORE the Command Center dashboard existed to hold the displaced context (Today/ASAP, This Week, Dropped Balls, System Status). That created an impending gap: Monday morning's briefing would deliver decisions only, with no dashboard to see the context layer. Kay caught it: "because you are already updating the good morning skill it means we have to get the dashboard up and functioning right away. In the future I would recommend you get the new items up and functioning first and then sunset the old."

**How to apply:**
- Before editing a skill/format/workflow to remove functionality, verify the replacement is LIVE and WORKING (not just planned).
- If the replacement is non-trivial to build (multi-session, infra-heavy), hold the old format as operational and make the edits to the new format in a parallel location (e.g., a separate SKILL-v2.md), then swap atomically once the new is ready.
- Sequence: (1) design new, (2) build new, (3) verify new in production, (4) migrate usage to new, (5) retire old. NOT: (1) design new, (2) retire old, (3) build new.
- Applies to: briefing formats, skill outputs, sheet schemas, vault file formats, hook rules, dashboards, API contracts.
- Pairs with `feedback_close_out_executes_mutation` — "close out a decision by mutating source of truth same session" does NOT override "build new before sunset old" — the mutation should extend the system, not pre-empt the replacement.
