---
review_status: applied
schema_version: 1.1.0
date: 2026-05-26
type: trace
title: "Project Drone REJECT reversed + three-lane intermediary intake doctrine"
tags:
  - date/2026-05-26
  - trace
  - skill/email-intelligence
  - skill/deal-evaluation
  - verb/APPROVE
  - person/carlos-nieto-dca
  - company/digital-capital-advisors
  - topic/project-drone
  - topic/intermediary-doctrine
  - topic/pipeline-conflict
---

## Trigger

CIM for Project Drone (Carlos Nieto / DCA, AI-driven precision-ag drones) landed 2026-05-25 11:55 UTC — the deterministic next step after the mutual NDA was countersigned 5-23. Kay replied 5-25 22:03 ET: *"Thanks Carlos, I'll have a look over and follow up."* — a holding line, not a decision.

The 2026-05-20 session decisions had REJECTED Project Drone (travel-heavy + AI-exposure risk + investor-mix friction). The 5-25 email-intelligence run correctly SUPPRESSED the `<cim_auto_trigger>` 4-step pipeline per the conflict-suppression precedent. Two prior conflict-escalation inbox items existed: `2026-05-25-project-drone-nda-signed-reject-conflict` + `2026-05-25-project-drone-cim-received-conflict-escalation`.

This morning's briefing recommended *"Confirm REJECT stands → I draft decline-with-calibration to Carlos + file NDA/CIM to LEGAL holding."*

## Decision

**REVERSE the 2026-05-20 REJECT. Move Project Drone INTO active pipeline.** Kay 2026-05-26: *"We are not rejecting, we have moved forward with NDA and received CIM. Please put in active pipeline. Please update context that we will say yes to any intermediary lead but will be selective with Broker offerings. We will also say yes to any personal introductions."*

Action sequence (all executed in-session):
- Drive ACTIVE DEALS / PROJECT DRONE folder structure created (CIM/ + FINANCIALS/ + LEGAL/ + DILIGENCE/ + CORRESPONDENCE/)
- CIM (6.1 MB) filed to CIM/; countersigned MNDA (369 KB) filed to LEGAL/
- Attio Company `Project Drone` created (placeholder until de-anonymized) — id `08d198dc-f9eb-4c7e-b127-63fbea65dc60` — list entry `571b7bb8-8dce-4671-b894-de660ce0bd72` on `active_deals_owners` at stage **Financials Received**
- Slack #active-deals 200 OK
- Both prior conflict-escalation inbox items marked `resolved` with `## Outcome` pointing at new `2026-05-26-project-drone-cim-intake-deal-evaluation-trigger`
- New three-lane intake doctrine codified: [[feedback-intermediary-lead-default-yes-broker-selective]]

## Alternatives Considered

1. **Keep REJECT — draft decline-with-calibration + file to LEGAL holding (the morning brief recommendation).** Honors the 5-20 thesis-shape call. Cost: relationship with DCA + signals decline criteria narrower than Kay actually wants.
2. **Re-evaluate the deal silently without changing intake doctrine.** Project Drone gets reviewed but the underlying "REJECT at intake based on thesis shape" stays the default for future intermediary leads. Surfaces ad-hoc per-deal which makes future Claude inconsistent.
3. **Reverse the REJECT AND codify a new intake rule (chosen).** Project Drone goes to pipeline; future intermediary leads default-admit regardless of thesis-shape mismatch (decline at evaluation stage only). Future intermediary-presented deals follow the new lane.

Option 3 chosen because Kay's direction is universal: *"yes to any intermediary lead"* — not deal-specific. Codifying as memory ensures consistency.

## Reasoning

The cost of declining intermediary leads at intake stage is relationship + future deal flow from that intermediary. The cost of accepting and properly diligencing through the pipeline is one cycle of evaluation work. The pipeline already has decline-with-calibration as its exit mechanism — let it do its job.

**Three lanes (codified):**
1. **Intermediary-presented deal lead** (sell-side advisor presenting a specific company — Carlos / DCA, individual Generational Equity pitches): default YES, admit to pipeline, evaluate properly, decline only post-CIM if criteria fail.
2. **Broker BLAST offering** (mass-market listings, BizBuySell/Flippa digests): SELECTIVE, apply thesis-shape filters at intake.
3. **Personal introduction** (warm intro from network): default YES per [[feedback-bias-yes-on-introductions]].

Hard excludes (US-only, no CA, no PE-owned, no aviation, no lending, no NYC-construction, no carve-outs) still apply at intake. Thesis-shape concerns (travel-heavy / AI-exposed / investor-mix friction) move to deal-evaluation stage, not intake.

The `<cim_auto_trigger>` skill's REJECT-conflict pre-check (proposed in this morning's email-scan-results calibration candidates) is now WRONG under rule 1 — don't add it. Original deterministic 4-step pipeline is correct for intermediary CIMs.

## Why This Trace Matters

Without this trace, a future agent encountering a Carlos Nieto deal pitch would default to the 5-20 REJECT pattern (or re-evaluate per case ad hoc). The shift from thesis-shape REJECT-at-intake to evaluate-through-pipeline is non-obvious and applies broadly — not just to Project Drone. Future intermediary leads need to be admitted, not screened out by thesis shape.

Also: the suppression doctrine for `<cim_auto_trigger>` based on prior REJECTs is REVERSED. The trigger fires for intermediary CIMs even when the deal's thesis-shape was previously REJECT'd.

## Key Insight

**Lane-based intake routes deals to different DECISION points, not different INCLUSION criteria.** Intermediary leads route to deal-evaluation (post-CIM judgment). Brokers route to intake screen (gate at the door). Personal intros route to conversation-first (no gate at all). Reversing Project Drone wasn't a one-off — it surfaced that the intake gate was over-aggressive for the intermediary lane.

Open question Kay deferred: does this reverse the OTHER DCA AI-exposed tech deal REJECT'd on 5-20? Surfaced in tomorrow's brief.
