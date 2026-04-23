# Conference Engagement Email Templates — Source of Truth

**Authoritative store:** Google Sheet in G&B Master Templates folder (ID: `19TxdV5GHHbYq_O8YupQ-gkEH7V00iykx`).
**Sheet name:** `G&B Conference Engagement Templates`
**Sheet ID:** stored in `references/templates-sheet.md` after sheet creation.

This markdown is the local reference for the skill. The Google Sheet is what Kay edits directly. Skill reads the Sheet at runtime so Kay's edits propagate immediately.

## Template Variables

| Variable | Meaning |
|----------|---------|
| `{{first_name}}` | Recipient first name |
| `{{conference}}` | Conference name (e.g., "XPX") |
| `{{conference_day}}` | "today" / "yesterday" / "Monday" / "last Tuesday" |
| `{{callback}}` | Specific reference to something they said or a shared topic |
| `{{personalization}}` | Pre-conf only. One-sentence reason this specific person is interesting. |
| `{{reciprocal_hook}}` | Optional. What Kay can offer them (intermediary template). |
| `{{deal_sector}}` | Sector/business they mentioned having on their desk (deal variant only). |
| `{{buy_box_intermediary}}` | Snippet replacement. See Snippets tab. |

## Voice Rules (apply to all templates)

- No em dashes. Use periods, commas, line breaks. See `feedback_email_no_em_dashes`.
- Warm opener on first line ("Hope this finds you well" / "Really enjoyed..."). See `feedback_email_niceties`.
- Sign-off: `Very best,\nKay` only. See `feedback_sign_off_style`.
- Never say "fund" or "PE" or position as institutional. See `feedback_never_say_fund_or_lead`.
- Never leak thesis (no "underpenetrated," no "consolidation play"). See `feedback_outreach_no_strategy_leaks`.
- Curiosity about them first, not Kay's agenda. See `feedback_outreach_about_them`.
- No fake-sounding lines ("your name keeps coming up") unless literally true. See `feedback_outreach_no_fake_lines`.

---

## Snippet: Buy-Box Reference Paragraph (Intermediary)

```
For context on what we are looking for: Greenwich & Barrow is a single-family private investment office acquiring founder-led or family-owned businesses in the US, typically $2-5M EBITDA, with a long-term hold orientation. We focus on operationally critical B2B services businesses where the current owner is thinking about succession, legacy, or stepping back. We move quickly, hold indefinitely, and care more about fit with the owner than maximizing multiples, so we are often a good home for sellers who want to pick their buyer.
```

Used in: `postconf_intermediary`, `postconf_intermediary_deal`, `preconf_intermediary` (optional).
Update in one place (Snippets tab), cascades to all intermediary templates.

---

## Template: `preconf_intermediary`

**Audience:** Intermediary (advisor, wealth manager, M&A, broker, exit planner)
**Mode:** Pre-Conference (T-7 to T-1 before conference)
**Subject:** `{{conference}} next week`

```
Hi {{first_name}},

Hope this finds you well. I saw you are on the {{conference}} attendee list next {{conference_day}} and wanted to reach out.

{{personalization}}

I will be there and would love 15 minutes to say hello. Happy to meet at the venue or grab coffee before or after.

Very best,
Kay
```

---

## Template: `preconf_owner`

**Audience:** Owner (potential seller attending conference)
**Mode:** Pre-Conference (T-7 to T-1 before conference)
**Subject:** `{{conference}} next week`

**Note:** Rare. Only use when attendee list includes an identifiable owner of a target-niche business.

```
Hi {{first_name}},

Hope this finds you well. I noticed you are attending {{conference}} next {{conference_day}} and wanted to introduce myself before the event.

{{personalization}}

I will be there and would love to say hello. No agenda, just wanted to put a face to a name.

Very best,
Kay
```

---

## Template: `postconf_intermediary`

**Audience:** Intermediary
**Mode:** Post-Conference (within 24-48 hours of conference per `feedback_followup_timing`)
**Subject:** `Great meeting you at {{conference}}`

```
Hi {{first_name}},

Really enjoyed our conversation at {{conference}} {{conference_day}}. {{callback}}

{{buy_box_intermediary}}

If anything crosses your desk that fits, I would love to hear. {{reciprocal_hook}}

Very best,
Kay
```

**Usage notes:**
- `{{reciprocal_hook}}` is optional. Examples: "And happy to be a resource if you are ever thinking through a client succession scenario." / "And let me know if I can ever be a reference on the family-office buyer side for one of your advisors." Leave blank if nothing natural.

---

## Template: `postconf_intermediary_deal`

**Audience:** Intermediary who mentioned a specific deal on their desk
**Mode:** Post-Conference
**Subject:** `Great meeting you at {{conference}}`

**Note:** Use this variant when the intermediary pitched Kay a specific business at the conference (e.g., XPX aerospace/defense scenario).

```
Hi {{first_name}},

Really enjoyed our conversation at {{conference}} {{conference_day}}. {{callback}}

You mentioned a {{deal_sector}} business on your desk. I would love to learn more when you have a chance. Happy to sign an NDA and move quickly if it is a fit.

{{buy_box_intermediary}}

Looking forward to talking soon.

Very best,
Kay
```

---

## Template: `postconf_owner`

**Audience:** Owner (potential seller) met at conference
**Mode:** Post-Conference
**Subject:** `Great meeting you at {{conference}}`

**Note:** No buy-box paragraph. No ask. Curiosity only. Owners met at conferences are relationship-first, long-game.

```
Hi {{first_name}},

Really enjoyed our conversation at {{conference}} {{conference_day}}. {{callback}}

Would love to stay in touch. If you are ever in Manhattan, coffee is on me.

Very best,
Kay
```

---

## Template: `postconf_peer`

**Audience:** Peer / ecosystem (other searcher, service provider, fellow LP, family office)
**Mode:** Post-Conference
**Subject:** `Great meeting you at {{conference}}`

```
Hi {{first_name}},

Really enjoyed meeting you at {{conference}} {{conference_day}}. {{callback}}

Keep in touch. If there is ever a way I can be useful, let me know.

Very best,
Kay
```

---

## Subject Line Defaults

| Mode | Default | Alternate |
|------|---------|-----------|
| Pre-conference | `{{conference}} next week` | `{{conference}} on {{conference_day}}` |
| Post-conference | `Great meeting you at {{conference}}` | `Following up from {{conference}}` |

Do NOT use the cold-outreach default `Introduction, Greenwich & Barrow` for conference follow-ups. The conference name is the warm hook.
