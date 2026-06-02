---
date: 2026-06-02
type: relationship-status
---

## Overdue Contacts (Top 5)

1. **Kristina Marcigliano** (Willis Towers Watson) — Quarterly, last contact 2025-12-23, **161 days overdue** (threshold: 98d)
   Email: kristina.marcigliano@wtwco.com
   Suggested action: quarterly check-in email (insurance professional; women-priority per standing doctrine)
   Note: No Attio nurture_cadence set on her record — she appears in the overdue list because her last_interaction pre-dates the quarterly threshold. Recommend setting nurture_cadence = Quarterly in Attio.

2. **Molly Epstein / Goodman Taft** (via Chase Lacson record) — Monthly, last Attio interaction 2025-10-28, **217 days** since logged interaction. Attio next_action: "Reconnection email sent to Molly 3/30. Awaiting reply." — March 30 email has gone 63 days unanswered.
   Email: mee_admin@goodmantaft.com (Chase admin); Molly Epstein is the principal.
   Suggested action: gentle follow-up on the March 30 email — one brief nudge, then close loop if no reply.

3. **Hunter Hartwell** (Ellirock) — Quarterly, last contact 2026-01-14, **139 days overdue** (threshold: 98d)
   Email: hunter@ellirock.com
   Suggested action: quarterly email check-in; no specific next_action logged.

4. **Kyle McGrath** (Markel) — Quarterly, last contact 2026-02-10, **112 days overdue** (threshold: 98d)
   Email: kyle.mcgrath@markel.com
   Attio next_action: "No immediate action. Maintain quarterly touchpoint."
   Suggested action: quarterly touchpoint — coffee or short call.

5. **Christopher Wise** (Risk Strategies) — Quarterly, last contact 2026-02-18, **104 days overdue** (threshold: 98d)
   Email: cwise@risk-strategies.com
   Attio next_action: "Quarterly nurture. No immediate action."
   Suggested action: quarterly email check-in.

**Contacts reviewed and NOT surfaced (reasons logged):**
- Britta Nelson: Attio next_action confirms text contact "late March 2026" (~63d ago) → within quarterly threshold. Not overdue.
- Austin Yoder (hello@cal.com): Duplicate record; real record (austin@magratheapartners.com) last contact 2026-03-23 = 71d, within quarterly threshold.
- Squarespace (customercare@squarespace.com): Vendor auto-email address, not a real relationship.
- bluerideradmin@morganstanley.com: Role/system email, not a real contact relationship.
- Donald Moore (Marsh, 217d Occasionally): Attio next_action says "Nurture bi-annually. No immediate action." — borderline at 217d vs 213d threshold but next_action signals no urgency. Noted in Metadata Drift below.
- Alexandra Kelly (UOVO Art): Trigger — "On maternity leave. Do not contact until she returns."
- August Felker: Trigger — "Re-engage when we have an insurance deal for him to review."
- Jim Vigna: Trigger — "Quarterly nurture; escalate when active deal financing comes into play."
- Ian Stuart: Trigger — "Re-engage only if portfolio fractional CFO need arises."

*Note: Gmail and calendar are the only verified interaction channels. Kay also communicates via text and phone. Contacts with Attio next_action evidence of recent non-email contact (e.g., Britta Nelson) are trusted and not surfaced.*

## Auto-Resolved (No Action Needed)

None — no outbound emails found in the 14-day Gmail verification window for any overdue contact.

## Pending Intros / Open Actions

- **Sam Curcio (Transworld of NY):** Post-call thank-you (canonical Intermediary Email Templates) + proof-of-funds letter still outstanding. Call was 2026-05-22 (11 days ago). Open action items from `brain/calls/2026-05-22-sam-curcio.md`. Not in nurture cadence queue — surface here as an open loop.
  Email: samuelcurcio@sydney.tworld.com (or scurcio@tworld.com)

## Warm Intro Opportunities (from target-discovery)

None — no target-discovery handoff processed today.

## Vault → Attio Syncs

- **Paul Giannamore** (The Potomac Company): Attio record already existed (id: `be8fbfdd-f122-46fc-9925-1b142490fd38`). Engagement note "LinkedIn DM sent - 2026-05-29" already attached (idempotency check passed — no duplicate created). Vault entity updated: `attio_id` + `attio_synced_at: 2026-06-02T07:00:00Z` written back.
- **Leigh Fryxell** (Pest-End): Vault entity marked "Logged to Attio" (2026-05-29) but no Attio record found across 1,500 records searched. No confirmed email in vault entity → cannot locate or create record. Will retry on next run when email is confirmed.
- **Bob Williamson** (business broker, entity created 2026-06-01): No email confirmed, no Attio record found. Skip — retry when email arrives.
- **carlos-in3o, erika-teresko, joe-vanore, amanda-forrestall**: No `## Relationship Notes` section → excluded from sync per detection criteria.

## Attio Dedup Needed

- **Austin Yoder**: 2 active records — `hello@cal.com` (id: `24aef54c`) and `austin@magratheapartners.com` (id: `2928b44c`). Real contact is Magratheapartners. Kay must merge: keep Magratheapartners record, retire Cal.com record.
- **Carlos Nieto**: 2 records — `carlosnietov@gmail.com` (id: `97e90c25`) and `carlos@in3o.com` (id: `12f84371`). Both Dormant per next_action notes. May be same person — Kay to confirm and merge or archive one.

## Metadata Drift

- **Donald Moore** (Marsh, id: `cb5ef7fb`): Attio next_action says "Nurture bi-annually." but `nurture_cadence` = Occasionally (213d threshold). He is at 217d — technically overdue by 4d. Next_action text implies intended cadence is bi-annual (~180d), which would make him MORE overdue. Recommend Kay confirm: update `nurture_cadence` to Monthly or accept Occasionally-but-past-due and take action.
- **Kristina Marcigliano** (WTW, id: `1afabadc`): No `nurture_cadence` set, but clearly on a Quarterly cadence based on relationship context. Recommend setting `nurture_cadence = Quarterly` in Attio.
- **thyme@everystall.com** (id: `53241063`): Attio record has no name, no job title, no next_action, Occasionally cadence, last interaction 2025-06-03 (364d ago). Unactionable without identity. Recommend Kay identify and either name the record or archive it.

## System Status Alerts

None — Attio REST API healthy (HTTP 200 on `/v2/self`). All 1,500 Attio person records queried successfully via op-resolved credentials.
