# Quarterly Investor Update Deck — Template

**Purpose:** 3-slide deck summarizing the quarter, emailed to all 12 G&B investors. Uses Start/Stop/Continue/Pause framework. Triggers follow-up scheduling via Motion tasks.

**Golden reference:** always load the most recent file in `../examples/quarterly/` as the format anchor before drafting. If the folder is empty, pull the most recent quarterly deck from Drive `INVESTOR COMMUNICATION / QUARTERLY / QUARTERLIES SENT` folder (`10xTxhVvuz8dmpwXvTV0j0NHF_ghW-GI5`) and use that as the anchor.

**Fiscal calendar:** Q1 = Feb 7 – May 7, Q2 = May 7 – Aug 7, Q3 = Aug 7 – Nov 7, Q4 = Nov 7 – Feb 7. Delivery deadline: 7 days after quarter end (so Q1 due May 7+7 = May 14, etc., but Kay's policy is deliver AT quarter end — May 7 for Q1).

**Drive save (draft):** INVESTOR COMMUNICATION / QUARTERLY / DRAFTS — `1mAOJgIy1_0QmfjtuHMDZQBg5_AIFsF5u`
**Drive save (sent):** INVESTOR COMMUNICATION / QUARTERLY / QUARTERLIES SENT — `10xTxhVvuz8dmpwXvTV0j0NHF_ghW-GI5`
**Filename:** `G&B Q{N} {YYYY} Investor Update`

---

## Slide Structure

### Slide 1: Executive Summary
- **{STRICTLY CONFIDENTIAL}** header (every slide, required)
- **Q{N} {YYYY}** label
- 3-4 bullet highlights for the quarter — real milestones, not effort logs
- **Investor Ask:** specific, actionable — intros to named industries/verticals, domain-expert connections, pattern-recognition on specific questions. Never "send me deals" (Yale paper rule).

### Slide 2: Start / Stop / Continue / Pause
- **PROGRESS:** Key metric or milestone + budget remaining (`${X}K ({XX}% remaining of $550K raised) [context line]`)
- **START:** New approaches or initiatives this quarter
- **STOP:** What was deprioritized and why (honest, not self-flagellating)
- **PAUSE:** What's on hold and why
- **CONTINUE:** What's working and will keep doing

### Slide 3: Key Learnings + Opportunity Highlights + Strategic Planning
- **CONTINUE:** 3-4 operational learnings from the quarter
- **Opportunity Highlights:** Active deals with coded names (first 2-3 letters), source, status — 1-2 lines each. Never use real company names in LP-facing materials.
- **Strategic Planning:** Next quarter focus (2-3 sentences)

---

## Voice + Content Rules

- Direct and confident, even when reporting challenges
- Frame pivots as strategic decisions, not failures
- Operational improvements (AI tooling, automation) are competitive advantage, not gap-filling
- Honest about what didn't work without being self-deprecating
- **No em dashes** (per `feedback_email_no_em_dashes`)
- **No HoldCo / continuation-vehicle / multi-acquisition / Bridge-Engine-Community-Jewel language** for traditional-searcher LP audience
- **Coded deal names** — first 2-3 letters only (e.g., ACU, HG, PR). Never real company names.
- **Budget line always present** — single inline bullet per `feedback_investor_budget_format`: `$XXK (XX% remaining of $550K raised) [context]`. No extra metrics.

---

## Investor Email Drafts (personalized per investor)

After the deck is approved, draft 12 personalized emails in Superhuman (via `~/.local/bin/superhuman-draft.sh`):

| Investor | Personalization |
|----------|-----------------|
| Jeff Stevens (Anacapa) | Reference recent monthly call topic |
| Guillermo Lavergne (Ashford) | Reference recent biweekly call topic |
| BK Growth, Saltoun, Tom Jackson, Clayton Sachs | Reference recent office conversation if available (co-located) |
| 6 others | General but warm; reference any recent event or touch |

Email structure:
- Warm opener (per `feedback_email_niceties`)
- "Attached is our Q{N} update"
- 1-2 sentence highlight most relevant to that investor
- Investor Ask repeated
- Sign off "Very best, Kay" (per `feedback_sign_off_style`)

---

## Data Sources to Pull

- Weekly tracker (all quarter): `gog sheets get 1NGGZY_iq9h8cNzLAXSJ1vTcsfXWNU9oin2RiOMtl9NE 'Weekly Topline'!A:Z --json`
- Attio pipeline snapshot (Intermediary, Active Deals, Investor lists)
- Niche tracker: `gog sheets get 1vHx4E1tRTR6V3k7NQeHdCrUjDITJVtZA5YPSIFeSins "WEEKLY REVIEW!A:Z" --json`
- Budget: latest bookkeeper report in `brain/outputs/` or Drive BUDGETS folder
- Vault calls this quarter: `Glob brain/calls/{QUARTER_START}*` through `brain/calls/{QUARTER_END}*`
- Session decisions for the quarter: `brain/context/session-decisions-{date}.md` range

## Validation Gates

- [ ] All 3 slides have content (no placeholders)
- [ ] Start/Stop/Continue/Pause present on Slide 2
- [ ] Budget remaining reported in required inline-bullet format
- [ ] All deal names coded (first 2-3 letters only)
- [ ] No em dashes anywhere
- [ ] `STRICTLY CONFIDENTIAL` on every slide
- [ ] 12 personalized email drafts created in Superhuman
- [ ] Motion follow-up tasks created for all 12 investors, due 2 weeks out
- [ ] Deck lives in DRAFTS folder; only moved to QUARTERLIES SENT after Kay's send
