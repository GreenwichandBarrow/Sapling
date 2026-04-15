---
schema_version: "1.0.0"
date: 2026-04-15
type: relationship-status
tags:
  - date/2026-04-15
  - relationship-status
  - topic/nurture-cadence
---

# Relationship Status — April 15, 2026 (Wednesday)

**Scope:** Queried Attio People with `nurture_cadence` set — 3 Monthly, 18 Quarterly, 28 Occasionally. Cross-referenced `session-decisions-2026-04-14.md` (thesis/architecture session, no outbound — no new auto-resolves from yesterday). Verified candidates via 14-day Gmail outbound check from `kay.s@greenwichandbarrow.com`.

**Channels verified:** Gmail + calendar only. Text, phone, and in-person not captured — trust `next_action` when it references recent contact.

**State changes since 4/13 briefing:**
- [[entities/michael-topol|Michael Topol]] `next_action` updated to explicit trigger: "Re-engage when we have an insurance deal for him to review. Trigger: deal flow only, not elapsed time." → now suppressed as trigger-based (was #1 overdue on 4/13).
- [[entities/emily-schaffer|Emily Schaffer]] `nurture_cadence` moved to **Dormant** on 4/13 → never surface per skill rule.

## Overdue Contacts (Top 5)

1. **[[entities/ashley-emerole|Ashley Emerole]]** (Saunders Street Capital, Fellow Searcher) — Monthly, last contact 2026-02-19 (55 days, 25 days overdue vs 30-day threshold). Attio `next_action`: "Reschedule coffee (cancelled Mar 5 due to sick kid). Circle back to set new date." No outbound from Kay in last 14 days. Active deal-sharing relationship per `value_to_search` (Education Co, E-Learning flow).
   Suggested action: Short email — "Got knocked off the calendar after the kid sickness — want to grab that coffee, next 2 weeks?" 2-3 sentences, propose concrete slots. Cleanest overdue in the pool.

(Only 1 genuinely overdue non-trigger, non-admin, non-dormant contact this cycle. See Suppressions for why.)

## Auto-Resolved (No Action Needed)

- No new auto-resolves this cycle. Kay's 4/14 session was thesis/architecture — no outbound to relationship-pool contacts. Prior resolves ([[entities/ashley-emerole|Ashley]] coffee Apr 10, [[entities/dan-tanzilli|Dan Tanzilli]] thank-you Apr 10, [[entities/britta-nelson|Britta Nelson]] text late March, etc.) still hold. Ashley is re-surfacing above because the 4/10 coffee was the earlier meeting — current `next_action` references the reschedule.

## Pending Intros

None outstanding. Scanned all 21 Monthly+Quarterly contacts for `next_action` containing "intro to" / "Connect X with Y" / "Send intro" — none open.

## Warm Intro Opportunities (from target-discovery)

None this cycle. No target-discovery handoff today requiring warm-path check. Will re-evaluate on next target-discovery run for Active-Outreach niches.

---

## Suppressed / Not Surfaced (audit trail)

**Trigger-based contacts (do NOT surface on elapsed time):**
- [[entities/michael-topol|Michael Topol]] (MGT/AI insurance) — next_action: "Re-engage when we have an insurance deal... Trigger: deal flow only, not elapsed time." NEW trigger language since 4/13.
- [[entities/richard-augustyn|Richard Augustyn]] (Endurance Search) — "Reach out when insurance deal enters Active Deals pipeline."
- [[entities/rachele-adelman|Rachele Adelman]] (Oberle Risk, assistant) — "When insurance DD needed, reach out to August Felker, cc Rachele." Principal = [[entities/august-felker|August Felker]].
- [[entities/sarah-de-blasio|Sarah de Blasio]] (Chartwell) — "SHORT LIST: Contact immediately when a deal of interest surfaces." Within quarterly threshold anyway (last 2026-01-23, 82d).
- [[entities/chase-lacson|Chase Lacson]] (Goodman Taft, assistant) — "Reconnection email sent to Molly 3/30. Awaiting reply." Principal = [[entities/molly-epstein|Molly Epstein]], in waiting state.

**Dormant (never surface):**
- [[entities/emily-schaffer|Emily Schaffer]] (Risk Strategies, Fine Arts) — moved to Dormant 2026-04-13. Prior "borderline" surface from 4/13 is now closed.

**Within cadence threshold:**
- [[entities/dan-tanzilli|Dan Tanzilli]] (2026-03-26, 20d — Monthly threshold 30d)
- [[entities/stanley-rodos|Stanley Rodos]] (2026-03-17, coffee on calendar)
- [[entities/austin-yoder|Austin Yoder]] (2026-03-23)
- [[entities/jeremy-black|Jeremy Black]] (2026-03-10)
- [[entities/nikki-higgins|Nikki Higgins]] (2026-03-12)
- [[entities/kendall-warson|Kendall Warson]] (2026-03-02, next_action cleared)
- [[entities/christopher-wise|Christopher Wise]] (2026-02-18, 56d — Quarterly threshold 98d)
- [[entities/kyle-mcgrath|Kyle McGrath]] (Markel Fine Art, 2026-02-10, 64d)
- [[entities/britta-nelson|Britta Nelson]] (texted late March per next_action, trusted)

**Low-signal records suppressed (no `next_action`, no `value_to_search`, Very Weak/Weak connection, or admin/auto-generated inboxes):**
- Kristina Marcigliano (WTW), Hunter Hartwell (Ellirock), Carlos Nieto (In3o), bluerideradmin@morganstanley.com, Heritage Auctions do-not-reply@, cal.com Austin Yoder duplicate, Caroline Fall (Marriott), David Freeman, Colin Woolway.

**Data-hygiene flag for Kay (carried from 4/13, still open):** 28 Occasionally + several Quarterly records have no `value_to_search`, no `next_action`, Very Weak connection. Recommend one-pass sweep to either set `nurture_cadence` = Dormant or populate `value_to_search`. Currently inflating queue without providing signal.
