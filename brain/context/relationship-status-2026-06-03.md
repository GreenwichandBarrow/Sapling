---
date: 2026-06-03
type: relationship-status
---

## Overdue Contacts (Top 5)

1. **[[entities/kristina-marcigliano|Kristina Marcigliano]]** (Willis Towers Watson) — Quarterly, last contact 2025-12-23, **162d (+64 over** 98d threshold). Women-priority. Carried from 2026-06-02 (no action taken). No outbound in 14d Gmail check.
   Suggested action: short warm quarterly check-in (insurance SME).

2. **[[entities/hunter-hartwell|Hunter Hartwell]]** (Ellirock) — Quarterly, last contact 2026-01-14, **140d (+42 over)**. No next_action, no outbound in 14d. Carried from 2026-06-02.
   Suggested action: quarterly check-in email.

3. **[[entities/dan-tanzilli|Dan Tanzilli]]** — Monthly, last contact 2026-03-26, **69d (+34 over** 35d threshold). No next_action, no outbound in 14d. Carried from 2026-06-02. Monthly cadence may be aggressive for this relationship.
   Suggested action: catch-up note — confirm Monthly vs downgrade to Quarterly.

4. **[[entities/sarah-de-blasio|Sarah de Blasio]]** (Chartwell) — Quarterly, last contact 2026-01-23, **131d (+33 over)**. Women-priority; art-insurance brokerage SME. next_action carries a deal-trigger ("contact immediately when a deal surfaces") PLUS standing "maintain quarterly touchpoint" — quarterly maintenance touch is due regardless of deal status. No outbound in 14d.
   Suggested action: light quarterly check-in (no deal pretext needed).

5. **[[entities/kyle-mcgrath|Kyle McGrath]]** (Markel) — Quarterly, last contact 2026-02-10, **113d (+15 over)**. next_action "maintain quarterly touchpoint, no immediate action." No outbound in 14d.
   Suggested action: low-priority quarterly touchpoint.

**Also just over threshold:** Christopher Wise (Risk Strategies, Quarterly +6d), Chris Goyette (Private Risk Mgmt, Occasionally +5d — likely system/role address, see Cleanup Candidates), Donald Moore (Marsh, Occasionally +4d — metadata drift, see below).

*Verified-channel caveat: Gmail + calendar are the ONLY channels this skill verifies. Kay also reaches contacts by text, phone, and in person. Where Attio next_action records a recent non-email touch, that is trusted over Gmail silence.*

## Auto-Resolved (No Action Needed)

None this run. No outbound emails found in the 14-day Gmail window for any surfaced candidate.

## Pending Intros / Open Actions

- **[[entities/sam-transworld|Sam Curcio]]** (Transworld of NY): post-call thank-you + proof-of-funds letter still outstanding from the 2026-05-22 call (open items in `brain/calls/2026-05-22-sam-curcio.md`). Carried from 2026-06-02. No outbound to samuelcurcio@sydney.tworld.com in 14d. (Reactive: Kay handles intermediary replies; flagged for awareness.)
- No other promised intros outstanding — Kendall Warson → Amanda, Rachel Tepper → Zoe, Melissa Goldberg → Amanda all logged complete.

## Warm Intro Opportunities (from target-discovery)

None — no target-discovery handoff processed today.

## Vault → Attio Syncs

- **[[entities/leigh-fryxell|Leigh Fryxell]]** (Pest-End) — type=person, no attio_id, has Relationship Notes. Attio name search returned 0 records (no email on file to match). Cannot sync. Skip — retry when email enriched via Apollo or captured from LinkedIn reply.
- **[[entities/bob-williamson|Bob Williamson]]** — type=person, no attio_id, no verified email on file. Cannot match in Attio. Skip per spec; retry when email enriched post-2026-06-01 intro call.
- **[[entities/paul-giannamore|Paul Giannamore]]**, **[[entities/sarah-rowell|Sarah Rowell]]**, **[[entities/marsha-weiner|Marsha Weiner]]**, **[[entities/greg-pitkoff|Greg Pitkoff]]** — already synced (synced_at ≥ last modified). No action.
- carlos-in3o.md, erika-teresko.md, amanda-forrestall.md, joe-vanore.md, ever-kerr.md — no Relationship Notes section. Not sync candidates.

## Attio Dedup Needed

- **Austin Yoder**: 2 records — `hello@cal.com` (id `24aef54c`, Quarterly) is a Cal.com scheduling-service address, not a personal email. `austin@magratheapartners.com` (id `2928b44c`, Quarterly, Fellow Searcher, last interaction 2026-03-23) is the real record. Keep Magrathea, retire/merge cal.com. Carried from 2026-06-02.

## Metadata Drift / Cleanup Candidates

- **Donald Moore** (Marsh): next_action "Nurture bi-annually" but nurture_cadence = Occasionally (213d threshold). At 217d he is marginally over. Cadence field is sole source of truth — surfaced as borderline overdue. If intent is truly bi-annual, upgrade cadence to a custom description or adjust to match. Confirm intended cadence.
- **System/role addresses still carrying active cadences** (recommend → Dormant): bluerideradmin@morganstanley.com (Quarterly), Squarespace customercare@squarespace.com (Occasionally), thyme@everystall.com (Occasionally, no name attached, single interaction 2026-06-03 — appears to be an auto-detected inbound).
- **Chase Lacson** (mee_admin@goodmantaft.com, Monthly): admin at Goodman Taft. Molly Epstein's own Attio record (molly.epstein@gmail.com, Occasionally) shows last interaction 2026-03-31 and is within cadence. Chase Lacson's Monthly cadence record is dead/redundant — recommend → Dormant. Carried from 2026-06-02.
- **Chris Goyette** (chris.goyette@privateriskmanagement.org, Occasionally): no name populated, role/admin address. At +5d over Occasionally threshold. Verify whether this is a personal contact or a role mailbox before surfacing.

## Excluded — Trigger-Gated (do NOT surface on elapsed time)

- [[entities/richard-augustyn|Richard Augustyn]] — "Reach out when insurance deal enters Active Deals pipeline."
- [[entities/michael-topol|Michael Topol]] — "Re-engage when we have an insurance deal for him to review."
- [[entities/rachele-adelman|Rachele Adelman]] — "When insurance DD needed, reach out to August Felker."
- [[entities/jim-vigna|Jim Vigna]] — "Escalate when active deal financing comes into play."
- [[entities/scott-casper|Scott Casper]] / [[entities/eric-dreyer|Eric Dreyer]] — "Re-engage ~July 2026 if no new deals cross."
- [[entities/alexandra-kelly|Alexandra Kelly]] — "On maternity leave. Do not contact until she returns."
- [[entities/lauren-young|Lauren Young]] — "Re-engage when a specific introduction need arises."

## Excluded — Recent Interaction via Non-Email Channel

- [[entities/britta-nelson|Britta Nelson]] — Quarterly, last email 169d ago but next_action: "Texted recently (late March 2026). No follow-up needed." Trusted per skill rule.
- [[entities/molly-epstein|Molly Epstein]] — Occasionally cadence, Attio last_interaction 2026-03-31 (63d), well within 213d threshold. Not overdue. Outstanding reconnection email awaiting reply — no action until she responds.

## System Status Alerts

None. Attio REST health-check returned HTTP 200 on `/v2/self` after op-env credential resolve. 1,860 person records queried (full paginated sweep, 49 contacts with active cadences identified).
