---
name: Silent mode when executing multi-step ops
description: Once Kay approves a multi-step execution, work silently — minimal narration, no explanations, only one-line status updates between steps.
type: feedback
originSessionId: be424d14-c643-43f3-aebd-a481ac5ad995
---
When Kay has approved a multi-step plan and execution is underway, default to silent execution mode: run the commands, report only what landed (one-line status), no preamble or explanation per step. She doesn't need walkthrough commentary mid-flow.

**Why:** Stated explicitly 2026-05-09 mid-1Password-migration: "please function in silent mode." Mid-execution chatter dilutes signal — Kay can read tool output and infer state. She wants progress, not narration.

**How to apply:**
- After plan approval ("agree" / "do it" / "yes"), drop preamble — just execute
- Tool calls are visible to her; trust she can read them
- One-line status between major steps is fine ("iMac side done, moving to server")
- Save explanations for: errors, decision points needing input, final summary
- Resume conversational mode only when work pauses (waiting on user input, plan approval, or natural step boundary)
- Distinguish from initial planning/scoping — those still warrant context. Silent mode is *during execution*, not before.
