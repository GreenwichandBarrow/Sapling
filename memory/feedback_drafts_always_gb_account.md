---
name: Drafts always go to G&B account
description: All Superhuman drafts must use kay.s@greenwichandbarrow.com, never personal email accounts
type: feedback
---

All Superhuman email drafts MUST go to the G&B account (kay.s@greenwichandbarrow.com). Never use personal accounts (kaycschneider@gmail.com, etc.).

**Why:** A draft landed in Kay's personal Gmail instead of G&B because the token was expired and the CLI fell back to a personal account silently.

**How to apply:**
- Always specify `--account "kay.s@greenwichandbarrow.com"` when creating drafts
- If the token is expired, re-auth FIRST (`account auth` via CDP), then create the draft
- Never let the CLI silently fall back to another account — if auth fails, fix it before drafting
- Verify the draft confirmation shows `kay.s@greenwichandbarrow.com` in the account field
