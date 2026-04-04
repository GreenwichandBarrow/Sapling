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
1. **Cold Outreach** — sequenced multi-channel cadence for Apollo-sourced targets
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

**Delivery tracking note:** For cold outreach, pipeline-manager reads Salesforge stats via MCP for tracking and updates Attio stages. For warm/relationship emails, pipeline-manager tracks Superhuman draft send status. Outreach-manager focuses on drafting/sequencing only.
</dedup_layer>

<cold_outreach>
## Subagent 1: Cold Outreach

Handles outreach for targets sourced from skill/target-discovery (Apollo + free sources).

### Cold Outreach Delivery (UPDATED April 3, 2026)

Cold outreach emails are sent via **Salesforge** (MCP + API), NOT Superhuman drafts.
- Salesforge handles: cold email sequences + LinkedIn DMs + follow-up automation
- Superhuman stays for: warm/relationship emails only (thank-yous, intros, investor comms)

**Review Model:** Auto-advance targets that pass buy box + ICP criteria are enrolled in Salesforge automatically — no Kay review needed. Warm intro targets and edge cases are surfaced in the morning briefing for Kay to decide (personal draft or Salesforge). Kay spot-checks Salesforge outputs. If she sees bad emails flowing, tighten criteria or adjust templates.

Flow per approved target:
```
1. create_contact(workspaceId="wks_90dzvksqb1zcm2aifcfk6", firstName, lastName, email, company,
   linkedinUrl, position, tags=["niche:{niche}"],
   customVars={warm_opener, specific_hook, niche, company,
   connection_point, followup_hook, li_note})
2. enroll_contacts(workspaceId, sequenceId, filters={leadIds: [contactId]})
3. Create Attio entry at "Identified" stage
```
4. Salesforge sends Day 0 email automatically through Gmail
5. Salesforge sends Day 3 follow-up, Day 6 LinkedIn DM, and Day 14 final email automatically
6. Pipeline-manager reads Salesforge stats via MCP for tracking

Salesforge API key: /tmp/salesforge-key.txt (read silently, never echo)
Salesforge MCP: configured in .mcp.json with X-Salesforge-Key header

### G&B Cold Email Outreach Cadence (Universal — All Niches)

| Day | Channel | Action |
|-----|---------|--------|
| Day 0 | Email (Salesforge) | Personalized cold email, A/B variant auto-assigned |
| Day 3 | Email (Salesforge) | Follow-up email #1, auto-send (same thread) |
| Day 6 | LinkedIn DM (Salesforge) | Standalone LinkedIn DM (must work without email context) |
| Day 14 | Email (Salesforge) | Follow-up email #2 (final), auto-send (same thread) |

After Day 14 with no response, move to nurture cadence (pipeline-manager handles from here).

**Business days only.** All day counts are business days (Mon-Fri). No emails sent on weekends.

**Why this cadence:** 4 touchpoints across 14 days, two channels. Day 0 email establishes who Kay is and gives time to check LinkedIn. Day 3 follow-up shows genuine interest. Day 6 LinkedIn DM reaches them on a different channel (and works standalone if they never read emails). Day 14 final email references elapsed time ("since I first reached out") showing Kay's serious, not mass-emailing. No connection requests — they clutter Kay's network.

**Reference doc:** "G&B Cold Email Outreach Cadence & Templates 4.4.26" in the master templates Drive folder.

### Target Sheet Columns (added by outreach-manager)

When outreach-manager receives approved targets, it writes to the target sheet:

- **Col O: Kay's Approval Gate** — `Approve` or `Pass`. The ONLY trigger for Attio entry creation and Salesforge enrollment.
- **Col P: Pass Reason** — Why Kay passed (if applicable).
- **Col Q: Agent Notes** — Agent recommendation for each target. Must start with `RECOMMEND: Approve` or `RECOMMEND: Pass` followed by reasoning (e.g., "RECOMMEND: Approve — strong niche fit, verified email, no PE ownership" or "RECOMMEND: Pass — PE-owned since 2023, skip"). This format enables calibration-workflow to programmatically compare agent recommendations against Kay's decisions in Col O. If a warm intro path is found (mutual connection in Attio), include it here: "RECOMMEND: Approve — WARM INTRO via {connection name}".

