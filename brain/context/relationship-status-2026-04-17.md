---
schema_version: "1.0.0"
date: 2026-04-17
type: relationship-status
tags:
  - date/2026-04-17
  - relationship-status
  - topic/nurture-cadence
---

# Relationship Status — April 17, 2026 (Friday)

**Scope:** Queried Attio People with `nurture_cadence` set — 0 Weekly, 2 Monthly, 18 Quarterly, 28 Occasionally (Dormant excluded per skill rule). Cross-referenced [[brain/context/session-decisions-2026-04-16]] and [[brain/context/email-scan-results-2026-04-17]] for auto-resolves. Verified all candidates via 14-day Gmail outbound check from `kay.s@greenwichandbarrow.com` — no false positives.

**Channels verified:** Gmail + calendar only. Text, phone, and in-person not captured — trust `next_action` when it references recent contact.

**State changes since 4/15 briefing:**
- [[entities/ashley-emerole|Ashley Emerole]] `next_action` updated to "Met 2026-04-15; next touch Q3 (Jul 2026)" — auto-resolved per 4/15 in-person meet. No longer overdue.
- [[entities/katie-walker|Katie Walker]] relationship created 4/16 (Conwell mtg). Attio enrichment queue (relationship_type +Investor, cadence Occasionally, trigger-based next_action, value_to_search) still pending Kay's explicit AM confirm per session-decisions-2026-04-16.
- [[entities/lacey-wismer|Lacey Wismer]] — **NEVER surface** per Kay's hard rule (session-decisions-2026-04-16). Record stays as-is.

---

## Overdue Contacts (Top 5)

Only 3 genuinely overdue contacts this cycle after trigger/assistant/dormant filtering and 14-day outbound verification. The pool is thin because most Quarterly/Monthly contacts are within threshold or trigger-gated.

1. **[[entities/ashlee-walter|Ashlee Walter]]** (Chanel, Former Colleague) — Occasionally, last contact 2025-02-10 (431 days, **221 days overdue** vs 210-day threshold). `next_action`: "No immediate action. Occasional personal check-in." `value_to_search`: potential warm path to luxury/Chanel contacts. No outbound in 14d.
   Suggested action: Short personal check-in email, 2-3 sentences. Low-stakes, warmth-maintenance note referencing Chanel days. No ask.

