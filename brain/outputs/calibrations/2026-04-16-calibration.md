---
schema_version: 1.0.0
date: 2026-04-16
type: output
output_type: calibration
title: "Calibration — 2026-04-16 (13 traces, week of 2026-04-10 → 2026-04-16)"
tags: ["date/2026-04-16", "output", "output/calibration", "status/proposed", "topic/calibration"]
---

# Calibration Report — 2026-04-16

## Summary

- **Traces analyzed:** 13
- **Unique proposals after dedup:** 12
- **Critical:** 1 (already applied) · **High:** 5 · **Medium:** 4 · **Low:** 2
- **Weekly tracker signal:** Owner conversations = 0 for 4 straight weeks. Outreach volume critically low (1 email / 4 business days). DealsX onboarding April 10 is the throughput unlock the system is waiting on. Calibration should NOT propose more manual workflows that sit on top of Kay — it should remove them.

The week's dominant theme: **thesis architecture matured faster than it was documented**. 7 of 13 traces are frame-level rules the agents should have had before the week started (SaaS filter vs scorecard, AI-native disruption lens, Col D routing determines cadence, time-budget as a first-class demotion reason). The skills are now playing catch-up to Kay's operating model.

---

## Critical (1)

### [C1] Pipeline-manager outbound-scan creates missing Attio Active Deals list entries
**Source traces:** 2026-04-15-pipeline-manager-outbound-scan-gap
**Target:** `.claude/skills/pipeline-manager/SKILL.md`
**Problem:** Outbound email to recipient with Person record but no Active Deals list entry was silently skipped. Timothy Wong / MMPC sat un-entered for 6 days.
**Proposed change:** Path A/B/C reconciler-and-creator logic.
**Status:** **ALREADY APPLIED** 2026-04-15. Lines 261–264 (section 11 of the workflow) and lines 346–370 (Path A/B/C) of `pipeline-manager/SKILL.md` now implement the fix. The trace records the rationale; no further edit needed. Mark trace as `review_status: applied`.
**Agents concurring:** ARCH
**Applicable?:** N/A — already in skill.

---

## High (5)

### [H1] CIO agent: encode SaaS buy-box revenue band 2–6M ARR (separate from generic G&B band)
**Source traces:** 2026-04-15-saas-revenue-band-revised (Sam Singh, DealsX call 4/15)
**Target:** `.claude/agents/cio.md`
**Problem:** CIO's hard-filters block enumerates PE-owned, California, aviation, lending, etc. — but no explicit SaaS revenue band. Current implicit assumption is the generalist G&B band. Sam's calibration (from hundreds of DealsX campaigns): searchers buy 2–6M ARR SaaS. 10M ARR SaaS = $30M deal = independent-sponsor/PE territory, not search.
**Proposed change:** Add a new "Model-specific bands" block under Hard Filters:

```
## Model-specific revenue bands
- SaaS / vertical SaaS / data platforms: $2M–$6M ARR (per Sam Singh / DealsX, 2026-04-15).
  Floor $2M if the underlying business is good; ceiling $6M because a 3–4× revenue
  multiple at $10M ARR = $30M acquisition, out of search range. Flag any SaaS target
  outside 2–6M as out-of-buy-box for SaaS evaluation.
- Services / brokerage / distribution: existing G&B buy-box band (unchanged).
```

**Agents concurring:** ARCH, PAT
**Applicable?:** YES — small edit to cio.md.

---

### [H2] Niche-intelligence: add AI-native-vs-AI-enhanced disruption screen + physical-vs-documentation workflow split
**Source traces:** 2026-04-16-ai-native-vs-ai-enhanced-lens
**Target:** `.claude/skills/niche-intelligence/SKILL.md` (Step 2 Identify criteria) + new memory `feedback_ai_native_vs_enhanced_lens.md`
**Problem:** Kovr.ai forced Kay to stress-test the vertical SaaS thesis. Acquire-and-modernize produces AI-enhanced, not AI-native; the gap is 10× not 1.5× and customers migrate. Pattern extends: physical-workflow verticals are structurally defended (vet, funeral, childcare, estate mgmt, PT, fertility, senior living, premium pest); documentation-workflow verticals need AI-native stress-tests (healthcare regulatory compliance, digital accessibility compliance, behavioral health practice mgmt docs layer).
**Proposed change:**
1. Niche-intelligence Step 2 Identify: add a required classification field `workflow_type: physical | documentation | hybrid`. Documentation/hybrid niches must pass an explicit "AI-native incumbent stress test" question before scoring (not killing — stress-testing).
2. Memory: `feedback_ai_native_vs_enhanced_lens.md` capturing the principle + the physical/documentation split.
**Agents concurring:** ARCH, PAT, SIMP
**Applicable?:** YES for memory; YES for a short Step 2 addition. The full stress-test rubric is INBOX (can be added iteratively).

