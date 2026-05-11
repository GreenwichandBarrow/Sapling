---
name: Subagent safety rule — validate inputs before batch sheet writes
description: Subagents running shell loops that write to Google Sheets must validate loop-index variables and tab names are non-empty BEFORE calling gog sheets update. Empty values silently write to wrong ranges and can clobber production data.
type: feedback
originSessionId: 04cda994-9d0c-4401-8a83-d7e4b3e0cc04
---
When delegating subagent work that involves batch updates to Google Sheets (or any other high-value system of record), the subagent MUST validate inputs before every write, especially in shell loops.

**Known failure mode (discovered 2026-04-17):**
A subagent running `jj-operations prep` used a zsh array with 0-indexing on the first iteration, leaving `tab_name` as an empty string. The gog CLI silently accepted the empty tab reference and wrote the payload to `Full Target List!A1:W41` instead of the intended `Call Log 4.20.26!A1:W41`, **clobbering the first 41 rows of the master Premium Pest Management target sheet**. Caught by luck because the subagent took a snapshot to `/tmp` before writes. No data lost, but this was one mistake away from a production data incident.

**Rules for subagent prompts involving sheet writes:**

1. **Never use zsh for loops over array indices that write to sheets.** Use bash. Zsh's 1-indexed arrays + 0-indexed fallback create silent-corruption class bugs.
2. **Validate every target range before every write.** If a tab_name / sheet_id / range variable is empty or matches a master / source tab, ABORT the write and surface an error.
3. **Pre-write snapshot.** Before any batch write, snapshot the affected range to `/tmp` as rollback material. Don't trust the subagent to do this unprompted — explicitly require it in the prompt.
4. **Dry-run first when batch writing.** For loops with ≥3 iterations, do the first iteration in dry-run mode (log the intended target, don't execute), then proceed if the target is sane.
5. **Guard rail on target ranges.** Never write to a tab named "Full Target List", "Master", or any unprefixed name via loop automation. Those tabs should only be modified by a designated harvest step with explicit intent.

**How to apply:**
- When spawning a subagent that writes to Google Sheets, include these rules in the subagent prompt explicitly.
- When reviewing subagent output, check for "restore from snapshot" language — that's a signal that a near-miss happened.
- If a subagent reports data restoration from `/tmp` snapshot, treat it as a P0 event requiring a trace file + skill-hardening plan.

**Why this exists:** Silent sheet corruption is unrecoverable if not caught in-session. Source-of-truth sheets (master target lists, investor tracker, industry research tracker) get downstream-read by every skill. One bad write cascades for days before being noticed.
