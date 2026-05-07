---
date: 2026-05-06
type: relationship-status
---

## Overdue Contacts (Top 5)

None — Friday-only surfacing rule. Today is Wednesday. Per `feedback_relationship_cadence_friday_only`, routine cadence overdue contacts are not surfaced Mon-Thu briefings. Cadence threshold checks (Cadence field = sole source of truth) and trigger-based exclusions still ran in the background; full overdue list will surface in Friday's run if still applicable.

Carry-forward awareness from 2026-05-05's run (do NOT re-surface as briefing items, captured here for Friday continuity):
- **Lauren Young** (Union Square Ventures, Friend/Personal, Occasionally cadence) — 116 days past 213-day threshold. Light check-in (no ask).
- **Sarah de Blasio** (Chartwell, Quarterly cadence, 4 days past 98-day threshold) — Outreach BLOCKED pending Goodwin finder's fee doc on G&B letterhead. Awareness only.

Caveat: Gmail and calendar are the only verified channels. Texts/phone calls not captured — if Kay has touched any contact via SMS or phone, treat as resolved.

## Auto-Resolved (No Action Needed)

- **Eric Carter close-the-loop reply** — Per `session-decisions-2026-05-05.md`, deferred to today AM pending Kay's review of the thread (was hidden behind `[Superhuman]/AI/Respond` Gmail label + `CATEGORY_PERSONAL`). Direct thread URL was provided yesterday. Decision-on-draft owned by pipeline-manager today, not relationship-manager.
- **Guillermo Lavergne reschedule pick** — Two time options proposed yesterday (Tue 5/12 1:30 PM ET / Wed 5/13 10 AM ET). Awaiting Kay's pick before draft. Owned by pipeline-manager today.
- **Andrew Lowis (Axial) reschedule** — Gmail draft `r-7216983259268091776` already created 2026-05-05 asking to push 10:00 → 10:30. Kay reviews + sends manually per `feedback_kay_handles_all_replies`. Not relationship-manager territory.
- **Kristina Marcigliano** (WTW), **Hunter Hartwell** (Ellirock), **Dan Tanzilli** (Third Eye) — PASS verbs in `session-decisions-2026-05-01.md` Friday nurture cluster. Suppressed.
- **Chase Lacson** (Goodman Taft, assistant) — Suppressed in favor of principal Molly Epstein per assistant-vs-principal rule. Molly within Occasionally cadence (last interaction 2026-03-31).
- **Lauren Della Monica** — Confirmed Dormant per `feedback_lauren_della_monica_dead_end.md`. Never surface.

## Trigger-Based Contacts (Excluded from Overdue Logic)

These contacts have `next_action` text containing trigger language ("when", "if", "once") and remain correctly excluded:

- **Richard Augustyn** (Endurance Search) — "Reach out when insurance deal enters Active Deals pipeline."
- **Michael Topol** (MGT Insurance) — "Re-engage when we have an insurance deal for him to review."
- **Rachele Adelman** (Oberle Risk, assistant) — "When insurance DD needed, reach out to August Felker, cc Rachele."
- **Alexandra Kelly** (UOVO) — "On maternity leave. Do not contact until she returns."
- **Scott Casper** (EQA), **Eric Dreyer** (EQA) — "Re-engage ~July 2026 if no new deals cross."

## Pending Intros

None outstanding this morning. Last cycle's intros all closed (Rachel Tepper → Zoe Wen 2026-04-01; Melissa Goldberg → Kendall → Amanda).

## Warm Intro Opportunities (from target-discovery)

None this morning — no target-discovery handoff received yet for today's run. Today's roster build (5+5 broker outreach roster) is deferred per session-decisions-2026-05-05.md and routes through outreach-manager, not target-discovery.

## Vault → Attio Syncs

- **Guillermo Lavergne** (`glavergne@ashfordventures.com`) — Attio person record found (ID `2b613b57-537c-4cef-8fc5-e053b51d7a98`). Engagement note attached: "Vault 2026-05-06 — engagement context" (note ID `d08cdcf1-b0a8-4f61-948c-dfd29a8738d0`). Set 4 empty Attio attributes from vault: `relationship_type=Investor Contact`, `nurture_cadence=Weekly`, `how_introduced="Largest investor in G&B search fund (committed via initial capital raise)"`, `value_to_search="Bi-weekly strategic counsel + capacity letter for broker-channel positioning + named-deal connector (introduced Austin Yoder, advises against carve-outs)"`. Vault frontmatter updated with `attio_id` + `attio_synced_at: 2026-05-06T10:34:30Z`.
- **Mike Hollywell** (Hollywell, prospect) — Vault entity has `## Relationship Notes` section but NO email field captured (entity at `brain/entities/mike-hollywell.md` modified 2026-05-01). Attio person record does not exist yet under "Mike Hollywell" search. Skipped — will retry when email surfaces or when Attio person auto-creates on next email send/receive. Not a failure; expected behavior per skill detection criteria.

Sweep covered all `brain/entities/*.md` modified in last 7 days where `type: person` AND has `## Relationship Notes` AND `attio_id` is empty. Two candidates total; one synced, one deferred for missing email.

## Attio Dedup Needed

None detected.

## System Status Alerts

- Attio MCP `aaa-health-check`: `ok: true` (`production`).
- Note from yesterday's perf log (`session-decisions-2026-05-05.md`): scheduled fire ran 3h22m due to `is_not_empty` filter on `nurture_cadence` returning 400. Per-cadence-value workaround applied. Watch next Tuesday's runtime — if still 3+ hours, treat as perf regression to chase.
- Eric Carter Gmail label issue from 2026-05-05 (thread hidden behind `[Superhuman]/AI/Respond` + `CATEGORY_PERSONAL`) is a one-off legacy-label artifact, not a system alert. Resolved by direct URL handoff.

## Metadata Drift

- **Sarah de Blasio**: cadence Quarterly, `next_action` says "Maintain quarterly touchpoint" — aligned, not drifted.
- **Britta Nelson**: cadence Quarterly, `next_action` references texted-recently (late March 2026). Trust next_action over Gmail silence per skill doctrine. No action needed.
- **Guillermo Lavergne** (post-sync): `nurture_cadence` set to **Weekly** (matches bi-weekly call cadence + One Hanover ad-hoc visits, conservative-frequent default for largest-investor relationship). If Kay prefers Bi-weekly as a literal cadence label or Quarterly as a strategic-reset default, adjust manually.
