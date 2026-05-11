---
date: 2026-05-11
type: relationship-status
---

## Overdue Contacts (Top 5)

Monday morning run (first weekday relationship-manager fire after the 5/8–5/10 server-cutover weekend). Gmail outbound check: `gog gmail search "in:sent from:kay.s@greenwichandbarrow.com newer_than:3d" --max 30` returned only the Harrison Wells thread (already an auto-resolve). No new substantive Kay-outbound to surface-affected contacts since the 2026-05-10 artifact. After applying suppression rules (action-already-taken / trigger-based / explicit PASS / within-cadence-commitment-drift / assistant-vs-principal), two contacts remain surfaceable — both carry-forwards:

1. **Lauren Young** ([[entities/lauren-young]] — Union Square Ventures, Friend/Personal, Occasionally cadence) — last interaction 2025-06-10 (Gmail thread "Slow to respond Re: Hi there!", `lauren@usv.com`). **335 days overdue against the 213-day Occasionally threshold (122 days past).** `next_action` reads "Re-engage when a specific introduction need arises" — contains soft trigger language; prior runs ruled this Friday-surface-with-light-check-in rather than excluding her as trigger-based.
   **Status: intent-approved, draft creation unverified.** Per `session-decisions-2026-05-10.md` Item 5: Kay APPROVE'd the check-in draft for Monday AM send ("Lauren Young check-in draft for Monday AM send. Kay handled server-side; verification of actual draft creation outstanding"). Gmail probes this morning (`to:lauren@usv.com newer_than:1d in:sent` and `in:drafts to:lauren@usv.com`) returned zero threads — neither sent nor visible as draft via `gog gmail search`. Two possibilities: (a) draft created in Gmail UI but not indexed by gog drafts query, (b) the open-loop on draft creation never actually closed. Surfacing here as awareness, NOT as a new draft request — the action is intent-approved. Pipeline-manager should verify the draft exists in Gmail before Kay's AM send window closes.
   Suggested action: **none new — verify the existing draft and send.** Do not regenerate.

2. **Sarah de Blasio** ([[entities/sarah-de-blasio]] — Chartwell, Industry Expert, Quarterly cadence) — last interaction 2026-01-23 (Gmail "Happy New Year" sent by Kay, `sdeblasio@chartwellins.com`). **108 days overdue against the 98-day Quarterly threshold (10 days past).** Carry-forward awareness from 2026-05-05.
   Suggested action: **outreach BLOCKED** pending the Goodwin finder's-fee doc on G&B letterhead. Once the doc lands, drafting moves to outreach-manager. Surface only as awareness today — do not draft.

Caveat: Gmail and calendar are the only verified channels in this run. Texts, phone calls, and in-person interactions are not captured. If Kay has touched either contact via SMS or phone in the last quarter, treat as resolved.

## Auto-Resolved (No Action Needed)

Carry-forward from 2026-05-10 — all still within 14-day Gmail-verification window or within threshold. Ages incremented by +1 day (Sun → Mon):

- **Andrew Lowis** ([[entities/andrew-lowis]] — Axial, Quarterly) — last interaction 2026-05-06 (Axial 12pm meeting + thread "Nice meeting you at XPX yesterday"). 5 days. Within Quarterly threshold. Open follow-ups (Axial member-application, panel deck digital copy) tracked in pipeline-manager open-loops.
- **Guillermo Lavergne** ([[entities/guillermo-lavergne]] — Investor, Weekly) — last interaction 2026-05-06 (biweekly call). 5 days. Within Weekly threshold. Next interaction confirmed 2026-05-20 on Attio.
- **Jim Vigna** ([[entities/jim-vigna]] — Live Oak Bank, Quarterly) — Gmail thread "Follow Up" reply 2026-04-27. 14 days. Coffee/lunch open per Apr 24 reply. Within Quarterly threshold; rolls off the 14-day verification window tomorrow.
- **Nikki Higgins** ([[entities/nikki-higgins]] — Jet Aviation, Quarterly) — last interaction 2026-04-22. 19 days. Within Quarterly threshold (98 days).
- **James Emden** ([[entities/james-emden]] — Helmsley Spear, Occasionally) — Gmail thread "RE: Meeting You Yesterday" active 2026-05-07 (9 messages). 4 days. Filter add executed 2026-05-10 (label `auto/personal & network`).
- **Harrison Wells** ([[entities/harrison-wells]] — Dodo Digital, Occasionally) — Gmail threads "Server setup guide + Tailscale" (9 msgs, last 2026-05-10 12:48) and "[Action Required] Engagement Scope + Invoice" (4 msgs, 2026-05-07) actively running. 1 day. **DRAFTED 2026-05-10 for Monday AM ~9am ET send** per `session-decisions-2026-05-10.md` line 135. Gmail probe this morning shows no send yet — expected; relationship-manager fires 7am, Harrison send window is 9am.
- **Stanley Rodos** ([[entities/stanley-rodos]] — Crate Capital, Quarterly) — last interaction 2026-03-17. 55 days. Within Quarterly threshold. Per `feedback_within_cadence_commitment_drift`: aged commitment text in `next_action` does not justify surfacing inside cadence window. Suppressed.
- **Britta Nelson** ([[entities/britta-nelson]] — Quarterly, Art World) — Gmail-silent since 2025-12-16 but `next_action` documents "Texted recently (late March 2026). No follow-up needed." Per SKILL.md, recent text-channel evidence in `next_action` overrides Gmail silence. Suppressed.
- **Ali Doswell** ([[entities/ali-doswell]] — Potomac View Partners, Quarterly) — Gmail thread "Just wanted to say thank you" 2026-04-30. 11 days. Within Quarterly threshold.

