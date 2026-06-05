---
name: email-intelligence
description: "Gmail/Granola scanning, deal flow classification, CIM auto-trigger, Active Deal Fast-Path, intro detection, and email-scan-results artifact. Runs before pipeline-manager. Gmail-only for drafts and sent-status checks."
archetype: router
context_budget:
  skill_md: 200
  max_references: 12
  learnings_md: 40
  sub_agent_limit: 500
user_invocable: true
---

<credentials>
## Credentials (read first)

**1Password is the first rung — always.** Before any op://-backed CLI or REST call:
```bash
source /home/ubuntu/projects/Sapling/scripts/op-env.sh
```
Exports `ATTIO_API_KEY`, `APOLLO_API_KEY`, `GRANOLA_KEY`, `GOG_KEYRING_PASSWORD`, `SLACK_WEBHOOK_*`. **NEVER `source scripts/.env.launchd` raw** — it exports literal op:// reference strings, not values (hook-blocked; see `feedback_op_env_before_op_backed_cli`).

**REST is the default, MCP is a convenience.** If an MCP call appears below (`mcp__granola__*`, `mcp__attio__*`), it has a REST fallback. An unloaded MCP tool is NOT an outage — fall through to REST. For Granola, the canonical wrapper is `~/.local/bin/granola-api`.

**Health-check pattern (mandatory before claiming a service is down in an artifact):**
```bash
curl -s -o /dev/null -w "%{http_code}\n" -H "Authorization: Bearer $ATTIO_API_KEY" https://api.attio.com/v2/self
# 200 = up. Non-200 = real outage. Unloaded MCP tool = not an outage.
```

**Forbidden in the scan artifact:** writing "MCP unauthenticated / disconnected / unavailable" as a system-status alert without first running the op-env resolve + REST health-check above. Phantom outages corrupt downstream decisions.
</credentials>

<objective>
Scan all inbound and outbound email, Gmail drafts, and Granola transcripts. Classify, detect deal signals, and write the email-scan-results artifact that pipeline-manager and other skills consume.

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

### Gmail Draft Status
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
- **If body matches broker-signal keywords ("for sale", "exclusive listing", "asking price", "we represent", "new listing", "now available"), trigger per-listing body parsing. See `<broker_blast_listing_extraction>` below. NOTE: known-broker sender recognition (previously Attio-list-driven) is currently body-keyword-only — TODO: future enhancement to look up sender domain against `Intermediary Target List` Sheet (`18zzE1y-BU1xuD-y0BOmEl8GtJ4I-iclSuBqAi0q3pkk`).**

### DIRECT Detection
- Addressed specifically to Kay
- References G&B, search fund, or prior conversation
- Personalized content about a specific company
- Action: Flag for review, classify by source (intermediary, owner, advisor)

### NEWSLETTER Detection
- Subscription/mailing list headers
- Known newsletter senders
- Action: Scan for niche signals only, then archive
- **BUT FIRST — check for deal-listing content (see DEAL_NEWSLETTER below).** Many newsletters carry deal listings inside an otherwise-newsletter format; missing those is the failure mode codified 2026-05-26 (Helen Guo SMB Deal Hunter 5/26 Market Watch issue had 5 explicit listings; the parser saw the mid-email Member Spotlight case study and labeled the whole email "content marketing — no listings". Wrong.)

### DEAL_NEWSLETTER Detection (subtype — added 2026-05-26)

A newsletter that contains structured deal listings inside the body. These get per-listing extraction (Section 7) regardless of their NEWSLETTER classification. Two-signal detection (either alone is sufficient):

**Signal 1 — known deal-newsletter senders:**
- `helenguo.com` / `smbdealhunter.com` / sender "Helen Guo" / subject contains "SMB Deal Hunter" or "Market Watch" — ALWAYS treat as deal-newsletter, extract every numbered listing.
- `acquiringminds.co` / sender "Will Smith" / Acquiring Minds — deal-newsletter when the body has numbered listings + $ amounts (their pure-content episodes have neither).
- `flippa.com` marketplace digests / subject contains "Flippa" + "this week" / "newly listed" / "featured" — marketplace deal-newsletter, extract.
- `bizbuysell.com` email alerts — marketplace deal-newsletter, extract.
- Walker Deibel newsletter — deal-newsletter only when body has numbered listings + $ amounts (most of his sends are educational).
- Empire Flippers / Quiet Light / Synergy / Viking Mergers email digests — broker deal-newsletter, extract.
- This list extends over time. When a new deal-newsletter sender is identified, add it here.

