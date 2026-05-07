---
date: 2026-05-07
type: relationship-status
---

## Overdue Contacts (Top 5)

None — Friday-only surfacing rule. Today is Thursday. Per `feedback_relationship_cadence_friday_only`, routine cadence overdue contacts are not surfaced in Mon-Thu briefings. Cadence threshold checks (cadence field = sole source of truth) and trigger-based exclusions still ran in the background; full overdue list surfaces in tomorrow's Friday run if still applicable.

Carry-forward awareness from 2026-05-05 → 2026-05-06 runs (do NOT re-surface as briefing items, captured here for Friday continuity):
- **Lauren Young** (Union Square Ventures, Friend/Personal, Occasionally cadence) — was 116 days past 213-day threshold on 5/05. Light check-in (no ask) when surfaced Friday.
- **Sarah de Blasio** (Chartwell, Quarterly cadence, was 4 days past 98-day threshold on 5/05) — outreach BLOCKED pending Goodwin finder's-fee doc on G&B letterhead. Awareness only.

Caveat: Gmail and calendar are the only verified channels. Texts/phone calls not captured — if Kay has touched any contact via SMS or phone, treat as resolved.

## Auto-Resolved (No Action Needed)

- **Andrew Lowis (Axial) reschedule** — Gmail draft `r-7216983259268091776` was SENT yesterday per `session-decisions-2026-05-06.md` (push 10:00 → 10:30 ET). Today's call already on calendar. Closed loop.
- **Guillermo Lavergne biweekly call** — Held yesterday (5/06). Brief landed (vault + Drive). Open follow-ups (Axial reaction, lender cadence) tracked in pipeline-manager open-loops, not relationship-manager.
- **Eric Carter** — Confirmed Dormant suppression stub created 5/06. Spam-tier marked. Never surface.
- **Lauren Della Monica** — Confirmed Dormant per `feedback_lauren_della_monica_dead_end.md`. Never surface.
- **Kristina Marcigliano** (WTW), **Hunter Hartwell** (Ellirock), **Dan Tanzilli** (Third Eye) — PASS verbs in `session-decisions-2026-05-01.md` Friday nurture cluster. Suppressed.
- **Chase Lacson** (Goodman Taft, assistant) — Suppressed in favor of principal Molly Epstein per assistant-vs-principal rule.

## Trigger-Based Contacts (Excluded from Overdue Logic)

These contacts have `next_action` text containing trigger language ("when", "if", "once") and remain correctly excluded from cadence surfacing:

- **Richard Augustyn** (Endurance Search) — "Reach out when insurance deal enters Active Deals pipeline."
- **Michael Topol** (MGT Insurance) — "Re-engage when we have an insurance deal for him to review."
- **Rachele Adelman** (Oberle Risk, assistant) — "When insurance DD needed, reach out to August Felker, cc Rachele."
- **Alexandra Kelly** (UOVO) — "On maternity leave. Do not contact until she returns."
- **Scott Casper** (EQA), **Eric Dreyer** (EQA) — "Re-engage ~July 2026 if no new deals cross."

## Pending Intros

None outstanding this morning. Last cycle's intros all closed (Rachel Tepper → Zoe Wen 2026-04-01; Melissa Goldberg → Kendall → Amanda).

Awareness: Andrew Lowis offered to introduce Arturo (Axial founder) — gated on Kay submitting Axial member-application form post-call. Status uncertain per `session-decisions-2026-05-06.md` open loops. Pipeline-manager will surface if it remains open. Not a relationship-manager-owned intro.

## Warm Intro Opportunities (from target-discovery)

None this morning — no target-discovery handoff received yet for today's run. The 7-per-day intermediary outreach roster is owned by outreach-manager Subagent 3 (intermediary outreach), not target-discovery.

## Vault → Attio Syncs

Sweep covered all `brain/entities/*.md` modified in last 7 days where `type: person` AND has `## Relationship Notes` AND `attio_id` is empty. Three candidates surfaced; all three skipped this run (none failures — all expected per skill detection criteria):

- **Eric Carter** (`brain/entities/eric-carter.md`) — Vault-only Dormant suppression stub created 2026-05-06. Body explicitly notes "No Attio record; vault-only stub for suppression bookkeeping." Skipped permanently — recommend setting a sentinel value (`attio_id: SUPPRESSED`) on this stub to remove it from sweep noise. Will surface as a metadata-cleanup ask in Friday's run.
- **Bill (Sales Captain)** (`brain/entities/bill-sales-captain.md`) — Webinar-only contact. No surname captured, no email field. Cannot search Attio meaningfully. Will retry when contact info surfaces.
- **Mike Hollywell** (`brain/entities/mike-hollywell.md`) — Webinar-only contact. Email field still empty ("(none yet — first contact via webinar)"). Will retry when email surfaces or Attio person auto-creates on first send/receive. Same status as 2026-05-06 sweep.

Guillermo Lavergne already synced 2026-05-06 (`attio_id: 2b613b57-537c-4cef-8fc5-e053b51d7a98`); not re-swept (idempotency guard via `attio_synced_at >= file mtime`).

## Attio Dedup Needed

None detected.

## System Status Alerts

- Attio MCP `aaa-health-check`: `ok: true` (`production`, timestamp `2026-05-07T12:02:43Z`).
- **Known issue:** `nurture_cadence is_not_empty` filter on Attio People returns 400. Per-cadence-value workaround (querying each of Weekly/Monthly/Quarterly/Occasionally separately) was applied in 5/05's run. Today's run did not enumerate the full cadence universe (Friday-only rule means routine surfacing is suppressed Mon-Thu) — workaround status is unchanged. Watch tomorrow's Friday run for runtime; if still 3+ hours, treat as perf regression to chase.
- No new system-level alerts this run.

## Metadata Drift

- **Eric Carter vault stub** — Recommend adding `attio_id: SUPPRESSED` sentinel to remove from daily sweep. (Soft ask; surfaces in Friday's full run.)
- **Bill (Sales Captain)** — Surname missing in vault frontmatter. Until captured, no Attio match possible.
- **Mike Hollywell** — Email field still empty per 2026-04-30 entity. Until captured, no Attio match possible.
- No active drift between cadence field and `next_action` text on currently-tracked contacts.
