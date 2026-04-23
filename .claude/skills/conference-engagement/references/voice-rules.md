# Voice Rules — Conference Engagement Emails

All voice rules below apply to every template in this skill.

## Formatting

- **No em dashes.** Use periods, commas, or line breaks instead. (`feedback_email_no_em_dashes`)
- **Warm opener on first line.** "Hope this finds you well" / "Really enjoyed meeting you at {{conference}}" / "Hi {{first_name}}". (`feedback_email_niceties`)
- **Sign-off:** `Very best,\nKay` only. Superhuman's built-in signature handles the rest. Never add title, firm name, contact info, or signature block in the body. (`feedback_sign_off_style`)
- **Paragraph breaks between ideas.** Don't wall-of-text. Short paragraphs (1-3 sentences).

## Language to Avoid

- **Never say "fund" or "private equity" or position as institutional.** G&B is a single-family private investment office. (`feedback_never_say_fund_or_lead`, `feedback_never_say_fund`)
- **Never leak thesis.** Forbidden words: "underpenetrated," "consolidation play," "roll-up," "platform," "tuck-in," "arbitrage," "multiple expansion." These are internal thesis vocabulary, not owner/intermediary vocabulary. (`feedback_outreach_no_strategy_leaks`)
- **No fake-sounding lines.** "Your name keeps coming up" / "I've been following your work" unless literally true. (`feedback_outreach_no_fake_lines`)
- **Never reveal revenue or employee count in owner outreach.** Buy-box EBITDA is OK for intermediaries (they expect it) but never for owner outreach. (`feedback_no_revenue_in_outreach`)
- **Never use "Kay" inside the body.** The body is signed by Kay; referring to "Kay" in third person is weird. (`feedback_no_name_in_deliverables` adapted)

## Language to Use

- **"Greenwich & Barrow"** when naming the firm. Never abbreviate to "G&B" externally (internal only).
- **"Single-family private investment office"** when describing G&B. Alternatives: "family investment office," "private investment office." Never "fund" or "PE firm."
- **"Founder-led or family-owned businesses"** when describing buy-box.
- **"Long-term hold"** or **"hold indefinitely"** (not "buy and hold" which sounds PE).
- **"We move quickly"** / **"happy to move fast"** — conveys execution without PE-speak.
- **"Fit with the owner"** / **"home for the business"** — relationship-first framing consistent with the Alain Wertheimer / Wedgwood archetype.

## Subject Lines

- Pre-conference: `{{conference}} next week` or `{{conference}} on {{conference_day}}`
- Post-conference: `Great meeting you at {{conference}}` (default) or `Following up from {{conference}}`
- **Do NOT** use the cold-outreach default `Introduction, Greenwich & Barrow`. The conference is the warm hook; use it.

## Superhuman Delivery

Drafts go into Superhuman via the CLI wrapper:

```bash
~/.local/bin/superhuman-draft.sh --to "{email}" --subject "{subject}" --body "{body}"
```

**Never use the MCP `superhuman_draft` tool.** That routes through Gmail API and creates invisible drafts Kay never sees. (`feedback_drafts_superhuman`)

Kay reviews in Superhuman, customizes the `{{callback}}` and any other per-recipient touches, and hits send. Claude drafts; Kay sends. No third-party tool ever touches Kay's SMTP.

## What Goes Where

| Content | Intermediary | Owner | Peer |
|---------|--------------|-------|------|
| Warm opener | YES | YES | YES |
| Specific callback to conversation | YES | YES | YES |
| Buy-box paragraph ($2-5M EBITDA) | **YES** | NO | NO |
| Ask for deal flow ("keep me in mind") | YES | NO | NO |
| Reciprocal value hook | Optional | NO | NO |
| Curiosity question about their work | Optional | **YES** | Optional |
| Stay-in-touch close | YES | YES | YES |
| Coffee invitation | Optional | YES | NO |

## Quality Bar

Before any draft leaves for Superhuman:

1. [ ] No em dashes
2. [ ] Warm opener on line 1
3. [ ] Specific callback (not generic). If unknown, escalate to Kay.
4. [ ] Correct template per audience (no buy-box leak into Owner or Peer drafts)
5. [ ] Sign-off is `Very best,\nKay` and nothing more
6. [ ] Subject matches mode defaults
7. [ ] No forbidden vocabulary ("fund," "underpenetrated," etc.)
8. [ ] No "Kay" in third person inside the body
