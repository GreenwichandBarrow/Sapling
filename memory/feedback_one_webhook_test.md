---
name: One webhook test is enough
description: Only test Slack webhooks once per setup, not every time they're used
type: feedback
---

One test per webhook is enough. Don't test every time a webhook is used. Only re-test if the URL changes.

**Why:** Kay doesn't want unnecessary test messages cluttering Slack channels, especially ones shared with contractors.

**How to apply:** When setting up a new webhook, test once to confirm it works. After that, trust it.
