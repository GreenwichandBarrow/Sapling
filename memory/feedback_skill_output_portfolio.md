---
name: Every brain/outputs file is tagged with skill_origin and kay_approved
description: Creates a queryable corpus — per skill, which outputs Kay approved vs rejected. Powers golden-examples self-maintenance.
type: feedback
originSessionId: 79f2536c-7455-4155-bafd-6653508b83e4
---
**Rule: every file written to `brain/outputs/` includes `skill_origin:` and `kay_approved:` in frontmatter.**

- `skill_origin:` — slug of the skill that produced the output (e.g., `niche-intelligence`, `meeting-brief`, `deal-evaluation`). Always populated at creation.
- `kay_approved:` — `true` / `false` / `null`. Populated when Kay reacts. `null` = pending review. `true` = explicit approve. `false` = rejected.
- `kay_approval_date:` — date Kay approved/rejected. Used for golden-example rotation.

**Why:** Per Harry Liu's "Going Deeper with Claude" webinar (Apr 17 2026), skill outputs should build into a shared portfolio — a reference corpus of what "good" looks like. We've never tagged outputs by skill-of-origin, which means we can't query "show me everything niche-intelligence has produced" to judge quality or nominate golden examples. With these fields, the loop self-maintains: Kay-approved outputs auto-nominate for `examples/` folders; rejections feed anti-pattern lists.

**How to apply:**

1. **Skill output hygiene.** Every skill that writes to `brain/outputs/` MUST set `skill_origin` at creation time. Schema v1.2.0 enforces this (optional for now, required-by-default once migration lands).

2. **Reaction capture.** When Kay says "this is great" or "I don't love this format" about a specific output, update the file's `kay_approved` + `kay_approval_date` fields before session ends. Evening workflow's session-decisions capture explicitly scans for output approvals/rejections.

3. **Golden-example loop.** Calibration-workflow weekly pass:
   - Query outputs by skill_origin over last 90 days
   - Filter kay_approved == true
   - Take 3 most recent per skill
   - Copy to `.claude/skills/{skill}/examples/` if not already present
   - Archive older approvals to `examples/archive/`

4. **Queries this enables:**
   - "How often does Kay approve niche-intelligence one-pagers?" — approval rate per skill
   - "What outputs should never be shown again?" — kay_approved == false
   - "Show me Kay's 3 favorite meeting briefs" — for cloning format in new briefs

5. **Migration.** Existing `brain/outputs/` files don't have these fields. `/migrate` skill handles backfill — for old files, leave skill_origin null and kay_approved null unless clear from context.

**Source:** 2026-04-19 Anacapa deck analysis, Lesson 9. Paired with `feedback_golden_examples_stable_deliverables`.

**Schema reference:** `schemas/vault/output.yaml` v1.2.0.
