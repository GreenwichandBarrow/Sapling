---
description: Strategic conversation — Socratic questioning before plan mode. No solutions until the problem is framed.
---

# /socrates

Strategic thinking skill. Runs Socratic conversation BEFORE plan mode — frames the problem, surfaces assumptions, names alternatives, stress-tests direction. Hands off to `/plan` at convergence.

## Usage

```
/socrates                    # Open with "what's on your mind?"
/socrates {topic}            # Open with a specific topic
```

Aliases (verbal in conversation, not separate slash commands): `/think`, `/discuss` — Chief of Staff routes to this skill.

## What it does

1. Restates your problem in its own words to confirm understanding
2. Maps goal hierarchy (surface ask vs underlying goal)
3. Surfaces assumptions you're treating as fixed
4. Names 2-4 alternative paths with tradeoffs (always includes "do nothing")
5. Asks ONE sharp clarifying question at a time
6. Plays counter-argument, cites relevant memories that contradict
7. Detects convergence and proposes handoff to `/plan`
8. Optionally writes a brief at convergence (you say "save it")

## What it does NOT do

- Generate task lists, write code, or commit changes
- Recommend solutions before the problem is framed
- Ask multiple questions per turn
- Continue past convergence

## Three-phase pipeline

```
/socrates  →  /plan  →  execute
strategy      structure   action
```

Per Harrison Wells coaching 4/30: plan mode is the final step, not the thinking step. `/socrates` is the missing first phase.

## Workflow

Invoke the `socrates` skill in `.claude/skills/socrates/`. The skill handles the full conversation loop, convergence detection, and optional brief output.

When convergence is reached, the skill suggests `/plan` and offers to save the discussion brief to `brain/outputs/{date}-discussion-{slug}.md` for plan-mode input.
