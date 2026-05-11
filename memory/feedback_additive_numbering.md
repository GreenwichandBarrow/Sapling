---
name: Additive numbering across messages in a conversation
description: When presenting numbered items across multiple messages in the same conversation, numbers must be additive — never restart at 1. Kay responds to items by number, so restarting numbering makes her replies ambiguous.
type: feedback
originSessionId: 04cda994-9d0c-4401-8a83-d7e4b3e0cc04
---
Within a single conversation, numbered lists must be ADDITIVE across messages — never restart at 1.

**Why:** Kay responds to items by number (e.g., "3 approve, 5 pass, 7 defer"). If each message restarts numbering, her replies become ambiguous — which message's #3? This has caused re-clarification burn in multiple sessions.

**How to apply:**
- Track the highest number used in the conversation so far
- Next numbered item starts at that number + 1
- Works across sections and across messages
- Exception: a fresh topic that has NO relationship to prior numbered items CAN restart (e.g., morning briefing runs numbering fresh — but within a single threaded workflow, numbering compounds)
- Related rule: `feedback_ascending_numbering` (ascending across all briefing sections, never reset to 1 within a briefing)