---

### [H3] Niche-intelligence: enforce SaaS Filter (Jake + Adam) as a gate BEFORE the G&B scorecard, not a replacement for it
**Source traces:** 2026-04-12-saas-filter-vs-scorecard, 2026-04-12-adam-right-to-win-reframe, 2026-04-11-specialty-healthcare-niche-selection
**Target:** `.claude/skills/niche-intelligence/SKILL.md`
**Problem:** Three traces converge on a structural point: SaaS Filter is a pass/fail qualification gate; G&B Scorecard is a ranking tool among qualified niches. Instinct (after Specialty Healthcare scored 2.24–2.51 vs actives at 2.60–2.81) is to rework the scorecard. That's wrong — it would erase signal. Filter and scorecard reward different structural features; both must run in order.
**Proposed change:** Niche-intelligence Step 2 (Identify) must tag each candidate as `niche_category: saas | services | brokerage | distribution`. SaaS-tagged niches run the SaaS Filter BEFORE Step 3 (one-pager) — filter-fail niches stop, do not waste work. Filter-pass SaaS niches proceed to scorecard with the understanding that a 2.25 score on filter-pass is more interesting than 2.57 on filter-fail. Non-SaaS niches skip the filter and run the scorecard normally.
**Agents concurring:** ARCH, PAT
**Applicable?:** YES — add a ~20-line block to Step 2 of niche-intelligence/SKILL.md. The SaaS Filter rubric itself lives in `references/saas-filter.md` (INBOX — create later).

---

### [H4] CIO agent: broaden "right-to-win" to accept 3 forms, not just industry-operator experience
**Source traces:** 2026-04-12-adam-right-to-win-reframe, 2026-04-11-specialty-healthcare-niche-selection, 2026-04-16-ai-native-vs-ai-enhanced-lens
**Target:** `.claude/agents/cio.md`
**Problem:** CIO default question #2 ("Does Kay have a right-to-win here?") is undefined. Adam Aisen precedent (no senior-care operator background, grew ECP to Level Equity exit at ~15× ARR via adjacent tech fluency + sector pattern recognition) plus Kay's own AI-native-rebuild experience prove right-to-win is broader than direct operator experience.
**Proposed change:** Update CIO's "Soft signals" and question #2 with the 3-form definition:

```
Right-to-win has three acceptable forms:
  1. Industry-operator experience (traditional)
  2. Adjacent tech/sector expertise (Adam Aisen / ECP model — Google + prior healthcare tech investing)
  3. Investor / network credibility + lived-experience pattern recognition
     (Kay: finance/PE + women's health nonprofit + luxury operations + AI-native rebuild)
Any ONE form clears the filter. Two is stronger. None = KILL.
```

**Agents concurring:** ARCH, PAT
**Applicable?:** YES — small edit.

---

### [H5] Outreach-manager: JJ-Call-Only route Day-0 email is SUPPRESSED until phone acknowledgement
**Source traces:** 2026-04-15-channel-mix-by-route
**Target:** `.claude/skills/outreach-manager/SKILL.md` + `.claude/skills/jj-operations/SKILL.md`
**Problem:** Current outreach-manager treats Day-0 email uniformly. For JJ-Call-Only targets, sending a Day-0 email before JJ confirms phone acknowledgement is a volume-outreach signal — contradicts Kay's 5/day thoughtful brand. Trace specifies: email triggered ONLY on "Connected + Interested" or "Connected + Curious". No email after voicemail / no-answer / wrong-number.
**Proposed change:**
1. outreach-manager SKILL.md — add explicit rule near line 42 (the niche routing table): JJ-Call-Only Day-0 email is suppressed; first email only after JJ logs `Connected + Interested` or `Connected + Curious` on the call log. Any tooling must read JJ's call-log status column before queuing an email.
2. jj-operations SKILL.md — call log schema must include an `acknowledgement_status` column with explicit values: `Connected+Interested`, `Connected+Curious`, `Connected+NotReady`, `Voicemail`, `NoAnswer`, `WrongNumber`. This is load-bearing for the email gate.
**Agents concurring:** ARCH
**Applicable?:** YES for outreach-manager rule. Call-log schema change in jj-operations is a smaller edit (~10 lines).

