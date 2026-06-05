# Monthly Investor Call Prep — Template

**Purpose:** Terse forward-looking call prep for monthly investor 1:1s (currently Jeff Stevens at Anacapa Partners). Max ~40 body lines. Format mirrors `biweekly-call-prep.md` so Jeff and Guillermo briefs feel consistent to Kay.

**Golden reference:** always load the most recent file in `../examples/monthly/` before drafting. It is a format anchor only where it does not conflict with the current rules below. Current rule wins over older examples: numbered situational sections, `Insight:` lines, tight 2-4 line bodies, and no standalone questions section. If the folder is empty, stop and ask Kay for a golden.

**Vault save:** `brain/briefs/{YYYY-MM-DD}-{person-slug}-call-prep.md`
**Drive save:** INVESTOR COMMUNICATION / MONTHLY folder — `1FGxl4_q44sHK-Kv7t1hHfCMfYXA3H9YW`
**Filename:** `{Investor Last Name} Call Prep {M.DD.YY}` (per `feedback_file_naming`)

---

## Structure (rendered Doc body — situational, NOT canonical)

```
{Investor Name} Call Prep — {Month DD, YYYY}
Insight: {one-sentence meta-takeaway across all sections}

1. {Situational Topic 1}
{2-4 line body covering what moved since last live call}
Insight: {one-line takeaway}

2. {Situational Topic 2}
{2-4 line body}
Insight: {one-line takeaway, if genuine}

3. {Situational Topic 3}
{2-4 line body}

4. Active Niches. {short context line}
* {Niche 1} — {descriptor}
* {Niche 2} — {descriptor}
* {Niche 3} — {descriptor}

5. Upcoming.
- {item 1}
- {item 2}

{Optional closing line: one-sentence target Kay is carrying into the cadence}
```

Number of sections: 5-7 typical. Driven by what actually moved, not a fixed checklist.

## Voice + Content Rules

- **Forward-looking, not retrospective.** Do NOT include Relationship Arc, Prior Call Notes, or Red Flags sections. Those belong in CRM diligence, not investor conversation prep.
- **Numbered situational sections, not thematic walls.** Use topics that reflect what actually moved since the last live call. Do not use fixed thematic headers when there is no movement.
- **Terse, not prose narrative.** Keep each section body to 2-4 lines.
- **No em dashes** (per `feedback_email_no_em_dashes`).
- **No HoldCo / continuation-vehicle / Bridge-Engine-Community-Jewel language** for traditional-searcher LPs (per `feedback_silent_focus_not_formal_drop` + 4/21-evening disclosure rule).
- **Do NOT ask investor to source deals** (per Wolfe/Stevens/Wasserstein 2025 Yale paper, Figure 4 item #1).
- **Deal-triggered warm-intro asks are fine** — specific to a niche or a live diligence question. Generic "know anyone in X?" asks are not.
- **No standalone Questions section.** Questions live in Kay's head; include only an optional one-sentence target or commitment if it clarifies the call posture.
- **No "Very best, Kay" sign-off** — this is a prep doc, not an email.

## Data Sources to Pull

- Last call note: `brain/calls/{date}-{person-slug}*.md`
- Prior brief: most recent file in `examples/monthly/` + any matching `brain/briefs/*{person-slug}*call-prep*.md`. If older examples include a Questions section, treat that as superseded by this template.
- Weekly tracker: `gog sheets get 1NGGZY_iq9h8cNzLAXSJ1vTcsfXWNU9oin2RiOMtl9NE 'Weekly Topline'!A:Z --json`
- Industry Research Tracker: `gog sheets get 1vHx4E1tRTR6V3k7NQeHdCrUjDITJVtZA5YPSIFeSins "WEEKLY REVIEW!A3:I20" --json`
- Budget (latest bookkeeper report): `brain/outputs/` search for `budget-manager` or bookkeeper reports
- Recent session decisions: `brain/context/session-decisions-{last-14-days}.md`
- Gmail thread with investor: `gog gmail search "from:{investor-email} OR to:{investor-email}" --max 20 --json`

## Validation Gates

- [ ] Body text under 45 lines (frontmatter not counted)
- [ ] 5-7 numbered situational sections present
- [ ] `Insight:` line at top and under sections where there is a real takeaway
- [ ] No standalone Questions section
- [ ] No em dashes anywhere
- [ ] No HoldCo/continuation-vehicle language
- [ ] No "ask investor to source deals" framing
- [ ] Vault file + Drive doc both saved; Drive doc in MONTHLY folder
