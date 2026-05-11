---
name: No clear+rewrite of populated sheets
description: Never use the "clear all data rows then rewrite from scratch" pattern on a populated Google Sheet, especially in a subagent that may time out mid-rewrite
type: feedback
originSessionId: e323b4e0-bf25-4d39-b46f-cbb9be95e424
---
Never use the "clear all data rows then rewrite from scratch" pattern on a populated Google Sheet, especially when the operation runs in a subagent that may hit a stream timeout.

**Why:** 2026-05-03, conference-discovery archival subagent cleared the Conference Pipeline tab (~70 rows) as Step 1 of a "clear → rewrite remaining rows" pattern, then hit Stream idle timeout before the rewrite step. Result: total Pipeline data loss. Recoverable only via Sheets Version History restore. The clear+rewrite pattern looks atomic in code but is two API calls, and any failure between them = catastrophic data loss.

**How to apply:** For Google Sheets archival/cleanup operations:
- **Per-row deletes only.** Move row → confirm append succeeded → delete that one row → next row. Each row is independently recoverable.
- **Never clear a range > 5 rows in a single call** unless the destination has already received the appended copy AND verified.
- **No "rewrite from scratch" patterns** on populated tabs. Update specific ranges only.
- **No subagent for destructive sheet ops longer than 5 minutes.** Stream-idle timeout > rollback. If the work is large, drive it from the parent agent so context isn't lost on timeout.
- **Snapshot before destruction.** Before any multi-row delete, write the current state to `/tmp/sheet-snapshot-{date}-{tab}.json` so a restore is possible without Version History.

This rule supersedes the "rewrite Pipeline with: header row + all non-archived rows" instruction in the conference-discovery skill's archival section. That instruction caused the incident — it should be edited to use per-row deletes instead.
