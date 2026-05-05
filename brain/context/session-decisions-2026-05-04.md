---
date: 2026-05-04
type: context
title: "Session Decisions — 2026-05-04"
tags: ["date/2026-05-04", "context", "topic/session-decisions", "topic/broker-channel-build", "topic/intermediary-templates"]
---

## Decisions

- **APPROVE** Phase 3 pipeline-manager surgery interpretation — 8 lines of Intermediary Pipeline residue removed; Active Deals list logic untouched.
- **APPROVE** USE-GOG-FALLBACK for `gmail-draft.sh` — gog already wraps Gmail API; wrapper script unnecessary.
- **APPROVE** BOTH-FIRE chain for CIM auto-trigger + auto-ack reply (internal Drive/Attio work + broker-facing reply).
- **APPROVE** new doctrine: ALL intermediary email drafts MUST originate from a canonical template (Intermediary Email Templates Doc OR Conference Engagement Templates Sheet). No ad-hoc body copy.
- **REJECT** visual signature embedding (logo card / buy-box graphic / both). One-pager attachment only (Megan Lawlor pattern).
- **APPROVE** new templates added to canonical Intermediary Email Templates Google Doc: CIM RECEIVED, THANK YOU, DAY 5 FOLLOW-UP, DECLINE POST-REVIEW, NDA SIGNED.
- **REJECT** Day 12 soft-close — cadence reduced from 3-touch to 2-touch (Day 0 + Day 5 only) for Brokers + IBs.
- **REJECT** "Need more info" path after CIM screen — too rare for broker engagement; replaced with "Move to owner call" pattern.
- **APPROVE** conference-engagement skill audit — already template-driven by design; added explicit doctrine reference.
- **APPROVE** capacity letter requests for Guillermo Lavergne + Jeff Stevens — surface in next meeting prep brief, no email beforehand.
- **APPROVE** Day 5 follow-up rewrite — collapsed 3 soft signals into single confident sentence ("Bumping my note to the top of your inbox. Would love to find 20 min whenever it works.").

## Actions Taken

- **UPDATED** `pipeline-manager/SKILL.md` — 8 Intermediary Pipeline residue lines surgically removed (532, 679-681, 703, 779-781, 807, 837, 859-863, 1212).
- **UPDATED** `pipeline-manager/SKILL.md` Step 5 added — CIM auto-ack chain pulls template from canonical doc via `gog docs export`. Hard gate: skip + warning if template not found, no ad-hoc fallback.
- **UPDATED** `pipeline-manager/SKILL.md` line 871-873 — "Need more info" replaced with "Move to owner call" (triggers deal-eval Phase 4 with `pending_owner_call: true`).
- **UPDATED** `pipeline-manager/SKILL.md` line 879 — "Pass" path now templated (DECLINE POST-REVIEW lookup from canonical doc).
- **UPDATED** `pipeline-manager/SKILL.md` line 1211 — `gmail-draft.sh` reference replaced with `gog gmail draft`. Thank-you path classified by recipient: intermediary→template-driven, non-intermediary→ad-hoc allowed.
- **UPDATED** `outreach-manager/SKILL.md` line 631 — master template doc ID updated from superseded `1_cNsAPC...` to live `1gTQoCb...`.
- **UPDATED** `outreach-manager/SKILL.md` line 651 — cadence rewritten: Brokers + IBs = 2-touch (Day 0 + Day 5), Lawyers + CPAs = ONE-AND-DONE.
- **UPDATED** `conference-engagement/SKILL.md` — added explicit doctrine reference enforcing template-only drafts.
- **UPDATED** `CLAUDE.md` pre-flight checklist — added intermediary template doctrine line with both canonical source IDs (Doc + Sheet).
- **CREATED** `memory/feedback_no_intermediary_drafts_outside_template.md` — doctrine memory, indexed in MEMORY.md.
- **CREATED** `memory/project_broker_email_one_pager_only.md` — visual signature decision, indexed in MEMORY.md.
- **CREATED** canonical Google Doc additions (3 PROPOSED batches via `gog docs write --append`): CIM RECEIVED + THANK YOU + visual sig note + doctrine note (round 1), THANK YOU template (round 2), Day 5 + DECLINE POST-REVIEW + NDA SIGNED (round 3).
- **UPDATED** canonical Google Doc — Day 5 body rewrite ("Bumping my note to the top of your inbox. Would love to find 20 min whenever it works.") via 3-step find-replace; THANK YOU header typo `{Brokers` → `(Brokers` fixed; CIM RECEIVED orphan close paragraph deleted via index-range `gog docs delete`.
- **UPDATED** `entities/guillermo-lavergne.md` — Pending Discussion Topics section added with capacity letter ask.
- **UPDATED** `entities/jeff-stevens.md` — Pending Discussion Topics section added with capacity letter ask.

## Deferred

- **DEFER** broker-channel one-pager creation to **2026-05-05** — Kay wants to pair with website iteration so they're aligned. Pre-existing draft already in Drive.
- **DEFER** 10 broker first-touch emails to **2026-05-05** — today's first 5 missed; expanding to 10 tomorrow. Apollo enrichment running tonight in parallel session.
- **DEFER** code-level PreToolUse stop hook for intermediary draft enforcement — sufficient layers exist (CLAUDE.md pre-flight + skill code template-gates + canonical-source mandatory lookups). Building a real PreToolUse hook would have high false-positive rate (recipient classification + template-source verification both stateful). Revisit if a doctrine violation actually slips through in practice.
- **DEFER** vault snapshot refresh of `brain/outputs/2026-05-04-broker-outreach-templates.md` — happens on /goodnight (Drive doc has 9 templates vs snapshot's 4).

## Open Loops

- Broker-channel one-pager file does not exist yet. Day 0 + Day 5 templates reference attachment that needs creation. Blocking for outreach if pipeline starts firing tomorrow morning before one-pager is built.
- Broker list verification + Apollo enrichment status: verification DONE per Kay; Apollo enrichment running in another session tonight. Outcome lands tomorrow morning.
- 10 broker emails for tomorrow not yet drafted — will fire from outreach-manager Subagent 3 once enriched targets land.
- Capacity letter ask sits in Pending Discussion Topics for Guillermo + Jeff. Will surface in next meeting brief for each. No external action until then.