**Signal 2 — body structure pattern (catches unknown deal-newsletter senders):**
- Body contains a section header like `In Today's Issue` / `New Deals` / `This Week's Listings` / `Newly Listed` / `Featured Businesses` AND
- ≥2 numbered listing items (`#1:`, `#2:`, ... OR `1/`, `2/`, ... OR similar enumeration) AND
- ≥1 of the numbered items has structured deal-data (asking price, EBITDA, revenue, or location)

If EITHER signal fires → treat as DEAL_NEWSLETTER → fire `<broker_blast_listing_extraction>` for the listings section.

**Forbidden — the 2026-05-26 case-study coexistence bug:**
Do NOT classify the email as "content marketing" / "newsletter — no listings" when:
- The body contains a numbered listings section at the top AND a Member Spotlight / Community Wins / Case Study / Podcast Episode section elsewhere in the same email.
- Helen Guo SMB Deal Hunter editions consistently mix `In Today's Issue` (listings) + Member Spotlight (case study) + Recent Podcast Episode in a single email. The case-study section is commentary, not a re-classification signal. **Extract from the listings section regardless of what other sections exist.**

Same rule for any deal-newsletter: presence of an unrelated case-study/spotlight/podcast section does NOT override deal-listing classification when the listings section is also present.

**Idempotency:** same Gmail message ID + listing ordinal dedup as `<broker_blast_listing_extraction>`. A re-run on the same DEAL_NEWSLETTER email does not duplicate rows.

</deal_flow_classification>

<broker_blast_listing_extraction>
## Broker BLAST Listing Extraction (per-deal body parsing)

**Why this exists:** Broker BLAST emails (Lisa @ Generational Equity, Viking, Helen Guo SMB Deal Hunter, Sunbelt, Transworld, etc.) typically contain MULTIPLE distinct listings inside a single email body. Counting one BLAST as one entry undercounts true broker deal-flow volume. The 2026-05-04 broker ingestion 30-day audit (`brain/outputs/2026-05-04-broker-ingestion-audit-30day.md`) flagged this gap; the 2026-05-26 Helen Guo Market Watch miss expanded the trigger set to deal-newsletters too. Future audits read the per-listing rows below directly.

**When to trigger (ANY one is sufficient):**
- (a) Email classified BLAST AND body contains any broker-signal keyword: "for sale", "exclusive listing", "asking price", "we represent", "new listing", "now available", "teaser", "project [codename]"
- (b) Email classified DEAL_NEWSLETTER per `<deal_flow_classification>` Signal 1 (known sender — Helen Guo / Acquiring Minds / Flippa / BizBuySell / Walker Deibel with listings / Empire Flippers / Quiet Light / Synergy / Viking Mergers digests) OR Signal 2 (body structure: section header + ≥2 numbered listings + structured deal-data)
- (c) Email classified NEWSLETTER but body contains a numbered listings section matching DEAL_NEWSLETTER Signal 2 — fire extraction; the NEWSLETTER label was over-broad

The trigger fires INDEPENDENTLY of overall email classification. A NEWSLETTER with listings still produces Section-7 rows. A BLAST with no listings produces zero rows. Classification and extraction are decoupled.

**Forbidden patterns:**
1. Do not collapse multi-listing blasts/newsletters into single rows. Each listing in the body gets its own row.
2. Do not skip extraction because a Member Spotlight / Community Wins / Case Study / Podcast Episode section exists elsewhere in the same email. The listings section is the signal; other sections are noise. Codified 2026-05-26 after Helen Guo SMB Deal Hunter 5/26 Market Watch issue (5 listings) was mis-classified "content marketing" because the parser focused on the mid-email Chelsea case study.
3. Do not treat the Flippa/BizBuySell `feedback_marketplace_vs_broker_distinction` doctrine as a parser-suppression rule. That doctrine says: do not classify Flippa as a sell-side intermediary. It does NOT say: do not extract listings from Flippa's email digests. Marketplace digests contain real for-sale listings; extract them.

