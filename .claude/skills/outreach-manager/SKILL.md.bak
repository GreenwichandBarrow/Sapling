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

Three subagents:
1. **Cold Outreach** — sequenced multi-channel cadence for Linkt-sourced targets
2. **Conference Outreach** — pre-conference emails and post-conference follow-ups
3. **Intermediary Outreach** — relationship-building with association heads, brokers, river guides
</objective>

<dedup_layer>
## Attio Dedup Layer

Before either subagent drafts outreach, run these checks:

1. **Does this person already exist in the pipeline?** If yes, check their current stage and last outreach date. Don't double-contact someone already in an active cadence.
2. **Is this person receiving outreach from the other subagent?** If a conference target is also in the cold outreach queue (or vice versa), the conference outreach subagent takes priority — the conference framing ("I'll be at your booth Thursday" or "Great meeting you yesterday") is always stronger than cold email.
3. **Has this person been contacted in the last 30 days?** If yes, skip unless there's a new context (conference, referral, signal change).
4. **Warm intro check (CRITICAL).** Before cold outreach, search Attio People records for the target owner AND anyone at their company. If Kay has an existing connection (LinkedIn import, prior email, meeting), flag as "Warm Intro" on the target sheet. Warm intro targets skip cold email + JJ call entirely — instead, draft a warm intro request email for Kay referencing the mutual connection. See Warm Intro Outreach section below.

The dedup + warm intro check runs once when targets are received, before any drafting begins.

**Delivery tracking note:** Pipeline-manager tracks Superhuman draft send status and updates Attio stages. Outreach-manager focuses on drafting only.
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

**Business days only.** All day counts are business days (Mon-Fri). No emails drafted for weekends, no JJ calls scheduled on weekends. If Day 1 is Thursday, Day 3 is the following Monday, not Saturday.

