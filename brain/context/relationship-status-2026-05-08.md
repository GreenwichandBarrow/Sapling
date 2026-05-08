---
date: 2026-05-08
type: relationship-status
---

## Overdue Contacts (Top 5)

Friday full sweep ran (per `feedback_relationship_cadence_friday_only`). Cadence universe enumerated via per-value workaround (Weekly/Monthly/Quarterly/Occasionally — `is_set`/`is_not_empty` filter on the select attribute still returns 400). Threshold dates as of 2026-05-08: Weekly < 2026-04-28, Monthly < 2026-04-03, Quarterly < 2026-01-30, Occasionally < 2025-10-07.

After suppression rules (action-already-taken / trigger-based / explicit PASS / within-cadence-commitment-drift / assistant-vs-principal), only two contacts remain surfaceable, both carry-forwards from 2026-05-05 → 2026-05-07 awareness logs that are now formally on this Friday's list:

1. **Lauren Young** (Union Square Ventures, Friend/Personal, Occasionally cadence) — last interaction 2025-06-10, **332 days overdue against the 213-day threshold (119 days past).** `next_action` field reads "Re-engage when a specific introduction need arises" which contains soft trigger language, but yesterday's artifact (5/07) and 5/05's run both flagged her as Friday-surface-with-light-check-in rather than excluding her as trigger-based. Holding that interpretation.
   Suggested action: light check-in email, no ask. Reference shared NYC orbit, send a "thinking of you, hope you're well" note. Friend/Personal — avoid forcing a search-fund frame.

2. **Sarah de Blasio** (Chartwell, Industry Expert, Quarterly cadence) — last interaction 2026-01-23, **105 days overdue against the 98-day threshold (7 days past).** Carry-forward awareness from 2026-05-05.
   Suggested action: **outreach BLOCKED** pending the Goodwin finder's-fee doc on G&B letterhead. Once the doc lands, drafting moves to outreach-manager. Surface only as awareness — do not draft today.

Caveat: Gmail and calendar are the only verified channels. Texts, phone calls, and in-person interactions are not captured. If Kay has touched either contact via SMS or phone in the last quarter, treat as resolved.

## Auto-Resolved (No Action Needed)

- **Andrew Lowis** (Axial, Quarterly) — last interaction 2026-05-06 (call held). Closed loop. Open follow-ups (Axial member-application, panel deck digital copy) tracked in pipeline-manager open-loops, not relationship-manager.
- **Guillermo Lavergne** (Investor, Weekly) — last interaction 2026-05-06 (biweekly call). Within Weekly threshold (2 days). Next interaction confirmed 2026-05-20 on Attio. No action.
- **Jim Vigna** (Live Oak Bank, Quarterly) — Gmail confirms reply on thread 2026-04-27 ("Follow Up"). Coffee/lunch open per his Apr 24 reply. Within Quarterly threshold. No action.
- **Nikki Higgins** (Jet Aviation, Quarterly) — last interaction 2026-04-22 (16 days). Within threshold. No action.
- **James Emden** (Helmsley Spear, Occasionally) — last interaction 2026-05-08 (active thread, RE: Meeting You Yesterday). No action.
- **Harrison Wells** (Dodo Digital, Occasionally) — last interaction 2026-05-08 (server setup + invoice threads active). No action.
- **Stanley Rodos** (Crate Capital, Quarterly) — last interaction 2026-03-17 (52 days). Within threshold. Per `feedback_within_cadence_commitment_drift` (SKILL.md): aged commitment text in `next_action` does not justify surfacing inside cadence window. Suppressed.
- **Britta Nelson** (Quarterly, Art World) — Gmail-silent since 2025-12-16, but `next_action` notes "Texted recently (late March 2026). No follow-up needed." Per SKILL.md, recent text-channel evidence in `next_action` overrides Gmail silence. Suppressed.

## Trigger-Based Contacts (Excluded from Overdue Logic)

These contacts have `next_action` text containing trigger language ("when", "if", "once", "until") and remain correctly excluded from cadence surfacing:

- **Richard Augustyn** (Endurance Search, Quarterly) — "Reach out when insurance deal enters Active Deals pipeline."
- **Michael Topol** (MGT Insurance, Quarterly) — "Re-engage when we have an insurance deal for him to review. Trigger: deal flow only, not elapsed time."
- **Rachele Adelman** (Oberle Risk, Quarterly) — "When insurance DD needed on a target, reach out to August Felker, cc Rachele."
- **Alexandra Kelly** (UOVO, Occasionally) — "On maternity leave. Do not contact until she returns."
- **Scott Casper** (EQA, Quarterly) and **Eric Dreyer** (EQA, Quarterly) — "Re-engage ~July 2026 if no new deals cross."

## PASS-Suppressed Contacts (Session Decision Log)

Per `session-decisions-2026-05-01.md` Friday nurture cluster — Kay PASS'd these and they remain suppressed:

- **Kristina Marcigliano** (WTW, Quarterly) — would otherwise be 137 days overdue.
- **Hunter Hartwell** (Ellirock, Quarterly) — would otherwise be 114 days overdue.
- **Dan Tanzilli** (Third Eye, Monthly) — would otherwise be 43 days overdue.

Per `feedback_lauren_della_monica_dead_end.md` and `session-decisions-2026-05-06.md`:
- **Lauren Della Monica** — confirmed dead end. Never surface.
- **Eric Carter** (Cohort Peak) — Dormant suppression stub. Spam-tier marked.