**Per-listing extraction fields:**
- `source` — sender name + firm (e.g., "Helen Guo, SMB Deal Hunter" / "Lisa McKnight, Generational Equity" / "Flippa Marketplace")
- `headline` — deal name, project codename, or one-line description from the body
- `geo` — state if disclosed, else "undisclosed"
- `revenue` — if disclosed (raw string with units, e.g., "$8.2M" / "$4.36M")
- `ebitda` — if disclosed
- `margin` — if disclosed
- `industry` — if disclosed (NAICS or plain-English category)
- `flag_reason` — one of: `multi-listing` (body contained 2+ listings), `single-listing-blast` (body contained exactly 1 listing), `unknown-broker-signal` (body matched signal keywords; known-sender list extension candidate), `deal-newsletter-known-sender` (Signal-1 trigger), `deal-newsletter-pattern` (Signal-2 trigger — header + numbered + $ amounts)

**Idempotency:** Use Gmail message ID + listing ordinal (1-indexed within body) as the dedup key. Re-runs on the same message must not duplicate rows.

**Output destination:** Section 7 of the email-scan-results artifact. See `<artifact>` schema below.

**Section-2 reconciliation:** when extraction fires on a NEWSLETTER-classified or DEAL_NEWSLETTER-classified email, Section 2 counts the email under NEWSLETTER (no double-count); Section 7 carries the per-listing rows. Section 7 row count is the deal-flow KPI, not Section 2 BLAST count.
</broker_blast_listing_extraction>

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

**4-step automatic execution (CRITICAL: all four steps execute in-session, not deferred):**
1. File the PDFs from email to `BOOKKEEPING / MONTHLY REPORTING / {MONTH YEAR}` Drive subfolder (folder ID `1Z__A8AXWBCwQN7x1nK2fqaqhVKlJBJOb`). Create the month subfolder if it doesn't exist.
2. Create inbox item at `brain/inbox/{date}-{month}-management-report-budget-trigger.md` with `urgency: trigger` and tags `topic/bookkeeper-pl-received`, `trigger/budget-manager-monthly`. Filename pattern is load-bearing: the wrapper-level validator matches on it.
3. **Invoke `budget-manager monthly` IN THIS SESSION.** Pass `period: {YYYY-MM}` for the detected month. Wait for budget-manager's 3-subagent pipeline to complete. Forbidden pattern: creating the inbox item and stopping. That is the March 2026 silent-skip failure (inbox landed 2026-04-29, no budget-manager output 13 days later).
4. Emit the literal string `BOOKKEEPER-PL-CHAIN: invoked budget-manager monthly for period {YYYY-MM}` to stdout so the wrapper validator can confirm the chain fired. If budget-manager failed, emit `BOOKKEEPER-PL-CHAIN: FAILED for period {YYYY-MM} reason: {brief}` instead, surface the failure in the artifact's Actionable Items section, and continue.
5. The briefing surfaces budget-manager OUTPUT (variance flags, runway change, action items), NOT the trigger event.

**Validation (must pass before next-step Slack):**
- PDFs in Drive with size > 0
- Inbox item written
- budget-manager invoked successfully (Phase 1 Document Ingester returned non-empty JSON)
- Stdout log contains `BOOKKEEPER-PL-CHAIN:` marker for this period

**No Attio write.** Bookkeeper reports do not flow into Active Deals or any Attio list.

**No Decisions bucket surface.** The morning briefing should show this trigger only as a `🟢 Wired` line item under System Status, never as a 🔴/🟡 Decision asking for Kay's approval.
</bookkeeper_pl_auto_trigger>

<auto_ack_drafts>
## Auto-Acknowledgment Drafts (Known Broker + Attachment)

**Purpose:** When a broker emails Kay with an NDA or CIM attached, auto-CREATE a Gmail draft reply so Kay sends it in <5 min after review. Drafts are NEVER auto-sent. Reference `feedback_kay_handles_all_replies` and `feedback_day_aware_signoffs`.

