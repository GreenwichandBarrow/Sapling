---
name: jj-operations
description: "Cold-call operations: weekly call-tab creation, Slack delivery, and post-shift outcome harvesting. Legacy file name remains jj-operations until Phase 3 cleanup."
archetype: router
context_budget:
  skill_md: 200
  max_references: 12
  learnings_md: 40
  sub_agent_limit: 500
user_invocable: true
---

<objective>
Manage cold-call operations end-to-end. The current operator works Mon-Fri 10am-2pm ET. This skill handles:
1. Sunday prep: create the full week's 5 Call Log tabs (Mon-Fri, 40 targets each) from the clean target-discovery pool
2. Monday 10am Slack delivery: week's sheet link + call guide
3. Daily harvest (Mon-Fri after 2pm): read each day's Call Log tab, update Full Target List

The cold-call operator works from the daily Call Log tab on the master target sheet and Slack messages. They use a single generic **G&B Cold Call Guide** (Google Doc ID `12Hqfwxg4qJA3YdZh36ndd-flvYgWN`) that applies across niches — scripts, objections, and universal context. Do NOT search for per-niche call guides; the guide is intentionally generic.

## Codex-era role

This skill still adds value as the **call execution operations layer**:
- Own: weekly tab creation from target-discovery's pool, DealsX universe exclusion, Do Not Call exclusion, Slack logistics, call outcome harvesting, owner-name backfill, and dashboard freshness via the snapshot jobs.
- Consume: target-discovery's `brain/context/jj-week-pool-{YYYY-MM-DD}.md` artifact (legacy filename), target sheets, Do Not Call tabs, and DealsX universe sheets.
- Avoid duplicating: sourcing/enrichment strategy, email drafting/sending, Attio stage movement, and deal screening.
- Preserve legacy technical identifiers (`jj-operations`, `JJ_CALL_NICHES`, `jj-week-pool-*`) until Phase 3 cleanup because scheduled jobs and validators depend on them.

<credentials>
## Credentials (read first)

**1Password is the first rung — always.** Before any op://-backed CLI (this skill uses `gog sheets`/`gog drive` + `$SLACK_WEBHOOK_SVA`):
```bash
source /home/ubuntu/projects/Sapling/scripts/op-env.sh
```
Exports `GOG_KEYRING_PASSWORD`, `SLACK_WEBHOOK_SVA`. **NEVER `source scripts/.env.launchd` raw** — hook-blocked; see `feedback_op_env_before_op_backed_cli`.

If `${#SLACK_WEBHOOK_SVA}` = 0 after sourcing, surface to Kay — 1Password resolve broken. Do NOT skip the 10am SVA delivery on a phantom "Slack unavailable" — confirm the var is actually empty first.

**Sheet header resolution contract (mandatory):** Never hardcode Google Sheet column letters, column numbers, or fixed table ranges as business logic. Resolve every field by header name at runtime using `scripts/col-lookup.py` or an equivalent header-map read, then use the resolved cell/range only for that execution. If a required header cannot be resolved, stop that branch and log the missing header.

**Email safety contract:** This skill does not send emails and does not create Gmail drafts. If a call outcome needs an email follow-up, route that to outreach-manager as draft-only work. Kay alone sends emails.
</credentials>

**Two run modes:**
- `prep` — Sunday 6pm, creates 5 Call Log tabs (Mon-Fri) for the full week. Runs AFTER target-discovery's Sunday 3pm pipeline (owner enrichment → PE re-screen → warm intro check) has cleaned the pool artifact.
- `harvest` — Mon-Fri after 2pm, reads that day's Call Log tab and updates the Full Target List

**Weekly cadence:**
- Sunday 3pm: target-discovery Phase 2 pipeline runs (select pool → enrich → PE screen → warm intro check)
- Sunday 6pm: cold-call operations `prep` creates 5 tabs from clean pool
- Monday 10am: Slack to the cold-call operator with week's sheet link
- Mon-Fri 4pm: cold-call operations `harvest` reads each day's results
- Monday morning: previous week's tabs archived (hidden, not deleted)

