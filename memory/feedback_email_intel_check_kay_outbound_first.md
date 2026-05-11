---
name: Email-intelligence — verify Kay's outbound on thread before flagging "needs reply"
description: Before surfacing any email thread as a "needs reply" actionable item, email-intelligence MUST cross-reference Kay's Sent folder for outbound on the same thread. If Kay has replied since the last inbound she's "responding to," suppress.
type: feedback
originSessionId: aaa7fafb-587f-4eef-b828-ac937c5c9b99
---
Email-intelligence threads-needing-reply filter must check Kay's outbound on the thread before classifying as actionable.

**Why:** 2026-05-07 morning briefing surfaced Jackson Niketas (Terra Mar) AI-coaching scheduling as 🟡 needing reply. Kay had already replied 2026-05-06 09:02 ET; thread had 3 messages (Jackson inbound → Kay reply → Jackson back-reply). Email-intelligence flagged because the latest message was inbound from Jackson, but didn't recognize that Kay's prior reply had answered the original ask (window-pick) and Jackson's third message was a routine confirmation/calendar invite ack, not a new question.

The thread-level signal "latest message is inbound" is necessary-but-not-sufficient for "needs reply." Required logic:
1. Find latest inbound message timestamp on thread
2. Check if Kay has any outbound on the thread between (latest inbound from counterparty asking a question) and (now)
3. If yes → suppress, OR demote to "thread continued — verify if action remains" with low urgency
4. Only flag as actionable if Kay has NEVER replied to the original ask, OR the latest inbound contains a new explicit ask

**How to apply:**
- Email-intelligence skill (`actionable items` table) — add outbound-cross-reference step before tagging urgency.
- Pipeline-manager — when reading email-scan-results, treat any "🟡 needs reply" item that has Kay outbound within last 48h on the same thread as suppressed-by-default; surface only if Kay's outbound was clearly a non-answer (e.g., "let me check and get back").
- Same fix applies to relationship-manager dropped-ball detection — Kay's outbound on a thread = engagement, regardless of whether the counterparty has back-replied.

**Quick check pattern:** `gog gmail read {thread_id} -j` shows full thread with `from` per message. If any message in the thread is `from: Kay Schneider` and is newer than the original-ask inbound, the thread is engaged.
