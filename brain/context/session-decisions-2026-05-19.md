---
date: 2026-05-19
type: context
title: "Session Decisions — 2026-05-19 (late-night session, work spans 5/18 PM → 5/19)"
tags: ["date/2026-05-19", "context", "topic/session-decisions", "topic/credentials", "topic/intermediary-outreach", "topic/outreach-voice", "topic/tooling", "person/becky-wuest-creavin", "person/sam-transworld", "person/matt-becky-colleague", "company/transworld", "status/done"]
---

# Session Decisions — 2026-05-19

Continues [[brain/context/session-decisions-2026-05-18]] (morning file, written 08:41). This session ran late 5/18 into 5/19: Becky→Sam warm intro, Matt XPX follow-up, and two durable infra fixes triggered by recurring "not referencing the canonical source first" failures.

## Decisions

### Sam @ Transworld warm intro (via Becky Creavin)
- **APPROVE (de facto — Kay sent it herself):** Warm-intro reply to [[entities/sam-transworld|Sam]] (broker, [[entities/transworld|Transworld]]), introduced by [[entities/becky-wuest-creavin|Becky]]. Body = canonical INTRODUCTION verbatim with first sentence swapped to a referral opener (the doc's sanctioned DIRECTORY-SOURCED VARIANT mechanism), not ad-hoc.
- **PASS:** Did not echo Becky's "women-owned" framing (silent bias, never announced).

### Matt XPX follow-up
- **DRAFTED → FINAL (Kay handles send):** Follow-up to [[entities/matt-becky-colleague|Matt]]. Iterated v1→final across 5 Kay corrections: no XPX/conversation callback at all, no "keep it open" exit door, goal = get a June meeting on the calendar, June framed as offer (not presumed), restored Kay's preferred first paragraph. Kay to schedule (~8am, Mon–Wed opener). Not sent.

### Durable fix 1 — 1Password-first credential resolution
- **APPROVE:** Investigate + fix the recurring gog auth failure. Root cause: sourcing `.env.launchd` raw loads `op://` ref strings, not values → `aes.KeyUnwrap` (looked like keyring corruption; was not). Kay: "why aren't you going through 1password again" / "this keeps happening."

### Durable fix 2 — pull canonical template doc live, not stale snapshot
- **APPROVE:** Kay: "we already created templates… update to make sure you are referencing them." Fixed the habit of drafting from the stale `brain/outputs/2026-05-04-broker-outreach-templates.md` snapshot.

## Actions Taken
- CREATED `scripts/op-env.sh` (one-line op-resolved cred bootstrap), `scripts/fetch-template-doc.sh` (live canonical doc fetch). Both tested working.
- CREATED + REGISTERED `.claude/hooks/router/handlers/op_first_guard.py` (PreToolUse[Bash]) — blocks raw `source/eval .env.launchd`; unit-tested.
- UPDATED `CLAUDE.md` (two pre-flight bullets: 1Password-first + pull-template-live), `.claude/skills/outreach-manager/SKILL.md` (pull-live + never-snapshot), `brain/outputs/2026-05-04-broker-outreach-templates.md` (loud DO-NOT-DRAFT banner).
- CREATED entities `transworld`, `sam-transworld`; UPDATED `becky-wuest-creavin` relationship notes (5/18 intro logged).
- CREATED memory `feedback_op_env_before_op_backed_cli`, `feedback_pull_canonical_doc_live_not_snapshot`; UPDATED `feedback_continue_dont_reintroduce` (Matt 5/18 sharpening); MEMORY.md index updated (both clusters).
- CREATED traces: `2026-05-19-1password-first-credential-resolution`, `2026-05-19-stale-vault-snapshot-not-canonical-template`, `2026-05-19-warm-followup-no-event-reminder`.

## Deferred
- **REFERRAL-SOURCED VARIANT codification into the live Drive template doc** — proposed; Kay sent the email built on it (validates the pattern) but did not explicitly approve adding it to the canonical Doc. Trigger: next intermediary-outreach session or Kay confirmation.
- **Matt entity correction** — `matt-becky-colleague.md` still says "outreach blocked / no verified email"; stale now that Kay has an active thread. Offered to fix; trigger: Kay confirmation (no verified email value on hand — will not fabricate).
- **Sam full name + Transworld branch** — both entities name-pending; trigger: Kay provides.

## Open Loops
1. **Matt follow-up** — drafted/final, awaiting Kay to schedule (~8am). (Resolves 5/18 Open Loop #2's "fold-vs-separate" — Becky luncheon folded in, sent as direct follow-up.)
2. **Task 12** (retire weekly-tracker / weekly-archive-export) — still open from 5/18; one-keystroke Kay decision.
3. **Laura Smith** — 2 warm intros still BLOCKED (no verified email; will not construct). Carry from 5/16 / 5/18.
4. **MEMORY.md size** — now ~60KB (grew with this session's 2 new entries); Friday meta-calibration consolidation candidate. Carry from 5/18 #6.
5. **Optional `is_owner` call-schema change** — offered, not built; needs Kay go-ahead. Carry from 5/18 #5.
6. REFERRAL-SOURCED VARIANT Drive codification (see Deferred).

## Calibration Candidates
- **skill-router precision** — every user turn this session fired a SKILL ACTIVATION suggestion that evaluated to NO (socrates/tracker/etc., ~100% false-positive rate, ~8 turns). Existing-system tuning → `evolve` candidate for the skill-router matcher, not a new skill. Surface, do not fix here.
- Meta-pattern "not referencing canonical source first" recurred 2x (creds, templates) — both now hook/doctrine-enforced this session; not an open candidate.
