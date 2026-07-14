---
schema_version: 1.1.0
date: 2026-07-13
type: trace
task: "Correct meeting brief trigger workflow after Ray Radigan brief miss"
had_human_override: true
importance: high
target: skill:meeting-brief-manager
tags: [date/2026-07-13, trace, topic/meeting-brief, topic/goodmorning, pattern/approval-gated-generation, status/pending]
---

## Context

Kay asked why the [[entities/raymond-radigan|Ray Radigan]] / [[entities/peapack-private|Peapack Private]] brief did not surface for the next-day meeting. The skill body still implied nightly generation, while the actual configured behavior was on-demand and Good Morning proposal-based.

## Decisions

### Good Morning proposes; meeting-brief generates only after Kay approves
**AI proposed:** Treat the morning-before rule as automatic brief generation or a missing nightly automation.
**Chosen:** Treat the morning-before rule as a Good Morning decision prompt. Generate the brief only after Kay says yes or asks directly.
**Reasoning:** Kay wants to decide which meetings merit briefs. Silent automation creates unnecessary artifacts and contradicts the configured `Pre-meeting trigger: Never run / On-demand` behavior.
**Pattern:** #pattern/approval-gated-generation

## Learnings

- meeting-brief-manager: Remove stale language that implies automatic nightly generation unless a future timer is explicitly reintroduced with Kay approval semantics.
- pipeline-manager: Meeting Briefs must be a concise proposal surface in Good Morning, not an auto-runner.
