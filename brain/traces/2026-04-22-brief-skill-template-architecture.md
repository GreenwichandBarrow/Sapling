---
schema_version: 1.1.0
date: 2026-04-22
type: trace
title: "Brief-Skill Architecture — Hybrid Templates + Examples, Not One Skill Per Variant"
tags: ["date/2026-04-22", "trace", "topic/skill-architecture", "topic/brief-skills", "topic/templates-vs-skills", "topic/investor-update", "topic/meeting-brief"]
had_human_override: false
importance: high
target: process
people: ["[[entities/kay-schneider]]"]
companies: []
---

# Trace: Brief-Skill Template Architecture

## Context

investor-update and meeting-brief each need to produce several distinct deliverables — investor-update has at least four modes (monthly for Jeff, biweekly for Guillermo, quarterly for all 12 LPs, weekly-dd post-LOI); meeting-brief has at least four (new-contact, owner-call, intermediary, conference-prep). Until today, both skills used a single generic template per skill, which had failed to hit the right tone in the room for several specific modes (e.g., quarterly vs biweekly cadence rooms have very different disclosure thresholds; conference-prep rooms require a different structure than 1:1 owner calls).

The question this session: should we split each skill into N sibling skills (investor-update-monthly, investor-update-quarterly, …), or keep one skill per family and split the template layer underneath?

## Decisions

### One skill per family, typed templates + examples folder underneath
**AI proposed:** Split into 7 sibling skills — one per variant — so each mode has its own SKILL.md and its own owner.
**Chosen:** Keep 2 parent skills (`investor-update/`, `meeting-brief/`). Each gets a `templates/` folder with one file per mode (`templates/monthly.md`, `templates/biweekly.md`, …) and an `examples/` folder with one subfolder per mode (`examples/monthly/*.md`, `examples/biweekly/*.md`, …). SKILL.md resolves `{mode}` → loads both the template and the most-recent example before drafting.
**Reasoning:** 7 sibling skills would have duplicated 80%+ of shared hygiene (sender-voice rules, formatting, Drive-file naming, approval routing) across every SKILL.md — changes would need to be made in 7 places, and drift would be inevitable. One parent skill with typed templates concentrates the shared hygiene and localizes the per-mode differences to just the template + examples. It also means a new mode is an additive template file, not a new skill directory.
**Pattern:** #pattern/one-skill-per-family-templates-for-variants

### No fall-through to a generic template
**AI proposed:** Have the skill fall back to a generic template if `{mode}` is not specified.
**Chosen:** Skill errors if `{mode}` is not provided. The invocation must name the mode.
**Reasoning:** The reason this architecture exists at all is that the generic template kept producing wrong-tone output. A silent fallback to generic would recreate the exact failure mode we just engineered around. A noisy error forces the caller (Claude or Kay) to pick a mode, which is the entire point.
**Pattern:** #pattern/no-silent-defaults-on-routed-skills

### Templates also live in G&B MASTER TEMPLATES Drive folder
**AI proposed:** Keep templates only in `.claude/skills/{skill}/templates/` — Kay can read them in the repo if needed.
**Chosen:** Mirror all 8 templates into G&B MASTER TEMPLATES Drive folder (id `19TxdV5GHHbYq_O8YupQ-gkEH7V00iykx`). Drive is source of truth for humans; skill reads from repo.
**Reasoning:** Per `reference_master_templates`, Kay's humans (JJ, future hires) look in Master Templates when they need a template. If templates only live in the skill repo, non-Claude users can't find them. Dual-sync is worth the maintenance cost because the alternative — humans opening files in a different format and Claude in yet another — would guarantee drift.
**Pattern:** #pattern/templates-mirrored-to-drive

### Example folders allowed to ship empty
**AI proposed:** Require every example folder to have at least one example before the mode ships.
**Chosen:** Quarterly, weekly-dd, and conference-prep example folders ship empty today. Populate as next Kay-approved golden of each mode lands.
**Reasoning:** Blocking a structural refactor on having goldens for every mode would have held up monthly / biweekly / new-contact / owner-call / intermediary — all of which have recent goldens — because quarterly fires once a quarter and weekly-dd only fires during active DD. Better to ship the scaffolding and backfill goldens on next fire. The skill's mode-routing logic handles an empty `examples/{mode}/` gracefully (template-only draft).
**Pattern:** #pattern/ship-scaffold-backfill-examples

## Why This Trace Matters

The next time a skill starts producing mode-specific wrong-tone output (likely candidates: outreach-manager for cold vs warm vs intermediary channels, call-prep beyond just external meetings, any future newsletter / blog / LinkedIn skill), the default refactor instinct will be "split into sibling skills." That instinct is wrong for skills where the modes share 80%+ of the hygiene. The right move is the hybrid architecture codified today: one parent skill, typed templates, per-mode example folders, no silent fallback, templates mirrored to Drive if humans use them.

## Key Insight

**Skill boundaries should track shared hygiene, not shared output format.** Two deliverables with identical hygiene but different templates belong in one skill with two templates. Two deliverables with identical templates but different hygiene (e.g., one goes to Kay's inbox for review, one auto-sends to JJ) belong in two skills. The investor-update family has shared hygiene (voice, Drive naming, approval routing) and different templates per audience — one skill, 4 templates is correct. Had it been the inverse — shared template, different hygiene — sibling skills would be correct.

## Connected Decisions (same session)

- Deal-aggregator Phase 2 shipped with Source Scorecard + Weekly Digest + Source Scout subagent — same "finish step one before step two" doctrine (`feedback_finish_step_before_next`) that held Phase 3 until two Friday digest cycles prove Phase 2.
- Industry Research Tracker rank column updated to 4/21 searcher ranking — unrelated to this trace, but part of the same session.
