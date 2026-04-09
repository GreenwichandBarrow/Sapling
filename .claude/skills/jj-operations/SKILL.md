---
name: jj-operations
description: "JJ daily call prep, daily call tab creation, 10am Slack delivery, and post-shift outcome harvesting. Owns all JJ-facing operations."
user_invocable: true
context_budget:
  skill_md: 2000
  max_references: 2
  sub_agent_limit: 2000
---

<objective>
Manage JJ's calling operations end-to-end. JJ is a VA (Philippines) working Mon-Fri 10am-2pm ET. This skill handles:
1. Monday morning prep: create the full week's 5 Call Log tabs (Mon-Fri, 40 targets each) from the clean Full Target List
2. Monday 10am Slack delivery: week's sheet link + call guide
3. Daily harvest (Mon-Fri after 2pm): read each day's Call Log tab, update Full Target List

JJ works from the daily Call Log tab on the master target sheet and Slack messages. Each niche has a static Call Guide doc he references for scripts, objections, and niche context.

**Two run modes:**
- `prep` — Monday 9am, creates 5 Call Log tabs (Mon-Fri) for the full week. Runs AFTER target-discovery's Sunday night pipeline (owner enrichment → PE re-screen → warm intro check) has cleaned the Full Target List.
- `harvest` — Mon-Fri after 2pm, reads that day's Call Log tab and updates the Full Target List

**Weekly cadence (Option A):**
- Sunday 11pm: target-discovery Phase 2 pipeline runs (enrich → PE screen → warm intro check)
- Monday 9am: jj-operations `prep` creates 5 tabs from clean pool
- Monday 10am: Slack to JJ with week's sheet link
- Mon-Fri 4pm: jj-operations `harvest` reads each day's results
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

**JJ is decoupled from email outreach cadences (Kay Email and DealsX Email channels).** JJ's call list is managed independently by jj-operations, not triggered by email send events. Targets come from the Full Target List (all pre-approved by target-discovery auto-screening).

