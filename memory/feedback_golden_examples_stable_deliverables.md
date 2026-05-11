---
name: Stable deliverables get an examples/ folder with Kay-approved golden outputs
description: Skills producing one-pagers, scorecards, meeting briefs, call logs, LOI templates load 2-3 approved goldens at runtime for consistency
type: feedback
originSessionId: 79f2536c-7455-4155-bafd-6653508b83e4
---
**Rule: skills producing stable-format deliverables maintain an `examples/` subfolder with 2-3 Kay-approved golden outputs. The skill loads these at runtime to enforce format consistency.**

**Why:** Per Harry Liu's "Going Deeper with Claude" webinar (Apr 17 2026): "you can also provide examples of board packs or decks that are best in class or golden examples for claude to reference every single time." Instruction-only skills drift run-to-run because SKILL.md leaves too much interpretation latitude. A concrete example pins the structure. Our format-stable deliverables have had Kay flag formatting inconsistency multiple times — examples fix it.

**Qualifying deliverables (format stable for 60+ days):**
- Niche one-pager (`niche-intelligence`)
- Niche scorecard (`niche-intelligence`)
- Meeting brief (`meeting-brief`)
- Call log (`jj-operations`)
- LOI template (`deal-evaluation`)
- Thumbs Up/Thumbs Down deck (`deal-evaluation`)

**Explicitly NOT qualifying (still evolving):**
- Morning briefing (format changed 3x in April)
- Investor update (quarterly evolution)
- Email drafts (per-target, voice varies)
- Slack messages (channel-specific voice)

**How to apply:**

1. **Create `.claude/skills/{skill}/examples/` if missing.** Populate with 2-3 outputs Kay has explicitly approved (via session-decisions "APPROVE" tag or direct confirmation).

2. **Skill must load examples at runtime.** SKILL.md adds a line: *"Load 2-3 files from `examples/` folder before generating output. Match structure, section headers, voice, length, and formatting exactly."*

3. **Examples self-maintain via the output portfolio.** When Kay approves an output (via frontmatter `kay_approved: true` on brain/outputs files — see `feedback_skill_output_portfolio`), the file becomes a candidate example. Rotation rule: keep the 3 most recent Kay-approved outputs per skill; older examples archive to `examples/archive/`.

4. **Don't add examples to evolving skills.** Adding golden examples to a skill whose format isn't settled will calcify the wrong thing. Wait for 60 days of stability.

5. **Update cadence.** Each Friday, calibration-workflow checks: are the newest examples still representative of Kay's current preferences? If she's rejected the pattern in recent feedback, rotate examples out.

**Source:** 2026-04-19 Anacapa deck analysis, Lesson 3.
