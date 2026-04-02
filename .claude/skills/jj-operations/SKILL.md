---
name: jj-operations
description: "JJ daily call prep, call log creation, 10am Slack delivery, and post-shift outcome harvesting. Owns all JJ-facing operations."
user_invocable: true
context_budget:
  skill_md: 2000
  max_references: 2
  sub_agent_limit: 2000
---

<objective>
Manage JJ's daily calling operations end-to-end. JJ is a VA (Philippines) working Mon-Fri 10am-2pm ET. This skill handles:
1. Overnight call prep (target selection, reply checking, Call Log doc creation)
2. 10am Slack delivery (call list with links)
3. Post-shift outcome harvesting (reading Call Logs, updating master sheet)

JJ does NOT touch the master target sheet. He works from Call Log docs and Slack messages only.

**Two run modes:**
- `prep` — overnight before 10am, selects targets and creates Call Logs
- `harvest` — overnight after 2pm, reads completed Call Logs and updates the sheet

**This skill does NOT:**
- Create outreach drafts (that's outreach-manager)
- Decide which targets get approved (that's Kay via the tracker)
- Manage the target list sheet (that's target-discovery)
- Move Attio pipeline stages (that's pipeline-manager)
</objective>

<call_prep>
## Mode: Prep (Before 10am ET)

### 1. Target Selection

Read the active niche sprint's master sheet ("{Niche} - Target List"). Select targets where:
- Col O (Kay: Decision) = "Approve"
- Col X (Outreach Stage) = "Email Sent"
- Col R (JJ: Call Status) is empty

**Sheet IDs (all 5 target lists):**
- Art Insurance: `15M76-gpcklwc47HDXIwyFC9Tj8K4wDOor4i0uxCYyHQ`
- Domestic TCI: `1lEAx-3pEshsSc0Rix4KunJ38mzHahjAmV6nQA_cuwLw`
- IPLC: `1Cdw6yb8-yBQtx5mTB8Hu4rENkJfpmt3t7HZdGqtdylQ`
- Art Storage: `1PDprJ_gApm7T_kzpNWlWk7qItQ11M95ssL9_UD5sE9g`
- Art Advisory: `1c6Db21D2qDpiT7LnEQ4l0AROlA-gucDQD1ZGOlrZ-K0`

**Master sheet columns (A-X, 24 columns):**
- A-N: Source through LinkedIn (Company) — list building data
- O: Kay: Decision (Approve/Pass)
- P: Kay: Pass Reason
- Q: Agent Notes (RECOMMEND: Approve/Pass prefix)
- R: JJ: Call Status
- S: JJ: Call Date
- T: JJ: Call Notes
- U: JJ: Owner Sentiment
- V: ICP Match
- W: ICP Miss Reason
- X: Outreach Stage (trigger column: Approved → Email Drafted → Email Sent → JJ Queued → JJ Called)

### 2. Reply Check (CRITICAL)

Before adding ANY target to JJ's call list, search Gmail for replies:
```bash
gog gmail search "from:{target_email}" --max 5 --plain
```
- **Reply found** → Remove from call list. Update Col X to "Reply Received". Flag in pipeline-manager's morning briefing: "{owner} at {company} replied. JJ call canceled."
- **No reply** → Proceed with call assignment.

JJ only calls targets who haven't responded. A call after a reply is redundant and could annoy the owner.

### 3. Personal Tidbit (Optional)

For each verified no-reply target, search for one personal detail:
```bash
WebSearch: "{Owner Name}" "{Company Name}"
```
Extract ONE detail: recent award, conference appearance, company anniversary, industry publication, community involvement, or career milestone. Single sentence. If nothing found, leave blank.

### 4. Call Log Creation

For each target, create a Call Log doc from template (ID: `1nvvdOU7I5NLAwxrYgHIFTRNrEZmc67X8`):
- Copy template → save to OPERATIONS / CALL LOGS / TARGET LIST CALLS
- Name: "Call Log - {Company Name} {M.DD.YY}.docx"
- Pre-populate COMPANY INFO from master target sheet
- Customize SCRIPT section with company-specific operational signal
- Add "Personal Note for JJ" field with tidbit (if found)
- Include Howie's email (barrie@greenwichandbarrow.com) for scheduling

### 5. Slack Message Draft

Draft the Slack message and present to Kay for approval before sending. Use two-gate process: Kay approves content, then approves the message draft.

**Call type labels (CRITICAL):** Every call must be labeled OWNER CALL, CUSTOMER CALL, or CALLBACK. JJ needs this before dialing.

**Slack message format:**
```
Hey JJ, here are your calls for today:

OWNER CALL:
1. {Owner Name} - {Company} ({Industry})
   Phone: {phone}
   Call Log: {google_doc_link}

CUSTOMER CALL:
2. {Contact Name} - {Company} (validating {niche name})
   Phone: {phone}
   Call Log: {google_doc_link}

CALLBACK:
3. {Owner Name} - {Company} (follow-up from {date})
   Phone: {phone}
   Call Log: {google_doc_link}

Dial target today: {n} ({n} owner + {n} customer validation + {n} callbacks)
```

**Rules:**
- Claude identifies as "Claude" in all JJ messages. Never mention Kay by name.
- Send to #operations-sva channel via SLACK_WEBHOOK_SVA
- JJ dial target: 8-12 dials/day (owner + customer validation + callbacks)
- Add at bottom: "Any feedback on this process at all along the way is welcome and appreciated. Any questions, reply here and I will get them to the right person."

### 6. Scheduling Protocol

If owner wants to schedule during JJ's call: JJ books a time with the owner, then emails Howie (barrie@greenwichandbarrow.com) with owner name, owner email, and agreed time. Howie creates the calendar invite.
</call_prep>

<call_harvest>
## Mode: Harvest (After 2pm ET)

### 1. Read Call Logs

Read all Call Log docs updated today in OPERATIONS / CALL LOGS:
- Check for docs with today's date in the filename
- Read Call Outcome and Call Notes fields

### 2. Update Master Sheet

For each completed call, update the master target sheet:
- Col R: JJ: Call Status ← from Call Status field (Connected/Voicemail/No Answer/Wrong Number)
- Col S: JJ: Call Date ← from Call Date field
- Col T: JJ: Call Notes ← summarize detailed notes into one line
- Col U: JJ: Owner Sentiment ← from Owner Sentiment field
- Col X: Outreach Stage ← "JJ Called"

### 3. Flag Interested Targets

If Call Status = "Connected" and sentiment is positive → flag for pipeline-manager's morning briefing, trigger deal-evaluation Phase 1.
</call_harvest>

<customer_validation_calls>
## Customer Validation Call Lists

Customer validation calls follow a separate process managed by niche-intelligence (Step 5b). JJ-operations delivers approved lists to JJ via Slack using the two-gate process:

1. Niche-intelligence preps the call list docs
2. Kay reviews and approves each doc individually
3. For each approved doc, Claude drafts the Slack message and presents to Kay
4. Once Kay approves the message, Claude sends ONE Slack message per niche
5. Each message includes the call list link AND the niche one-pager link
6. "Any feedback on this process at all along the way is welcome and appreciated"

See niche-intelligence SKILL.md Step 5b for the full customer validation call list process.
</customer_validation_calls>

<stop_hooks>
## Stop Hooks

### Prep Mode Validation
- [ ] All selected targets passed reply check (no false positives)
- [ ] Call Log docs created in Drive with correct naming
- [ ] Each Call Log has pre-populated company info and customized script
- [ ] Slack message draft matches expected format with correct call type labels
- [ ] Kay approved the Slack message before sending

### Harvest Mode Validation
- [ ] All updated Call Log docs were read
- [ ] Master sheet columns R-U updated for each call, Col X set to "JJ Called"
- [ ] Positive-sentiment targets flagged for pipeline-manager
- [ ] No duplicate entries in master sheet
</stop_hooks>

<success_criteria>
## Success Criteria

- [ ] JJ receives call list by 10am ET with all links working
- [ ] Call types correctly labeled (OWNER/CUSTOMER/CALLBACK)
- [ ] No targets with prior replies included in call list
- [ ] Call outcomes harvested same day and sheet updated
- [ ] Interested leads flagged immediately
</success_criteria>
