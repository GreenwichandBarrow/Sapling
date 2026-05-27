---
name: feedback-chat-drafts-dont-land-in-gmail
description: "When Kay says \"draft\" in conversation about email copy, iterate on the text in chat only. Never create the Gmail draft until she explicitly asks (e.g., \"create the draft in Gmail\" / \"save this to drafts\" / \"ready, file it\")."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: c4d1136f-f761-402e-8241-8a567c090bbe
---

When Kay says "draft" in conversation about an email/message, present the body text in the chat for back-and-forth iteration. **Do NOT create a Gmail draft** until she explicitly asks for it ("create the draft in Gmail" / "save this to drafts" / "ready, file it" / equivalent).

**Why:** Iterating on copy is a fast loop in chat. Pre-landing the draft in Gmail creates a stale-draft cleanup burden every time we revise — and Kay already has the text from the chat the moment she sees it. Premature draft creation is friction, not service. (Recurring failure 2026-05-22: she asked me to draft a reply to Sam Lamson, I shipped the body to chat AND created the Gmail draft; she corrected — she only wanted the chat back-and-forth.)

**How to apply:**
- Default mode for any "draft a reply to X" / "draft an email to Y" / "write back to Z" request: present the body text inline in the chat. Offer **YES (post to Gmail drafts) / EDIT / NO** but do NOT preemptively create the draft.
- Wait for her explicit "yes, create" / "save it" / "ready" before invoking `gog gmail draft create` or any wrapper.
- This OVERRIDES the pipeline-manager / email-intelligence "create draft for review" pattern when the request originated as a chat-iteration request rather than as an auto-trigger (CIM auto-ack, follow-up cadence, etc.). Skill-triggered drafts still land in Gmail per their own SKILL.md doctrine; conversational drafts do not.
- Distinct from [[feedback-kay-handles-all-replies]] (which is about not auto-sending). This is about not auto-CREATING.
