---
schema_version: 1.1.0
date: 2026-04-25
type: trace
today: "[[notes/daily/2026-04-25]]"
task: Migrate morning briefing 4-bucket → Decisions-only post-dashboard
had_human_override: false
importance: high
target: skill:pipeline-manager
tags: [date/2026-04-25, trace, topic/morning-workflow, topic/decision-fatigue, pattern/urgency-emoji-instead-of-bucket-headers, domain/process]
---

# Decision Trace: Decisions-only briefing with urgency emojis (not sub-headers, not collapsed)

## Context

Original migration plan in CLAUDE.md (Apr 17): briefing collapses from 4 buckets (Today/ASAP, Decisions, This Week, Dropped Balls + System Status footer) to Decisions-only once Command Center dashboard goes live to hold the displaced context. Per `feedback_build_new_before_sunset_old`, held the migration until dashboard was operational. Apr 25: gating condition met (all 6 pages live + scheduled refresh + production-readiness).

But "Decisions-only" alone loses urgency signal. Kay needs to know which decisions are 🔴 today-urgent vs 🟢 nurture-recovery — the prior bucket structure encoded that. How to preserve urgency without re-introducing buckets?

## Decisions

### Urgency representation

**Considered:**
- (a) Sub-headers within Decisions list ("Urgent / Routine / Recovery"). Re-introduces structure the migration was meant to flatten.
- (b) Implicit ordering — urgent items sorted to top, no markers. Kay has to infer urgency from item position, fragile.
- (c) Inline emoji tags (🔴/🟡/🟢) per item. Single visual scan-line shows urgency mix. No bucket re-introduction.

**Chosen:** (c). Per-item format: `N. {emoji} *{C-suite}* **RECOMMEND: {action}** — {reason} → YES/NO/DISCUSS`.

**Reasoning:** (a) loses the "shrink" goal of the migration. (b) is fragile — Kay shouldn't have to count down to figure out "is this still in today's window?" (c) preserves urgency at the item level where it belongs (each item knows its own urgency) without imposing a structural layer.

**Pattern:** #pattern/urgency-emoji-instead-of-bucket-headers

### What to do with broken-system signals

**Considered:**
- Keep separate System Status footer line (mini version of old format).
- Surface as a 🔴 Decision: **RECOMMEND: Investigate {job} (last log {ts})** → YES/NO.

**Chosen:** Surface as 🔴 Decision. Don't bury silent failures in a footer.

**Reasoning:** A broken scheduled skill is decision-worthy ("investigate or wait") not status-worthy. Putting it in a footer trains Kay to skim past it. Putting it in the Decisions list with Obama framing forces action. The dashboard's stale-snapshot banner already shows passive status; the briefing shouldn't duplicate that — it should surface the *decision* the broken system requires.

### Don't reduce to ≤3 items

**Considered:** Push the cap from ≤5 to ≤3 to maximally minimize decision fatigue.

**Chosen:** Keep ≤5.

**Reasoning:** ≤3 forces over-aggressive collapse, losing items that legitimately need Kay's eyes. ≤5 is the existing decision-fatigue doctrine number from `feedback_decision_fatigue_minimization`. Don't tighten without a calibration signal that Kay finds 5 too many.

## Learnings

- **When migrating away from a structural layer (buckets), the information that layer carried needs an alternative encoding (emoji tags) — not just removal.** Otherwise the migration silently loses signal.
- **Default escalation route for system signals: surface as Decisions, not as status.** Status sections train skim-past behavior; Decisions sections force engagement.
- **Future agent instruction:** when migrating a structured surface (multi-bucket, multi-section, multi-tab) into a flat one, enumerate every signal the structure was carrying and verify each has a per-item encoding before sunsetting. Run a "what would this lose?" check.
