---
name: outreach-manager
description: "Owns all outreach across all channels and funnels. Four subagents: Kay Email cold outreach, DealsX coordination, conference outreach, intermediary outreach. Channel routing by niche (Kay Email / DealsX Email / JJ-Call-Only). Attio dedup catches crossover."
user_invocable: true
context_budget:
  skill_md: 3000
  max_references: 2
  sub_agent_limit: 2000
---

> **2026-05-01 calibration:** Superhuman fully sunset 4/29/26. All draft references in this file mean **Gmail directly** via the bash wrapper. See .

<objective>
Own all outreach. Every email, call, DM, and follow-up flows through this skill.

This skill receives targets from two upstream skills and runs personalized outreach via four subagents. A shared dedup layer prevents any person from receiving overlapping outreach from both funnels.

**Inputs from other skills:**
- **skill/target-discovery** — approved cold targets with enriched contact info and research context
- **skill/conference-discovery** — conference attendee targets (pre-conference) and conversation data (post-conference)

**Outputs to other skills:**
- Outreach status updates → skill/pipeline-manager (stage progression based on responses)
- JJ's call outcomes feed back into pipeline-manager
- Weekly outreach metrics → skill/weekly-tracker

Four subagents:
1. **Kay Email Cold Outreach** — multi-channel cadence for Kay Email niches, Claude-drafted in Gmail
1b. **DealsX Coordination** — coordination with Sam Singh / DealsX for mass email + LinkedIn outreach on DealsX niches
2. **Conference Outreach** — pre-conference emails and post-conference follow-ups (Kay always, regardless of niche channel)
3. **Intermediary Outreach** — relationship-building with association heads, brokers, river guides (Kay always)

### Niche Channel Routing

Each niche is assigned a channel on the WEEKLY REVIEW tab (Col D). This determines which subagent handles outreach.

| Niche | Channel | Notes |
|-------|---------|-------|
| Art Advisory | Kay Email | Small TAM, relationship-driven, no JJ calls |
| Art Storage | Kay Email | Small TAM, Active-Long Term |
| Fractional CFO | DealsX Email | Sam handles outreach |
| Specialty Insurance Brokerage | DealsX Email | Sam handles, Margot geographic arbitrage thesis |
| Estate Management | DealsX Email | Sam handles, UHNW focus |
| Premium Pest Management | JJ-Call-Only | Decoupled, handled by jj-operations, not outreach-manager's scope |

**Channel routing rule:** Before running any subagent, read the WEEKLY REVIEW tab Col D for the niche. Route to the correct subagent. Never cross channels.

**Delivery model (Kay Email channel):** Claude drafts in Gmail directly. Kay reviews and sends. No third-party tool ever touches Kay's SMTP credentials.
**Delivery model (DealsX Email channel):** Sam/DealsX handles all outreach. We provide templates, exclusion lists, and warm intro intercepts. We draft replies to inbound responses.
**Delivery model (JJ-Call-Only channel):** Handled entirely by jj-operations skill, not outreach-manager.
</objective>

<dedup_layer>
## Attio Dedup Layer

Before either subagent drafts outreach, run these checks:

1. **Does this person already exist in the pipeline?** If yes, check their current stage and last outreach date. Don't double-contact someone already in an active cadence.
2. **Is this person receiving outreach from the other subagent?** If a conference target is also in the cold outreach queue (or vice versa), the conference outreach subagent takes priority — the conference framing ("I'll be at your booth Thursday" or "Great meeting you yesterday") is always stronger than cold email.
3. **Has this person been contacted in the last 30 days?** If yes, skip unless there's a new context (conference, referral, signal change).
4. **Warm intro check (CRITICAL).** Before cold outreach, search Attio People records for the target owner AND anyone at their company. If Kay has an existing connection (LinkedIn import, prior email, meeting), flag as "Warm Intro" on the target sheet. Warm intro targets skip cold email + JJ call entirely — instead, draft a warm intro request email for Kay referencing the mutual connection. See Warm Intro Outreach section below.

The dedup + warm intro check runs once when targets are received, before any drafting begins.
</dedup_layer>

<cold_outreach>
## Subagent 1: Kay Email Cold Outreach

**Channel gate:** This subagent ONLY runs for niches where Col D on WEEKLY REVIEW = "Kay Email". For DealsX Email niches, see Subagent 1b. For JJ-Call-Only niches, see jj-operations skill.

Handles outreach for Kay Email targets sourced from skill/target-discovery (Apollo + free sources).

### Cold Outreach Delivery

All cold outreach emails are drafted in **Superhuman** via the CLI wrapper. Kay reviews Day 0 emails, then hits send on all emails from Gmail (Day 0 reviewed, Day 3/6/14 follow-ups sent without editing).

```bash
~/.local/bin/gmail-draft.sh  # (was superhuman-draft.sh — Superhuman sunset 4/29) --to "{email}" --subject "{subject}" --body "{body}"
```

**No third-party email tool ever gets SMTP credentials.** Kay sends every email herself from Gmail. Claude drafts, Kay sends.

