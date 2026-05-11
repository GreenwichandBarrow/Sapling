---
name: Context thin signal phrase — ENFORCEMENT RULE
description: Say "Context is getting thin" when conversation approaches compression or session shows strain so Kay can save state before a freeze
type: feedback
originSessionId: e87a4d74-05bd-4c97-a681-d055e0076b72
---
**Say "Context is getting thin" proactively when ANY of these are true:**

- Session has crossed ~30 tool calls or ~15 file writes
- Session has been running for 2+ hours of heavy work
- Response latency is noticeably degrading
- Multiple threads have accumulated (e.g., email triage + deal work + memory writes + drafts all stacked)
- An MCP tool has started hanging or re-authenticating
- Any sign of compaction imminent

**Why:** Kay originally asked for this signal 13 days ago (file originally dated Apr 4, 2026). On 4/17 a long session froze completely — Linkt thread + Mark Gardella drafts + JJ tab generation + Anacapa PDF + investor questions + inbox triage all stacked up. No warning was given. Kay lost the ability to type in the session and had to paste the entire transcript into a new window to recover hours of work. **The rule existed and was not enforced — this is worse than the rule not existing.**

**How to apply:**
- Check for thinning signals every ~10 tool calls during heavy sessions. Don't wait for a feeling.
- Say it EXPLICITLY with those words: *"Context is getting thin — want to save state and open a fresh session?"*
- Erring toward false positives costs nothing. Missing the warning costs Kay's work.
- Do NOT suggest stopping. Kay decides when to stop (`feedback_never_suggest_stopping`). This signal is information, not a recommendation to wind down.
- On trigger: write a continuation file to `brain/context/continuation-{date}-{N}.md` proactively so Kay has a clean handoff if the session dies.

**Enforcement note:** This rule failed once. If it fails again, escalate to Kay — propose a hook or automated check, because passive memory isn't sufficient.