## Trigger-Based Contacts (Excluded from Overdue Logic)

Contacts whose `next_action` text contains trigger language ("when", "if", "once", "until") — correctly excluded from cadence surfacing today:

- **Richard Augustyn** (Endurance Search, Quarterly) — "Reach out when insurance deal enters Active Deals pipeline."
- **Michael Topol** (MGT Insurance, Quarterly) — "Re-engage when we have an insurance deal for him to review. Trigger: deal flow only, not elapsed time."
- **Rachele Adelman** (Oberle Risk, Quarterly) — "When insurance DD needed on a target, reach out to August Felker, cc Rachele."
- **Alexandra Kelly** (UOVO, Occasionally) — "On maternity leave. Do not contact until she returns."
- **Scott Casper** (EQA, Quarterly) and **Eric Dreyer** (EQA, Quarterly) — "Re-engage ~July 2026 if no new deals cross."

## PASS-Suppressed Contacts (Session Decision Log)

Per `session-decisions-2026-05-01.md` Friday nurture cluster — Kay PASS'd these and they remain suppressed until further notice:

- **Kristina Marcigliano** (WTW, Quarterly) — would otherwise be 140 days overdue.
- **Hunter Hartwell** (Ellirock, Quarterly) — would otherwise be 117 days overdue.
- **Dan Tanzilli** (Third Eye, Monthly) — would otherwise be 46 days overdue.

Per `feedback_lauren_della_monica_dead_end.md` and `session-decisions-2026-05-06.md`:
- **Lauren Della Monica** — confirmed dead end. Never surface.
- **Eric Carter** (Cohort Peak) — Dormant suppression stub. Spam-tier marked.

Per assistant-vs-principal rule (SKILL.md):
- **Chase Lacson** (Goodman Taft, Monthly) — assistant. Would be 195 days overdue against Monthly. Suppressed in favor of principal **Molly Epstein** (Occasionally cadence, last interaction 2026-03-31, 41 days — within Occasionally threshold). Net: nothing surfaced.

Per `session-decisions-2026-05-08.md` / `-2026-05-09.md` / `-2026-05-10.md`:
- No new PASS/REJECT decisions on cadence contacts across the three-day window. Sessions were dominated by server-cutover + 1Password migration + Magic DNS + KeyReach inventory updates — no contact-cadence overrides issued.
- Two DEFER items from `session-decisions-2026-05-09.md` (Allison Allen PWIPM reply; Taft/KeyBank Thu dinner pick) are pipeline-manager / decisions-bucket items today, not relationship-manager cadence surfaces. Noted for cross-reference; not surfaced here.

## Pending Intros

None outstanding this morning. Last cycle's intros all closed (Rachel Tepper → Zoe Wen 2026-04-01; Melissa Goldberg → Kendall → Amanda 2026-02-03 era). Andrew Lowis's offered intro to Arturo (Axial founder) remains gated on Kay submitting the Axial member-application form post-call — pipeline-manager owns that open loop, not relationship-manager.

## Warm Intro Opportunities (from target-discovery)

None this morning — no target-discovery handoff has landed yet today. Monday morning workflow may trigger target-discovery for Active-Outreach niches that need refill; if so, warm-intro paths will surface on the next run, not this artifact.

## Vault → Attio Syncs

Sweep covered all `brain/entities/*.md` files modified on/after 2026-05-04 (156 files in the 7-day window) where `type: person` AND has `## Relationship Notes` AND `attio_id` is missing/empty. **No new entity activity since the 2026-05-10 artifact** — same 14 net-new candidate universe carries forward from yesterday: kevin-hong, mark-gardella, august-felker, megan-lawlor, clayton-sachs, katie-walker, adilene-dominguez, tom-jackson, sarah-rowell, ali-potomac-view, jake-stoller, ali-doswell, hunter-hartwell, christine-kobel.

**Net syncs executed this run: 0.** Status update from yesterday: the Attio API auth path is now resolved (token migrated to 1Password via `op inject`; direct curl `GET /v2/objects` returns **200** this morning), so the underlying credential gap that blocked yesterday's sync is closed. However, the `mcp__attio__*` MCP tool inventory is still empty in this server-side session (no `mcp__attio__search_records` / `mcp__attio__create_note` surfaced via ToolSearch), and the SKILL.md sync flow is written against the MCP path. Executing the sync via raw HTTP curls would be a meaningful re-implementation of multi-step idempotent note-attachment logic outside this skill's tested code path — deferred to a session where MCP is connected (or a follow-up bead to re-implement against raw API). All 14 candidates remain queued. Idempotency guard (note-title check) will hold when sync resumes.

