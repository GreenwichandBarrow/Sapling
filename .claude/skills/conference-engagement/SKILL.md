---
name: conference-engagement
description: "Pre-conference outreach and post-conference follow-up lifecycle. Runs T-7 to T+2 around any conference Kay attends. Drafts personalized emails from attendee lists (pre) and business cards (post). Uses the 3-audience taxonomy (Intermediary / Owner / Peer) and pulls templates from the G&B Conference Engagement Templates sheet."
user_invocable: true
context_budget:
  skill_md: 3000
  max_references: 2
  sub_agent_limit: 2000
---

<objective>
Own everything from T-7 days before a conference through T+2 days after. This is the companion skill to `conference-discovery` (upstream, which finds and registers).

**Inputs from other skills:**
- `conference-discovery` hands off confirmed attendance (conference name, date, venue, attendee list if acquired)
- Kay directly sends business cards (photo) after the event

**Outputs to other skills:**
- `outreach-manager` (conference-outreach subagent) receives drafted emails for Superhuman delivery
- `relationship-manager` receives new contacts for cadence setup
- `tracker-manager` writes Attio entries for new contacts (tag source=conference/{slug}-{date})
- `river-guide-builder` receives intermediary cards as river-guide candidates
- `deal-evaluation` is triggered if an intermediary pitched a specific deal (use `postconf_intermediary_deal` variant and route to active-deal fast-path)

**Why this matters:** Per `feedback_in_person_conferences_highest_roi`, 1 in-person conference/week is G&B's highest-ROI deal-sourcing channel (validated XPX wk 2 = live aerospace deal pitched). Follow-up within 24 hours is what converts warm conference contact into durable pipeline. Per `feedback_engine_architecture`, Kay's time is for owners and intermediaries; every step of the pre/post process runs without her manual effort except the final Superhuman review and send.

**Seller psychology to encode in messaging:** Per `feedback_seller_short_transition_matters`, founder-led sellers in the $2-5M EBITDA band are allergic to long post-close transition obligations. The buy-box paragraph handles this implicitly via "customized terms" — never mention transition length explicitly in outreach. In first owner calls and LOI defaults, bias toward short (3-6mo) transition unless seller asks for more.
</objective>

<essential_principles>
## When to Trigger

**Pre-conference mode:**
- `conference-discovery` confirms Kay is registered for a conference
- 7 days before the event: run pre-mode. Identify high-priority attendees. Draft outreach. Queue sends for Mon AM (never Sunday per `feedback_no_sunday_emails`).

**Post-conference mode:**
- Kay sends a photo of business cards collected at the event
- Within 24 hours of conference end, per `feedback_followup_timing`
- Active deal fast-path if an intermediary pitched a specific deal at the conference (per `feedback_active_deal_urgency`)

## Audience Taxonomy (3 buckets, per `feedback_audience_taxonomy_conferences`)

1. **Intermediary** — advisors, wealth managers, M&A, brokers, exit planners, CPAs, attorneys, bankers. Gets the buy-box reference paragraph.
2. **Owner** — potential sellers. No buy-box. No ask. Curiosity only.
3. **Peer / Ecosystem** — other searchers, service providers, fellow LPs, family offices. Simple stay-in-touch.

Never create a fourth "advisor" bucket. Advisors are intermediaries.

## Template Store (Single Source of Truth)

All email templates and the buy-box snippet live in ONE Google Sheet:

- **Sheet name:** `G&B Conference Engagement Templates`
- **Sheet ID:** `1Y4XcQJDe28RB7k_Cw5NZNjKRyX4d1qEczadXdQrjpaQ`
- **Folder:** G&B Master Templates (`19TxdV5GHHbYq_O8YupQ-gkEH7V00iykx`)
- **URL:** https://docs.google.com/spreadsheets/d/1Y4XcQJDe28RB7k_Cw5NZNjKRyX4d1qEczadXdQrjpaQ/edit

**Tabs:**
- `Templates` — 6 templates: `preconf_intermediary`, `preconf_owner`, `postconf_intermediary`, `postconf_intermediary_deal`, `postconf_owner`, `postconf_peer`
- `Snippets` — reusable fragments: `buy_box_intermediary` ($2-5M EBITDA paragraph)
- `README` — usage guide

**Read from the sheet at every run.** Kay edits templates directly in the sheet; the skill must pick up her edits immediately. Never cache or hard-code template content.

