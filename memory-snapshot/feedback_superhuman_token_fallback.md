---
name: Superhuman CLI Token Fallback Creates Wrong-Account Drafts
description: When G&B token expires, CLI silently falls back to personal Gmail — always verify account in output before confirming success
type: feedback
---

The Superhuman CLI silently falls back to kaycschneider@gmail.com when the G&B (kay.s@greenwichandbarrow.com) token expires. Drafts get created on the wrong account without any error.

**Why:** Kay discovered drafts in her personal email instead of work email. The CLI logs show "Refreshing token" failures but doesn't error out — it just uses a different account.

**How to apply:** After every Superhuman draft creation, check the CLI output to confirm which account was used. If you see token refresh errors or the wrong account, STOP and tell Kay the token needs refreshing. Never report "draft created" without verifying the correct account.

Re-auth command: `cd ~/.local/share/superhuman-cli && CDP_PORT=9400 bun run src/cli.ts account auth --account kay.s@greenwichandbarrow.com`
