---
date: 2026-06-02
type: relationship-status
---

## Overdue Contacts (Top 5)

1. **[[entities/kristina-marcigliano|Kristina Marcigliano]]** (Willis Towers Watson) — Quarterly, last contact 2025-12-23, **161d (+63 over** 98d threshold). Women-priority. Carried unanswered from 2026-05-31 deferred list. No outbound in 21d. `nurture_cadence = Quarterly` is set in Attio (id `1afabadc`).
   Suggested action: short warm quarterly check-in (insurance SME).

2. **[[entities/hunter-hartwell|Hunter Hartwell]]** (Ellirock) — Quarterly, last contact 2026-01-14, **139d (+41 over)**. No next_action logged, no outbound in 21d.
   Suggested action: quarterly check-in email.

3. **[[entities/dan-tanzilli|Dan Tanzilli]]** — Monthly, last contact 2026-03-26, **68d (+33 over** 35d threshold). No next_action.
   Suggested action: catch-up note. NOTE: Monthly cadence is aggressive for this relationship — recommend confirming Monthly vs downgrade to Quarterly.

4. **[[entities/sarah-de-blasio|Sarah de Blasio]]** (Chartwell) — Quarterly, last contact 2026-01-23, **130d (+32 over)**. Women-priority; art-insurance brokerage SME. Carried from 2026-05-31 deferred. next_action carries a deal-trigger ("contact immediately when a deal surfaces" — GATED) PLUS standing "maintain quarterly touchpoint" — the quarterly maintenance touch is genuinely due.
   Suggested action: light quarterly check-in (no deal pretext needed).

5. **[[entities/kyle-mcgrath|Kyle McGrath]]** (Markel) — Quarterly, last contact 2026-02-10, **112d (+14 over)**. next_action "maintain quarterly touchpoint, no immediate action."
   Suggested action: low-priority quarterly touchpoint. Marginal (only 14d over).

**Also just over threshold (low priority):** Christopher Wise (Risk Strategies, Quarterly +6d), Austin Yoder/hello@cal.com (Quarterly +5d — duplicate/tool address, see Dedup).

*Verified-channel caveat: Gmail + calendar are the ONLY channels this skill verifies. Kay also reaches contacts by text, phone, and in person. Where Attio next_action records a recent non-email touch (e.g., Britta Nelson), that is trusted over Gmail silence.*

## Assistant vs Principal Routing
- **[[entities/molly-epstein|Molly Epstein]]** (Goodman Taft) via [[entities/chase-lacson|Chase Lacson]] assistant record (Monthly, 217d): next_action "Reconnection email sent to Molly 3/30, awaiting reply"; Molly's own record logs "3 follow-ups (Nov 2025), no response." This is a cold/dead thread, NOT a fresh nurture nudge. Not surfaced as actionable. Recommend Chase → Dormant.

## Excluded — Trigger-Gated (do NOT surface on elapsed time)
- [[entities/richard-augustyn|Richard Augustyn]] — "Reach out when insurance deal enters Active Deals pipeline."
- [[entities/michael-topol|Michael Topol]] — "Re-engage when we have an insurance deal for him to review."
- [[entities/rachele-adelman|Rachele Adelman]] — "When insurance DD needed, reach out to August Felker."
- [[entities/jim-vigna|Jim Vigna]] — "escalate when active deal financing comes into play."
- [[entities/scott-casper|Scott Casper]] / [[entities/eric-dreyer|Eric Dreyer]] — "Re-engage ~July 2026 if no new deals cross."
- [[entities/alexandra-kelly|Alexandra Kelly]] — "On maternity leave. Do not contact until she returns."
- [[entities/lauren-young|Lauren Young]] — "Re-engage when a specific introduction need arises."
- [[entities/anna-raginskaya|Anna Raginskaya]] — "Hold until late April 2026" (treat as gated; Dormant-class).

## Excluded — Recent Interaction via Non-Email Channel
- [[entities/britta-nelson|Britta Nelson]] — Quarterly, last email 189d ago BUT next_action records "Texted recently (late March 2026). No follow-up needed." Trusted per skill rule. NOT overdue.

## Auto-Resolved (No Action Needed)
- None this run. No outbound emails found in the 14-21d Gmail window for any surfaced candidate; nothing auto-resolved off the list.

## Pending Intros / Open Actions
- **[[entities/sam-transworld|Sam Curcio]]** (Transworld of NY): post-call thank-you + proof-of-funds letter still outstanding from the 2026-05-22 call (open items in `brain/calls/2026-05-22-sam-curcio.md`). Not a cadence item — surfaced here as an open loop. Email `samuelcurcio@sydney.tworld.com`. (Reactive: Kay handles intermediary replies; flag for her awareness.)
- No other promised intros outstanding — Kendall Warson → Amanda, Rachel Tepper → Zoe, Melissa Goldberg → Amanda all logged complete.

## Warm Intro Opportunities (from target-discovery)
- None — no target-discovery handoff processed today.

## Vault → Attio Syncs
- **[[entities/sam-transworld|Sam (Transworld) / Samuel Curcio]]** — file modified 2026-06-02 (Quick Facts full-name + email added per 5/31 recovered session); Relationship Notes content UNCHANGED since last sync (2026-05-27). No new engagement note to attach → no Attio note write performed. Already carries attio_id `cd3f4d27-2c1c-4936-837b-41102ab3e9fc`.
- **[[entities/leigh-fryxell|Leigh Fryxell]]** (Pest-End) — Attio Person + note already created 2026-05-29 (LinkedIn DM). No verified email in vault; nothing pending.
- **[[entities/bob-williamson|Bob Williamson]]** — no verified email, no attio_id; cannot match in Attio. Skip per spec, retry when email enriched.
- **[[entities/paul-giannamore|Paul Giannamore]]**, [[entities/eric-mendelsohn|Eric Mendelsohn]], [[entities/sarah-rowell|Sarah Rowell]], [[entities/marsha-weiner|Marsha Weiner]], [[entities/greg-pitkoff|Greg Pitkoff]] — already synced (synced_at >= modified). No action.

## Attio Dedup Needed
- **Austin Yoder**: 2 records — `hello@cal.com` (id `24aef54c`) and `austin@magratheapartners.com` (id `2928b44c`). Keep Magrathea, retire cal.com.
- **[[entities/carlos-in3o|Carlos Nieto]]**: `carlos@in3o.com` (id `12f84371`) vs `carlosnietov@gmail.com` (id `97e90c25`). Both Dormant — merge or archive one.

## Metadata Drift / Cleanup Candidates
- **Donald Moore** (Marsh): next_action "Nurture bi-annually" but nurture_cadence = Occasionally (213d); at 217d, marginally over. Confirm intended cadence.
- Role/system addresses carrying cadences (recommend → Dormant): bluerideradmin@morganstanley.com, hello@cal.com, chris.goyette@privateriskmanagement.org, Squarespace customercare@, Heritage do-not-reply@.
- **Chase Lacson** (assistant, dead Molly thread) → recommend Dormant.

## System Status Alerts
- None. Attio REST health-check returned HTTP 200 on `/v2/self` after op-env credential resolve. No outage. ~1,860 person records queried successfully.

## Suppressions Honored (already decided/deferred — not re-surfaced)
- DealsX cancellation (deferred ~Jun 11), JJ off Jul 1, DealsX off ~Aug 1 — per session-decisions-2026-06-02.
- Camilla approach codification → late June.
- All trigger-language next_action contacts (when/once/after/if) excluded per CLAUDE.md.
