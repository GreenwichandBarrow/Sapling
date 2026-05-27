---
name: feedback-intermediary-lead-default-yes-broker-selective
description: Default-YES posture toward intermediary leads (sell-side advisor deals presented individually); SELECTIVE toward broker offerings (BLAST mass-market listings). Codified 2026-05-26 after Project Drone REJECT reversal.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 37de3c90-d2d0-44f1-9b4b-ddb0727158c9
---

Default-accept any specific deal lead brought by a sell-side intermediary; default-screen mass-broker offerings; default-accept any personal introduction. These are three different decision rules, not one rule applied with different weights.

**Why:** The 2026-05-20 REJECT on Project Drone (DCA / Carlos Nieto, AI drone agtech) was reversed on 2026-05-26 — Kay signed the MNDA on 5-23, received the CIM on 5-25, and on 5-26 directed: *"We are not rejecting, we have moved forward with NDA and received CIM. Please put in active pipeline. We will say yes to any intermediary lead but will be selective with Broker offerings. We will also say yes to any personal introductions."* The cost of declining intermediary leads at intake stage is relationship + future deal flow from that intermediary; the cost of accepting and then properly diligencing through the pipeline is one cycle of evaluation work. The pipeline already has decline-with-calibration as its exit mechanism — let it do its job. This generalizes the [[feedback-bias-yes-on-introductions]] rule from personal introductions to intermediary-presented deals.

**How to apply:**

1. **Intermediary-presented deal lead** (sell-side advisor or M&A firm presenting a specific company for sale — e.g., Carlos Nieto / DCA, individual deal pitches from Generational Equity reps, Sunbelt brokers presenting a specific listing): **default YES — admit to pipeline.** Evaluate through normal deal-evaluation flow; decline only if criteria fail after CIM/financials review. Do NOT decline at intake based on thesis-shape mismatch alone — the courtesy of evaluation is the cost of preserving the intermediary relationship.

2. **Broker offering (mass-market BLAST listing)** — broker emails carrying multiple listings per body, Flippa/BizBuySell marketplace digests, generic "exclusive listing" blasts: **SELECTIVE.** Apply [[feedback-broker-competition]] + [[feedback-broker-channel-opportunistic-floor]] + thesis-shape filters at intake. Most don't make it to pipeline. Section-7 broker-BLAST extraction still runs for tracking volume; pipeline admission is screened.

3. **Personal introduction** (warm intro from network, "I'd like you to meet…"): **default YES — take the conversation** per [[feedback-bias-yes-on-introductions]]. The intro itself is the asset.

**Key distinction:** Intermediary lead (rule 1) ≠ broker offering (rule 2). Same source can produce both — a BLAST email from a broker is rule 2; a personally-curated one-deal pitch from the same broker is rule 1. The signal is curation, not the sender's job title.

**Pipeline entry mechanics for rule 1:** CIM received → run `<cim_auto_trigger>` 4-step pipeline (Drive folder + Attio "Financials Received" + inbox + deal-evaluation invocation). The previous REJECT-conflict suppression pattern from [[brain/inbox/2026-05-25-project-drone-cim-received-conflict-escalation]] no longer applies — REJECT at the 5-20 thesis-shape level is NOT a sufficient suppression signal for intermediary leads under this rule. Only an explicit Kay-directive "decline this specific deal" suppresses the pipeline.

**Open question (not auto-actioned):** the other DCA AI-exposed tech deal REJECT'd on 5-20 — does this rule reverse that too? Surface for Kay's call; do not presume.

**Edge cases:**
- Hard excludes (US-only, no CA, no PE-owned, no aviation, no lending, no carve-outs, no NYC-construction) still apply at intake — these are jurisdictional / structural hard-stops, not thesis-shape preferences. Decline an intermediary lead at intake ONLY if it hits a hard exclude.
- "Travel-heavy" / "AI-exposed" / "investor-mix friction" are thesis-shape concerns, NOT hard excludes — under rule 1 they move to the deal-evaluation stage, not the intake decision.
- Industry-level exclusions (e.g., collectibles specialty insurance as a category, per 5-20) still apply.

**`<cim_auto_trigger>` calibration:** Skill text needs an update — the REJECT-conflict pre-check pattern proposed in the 2026-05-26 email-scan-results calibration candidates is now WRONG under rule 1. Don't add it. The original deterministic 4-step pipeline is the right behavior for intermediary CIMs.

See also: [[feedback-bias-yes-on-introductions]], [[feedback-broker-competition]], [[feedback-broker-channel-opportunistic-floor]], [[feedback-marketplace-vs-broker-distinction]], [[feedback-classify-intermediary-by-self-id]], [[feedback-no-pe-owned-targets]].
