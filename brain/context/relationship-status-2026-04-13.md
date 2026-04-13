---
schema_version: "1.0.0"
date: 2026-04-13
type: relationship-status
tags:
  - date/2026-04-13
  - relationship-status
  - topic/nurture-cadence
---

# Relationship Status — April 13, 2026 (Monday)

**Scope:** Queried 50 Attio People records with nurture_cadence set (3 Monthly, 19 Quarterly, 28 Occasionally). Cross-referenced against session-decisions Apr 10-12. Verified top candidates via 14-day Gmail check (from:kay.s@greenwichandbarrow.com).

**Channels verified:** Gmail + calendar only. Text, phone, and in-person interactions not captured — trust `next_action` field when it references recent contact.

## Overdue Contacts (Top 5)

1. **[[entities/michael-topol|Michael Topol]]** (MGT Insurance / AI insurance startup) — Quarterly, last contact 2025-12-08 (126 days overdue vs 98-day threshold). Attio `next_action`: "Quarterly touch-base due (last contact Nov 2025 meeting)." Insurance industry expert (Industry Expert tag), introduced by Luka Salamunic. No outbound from Kay in last 14 days.
   Suggested action: Short check-in email — "what are you seeing in insurance / how's the AI build going?" (~4 sentences). Not urgent, but cleanest overdue case in the nurture pool.

2. **[[entities/emily-schaffer|Emily Schaffer]]** (Risk Strategies, Fine Arts) — Quarterly, last contact 2025-11-06 (158 days overdue). Attio `next_action` says "No follow-up needed at this time" — but insurance thesis is live (per 4/10-4/12 decisions) and she's same-firm as [[entities/christopher-wise|Chris Wise]] (Good strength connection). Borderline: next_action suggests dormant, but thesis shift could justify warm re-engagement.
   Suggested action: Kay's call — either update `nurture_cadence` to Dormant if truly no value, OR send a 2-sentence art-insurance-thesis update email now that DealsX vertical SaaS is running parallel. Flagging for Kay's decision, not auto-surfacing as action.

(Only 2 genuinely overdue non-trigger non-admin contacts surfaced. See Suppressions below for why the rest didn't make it.)

## Auto-Resolved (No Action Needed)

- **[[entities/ashley-emerole|Ashley Emerole]]** (Saunders Street, Fellow Searcher, Monthly): coffee happened Apr 10 per session-decisions-2026-04-10.md ("Ashley Emerole coffee happened today — relationship-manager auto-resolves"). Last Attio-logged interaction (2026-02-19 email) is stale, but Kay confirmed in-person contact. Auto-resolved.
- **[[entities/dan-tanzilli|Dan Tanzilli]]** (Third Eye, Art World, Monthly): thank-you sent Apr 10 (per session-decisions-2026-04-10.md). Attio `next_action` was cleared same day. Last interaction 2026-03-26 — within threshold. Auto-resolved.
- **[[entities/britta-nelson|Britta Nelson]]** (David Zwirner, Art World, Quarterly): Attio `next_action` updated 2026-03-31: "Texted recently (late March 2026). No follow-up needed. Maintain quarterly nurture." Trusted per skill rule — text channel not verifiable via Gmail. Auto-resolved.
- **[[entities/stanley-rodos|Stanley Rodos]]** (Crate Capital, Fellow Searcher, Quarterly): last email 2026-03-17, quarterly coffee on calendar per next_action. Within threshold.
- **[[entities/austin-yoder|Austin Yoder]]** (Magrathea, Fellow Searcher, Quarterly): last email 2026-03-23. Within threshold.
- **[[entities/jeremy-black|Jeremy Black]]** (Jasper+Black, Fellow Searcher, Quarterly): last email 2026-03-10. Within threshold.
- **[[entities/nikki-higgins|Nikki Higgins]]** (Jet Aviation, Quarterly): last email 2026-03-12. Within threshold.
- **[[entities/kendall-warson|Kendall Warson]]** (Cohart, Quarterly): last email 2026-03-02. Thank-you already sent per next_action.

## Pending Intros

None currently outstanding. Scanned all 22 Monthly+Quarterly contacts for `next_action` containing "intro to" / "Connect X with Y" / "Send intro" — no open intros owed.

Historical note: Kendall Warson intro to [[entities/amanda-neilson|Amanda]] was completed (next_action: "Thank you sent, introduced to Amanda. No pending action.").

## Warm Intro Opportunities (from target-discovery)

None this cycle. Target-discovery did not hand off any targets requiring warm-path check today. Will re-evaluate on next target-discovery run (Active-Outreach niches).

---

## Suppressed / Not Surfaced (audit trail)

**Trigger-based contacts (skill rule — do NOT surface on elapsed time):**
- [[entities/richard-augustyn|Richard Augustyn]] (Endurance Search, Industry Expert): next_action = "Reach out when insurance deal enters Active Deals pipeline. Do not contact before then." Trigger = deal, not time.
- [[entities/rachele-adelman|Rachele Adelman]] (Oberle Risk Strategies, Administrative Assistant): next_action = "When insurance DD needed on a target, reach out to August Felker, cc Rachele." Trigger = DD need, not time. Also: assistant — skill rule says surface principal [[entities/august-felker|August Felker]], not Rachele.
- [[entities/sarah-de-blasio|Sarah de Blasio]] (Chartwell Insurance, Industry Expert): next_action = "SHORT LIST: Contact immediately when a deal of interest surfaces, especially art insurance brokerage." Trigger = deal surfacing. Within threshold anyway (last 2026-01-23).
- [[entities/chase-lacson|Chase Lacson]] (Goodman Taft, assistant, Monthly): next_action = "Reconnection email sent to Molly 3/30. Awaiting reply." Principal is [[entities/molly-epstein|Molly Epstein]]; in waiting state, not overdue.

**Weekend session decisions honored (do NOT surface):**
- [[entities/mark-gardella|Mark Gardella]] — DEFERRED Apr 11 to Kay's initiative.
- [[entities/philip-hoffman|Philip Hoffman]] — warm intro path DEFERRED.
- [[entities/andrew-freiman|Andrew Freiman]] — Monday send draft ready (outreach-manager owns, not relationship-manager).

**Low-signal records suppressed:**
- Carlos Nieto, Kristina Marcigliano, Hunter Hartwell, "bluerideradmin", Heritage Auctions (do-not-reply@), cal.com Austin Yoder duplicate, David Freeman, Colin Woolway — all Very Weak/Weak connection strength, no value_to_search, no next_action, no description, or auto-generated admin inboxes. Surfacing these is noise. Consider bulk-moving to Dormant.

**Data-hygiene flag for Kay:** 28 Occasionally and several Quarterly records have no `value_to_search`, no `next_action`, and Very Weak connection scores. Recommend a one-pass sweep to either (a) set `nurture_cadence` to Dormant or (b) populate `value_to_search`. Currently they inflate the queue without providing signal. Not blocking today's briefing.
