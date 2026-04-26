---
schema_version: 1.1.0
date: 2026-04-26
type: trace
today: "[[notes/daily/2026-04-26]]"
task: Distinguish scheduled/recurring jobs from to-do items in checkpoint formatting
had_human_override: true
importance: medium
target: morning briefing assembly, checkpoint summaries, memory feedback_scheduled_vs_todo_presentation.md
tags: [date/2026-04-26, trace, topic/decision-fatigue, topic/automation-presentation, pattern/cognitive-load-leakage, domain/operational]
---

# Decision Trace: Scheduled jobs are not to-do items — present them differently

## Context

After loading two new launchd plists (`apollo-credits-refresh` + `external-services-probe`), I confirmed both registered and added to my checkpoint summary:

> "Apollo credits → next hour Mon 4/27 8am ET"
> "External services probe → every 30 min Mon-Fri 8am-8pm ET starting tomorrow"

Kay pushed back: *"You made it look like something we need to work on. I dont think you should present it the same way as the 'to do' items when its a scheduled item for weekly work flow."*

Sharp catch. I was treating "scheduled and self-managing" as if it were "open and tracked." Same checkpoint format, same mental cost.

## Decision

When confirming a scheduled job is set up: present it as **"wired up, runs Mon-Fri"** — one line, no fire-time call-out, no "next fires at..." Cognitive load on Kay = zero (which is the whole point of scheduling it).

To-do format (date, time, what's blocked) is reserved for items Kay needs to act on. Scheduled jobs only re-surface if they FAIL.

Memory shipped: `feedback_scheduled_vs_todo_presentation.md`.

## Alternatives Considered

1. **Keep listing fire times "for transparency"** — the impulse here is "user should know when things will happen." But Kay doesn't *need* to know — that's literally the point of having scheduled it. Transparency at the cost of cognitive load is anti-pattern. **Rejected.**

2. **Only list fire times for first-run-after-creation** ("watch this fire tomorrow to confirm it works") — defensible as a one-time validation prompt. **Partially adopted** — the rule allows surfacing IF a known issue means she should watch the first run. Default suppressed.

3. **One-line "wired up" only (chosen)** — minimum viable confirmation. Kay knows it's set; she doesn't need to track it.

## Reasoning

- Kay's permanent goal is decision-fatigue minimization. Listing scheduled fire times converts an automation (zero-load) into a tracked event (load).
- The format I used ("→ next hour Mon 4/27 8am ET") looks identical to a to-do reminder. Same visual weight, same mental category. Kay correctly read it as "thing to remember."
- This is a presentation rule, not a behavior rule — the underlying scheduling is fine. Just the surface formatting needs to change.

## Why This Trace Matters

Future agent setting up a launchd job, cron entry, or any recurring automation will instinctively want to confirm "you'll see the first run tomorrow at 8am" — feels helpful, transparent, professional. It's not. It's noise. Trace + memory prevent that pattern.

## Key Insight

Automations exist to remove things from the user's mental queue. When you confirm an automation by adding the schedule to their mental queue, you've defeated the purpose. Confirmation = "wired up." Period. No fire times. No "watch for the first run." Save those for failure modes.