**Standardized sheet layout:** A-N (list building / discovery data), O (Kay: Decision), P (Kay: Pass Reason), Q (Agent Notes).

**Outreach tracking lives in Salesforge.** Pipeline-manager reads Salesforge MCP directly for sequence status, reply tracking, and cadence progression. The target sheet is the staging area for discovery and approval only. No outreach tracking columns on the sheet.

**Warm intro handling:** When a warm intro is found, note it in Col Q. Warm intro targets skip cold email entirely — instead, draft a warm intro request email for Kay via Superhuman.

### Personalization Layer

Every target gets personalized variables filled from the Pre-Draft Research Brief. The templates above are the structure — {specific detail}, {specific question}, and {connection point} are what make each email unique.

**Voice:** Kay's calibrated outreach voice (see memory: user_outreach_voice.md)

### A/B Test: Two Email Variants (Active Experiment)

Salesforge handles A/B variant distribution natively at 50/50 on the Day 0 email node. Each variant tracks open/reply rates independently. No manual variant assignment needed.

Warm intro targets are excluded from this experiment (they go through Superhuman, not Salesforge).

**Subject line (both variants):** Intro {first name} & Kay

**VARIANT A — Learning (curiosity-first)**

Day 0:
```
Hope this finds you well. I came across {company} and was really impressed by {specific detail}.

I am spending some time getting to know the {niche} space. {connection point}.

I'd love to learn more about how you think about the business, especially {specific question}.

If you're available over the next few weeks, I'd greatly appreciate a short time to connect.

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
Hope this finds you well. I came across {company} and was impressed by {specific detail}.

Coming from the luxury industry, I'm looking to either build or acquire a business in the {industry} space. {connection point}.

If you'd be open to a conversation, I'd greatly appreciate some time over the next few weeks.

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
- {specific detail} — researched detail about the company (unique per target, never generic)
- {specific question} — researched question about their business (Variant A Day 0 only)
- {niche} — niche name as on tracker (e.g., "art advisory", "fractional CFO")
- {industry} — broader industry term (e.g., "art advisory", "financial advisory", "commercial pest management")
- {connection point} — shared school, mutual contact, location. Omit entirely if none exists.

**What we're testing:** Does transparency about acquisition intent help or hurt response rates? Variant A positions Kay as a curious learner. Variant B is upfront about being a buyer.

**Tracking:** Salesforge tracks variant performance natively. Weekly tracker dashboard (Signal Quality lens) reviews A/B performance per niche. Metrics: response rate, time to response, tone of response (warm vs defensive), conversion to call.

**HARD RULES (apply to BOTH variants):**
- The email is about THEM, not Kay or G&B. Never mention Greenwich & Barrow. Never describe what Kay does. LinkedIn handles credibility (they'll check).
- NEVER reference revenue, employee count, or financial metrics. Could be wrong, and it signals you care about money not legacy.
- NEVER call G&B a "fund." Sounds like PE and kills trust.
- NEVER reveal thesis/growth strategy (underpenetration, consolidation, market size).
- Don't make claims you can't source. Every line must be grounded in real research.
- No em dashes. Periods, commas, line breaks.
- Lead with curiosity about what they've built, even in Variant B.

### Email Verification (ALL Targets — NO EXCEPTIONS)

**NEVER draft an email to an address that was guessed or constructed from name + domain patterns.** If the email address does not come from a verified source (Apollo enrichment, company website, email signature, LinkedIn profile, direct correspondence), do NOT use it. Guessing email formats (e.g., cjanuski@domain.com from "Chris Januski" + domain) burns Kay's sender reputation and wastes outreach. This rule applies EVERYWHERE — inside outreach-manager, inside pipeline-manager, and in ad-hoc conversation drafting.

All targets are enriched via Apollo before reaching outreach-manager. Before drafting, verify the email address status:

```bash
source .env && curl -s "https://api.apollo.io/v1/people/match" \
  -H "Content-Type: application/json" \
  -H "X-Api-Key: $APOLLO_API_KEY" \
  -d '{"first_name":"{first}","last_name":"{last}","organization_name":"{company}","domain":"{domain}"}'
