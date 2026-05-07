---
schema_version: 1.1.0
date: 2026-04-27
type: trace
today: "[[notes/daily/2026-04-27]]"
task: Saved personal task tracker as project memory rather than formalizing as a skill
had_human_override: false
importance: medium
target: future skill-creation decisions, memory/project_personal_task_tracker.md, .claude/skills/ proliferation guard
tags: [date/2026-04-27, trace, topic/skill-architecture, topic/skill-vs-memory, pattern/dont-formalize-personal-artifacts, domain/system-design]
---

# Decision Trace: Personal task tracker → memory, not skill

## Context

After building [[outputs/to-do-4-26-26-xlsx|TO DO 4.26.26.xlsx]], Kay asked: *"should this be created as a skill that I call on one in a while or just a one off task?"*

The natural impulse was to wrap the build/populate scripts into a skill — `/personal-task-tracker` or similar — so future invocations could rebuild, add Gantt projects, etc. Skills are how this OS formalizes work.

I recommended *no skill*, just a project memory + the existing scripts.

## Decision

Wrote `memory/project_personal_task_tracker.md` capturing: file path, script paths, 5-tab architecture, key design decisions (manual-tick Gantt, day pairs, etc.), Sunday rollover ceremony, and pending items. Did NOT create a skill in `.claude/skills/`.

## Alternatives Considered

1. **Create `personal-task-tracker` skill** — wrap build/populate scripts in SKILL.md, give Kay slash-command access. Rejected: she'll never invoke it. Once built, she works in Excel directly. The skill would sit unused.

2. **Create `add-gantt-project` skill** — narrower; only invoked when promoting an item from To Do Long Term to a real Gantt project. Rejected: that's a maybe-monthly action, can be handled via direct conversation + script edit. Not enough recurrence to justify formalization.

3. **No memory either, just leave the scripts** — relies on future Claude finding the scripts via grep. Rejected: the *why* behind the architecture (manual-tick over auto, day pairs, promotion model) isn't in the scripts, it's in the conversation we just had. Without the memory, future Claude rebuilds the wrong thing.

4. **Memory only (chosen)** — captures the durable knowledge (architecture, decisions, ceremony, pending items). Future Claude finds it when Kay says "let me add a Gantt project" and can pick up correctly without re-asking everything.

## Reasoning

- Skills are **logic-driven recurring workflows** (deal-evaluation runs every time financials arrive; niche-intelligence runs every Tuesday night). They have triggers, inputs, outputs.
- Personal tools are **artifacts**. Once built, the user uses them directly. The "skill" is just the build script — and the build script is one-shot or near-one-shot.
- Litmus question: *"Will Kay invoke this slash command more than 5 times over the next year?"* For deal-evaluation: yes, dozens. For personal-task-tracker: no, maybe once if she rebuilds the whole template, otherwise zero.
- Memory captures the same recoverable state (file path, scripts, decisions) without adding a slash-command surface that nobody calls. Skills proliferate; clutter has cost (skill-loader budget, user mental model, calibration noise).

## Why This Trace Matters

Future agent will be tempted to formalize every meaningful build into a skill. That's the OS's natural instinct — the OS rewards skills with discoverability and reusability. But not everything benefits from formalization. Personal one-off artifacts get **memory + scripts**, not skills. Operational recurring workflows get **skills + memory + scripts**. Mismatching either way costs.

## Key Insight

The skill/memory split tracks **recurrence**, not importance. A high-importance one-off (this task tracker is a daily-use file) goes into memory + scripts. A low-importance recurring pattern (e.g., a daily snapshot refresh) gets a skill. Don't conflate "this matters" with "this should be a skill" — those are orthogonal.
