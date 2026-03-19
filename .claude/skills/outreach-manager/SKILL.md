---
name: outreach-manager
description: "Owns all outreach across all channels and funnels. Two subagents: cold outreach (from target-discovery) and conference outreach (from conference-discovery). Attio dedup catches crossover."
user_invocable: true
context_budget:
  skill_md: 3000
  max_references: 2
  sub_agent_limit: 2000
---

<objective>
Own all outreach. Every email, call, DM, and follow-up flows through this skill.

This skill receives targets from two upstream skills and runs personalized outreach via two subagents. A shared dedup layer prevents any person from receiving overlapping outreach from both funnels.

**Inputs from other skills:**
- **skill/target-discovery** — approved cold targets with enriched contact info and research context
- **skill/conference-discovery** — conference attendee targets (pre-conference) and conversation data (post-conference)

**Outputs to other skills:**
- Outreach status updates → skill/pipeline-manager (stage progression based on responses)
- JJ's call outcomes feed back into pipeline-manager
- Weekly outreach metrics → skill/weekly-tracker

Two subagents:
1. **Cold Outreach** — sequenced multi-channel cadence for Linkt-sourced targets
2. **Conference Outreach** — pre-conference emails and post-conference follow-ups
</objective>

<dedup_layer>
## Attio Dedup Layer

Before either subagent drafts outreach, check Attio Active Deals:

1. **Does this person already exist in the pipeline?** If yes, check their current stage and last outreach date. Don't double-contact someone already in an active cadence.
2. **Is this person receiving outreach from the other subagent?** If a conference target is also in the cold outreach queue (or vice versa), the conference outreach subagent takes priority — the conference framing ("I'll be at your booth Thursday" or "Great meeting you yesterday") is always stronger than cold email.
3. **Has this person been contacted in the last 30 days?** If yes, skip unless there's a new context (conference, referral, signal change).

The dedup check runs once when targets are received, before any drafting begins.

**How outreach-manager knows Kay sent the email:**
Check Superhuman via the `superhuman` MCP server for sent status on drafted emails. If the draft was sent (no longer in drafts folder), the email was sent. Update Attio accordingly.
</dedup_layer>

<cold_outreach>
## Subagent 1: Cold Outreach

Handles outreach for targets sourced from skill/target-discovery (Linkt + free sources).

### Outreach Cadence (Per Target)

| Day | Channel | Who | Action |
|-----|---------|-----|--------|
| Day 1 | Email | Kay (via Superhuman draft) | Personalized cold email |
| Day 3 | Phone | JJ | Confirmation call — "wanted to make sure you received Kay's note" |
| Day 5-6 | Email | Kay (via Superhuman draft) | Follow-up email if no response — short, one line |
| Day 8-10 | LinkedIn DM | Kay (manually) | High-value targets only, if email + call didn't land |

After Day 10 with no response, move to nurture cadence (pipeline-manager handles from here).