### Cadence Tracking (Claude-Managed)

Claude manages the outreach cadence by tracking per-touchpoint date columns on the target sheet + Attio notes:

**Target sheet columns (managed by Claude, referenced by header name via col-lookup.py):**
- **Variant** — `A` or `B` (set once when Day 0 is drafted, never changes)
- **Day 0 Sent** — date when Day 0 email was sent
- **Day 3 Sent** — date when Day 3 follow-up was sent
- **Day 6 DM Sent** — date when LinkedIn DM was sent
- **Day 14 Sent** — date when Day 14 final email was sent
- **Cadence Status** — current state: `Active`, `Complete`, `Replied`

**Real-time tracking flow:**
1. Claude drafts email/DM in Superhuman (or surfaces DM text in briefing)
2. Kay says "looks good" or confirms sent
3. Claude immediately updates: target sheet (writes date to the specific touchpoint column, e.g. "Day 0 Sent", "Day 3 Sent"; sets "Cadence Status" to `Active` or `Complete`) + Attio note on the contact record

**Picking new targets:** `"Kay: Decision" = "Approve"` AND `"Day 0 Sent"` is blank.

**Daily cadence check (runs each morning):**
1. Read target sheet: find all targets where "Cadence Status" = `Active`
2. For each active target, check which touchpoint columns are blank:
   - "Day 0 Sent" filled, "Day 3 Sent" blank, 3+ business days since Day 0 → draft Day 3 follow-up in Superhuman
   - "Day 3 Sent" filled, "Day 6 DM Sent" blank, 3+ business days since Day 3 → surface LinkedIn DM in briefing (message text + LinkedIn URL)
   - "Day 6 DM Sent" filled, "Day 14 Sent" blank, 8+ business days since Day 6 → draft Day 14 final email in Superhuman
   - "Day 14 Sent" filled → set "Cadence Status" to `Complete`
3. Draft 5 new Day 0 emails for fresh targets (approved, Day 0 Sent blank)
4. Present in morning briefing: "5 new drafts to review, X follow-ups to send, X LinkedIn DMs to send"

**Kay's daily effort:**
- Day 0 emails: review, edit if needed, send (~5-10 min)
- Follow-up emails (Day 3/14): just hit send, no review needed (~1 min each)
- LinkedIn DMs (Day 6): copy message from briefing, paste in LinkedIn, send (~1 min each)

### Review Model

- **Day 0 emails:** Kay reviews every one (personalized, needs her eye)
- **Day 3/14 follow-ups:** Pre-approved templates, Kay just hits send
- **Day 6 LinkedIn DMs:** Pre-approved templates, Kay pastes and sends
- **Warm intros + edge cases:** Surfaced in morning briefing for Kay to decide

### G&B Cold Email Outreach Cadence (Universal — All Niches)

| Day | Channel | Action | Kay's Role |
|-----|---------|--------|------------|
| Day 0 | Email (Gmail) | Personalized cold email, A/B variant | Review + send |
| Day 3 | Email (Gmail) | Follow-up email #1 (same thread) | Just send |
| Day 6 | LinkedIn DM | Standalone LinkedIn DM | Copy-paste + send |
| Day 14 | Email (Gmail) | Follow-up email #2, final (same thread) | Just send |

After Day 14 with no response, move to nurture cadence (pipeline-manager handles from here).

**Business days only.** All day counts are business days (Mon-Fri). No emails sent on weekends. No Sunday drafts scheduled for send.

**Why this cadence:** 4 touchpoints across 14 business days, two channels. Day 0 email establishes who Kay is and gives time to check LinkedIn. Day 3 follow-up shows genuine interest. Day 6 LinkedIn DM reaches them on a different channel (and works standalone if they never read emails). Day 14 final email references elapsed time ("since I first reached out") showing Kay's serious, not mass-emailing. No connection requests — they clutter Kay's network.

**Volume:** 5 new targets per day, every weekday. No zero days. 25+ emails per week minimum.

**Reference doc:** "G&B Cold Email Outreach Cadence & Templates 4.4.26" in the master templates Drive folder.

### Niche-Specific Channel Rules (Kay Email Niches Only)

This subagent only handles niches routed to Kay Email. See the Niche Channel Routing table in the objective for the full mapping.

| Niche | Email | LinkedIn DM | JJ Call |
|-------|-------|-------------|---------|
| Art Advisory | Yes | Yes | NO — small world, cold call burns relationships |
| Art Storage | Yes | Yes | NO — small TAM, relationship-driven |

DealsX Email niches (Fractional CFO, Specialty Insurance Brokerage, Estate Management) are handled by Subagent 1b.
JJ-Call-Only niches (Premium Pest Management) are handled by jj-operations.

### Target Sheet Columns

**Discovery columns:** Source, Company, Website, Headquarters, Industry, Employees, Revenue, Ownership, Owner Name, Owner Title, Email, Phone, LinkedIn (Owner), LinkedIn (Company)

