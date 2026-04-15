---
name: gc
description: Invoke the GC agent for NDA/LOI review, compliance hard-stops (PE/lending/California/carve-outs), secrets hygiene, sender-reputation risk. Returns APPROVE / REDLINE / HARD STOP.
argument-hint: [NDA, LOI, or question]
disable-model-invocation: true
---

Invoke the GC subagent (`.claude/agents/gc.md`) with the following prompt:

$ARGUMENTS

Return the GC's verdict in its output contract format. If the GC emits `frame_learning: true`, write a trace file to `brain/traces/{today}-gc-{slug}.md` tagged `role/gc` before presenting the verdict.