## Attio Dedup Needed

None detected — no Attio reads attempted via MCP this run. Direct API is live but full People-list enumeration was not run (out of scope for headless 7am fire; dedup detection is a sweep-level concern, best handled on a host with MCP connected).

## System Status Alerts

- **Attio API auth — RESOLVED today.** Yesterday's 401 condition is cleared. The 1Password migration (`session-decisions-2026-05-09.md` Items 7–10) is fully landed: server-side `op inject` resolves `op://GB Server/Attio API Key/password` cleanly to a 64-char live key; direct `curl -s -o /dev/null -w "%{http_code}\n" -H "Authorization: Bearer $LIVE" https://api.attio.com/v2/objects` returns 200 this morning. Credential leak risk during verification was zero (value-suppressing curl pattern per CLAUDE.md). Backup copies of the SA token live at `~/.config/op-sa-token.env` (chmod 600) and in 1Password `GB Server` vault.
- **Attio MCP server-side still not connected** (carry-forward). `mcp__attio__*` tool inventory remains empty in this session. The MCP layer is what the SKILL.md sync flow targets; raw API is live but writes (note attachments) require MCP-side scope handling. Carry-forward gap: the Attio MCP needs to come up on this server before the queued 14 vault→Attio note-attachment syncs can execute through the documented path.
- **Granola MCP server-side auth unresolved** (carry-forward from `session-decisions-2026-05-08.md`). Localhost-callback OAuth flow incompatible with headless Linux VPS. Not blocking relationship-manager (this skill does not depend on Granola).
- **Gmail outbound 3-day window confirmed** via `gog gmail` — no new substantive Kay-outbound between 2026-05-10 morning and 2026-05-11 morning. All auto-resolves carry forward at +1 day age. Harrison Wells thread still active (9 messages, last 5/10 12:48); Lauren Young + Sarah de Blasio + Andrew Lowis Gmail-silent in this window.
- **Lauren Young draft visibility gap.** `session-decisions-2026-05-10.md` records APPROVE on a Monday-AM check-in draft, but Gmail `in:drafts to:lauren@usv.com` returns zero threads this morning. Could be a gog-search-drafts indexing quirk or the open-loop on draft creation never closed. Surface to pipeline-manager so Kay confirms the draft is in her Gmail compose surface before the AM send window.
- **Wrapper validator path fixed in-session.** Discovered during self-run: `scripts/validate_relationship_manager_integrity.py` had `VAULT_DIR` hardcoded to the iMac path `/Users/kaycschneider/Documents/AI Operations/brain/context`. On server-side fires (every weekday since the 2026-05-09/10 cutover), the POST_RUN_CHECK has been tripping "VALIDATOR FAILED" on healthy artifacts because the path doesn't exist on Linux. Patched to derive VAULT_DIR relative to the script directory (with `RELATIONSHIP_MANAGER_VAULT_DIR` env override). Validator now PASSES against today's artifact. Per `feedback_ship_compounding_fixes_now.md`: fix shipped same session before next weekday fire (Tue 7am).
- **Broader server-migration validator-path gap (Kay triage).** `grep /Users/kaycschneider scripts/` returns **15 files**, including 4 other validators (`validate_weekly_tracker_integrity.py`, `validate_deal_aggregator_integrity.py`, `validate_niche_intelligence_integrity.py`, plus `generate_systemd_units.py`). All have the same iMac-only path baked in. Surfacing for follow-up since fixing them all in this headless run exceeds the relationship-manager scope. Recommended decision-bucket item: **RECOMMEND: Sweep all 15 scripts to use repo-relative paths in one pass** — small, low-risk, eliminates a class of phantom Slack alerts.
- **Known Attio API limitation (no regression):** `nurture_cadence is_set` and `is_not_empty` select-attribute filters on Attio People still return 400 (Attio MCP filter limitation). Per-cadence-value workaround documented. Not exercised today.
- No new system-level alerts beyond the above.

## Metadata Drift

Carry-forward from 2026-05-10 — no new metadata events. Same set of soft-asks:

- **Eric Carter vault stub** — Recommend adding `attio_id: SUPPRESSED` sentinel to `brain/entities/eric-carter.md` to remove from daily sweep noise. Soft ask; carry-forward from 2026-05-07.
- **Bill (Sales Captain)** — Surname missing in vault frontmatter. No Attio match possible until captured.
- **Mike Hollywell** — Email field still empty per 2026-04-30 entity. No Attio match possible until captured.
- **Mark Wilcox** — No email in vault frontmatter despite call held 2026-04-24. If Kay has the email, capturing it would unblock the next sweep.
- **Kristin Wihera** — No email in vault frontmatter despite the WSN/Pacific-Lake context. Same gap as Mark Wilcox.
- **Denning (Lawyer)** — Surname + email both missing. Lowest priority of the metadata gaps.
- No active drift between `nurture_cadence` field and `next_action` text on currently-tracked contacts (Lauren Della Monica precedent stays clean).
