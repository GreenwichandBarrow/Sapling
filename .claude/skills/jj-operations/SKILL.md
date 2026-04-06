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
Manage JJ's daily calling operations end-to-end. JJ is a VA (Philippines) working Mon-Fri 10am-2pm ET. This skill handles:
1. Overnight call prep (target selection, reply checking, daily call tab creation)
2. 10am Slack delivery (call list with sheet link)
3. Post-shift outcome harvesting (reading daily call tab, updating master sheet)

JJ works from the daily call tab on the master target sheet and Slack messages. Each niche has a static Call Guide doc he references for scripts, objections, and niche context.

**Two run modes:**
- `prep` — overnight before 10am, selects targets and creates daily call tab
- `harvest` — overnight after 2pm, reads daily call tab and updates the master sheet

**This skill does NOT:**
- Create outreach drafts (that's outreach-manager)
- Decide which targets get approved (that's Kay via the tracker)
- Manage the target list sheet (that's target-discovery)
- Move Attio pipeline stages (that's pipeline-manager)
</objective>

<call_prep>
## Mode: Prep (Before 10am ET)

### 1. Target Selection

**JJ is decoupled from Salesforge cold outreach cadences.** JJ's call list is managed independently by jj-operations, not triggered by email send events. Targets come from Kay's approvals and the ad-hoc queue, not from Col X.

Read the active niche sprint's master sheet ("{Niche} - Target List"). Select targets where:
- Col Q (Kay: Decision) = "Approve"
- Col T (JJ: Call Status) is empty
- Target's niche has Outreach Channel = "JJ-Call-Only" on WEEKLY REVIEW (see Channel Filter below)

### Two-Tier Target Selection (Calls-First)

Calls-first niches load 500-1000 targets via Phase 1 volume load. Not all will have owner names yet (owner enrichment happens weekly in Phase 2). JJ handles both tiers:

**Tier 1 (enriched):** Col J (Owner Name) is populated. JJ asks the gatekeeper for the owner by name: "Is {Owner Name} available?" Higher conversion.

**Tier 2 (raw):** Col J (Owner Name) is blank. JJ uses generic opener: "May I speak with the owner or person in charge?" Lower conversion but still valuable. JJ can extract the owner's name from the call for future attempts.

**Daily target selection priority:**
1. Fill from Tier 1 first (up to 40)
2. If Tier 1 has fewer than 40 available, backfill from Tier 2
3. Always prefer Tier 1

**Owner name backfill:** If JJ learns the owner's name during a call (gatekeeper tells him, voicemail greeting, owner introduces themselves), capture it in Call Notes. Harvest mode writes it to Col J — free enrichment from the call itself.

### Channel Filter (CRITICAL)

**Why this exists:** JJ is decoupled from Salesforge email cadences. Calling a target who's in an active email sequence creates conflicting touchpoints.

Before building the call list, read the WEEKLY REVIEW tab to determine which niches route to JJ:

```bash
gog sheets get 1vHx4E1tRTR6V3k7NQeHdCrUjDITJVtZA5YPSIFeSins --range "WEEKLY REVIEW!A3:D20" --json
```

Build a map of **niche name (Col B) → outreach channel (Col D)**. Then for each target sheet:
- Match the sheet's niche to the WEEKLY REVIEW map
- **Include** targets only if their niche's outreach channel = `JJ-Call-Only`
- **Skip** targets if their niche's outreach channel = `Salesforge Email` or any other value
- **HARD STOP:** If a niche is missing from WEEKLY REVIEW, do NOT add ANY targets from that niche to the call list. Flag in morning briefing as requiring manual review. This is a safety gate — unknown channel means unknown routing.

This filter runs BEFORE the reply check — no point checking replies for targets JJ won't call.

**Sheet IDs (all 5 target lists):**
- Art Insurance: `15M76-gpcklwc47HDXIwyFC9Tj8K4wDOor4i0uxCYyHQ`
- Domestic TCI: `1lEAx-3pEshsSc0Rix4KunJ38mzHahjAmV6nQA_cuwLw`
- IPLC: `1Cdw6yb8-yBQtx5mTB8Hu4rENkJfpmt3t7HZdGqtdylQ`
- Art Storage: `1PDprJ_gApm7T_kzpNWlWk7qItQ11M95ssL9_UD5sE9g`
- Art Advisory: `1c6Db21D2qDpiT7LnEQ4l0AROlA-gucDQD1ZGOlrZ-K0`
- Premium Pest Management: `1Y0ZjEkc2LHhBoO4QGO8Ny9MvG90NpojQn8bloKA291I`

**Master sheet columns (A-X, 24 columns):**
- A: Source, B: Company, C: Website, D: Headquarters, E: Industry, F: Employees
- G: Rev Source, H: Revenue, I: Ownership, J: Owner Name, K: Owner Title
- L: Email, M: Phone, N: LinkedIn Connection, O: LinkedIn (Owner), P: LinkedIn (Company)
- Q: Kay: Decision (Approve/Pass)
- R: Kay: Pass Reason
- S: Agent Notes (RECOMMEND: Approve/Pass prefix)
- T: JJ: Call Status
- U: JJ: Call Date
- V: JJ: Call Notes
- W: JJ: Owner Sentiment
- X: ICP Match
- Outreach tracking columns (managed by outreach-manager, not read or written by jj-operations)

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

### 4. Daily Call Tab Creation

Instead of individual Call Log docs, create a single tab on the master target sheet for the day's calls.

**Tab name:** `Calls {M.DD.YY}` (e.g., `Calls 4.07.26`)

**Columns (A-I):**
| Col | Header | Source | JJ Fills |
|-----|--------|--------|----------|
| A | # | Row number | |
| B | Company | Col B from master | |
| C | Owner Name | Col J from master (blank if Tier 2) | |
| D | Phone | Col M from master | |
| E | Signal | One-line tidbit from web search (Step 3) | |
| F | Call Status | | Yes |
| G | Duration | | Yes |
| H | Notes | | Yes |
| I | Sentiment | | Yes |

**Call Status dropdown values:** Connected, Voicemail, No Answer, Wrong Number, Gatekeeper, Callback Requested
**Sentiment dropdown values:** Interested, Neutral, Not Interested

**Tab formatting:**
- Freeze row 1 (headers)
- Bold headers
- Columns F-I highlighted light yellow (JJ's input columns)
- Add data validation dropdowns on Col F (Call Status) and Col I (Sentiment)
- Row order: Tier 1 targets first (owner name known), then Tier 2 (owner name blank), then ad-hoc calls at bottom with "AD-HOC" prefix in Col B

**Niche Call Guide reference:** Add a merged header row above the table (row 1): "Call Guide: {link to niche call guide Google Doc}" — data table starts at row 2.

**Niche Call Guide locations (Google Docs):**
- Premium Pest Management: https://docs.google.com/document/d/1EGDgKvIHm4EtmP87YM9ffibmpKs4JqVbsuYGLvHWj5M/edit
- Other niches: create from `templates/cold-call-guide-{niche-slug}.md` on niche activation

**Tab archival:** Old daily tabs accumulate. On Monday prep, archive previous week's tabs by hiding them (not deleting — harvest may need re-reads).

### 5. Slack Message Draft

Draft the Slack message and present to Kay for approval before sending. Use two-gate process: Kay approves content, then approves the message draft.

**Call type labels (CRITICAL):** Every call must be labeled OWNER CALL or CALLBACK. JJ needs this before dialing.

**Slack message format:**
```
Hey JJ, here are your calls for today:

{n} calls on the sheet: {link to daily call tab on master sheet}
Call Guide: {link to niche call guide Google Doc}

OWNER CALLS: {n}
CALLBACKS: {n}
AD-HOC: {n}

Dial target today: {n} total

Reminder: Log results directly on the sheet tab (columns F-I). If you learn an owner's name, add it to Notes.
```

**Rules:**
- Claude identifies as "Claude" in all JJ messages. Never mention Kay by name.
- Send to #operations-sva channel via SLACK_WEBHOOK_SVA
- JJ dial target: 40 dials/day (1,000/month). Most will be voicemails, gatekeepers, or no-answers — that's expected. Volume is how cold calling works.
- Add at bottom: "Any feedback on this process at all along the way is welcome and appreciated. Any questions, reply here and I will get them to the right person."

### 6. Scheduling Protocol

If owner wants to schedule during JJ's call: JJ books a time with the owner, then emails Howie (barrie@greenwichandbarrow.com) with owner name, owner email, and agreed time. Howie creates the calendar invite.
</call_prep>

<call_harvest>
## Mode: Harvest (After 2pm ET)

### 1. Read Daily Call Tab

Read the `Calls {M.DD.YY}` tab from the master target sheet for today's date.
- Read columns F-I for all rows where Col F (Call Status) is not empty
- Match each row back to the master sheet's main tab by company name (Col B)

### 2. Update Master Sheet

For each completed call on the daily tab, update the master sheet's main tab:
- Col T (JJ: Call Status) ← from daily tab Col F
- Col U (JJ: Call Date) ← today's date
- Col V (JJ: Call Notes) ← from daily tab Col H
- Col W (JJ: Owner Sentiment) ← from daily tab Col I

### 3. Owner Name Backfill

If JJ's Notes (daily tab Col H) contain an owner name AND Col J (Owner Name) is blank on the master sheet, write the name to Col J. Free enrichment from the call itself.

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
- [ ] Daily call tab created on master sheet with correct date naming (`Calls {M.DD.YY}`)
- [ ] Tab has all columns (A-I) with headers and data validation dropdowns
- [ ] Tier 1 targets listed before Tier 2 targets
- [ ] Niche call guide link included in tab header or Slack message
- [ ] Slack message draft matches expected format with sheet link
- [ ] Kay approved the Slack message before sending

### Harvest Mode Validation
- [ ] Daily call tab read for all rows with Call Status filled
- [ ] Master sheet columns T-W updated for each call
- [ ] Owner name backfill applied where applicable (Col J)
- [ ] Positive-sentiment targets flagged for pipeline-manager
- [ ] No duplicate entries in master sheet
</stop_hooks>

<success_criteria>
## Success Criteria

- [ ] JJ receives call list by 10am ET with sheet link working
- [ ] Daily call tab has correct columns, dropdowns, and call guide link
- [ ] Call types correctly labeled in Slack (OWNER/CALLBACK/AD-HOC counts)
- [ ] No targets with prior replies included in call list
- [ ] Call outcomes harvested same day and master sheet columns T-W updated
- [ ] Interested leads flagged immediately
</success_criteria>