**Decision columns:**
- **Kay: Decision** — `Approve` or `Pass`. The ONLY trigger for Attio entry creation and outreach.
- **Kay: Pass Reason** — Why Kay passed (if applicable).
- **Agent Notes** — Agent recommendation. Must start with `RECOMMEND: Approve` or `RECOMMEND: Pass` followed by reasoning. If a warm intro path is found, include: "RECOMMEND: Approve — WARM INTRO via {connection name}".

**Outreach tracking columns (managed by Claude, after "LinkedIn Connection"):**
- **Variant** — `A` or `B` (set once at Day 0)
- **Day 0 Sent** — date Day 0 email was sent
- **Day 3 Sent** — date Day 3 follow-up was sent
- **Day 6 DM Sent** — date LinkedIn DM was sent
- **Day 14 Sent** — date Day 14 final email was sent
- **Cadence Status** — `Active` / `Complete` / `Replied`
- **LinkedIn Connection** — Kay marks 1st/2nd/3rd degree manually

**JJ call columns (managed by JJ, for niches where calls are approved):**
- **JJ: Call Status** — dropdown: Not Called, Connected, Voicemail, Callback, Not Interested, Wrong Number, Schedule Requested
- **JJ: Call Date**
- **JJ: Call Notes**
- **JJ: Owner Sentiment** — dropdown

### Personalization Layer

Every Day 0 target gets personalized variables filled from the Pre-Draft Research Brief. The templates are the structure — {specific detail}, {specific question}, and {connection point} are what make each email unique.

**Voice:** Kay's calibrated outreach voice (see memory: user_outreach_voice.md)

### A/B Test: Two Email Variants (Active Experiment)

Claude alternates variants 50/50 on Day 0 emails. Record the assigned variant in the "Variant" column (`A` or `B`) when Day 0 is drafted. This value is set once and never changes.

Warm intro targets are excluded from this experiment.

**Subject line (both variants):** Intro {first name} & Kay

**VARIANT A — Learning (curiosity-first)**

Day 0:
```
Hi {first name},

Hope this finds you well. I came across {company} and was impressed by the work you've done in the {industry} space.

After a decade in the luxury world, I recognized the client crossover in the art world and have been really curious to learn more about art advisory. I'd welcome the chance to connect and hear your perspective.

I'd love to connect and learn more about your business. When would be a good time to speak? Looking forward to hearing from you.

Very best, Kay
```

Day 3 (same thread):
```
Was thinking more about {company}. Still hoping we can find some time to connect.

Very best, Kay
```

Day 6 (LinkedIn DM — standalone):
```
Hi {first name}, your work at {company} caught my eye. I'm exploring the {industry} space and would love to chat if you're able.
```

Day 14 (same thread):
```
I've been learning more about the {industry} space since I first reached out and have some key questions I'd love to ask, as your reputation really stands out. Would love to connect if you're available.

Very best, Kay
```

**VARIANT B — Direct (transparent acquisition intent)**

Day 0:
```
Hi {first name},

Hope this finds you well. I'm reaching out because I've been looking to build or acquire a business in the {industry} space and I'm interested in {company}.

I grew up around small business through my father, a serial entrepreneur, and went into luxury because I loved the mix of art and commerce. After a decade at Chanel, I recognized the client crossover in the art world and am now looking to build my next chapter here.

I'm looking to acquire one business and run it myself, full time. I'd love to connect and learn more about yours. If you're open to an exploratory conversation, let me know when would be a good time to speak.

Looking forward to connecting.

Very best, Kay
```

Day 3 (same thread):
```
Was thinking more about {company}. I'm a well capitalized buyer and think we could have a great conversation. Let me know when would be best to connect.

Very best, Kay
```

Day 6 (LinkedIn DM — standalone):
```
Hi {first name}, I came across {company}. As you can see I've spent my career in the luxury space and am now looking to acquire a great business in the {industry} space. {company}'s reputation really stands out. Please let me know if you're free to chat.
```

Day 14 (same thread):
```
Since I first reached out I've explored the {industry} space and keep thinking back to {company}. Would love to connect if you're available.

Very best, Kay
```

**Variables:**
- {first name} — contact first name
- {company} — company name
- {industry} — broader industry term (e.g., "art advisory", "financial advisory", "commercial pest management")

**What we're testing:** Does transparency about acquisition intent help or hurt response rates? Variant A positions Kay as a curious learner. Variant B is upfront about being a buyer.

**Tracking:** Claude tracks variant assignment per target. Weekly tracker dashboard (Signal Quality lens) reviews A/B performance per niche. Metrics: response rate, time to response, tone of response (warm vs defensive), conversion to call.

