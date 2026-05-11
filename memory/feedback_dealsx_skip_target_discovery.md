---
name: DealsX channel niches skip target-discovery
description: If a niche's Outreach Channel = DealsX Email, target-discovery is NOT needed — Sam's team manages the contact list externally. Never surface DealsX niches as "needs refill."
type: feedback
originSessionId: f8be9c15-9637-4853-b0f6-7cf93e164c94
---
For any niche on the Industry Research Tracker where Col D (Outreach Channel) = `DealsX Email`, target-discovery runs at most a thin slice (warm-intro check + Attio dedup against Sam's submitted list) — never an initial fill or a refill. The local target sheet for a DealsX niche is *expected* to be empty most of the time because the contact universe lives at Sam's team, not in our sheet.

**Why:** DealsX (Sam Singh's team) handles list building, enrichment, and mass email/LinkedIn outreach for these niches. Our role is exclusion-list governance, not target generation. Surfacing an empty DealsX target sheet as "needs refill" wastes Kay's attention and would trigger an inappropriate target-discovery run.

**How to apply:**
- In the morning Active-Outreach niche check, **filter by channel first**. Only Kay Email and JJ-Call-Only channels qualify for the "needs refill / needs initial fill" branch.
- DealsX niches: skip the fill-rate check entirely. Never raise as a 🟡 decision item.
- target-discovery `.claude/skills/target-discovery/SKILL.md` (lines 463-504) already encodes this at the execution layer — the rule above closes the loop at the trigger layer (goodmorning workflow).
- If a DealsX niche legitimately needs work — e.g., warm intro check on a fresh batch from Sam — that comes from outreach-manager DealsX Coordination subagent, not from a target-sheet refill signal.

**Current DealsX niches** (per target-discovery SKILL.md): Fractional CFO, Specialty Insurance Brokerage, Estate Management, Specialty Coffee Equipment Service. Cross-check against the live tracker rather than hardcoding — channel assignments evolve.

**Precedent:** Surfaced 2026-04-28 morning briefing — flagged Estate Management + Specialty Coffee Equipment Service as 🟡 "needs refill" for Kay's decision; Kay corrected: "DealsX already has it. Can you update skill so that if it says DealsX that means no target discovery needed. It's only needed for Kay emails and JJ calls."