### Trigger conditions

1. **Attachment classification (one of):**
   - **NDA-like:** PDF attachment whose filename contains any of `NDA`, `non-disclosure`, `confidentiality agreement`, `CA`. Or body subject contains those tokens with a single PDF attached.
   - **CIM-like:** PDF attachment whose filename contains any of `CIM`, `Confidential Information Memorandum`, `offering-memorandum`, `teaser`. OR PDF >= 5 pages with structured financials in body (CIM heuristic, same signal as `<cim_auto_trigger>`).
   - If both classifications match (rare), prefer CIM template.

### Templates (placeholders filled at render time by orchestrator)

```
NDA-RECEIVED TEMPLATE
Subject: Re: {{original_subject}}
Body:
Got it, signing now and will send back today.
{{day_of_week_close}}
{{signer_first_name}}
```

```
CIM-RECEIVED TEMPLATE
Subject: Re: {{original_subject}}
Body:
Got it, reviewing this week and will follow up with my read by {{end_of_week_date}}.
{{day_of_week_close}}
{{signer_first_name}}
```

### Render rules

- `{{signer_first_name}}` = `Kay`.
- `{{day_of_week_close}}` matches the SEND day (per `feedback_day_aware_signoffs`). Friday = "Have a great weekend!"; Mon-Thu = "Best,"; Sunday drafts schedule for Monday so close = "Best,". Never echo the draft-day if it differs from the intended send day.
- `{{end_of_week_date}}` = upcoming Friday rendered as `Mmm D` (e.g., `May 8`). If today IS Friday, use the following Friday.
- `{{original_subject}}` = the inbound email's exact Subject line. If it already starts with `Re:`, do not double-prefix.
- No em dashes anywhere. Plain text body. No blockquote, no code fence, no leading bar.

### Draft creation

Drafts go into Gmail via `~/.local/bin/gmail-draft.sh`. NEVER call `gog gmail send` for these. If the wrapper is missing, fall back to `gog gmail draft create` directly with the same payload. DO NOT skip silently.

Pass:
- `--to` (broker email)
- `--subject` (rendered with `Re:` prefix logic)
- `--body` (rendered template, plain text)
- `--in-reply-to` (the inbound message ID, so Gmail threads it)

### Forbidden patterns

- **Auto-send broker NDA/CIM acknowledgment without Kay review.** This NEVER fires. Drafts are CREATED only. Per `feedback_kay_handles_all_replies` Kay sends every reply herself.
- Use any non-Gmail drafting tool or send-capable command.

### Logging

Each auto-draft created emits one row into the artifact's `Auto-Drafts Created` section (see `<artifact>` schema below).
</auto_ack_drafts>

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

