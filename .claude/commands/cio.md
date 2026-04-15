---
name: cio
description: Invoke the CIO agent for buy-box enforcement, niche scoring, target go/no-go, thesis coherence, searcher-overlap filtering, and warm-intro prioritization. Pass context inline.
argument-hint: [niche, target, or question]
disable-model-invocation: true
---

Invoke the CIO subagent (`.claude/agents/cio.md`) with the following prompt:

$ARGUMENTS

Return the CIO's verdict in its output contract format. If the CIO emits `frame_learning: true`, write a trace file to `brain/traces/{today}-cio-{slug}.md` tagged `role/cio` before presenting the verdict.
