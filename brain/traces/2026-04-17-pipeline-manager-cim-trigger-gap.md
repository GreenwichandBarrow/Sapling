---
schema_version: 1.1.0
date: 2026-04-17
type: trace
had_human_override: true
importance: high
target: skill:pipeline-manager
review_status: pending
tags: [date/2026-04-17, trace, pattern/automation-gap, status/proposed, severity/high]
---

# Pipeline-manager CIM Auto-Trigger failed silently on Project Restoration (EQA)

## Context

On 2026-03-20 a CIM arrived for Project Restoration (Colorado Art Restoration Services + CFC) from Eric Dreyer at Eight Quarter Advisors. Pipeline-manager's documented CIM Auto-Trigger — a 4-step automated workflow (Drive folder creation, CIM filing, inbox item creation, deal-evaluation invocation) — did NOT execute. The Attio Active Deals entry jumped from Identified straight to Closed / Not Proceeding on 3/26 with no NDA Signed or Financials Received stages recorded. No Slack notification fired to `#active-deals`. No ACTIVE DEALS Drive folder was created.

Kay discovered the gap on 2026-04-17 when reviewing whether to pass or reconsider. She asked: "do we have this recorded in the active deal pipeline as an NDA signed, CIM received and then passed." The answer was no — the skill had produced no audit trail.

Weekly-tracker DID capture the deal (1 NDA Signed + 1 Financials Received for week ending 3/20). That's the only place in the system where the progression was visible, and it was captured via the human-in-the-loop Friday ritual, not automated pipeline hygiene.

## Decisions

### Diagnosing the root cause
**AI proposed:** Frame as a "skill hardening" issue to fix before May 7 DealsX launch.
**Chosen:** Full root-cause analysis.
**Reasoning:** Kay asked explicitly "whats wrong with the skill." Three compounding failures identified:
  1. Email-intelligence launchd plist wasn't installed until ~4/13 — no scheduled scan ran on 3/20 or 3/23
  2. Even when email-intelligence runs, the CIM Auto-Trigger requires agent-driven execution of 4 steps — no enforcement hook
  3. Attio stage transitions are Claude-manual — no background process keeps Attio in sync with email/Drive reality
**Pattern:** #pattern/automation-gap — skill specs describe aspirational behavior, not actual automation. The system works when the agent actively executes it, silently fails when the agent isn't in-session.

### C-suite ownership
**AI proposed:** Flag as pipeline-manager skill issue (infrastructure).
**Chosen:** Assign GC (General Counsel) as primary owner, CPO (Chief People Officer) secondary.
**Reasoning:** Signed NDA not properly tracked = compliance + audit-trail integrity = GC lane. Dropped-ball pattern detection = CPO lane. Not CIO — the underlying pass decision was sound.
**Pattern:** #pattern/c-suite-routing

### Repair action
**AI proposed:** Walk the Attio entry through NDA Signed → Financials Received → Closed stages to build history.
**Chosen:** Add a detailed audit note to the Attio list entry instead.
**Reasoning:** Stage walking would create 3 timestamps all dated 4/17, making the history misleading. An audit note with real dates is the more honest record. The API rejected the stage update format anyway.
**Pattern:** #pattern/audit-over-automation-when-dates-matter

## Learnings

- **Skill specs are aspirational until proven running.** Before trusting any "auto-trigger" in a skill spec, verify: (a) the invoking schedule exists (launchd plist installed), (b) logs show recent successful runs, (c) the downstream actions actually fire end-to-end. Test post-hoc after any CIM/NDA arrival.
- **Weekly tracker is the operational backstop.** When pipeline tracking fails, weekly-tracker's human-in-the-loop ritual still captures the milestone count. Lose weekly-tracker → lose the last line of defense.
- **Audit notes beat stage-walking when dates don't match today.** For historical record-keeping, text notes preserve real dates. API-level stage changes stamp today's timestamp and make history worse, not better.
- **On DealsX launch (5/7), deal volume increases ~10x.** Silent failures tolerable today become operationally catastrophic at scale. Fix the skill hardening BEFORE launch, not after.

## Repair actions taken 2026-04-17

- Attio list entry `15b11bdf-09f7-490f-b303-b59cb176e774` updated with full audit-trail note documenting the 3/17 → 4/17 timeline
- Monday 4/20 pins (`brain/context/tomorrow-pins-2026-04-20.md`) updated with 4-point fix requirements + regression test proposal
- This trace filed for calibration-workflow to pick up on next run