Read the active niche sprint's master sheet ("{Niche} - Target List"). Select targets where:
- Col T (JJ: Call Status) is empty (hasn't been called yet)
- Target's niche has Outreach Channel = "JJ-Call-Only" on WEEKLY REVIEW (see Channel Filter below)

### Two-Tier Target Selection (Calls-First)

Calls-first niches load 500-1000 targets via Phase 1 volume load. Not all will have owner names yet (owner enrichment happens weekly in Phase 2). JJ handles both tiers:

**Tier 1 (enriched):** Col K (Owner Name) is populated. JJ asks the gatekeeper for the owner by name: "Is {Owner Name} available?" Higher conversion.

**Tier 2 (raw):** Col K (Owner Name) is blank. JJ uses generic opener: "May I speak with the owner or person in charge?" Lower conversion but still valuable. JJ can extract the owner's name from the call for future attempts.

**Daily target selection priority:**
1. Fill from Tier 1 first (up to 40)
2. If Tier 1 has fewer than 40 available, backfill from Tier 2
3. Always prefer Tier 1

**Owner name backfill:** If JJ learns the owner's name during a call (gatekeeper tells him, voicemail greeting, owner introduces themselves), capture it in Call Notes. Harvest mode writes it to Col K — free enrichment from the call itself.

### Channel Filter (CRITICAL)

**Why this exists:** JJ is decoupled from email outreach cadences (Kay Email and DealsX Email). Calling a target who's in an active email sequence creates conflicting touchpoints.

Before building the call list, read the WEEKLY REVIEW tab to determine which niches route to JJ:

```bash
gog sheets get 1vHx4E1tRTR6V3k7NQeHdCrUjDITJVtZA5YPSIFeSins --range "WEEKLY REVIEW!A3:D20" --json
```

Build a map of **niche name (Col B) → outreach channel (Col D)**. Then for each target sheet:
- Match the sheet's niche to the WEEKLY REVIEW map
- **Include** targets only if their niche's outreach channel = `JJ-Call-Only`
- **Skip** targets if their niche's outreach channel = `Kay Email`, `DealsX Email`, or any other value
- **HARD STOP:** If a niche is missing from WEEKLY REVIEW, do NOT add ANY targets from that niche to the call list. Flag in morning briefing as requiring manual review. This is a safety gate — unknown channel means unknown routing.

This filter runs BEFORE the reply check — no point checking replies for targets JJ won't call.

**Sheet IDs (all target lists):**
- Art Insurance: `15M76-gpcklwc47HDXIwyFC9Tj8K4wDOor4i0uxCYyHQ`
- Domestic TCI: `1lEAx-3pEshsSc0Rix4KunJ38mzHahjAmV6nQA_cuwLw`
- IPLC: `1Cdw6yb8-yBQtx5mTB8Hu4rENkJfpmt3t7HZdGqtdylQ`
- Art Storage: `1PDprJ_gApm7T_kzpNWlWk7qItQ11M95ssL9_UD5sE9g`
- Art Advisory: `1c6Db21D2qDpiT7LnEQ4l0AROlA-gucDQD1ZGOlrZ-K0`
- Premium Pest Management: `1Y0ZjEkc2LHhBoO4QGO8Ny9MvG90NpojQn8bloKA291I`

**Master sheet columns (A-W, 23 columns):**
- A: Source, B: Company, C: Website, D: Headquarters, E: Industry, F: Employees
- G: Rev Source, H: Revenue, I: Year Founded, J: Ownership
- K: Owner Name, L: Owner Title, M: Email
- N: Phone (Company), O: Phone (Owner)
- P: LinkedIn Connection, Q: LinkedIn (Owner), R: LinkedIn (Company)
- S: Agent Notes
- T: JJ: Call Status, U: JJ: Call Date, V: JJ: Call Notes, W: JJ: Owner Sentiment

**Master sheet tabs:**
- Full Target List — all pre-approved targets
- Do Not Call — warm intro targets (Kay handles personally, JJ never calls)
- Niche Context — industry overview for JJ
- Associations — niche associations and events
- Call Log {M.DD.YY} — daily call log tabs

### Ad-Hoc Call Queue

In addition to niche target sheets, jj-operations reads a "JJ Ad-Hoc Calls" Google Sheet for one-off calls that don't belong to any niche (intermediary follow-ups, conference contacts, warm intro follow-ups, etc.).

**Sheet location:** OPERATIONS folder in Google Drive
**Columns:** A (Company), B (Contact Name), C (Phone), D (Context/Script Notes), E (Target Call Date), F (Priority: Normal/Urgent), G (Call Status: Pending/Called/Voicemail/Connected/Cancelled), H (Call Date), I (Call Notes), J (Source Link)

**Morning prep reads:** Col G = "Pending" AND Col E <= today
**Harvest:** jj-operations reads ad-hoc sheet during harvest mode and updates Col G, H, I.
**Stale check:** If Col E (Target Call Date) is 3+ business days past and Col G is still "Pending", flag in morning briefing.

### 2. Reply Check (CRITICAL)

Before adding ANY target to JJ's call list, search Gmail for replies:
```bash
gog gmail search "from:{target_email}" --max 5 --plain
```
- **Reply found** → Remove from call list. Flag in pipeline-manager's morning briefing: "{owner} at {company} replied. JJ call canceled."
- **No reply** → Proceed with call assignment.

JJ only calls targets who haven't responded. A call after a reply is redundant and could annoy the owner.

### 3. Personal Tidbit (Optional)

For each verified no-reply target, search for one personal detail:
```bash
WebSearch: "{Owner Name}" "{Company Name}"
```
Extract ONE detail: recent award, conference appearance, company anniversary, industry publication, community involvement, or career milestone. Single sentence. If nothing found, leave blank.

### 4. Weekly Call Log Tab Creation (Monday Morning)

Create **5 Call Log tabs (Mon-Fri)** on the master target sheet for the full week's calls. Each tab uses the **same 23 columns (A-W) as the Full Target List** — a straight copy of rows.

**Tab names:** `Call Log {M.DD.YY}` for each weekday (e.g., `Call Log 4.14.26` through `Call Log 4.18.26`)

**Process:**
1. Archive previous week's Call Log tabs (hide, don't delete)
2. Create 5 new tabs (Mon through Fri)
3. Write header row on each (same A-W headers as Full Target List)
4. Select 200 targets total (40 per tab) from Full Target List where Col T (JJ: Call Status) is empty
5. Copy target rows with all their data — 40 per tab
6. Tier 1 targets (Col K populated) listed first, then Tier 2, then ad-hoc calls at bottom

**CRITICAL DEPENDENCY:** Prep MUST run AFTER target-discovery's Sunday night pipeline completes. The Full Target List must already be enriched, PE-screened, and warm-intro-cleared before targets are copied to Call Log tabs. If the Sunday pipeline hasn't run, do NOT create tabs — flag in morning briefing.

**Call Status dropdown values (Col T):** Connected, Voicemail, No Answer, Wrong Number, Gatekeeper, Callback Requested, Not In Service
**Sentiment dropdown values (Col W):** Interested, Neutral, Not Interested