**This skill does NOT:**
- Create outreach drafts (that's outreach-manager)
- Decide which targets get approved (that's target-discovery auto-approve)
- Manage the target list sheet (that's target-discovery)
- Move Attio pipeline stages (that's pipeline-manager)
</objective>

<call_prep>
## Mode: Prep (Before 10am ET)

### 1. Target Selection

**Cold-call operations is decoupled from email outreach cadences (Kay Email and DealsX Email channels).** The call list is managed independently, not triggered by email send events. Targets come from target-discovery's clean weekly pool.

Read the active niche sprint's master sheet ("{Niche} - Target List"). Select targets where:
- The first-call date/status headers indicate the target has not been called yet
- Target's niche has `Outreach Channel` = `Cold-Call-Only` or legacy `JJ-Call-Only` on WEEKLY REVIEW (see Channel Filter below)

### Two-Tier Target Selection (Calls-First)

Calls-first niches load 500-1000 targets via Phase 1 volume load. Not all will have owner names yet (owner enrichment happens weekly in Phase 2). The operator handles both tiers:

**Tier 1 (enriched):** `Owner Name` is populated. The operator asks the gatekeeper for the owner by name: "Is {Owner Name} available?" Higher conversion.

**Tier 2 (raw):** `Owner Name` is blank. The operator uses generic opener: "May I speak with the owner or person in charge?" Lower conversion but still valuable. The operator can extract the owner's name from the call for future attempts.

**Daily target selection priority:**
1. Fill from Tier 1 first (up to 40)
2. If Tier 1 has fewer than 40 available, backfill from Tier 2
3. Always prefer Tier 1

**Owner name backfill:** If the operator learns the owner's name during a call (gatekeeper tells them, voicemail greeting, owner introduces themselves), capture it in Call Notes. Harvest mode writes it to `Owner Name` — free enrichment from the call itself.

### Channel Filter (CRITICAL)

**Why this exists:** Cold-call operations is decoupled from email outreach cadences (Kay Email and DealsX Email). Calling a target who's in an active email sequence creates conflicting touchpoints.

Before building the call list, read the WEEKLY REVIEW tab to determine which niches route to cold-call operations. Resolve `Niche`, `Status`, and `Outreach Channel` by header name; do not use fixed ranges.

Build a map of **niche name → outreach channel**. Then for each target sheet:
- Match the sheet's niche to the WEEKLY REVIEW map
- **Include** targets only if their niche's outreach channel = `Cold-Call-Only` or legacy `JJ-Call-Only`
- **Skip** targets if their niche's outreach channel = `Kay Email`, `DealsX Email`, or any other value
- **HARD STOP:** If a niche is missing from WEEKLY REVIEW, do NOT add ANY targets from that niche to the call list. Flag in morning briefing as requiring manual review. This is a safety gate — unknown channel means unknown routing.

This filter runs BEFORE the reply check — no point checking replies for targets the operator won't call.

### DealsX Universe Cross-Reference (CRITICAL — HARD doctrine 2026-05-26)

Even within a cold-call niche, individual companies on the Full Target List can be touched by DealsX cold email (Sam's team manages the DealsX universe externally — overlap happens). Per `memory/feedback_outreach_channel_universes_separate.md`: **outreach target universes must remain separate across all channels.** No company may appear on both a cold-call Call Log tab and the DealsX target universe.

**Cross-reference at every tab build:**

```bash
# DealsX universe source — Drive Verticals sheet
DEALSX_SHEET="1VaviHqaJT9Wtm6X1h9B6Q8aOrA8adTiBvt851pkEUFg"
# Pest-relevant tabs (extend as new niches activate DealsX):
# - 'Specialty Pest & ENV Service (Good Fit) Valid'  (~55 contacts, `Company Name` header)
# - 'Specialty Pest& ENV Service(Probable Fit) Valid' (~575 contacts)
# Combined unique normalized companies ~950 (lowercase + suffix-stripped)
```

- **Match logic:** lowercase, strip Inc/LLC/Corp/Co/Ltd/Services, collapse punctuation. Strict-on-match — `Pest Management Services Inc` ≠ `Pest Management Inc`. If uncertain, KEEP and log.
- **Removal pattern:** when a match is found, DELETE the row from the Call Log tab. Do NOT annotate-and-keep — that was the OLD pattern, retired 2026-05-26.
- **Ordering:** the cross-reference fires BEFORE Apollo enrichment is spent on the row. Apollo credits cost money; eliminate first, then enrich the survivors. Per Kay 2026-05-26: *"enRich through Apollo, not before you eliminate those ones."*
- **Snapshot before delete:** `brain/context/rollback-snapshots/jj-dealsx-dedup-{ISO timestamp}.json`.
- **Tab-floor flag:** if dedup drops a daily Call Log tab below 20 rows, surface to Kay; do NOT auto-backfill from other lanes (could reintroduce overlap).
- **Audit precedent:** 2026-05-26 retro-cleanup removed 43 rows total across Tue/Wed/Thu/Fri 5/24-30 tabs. Going forward this fires at build time, not as a cleanup pass. See `headless-sunday-prep-prompt.md` Step 6 for the prep-mode mechanic.

**Sheet IDs (all target lists):**
- Art Insurance: `15M76-gpcklwc47HDXIwyFC9Tj8K4wDOor4i0uxCYyHQ`
- Domestic TCI: `1lEAx-3pEshsSc0Rix4KunJ38mzHahjAmV6nQA_cuwLw`
- IPLC: `1Cdw6yb8-yBQtx5mTB8Hu4rENkJfpmt3t7HZdGqtdylQ`
- Art Storage: `1PDprJ_gApm7T_kzpNWlWk7qItQ11M95ssL9_UD5sE9g`
- Art Advisory: `1c6Db21D2qDpiT7LnEQ4l0AROlA-gucDQD1ZGOlrZ-K0`
- Premium Pest Management: `1Y0ZjEkc2LHhBoO4QGO8Ny9MvG90NpojQn8bloKA291I`

**Master sheet headers — schema migrated 2026-04-23:**
Resolve these by header at runtime: `Source`, `Company`, `Website`, `Headquarters`, `Industry`, `Employees`, `Rev Source`, `Revenue`, `Year Founded`, `Ownership`, `Owner Name`, `Owner Title`, `Email`, `Phone Company`, `Phone Owner`, `LinkedIn Connection`, `LinkedIn Owner`, `LinkedIn Company`, `Agent Notes`, legacy cold-call date/status/notes/sentiment headers.

**Two-attempt rule (added 2026-04-23 after status overwrite discovery):**
The operator logs first-attempt date/status. If the target doesn't answer, the operator calls back later and logs second-attempt date/status. After 2 unsuccessful attempts (No Answer / Voicemail twice), the target moves to Do Not Pursue rather than continuing to dial. Notes and Sentiment reflect the most recent call.

**Pace measurement rule (added 2026-04-23, reinforced 2026-04-24 after weekly-tracker miscount):** Daily dial count is computed by counting populated first-call and second-call date field values where the value = today's date, ACROSS ALL Call Log tabs AND the Full Target List. Tab name (e.g., "Call Log 4.20.26") is only the *estimated* call date when the row was assigned — the operator rolls through tabs as a working list, not a daily-strict bucket. **Never measure pace by tab name — always measure by the Call Date field values.** See `memory/feedback_jj_call_date_from_field_not_tab.md`.

**Date-format normalizer (added 2026-04-24):** The operator may use inconsistent date formats in the Call Date fields: `4/20/26`, `4.24.26`, `4/13/2026`, `4/14/2026`, and occasionally malformed entries (`4/8//2026` with a double slash). Before counting or grouping, normalize: strip `//` to `/`, accept both `.` and `/` as separators, accept 2-digit and 4-digit years. Treat any field value containing at least one digit followed by `/` or `.` followed by more digits as a candidate date.

**Migration history:**
- 2026-04-23: Schema migrated from 4-col (T:Status, U:Date, V:Notes, W:Sentiment) to 6-col (T:1st Date, U:1st Status, V:2nd Date, W:2nd Status, X:Notes, Y:Sentiment). Full Target List + Call Log tabs from 4.21.26 forward. Historical Call Log tabs (4.20.26 and earlier) preserved as-is to maintain audit trail integrity.

**Master sheet tabs:**
- Full Target List — all pre-approved targets
- Do Not Call — warm intro targets (Kay handles personally, cold-call operator never calls)
- Niche Context — industry overview for cold-call operator
- Associations — niche associations and events
- Call Log {M.DD.YY} — daily call log tabs

### Ad-Hoc Call Queue

In addition to niche target sheets, cold-call operations reads a "Cold Call Ad-Hoc Calls" Google Sheet for one-off calls that don't belong to any niche (intermediary follow-ups, conference contacts, warm intro follow-ups, etc.). Legacy sheet names may still include JJ until Phase 3 cleanup.

**Sheet location:** OPERATIONS folder in Google Drive
**Headers:** `Company`, `Contact Name`, `Phone`, `Context/Script Notes`, `Target Call Date`, `Priority`, `Call Status`, `Call Date`, `Call Notes`, `Source Link`.

**Morning prep reads:** `Call Status` = "Pending" AND `Target Call Date` <= today
**Harvest:** cold-call operations reads ad-hoc sheet during harvest mode and updates `Call Status`, `Call Date`, `Call Notes`.
**Stale check:** If `Target Call Date` is 3+ business days past and `Call Status` is still "Pending", flag in morning briefing.

### 2. Reply Check (CRITICAL)

Before adding ANY target to the cold-call list, search Gmail for replies using the no-send guard:
```bash
gog gmail search "from:{target_email}" --max 5 --plain --account kay.s@greenwichandbarrow.com --gmail-no-send
```
- **Reply found** → Remove from call list. Flag in pipeline-manager's morning briefing: "{owner} at {company} replied. Cold call canceled."
- **No reply** → Proceed with call assignment.

The operator only calls targets who haven't responded. A call after a reply is redundant and could annoy the owner.

### 3. Personal Tidbit (Optional)

For each verified no-reply target, search for one personal detail:
```bash
WebSearch: "{Owner Name}" "{Company Name}"
```
Extract ONE detail: recent award, conference appearance, company anniversary, industry publication, community involvement, or career milestone. Single sentence. If nothing found, leave blank.

### 4. Weekly Call Log Tab Creation (Monday Morning)

Create **5 Call Log tabs (Mon-Fri)** on the master target sheet for the full week's calls. Each tab uses the **same headers as the Full Target List** — a straight copy of rows.

**Tab names:** `Call Log {M.DD.YY}` for each weekday (e.g., `Call Log 4.14.26` through `Call Log 4.18.26`)

**Process:**
1. Archive previous week's Call Log tabs (hide, don't delete)
2. Create 5 new tabs (Mon through Fri)
3. Write header row on each (same headers as Full Target List)
4. Select 200 targets total (40 per tab) from Full Target List where first-call date/status headers indicate uncalled
5. Copy target rows with all their data — 40 per tab
6. Tier 1 targets (`Owner Name` populated) listed first, then Tier 2, then ad-hoc calls at bottom

**CRITICAL DEPENDENCY:** Prep MUST run AFTER target-discovery's Sunday 3pm pipeline completes. The pool artifact must already be enriched, PE-screened, and warm-intro-cleared before targets are copied to Call Log tabs. If the Sunday pipeline hasn't run, do NOT create tabs — flag in morning briefing.

**Call Status dropdown values:** Connected, Voicemail, No Answer, Wrong Number, Gatekeeper, Callback Requested, Not In Service
**Sentiment dropdown values:** Interested, Neutral, Not Interested

### 5. Monday Slack Message (10am ET)

One Slack message per week on Monday at 10am with the full week's sheet link. This is an operational Slack post, not an email. Only send after validation passes.

**Slack message format:**
```
Hey, here are your calls for this week:

This week's call logs are ready on the sheet: {link to master target sheet}
Tabs: Call Log {M.DD.YY} through Call Log {M.DD.YY} (Mon-Fri)
Call Guide: https://docs.google.com/document/d/12Hqfwxg4qJA3YdZh36ndd-flvYgWN/edit  (G&B Cold Call Guide — generic, not per-niche)

40 calls per day, 200 total this week.
{n} Tier 1 (owner name known), {n} Tier 2 (ask for the owner).

Reminder: Log results directly on each day's tab. If you learn an owner's name, add it to Notes — we'll update the master list.
```

**Rules:**
- Codex identifies as "Codex" in all operator messages. Never mention Kay by name.
- Send to #operations-sva channel via SLACK_WEBHOOK_SVA
- Cold-call target: 40 dials/day (1,000/month). Most will be voicemails, gatekeepers, or no-answers — that's expected. Volume is how cold calling works.
- Add at bottom: "Any feedback on this process at all along the way is welcome and appreciated. Any questions, reply here and I will get them to the right person."
- First week only: add "This is our first week running the new call log format. Please review and share any feedback on the layout."

### 6. Scheduling Protocol

If owner asks for contact info: the operator shares Kay's direct email (kay.s@greenwichandbarrow.com).

If owner wants to schedule during the call: the operator records the agreed time and notifies Kay with owner name, owner email, and agreed time. Kay confirms the calendar invite.
</call_prep>

<call_harvest>
## Mode: Harvest (After 2pm ET)

### 1. Read Daily Call Log Tab

The operator rolls through tabs as a working list — they do NOT strictly call only the rows on today's nominal tab. Harvest must read across ALL Call Log tabs for the current week, not just today's.

For each Call Log tab in the current week (Mon-Fri):
- Read call date/status/notes/sentiment headers for every row
- Identify dialed rows: first-call date populated OR second-call date populated, with corresponding status
- Match each row back to the Full Target List tab by `Company`

### 2. Update Master Sheet

For each row that has any new call data on a daily Call Log tab, update the Full Target List tab:
- First-call date ← from daily Call Log first-call date (only if Full Target List first-call date is currently empty — never overwrite a 1st call date)
- First-call status ← from daily Call Log first-call status (only on first write)
- Second-call date ← from daily Call Log second-call date (only if Full Target List second-call date is currently empty)
- Second-call status ← from daily Call Log second-call status (only on first write)
- Call notes ← from daily Call Log call notes (always overwrite — reflects most recent call)
- Owner sentiment ← from daily Call Log owner sentiment (always overwrite — reflects most recent call)

**Two-attempt cap:** If a row has BOTH first-call status and second-call status populated with No Answer / Voicemail / Gatekeeper (i.e., never connected after 2 attempts), move the company from Full Target List to "Do Not Pursue" tab and flag in pipeline-manager's morning briefing.

### 3. Pace Reporting

Calculate daily dial count by counting populated first-call and second-call date field values across ALL Call Log tabs + the Full Target List, where the normalized date value = today. Tab name is irrelevant (see Pace measurement rule above). Report to Slack at end of harvest: "Cold calls today: {N} dials ({N1} 1st attempts, {N2} 2nd attempts)."

### 4. Owner Name Backfill

If Call Notes contain an owner name AND `Owner Name` is blank on the Full Target List, write the name to `Owner Name`. Free enrichment from the call itself.

### 4. Post-Engagement Enrichment (Phase 3 Trigger)

If Call Status = "Connected" AND Owner Sentiment = "Interested" or "Neutral":
1. Run Apollo `/people/match` for email reveal (1 credit) — need email for follow-up
2. Run warm-intro-finder — check if Kay has a connection for a warmer follow-up
3. Flag for pipeline-manager: "Cold call connected with {owner} at {company}. Sentiment: {sentiment}. Ready for follow-up."
4. If owner said "send me more info" → route to outreach-manager for a draft-only follow-up. Do not create or send email here.
5. Trigger deal-evaluation Phase 1

### 5. Flag Interested Targets

If Call Status = "Connected" and sentiment is positive → flag for pipeline-manager's morning briefing.
</call_harvest>

<stop_hooks>
## Stop Hooks

### Prep Mode Validation

**MANDATORY pre-flight check (runs BEFORE anything else in prep mode):**
- [ ] target-discovery pool artifact exists for the current Sunday at `brain/context/jj-week-pool-{YYYY-MM-DD}.md` and has enough `- row:` entries. If missing or incomplete, **STOP** — do not build Call Log tabs on stale pool. Escalate to Monday briefing: "target-discovery Phase 2 did not complete Sunday; pool is un-enriched. Do not call until rescued." This is the check that would have caught the 2026-04-20 fire.

**Tab build validation:**
- [ ] All selected targets passed reply check (no false positives)
- [ ] Daily Call Log tab created on master sheet with correct date naming (`Call Log {M.DD.YY}`)
- [ ] Tab has the same headers as Full Target List
- [ ] No targets from Do Not Call tab included in call list
- [ ] **No targets with first-call status = "PE-OWNED - SKIP"** (or any other skip-flag) pulled into this week's tabs. Resolve the status header by name. These are companies previously flagged as PE/rollup-owned and permanently excluded from outreach per `memory/feedback_no_pe_owned_targets.md`.
- [ ] **Cross-reference every selected row against the Do Not Call tab by exact `Company` match.** If a company appears on both Do Not Call AND the Full Target List pool, remove from pool. This catches the case where PE re-screen (target-discovery Phase 2 Step 3) moved a company to DNC but the Full Target List row wasn't marked SKIP.
- [ ] **Cross-reference every selected row against the DealsX target universe** (sheet `1VaviHqaJT9Wtm6X1h9B6Q8aOrA8adTiBvt851pkEUFg`, Pest tabs `Specialty Pest & ENV Service (Good Fit) Valid` + `Specialty Pest& ENV Service(Probable Fit) Valid`). Resolve company headers by name. Normalized company-name match (lowercase + strip Inc/LLC/Corp/Co/Ltd + collapse punctuation; strict-on-match). Drop every matching row from the Call Log tab — do NOT annotate-and-keep. Snapshot pre-deletion to `brain/context/rollback-snapshots/jj-dealsx-dedup-{ISO timestamp}.json`. Per `memory/feedback_outreach_channel_universes_separate.md` (HARD doctrine, 2026-05-26). Tab-floor flag (<20 rows after dedup) emits `COLD-CALL WARN` to stdout — does NOT auto-backfill.

**Enrichment integrity (hard gate — blocks Slack send):**
- [ ] Locate pool artifact at `brain/context/jj-week-pool-{YYYY-MM-DD}.md` (written by target-discovery Phase 2 Step 1). If artifact missing → STOP. Pool selection never ran.
- [ ] Every Call Log row has `Owner Name` populated. **If any row has blank `Owner Name`, do NOT send the Slack message.** Run `.codex/hooks/enrichment_integrity_check.py <sheet_id> <pool_artifact_path>` and require PASS before proceeding. On FAIL, escalate as "ENRICHMENT INTEGRITY FAILURE" in Monday briefing and halt prep mode.
- [ ] Every pool row (from Phase 2 Step 1 artifact) appears on exactly one Mon–Fri Call Log tab — no drift between enriched rows and called rows.

> **Enforcement reality (UPDATED 2026-06-07):** Wrapper-level POST_RUN_CHECK validator is in place at `scripts/validate_jj_operations_integrity.py`. Runs after Sunday 18:00 prep mode exits, resolves `Company` and `Owner Name` by header, and verifies all 5 Mon-Fri Call Log tabs exist with owner names populated. Failure overrides EXIT_CODE → Slack alert prefixed `VALIDATOR FAILED`. Two-layer defense: (1) the LLM-level checklist above runs inside the agent, (2) the wrapper validator catches silent-success failures regardless of what the agent did.

**Wrapper validator copyable invocation (manual run):**
```bash
JJ_CALL_NICHES="Premium Pest Management" python3 "$HOME/projects/Sapling/scripts/validate_jj_operations_integrity.py"
# Pass --week-start YYYY-MM-DD to validate a specific week
```

**Slack send gate:**
- [ ] All enrichment integrity checks PASSED (see above)
- [ ] Slack message draft matches expected format with sheet link
- [ ] Operational Slack send is allowed only after validation passes
- [ ] Niche call guide link included

### Harvest Mode Validation
- [ ] Daily Call Log tab read for all rows with Call Status filled
- [ ] Full Target List call date/status/notes/sentiment headers updated for each call
- [ ] Owner name backfill applied where applicable (`Owner Name`)
- [ ] Positive-sentiment targets flagged for pipeline-manager
- [ ] No duplicate entries in master sheet
</stop_hooks>

<success_criteria>
## Success Criteria

- [ ] Cold-call operator receives call list by 10am ET with sheet link working
- [ ] Daily Call Log tab has correct headers matching Full Target List
- [ ] Call types correctly labeled in Slack (OWNER/CALLBACK/AD-HOC counts)
- [ ] No targets with prior replies included in call list
- [ ] Call outcomes harvested same day and Full Target List call headers updated
- [ ] Interested leads flagged immediately
</success_criteria>