---

## Medium (4)

### [M1] Memory: add `feedback_cold_warm_hybrid_dm_pattern.md` + extend no-contact rule scope
**Source traces:** 2026-04-16-cold-warm-linkedin-dm-strategy, 2026-04-16-lacey-mention-vs-reengage-distinction
**Target:** Memory — new file + updates to `feedback_never_reask_decided.md` or a new `feedback_no_contact_rule_scope.md`
**Problem:** Two distinct patterns worth codifying:
  (a) Cold-warm hybrid DM — send cold DM, mention mutual connection by name; target verifies on LinkedIn; no intro-ask burns the connector.
  (b) No-contact rule scope — "no contact with X" means no outreach TO X, not suppressing X from the world. Mentioning X as social proof to a third party is allowed when X is never contacted.
**Proposed change:** Two memory files:
  1. `feedback_cold_warm_hybrid_dm_pattern.md` — pattern, when to use, with Lacey-mentioned-to-Bryan as a canonical example.
  2. `feedback_no_contact_rule_scope.md` — the scope rule, with reasoning = protect Kay's intent (relationship boundary), not the literal word "contact".
**Agents concurring:** PAT
**Applicable?:** YES.

---

### [M2] Conference-discovery: annotated-attendee-list routing (do not bulk catalog)
**Source traces:** 2026-04-16-cold-warm-linkedin-dm-strategy
**Target:** `.claude/skills/conference-discovery/SKILL.md`
**Problem:** ACG NY DealSource had 54 attendees; Kay annotated only 4 as "1" (would-have-met) with mutual-connection notes. Default skill behavior would be to bulk-catalog all 54 into Attio. That dilutes signal (per `feedback_broker_competition`: IB/PE conference rosters are the "3000+ buyers" noise pool). Kay's annotations are the signal.
**Proposed change:** Conference-discovery attendee-list processing must detect two list modes:
  - **Annotated mode:** Kay's column ranks/notes present → act only on ranked rows (default: cold-warm hybrid DM with mutual-connection mention). Leave un-ranked rows as a Drive reference file, NOT Attio entries.
  - **Unannotated mode (speaker/small-format events):** bulk-catalog is acceptable because the whole list is pre-filtered.
**Agents concurring:** ARCH, SIMP
**Applicable?:** YES — small addition to conference-discovery/SKILL.md.

---

### [M3] Outreach-manager: add `cold-warm hybrid DM` as a formal third channel
**Source traces:** 2026-04-16-cold-warm-linkedin-dm-strategy
**Target:** `.claude/skills/outreach-manager/SKILL.md`
**Problem:** Current outreach-manager has pure-cold and warm-intro channels. Cold-warm hybrid (mention mutual connection without asking connector for anything) is a distinct third channel. Without formalizing it, skill defaults to warm-intro-finder which over-spends connector goodwill.
**Proposed change:** Add `cold-warm hybrid` as a named channel in outreach-manager. Rule: when a target has an annotated mutual connection AND the connector is inconvenient (time, depth, or prohibited by a rule — e.g., Lacey), default to cold-warm hybrid rather than warm-intro request.
**Agents concurring:** SIMP, ARCH
**Applicable?:** YES — small edit.

---

### [M4] Niche-intelligence: "filter vs niche" labeling discipline
**Source traces:** 2026-04-11-specialty-healthcare-niche-selection, 2026-04-12-dealsx-industry-bucket-model
**Target:** `.claude/skills/niche-intelligence/SKILL.md`
**Problem:** "Compliance-Driven System-of-Record Vertical Software" is a filter Kay applies to pick sub-verticals; it is NOT a niche Sam searches. Same confusion would send DealsX on an impossible Apollo query. Kay's right-to-win for Specialty Healthcare is applied as a *filter* inside the broad niche, not by narrowing the niche.
**Proposed change:** Niche-intelligence Step 2 (Identify) requires each candidate to be labeled explicitly as `label_type: niche | filter`. Niches are what DealsX/target-discovery searches. Filters are what Kay applies to select sub-segments or rank targets. Never hand DealsX a filter as if it were a niche.
**Agents concurring:** ARCH, PAT
**Applicable?:** YES — small addition to Step 2.

---

## Low (2)

