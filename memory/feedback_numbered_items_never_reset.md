---
name: Numbered list items NEVER reset within a thread
description: Item numbers in numbered lists must ascend monotonically across the entire conversation thread. Never restart at 1 in a new message. Never duplicate a number already used in the same thread.
type: feedback
originSessionId: eadbe8c6-1597-404d-a31b-5cedebba7005
---
When using numbered lists in a thread, the counter must ascend across ALL messages. Never restart at 1 in a new message. Never duplicate a number you've already used elsewhere in the same thread. Keep counting up — Kay explicitly authorized going to 1000 if needed.

**Why:** Kay called this out hard on 2026-05-04: *"Im noticing you duplicated number again. NEVER duplicate item numbers in the same thread NEVER. Just keep counting, you can go to 1000 for all I care."* The friction: when you reset numbers, she has to mentally distinguish "item 1 from earlier conversation" from "item 1 in this message" — adds cognitive load to a fast-moving thread. Ascending numbers give her a single index she can reference anytime ("item 47 — let's discuss").

**How to apply:**
- When in doubt about prior numbering, jump to a safe high baseline (e.g. start at 50 or 100 in a new message rather than restart at 1).
- Better: prefer **bullet points** for unordered/loose lists. Reserve numbered lists for cases where Kay needs to reference an item by number across messages (decisions, action items).
- Briefings already follow this rule per CLAUDE.md ("Numbering ascends across the list, never resets") — extend it to ALL numbered lists, not just briefings.
- This applies WITHIN a single message too: if I produce a list of N items and later in the same message produce another list, the second list continues from N+1, not 1.
- Code/config block snippets (e.g. CSS line numbers, pseudo-code) are exempt — this is about prose lists.

Source: 2026-05-04 broker-channel build session, Kay called out duplicate numbering in a single message that had two parallel sub-lists each starting at 1.
