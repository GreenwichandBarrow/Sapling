---
schema_version: "1.1.0"
date: 2026-05-28
type: trace
title: "Investor-update biweekly + monthly brief format pivot to numbered situational sections + Insight lines"
people: ["[[entities/kay-schneider]]", "[[entities/guillermo-lavergne]]"]
companies: ["[[entities/ashford-ventures]]", "[[entities/greenwich-and-barrow]]"]
tags:
  - date/2026-05-28
  - trace
  - person/kay-schneider
  - person/guillermo-lavergne
  - company/ashford-ventures
  - topic/investor-update-format
  - topic/skill-evolution-teaching
  - skill/investor-update
---

## Trigger

I generated a Guillermo biweekly call prep brief for 2026-05-28 2pm using the loaded `investor-update` skill template. The subagent produced a thematic-wall format: heavy YAML frontmatter, dense narrative paragraphs grouped by canonical headers ("Headline since last live call / Buy-box calibration / Thesis throughline / DealsX + JJ wind-down posture / Conferences / Interesting conversations / Active Niches / Active Deals / Focus ask / Upcoming / Pending / Questions for Guillermo"). Kay rejected the format and showed me the canonical April 9, 2026 Guillermo doc as the golden.

## Decision

APPROVE — pivot the biweekly + monthly investor-update format to the April 9 doc's structure. Promote April 9 to `examples/biweekly/2026-04-09-guillermo-lavergne.md` as the canonical golden. Rewrite `templates/biweekly-call-prep.md` to encode the structural invariants. Append to `learnings.md` so the next biweekly auto-loads the golden as format spec.

## Alternatives Considered

1. **Single-shot rewrite of the 5/28 brief** without updating the template or saving a golden. Tempting because Kay was about to be on the Guillermo call in <4 hours — fastest path. Rejected: the next biweekly run would regenerate the same thematic-wall failure. Skill evolution requires durable artifacts.
2. **Edit only the template, no golden example.** Templates without anchored examples drift; subagents fall through to generic structure when ambiguity exists. Rejected — Kay explicitly showed me the April 9 doc as the format anchor.
3. **Add a "Questions for {investor}" section to the new format** for completeness. Rejected — the April 9 golden has no Questions section; questions live in Kay's head, not the deliverable. Adding them re-introduces the wall pattern.
4. **Keep thematic-wall format for monthly (Jeff), use April 9 format for biweekly (Guillermo) only.** Rejected — Jeff prep yesterday (5/22) was the same brief I built today's Guillermo subagent prompt from; if April 9 is right for biweekly, it's likely also right for monthly. Logged for the next Jeff prep (6/26 monthly) — if monthly differs, branch then.

## Reasoning

The April 9 doc has six structural moves the rejected version missed: (1) GB letterhead at top (Doc template artifact), (2) opening `Insight:` anchor line that names the meta-takeaway BEFORE section 1, (3) numbered situational sections reflecting what changed SINCE last call rather than fixed thematic headers, (4) each section = bold title + 2-4 line body + underlined `Insight:` line, (5) NO Questions-for-{investor} section, (6) Section 5 niches is bulleted with terse em-dash-separated descriptors.

The signal Kay was teaching with: this is the textbook skill-evolution move. She showed the golden; I promote it. Three layers of skill memory exist (examples/, templates/, learnings.md, plus cross-skill memory/feedback_*.md) — the correct layer for this correction is examples + template + learnings, not memory, because the rule is skill-local (investor-update only).

Forbidden in future runs: thematic walls like "Headline / Buy-box / Thesis throughline" — that's the failure mode that just got rejected. Sections must be situational (what's new since the last call), not canonical thematic.

## Why This Trace Matters

The next biweekly run (Guillermo 6/12) and the next monthly (Jeff 6/26) will both fire investor-update with mode-specific templates. Without this trace + the example/template/learnings updates landed today, the run will default to thematic walls again. Future agents writing investor-facing prep for non-{Jeff, Guillermo} cadences (quarterly review, new investor, ad-hoc call) should also reach for the numbered-situational-sections + Insight-lines structure, not invent their own.

This trace also matters as a skill-evolution worked example: Kay's "this is what it should look like" + screenshot is the highest-leverage teaching signal she gives, and the right response is multi-layer promotion (examples + templates + learnings), not single-shot rewrite.

## Key Insight

For Kay specifically, "investor brief" is a clean external-doc artifact — no internal tag soup, no frontmatter in the rendered Doc body, no Questions section that doubles as a script. Frontmatter lives only in the vault snapshot, never in Drive. Questions live in her head, not the deliverable. The Doc is context + Insight lines; she handles the conversation.
