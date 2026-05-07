---
schema_version: 1.1.0
date: 2026-05-04
type: trace
title: "Intermediary email body must come from a canonical template — no ad-hoc drafts"
trace_type: doctrine-establishment
tags: ["date/2026-05-04", "trace", "topic/intermediary-outreach", "topic/template-doctrine", "topic/voice-calibration"]
---

# Intermediary email body must come from a canonical template — no ad-hoc drafts

## Trigger

While building the CIM auto-ack reply chain (BOTH-FIRE pattern in pipeline-manager Step 5), I drafted a CIM-RECEIVED template body inline in conversation, including a `{response_window}` placeholder with two options for Kay to pick. Kay's response: "there shouldnt be any email drafts that arent on a template and that one is not in the template. Please input any drafts you are planning for the intermediaries and put them on the google doc for my review and approval."

The template I'd drafted didn't exist in the canonical Intermediary Email Templates Google Doc. I'd improvised body copy in chat. Kay flagged the doctrine gap: the canonical doc is the review surface, templates locked there are the only legitimate source for outbound intermediary copy.

## Decision

Established new permanent doctrine: **all intermediary email drafts must originate from a template in a canonical templates source.** Two canonical sources (chosen per scenario):
1. `G&B Intermediary Email Templates` Doc `1gTQoCbaX8IyrTDli4Xd6IBtCqCT-DwciOUnNmgv0_J4` — for pipeline-manager + outreach-manager Subagent 3 paths.
2. `G&B Conference Engagement Templates` Sheet `1Y4XcQJDe28RB7k_Cw5NZNjKRyX4d1qEczadXdQrjpaQ` — for conference-engagement paths.

If no template covers the scenario: propose a new template in the canonical source for Kay's approval first, then use it. Never improvise body copy in chat.

Captured as `feedback_no_intermediary_drafts_outside_template` memory + CLAUDE.md pre-flight checklist line + skill code template-gates in pipeline-manager Step 5 + outreach-manager Subagent 3 + conference-engagement.

## Alternatives considered

1. **Continue ad-hoc drafting with conversation review** — what I'd been doing. Rejected because it puts review burden at the per-draft level instead of the per-template level (Kay reviews the same body 100 times instead of once).
2. **Single canonical doc for everything** — would force conference-engagement to migrate from Sheet to Doc. Rejected because the Sheet has a specific 6-template + Snippets structure that maps to conference-engagement's audience-detection + buy-box-snippet substitution flow. Two canonical sources is fine as long as routing is explicit.
3. **Code-level PreToolUse stop hook on `gog gmail draft`** — would block ad-hoc drafts at the harness layer. Rejected tonight because: high false-positive rate (recipient classification is stateful, template-source verification requires cross-tool state), and existing layers (CLAUDE.md pre-flight + skill code mandatory template lookup) are sufficient. Revisit if a doctrine violation actually slips through.

## Reasoning

Voice consistency is load-bearing. Intermediary outreach is high-stakes because brokers gossip — if Kay's outreach to broker A reads inconsistently with broker B's, it damages credibility. Template-source-of-truth puts the voice gate at the template level, where Kay reviews once carefully. Ad-hoc body copy in chat introduces drift even when each individual draft "looks fine" — drift compounds across hundreds of touches.

Memory + CLAUDE.md + skill code = three layers of defense. A future agent encountering this rule gets it from any of three places.

## What would change if reversed

If a future agent decides to draft ad-hoc instead of pulling from canonical doc, the immediate failure mode is voice drift on intermediary outreach. The deeper failure is loss of the review-once-use-many leverage Kay built into the canonical doc. Brokers would receive subtly different versions of "the same" message, and any voice problems Kay catches in one draft don't propagate to fix the others.

The pre-flight checklist line ("Intermediary email body MUST originate from a canonical template") and the skill code mandatory `gog docs export` gate are both designed so that even if memory recall fails, the doctrine surfaces.
