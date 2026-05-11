---
name: Post-conference replies are reactive only — no cold outbound to silent attendees
description: After a conference, Kay replies to attendees who reach out to her. She does NOT initiate cold outbound to attendees who collected her card but didn't follow up. Don't surface silent attendees as "dropped balls."
type: feedback
originSessionId: ed3ad1c6-9dba-4abb-b157-7867abbc3c13
---
After a conference (XPX, ACG, etc.), the conference-engagement workflow is **reactive by default**. The gate is depth of in-person conversation, not email reciprocity alone.

**The actual rule, in two cases:**

- **Silent + shallow card-swap = no outbound.** Attendee collected Kay's card, didn't reach out, no substantive conversation occurred. Don't surface as dropped balls. Vault entity stub for hygiene, but no draft, no reply.
- **Silent + substantive in-person conversation = follow up proactively.** If Kay had a real conversation with the attendee (they shared a specific deal lead, asked her buy-box questions, gave her substantive context about their book of clients), she initiates the email. Their not-reaching-out doesn't matter — the in-person engagement was the signal.

**Why:** Refined 2026-04-25 wrapping the XPX 2026-04-23 reply backlog. Initial pass said "silent = no outbound" based on Kay's "I will not have to work with you to send emails to the 3 that did not reach out." Within the same hour, Kay then said "Matt is the one about the aerospace defense — let's work on that one," because Matt Luczyk (Peapack Private) had told her in person about a specific seller client AND asked her buy-box questions. The depth of his in-person engagement made him a "follow up proactively" case despite his email silence. Charles Gerber and Pasang Jamling stayed in the no-outbound bucket because their in-person interactions were thinner.

**How to apply:**

- After any conference where Kay collects business cards, classify each card by depth of in-person interaction (Kay's call, surfaced via card processing flow):
  - **Substantive:** real conversation, specific deal mentioned, buy-box questions asked, river-guide signals, named-owner intros offered. → Outreach drafted regardless of email status.
  - **Shallow:** card swap, brief hello, no substantive content. → Reactive only — wait for them to email first.
- For attendees who email Kay first: full reply-flow variant per `conference-engagement` SKILL — vault entity + Attio person record + reply draft.
- For shallow + silent attendees: vault entity stub still gets created (close-out hygiene per `feedback_close_out_executes_mutation`) but **no draft, no reply, no surfacing as dropped balls** in subsequent briefings.
- Don't include shallow + silent attendees in `relationship-status-{date}.md` overdue lists or conference-engagement-loop tables. They're not a slipped follow-up — they're a non-engaged contact.
- If Kay later asks "did anyone from [conference] go quiet?" — surface them then. Otherwise leave the stubs idle.
- This refines `feedback_no_cold_outreach_to_strangers` for the conference-card sub-case: the *card swap alone* doesn't create a Kay-side outreach obligation; either the email-back OR the substantive in-person conversation does.

**Calibration candidate:** Update `conference-engagement` SKILL to encode this two-axis classification (depth-of-conversation × inbound-reply-status). Today's flow assumes all cards get the same treatment; should branch on the depth tag from card processing.