**Buy-box paragraph is Kay-authored.** The `buy_box_intermediary` snippet in the Snippets tab was written by Kay (2026-04-23) and uses first-person voice ("I am looking to acquire..."). Do NOT regenerate or "improve" this paragraph without Kay's explicit authorization. It encodes G&B's positioning deliberately, including the "customized terms" phrase that handles seller transition flexibility without quoting the anxiety back at them.

```bash
gog sheets get {SHEET_ID} "Templates!A2:F10" --json
gog sheets get {SHEET_ID} "Snippets!A2:C10" --json
```

## Business Card Handling (per `feedback_business_cards_no_enrichment`)

Cards handed to Kay in person are GOLD. Use them verbatim.

- **Never run Apollo enrichment on card data.** A card is a direct handoff, more authoritative than any lookup.
- **Do run Attio dedup** (new vs existing contact). This is deduplication, not enrichment.
- If a field is missing from the card (e.g., no email), ask Kay once or skip that channel. Never guess.

## Voice (all templates)

- No em dashes (per `feedback_email_no_em_dashes`)
- Warm opener on first line (per `feedback_email_niceties`)
- Sign-off: `Very best,\nKay` (per `feedback_sign_off_style`)
- Never say "fund" or "PE" (per `feedback_never_say_fund_or_lead`)
- Never leak thesis (per `feedback_outreach_no_strategy_leaks`)
- Curiosity about them first (per `feedback_outreach_about_them`)
- No fake lines (per `feedback_outreach_no_fake_lines`)
</essential_principles>

<pre_conference_mode>
## Pre-Conference Mode (T-7 to T-1)

### Inputs
- Conference name, date, venue
- Attendee list (from `conference-discovery` output, if acquired)

### Flow

1. **Read attendee list.** Parse into structured rows (name, title, company, email if available).

2. **Classify each attendee by audience** using the taxonomy above. Cross-reference Attio:
   - Existing target-niche owners → Owner
   - Existing Intermediary Pipeline entries → Intermediary
   - Unknown person at a firm that matches intermediary patterns (wealth mgmt, M&A, law, accounting, exit planning, brokerage) → Intermediary
   - Everyone else → Peer (low priority, skip unless specifically relevant)

3. **Prioritize** (draft outreach only to high-value contacts — 15-25 per conference, not the whole list):
   - Intermediaries: prioritize those in target G&B geographies (tri-state) and target sectors
   - Owners: prioritize those in Active-Outreach niches
   - Cap total pre-conference drafts at 25 per event to keep quality high

4. **Read templates** from the Google Sheet (`preconf_intermediary` or `preconf_owner`).

5. **Draft each email** in Superhuman via `~/.local/bin/superhuman-draft.sh`:
   - Populate variables: `{{first_name}}`, `{{conference}}`, `{{conference_day}}` (e.g., "Thursday"), `{{personalization}}` (one specific reason this person is interesting based on their firm/background)
   - Queue for Monday morning send (never Sunday per `feedback_no_sunday_emails`)
   - `{{buy_box_intermediary}}` optional in pre-conf (skip unless natural; buy-box hits harder post-conference when relationship is fresh)

6. **Log to Attio:** pre-conference touch on each contact, tagged `source=conference/{slug}-{date}`.

7. **Hand off to Kay** via morning briefing: "N pre-conference drafts in Superhuman for {Conference} on {date}."

### Draft Quality Bar
- Every `{{personalization}}` must be specific and defensible. If nothing specific is known about the person, escalate to Kay or skip.
- Never use generic filler ("impressive work in the industry"). Either have a concrete hook or don't draft.
</pre_conference_mode>

<post_conference_mode>
## Post-Conference Mode (T+0 to T+2)

### Inputs
- Photo (or multiple photos) of business cards Kay collected at the event
- Conference name + date
- Any Granola transcript from the event (if run)
- Kay's notes on specific conversations (optional)

### Flow

1. **OCR each card.** Extract: name, title, company, email, phone, LinkedIn (if printed). Use card data verbatim.

2. **Attio dedup.** For each person:
   - Search Attio People by email (primary) and name+company (fallback)
   - Match found → log a new touch on existing record
   - No match → create new People record with `source=conference/{slug}-{date}`

3. **Classify by audience** (Intermediary / Owner / Peer). Cues:
   - Firm type: M&A, wealth, law, accounting, exit planning, banking, brokerage → Intermediary
   - Firm type: operator / business owner / CEO of private business → Owner
   - Firm type: searcher, service provider, family office, VC/PE → Peer
   - If ambiguous, escalate to Kay for classification with card detail

