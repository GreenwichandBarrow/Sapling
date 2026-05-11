---
name: Silence on multi-batch recommendations is not approval
description: When Kay partially responds to a multi-part recommendation, treat unaddressed parts as pending, not approved. Wait for explicit yes per batch before writing.
type: feedback
originSessionId: 29fe887a-b391-45f3-9e99-2be7e94b5ed5
---
When you present Kay a multi-part recommendation (e.g., "here's 30 Work items + 15 Home items + 5 Projects, approve?") and she partially responds (e.g., revises only the Home list), do NOT treat her silence on the other parts as approval. Wait for explicit yes on each batch before writing.

**Why:** Caught 2026-04-27 during the Motion → personal task tracker import. Presented Work + Home + Projects together. Kay revised only Home. I read silence on Work as approval and wrote 35 Work items. She caught it: *"it seems like you put things on the work list in the file that you had dropped in the review to me in this chat."* Had to delete 17 items and rewrite. The rollback cost (delete + rewrite + apology) was much higher than the wait would have been (one extra round trip).

**How to apply:** When Kay's response to a multi-part recommendation only addresses some parts, before writing the remainder, surface them again briefly: "I'll wait for your call on the Work list before writing. Approve as-is or want changes?" Default to *wait*, not *act*. This is distinct from `feedback_decision_fatigue_minimization` (which is about framing the ask as RECOMMEND + YES/NO/DISCUSS) — the Obama framing still requires the yes. It's also distinct from `feedback_never_batch_changes_without_review` (which is about CRM-style batches); this generalizes to any multi-item write triggered by partial-response approval.
