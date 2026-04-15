---
name: cpo
description: Invoke the CPO agent for JJ/Sam communication review, nurture triage, follow-up timing, warm-intro etiquette, dropped-ball detection. Returns NUDGE / WAIT / ESCALATE verdicts.
argument-hint: [context or question]
disable-model-invocation: true
---

Invoke the CPO subagent (`.claude/agents/cpo.md`) with the following prompt:

$ARGUMENTS

Return the CPO's verdict in its output contract format. If the CPO emits `frame_learning: true`, write a trace file to `brain/traces/{today}-cpo-{slug}.md` tagged `role/cpo` before presenting the verdict.