**Why this sequence:** The email establishes who Kay is and gives the owner time to check LinkedIn (where Kay's Chanel/luxury background closes the credibility gap). JJ's call 2 days later references the email, making it a warm confirmation rather than a cold call. The follow-up email is a lightweight bump. LinkedIn DM is the escalation reserved for high-fit targets.

### Target Sheet Columns (added by outreach-manager)

When outreach-manager receives approved targets, it writes two new columns on the niche sprint target sheet:

- **Col X: Warm Intro** — "Warm - {connection name}" if a mutual connection is found in Attio, blank if cold. Agent checks Attio People records for the target owner and anyone at their company. A match means Kay knows someone there — route to warm intro path, NOT cold outreach.
- **Col Y: Outreach Stage** — Tracks where each target is in the sequence: `Email Drafted` → `Email Sent` → `JJ Called` → `Follow-Up Drafted` → `Follow-Up Sent` → `LinkedIn DM` → `Nurture`. Updated as each step completes.

**JJ trigger rule:** JJ's call sheet only includes targets where Col X (Warm Intro) is BLANK. Warm intro targets never go to JJ — Kay handles them personally.

### Day 1: Kay's Email

Every target gets a deeply personalized email. At 4-6 targets per day, there's no reason for templates.

**Voice:** Kay's calibrated outreach voice (see memory: user_outreach_voice.md)

### A/B Test: Two Email Variants (Active Experiment)

Outreach-manager alternates between two variants on every cold email. Targets are assigned **alternating** — odd-numbered approved cold targets get Variant A, even get Variant B. Log the variant in **Col Z ("Email Approach")** on the target sheet as `Learning` or `Direct`. Warm intro targets are excluded from this experiment — Col Z stays blank for warm intros.

Kay knows about this test and will generally stick to the assigned variant when reviewing drafts in Superhuman. She may tweak wording but will preserve the core positioning.

**Learning (curiosity-first, loose approach)**
```
Subject: Quick question about {company}

Hi {first name},

{warm opener}. I came across {company} while looking into {niche} and was impressed by {something specific they built}. {Optional: real connection point — shared location, school, mutual contact}.

I've been looking to get into the {niche} space and trying to learn as much as I can. Given your expertise I'd welcome the chance to hear your perspective.

If you're open, I'd love to find a short time to connect.

Very best,
Kay
```

**Direct (transparent intent)**
```
Subject: {niche} — quick introduction

Hi {first name},

{warm opener}. I came across {company} while looking into {niche} and was impressed by {something specific they built}.

I'm a well-capitalized buyer looking to acquire a {niche} business and wondered if you or someone you know in the industry might be open to a conversation. I'm trying to learn as much as I can about the space.

If you're open, I'd love to find a short time to connect.

Very best,
Kay
```

**What we're testing:** Does transparency about acquisition intent help or hurt response rates? Variant A positions Kay as a curious learner. Variant B is upfront about being a buyer but uses "you or someone you know" to take pressure off.

**Tracking:** Col Z on the target sheet. Calibration agent analyzes after 20-30 sends (roughly 1 month at 4-6/day). Metrics: response rate, time to response, tone of response (warm vs defensive), conversion to call.

**HARD RULES (apply to BOTH variants):**
- The email is about THEM, not Kay or G&B. Never mention Greenwich & Barrow. Never describe what Kay does. LinkedIn handles credibility (they'll check).
- NEVER reference revenue, employee count, or financial metrics. Could be wrong, and it signals you care about money not legacy.
- NEVER call G&B a "fund." Sounds like PE and kills trust.
- NEVER reveal thesis/growth strategy (underpenetration, consolidation, market size).
- Don't make claims you can't source. Every line must be grounded in real research.
- No em dashes. Periods, commas, line breaks.
- Lead with curiosity about what they've built, even in Variant B.

### Email Verification (Non-Linkt Targets Only)

Before drafting, verify email addresses for targets where **Col A (Source) is NOT "Linkt."** Linkt does its own enrichment and verification — skip this step for Linkt-sourced targets.

```bash
source .env && curl -s "https://api.apollo.io/v1/people/match" \
  -H "Content-Type: application/json" \
  -H "X-Api-Key: $APOLLO_API_KEY" \
  -d '{"first_name":"{first}","last_name":"{last}","organization_name":"{company}","domain":"{domain}"}'
```

**Gate logic based on `email_status`:**
- `verified` → proceed to draft
- `guessed` / `unavailable` / `bounced` → do NOT draft. Write status to Col W (Email Verified) on target sheet. Notify Kay: "{owner} at {company} — email not verified ({status}). Skip or find alternate?"
- `pending` → retry once after 5 minutes. If still pending, flag.

**Why:** Bounced emails burn Kay's sender domain reputation. Linkt validates its own data. Non-Linkt sources (association directories, conference lists, web scraping) need verification.

### Draft Creation

Draft in Superhuman via the wrapper script (NOT the MCP tool — it uses Gmail API which creates invisible drafts). Use Bash:
```bash
superhuman-draft.sh --to "{email}" --subject "{subject}" --body "{body}"
```
This creates native Superhuman drafts via CDP. Kay reviews and sends from Superhuman. Sign off "Very best, Kay" only — signature is built in.

**Attio State Machine:**

Outreach-manager is the only skill that writes to Attio for targets. The sequence:

1. Read the target sheet, find rows where Col O = "Approve" that weren't approved in the prior run (new approvals)
2. For non-Linkt targets, verify email via Apollo API. Only proceed if `verified`.
3. For each verified approved target, search Attio for the person AND company:
   - **If found** → someone Kay already knows. Flag as warm intro (Col X), skip cold outreach. This is both the dedup check AND the warm intro check in one step.
   - **If not found** → create the company + person in Attio, add company to Active Deals at "Identified" stage. Proceed with cold outreach.
3. When outreach-manager drafts the Day 1 email → target stays at "Identified" (draft only, not sent yet)
4. Pipeline-manager detects when Kay sends the email from Superhuman and moves Attio to "Contacted"
5. Pipeline-manager then notifies JJ with Day 3 call date
6. After Day 10 with no response → pipeline-manager moves to nurture cadence

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

**If the owner wants to schedule a call with Kay:** JJ books a time directly with the owner on the phone, then emails Howie (barrie@greenwichandbarrow.com) with: owner name, owner email, and agreed time. Howie creates the calendar invite and sends it to the owner. Kay gets notified via calendar. JJ does NOT manage Kay's calendar directly.

**Call columns** — JJ works directly from the niche sprint master sheet ("{Niche} - Target List" in LINKT TARGET LISTS folder). No separate call list. JJ fills in columns Q-T on the Active tab:
- Col Q: Call Status (dropdown: Not Called, Connected, Voicemail, Callback, Not Interested, Wrong Number, Schedule Requested)
- Col R: Call Date
- Col S: Call Notes
- Col T: Owner Sentiment (dropdown)

**Feedback:** JJ is encouraged to share qualitative observations on Slack anytime (e.g., "owners in this niche seem skeptical" or "getting a lot of voicemails"). This is normal team communication, not a formal process.

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

### Warm Intro Handling

Two scenarios trigger a warm intro flag:

**A. Shared Attio connection found** (during outreach-manager warm intro check):
1. Write "Warm - {connection name}" in Col X on the target sheet
2. Slack ping to #operations: "Warm intro available: {target owner} at {company}. You're connected to {connection name}. Cold outreach paused for this target."
3. Cold outreach is PAUSED for this target — no email drafted, no JJ call scheduled
4. Kay decides approach case by case (ask for intro, mention connection directly, etc.)
5. Claude drafts per Kay's direction — no template, each is unique

**B. Inbound introduction via email** (pipeline-manager detects intro):
1. Pipeline-manager surfaces the intro in morning briefing
2. Kay decides approach
3. Claude drafts per Kay's direction
4. Thank-you to introducer is always drafted (short, same day)
5. No JJ call — warm intros are Kay-only

Warm intros are the exception, not the rule. Don't over-automate — just flag and pause.
</cold_outreach>

<conference_outreach>
## Subagent 2: Conference Outreach

Handles all outreach related to conferences — pre-conference emails to attendees and post-conference follow-ups.

### Conference Outreach Cadence

Outreach-manager pulls the conference date from the **Conference Pipeline Google Sheet** (Col A: Date of Conference, Sheet ID: `1bdf7xlcRjOTlVkuXA-HNGOQgjtDRmVN2RfDf9aUsDpY`). This is the source of truth for timing — no dependency on Kay's calendar. All timing works backwards from this date.

**Pre-Conference Cadence:**

| When | Action | Details |
|------|--------|---------|
| T-minus 14 days | First outreach email | Introduce Kay, mention the conference, propose connecting |
| T-minus 7 days | Follow-up (if no response) | Shorter, reference the first note, re-propose meeting |
| T-minus 3 days | Final nudge (high-value only) | Very short — "Looking forward to {conference} on Monday. Hope to connect." |
| Conference day | Kay meets in person | Granola captures conversations |
| T+1 day (morning) | Post-conference follow-up | References specific conversation from Granola |

### Pre-Conference Email — First Touch (T-minus 14 days)

**Voice:** Kay's calibrated outreach voice (see memory: user_outreach_voice.md)
**Rules:**
- No em dashes. Use periods, commas, line breaks.
- Conversational, warm, direct
- Reference the specific conference by name and date
- Mention Kay will be attending and would love to connect briefly
- Keep it short (3-4 sentences max)
- Propose a specific ask: "Would love to stop by your booth" or "Grab a coffee during the break"

**Structure:**
```
Subject: {Conference Name} — quick hello

Hi {first name},

{1 sentence about finding them on the exhibitor list / their company}.
{1 sentence about why Kay is interested — niche connection, not "I want to buy your company"}.
{1 sentence proposing a brief connection at the conference on {date}}.

Looking forward to it.

Kay Schneider
Greenwich & Barrow
```

Draft in Superhuman via the CLI (NOT the MCP tool — it uses Gmail API which creates invisible drafts). Use the same Bash command as cold outreach:
```bash
superhuman-draft.sh --to "{email}" --subject "{subject}" --body "{body}"
```
Kay reviews and sends from Superhuman.

Create Motion task: "Review and send {conference} pre-outreach emails" with due date T-minus 12 days.

### Pre-Conference Follow-Up (T-minus 7 days)

If no response to first touch:
```
Hi {first name},

Just circling back. I'll be at {Conference Name} next {day} and would love to connect briefly. Happy to stop by your booth or grab a quick coffee.

Kay
```

### Pre-Conference Final Nudge (T-minus 3 days, high-value targets only)

Only for top 3-5 targets Kay most wants to meet. Very short:
```
Hi {first name},

Looking forward to {Conference Name} on {day}. Hope to connect.

Kay
```

### Post-Conference Follow-Ups (T+1 Morning)

Receives conversation data from conference-discovery (Granola transcripts + Kay's notes).

For each person Kay spoke with:
1. Draft personalized follow-up email referencing specific conversation points from the booth
2. Use Kay's voice, no em dashes
3. Propose a specific next step (call, meeting, send info)
4. Short and specific — reference something from the actual conversation, not generic

For people Kay didn't get to meet but emailed pre-conference:
```
Hi {first name},

Sorry I missed you at {Conference Name}. Would still love to connect. Do you have 15 minutes this week?

Kay
```

Draft all in Superhuman. Present during morning pipeline-manager review. Kay approves and sends.
</conference_outreach>

<intermediary_outreach>
## Subagent 3: Intermediary Outreach

Handles outreach to force multipliers — people who know every owner in the niche and can open doors. These are NOT acquisition targets. They are relationship-building contacts who go into the Attio Intermediary Pipeline, not Active Deals.

### Who Are Intermediaries?
- **Association heads and executive directors** — run the industry organization, know every member
- **Conference organizers** — can introduce Kay to exhibitors and speakers
- **Industry brokers and M&A advisors** — actively seeing deal flow in the niche
- **CPAs and lawyers** — serve business owners in the niche, know who's thinking about succession
- **Industry consultants** — "river guides" who can walk Kay through the landscape
- **Fellow searchers** who've explored adjacent niches — can share intel and introductions

### Different Framing (Not a Pitch)

Intermediary outreach positions Kay as a **student of the industry**, not a buyer. The goal is to learn and build a relationship, not pitch an acquisition.

**Email structure:**
```
Subject: {Something specific to their role in the industry}

Hi {first name},

{1 sentence showing you know their role — association they run, event they organize, practice area}.
{1 sentence about Kay researching the {niche} space and wanting to learn from someone who sees the full landscape}.
{1 sentence proposing a conversation — positioned as learning, not deal-sourcing}.

Would love to find 20 minutes to hear your perspective.

Kay Schneider
Greenwich & Barrow
```

### Conference River Guide Play

When an upcoming conference is registered, identify the association head or organizer and reach out T-minus 3 weeks (before attendee outreach starts). The goal: meet them before the conference so they walk Kay through the room making introductions.

**Conference river guide cadence:**

| When | Action |
|------|--------|
| T-minus 21 days | First email to association head / organizer — "I'm attending {conference}, would love to connect beforehand" |
| T-minus 14 days | Follow-up if no response — "Would love 15 minutes before the conference" |
| T-minus 7 days | If connected, ask: "Who should I make sure to meet at {conference}?" |
| Conference day | Meet in person. They introduce Kay to key people. |
| T+1 day | Thank-you email + follow-up on any introductions they made |

### General Intermediary Cadence (non-conference)

For intermediaries identified through niche research, not tied to a specific conference:

| Day | Channel | Action |
|-----|---------|--------|
| Day 1 | Email (Superhuman) | Personalized "learning about the industry" email |
| Day 5 | Email (Superhuman) | Follow-up if no response |
| Day 10 | LinkedIn DM (Kay) | High-value only |

No JJ call. Intermediaries should only hear from Kay directly.

### Attio Pipeline

Intermediaries go into the **Intermediary Pipeline** in Attio, not Active Deals:
- New contact → "Identified"
- First email sent → "Contacted"
- Positive response → "Warmed"
- Actively sending introductions → "Actively Receiving Deal Flow"

### Sources for Intermediary Discovery

- **Niche intelligence** — when a niche is activated, identify the key associations, brokers, and advisors in the space
- **Conference discovery** — conference organizers and association hosts
- **Web research** — industry blogs, podcasts, LinkedIn thought leaders in the niche
- **Existing network** — vault entities tagged with `relationship_type: River Guide` or `relationship_type: Intermediary`
- **Referrals** — one intermediary often knows others ("You should also talk to...")

Draft all emails in Superhuman via CLI (see Cold Outreach section for exact command). Do NOT use the MCP `superhuman_draft` tool.
</intermediary_outreach>

<essential_principles>
## Principles

### Kay/Camilla Decision Column (Temporary — Testing Phase)
During the testing phase, outreach-manager only drafts outreach for targets where Col O (Kay/Camilla: Decision) = "Approve". Either Kay or Camilla can approve targets. This is a temporary human-in-the-loop gate. Once target-discovery's accept rate stabilizes at 85%+ for 2 consecutive weeks (tracked on Skill Calibration tab of Weekly Tracker), this gate graduates to Spot Check and then Auto-Advance. Kay decides when to graduate — the system proposes it with data.

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
Confirm every email draft was created via the superhuman-cli Bash command (NOT the MCP `superhuman_draft` tool which uses Gmail API). For each target, verify the CLI returned a success response. If any draft creation failed, flag it. Drafts must exist in Superhuman's native draft system, not Gmail.

### 2. Call Sheet Validation
For every new cold target added this session, verify JJ's call columns in the Linkt target sheet are populated:
- **Company** — non-empty
- **Owner Name** — non-empty
- **Phone** — non-empty
- **Call Date** — Day 3 date populated

Missing fields mean JJ can't execute. Fix before proceeding.

### 3. Warm Intro Validation
Confirm Attio People records were checked for every target before drafting. For each target:
- If Col X (Warm Intro) says "Warm - {name}" → verify NO cold email was drafted AND no JJ call was scheduled. Warm intros get a different email template and skip JJ entirely.
- If Col X is blank → verify cold outreach was drafted normally.
A cold email sent to a warm intro target wastes the relationship advantage and looks impersonal. This is a hard gate.

### 4. Dedup Validation
Confirm Attio was checked before any drafting began. No person should have outreach queued from both the cold outreach and conference outreach subagents. If a person appears in both queues, conference outreach takes priority and the cold draft must be removed.

### 5. Cadence Tracking
Every cold Day 1 email (NOT warm intros) must have a corresponding Day 3 call entry scheduled in JJ's call sheet. Cross-reference the list of drafted cold emails against the call sheet. Any cold email without a matching Day 3 entry is a gap — add it before proceeding. Warm intro emails should NOT have a Day 3 call entry.

### 6. Slack Notification (Only After Validation Passes)
Only send once checks 1-5 all pass:
```bash
curl -s -X POST "$SLACK_WEBHOOK_OPERATIONS" \
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