**HARD RULES (apply to BOTH variants):**
- Never mention Greenwich & Barrow in Day 0 emails. LinkedIn handles credibility (they'll check).
- NEVER reference revenue, employee count, or financial metrics. Could be wrong, and it signals you care about money not legacy.
- NEVER call G&B a "fund." Sounds like PE and kills trust.
- Keep it light on the target. Don't over-research or reference specifics that could land wrong (partner names, articles, characterizations of their skills). The research is for follow-ups and the actual conversation, not the first email.
- Use Kay's exact phrasing for key lines ("After a decade in the luxury world", "the mix of art and commerce"). Don't paraphrase.
- Every sentence must add independent value. If it doesn't earn the reply, cut it.
- Variant A: "I came across {company}" — curiosity framing. Variant B: lead with why you're reaching out, then who you are, then the ask.
- Kevin Hong branding pointers: concise, customization early and clear, show why it matters to the seller, be bold and personable.
- NEVER reveal thesis/growth strategy (underpenetration, consolidation, market size).
- Don't make claims you can't source. Every line must be grounded in real research.
- No em dashes. Periods, commas, line breaks.
- Lead with curiosity about what they've built, even in Variant B.

### Email Verification (ALL Targets — NO EXCEPTIONS)

**NEVER draft an email to an address that was guessed or constructed from name + domain patterns.** If the email address does not come from a verified source (Apollo enrichment, company website, email signature, LinkedIn profile, direct correspondence), do NOT use it. Guessing email formats burns Kay's sender reputation. This rule applies EVERYWHERE.

All targets are enriched via Apollo before reaching outreach-manager. Before drafting, verify the email address status:

```bash
source .env && curl -s "https://api.apollo.io/v1/people/match" \
  -H "Content-Type: application/json" \
  -H "X-Api-Key: $APOLLO_API_KEY" \
  -d '{"first_name":"{first}","last_name":"{last}","organization_name":"{company}","domain":"{domain}"}'
```

**Gate logic based on `email_status`:**
- `verified` → proceed to draft
- `guessed` / `unavailable` / `bounced` → do NOT draft. Note status in "Agent Notes" column. Notify Kay: "{owner} at {company} — email not verified ({status}). Skip or find alternate?"
- `pending` → retry once after 5 minutes. If still pending, flag.

### Pre-Draft Research Brief (REQUIRED before any Day 0 draft)

Before writing any Day 0 outreach email, build a research brief for the target. This eliminates Kay's manual research step.

**For each target, collect:**
1. **Owner LinkedIn profile:** Background, tenure, posts, mutual connections with Kay, career arc
2. **Company website:** Services offered, team page, about us, any news/press, geographic focus
3. **Company LinkedIn page:** Employee count, recent posts, growth signals, follower count
4. **Search Activity tracker cross-reference:** River guide comments, prior outreach history
5. **Kay's LinkedIn connections:** Warm intro path (from Attio People cross-reference + LinkedIn CSV)
6. **Apollo data:** If available from verification step, any additional context

**Flag before drafting (do NOT draft if any of these):**
- Owner appears retired or no longer at the company
- Company appears acquired or part of a larger group
- Company website is down or domain expired
- Owner is a Kay LinkedIn connection (route to warm intro instead of cold)

**Get it right the first time.** Superhuman CLI cannot update or delete drafts. Every draft created is permanent until Kay manually deletes it.

### Draft Creation

All outreach drafts use the Superhuman CLI wrapper (NOT the MCP tool — it uses Gmail API which creates invisible drafts):

```bash
~/.local/bin/gmail-draft.sh  # (was superhuman-draft.sh — Superhuman sunset 4/29) --to "{email}" --subject "Intro {first name} & Kay" --body "{body}"
```

**CRITICAL:** Always verify the Superhuman CLI is using the G&B account (`kay.s@greenwichandbarrow.com`), not the personal email. If the G&B token is expired, the CLI silently falls back to the personal account. Check the output for the account confirmation line.

Sign off "Very best, Kay" only — signature is built in.

### Attio State Machine

Outreach-manager is the only skill that writes to Attio for targets. **No Attio entry exists until Kay approves.** The sequence:

1. Read the target sheet, find rows where **"Kay: Decision" = "Approve"** that weren't approved in the prior run (new approvals). "Kay: Decision" = "Approve" is the ONLY trigger for Attio entry creation.
2. Verify email via Apollo API. Only proceed if `verified`.
3. For each verified approved target, search Attio for the person AND company:
   - **If found** → someone Kay already knows. Note "WARM INTRO via {connection}" in "Agent Notes", skip cold outreach.
   - **If not found** → create the company + person in Attio, add company to Active Deals at "Identified" stage.
4. When Day 0 email is sent → update Attio stage to "Contacted"
5. When reply received → update Attio stage to "Engaged"
6. After Day 14 with no response → pipeline-manager moves to nurture cadence

### Attio Note Logging (Real-Time)

When Kay confirms an email was sent or a LinkedIn DM was sent, immediately create an Attio note on the person's record:

- **Email sent:** "Cold outreach Day {N} email sent. Variant {A/B}. Subject: {subject}"
- **LinkedIn DM sent:** "LinkedIn DM sent. Message: {message text}"
- **Reply received:** "Reply received from {owner}. {brief summary}"

This ensures the full outreach timeline lives in Attio alongside the automatically-tracked email history.

### JJ Call Prep (for JJ-Call-Only niches ONLY)

**Channel gate:** This section only runs for niches where Col D on WEEKLY REVIEW = "JJ-Call-Only". Kay Email niches and DealsX Email niches do NOT get JJ calls through outreach-manager.

For JJ-Call-Only niches, outreach-manager populates the call columns on the target sheet after Day 0 email is sent.

**JJ call timing:** JJ calls on Day 3 (same day as follow-up email). The call is a confirmation call, not a cold call — "We sent {owner name} a note a couple days ago and I just wanted to make sure it came through."

**Script:**
```
Hi, this is JJ with Greenwich & Barrow. We sent {owner name} a note
a couple days ago and I just wanted to make sure it came through.
We've been researching the {niche} space and would love to connect
briefly with {owner name} about their experience.
Would {owner name} have a few minutes for a quick call?
```

**JJ positioning:** JJ is a team member at G&B, not an assistant. He speaks as "we" and represents the firm in his own right. Never frame JJ as calling "on behalf of" anyone.

**If the owner wants to schedule a call with Kay:** JJ books a time directly with the owner on the phone, then emails Howie (barrie@greenwichandbarrow.com) with: owner name, owner email, and agreed time. Howie creates the calendar invite.

**JJ works directly from the target sheet.** No separate call list. JJ fills in the JJ columns on the Active tab.

**Feedback:** JJ is encouraged to share qualitative observations on Slack anytime.

### Follow-Up Emails

Day 3 and Day 14 follow-ups are drafted by Claude from the approved templates above. They are same-thread replies.

**Claude drafts these proactively each morning** for any target where the follow-up is due. Kay just hits send — no review needed unless she wants to customize.

### LinkedIn Actions

On Day 6, Claude surfaces the LinkedIn DM in the morning briefing:

```
LinkedIn DMs due today:
1. {Owner Name} at {Company} — {LinkedIn URL}
   Message: {DM text from template}
```

Kay opens LinkedIn, pastes or adapts the message, sends. Then confirms in conversation.

Claude immediately logs to Attio and updates the target sheet ("Day 6 DM Sent" column with today's date).

**DM personalization by connection degree:**

**1st degree:**
```
Hey {first name}, hope you're doing well. I came across {company} while looking into {niche} and was impressed by {something specific}. Would love to catch up for a few minutes if you're open.
```

**2nd degree:**
```
Hi {first name}, {mutual connection} and I were chatting and your name came up in the context of {niche}. I've been looking into the space and would love to hear your perspective. Open to a quick call?
```

**3rd degree / cold:**
```
Hi {first name}, I came across {company} while researching {niche} and was impressed by {something specific}. I'm trying to learn as much as I can about the space. Would you be open to a quick conversation?
```

**HARD RULES (same as email):**
- Never mention Greenwich & Barrow in DMs
- Never reference revenue, employee count, or financials
- LinkedIn tone is MORE casual than email — no "Very best, Kay" sign-off
- Keep DMs to 3-4 sentences max
- Lead with curiosity about THEM, not Kay
- Do NOT send LinkedIn DMs on weekends. Business days only.

### Warm Intro Handling

Two scenarios trigger a warm intro flag:

**A. Shared Attio connection found** (during outreach-manager warm intro check):
1. Note "WARM INTRO via {connection name}" in "Agent Notes"
2. Surface in morning briefing: "Warm intro available: {target owner} at {company}. You're connected to {connection name}. Cold outreach paused for this target."
3. Cold outreach is PAUSED for this target — no email draft, no JJ call
4. Kay decides approach case by case
5. Claude drafts per Kay's direction — no template, each is unique

**B. Inbound introduction via email** (pipeline-manager detects intro):
1. Pipeline-manager surfaces the intro in morning briefing
2. Kay decides approach
3. Claude drafts per Kay's direction
4. Thank-you to introducer is always drafted (short, same day)
5. No JJ call — warm intros are Kay-only
</cold_outreach>

<dealsx_coordination>
## Subagent 1b: DealsX Coordination

> **NOT YET ACTIVE.** This subagent is pending until Sam Singh / DealsX engagement is confirmed and onboarded. Do not run any DealsX workflows until this flag is removed.

**Channel gate:** This subagent ONLY runs for niches where Col D on WEEKLY REVIEW = "DealsX Email". Currently: Specialty Insurance Brokerage, Fractional CFO, Estate Management.

Sam Singh / DealsX handles mass email + LinkedIn outreach for these niches. Our role is coordination, not execution.

### What We Provide Sam

1. **ICP criteria per niche** — buy box parameters, geographic preferences, size filters
2. **Day 0 template variants (A/B)** — already on Google Drive in the "G&B Cold Email Outreach Cadence & Templates 4.4.26" doc
3. **Voice guidelines** — Kay's calibrated outreach voice (see memory: user_outreach_voice.md)
4. **Exclusion list (CRITICAL)** — before each batch, generate and send Sam:
   - PE-owned companies (hard stop, same as all channels)
   - Companies already in Attio (already in our pipeline)
   - Warm intro targets (pulled to Kay Email channel instead)
   - Companies previously contacted by Jessica (check Activity Report)

### What Sam Provides

Shared Google Sheet per niche with columns:
- Company name
- Owner name
- Email
- Date contacted
- Response status
- Meetings booked

### Warm Intro Intercept (CRITICAL)

Before Sam contacts anyone in a new batch, run warm-intro-finder on his target list.

1. Sam shares his upcoming batch (via shared Google Sheet)
2. Claude runs warm-intro-finder against the batch
3. Any targets where Kay has a connection get PULLED from Sam's list
4. Pulled targets get routed to Kay Email cold outreach (Subagent 1) with warm intro framing
5. Remaining targets stay with Sam

This check is a HARD STOP before Sam sends. If we miss the window, Sam may cold-email someone Kay knows personally.

### Reply Management

When targets reply to Sam's emails, replies arrive in Kay's Gmail inbox (kay.s@greenwichandbarrow.com). This is our primary value-add for DealsX niches.

**Flow:**
1. email-intelligence detects reply from a DealsX niche target
2. Claude drafts response in Gmail directly wrapper
3. Kay reviews and sends

```bash
~/.local/bin/gmail-draft.sh  # (was superhuman-draft.sh — Superhuman sunset 4/29) --to "{email}" --subject "Re: {original subject}" --body "{body}"
```

Same voice rules, same SMTP rules as Kay Email channel. Kay sends every reply herself.

### Attio Updates

- When Sam reports a contact was made (date appears in "Date contacted" column) → create/update Attio entry at "Contacted" stage
- When reply received in Kay's inbox → update Attio stage to "Engaged"
- When meeting booked → update Attio stage to "Meeting Scheduled"

### What We Do NOT Manage

- **Cadence timing:** Sam owns Day 0 through completion. We do NOT manage Day 3/6/14 timing for DealsX niches.
- **LinkedIn DMs:** Sam's team handles these for DealsX niches.
- **Volume:** No "5 per day" limit from our side. Sam handles his own volume and pacing.
- **Email drafting for initial outreach:** Sam drafts from our templates. We only draft replies to inbound responses.
- **A/B variant tracking:** Sam tracks his own variants. We track reply rates from our side (what comes into Kay's inbox).

### Daily Morning Check (DealsX Niches)

1. Check Sam's shared sheets for new contacts made (new dates in "Date contacted")
2. Check Kay's inbox for replies from DealsX niche targets
3. For new replies: draft response in Superhuman, surface in morning briefing
4. For new contacts: batch-update Attio entries
5. Report in briefing: "DealsX: X new contacts this week, X replies pending response"
</dealsx_coordination>

<conference_outreach>
## Subagent 2: Conference Outreach

Handles all outreach related to conferences — pre-conference emails to attendees and post-conference follow-ups.

### Conference Outreach Cadence

Outreach-manager pulls the conference date from the **Conference Pipeline Google Sheet** ("Date of Conference" column, Sheet ID: `1bdf7xlcRjOTlVkuXA-HNGOQgjtDRmVN2RfDf9aUsDpY`). This is the source of truth for timing. All timing works backwards from this date.

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

Draft in Superhuman via the CLI wrapper:
```bash
~/.local/bin/gmail-draft.sh  # (was superhuman-draft.sh — Superhuman sunset 4/29) --to "{email}" --subject "{subject}" --body "{body}"
```
Kay reviews and sends from Gmail.

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
1. Draft personalized follow-up email referencing specific conversation points
2. Use Kay's voice, no em dashes
3. Propose a specific next step (call, meeting, send info)
4. Short and specific — reference something from the actual conversation, not generic

For people Kay didn't get to meet but emailed pre-conference:
```
Hi {first name},

Sorry I missed you at {Conference Name}. Would still love to connect. Do you have a few minutes this week?

Kay
```

Draft all in Superhuman. Present during morning briefing. Kay approves and sends.
</conference_outreach>

<intermediary_outreach>
## Subagent 3: Intermediary Outreach

Handles outreach to force multipliers — people who know every owner in the niche and can open doors. These are NOT acquisition targets. They are relationship-building contacts who go into the Attio Intermediary Pipeline, not Active Deals.

### AUTHORITATIVE ARTIFACTS (Apr 29 2026 — read these first)

**Master template:** `G&B Intermediary Outreach Templates` — Google Doc ID `1_cNsAPCopDAfReoDXbB4d3hZW8TcYUqJ3XKYY_er7i4`, in `OPERATIONS / G&B MASTER TEMPLATES/`. Contains 8 audience-specific variations + shared core blocks + warm-intro language bank. Update this Doc as voice evolves; do NOT recreate from scratch.

**Master target sheet:** `Intermediary Target List` — Google Sheet ID `18zzE1y-BU1xuD-y0BOmEl8GtJ4I-iclSuBqAi0q3pkk`, in `OPERATIONS / TARGET LISTS / INTERMEDIARY/`. 8 tabs: Brokers / Investment Bankers / Association Heads / Industry Lawyers / CPAs / Corporate Advisors / Family Offices / Lenders. 17-column schema. Reference list (NOT maintained) — Attio owns ongoing status.

**Voice rules (must read before drafting):**
- `feedback_no_search_fund_language_intermediaries.md` — drop "search fund" / "search vehicle"; use "holding company in formation"
- `feedback_kay_handles_all_replies.md` — replies always Kay (Kay-sent or Sam-DealsX-sent)
- `feedback_gmail_only_no_superhuman.md` — drafts in Gmail directly (Superhuman sunset Apr 28)

### Who Are Intermediaries? (8 categories per the sheet)

- **Brokers** — business brokers / lower-mid-market M&A advisors. Voice: short, NDA-offer-ready, deal-flow ask.
- **Investment Bankers** — boutique IBs with active mandates. Voice: formal, mandate-distribution ask.
- **Corporate Advisors** — business-side advisors at private banks/wealth firms (Matt Luczyk archetype). Voice: relationship-build, succession angle.
- **Family Offices** — SFOs/MFOs (Bessemer, BBH, Cresset, Pathstone, Iconiq). Voice: peer-investor framing — co-investment + deal-flow ask.
- **Industry Lawyers** — M&A counsel, transaction attorneys, tax-PE attorneys. Voice: short, professional, referral relationship. **NOT employment lawyers** — those are reference-only, not outreach contacts.
- **CPAs** — M&A advisory CPAs, succession-planning accountants. Voice: continuity-focused, referral relationship.
- **Association Heads** — trade-association leaders. Voice: "student of the industry" — NOT a buyer pitch.
- **Lenders** — search-fund-friendly debt providers (commercial banks + SBA + mezz + BDCs + private credit). Voice: I'm a buyer with a buy-box, would value a lending relationship as we approach LOI.

### Cadence: ONE-AND-DONE

**Per Kay 2026-04-29: intermediary outreach is one-and-done.** No follow-up sequences. If they don't respond, move on. Different from owner outreach which has Day 0/3/14 cadence.

No JJ call. Intermediaries hear from Kay directly only.

### Conference River Guide Play

When an upcoming conference is registered, identify the association head or organizer and reach out T-minus 3 weeks (before attendee outreach starts). The goal: meet them before the conference so they walk Kay through the room making introductions.

| When | Action |
|------|--------|
| T-minus 21 days | First email to association head / organizer |
| T-minus 14 days | Follow-up if no response |
| T-minus 7 days | If connected, ask: "Who should I make sure to meet at {conference}?" |
| Conference day | Meet in person. They introduce Kay to key people. |
| T+1 day | Thank-you email + follow-up on any introductions they made |

### Attio Pipeline

Intermediaries go into the **Intermediary Pipeline** in Attio, not Active Deals:
- New contact → "Identified"
- First email sent → "Contacted"
- Positive response → "Warmed"
- Actively sending introductions → "Actively Receiving Deal Flow"

### Sources for Intermediary Discovery

- **Niche intelligence** — when a niche is activated, identify the key associations, brokers, and advisors
- **Conference discovery** — conference organizers and association hosts
- **Web research** — industry blogs, podcasts, LinkedIn thought leaders
- **Existing network** — vault entities tagged with `relationship_type: River Guide` or `relationship_type: Intermediary`
- **Referrals** — one intermediary often knows others

Draft all intermediary emails in Gmail directly.
</intermediary_outreach>

<essential_principles>
## Principles

### Volume & Cadence
- **Kay Email niches:** 5 new cold targets per day, every weekday. No zero days. 25+ owner emails per week minimum.
- **DealsX Email niches:** Sam handles volume. No daily limit from our side. We track replies only.
- **JJ-Call-Only niches:** Handled by jj-operations, not outreach-manager.
- Quality over quantity — deep research on each Kay Email target, personalized Day 0 outreach
- Follow-ups (Day 3/14) are templated — Kay just hits send (Kay Email niches only)
- LinkedIn DMs (Day 6) are templated — Kay copy-pastes and sends (Kay Email niches only)
- Conference targets excluded from cold cadence

### Channel Rules
- **Kay Email:** All via Superhuman CLI wrapper. Kay sends every email herself. No third-party SMTP access ever.
- **DealsX Email:** Sam sends from his infrastructure. We provide templates and exclusion lists. Replies come to Kay's inbox, Claude drafts responses in Superhuman.
- **Phone:** JJ's call columns in the target sheet. JJ logs outcomes. Only for JJ-Call-Only niches.
- **LinkedIn DM (Kay Email niches):** Kay sends manually from LinkedIn. Claude drafts and surfaces in morning briefing. Tracked in Attio notes.
- **LinkedIn DM (DealsX niches):** Sam's team handles.
- **All channels:** Same voice, same framing (curiosity, not acquisition pitch).

### Team Roles (for this skill only)
- **Claude:** Deep research per Kay Email target, draft all Kay Email emails/DMs, track cadence timing, update sheet + Attio in real-time, coordinate with Sam on DealsX niches, draft replies to DealsX inbound
- **Kay:** Review Day 0 emails (Kay Email), send all Kay emails, send LinkedIn DMs (Kay Email), take calls, review DealsX reply drafts
- **Sam / DealsX:** Own full outreach cadence for DealsX niches (email + LinkedIn). Provide contact sheets. NOT YET ACTIVE.
- **JJ:** Confirmation calls from sheet (JJ-Call-Only niches only), log outcomes

### Coordination with Other Skills
- **pipeline-manager:** After Day 14 with no response, pipeline-manager takes over with nurture cadence. Outreach-manager does not re-contact nurture targets unless pipeline-manager flags them.
- **weekly-tracker:** Outreach metrics (emails sent, DMs sent, response rates) feed into the weekly activity tracker.
</essential_principles>

<validation>
## Validation / Stop Hooks

Before reporting completion, run these checks. If any check fails, fix before proceeding.

### 0a. Jessica Prior Contact Check (STOP HOOK — before drafting)
Before drafting outreach for ANY company, check if they were previously contacted by Jessica. Cross-reference against the Activity Report (Google Sheet) or check Attio notes for "Cold emailed by Jessica" text. If previously contacted, frame as re-introduction, NOT cold outreach.

### 0b. Tracker Verification (STOP HOOK — before drafting)
Before drafting outreach for any target, verify the target is on Kay's tracker. If not on the tracker, flag: "{company} is not on the tracker. Add first or skip?" Do NOT draft outreach for unknown targets.

### 1. Channel Routing Validation
Verify every target was routed to the correct subagent based on its niche's Col D value on WEEKLY REVIEW:
- Kay Email niches → Subagent 1 only
- DealsX Email niches → Subagent 1b only
- JJ-Call-Only niches → jj-operations (not outreach-manager)
No cross-channel contamination.

### 2. Draft Delivery Validation (Kay Email niches only)
Confirm every email draft was created via the Superhuman CLI Bash wrapper (NOT the MCP `superhuman_draft` tool). Verify the CLI returned a success response AND confirmed the G&B account (not personal email fallback).

### 3. Cadence Tracking Validation (Kay Email niches only)
Verify the target sheet has been updated for every outreach action:
- Correct touchpoint date column populated (Day 0 Sent / Day 3 Sent / Day 6 DM Sent / Day 14 Sent)
- Variant column set (A or B) on Day 0
- Cadence Status reflects current state (Active / Complete / Replied)
- Attio note created for each outreach action

### 4. DealsX Coordination Validation (DealsX Email niches only)
- Warm intro intercept ran BEFORE Sam contacted new batch
- Exclusion list provided to Sam (PE-owned, already in Attio, warm intros, Jessica contacts)
- Attio entries created/updated for Sam's reported contacts
- Replies from DealsX targets drafted in Superhuman (not ignored)

### 5. Warm Intro Validation
For each target: if "Agent Notes" contains "WARM INTRO" → verify NO cold email was drafted and no JJ call was scheduled. Warm intros get a different approach and skip JJ entirely. For DealsX niches, warm intro targets must be PULLED from Sam's list and routed to Kay Email.

### 6. Dedup Validation
No person should have outreach queued from multiple subagents. Conference outreach takes priority over cold outreach. Kay Email warm intro takes priority over DealsX cold outreach.

### 7. Email Verification Validation (Kay Email niches only)
Every email address drafted to must have a `verified` status from Apollo. No guessed or constructed emails. DealsX handles their own verification.

### 8. PE Ownership Check
HARD STOP: never outreach to PE-owned companies. Applies to ALL channels including DealsX exclusion lists. If PE ownership detected, do not draft and do not include in Sam's batch.
</validation>

<success_criteria>
## Success Criteria

### Daily (Kay Email Niches)
- [ ] 5 new Day 0 drafts in Gmail (personalized, research brief completed)
- [ ] All due follow-ups (Day 3/14) drafted in Superhuman
- [ ] All due LinkedIn DMs (Day 6) surfaced in briefing
- [ ] Target sheet updated in real-time as Kay confirms sends
- [ ] Attio notes logged for every outreach action
- [ ] No duplicate outreach across funnels or channels

### Daily (DealsX Niches — when active)
- [ ] Sam's shared sheets checked for new contacts
- [ ] Replies from DealsX targets drafted in Superhuman
- [ ] Attio entries updated for Sam's reported contacts
- [ ] Warm intro intercept completed before each new Sam batch
- [ ] Exclusion list current (PE-owned, Attio existing, Jessica contacts)

### Weekly
- [ ] 25+ owners contacted via Kay Email (email + LinkedIn DM)
- [ ] DealsX contact volume tracked (Sam's sheets)
- [ ] Pre-conference emails sent for upcoming conferences
- [ ] Post-conference follow-ups drafted within 24 hours
- [ ] Outreach metrics available for weekly tracker (both channels separated)
- [ ] A/B variant performance tracked (Kay Email niches)
</success_criteria>
