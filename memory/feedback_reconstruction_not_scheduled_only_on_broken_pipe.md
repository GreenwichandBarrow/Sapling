---
name: feedback_reconstruction_not_scheduled_only_on_broken_pipe
description: A day with only automated git commits is NOT proof it was scheduled-skills-only — a broken-pipe interactive session leaves no commit but does major work.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: be6211d2-bac6-4937-8d6a-684bac0f2e87
---

When reconstructing a missing `session-decisions-{date}.md`, do NOT conclude "scheduled-skills-only day, no human decisions" merely because every git commit that day is an automated `update context` artifact. Interactive sessions that end in a **broken pipe / SSH timeout** (common on the VPS — see [[reference_vps_broken_pipe_use_agent_tmux]]) are never bookended and leave no human-authored commit, yet may contain a full day of build work and judgment calls.

Concrete failure: the 2026-05-13 file was reconstructed on 5/16 as "scheduled-only, no human decisions lost." It missed an entire interactive day — post-call-analyzer architecture rewrite, granola-api wrapper build, office-rent runway analysis, Heels to Deals pipeline write, Harrison supply-chain hardening. Kay recovered it from a pasted transcript on 5/17 and the file had to be corrected.

**Why:** All-automated commits is the *expected* signature of a broken-pipe day, not evidence of an idle one. Treating it as proof of idleness silently destroys decision/trace/memory capture for that day and feeds the calibration pipeline a false "nothing happened."

**How to apply:** When reconstructing, label the file low-confidence and explicitly list what evidence would be missing if a broken-pipe session occurred (build artifacts with that day's mtime, new memory files dated that day, skill-file edits, binaries in `~/.local/bin`). Cross-check artifact mtimes and memory-file dates against the supposed "scheduled-only" claim — if build artifacts carry that day's timestamp, an interactive session happened. Prefer "RECONSTRUCTED — interactive work suspected, transcript not recovered" over "confirmed scheduled-only." If Kay later supplies the transcript, run `/goodnight` on it and CORRECT the file rather than appending a second one.