### [L1] Niche-intelligence: codify gut-pull + analytical validation as the selection model (scorecard = validate, never select)
**Source traces:** 2026-04-10-vertical-saas-thesis-conviction
**Target:** `.claude/skills/niche-intelligence/SKILL.md` (Step 4 SCORE + Step 5 UPDATE)
**Problem:** Kay rejected forcing a 3rd/4th niche to fit scorecard output. Existing memory (`feedback_niche_selection_process`) captures the principle but the skill doesn't enforce it at the workflow level — Step 4 (Score) could auto-advance a top-scored niche Kay has no pull toward.
**Proposed change:** Step 4 output must present top-3 as candidates, never as "winner". Step 5 promotion to WEEKLY REVIEW requires explicit Kay pull-through signal (gut pull) separate from the score. No auto-promotion on score alone.
**Agents concurring:** PAT
**Applicable?:** YES — small rewrite of 2-3 lines in Step 4 description.

---

### [L2] MEMORY.md curation — index is 325 lines / 46.7KB (warned over-budget)
**Source traces:** (system signal, surfaced in context)
**Target:** `/Users/kaycschneider/.claude/projects/-Users-kaycschneider-Documents-AI-Operations/memory/MEMORY.md` + stale memory files
**Problem:** MEMORY.md is above the 200-line threshold. Entries that are redundant or fully absorbed into skills can be retired.
**Proposed retirements** (safe to remove because the rule now lives in code/skills, not just memory):
  - `feedback_linkt_is_list_builder.md` — Linkt cancelled 3/31/2026; superseded by Apollo + DealsX.
  - `feedback_one_webhook_test.md` — process hygiene that's been internalized; not referenced in ongoing workflows.
  - `feedback_gmail_drafts_cleared.md` — subsumed by `feedback_superhuman_drafts_only.md`.
**Proposed consolidations:**
  - Merge `feedback_draft_before_send.md` (appears twice in index) into a single entry.
  - Merge `feedback_jj_no_kay_name.md` (also appears twice) into a single entry.
**Agents concurring:** SIMP
**Applicable?:** YES — mechanical edit. Low risk.

---

## Proposals routed to /create-skill inbox (not applied directly)

1. **Conference-discovery + river-guide-builder merge.** Both skills operate on the same event-attendee data source (trace #7: "Ideally they become one skill or share one event-pipeline datastore"). A full merge is a larger architecture decision — parks in inbox for a future dedicated session. Interim fix (this calibration): both SKILL.md files already reference the shared Conference Pipeline sheet, so no duplication is currently happening — merge is nice-to-have, not urgent.
2. **Slack inbound scan for pipeline-manager.** Trace #9 flagged Timothy Wong's response arriving via team Slack, invisible to Gmail-based scans. Requires MCP Slack integration + security review. INBOX.
3. **SaaS Filter reference doc (`references/saas-filter.md`).** Jake Stoller's 7-dimension defensibility rubric + Adam Aisen's Datacor business-structure pattern. The gate logic belongs in SKILL.md (this calibration). The full rubric is its own deliverable — INBOX.
4. **Agent-Kay Alignment metric pipeline.** Skill doc describes reading Col Q (Agent Notes) vs Col O (Kay Decision) across 5 target sheets and computing alignment %. Needs a dedicated script before the pattern-recognizer agent can compute it reliably. INBOX.

---

## Meta observations

1. **Learning velocity is accelerating.** 13 traces in 7 days vs typical week. 5 of 13 from April 15 alone, all tagged `frame_learning: true`. This is what a thesis-consolidation week looks like after a major input (Sam Singh / DealsX call + Kovr.ai stress test). Do not over-process — many of this week's traces will become dormant reference material once the rules are encoded.
2. **AI keeps re-learning three distinctions.** (a) niche vs filter vs scorecard (3 traces), (b) right-to-win narrower than reality (3 traces), (c) pure cold vs pure warm missing a hybrid (2 traces). Each is a sign the prompts/skills don't yet carry the definitional load.
3. **Kay's time-budget is the load-bearing constraint.** Trace #8 is the strategic one: Kay's exit from list-scrubbing is first-class direction for the next 4 weeks of system evolution. Every proposal in this calibration was filtered through "does this put Kay back into toil?" Where answered yes, proposal was reframed or routed to DealsX.
4. **Conference-discovery is Kay's unlock channel.** Trace #7 + weekly-tracker data (4 weeks of 0 owner conversations) converge: grass-roots intermediary networking is the path out of the conversation drought, not more outbound email volume.

---

## Result banner

_(will be filled after Kay selects changes)_