### 5. Monday Slack Message (10am ET)

One Slack message per week on Monday at 10am with the full week's sheet link. Draft and present to Kay for approval before sending.

**Slack message format:**
```
Hey JJ, here are your calls for this week:

This week's call logs are ready on the sheet: {link to master target sheet}
Tabs: Call Log {M.DD.YY} through Call Log {M.DD.YY} (Mon-Fri)
Call Guide: {link to niche call guide Google Doc}

40 calls per day, 200 total this week.
{n} Tier 1 (owner name known), {n} Tier 2 (ask for the owner).

Reminder: Log results directly on each day's tab (columns T-W). If you learn an owner's name, add it to Notes — we'll update the master list.
```

**Rules:**
- Claude identifies as "Claude" in all JJ messages. Never mention Kay by name.
- Send to #operations-sva channel via SLACK_WEBHOOK_SVA
- JJ dial target: 40 dials/day (1,000/month). Most will be voicemails, gatekeepers, or no-answers — that's expected. Volume is how cold calling works.
- Add at bottom: "Any feedback on this process at all along the way is welcome and appreciated. Any questions, reply here and I will get them to the right person."
- First week only: add "This is our first week running the new call log format. Please review and share any feedback on the layout."

### 6. Scheduling Protocol

If owner asks for contact info: JJ shares Kay's direct email (kay.s@greenwichandbarrow.com).

If owner wants to schedule during JJ's call: JJ books a time with the owner, then emails Kay (kay.s@greenwichandbarrow.com) with owner name, owner email, and agreed time. Kay confirms the calendar invite.
</call_prep>

<call_harvest>
## Mode: Harvest (After 2pm ET)

### 1. Read Daily Call Log Tab

Read the `Call Log {M.DD.YY}` tab from the master target sheet for today's date.
- Read columns T-W for all rows where Col T (JJ: Call Status) is not empty
- Match each row back to the Full Target List tab by company name (Col B)

### 2. Update Master Sheet

For each completed call on the daily Call Log tab, update the Full Target List tab:
- Col T (JJ: Call Status) ← from daily Call Log Col T
- Col U (JJ: Call Date) ← today's date
- Col V (JJ: Call Notes) ← from daily Call Log Col V
- Col W (JJ: Owner Sentiment) ← from daily Call Log Col W

### 3. Owner Name Backfill

If JJ's Notes (Col V) contain an owner name AND Col K (Owner Name) is blank on the Full Target List, write the name to Col K. Free enrichment from the call itself.

### 4. Post-Engagement Enrichment (Phase 3 Trigger)

If Call Status = "Connected" AND Owner Sentiment = "Interested" or "Neutral":
1. Run Apollo `/people/match` for email reveal (1 credit) — need email for follow-up
2. Run warm-intro-finder — check if Kay has a connection for a warmer follow-up
3. Flag for pipeline-manager: "JJ connected with {owner} at {company}. Sentiment: {sentiment}. Ready for follow-up."
4. If owner said "send me more info" → draft follow-up email in Superhuman immediately
5. Trigger deal-evaluation Phase 1

### 5. Flag Interested Targets

If Call Status = "Connected" and sentiment is positive → flag for pipeline-manager's morning briefing.
</call_harvest>

<stop_hooks>
## Stop Hooks

### Prep Mode Validation
- [ ] All selected targets passed reply check (no false positives)
- [ ] Daily Call Log tab created on master sheet with correct date naming (`Call Log {M.DD.YY}`)
- [ ] Tab has all 23 columns (A-W) matching Full Target List
- [ ] Tier 1 targets listed before Tier 2 targets
- [ ] Niche call guide link included in Slack message
- [ ] Slack message draft matches expected format with sheet link
- [ ] Kay approved the Slack message before sending
- [ ] No targets from Do Not Call tab included in call list

### Harvest Mode Validation
- [ ] Daily Call Log tab read for all rows with Call Status filled
- [ ] Full Target List columns T-W updated for each call
- [ ] Owner name backfill applied where applicable (Col K)
- [ ] Positive-sentiment targets flagged for pipeline-manager
- [ ] No duplicate entries in master sheet
</stop_hooks>

<success_criteria>
## Success Criteria

- [ ] JJ receives call list by 10am ET with sheet link working
- [ ] Daily Call Log tab has correct 23 columns matching Full Target List
- [ ] Call types correctly labeled in Slack (OWNER/CALLBACK/AD-HOC counts)
- [ ] No targets with prior replies included in call list
- [ ] Call outcomes harvested same day and Full Target List columns T-W updated
- [ ] Interested leads flagged immediately
</success_criteria>
