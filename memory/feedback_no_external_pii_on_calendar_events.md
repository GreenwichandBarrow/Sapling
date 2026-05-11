---
name: No external counterparty PII on Kay's calendar event descriptions
description: 2026-05-11 rule. Calendar events Kay creates for external 1:1s (conference 1:1s, prospect meetings, intermediary calls) must NOT include the external counterparty's email, phone, or other PII in the event description. Kay's own email as organizer is fine; the event is for her reference only.
type: feedback
---

When creating Google Calendar events for external 1:1s, conference meetings, prospect calls, or any meeting where the counterparty is outside G&B, **do NOT include the counterparty's email, phone, or other PII in the event description.**

**Why:** Calendar events can leak (shared calendars, exported .ics files, family-Mac shared device, screen sharing during demos). Kay's calendar is for HER reference, not as a contact-info store. Source-of-truth for counterparty contact details belongs in the Intermediary Target List sheet, Attio records, or the firm's vault entity — not in a calendar event body. Source: 2026-05-11 Kay directive after I included Krupa Shah's email + phone in a Thursday 5/14 1:1 event description.

**How to apply:**

1. **Event title:** Use the counterparty's name + firm. e.g., `ACG 1:1 with Krupa Shah (STREAM Capital Partners)`. Name + firm only, no contact info.

2. **Event description:** Reference WHERE the contact data lives, don't duplicate it. e.g., *"Tracked in Intermediary Target List, Corporate Advisors tab row 19"* or *"Attio People record ID: {uuid}"*. The description can include relationship context (meeting purpose, slot details, conference source) but NEVER the email or phone.

3. **Attendees:** Don't add external counterparties as Google Calendar attendees unless explicitly required for a video meeting or you need them to RSVP. For conference 1:1s where the counterparty already has the meeting in their conference platform (ACG portal, Brella, etc.), the Google Calendar event is for Kay's reference ONLY — `--send-updates none` and no `--attendees` flag. Kay's email as organizer is implicit and fine.

4. **Location:** Venue name OK (e.g., "ACG NY Women's Leadership Summit"). Don't include counterparty's office address or other identifiers.

5. **For internal G&B 1:1s** (Kay + JJ, Kay + Sam at DealsX, Kay + investors who've explicitly consented to calendar invites): standard attendee flow is fine. The rule applies to EXTERNAL counterparties who haven't explicitly invited themselves onto Kay's calendar.

**Failure mode to catch:** Auto-generated calendar events from conference-engagement, post-call-analyzer, or any future scheduling skill must omit external PII from description by default. If a skill needs to attach contact info, it goes in the sheet or Attio, not the calendar event.

**Related memories:**
- `project_conference_platform_comms_via_intermediary_list.md` — contact info lives in Intermediary Target List rows, not calendar events
- `feedback_brokers_stay_in_sheet_until_reply.md` — pre-reply contacts have no Attio record; post-reply they do — but calendar events still don't carry the PII
