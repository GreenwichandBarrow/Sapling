---
name: Show rendered template for approval before bulk-drafting N emails
description: When a skill would draft N personalized emails in Superhuman, first show Kay the rendered template(s) in a Google Doc for approval. Drafts only go out after the template is locked.
type: feedback
originSessionId: 79db8074-299b-4018-a98a-3aced9a42eb3
---
Before drafting N personalized emails (to Superhuman, email, Slack, or anywhere else), show Kay the underlying template(s) in a rendered form for approval. Only after she approves or tunes the template should the bulk drafts be generated.

**Why:** Reviewing 1 template is an order-of-magnitude lower decision cost than rejecting or editing N drafts. Per `feedback_decision_fatigue_minimization`, every interaction should reduce Kay's decision surface. A bad template × N recipients = N mistakes; a reviewed template × N recipients = N correct starting points. This is especially true on first runs of a skill, when template language hasn't been battle-tested on a real send.

Also per `feedback_remove_kay_from_loop`: the engine should catch template errors BEFORE Kay is in the customize-and-send loop, not after.

**How to apply:**
- Any skill that drafts N > 3 personalized outputs using a shared template must produce a template review artifact FIRST.
- Artifact is a Google Doc in the appropriate Drive folder (G&B Master Templates for outreach templates, RESEARCH/BRIEFS for brief templates, etc.).
- Artifact shows the rendered template with sample/illustrative variable values filled in, NOT the raw `{{placeholder}}` version.
- Per `feedback_rules_in_skill_not_template`, the review artifact contains ONLY templates — no voice-rule preambles, no how-to-use sections, no skill metadata.
- Kay reviews. APPROVE means push drafts. Any edits she makes in the doc sync back to the authoritative template store (Sheet, etc.) before drafts go out.
- When the skill has been run successfully multiple times and the template is stable, the review step can be skipped on future runs unless the template materially changes (new variant, new audience, buy-box paragraph updated, voice rule shifted). Stability is established by Kay's own pattern of approvals without edits.

**Precedent:** 2026-04-23 conference-engagement first run for XPX. Kay wanted to review the rendered template before 8 drafts went to Superhuman. She wrote a better buy-box paragraph after seeing the rendered doc, which would have otherwise been baked into all 8 Superhuman drafts.
