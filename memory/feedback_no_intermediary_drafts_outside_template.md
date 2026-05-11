---
name: No Intermediary Drafts Outside Canonical Template Doc
description: All email drafts to intermediaries (brokers, IBs, lawyers, CPAs, family offices, association heads) must originate from a template in the canonical G&B Intermediary Email Templates Google Doc. No ad-hoc drafts. New scenarios require a new template added in suggestion mode for Kay's review/approval before any send.
type: feedback
originSessionId: b0545682-a352-4898-9fa7-a9ba99e3d30f
---
All intermediary email drafts must originate from a template in a canonical templates source. No ad-hoc drafts.

**Two canonical sources** (use the right one per scenario):
1. **G&B Intermediary Email Templates Google Doc** `1gTQoCbaX8IyrTDli4Xd6IBtCqCT-DwciOUnNmgv0_J4` — covers Brokers + IBs (Day 0 INTRODUCTION, Day 5 FOLLOW-UP, LEAD-YES, LEAD-NO, CIM RECEIVED, THANK YOU, DECLINE POST-REVIEW, NDA SIGNED) and Lawyers + CPAs (INTRODUCTION). Used by pipeline-manager + outreach-manager Subagent 3.
2. **G&B Conference Engagement Templates Sheet** — covers conference-attendee outreach (pre and post). Used by conference-engagement skill. Per the conference-engagement skill description, it uses the 3-audience taxonomy (Intermediary / Owner / Peer) with templates pulled from this sheet, not the Doc above.

**Why:** 2026-05-04 — when proposing a CIM auto-ack draft framing in conversation (the `{{end_of_week_date}}` window question), Kay flagged that the CIM auto-ack template doesn't even exist in the canonical doc yet, and that no intermediary email should ever be drafted outside a template. The canonical doc is the review surface; templates locked there are the only legitimate source for outbound intermediary copy. This protects voice consistency, prevents drift, and keeps Kay's approval gate at the template level (one review per template, reused N times) rather than at the per-draft level (review every send).

**How to apply:**
1. Before drafting any email to an intermediary, check the canonical templates doc for a matching template. If one exists, use it verbatim with placeholders filled.
2. If no matching template exists for the scenario (e.g., new acknowledgment type, new follow-up trigger, new audience subtype), do NOT draft ad-hoc. Instead:
   - Draft a proposed template
   - Add to the canonical Google Doc with clear "PROPOSED — pending review" markers (or suggestion mode if mechanism exists)
   - Surface to Kay for review/approval
   - Only after approval can the new template be used to generate sends
3. The pipeline-manager CIM auto-ack chain, the outreach-manager Subagent 3 (Intermediary), and any future intermediary-facing skill must reference this doc as the SOLE source for body copy. Voice rules (`feedback_no_search_fund_language_intermediaries`, `feedback_email_no_em_dashes`, `feedback_drafts_no_blockquote`, etc.) live in the doc's Voice Compliance Checklist and are enforced there.
4. The vault snapshot at `brain/outputs/2026-05-04-broker-outreach-templates.md` is a creation-time copy of the doc state at template-lock and should be refreshed only AFTER Kay approves new doc content.