**REST fallback (preferred — no MCP, no OAuth, no reconnect):**
```bash
source /home/ubuntu/projects/Sapling/scripts/op-env.sh
granola-api since "$(date -u -d 'yesterday' +%Y-%m-%dT00:00:00Z)"   # list updated notes
granola-api get-note <note_id>                                       # full transcript + summary
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

### Required Sections (all 8 must be present, even if "None")

1. **Actionable Items Created** — inbox items created from emails (with source_ref)
2. **Deal Flow Classified** — DIRECT/BLAST/NEWSLETTER counts
3. **Draft Status** — sent vs unsent drafts with age
4. **Introductions Detected** — new intros found in email
5. **Niche Signals** — passive niche observations from email/Granola
6. **In-Person Meetings Today** — from calendar, for Granola reminder
7. **Broker BLAST Listings (per-deal extraction)** — one row per listing parsed from the body of any broker BLAST or broker-signal email. Triggered per `<broker_blast_listing_extraction>`. Render as a markdown table with columns: `source | headline | geo | revenue | ebitda | margin | industry | flag_reason | gmail_msg_id | listing_ordinal`. If zero broker BLASTs landed today, write "None" under the heading. Forbidden pattern: do not collapse multi-listing blasts into single rows; each listing gets its own row.
8. **Auto-Drafts Created** — one row per auto-acknowledgment Gmail draft created via `<auto_ack_drafts>`. Render as a markdown table with columns: `timestamp | broker_name | broker_email | attachment_type (NDA / CIM) | original_subject | draft_gmail_link`. If zero auto-drafts fired today, write "None" under the heading. Drafts are CREATED only, never sent — Kay reviews and sends manually per `feedback_kay_handles_all_replies`.

### Validation
- File exists and is non-empty
- All 8 section headers present
- Each section populated or explicitly marked "None"
- Section 7 rows: every email whose body matches a `<broker_blast_listing_extraction>` trigger (BLAST + broker-signal keyword, OR DEAL_NEWSLETTER known-sender, OR DEAL_NEWSLETTER body-pattern, OR NEWSLETTER-with-listings) has at least one row in section 7. A NEWSLETTER-classified email producing zero section-7 rows is valid ONLY when the body has no numbered listings + no $ amounts in deal-data structure; if either is present, extraction must have fired.
- Section 8 rows: every inbound email that triggered `<auto_ack_drafts>` (NDA/CIM attachment) has exactly one row, and the corresponding Gmail draft exists (link resolves)
</artifact>

<stop_hooks>
## Stop Hooks

1. **Gmail ingestion** — actionable email count matches inbox files written
2. **Granola ingestion** — meeting count matches brain/calls/ files written
3. **CIM auto-trigger** — for every CIM: folder exists, file uploaded (size > 0), inbox item written, deal-eval invoked
4. **Active Deal Fast-Path** — for every fast-path item: file in Drive, Attio updated
5. **Email-scan-results artifact** — file exists, non-empty, all 8 sections present (section 7 covers Broker BLAST per-listing extraction; section 8 covers Auto-Drafts Created)
6. **Slack notifications** — webhook returned 200 OK for all pings
7. **ACTIVE DEALS folder sync** — every Drive subfolder has matching Attio entry
8. **Broker BLAST + Deal-Newsletter per-listing extraction** — every email matching ANY `<broker_blast_listing_extraction>` trigger (BLAST + broker-signal keyword, OR DEAL_NEWSLETTER known-sender, OR DEAL_NEWSLETTER body-pattern, OR NEWSLETTER carrying numbered listings) has a corresponding row (or rows, for multi-listing) in section 7. Forbidden patterns: (a) collapsing multi-listing blasts into single rows; (b) skipping extraction because a Member Spotlight / Case Study / Podcast section coexists with the listings section (2026-05-26 Helen Guo precedent); (c) using `feedback_marketplace_vs_broker_distinction` as a parser-suppression rule (it governs intermediary classification, not listing extraction).
9. **Auto-Acknowledgment Drafts** — every inbound email matching `<auto_ack_drafts>` triggers (NDA/CIM attachment) produced exactly one Gmail draft AND one row in section 8. Forbidden pattern: auto-sending the draft. Drafts are CREATED only.
10. **Bookkeeper P&L chain** — for every bookkeeper P&L detection this run: PDFs filed to Drive, inbox item written matching the canonical filename pattern, `budget-manager monthly` invoked in-session, `BOOKKEEPER-PL-CHAIN:` marker emitted to stdout. Forbidden pattern: creating the inbox item and exiting without invoking budget-manager (the March 2026 silent-skip failure mode). The wrapper validator (`scripts/validate_email_intelligence_integrity.py`) gates exit code on the marker.
</stop_hooks>

<success_criteria>
## Success Criteria

- [ ] All inbound emails classified (DIRECT/BLAST/NEWSLETTER)
- [ ] CIM/NDA/LOI detected and processed immediately
- [ ] Active deal emails filed to correct Drive subfolders
- [ ] Introductions detected and entities created
- [ ] Granola transcripts ingested
- [ ] email-scan-results artifact written with all 8 sections
- [ ] Broker BLAST per-listing extraction emitted for every triggering BLAST (multi-listing blasts decomposed into one row per listing)
- [ ] Auto-acknowledgment Gmail drafts CREATED (never sent) for every NDA/CIM inbound, with one row in section 8 per draft
- [ ] No missed deal signals
</success_criteria>