4. **Detect deal-mentioned subset.** If Granola transcript or Kay's notes indicate a specific intermediary pitched a deal:
   - Use `postconf_intermediary_deal` variant instead of `postconf_intermediary`
   - Trigger active-deal fast-path (per `feedback_active_deal_urgency`)
   - Flag for `deal-evaluation` skill pickup

5. **Read templates** from the Google Sheet. For intermediary templates, substitute `{{buy_box_intermediary}}` with the content of that row from the Snippets tab.

6. **Draft each email** in Superhuman:
   - `{{first_name}}` from card
   - `{{conference}}` = conference short name (e.g., "XPX")
   - `{{conference_day}}` = "today" if same-day, "yesterday" if next-day, otherwise day name
   - `{{callback}}` = specific reference to something they said (from Granola transcript or Kay's notes). If no specific callback exists, escalate to Kay or leave a placeholder for her to fill in Superhuman.
   - `{{reciprocal_hook}}` (intermediary only) = what Kay can offer them. Leave blank if nothing natural.
   - `{{deal_sector}}` (deal variant only) = the business/sector the intermediary mentioned.

7. **Use Superhuman CLI** (per `feedback_drafts_superhuman`):
   ```bash
   ~/.local/bin/superhuman-draft.sh --to "{email}" --subject "{subject}" --body "{body}"
   ```
   Never use the MCP `superhuman_draft` tool — that routes through Gmail API and creates invisible drafts.

8. **Attio updates:**
   - New contact: create People record, link to conference, set nurture cadence via `relationship-manager`
   - Existing contact: add touch note, update `last_contacted_at`

9. **River guide candidates:** any intermediary card gets flagged for `river-guide-builder` evaluation (next run).

10. **Summary to Kay:**
    ```
    Post-Conference Follow-up — {Conference}
    {N} cards processed:
    - {X} Intermediaries (includes {Y} deal-mentioned)
    - {A} Owners
    - {B} Peers
    All drafts in Superhuman awaiting review.
    ```

### Validation
- Every card produces exactly one draft (or a documented skip reason)
- Every `{{callback}}` is specific or escalated to Kay (no generic "enjoyed meeting you")
- Every intermediary draft includes the buy-box paragraph
- No owner or peer draft includes the buy-box paragraph
- No em dashes in any draft body
</post_conference_mode>

<quick_start>
## Execution Flow (Post-Conference, the common case)

```
Kay: "Here are the 8 cards from XPX" [sends photo]
↓
1. OCR photo → 8 card records
2. Attio dedup → N new / M existing
3. Classify by audience
4. Read templates from sheet
5. Draft 8 personalized emails in Superhuman
6. Create/update 8 Attio records
7. Report back: "8 drafts in Superhuman. Breakdown: X intermediaries, Y owners, Z peers."
```

Kay reviews each draft in Superhuman, customizes the `{{callback}}` where needed, hits send.
</quick_start>

<template_review_workflow>
## Template Review Workflow (Before Bulk Drafting)

Whenever a template changes (new variant added, buy-box paragraph edited, voice rule shifts) OR the skill is running for the first time in a new conference context, follow this workflow BEFORE pushing N drafts to Superhuman:

1. **Create a review Google Doc** in the G&B Master Templates folder (ID `19TxdV5GHHbYq_O8YupQ-gkEH7V00iykx`) named `G&B Post-Conference Email Templates` (or similar purpose-specific name).
2. **Render each template** with sample/illustrative variables filled in — NOT template string with `{{placeholders}}`. Kay needs to see how the email actually reads.
3. **No rule preambles in the doc.** Per `feedback_rules_in_skill_not_template`, the review doc shows ONLY templates. Voice rules, validation, workflow — all of that lives in SKILL.md and `references/`. Do NOT put "voice rules baked in:" or "how to use this doc" sections in the review doc.
4. **Kay reviews.** She can edit language directly in the doc or say APPROVE.
5. **Sync her edits back** to the authoritative Templates/Snippets tabs of the Sheet.
6. **Only then** push the N personalized drafts to Superhuman.

This workflow exists because reviewing 1 template is a lower decision cost than rejecting N drafts. Per `feedback_decision_fatigue_minimization`, minimize Kay's decision surface — 1 template approval vs 8 draft rejections is an 8x improvement.
</template_review_workflow>

<references>
## Further Reading

- `references/voice-rules.md` — full voice and formatting conventions
- `references/audience-classification.md` — how to classify ambiguous cards
- `references/templates-sheet.md` — sheet structure and variable substitution logic
- `templates/email-templates.md` — local copy of all templates (sheet is authoritative)
</references>
