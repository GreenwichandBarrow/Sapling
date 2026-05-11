---
name: Never echo Kay's phone number in chat
description: Kay's phone number is PII and must never appear in conversation output, draft text shown in chat, or memory bodies. When a phone number is needed for a draft or doc edit, route via terminal/file or have Kay update the doc directly. Same family as the never-echo-secrets rule, applied to PII.
type: feedback
originSessionId: d322cf09-a7ad-4a87-93d8-130a9c57bf7f
---
Kay's phone number must never appear in any text Claude outputs to the conversation, including drafts shown for review, memory file bodies, vault notes shown in-chat, briefing text, or any other surface that ends up in the transcript.

**Why:** Chat transcripts are persisted, searchable, and may be shared/reviewed later. PII leaking into transcript history creates downstream privacy exposure that cannot be retracted. Same risk model as API keys, webhooks, and tokens (per `feedback_never_echo_secrets.md` and `feedback_secrets_to_terminal.md`), applied to personal-identifiable information.

**How to apply:**
- When a draft (email, voicemail script, doc edit, etc.) needs Kay's phone number, do NOT ask Kay to paste it in chat. Either:
  1. Have Kay update the destination doc directly (preferred for living docs like the call guide), or
  2. Route via the `/tmp/<file>` method used for secrets — Kay drops the number in a tempfile, Claude reads it via Bash without echoing, uses it in the destination, and clears the tempfile.
- When showing draft text for review, render the phone-number slot as a placeholder like `[phone]` or `[Kay's number]` — never the actual digits.
- If Kay accidentally pastes her phone in chat, do NOT acknowledge or repeat it back; treat the line as if it weren't there for response purposes (similar to secret-handling).
- The same rule applies to any other PII Kay shares (home address, personal cell, family member contact info, financial account numbers).
- Kay shared her phone with JJ via chat between them on 2026-04-30, NOT with Claude. The fact that JJ has the number does not authorize Claude to receive or display it.