2. **[[entities/robert-dimartini|Robert DiMartini]]** (Chanel, Former Colleague) — Occasionally, last contact 2025-06-03 (318 days, **108 days overdue**). `next_action`: "Occasional coffee when schedules align. Don't expect quick email responses." Head of fashion architecture at Chanel. No outbound in 14d.
   Suggested action: Personal check-in text preferred over email given his response pattern (Kay's text channel not verified here). If emailing, keep it one-liner: "How's life, miss you, coffee when you surface?" Set low expectation for reply.

3. **[[entities/david-wolkoff|David Wolkoff]]** (Former Colleague) — Occasionally, **no last_interaction on record**. `next_action`: "Personal relationship, not search-related. Maintain warmth." Former manager and mentor. Email not on record in Attio.
   Suggested action: Kay's call on channel (text/phone/LinkedIn more likely than email given no email on Attio). If she wants to surface this, a personal "thinking of you" note via her preferred channel. Flag: record needs email enrichment if this is a live relationship.

(Slots 4 and 5 intentionally empty — no additional contacts meet threshold. See Suppressions for audit trail.)

---

## Auto-Resolved (No Action Needed)

- [[entities/ashley-emerole|Ashley Emerole]] — met 2026-04-15 (Wednesday), `next_action` reads "Met 2026-04-15; next touch Q3 (Jul 2026)". Prior overdue surface (4/15) cleared. No action this cycle.
- [[entities/katie-walker|Katie Walker]] — met in person 2026-04-16 (Conwell mtg). Thank-you email pinned for 4/17 drafting in [[brain/context/tomorrow-pins-2026-04-17]]. Handled by pipeline-manager briefing Section 3, not surfaced here as overdue.
- [[entities/rachel-tepper|Rachel Tepper]] — Zoe intro completed 2026-04-01, she replied 4/02. Loop closed.
- [[entities/kendall-warson|Kendall Warson]] — Amanda intro completed. `next_action` cleared.
- [[entities/melissa-goldberg|Melissa Goldberg]] — Kendall + Amanda connections made. `next_action` cleared.
- [[entities/melissa-rosenblatt|Melissa Rosenblatt]] — email interaction 2026-04-08, within threshold. BK Growth investor channel.

---

## Pending Intros

**None outstanding.** Scanned all 48 Monthly+Quarterly+Occasionally records for `next_action` containing "intro to" / "Connect X with Y" / "Send intro" / "Introduce". All prior intro commitments (Rachel→Zoe, Melissa→Kendall→Amanda, Lauren Young deal flow) are either completed or trigger-gated on specific need.

---

## Warm Intro Opportunities (from target-discovery)

**None this cycle.** No target-discovery handoff today requiring warm-path check. Friday's three review skills (weekly-tracker, health-monitor, calibration-workflow) do not generate new targets. Will re-evaluate on next target-discovery run for Active-Outreach niches.

---

## Suppressed / Not Surfaced (audit trail)

**Trigger-based contacts (do NOT surface on elapsed time — trigger language in `next_action`):**
- [[entities/michael-topol|Michael Topol]] (MGT/AI insurance) — "Re-engage when we have an insurance deal... Trigger: deal flow only, not elapsed time."
- [[entities/richard-augustyn|Richard Augustyn]] (Endurance Search) — "Reach out when insurance deal enters Active Deals pipeline. Do not contact before then."
- [[entities/sarah-de-blasio|Sarah de Blasio]] (Chartwell) — "SHORT LIST: Contact immediately when a deal of interest surfaces." Within quarterly threshold anyway (84d).
- [[entities/rachele-adelman|Rachele Adelman]] (Oberle Risk, **assistant**) — "When insurance DD needed, reach out to August Felker, cc Rachele." Principal = [[entities/august-felker|August Felker]].
- [[entities/chase-lacson|Chase Lacson]] (Goodman Taft, **assistant**) — "Reconnection email sent to Molly 3/30. Awaiting reply." Principal = [[entities/molly-epstein|Molly Epstein]], in waiting state (below).
- [[entities/molly-epstein|Molly Epstein]] — "Reconnection draft sent March 30, 2026. Awaiting response." Waiting on her reply, not Kay's move.
- [[entities/lauren-young|Lauren Young]] (USV) — "Re-engage when a specific introduction need arises." Trigger-based.
- [[entities/alexandra-kelly|Alexandra Kelly]] (UOVO) — "On maternity leave. Do not contact until she returns." Hard suppression.

**Hard-rule suppression (Kay's explicit rule):**
- [[entities/lacey-wismer|Lacey Wismer]] — NEVER surface per [[brain/context/session-decisions-2026-04-16]].

**Within cadence threshold (not overdue):**
- [[entities/dan-tanzilli|Dan Tanzilli]] (2026-03-26, 22d — Monthly threshold 35d)
- [[entities/kendall-warson|Kendall Warson]] (2026-03-02, 46d — Quarterly threshold 98d; next_action cleared)
- [[entities/stanley-rodos|Stanley Rodos]] (2026-03-17, 31d — coffee on calendar)
- [[entities/austin-yoder|Austin Yoder]] — Magrathea (2026-03-23, 25d)
- [[entities/jeremy-black|Jeremy Black]] (2026-03-10, 38d)
- [[entities/nikki-higgins|Nikki Higgins]] (2026-03-12, 36d)
- [[entities/britta-nelson|Britta Nelson]] (texted late March per next_action, trusted)
- [[entities/christopher-wise|Christopher Wise]] (2026-02-18, 58d)
- [[entities/kyle-mcgrath|Kyle McGrath]] (Markel Fine Art, 2026-02-10, 66d)
- [[entities/harrison-wells|Harrison Wells]] (2026-03-26, 22d)
- [[entities/colin-woolway|Colin Woolway]] (2026-02-17, 59d; same-office peer)
- [[entities/will-gallagher|Will Gallagher]] (2025-12-12, 126d — Occasionally threshold 210d)
- [[entities/bettina-huang|Bettina Huang]] (2026-02-09, 67d)
- [[entities/donald-moore@marsh|Donald Moore]] (2025-10-28, 171d; family-friend, bi-annual cadence per next_action)
- [[entities/lauren-della-monica|Lauren Della Monica]] (2025-10-10, 189d)
- [[entities/sarah-findlay|Sarah Findlay]] (2026-01-27, 80d)
- [[entities/anton-bogdanov|Anton Bogdanov]] (2026-01-13, 94d)
- [[entities/caroline-fall|Caroline Fall]] (Marriott, 2026-02-23, 53d)

**Low-signal records suppressed (no `next_action`, no `value_to_search`, Very Weak connection, or admin/auto-generated inboxes):**
- Kristina Marcigliano (WTW), Hunter Hartwell (Ellirock), Carlos Nieto (In3o, 2 records), bluerideradmin@morganstanley.com, Heritage Auctions do-not-reply@, cal.com Austin Yoder duplicate, Ashley Emerole @naset.org duplicate, chris.goyette@privateriskmanagement.org, Squarespace customercare, thyme@everystall.com, Kanayo Oweazim (Chase), Rick Hiebert (Wondeur), Michelle Perr (UBS, no interaction), David Freeman (Breakpoint Growth), Zoe Wen, Harrison Wells (dodo digital).

**Data-hygiene flag for Kay (carried forward from 4/13 and 4/15, still open):** 28 Occasionally + several Quarterly records have no `value_to_search`, no `next_action`, Very Weak connection. Recommend one-pass sweep to either set `nurture_cadence` = Dormant or populate `value_to_search`. Currently inflating queue without providing signal. Suggest adding this to next idle-window sweep.

---

## Attio Writes Queued (NOT executed — awaiting Kay's approval)

Per skill rules, relationship-manager does NOT auto-write cadence / relationship_type / next_action updates. The following are queued for Kay's AM review:

1. [[entities/katie-walker|Katie Walker]] — relationship_type (+Investor), nurture_cadence (Occasionally), next_action (trigger-based: "Re-engage when G&B reaches LOI on a vertical SaaS deal — Datacor precedent"), value_to_search enrichment. **Pending explicit AM confirm** per session-decisions-2026-04-16.
2. [[entities/ashley-emerole|Ashley Emerole]] — no write needed; `next_action` already reflects 4/15 meet and Q3 next touch.

No other queued writes this cycle.
