# Monthly Investor Call Prep — Template

**Purpose:** Terse forward-looking call prep for monthly investor 1:1s (currently Jeff Stevens at Anacapa Partners). Max ~40 body lines. Format mirrors `biweekly-call-prep.md` so Jeff and Guillermo briefs feel consistent to Kay.

**Golden reference:** always load the most recent file in `../examples/monthly/` as the format anchor before drafting. If the folder is empty, stop and ask Kay for a golden.

**Vault save:** `brain/briefs/{YYYY-MM-DD}-{person-slug}-call-prep.md`
**Drive save:** INVESTOR COMMUNICATION / MONTHLY folder — `1FGxl4_q44sHK-Kv7t1hHfCMfYXA3H9YW`
**Filename:** `{Investor Last Name} Call Prep {M.DD.YY}` (per `feedback_file_naming`)

---

## Structure (fill each section; keep it tight)

```
{Investor Name} Call Prep — {Month DD, YYYY}

AI Operations
Focus has been on {1-line per recent focus area — skills shipped, system work, C-suite architecture, platform changes, hires}

Conferences.
{booking cadence, notable events attended / upcoming this month}

Interesting conversations
{names of notable recent 1:1s, validation calls, peer meetings since last investor call}

Active Niches — {1-line rank context: "{n} Active-Outreach, {n} Active-Long Term; silent-focus on {top-2}"}
{niche list — current Industry Research Tracker order}

Focus ask for this period:
{Target Kay has set + operational posture — 3 lines max. Example from Guillermo 4/21:
• Fully operational automated system - calls, emails, mail, aggregator
• My time fully spent on owner calls, deal review & conferences
• Surface 1 deal worthy for Jeff & Guillermo}

Upcoming.
{bullets: next 1:1s, conferences, LP milestones, quarterly updates due}

{Questions for {Investor} — 3-4 direct questions, standard closing first}
Any deals or trends you're seeing in the market right now?
{Pressure-test on current thesis or niche stack}
{Pattern-recognition question on current operational gap, if one exists}
{Warm-intro-sourcing ask — deal-triggered, specific niche}
```

## Voice + Content Rules

- **Forward-looking, not retrospective.** Do NOT include Relationship Arc, Prior Call Notes, or Red Flags sections. Those belong in CRM diligence, not investor conversation prep.
- **Terse bulleted, not prose narrative.** Guillermo 4/21 was 27 lines of body text. Match that density.
- **No em dashes** (per `feedback_email_no_em_dashes`).
- **No HoldCo / continuation-vehicle / Bridge-Engine-Community-Jewel language** for traditional-searcher LPs (per `feedback_silent_focus_not_formal_drop` + 4/21-evening disclosure rule).
- **Do NOT ask investor to source deals** (per Wolfe/Stevens/Wasserstein 2025 Yale paper, Figure 4 item #1).
- **Deal-triggered warm-intro asks are fine** — specific to a niche or a live diligence question. Generic "know anyone in X?" asks are not.
- **Standard closing question:** "Any deals or trends you're seeing right now?" Always include.
- **No "Very best, Kay" sign-off** — this is a prep doc, not an email.

## Data Sources to Pull

- Last call note: `brain/calls/{date}-{person-slug}*.md`
- Prior brief: most recent file in `examples/monthly/` + any matching `brain/briefs/*{person-slug}*call-prep*.md`
- Weekly tracker: `gog sheets get 1NGGZY_iq9h8cNzLAXSJ1vTcsfXWNU9oin2RiOMtl9NE 'Weekly Topline'!A:Z --json`
- Industry Research Tracker: `gog sheets get 1vHx4E1tRTR6V3k7NQeHdCrUjDITJVtZA5YPSIFeSins "WEEKLY REVIEW!A3:I20" --json`
- Budget (latest bookkeeper report): `brain/outputs/` search for `budget-manager` or bookkeeper reports
- Recent session decisions: `brain/context/session-decisions-{last-14-days}.md`
- Gmail thread with investor: `gog gmail search "from:{investor-email} OR to:{investor-email}" --max 20 --json`

## Validation Gates

- [ ] Body text under 45 lines (frontmatter not counted)
- [ ] All 7 section headers present (AI Operations, Conferences, Interesting conversations, Active Niches, Focus ask, Upcoming, Questions)
- [ ] At least 3 direct questions, standard closing first
- [ ] No em dashes anywhere
- [ ] No HoldCo/continuation-vehicle language
- [ ] No "ask investor to source deals" framing
- [ ] Vault file + Drive doc both saved; Drive doc in MONTHLY folder