**Why this sequence:** The email establishes who Kay is and gives the owner time to check LinkedIn (where Kay's Chanel/luxury background closes the credibility gap). JJ's call 2 days later references the email, making it a warm confirmation rather than a cold call. The follow-up email is a lightweight bump. LinkedIn DM is the escalation reserved for high-fit targets.

### Day 1: Kay's Email

Every target gets a deeply personalized email. At 4-6 targets per day, there's no reason for templates.

**Voice:** Kay's calibrated outreach voice (see memory: user_outreach_voice.md)
**Rules:**
- No em dashes. Periods, commas, line breaks.
- Conversational, warm, direct
- Reference something specific about the owner or business (from deep research)
- Never mention "I want to buy your company" — frame as exploring the industry, learning from experts
- Keep it short (3-5 sentences)
- Propose a specific next step (phone call, coffee if local)

**Structure:**
```
Subject: {Something specific to their business}

Hi {first name},

{1 sentence showing you researched their specific business}.
{1 sentence connecting your background to their world — why you're credible}.
{1 sentence proposing a conversation — learning about the industry, not pitching}.

Would love to connect for 15 minutes.

Kay Schneider
Greenwich & Barrow
```

Draft in Superhuman via the `superhuman` MCP server using the `superhuman_draft` tool with `--account kay.s@greenwichandbarrow.com`. This creates native Superhuman drafts that appear in Kay's drafts folder. Do NOT use `gog gmail drafts create` — Gmail API drafts do not sync to Superhuman. Kay reviews and sends from Superhuman.

**Attio State Machine:**
- Outreach-manager monitors Attio for targets at "Identified" stage — these are Kay-approved targets ready for outreach
- When outreach-manager drafts the Day 1 email → target stays at "Identified" (draft only, not sent yet)
- When Kay sends the email from Superhuman → outreach-manager moves Attio to "Contacted"
- Pipeline-manager then picks up the "Contacted" status and notifies JJ with Day 3 call date
- After Day 10 with no response → pipeline-manager moves to nurture cadence

### Day 3: JJ's Confirmation Call

JJ calls to confirm receipt of Kay's email. This is NOT a cold call — it's a warm follow-up.

**Script:**
```
Hi, this is JJ calling on behalf of Kay Schneider at Greenwich & Barrow.
Kay sent {owner name} a note a couple days ago and I just wanted to make
sure it came through. She's been researching the {niche} space and would
love to connect briefly with {owner name} about their experience.
Would {owner name} have 15 minutes for a quick call?
```

**Call columns** — JJ works directly from the niche sprint master sheet ("{Niche} - Target List" in LINKT TARGET LISTS folder). No separate call list. JJ fills in columns Q-T on the Active tab:
- Col Q: Call Status (dropdown)
- Col R: Call Date
- Col S: Call Notes
- Col T: Owner Sentiment (dropdown)

See target-discovery/references/drive-locations.md for full column layout.

### Day 5-6: Follow-Up Email

If no response to email or call, Kay sends a short follow-up. One or two sentences max.

```
Hi {first name},

Just circling back on my note from earlier this week. Would love to find a time to connect.

Kay
```

Draft in Superhuman. Kay reviews and sends.

### Day 8-10: LinkedIn DM (High-Value Only)

Reserved for targets that are a strong fit but haven't responded to email or phone. Kay sends personally from her LinkedIn. Claude drafts the message, Kay copies and sends.

Not every target gets this. Only use for owners where the company is a clear buy-box match and worth the extra touch.

### Warm Intro Outreach (from pipeline-manager intro detection)

When pipeline-manager detects an inbound introduction via email, the target enters the outreach flow differently than cold targets.

**Warm intro email structure:**
```
Subject: {Introducer's first name} suggested I reach out

Hi {first name},

{Introducer} mentioned we should connect. {1 sentence about why — what the introducer said or the context of the intro}.
{1 sentence about G&B and why Kay is interested in their space}.

Would love to find 15 minutes to chat.

Kay Schneider
Greenwich & Barrow
```

**Thank-you to introducer:**
```
Subject: Thank you for the intro

Hi {introducer first name},

Really appreciate you connecting me with {person}. I reached out to them today.

Kay
```

**Warm intro cadence (no JJ call):**
| Day | Channel | Action |
|-----|---------|--------|
| Day 1 | Email (Superhuman) | Warm intro email + thank-you to introducer |
| Day 5-6 | Email (Superhuman) | Follow-up if no response |
| Day 8-10 | LinkedIn DM (Kay) | High-value only |

No Day 3 JJ confirmation call — the introduction already warmed the connection. JJ's time is better spent on cold targets.

Draft both emails (intro response + thank-you) in Superhuman via the `superhuman` MCP server using `superhuman_draft` with `--account kay.s@greenwichandbarrow.com`.
</cold_outreach>

<conference_outreach>
## Subagent 2: Conference Outreach

Handles all outreach related to conferences — pre-conference emails to attendees and post-conference follow-ups.

### Pre-Conference Emails (T-minus 1 week)

Receives scored target list from conference-discovery. For each approved target:

**Voice:** Kay's calibrated outreach voice (see memory: user_outreach_voice.md)
**Rules:**
- No em dashes. Use periods, commas, line breaks.
- Conversational, warm, direct
- Reference the specific conference by name
- Mention Kay will be attending and would love to connect briefly
- Keep it short (3-4 sentences max)
- Propose a specific ask: "Would love to stop by your booth" or "Grab a coffee during the break"

**Structure:**
```
Subject: {Conference Name} — quick hello

Hi {first name},

{1 sentence about finding them on the exhibitor list / their company}.
{1 sentence about why Kay is interested — niche connection, not "I want to buy your company"}.
{1 sentence proposing a brief connection at the conference}.

Looking forward to it.

Kay Schneider
Greenwich & Barrow
```

Draft in Superhuman via the `superhuman` MCP server using the `superhuman_draft` tool with `--account kay.s@greenwichandbarrow.com`. Kay reviews and sends from Superhuman.

Create Motion task: "Review and send {conference} pre-outreach emails" with due date T-minus 5 days.

### Post-Conference Follow-Ups (Next Morning)

Receives conversation data from conference-discovery (Granola transcripts + Kay's notes).

For each person Kay spoke with:
1. Draft personalized follow-up email referencing specific conversation points
2. Use Kay's voice, no em dashes
3. Propose a next step (call, meeting, send info)
4. Short and specific — reference something from the actual conversation

Draft in Superhuman. Present all drafts during morning pipeline-manager review. Kay approves and sends.
</conference_outreach>

<essential_principles>
## Principles

### Volume & Cadence
- 4-6 cold targets per day (funds that acquired averaged 4, not 9)
- Quality over quantity — deep research on each target, personalized outreach
- Sequenced multi-channel: email Day 1 → JJ confirmation call Day 3 → follow-up email Day 5-6 → LinkedIn DM Day 8-10 (high-value only)
- Conference targets excluded from cold cadence (conference outreach subagent owns that relationship)

### Channel Rules
- **Email:** Always via Superhuman drafts. Never Gmail API.
- **Phone:** JJ's call sheet in Google Sheets. JJ logs outcomes.
- **LinkedIn DM:** Kay sends manually. Claude drafts. High-value escalation only.
- **All channels:** Same voice, same framing (curiosity, not acquisition pitch).

### Team Roles (for this skill only)
- **Claude:** Deep research per target, draft all emails, build call list, track cadence timing
- **Kay:** Review/send emails, send LinkedIn DMs, take Stage 1 calls
- **JJ:** Confirmation calls from sheet, log outcomes

### Coordination with Other Skills
- **pipeline-manager:** After Day 10 with no response, pipeline-manager takes over with nurture cadence. Outreach-manager does not re-contact nurture targets unless pipeline-manager flags them.
- **weekly-tracker:** Outreach metrics (emails sent, calls made, response rates) feed into the weekly activity tracker.
</essential_principles>

<validation>
## Validation / Stop Hooks

Before reporting completion, run these checks in order. If any check fails, do NOT send the Slack notification. Report the failure and fix it before retrying.

### 1. Superhuman Draft Validation
Confirm every email draft was created via the `superhuman` MCP server (`superhuman_draft` tool). For each target, verify the tool returned a success response. If any draft creation failed or fell back to Gmail API, flag it — drafts must exist in Superhuman, not Gmail.

### 2. Call Sheet Validation
For every new cold target added this session, verify JJ's call columns in the Linkt target sheet are populated:
- **Company** — non-empty
- **Owner Name** — non-empty
- **Phone** — non-empty
- **Call Date** — Day 3 date populated

Missing fields mean JJ can't execute. Fix before proceeding.

### 3. Dedup Validation
Confirm Attio was checked before any drafting began. No person should have outreach queued from both the cold outreach and conference outreach subagents. If a person appears in both queues, conference outreach takes priority and the cold draft must be removed.

### 4. Cadence Tracking
Every Day 1 email must have a corresponding Day 3 call entry scheduled in JJ's call sheet. Cross-reference the list of drafted emails against the call sheet. Any email without a matching Day 3 entry is a gap — add it before proceeding.

### 5. Slack Notification (Only After Validation Passes)
Only send once checks 1-4 all pass:
```bash
curl -s -X POST "SLACK_WEBHOOK_REDACTED" \
  -H "Content-Type: application/json" \
  -d '{"text":"Outreach ready — {n} email drafts in Superhuman, {n} targets added to JJ call list. Review and send when ready."}'
```
Replace `{n}` with actual counts. If validation failed, report the failure details instead — never send the "ready" notification when outreach is incomplete.
</validation>

<success_criteria>
## Success Criteria

### Daily
- [ ] Email drafts ready for Kay's review (cold + any conference follow-ups)
- [ ] JJ's call sheet updated with Day 3 confirmation calls
- [ ] No duplicate outreach across funnels (dedup layer verified)

### Weekly
- [ ] 20-30 owners contacted (email + phone combined across both funnels)
- [ ] Pre-conference emails sent for upcoming conferences
- [ ] Post-conference follow-ups drafted within 24 hours
- [ ] Outreach metrics available for weekly tracker
</success_criteria>
