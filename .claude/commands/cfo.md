---
name: cfo
description: Invoke the CFO agent for financial discipline — runway, deal economics, IRR/MOIC, budget reconciliation, tech-stack ROI, "does this pencil?". Pass context inline.
argument-hint: [question or context]
disable-model-invocation: true
---

Invoke the CFO subagent (`.claude/agents/cfo.md`) with the following prompt:

$ARGUMENTS

Return the CFO's verdict in its output contract format. If the CFO emits `frame_learning: true`, write a trace file to `brain/traces/{today}-cfo-{slug}.md` tagged `role/cfo` before presenting the verdict.
