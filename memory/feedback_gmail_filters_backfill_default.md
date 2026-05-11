---
name: Gmail filter creation must always backfill existing matching messages
description: When creating Gmail filters, always apply the new label to existing matching messages in addition to filtering future mail. Never create a filter that only acts on incoming mail.
type: feedback
originSessionId: 54785998-5c5c-4c8d-956a-e32941f2ea6d
---
**Rule:** Every Gmail filter creation must include a backfill step that applies the new label to all existing matching messages in the mailbox, not just future incoming mail.

**Why:** Gmail's API filter create only acts on incoming mail going forward. The web UI exposes an "Also apply filter to N matching conversations" checkbox; the API doesn't. Without explicit backfill, the user's historical inbox stays unlabeled — defeating most of the value of setting up the filter (the existing pile is what's overwhelming, not future trickle). Stated by Kay 2026-04-26 after first round of `auto/...` filter creation: "should always check apply labels to all matching messages already in gmail."

**How to apply:**
- After every successful `gog gmail filters create` call, immediately run the equivalent search + label-apply for existing messages: `gog gmail search '<query>'` → `gog gmail thread modify --add-label='<label>' <thread-ids>` (or batch equivalent).
- Default behavior, not opt-in. Don't ask "do you want backfill?" — just do it.
- If the matching set is unusually large (>1000 threads), surface the count and confirm before proceeding, since broad backfills may be irreversible feeling and noisy.
- Holds for any client (Gmail filters, Apple Mail rules, any new auto-classification setup): create rule + retroactively apply.