```

**Gate logic based on `email_status`:**
- `verified` → proceed to draft
- `guessed` / `unavailable` / `bounced` → do NOT draft. Note status in Col Q (Agent Notes). Notify Kay: "{owner} at {company} — email not verified ({status}). Skip or find alternate?"
- `pending` → retry once after 5 minutes. If still pending, flag.

**Why:** Bounced emails burn Kay's sender domain reputation. All email addresses are verified via Apollo people match before outreach.

### Pre-Draft Research Brief (REQUIRED before any draft)

Before writing any outreach email, build a research brief for the target. This eliminates Kay's manual research step (she was searching LinkedIn + company website + company LinkedIn for every draft).

**For each target, collect:**
1. **Owner LinkedIn profile:** Background, tenure, posts, mutual connections with Kay, career arc
2. **Company website:** Services offered, team page, about us, any news/press, geographic focus
3. **Company LinkedIn page:** Employee count, recent posts, growth signals, follower count
4. **Search Activity tracker cross-reference:** River guide comments (SD/BN ratings), prior outreach history, snail mail sent
5. **Kay's LinkedIn connections:** Warm intro path (from Attio People cross-reference)
6. **Apollo data:** If available from verification step, any additional context (title, seniority, department)

```bash
# LinkedIn profile (via web search — no LinkedIn API)
WebSearch: "{owner_name} {company_name} LinkedIn"
# Company website
WebFetch: "{company_domain}" with prompt "Extract: services, team, about us, news, geographic focus"
# Company LinkedIn
WebSearch: "{company_name} LinkedIn company page employees"
```

**Embed research into the draft:**
- Weave 1-2 specific details into the email body (not generic "came across your firm")
- Reference something real: their career background, a specific service they offer, their geographic market, years in business

**Flag before drafting (do NOT draft if any of these):**
- Owner appears retired or no longer at the company
- Company appears acquired or part of a larger group
- Company website is down or domain expired
- Owner is a Kay LinkedIn connection (route to warm intro instead of cold)

**Get it right the first time.** Superhuman CLI cannot update or delete drafts. Every draft created is permanent until Kay manually deletes it. Do not create drafts that will need to be replaced.

### Draft Creation

**STOP HOOK: No draft may be created without a completed research brief.** Before calling the Superhuman draft wrapper, verify that the Pre-Draft Research Brief (above) has been completed for this target. Required evidence:
- Owner LinkedIn data extracted
- Company website scanned
- PE ownership checked (hard stop if PE-owned)
- Search Activity tracker cross-referenced
- At least one personalization hook identified

If any of these are missing, HALT and complete the research first. Never create a generic or placeholder draft. Every draft must contain specific details from the research that Kay would otherwise have to look up herself.

**For cold outreach, use Salesforge MCP instead. Superhuman drafts are for warm/relationship emails only.**

For warm intros and relationship emails, draft in Superhuman via the wrapper script (NOT the MCP tool — it uses Gmail API which creates invisible drafts). Use Bash:
```bash
~/.local/bin/superhuman-draft.sh --to "{email}" --subject "Introduction, Greenwich & Barrow" --body "{body}"
```
This creates native Superhuman drafts via CDP. Kay reviews and sends from Superhuman. Sign off "Very best, Kay" only — signature is built in.

For cold outreach, add the contact to a Salesforge sequence via MCP with all personalized variables populated. Salesforge handles sending through Gmail automatically.

**Subject line:** Default to "Intro {first name} & Kay" for all cold outreach. Warm intro emails through Superhuman may use a different subject.

**Attio State Machine:**

Outreach-manager is the only skill that writes to Attio for targets. **No Attio entry exists until Kay approves.** Target-discovery discovering a target does NOT create an Attio record. The sequence:

1. Read the target sheet, find rows where **Col O = "Approve"** that weren't approved in the prior run (new approvals). Col O = "Approve" is the ONLY trigger for Attio entry creation.
2. Verify email via Apollo API. Only proceed if `verified`.
3. For each verified approved target, search Attio for the person AND company:
   - **If found** → someone Kay already knows. Note "WARM INTRO via {connection}" in Col Q, skip cold outreach. This is both the dedup check AND the warm intro check in one step.
   - **If not found** → create the company + person in Attio, add company to Active Deals at "Identified" stage. Proceed with cold outreach.
4. When outreach-manager enrolls target in Salesforge sequence → target stays at "Identified" (enrolled, pending first send)
5. Pipeline-manager reads Salesforge events (email sent, opened, replied) and advances Attio stages: "Identified" → "Contacted" (first email sent) → "Engaged" (reply received)
6. After Day 14 with no response → pipeline-manager moves to nurture cadence

**Key rule:** Targets live on the Google Sheet ONLY until Kay sets Col O = "Approve". The sheet is the staging area. Attio is the pipeline. The approval gate keeps the CRM clean.

### Day 3: JJ's Confirmation Call

**NOTE: JJ is fully decoupled from Salesforge cold outreach cadences.** JJ cannot see Salesforge, so follow-up calls tied to email timing are too fragile. This section applies ONLY to warm intro follow-ups or targets where Kay specifically requests a JJ call.

JJ calls to confirm receipt of Kay's email. This is NOT a cold call — it's a warm follow-up.

**Script:**
```
Hi, this is JJ with Greenwich & Barrow. We sent {owner name} a note
a couple days ago and I just wanted to make sure it came through.
We've been researching the {niche} space and would love to connect
briefly with {owner name} about their experience.
Would {owner name} have a few minutes for a quick call?
```

**JJ positioning:** JJ is a team member at G&B, not an assistant. He speaks as "we" and represents the firm in his own right. Never frame JJ as calling "on behalf of" anyone.

**If the owner wants to schedule a call with Kay:** JJ books a time directly with the owner on the phone, then emails Howie (barrie@greenwichandbarrow.com) with: owner name, owner email, and agreed time. Howie creates the calendar invite and sends it to the owner. Kay gets notified via calendar. JJ does NOT manage Kay's calendar directly.

**Call columns** — JJ works directly from the niche sprint master sheet ("{Niche} - Target List" in TARGET LISTS folder). No separate call list. JJ fills in columns Q-T on the Active tab:
- Col Q: Call Status (dropdown: Not Called, Connected, Voicemail, Callback, Not Interested, Wrong Number, Schedule Requested)
- Col R: Call Date
- Col S: Call Notes
- Col T: Owner Sentiment (dropdown)

**Feedback:** JJ is encouraged to share qualitative observations on Slack anytime (e.g., "owners in this niche seem skeptical" or "getting a lot of voicemails"). This is normal team communication, not a formal process.

See target-discovery/references/drive-locations.md for full column layout.

### Follow-Up Emails

For Salesforge sequences, Day 3 and Day 14 follow-ups are automatic (no manual drafting needed). Salesforge sends them as same-thread replies per the approved templates above.

Manual follow-up drafting applies only to warm/relationship emails sent via Superhuman. For those:

```
Hi {first name},

