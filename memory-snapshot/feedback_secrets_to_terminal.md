---
name: Always route secrets to terminal, never to chat
description: API keys, webhooks, tokens — always instruct Kay to paste in terminal, never in conversation. Multiple key rotations caused by this.
type: feedback
---

Always instruct Kay to put sensitive values (API keys, webhook URLs, tokens, passwords) directly into their terminal, never paste them into the conversation.

**Why:** Multiple incidents where keys/webhooks shared in conversation had to be rotated afterward. The conversation is not a secure channel for secrets.

**How to apply:** Whenever Kay needs to provide a secret value, proactively say "paste this directly in your terminal" and give them the exact command (e.g., `echo "paste-key-here" > /tmp/keyname.txt`). Never ask them to share the value in chat. This applies to API keys, webhook URLs, OAuth tokens, passwords, and any other credentials.
