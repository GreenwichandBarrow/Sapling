---
name: no-suppressed-section-in-briefing
description: "Don't include a \"Suppressed\" section in briefings — if Kay has to read the item, it's not suppressed. True suppression is silent."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 03560fda-4372-4242-bb27-ca05145be53d
---

Briefings must not include a "Suppressed" / "Skipped" / "Not surfaced" footer that lists items by name. The point of suppression is silence. The moment the item appears under any heading, Kay's eyes have to process it, defeating the purpose.

**Why:** Decision-fatigue minimization (`feedback_decision_fatigue_minimization`). Every surfaced word costs attention. A "Suppressed" section is the worst of both worlds — Kay still reads it AND it implies the system is unsure whether to surface, which adds cognitive load. Source: 2026-05-15 morning briefing where I closed with "Suppressed: Sarah de Blasio nurture (Goodwin doc-blocked); Coalition breakfast (declined Tuesday); Lauren Della Monica (hard skip)." Kay's reply: "dont include things that are 'suppressed' If I have to read it, then its not being suppressed."

**How to apply:**
- Items that meet a suppression rule (PASS-suppressed, off-system-closed, trigger-based, hard-skip, blocked-pending-doc, action-already-taken) are silent — NEVER named in the briefing output, even in a footer/aside.
- Awareness-only items that genuinely warrant Kay seeing them get their own Decision slot with an explicit RECOMMEND, not a footer mention.
- Internal artifacts (relationship-status.md, email-scan-results.md) can still document the suppression for traceability — but the briefing output strips it.
- If you feel compelled to "explain why X isn't here," that's a signal X probably should be in the Decisions list as a real item, OR it should be silent. Pick one.

Related: [[feedback-decision-fatigue-minimization]], [[feedback-tracker-done-not-todo-celebration]] (same principle — celebrate done, don't enumerate what's not relevant).