Per assistant-vs-principal rule (SKILL.md):
- **Chase Lacson** (Goodman Taft, Monthly) — assistant. Would be 192 days overdue against Monthly. Suppressed in favor of principal **Molly Epstein** (Occasionally cadence, last interaction 2026-03-31, 38 days — well within Occasionally threshold). Net: nothing surfaced.

## Pending Intros

None outstanding this morning. Last cycle's intros all closed (Rachel Tepper → Zoe Wen 2026-04-01; Melissa Goldberg → Kendall → Amanda 2026-02-03 era). Andrew Lowis's offered intro to Arturo (Axial founder) remains gated on Kay submitting the Axial member-application form post-call — pipeline-manager will surface if it stays open. Not a relationship-manager-owned intro.

## Warm Intro Opportunities (from target-discovery)

None this morning — no target-discovery handoff received yet. The 7-per-day intermediary outreach roster is owned by outreach-manager Subagent 3, not target-discovery.

## Vault → Attio Syncs

Sweep covered all `brain/entities/*.md` files modified in last 7 days where `type: person` AND has `## Relationship Notes` AND (`attio_id` empty OR `attio_synced_at` older than file mtime). Today's previously-unsynced person entities, with verified Attio-search results:

- **Eric Carter** (`brain/entities/eric-carter.md`) — Vault-only Dormant suppression stub. Body explicitly notes "No Attio record; vault-only stub for suppression bookkeeping." Carry-forward — recommend setting a sentinel value (`attio_id: SUPPRESSED`) on this stub to permanently exclude from sweep noise. (See Metadata Drift.)
- **Bill (Sales Captain)** (`brain/entities/bill-sales-captain.md`) — Webinar-only. Surname not captured, no email field. Cannot search Attio meaningfully. Will retry when contact info surfaces.
- **Mike Hollywell** (`brain/entities/mike-hollywell.md`) — Webinar-only. Email field still empty. Will retry when email surfaces or Attio person auto-creates on first send/receive.
- **Mark Wilcox** (`brain/entities/mark-wilcox.md`) — Confirmed via Attio search today: no Mark Wilcox record exists yet (search returned only "Mark Aiston" + 2 unrelated). Frontmatter has no email. Will auto-create when first Gmail interaction lands.
- **Kristin Wihera** (`brain/entities/kristin-wihera.md`) — Confirmed via Attio search today: no Kristin Wihera record (only "Kristina Marcigliano" + others). No email in frontmatter. Will retry when contact info surfaces.
- **Filippe Chagas** (`brain/entities/filippe-chagas.md`) — Confirmed via Attio search today: zero matches. Email field is `info@standardpestcontrol.com` (role-based, owner-monitored) — would be a generic/role match, not a personal record. Cold owner outreach pre-engagement; auto-creates on first send/receive.
- **Denning (Lawyer)** (`brain/entities/denning-lawyer.md`) — Surname not captured, no email field. Cannot search Attio meaningfully. Will retry when contact info surfaces.

Guillermo Lavergne (`attio_id: 2b613b57-537c-4cef-8fc5-e053b51d7a98`) and the other already-synced entities (Ian Stuart, Nikki Higgins, Peter Shakalis, Andrew Lowis, Jim Vigna, James Emden) were not re-swept (idempotency guard via `attio_synced_at >= file mtime`).

Net: zero new syncs this run. All seven unsynced person-entities skipped per detection criteria. No failures to escalate.

## Attio Dedup Needed

None detected.

## System Status Alerts

- Attio MCP `aaa-health-check`: `ok: true` (`production`, timestamp 2026-05-08T13:46:42Z). `needs_api_key: true` flag is informational, not a failure — workspace ID still resolves and per-record reads/queries succeed.
- **Known issue (no regression):** `nurture_cadence is_set` and `is_not_empty` filters on Attio People still return 400 (select-attribute filter limitation in Attio's MCP layer). Per-cadence-value workaround (querying each of Weekly/Monthly/Quarterly/Occasionally separately) applied successfully. Total runtime acceptable; not a perf concern.
- Quarterly + Occasionally search results exceeded MCP token-cap; spilled to side-files and parsed via jq for the summary table. Mechanism worked — all records accounted for.
- Gmail outbound 14-day window confirmed action-already-taken for Andrew Lowis, Guillermo Lavergne, Jim Vigna, James Emden, Harrison Wells (all auto-resolved).
- No new system-level alerts.

## Metadata Drift

- **Eric Carter vault stub** — Recommend adding `attio_id: SUPPRESSED` sentinel to `brain/entities/eric-carter.md` to remove from daily Vault → Attio sweep. Soft ask; carry-forward from 2026-05-07.
- **Bill (Sales Captain)** — Surname missing in vault frontmatter. Until captured, no Attio match possible.
- **Mike Hollywell** — Email field still empty per 2026-04-30 entity. Until captured, no Attio match possible.
- **Mark Wilcox** — No email in vault frontmatter despite call held 2026-04-24. If Kay has the email, capturing it would unblock the next sweep.
- **Kristin Wihera** — No email in vault frontmatter despite the WSN/Pacific-Lake context. Same gap as Mark Wilcox.
- **Denning (Lawyer)** — Surname + email both missing. Lowest priority of the metadata gaps.
- No active drift between `nurture_cadence` field and `next_action` text on currently-tracked contacts (Lauren Della Monica precedent stays clean).
