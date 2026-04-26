---
schema_version: 1.1.0
date: 2026-04-25
type: trace
today: "[[notes/daily/2026-04-25]]"
task: Where to put non-interactive instructions for a headless-launched skill
had_human_override: false
importance: medium
target: scripts:run-skill.sh, .claude/skills/target-discovery/headless-phase2-prompt.md
tags: [date/2026-04-25, trace, topic/launchd-hardening, topic/headless-agents, pattern/wrapper-prompt-swap, domain/technical]
---

# Decision Trace: Wrapper-side prompt swap vs SKILL.md mode handler

## Context

Layer 2 of [[outputs/2026-04-25-saturday-launchd-hardening-plan]]: target-discovery Phase 2 needs explicit non-interactive instructions when launched by the Sunday 10pm launchd job. Current plist invokes `claude -p` with stdin `/target-discovery`, no further context. The agent then asks "which niche?" or invents a YES/NO/DISCUSS clarifying question and exits 0 (the 4/19 bug).

Three places to put the headless-mode instructions:

## Decisions

### Where the headless logic lives

**Considered:**
- (a) **Inside `target-discovery/SKILL.md`.** Add a "Headless Phase 2 Mode" section. SKILL.md detects the `phase2-sunday` arg and switches behavior. One file owns the skill end-to-end.
- (b) **Inside `scripts/run-skill.sh` as a case statement.** Wrapper recognizes `target-discovery + phase2-sunday` and pipes pre-baked instructions inline.
- (c) **A separate prompt file at `.claude/skills/target-discovery/headless-phase2-prompt.md`. Wrapper detects skill:args pair and pipes the file content as Claude's user prompt instead of bare `/skill-name`.**

**Chosen:** (c).

**Reasoning:**
- (a) fails because SKILL.md is loaded into the agent's context as reference material — the headless instructions would coexist with the conversational instructions and the agent might still pick the conversational path. The agent has to decide "am I in headless mode?" from prompt content, which is exactly the kind of judgment call that lets it invent reasons to exit.
- (b) puts long prompt strings inside bash, awkward to edit and read. Also conflates wrapper concerns (shell exit codes, retries) with prompt design.
- (c) — wrapper-side prompt SWAP — bypasses the conversational mode entirely. The agent never sees `/target-discovery`; it sees the headless prompt as the user's first message. SKILL.md is still the reference (loaded if the agent navigates to it) but the headless prompt is the operative instruction set.

### Headless prompt forbids /skill-name dispatch

**Chosen:** Headless prompt does not invoke `/target-discovery` or any other slash command. It tells the agent the steps directly, references SKILL.md by path for implementation details, and exits when done.

**Reasoning:** Slash command dispatch loads the skill's `<objective>` block which is conversational ("Trigger: Niche status changes... Do not run daily...") — useful for an interactive operator, misleading for a launchd job. Direct prompt avoids the misleading framing.

## Learnings

- **Conversational vs headless are two different products of the same skill.** SKILL.md should be authored for the conversational case (reference material, decision support). Headless prompts are runbooks — imperative, no clarifying questions, one-shot.
- **Wrapper-side swap keeps the two products clean.** The skill author owns SKILL.md; the launchd plist + wrapper own the headless prompt. They evolve independently without one polluting the other.
- **Future agent instruction:** when adding a launchd-fired mode to an existing skill, do NOT modify the skill's main SKILL.md objective. Instead, author a sibling `headless-{mode}-prompt.md` and route the launchd plist through the wrapper's prompt-swap mechanism.

## Why This Trace Matters

A natural instinct is to put all skill behavior in SKILL.md. For headless-launched modes, that instinct produces brittle skills that confuse the agent at runtime. The wrapper-swap pattern is cleaner but non-obvious — without this trace, a future agent extending Layer 4 to other mutating skills might reach for SKILL.md modifications first.

## Key Insight

**SKILL.md is for reasoning, headless-prompt files are for executing.** Don't mix them. The wrapper is the transport layer that picks which one to invoke.
