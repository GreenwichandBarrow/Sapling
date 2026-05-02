---
name: email-intelligence
description: "Gmail/Granola scanning, deal flow classification, CIM auto-trigger, Active Deal Fast-Path, intro detection, and email-scan-results artifact. Runs before pipeline-manager. (Superhuman sunset 4/29 — Gmail-only.)"
user_invocable: true
context_budget:
  skill_md: 3500
  max_references: 3
  sub_agent_limit: 2000
---

<objective>
Scan all inbound and outbound email, Gmail drafts, and Granola transcripts. Classify, detect deal signals, and write the email-scan-results artifact that pipeline-manager and other skills consume. (Superhuman sunset 4/29 per `feedback_gmail_only_no_superhuman` — Gmail draft scanning replaces Superhuman MCP.)

**This is the first skill to run in the morning workflow.** Everything downstream depends on its output.

**Output:** `brain/context/email-scan-results-{date}.md` — the handoff contract to pipeline-manager, relationship-manager, and /start.

**Urgent side effects (executed immediately, not deferred):**
- CIM auto-trigger: folder creation, filing, inbox item, deal-eval invocation
- Active Deal Fast-Path: document filing, Attio stage update, Slack ping

**This skill does NOT:**
- Recommend pipeline stage changes (that's pipeline-manager)
- Update People records (that's relationship-manager)
- Create outreach drafts (that's outreach-manager)
- Prep JJ's calls (that's jj-operations)

**Attio write governance:** Email-intelligence writes to Attio ONLY for time-sensitive items: CIM detected (new entry at "Financials Received"), NDA detected (new entry at "NDA Signed"). All other stage changes go through pipeline-manager.
</objective>

<gmail_scanning>
## Gmail Ingestion

### Inbound Email Scan
```bash
gog gmail search "newer_than:2d label:INBOX" --json --max 50
```

For each email, classify and extract:
1. **Deal flow classification:** BLAST (BCC'd, generic), DIRECT (personalized to Kay), or NEWSLETTER
2. **Document detection:** CIM, NDA, LOI, financials (check attachments and body)
3. **Introduction detection:** "I'd like to introduce", "meet my friend", CC patterns
4. **Niche signals:** passive observations about industries mentioned

### Outbound Email Scan
```bash
gog gmail search "from:kay.s@greenwichandbarrow.com newer_than:2d" --json --max 50
```

Detect manually-sent outreach emails not created by outreach-manager. If Kay sent an email to a target in the Active Deals pipeline, update the cadence tracking.

### Precision Rules for Email Characterization (CRITICAL)

When describing actions Kay took via email, use the **exact language from the confirmation/reply email**, not a paraphrase. Common errors to avoid:
- "Downgrade" ≠ "Cancel" — if the vendor confirmed a downgrade, say downgrade
- "Pause" ≠ "Cancel" — if Kay paused a subscription, say pause
- "Inquiry" ≠ "Complaint" — match tone exactly

**Process:** For service-related emails (subscriptions, vendors, support), ALWAYS read the vendor's reply to determine the actual outcome. Kay's outbound request may differ from what was processed. Report the **confirmed outcome**, not Kay's request.

**When the reply from the vendor is available, quote the key phrase** (e.g., "downgraded back to Starter tier" per Reid at Linkt). When no reply exists, say "requested" not "confirmed."

### Gmail Draft Status (replaces Superhuman MCP — sunset 4/29)
Check Gmail drafts via `gog gmail draft list --json`:
- Which drafts were sent vs still pending
- Age of unsent drafts (flag if > 48 hours)
- Cadence triggers from sent drafts

### Session Decision Log Cross-Check
Before flagging any draft as "stale" or "unsent," check `brain/context/session-decisions-{previous-workday}.md`:
- If the decision log shows SENT/DRAFTED for a draft, do not flag it as stale
- If the decision log shows DELETED for a draft, do not surface it at all
- This prevents re-surfacing items Kay already handled via Gmail when draft tooling is unavailable
</gmail_scanning>

<deal_flow_classification>
## Deal Flow Classification

### BLAST Detection
- BCC header present (Delivered-To != To)
- Generic language ("Dear Investor", "Dear Searcher")
- Multiple recipients visible
- Sent from known broker platform domains
- Action: Log count, auto-archive unless matches active niche

### DIRECT Detection
- Addressed specifically to Kay
- References G&B, search fund, or prior conversation
- Personalized content about a specific company
- Action: Flag for review, classify by source (intermediary, owner, advisor)

### NEWSLETTER Detection
- Subscription/mailing list headers
- Known newsletter senders
- Action: Scan for niche signals only, then archive
</deal_flow_classification>

<cim_auto_trigger>
## CIM Auto-Trigger (CRITICAL — Executes Immediately)

**Detection triggers:**
- Attachment filename contains CIM, Confidential Information Memorandum, offering-memorandum
- Attachment is PDF/DOCX > 5 pages
- Subject/body contains "Confidential Information Memorandum"
- Body contains structured financials + company name

**4-step automatic execution:**
1. Create ACTIVE DEALS folder with subfolder structure (CIM/, FINANCIALS/, LEGAL/, DILIGENCE/, CORRESPONDENCE/)
2. File CIM from email to CIM/ subfolder
3. Create inbox item at `brain/inbox/` with `urgency: critical`, `topic/cim-received` tag
4. Auto-invoke deal-evaluation with `source: intermediary-inbound`

**Attio write:** Create entry in Active Deals at "Financials Received" stage with `source: intermediary`

**Validation (must pass before Slack notification):**
- CIM in Drive with size > 0
- No duplicate company folders
- Attio entry created
- Inbox item written with urgency: critical
- deal-evaluation invoked

**Slack:** Notify #active-deals channel after validation passes
</cim_auto_trigger>

<active_deal_fast_path>
## Active Deal Fast-Path (CRITICAL — Executes Immediately)

**Trigger:** Email matches Active Deals entry in stages 3-9 (First Conversation through LOI Signed)

**Process:**
1. Tag as `urgency: critical`
2. Identify document type (CIM, financials, LOI, NDA amendment, etc.)
3. Download attachments, upload to correct Drive subfolder
4. Update Attio stage based on document type
5. Send Slack ping to #active-deals
6. Auto-trigger deal-evaluation if warranted

**Validation:** File in Drive + no duplicates + Attio updated + attachment size > 0
</active_deal_fast_path>

<bookkeeper_pl_auto_trigger>
## Bookkeeper P&L Auto-Trigger (CRITICAL — Executes Immediately)

**Pattern mirrors CIM auto-trigger.** Anthony's monthly Management Report is a deterministic recurring input. Auto-fire `budget-manager monthly` mode on detection — do NOT surface as a Decision item in the morning briefing. See `memory/feedback_bookkeeper_pl_auto_trigger_budget_manager.md` for the precedent.

**Detection triggers (any one):**
- Sender domain is `startvirtual.com` (currently `anthony.b@startvirtual.com`)
- Subject contains "Management Report" + a month/year reference (e.g., "March 2026")
- Attachment filename contains "Profit and Loss", "Balance Sheet", "P&L", or "Management Report"

**4-step automatic execution:**
1. File the PDFs from email to `BOOKKEEPING / MONTHLY REPORTING / {MONTH YEAR}` Drive subfolder (folder ID `1Z__A8AXWBCwQN7x1nK2fqaqhVKlJBJOb`). Create the month subfolder if it doesn't exist.
2. Create inbox item at `brain/inbox/{date}-{month}-management-report-budget-trigger.md` with `urgency: trigger` and tags `topic/bookkeeper-pl-received`, `trigger/budget-manager-monthly`.
3. Auto-invoke `budget-manager monthly` (sequential 3-subagent pipeline per its SKILL.md). Pass `period: {YYYY-MM}` so the skill knows which month to process.
4. The briefing surfaces budget-manager OUTPUT (variance flags, runway change, action items) — NOT the trigger event.

**Validation (must pass before next-step Slack):**
- PDFs in Drive with size > 0
- Inbox item written
- budget-manager invoked successfully (Phase 1 Document Ingester returned non-empty JSON)

**No Attio write.** Bookkeeper reports do not flow into Active Deals or any Attio list.

**No Decisions bucket surface.** The morning briefing should show this trigger only as a `🟢 Wired` line item under System Status, never as a 🔴/🟡 Decision asking for Kay's approval.
</bookkeeper_pl_auto_trigger>

<intro_detection>
## Introduction Detection

Detect warm introductions in email:
- "I'd like to introduce you to..."
- CC patterns (new person CC'd with intro context)
- Forwarded emails with "thought you two should connect"

For each detected intro:
1. Create entity in vault if person doesn't exist
2. Create inbox item with intro context
3. Flag in email-scan-results artifact
</intro_detection>

<granola_ingestion>
## Granola Ingestion

Query Granola MCP for meetings since last run:
```
mcp__granola__list_meetings
mcp__granola__get_meeting_transcript
```

For each new meeting:
1. Write call note to `brain/calls/{date}-{slug}.md`
2. Extract action items, next steps, commitments
3. Include in email-scan-results artifact under "Granola Action Items"

**Idempotency:** Check if `brain/calls/` file already exists (by call_id) before writing. Skip if duplicate.
</granola_ingestion>

<artifact>
## Email Scan Results Artifact

Write to `brain/context/email-scan-results-{date}.md`:

### Required Sections (all 6 must be present, even if "None")

1. **Actionable Items Created** — inbox items created from emails (with source_ref)
2. **Deal Flow Classified** — DIRECT/BLAST/NEWSLETTER counts
3. **Draft Status** — sent vs unsent drafts with age
4. **Introductions Detected** — new intros found in email
5. **Niche Signals** — passive niche observations from email/Granola
6. **In-Person Meetings Today** — from calendar, for Granola reminder

### Validation
- File exists and is non-empty
- All 6 section headers present
- Each section populated or explicitly marked "None"
</artifact>

<stop_hooks>
## Stop Hooks

1. **Gmail ingestion** — actionable email count matches inbox files written
2. **Granola ingestion** — meeting count matches brain/calls/ files written
3. **CIM auto-trigger** — for every CIM: folder exists, file uploaded (size > 0), inbox item written, deal-eval invoked
4. **Active Deal Fast-Path** — for every fast-path item: file in Drive, Attio updated
5. **Email-scan-results artifact** — file exists, non-empty, all 6 sections present
6. **Slack notifications** — webhook returned 200 OK for all pings
7. **ACTIVE DEALS folder sync** — every Drive subfolder has matching Attio entry
</stop_hooks>

<success_criteria>
## Success Criteria

- [ ] All inbound emails classified (DIRECT/BLAST/NEWSLETTER)
- [ ] CIM/NDA/LOI detected and processed immediately
- [ ] Active deal emails filed to correct Drive subfolders
- [ ] Introductions detected and entities created
- [ ] Granola transcripts ingested
- [ ] email-scan-results artifact written with all 6 sections
- [ ] No missed deal signals
</success_criteria>