Just circling back on my note from earlier this week. Would love to find a time to connect.

Kay
```

Draft in Superhuman via CLI. Kay reviews and sends.

### LinkedIn Actions (Connection-Degree Based)

For targets in Salesforge sequences, the Day 6 LinkedIn DM is automated via Salesforge social actions per the approved templates above. The DM must work standalone — the recipient may not have seen the emails. No manual Slack DM drafts needed for sequenced targets.

**Manual Slack DM drafts only for:**
- Warm intros (not in Salesforge)
- Conference outreach (not in Salesforge)
- Targets where Kay specifically requests a manual LinkedIn touch

**DM delivery via Slack (warm intros and conference only):**

One Slack message per DM to #ai-operations containing:
- The drafted DM text (ready to copy-paste into LinkedIn)
- Clickable LinkedIn profile URL (from Col M on target sheet)
- Link to the target's row in the Google Sheet
- Connection degree note

```bash
curl -s -X POST "$SLACK_WEBHOOK_OPERATIONS" \
  -H "Content-Type: application/json" \
  -d '{"text":"LinkedIn DM for {Owner Name} at {Company} ({connection degree}):\n\n{DM text}\n\nLinkedIn: {linkedin_url}\nTarget sheet: {sheet_url}"}'
```

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

**Attio tracking:**
- Salesforge logs LinkedIn actions automatically for sequenced targets
- Pipeline-manager reads Salesforge MCP for LinkedIn action status
- For manual DMs (warm/conference), log "LinkedIn DM - Drafted" as a note on the Attio entry

**Do NOT send LinkedIn DMs on weekends.** Business days only, same as email.

### Warm Intro Handling

Two scenarios trigger a warm intro flag:

**A. Shared Attio connection found** (during outreach-manager warm intro check):
1. Note "WARM INTRO via {connection name}" in Col Q
2. Slack ping to #operations: "Warm intro available: {target owner} at {company}. You're connected to {connection name}. Cold outreach paused for this target."
3. Cold outreach is PAUSED for this target — no Salesforge enrollment, no JJ call scheduled
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

Sorry I missed you at {Conference Name}. Would still love to connect. Do you have a few minutes this week?

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
| T-minus 14 days | Follow-up if no response — "Would love a few minutes before the conference" |
| T-minus 7 days | If connected, ask: "Who should I make sure to meet at {conference}?" |
| Conference day | Meet in person. They introduce Kay to key people. |
| T+1 day | Thank-you email + follow-up on any introductions they made |

### General Intermediary Cadence (non-conference)

For intermediaries identified through niche research, not tied to a specific conference:

| Day | Channel | Action |
|-----|---------|--------|
| Day 0 | Email (Superhuman) | Personalized "learning about the industry" email |
| Day 3 | Email (Superhuman) | Follow-up if no response |
| Day 6 | LinkedIn DM (Kay) | High-value only |
| Day 14 | Email (Superhuman) | Final touch if no response |

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

Draft all intermediary emails in Superhuman via CLI (see Cold Outreach section for exact command). Do NOT use the MCP `superhuman_draft` tool. Intermediary outreach is relationship-building, not cold outreach, so it stays in Superhuman.
</intermediary_outreach>

<essential_principles>
## Principles

### Kay/Camilla Decision Column (Temporary — Testing Phase)
During the testing phase, outreach-manager only drafts outreach for targets where Col O (Kay/Camilla: Decision) = "Approve". Either Kay or Camilla can approve targets. This is a temporary human-in-the-loop gate. Once target-discovery's accept rate stabilizes at 85%+ for 2 consecutive weeks (tracked on Skill Calibration tab of Weekly Tracker), this gate graduates to Spot Check and then Auto-Advance. Kay decides when to graduate — the system proposes it with data.

### Volume & Cadence
- 4-6 cold targets per day (funds that acquired averaged 4, not 9)
- Quality over quantity — deep research on each target, personalized outreach
- Sequenced multi-channel via Salesforge: email Day 0 → follow-up Day 3 → LinkedIn DM Day 6 → final email Day 14
- Conference targets excluded from cold cadence (conference outreach subagent owns that relationship)

### Channel Rules
- **Email (cold):** Via Salesforge sequences (auto-send through Gmail). **Email (warm/relationship):** Via Superhuman drafts. Never Gmail API directly.
- **Phone:** JJ's call sheet in Google Sheets. JJ logs outcomes.
- **LinkedIn DM:** For Salesforge sequences, Day 6 LinkedIn DM is automated. For warm/conference targets, Kay sends manually from LinkedIn. Outreach-manager drafts and delivers via Slack (#ai-operations). Tracked in Attio and Salesforge.
- **All channels:** Same voice, same framing (curiosity, not acquisition pitch).

### Team Roles (for this skill only)
- **Claude:** Deep research per target, draft all emails, build call list, track cadence timing
- **Kay:** Review/send emails, send LinkedIn DMs, take Stage 1 calls
- **JJ:** Confirmation calls from sheet, log outcomes

### Coordination with Other Skills
- **pipeline-manager:** After Day 14 with no response, pipeline-manager takes over with nurture cadence. Outreach-manager does not re-contact nurture targets unless pipeline-manager flags them.
- **weekly-tracker:** Outreach metrics (emails sent, calls made, response rates) feed into the weekly activity tracker.
</essential_principles>

<validation>
## Validation / Stop Hooks

Before reporting completion, run these checks in order. If any check fails, do NOT send the Slack notification. Report the failure and fix it before retrying.

### 0a. Jessica Prior Contact Check (STOP HOOK — before drafting)
Before drafting outreach for ANY company, check if they were previously contacted by Jessica. Cross-reference against the Activity Report (Google Sheet) or check Attio notes for "Cold emailed by Jessica" text. If the company was previously contacted by Jessica, the email MUST be framed as a re-introduction ("We reached out previously and wanted to reconnect"), NOT as cold outreach. A cold email to someone Jessica already contacted looks disorganized.

### 0b. Tracker Verification (STOP HOOK — before drafting)
Before drafting outreach for any target, verify the target is on Kay's tracker (the active niche sprint master sheet in TARGET LISTS folder). If the target is not on the tracker, flag it: "{company} is not on the tracker. Add first or skip?" Do NOT draft outreach for unknown targets.

### 1. Outreach Delivery Validation
**Cold outreach:** Confirm every approved target was enrolled in a Salesforge sequence via MCP (create_contact + enroll_contacts). Verify Salesforge MCP returned success for each contact creation and enrollment. If any failed, flag with the error.
**Warm/relationship emails:** Confirm every email draft was created via the superhuman-cli Bash command (NOT the MCP `superhuman_draft` tool which uses Gmail API). For each target, verify the CLI returned a success response. Drafts must exist in Superhuman's native draft system, not Gmail.

### 2. Call Sheet Validation
**For Salesforge-sequenced targets, this validation is optional.** JJ is decoupled from Salesforge cadences, so call sheet population is not required for cold outreach targets.

For warm intro targets or targets where Kay explicitly requested a JJ call, verify JJ's call columns in the target sheet are populated:
- **Company** — non-empty
- **Owner Name** — non-empty
- **Phone** — non-empty
- **Call Date** — populated per Kay's direction

Missing fields mean JJ can't execute. Fix before proceeding.

### 3. Warm Intro Validation
Confirm Attio People records were checked for every target before drafting. For each target:
- If Col Q (Agent Notes) contains "WARM INTRO" → verify NO cold email was drafted AND no JJ call was scheduled. Warm intros get a different email template and skip JJ entirely.
- If Col Q has no warm intro flag → verify cold outreach was drafted normally.
A cold email sent to a warm intro target wastes the relationship advantage and looks impersonal. This is a hard gate.

### 4. Dedup Validation
Confirm Attio was checked before any drafting began. No person should have outreach queued from both the cold outreach and conference outreach subagents. If a person appears in both queues, conference outreach takes priority and the cold draft must be removed.

### 5. Cadence Tracking
For Salesforge-sequenced cold targets, cadence tracking is handled by Salesforge natively. Verify each target was successfully enrolled in the correct sequence. No JJ call entry is required for Salesforge targets. For warm intro targets where Kay requested a JJ call, verify the call entry exists. Warm intro emails sent via Superhuman should NOT have an automatic Day 3 call entry unless Kay specifically requested one.

### 5b. LinkedIn DM Validation
For Salesforge-sequenced targets with a LinkedIn URL, verify the sequence includes a Day 6 LinkedIn DM node. Salesforge handles this automatically.

For warm/conference targets, verify a LinkedIn DM Slack message was created if the target has a LinkedIn URL in Col M.

Targets without a LinkedIn URL skip LinkedIn actions entirely — this is expected, not a gap.

### 6. Slack Notification (Only After Validation Passes)
Only send once checks 1-5 all pass:
```bash
curl -s -X POST "$SLACK_WEBHOOK_OPERATIONS" \
  -H "Content-Type: application/json" \
  -d '{"text":"Outreach ready — {n} targets enrolled in Salesforge, {n} warm/conference drafts in Superhuman. Review and approve when ready."}'
```
Replace `{n}` with actual counts. If validation failed, report the failure details instead — never send the "ready" notification when outreach is incomplete.
</validation>

<success_criteria>
## Success Criteria

### Daily
- [ ] Cold targets enrolled in Salesforge sequences (confirmed via MCP)
- [ ] Warm/conference email drafts ready for Kay's review in Superhuman
- [ ] No duplicate outreach across funnels (dedup layer verified)
- [ ] Day 6 LinkedIn DM configured in Salesforge sequence for targets with LinkedIn URLs
- [ ] Manual LinkedIn DM drafts delivered via Slack for warm/conference targets only

### Weekly
- [ ] 20-30 owners contacted (email via Salesforge + conference/warm via Superhuman)
- [ ] Pre-conference emails sent for upcoming conferences
- [ ] Post-conference follow-ups drafted within 24 hours
- [ ] Outreach metrics available for weekly tracker (Salesforge stats + Attio stages)
- [ ] Salesforge sequence health check (bounce rates, reply rates, LinkedIn action completion)
- [ ] A/B variant performance reviewed (Signal Quality on weekly tracker dashboard)
</success_criteria>
