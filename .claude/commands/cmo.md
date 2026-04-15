---
name: cmo
description: Invoke the CMO agent for brand-voice review on external-facing drafts (outreach, investor updates, conference pitches, LinkedIn). Returns APPROVE / REWRITE / KILL with inline redlines. Pass the draft or question inline.
argument-hint: [draft or question]
disable-model-invocation: true
---

Invoke the CMO subagent (`.claude/agents/cmo.md`) with the following prompt:

$ARGUMENTS

Return the CMO's verdict in its output contract format. If the CMO emits `frame_learning: true`, write a trace file to `brain/traces/{today}-cmo-{slug}.md` tagged `role/cmo` before presenting the verdict.
