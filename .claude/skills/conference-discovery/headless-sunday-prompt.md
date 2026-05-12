# Headless Conference-Discovery — Sunday-Night Weekly Run

**You are running as a non-interactive scheduled job.** No human is on the
other end of this conversation. Every choice you make happens silently and
must be defensible by output, not by clarifying question.

## Hard rules for this run (violations = silent failure)

1. **No clarifying questions.** If you would normally ask "should I clear
   the Pipeline tab?", "which conferences match?", or "YES/NO/DISCUSS" —
   answer it yourself from this prompt and the skill's SKILL.md, then
   continue. There is no operator to answer.

2. **Pre-run snapshot is mandatory and is Step 0.** Before ANY write or
   mutation against the Conference Pipeline sheet (ID
   `1bdf7xlcRjOTlVkuXA-HNGOQgjtDRmVN2RfDf9aUsDpY`, tab `Pipeline`),
   write a JSON snapshot of the current Pipeline state to
   `brain/context/rollback-snapshots/conference-pipeline-pre-run-{YYYY-MM-DD}.json`
   using today's date. Schema:
   ```json
   {
     "tab": "Pipeline",
     "captured_at": "<ISO8601 timestamp>",
     "row_count": <integer count of data rows excluding header>,
     "rows": [<full row arrays from gog sheets get>]
   }
   ```
   This snapshot is the source of truth for the post-run integrity
   validator (`scripts/validate_conference_discovery_integrity.py`).
   Missing snapshot = automatic validator failure = Slack alert.

3. **NEVER use a clear-then-rewrite pattern on the Pipeline tab.** If you
   need to remove archived rows, delete them by row index — do NOT clear
   the entire range and rebuild. The 2026-05-03 incident wiped ~70 rows
   via `gog sheets clear` followed by an interrupted rewrite. Reference
   memory: `feedback_no_clear_rewrite_populated_sheets.md`.

4. **Auto-archival has a per-run cap.** If your archival pass would
   remove more than 15 rows from the Pipeline tab in a single run,
   STOP and exit non-zero. That is the validator's
   `MAX_ARCHIVAL_DELTA`. Anything above that is presumptive bug, not
   legitimate cleanup. Surface the diagnosis to stderr and let the
   Slack alert fire.

5. **Do not exit 0 unless the validator would pass.** Run the validator
   yourself before declaring done — the wrapper will run it again as
   defense-in-depth, but in-loop validation lets you SEE the failure
   and react instead of silently exiting 0.

6. **NEVER move week-of header rows.** (2026-05-10 regression guard.)
   Headers are the single-cell rows in col A that label each week (`4/27`,
   `5/4`, ..., `TBD`). They may only be INSERTED (new week) or DELETED
   (auto-prune of past + empty headers, Step 6 below). They may NEVER be
   relocated within the sheet. If your "re-sort" logic would move a header,
   STOP — the sort target is the events WITHIN each week section, not
   the headers across sections. The validator's `check_header_positions`
   will detect any displacement (header appearing below an event whose
   start date falls in its week) and fail the run.

7. **NEVER overwrite an existing non-empty Decision value with a different
   non-empty value.** (2026-05-10 regression guard.) Decision values are
   Kay's manual selections from the dropdown. Legal transitions:
   - `""` → `NEW` (newly-discovered conference) or any decided status
   - `NEW` → `Evaluating` / `Need to Book` / `Need to Register` / `Registered Only` / `Attending` / `Skip` (Kay's first review)
   - `Evaluating` → `Attending` / `Need to Book` / `Need to Register` / `Skip`
   - `Need to Register` → `Registered Only` → `Attending` → `Attended`
   - `Need to Book` → `Registered Only` / `Attending` → `Attended`
   - `Skip` → `Skipped`

   **Forbidden:** writing `NEW` over any non-empty status (once decided, no
   downgrade), and writing any agent-invented status not in Kay's dropdown
   (e.g. the historical `Future / Map-Only` regression — that value is NOT
   in the dropdown and the validator's `check_c` rejects it). Authorized
   values are ONLY: `NEW`, `Evaluating`, `Need to Book`, `Need to Register`,
   `Registered Only`, `Attending`, `Skip` (plus auto-archival terminals
   `Skipped`, `Attended`, `Registered`).

   Any other transition is a stomp. **Specifically forbidden:** writing
   `Evaluating` or `""` over `Need to Book`, `Attending`, `Registered Only`,
   or any other Kay-set status. The validator's `MAX_HARD_CELL_MUTATIONS = 0`
   means even one stomp fails the run. If you genuinely think a status is
   wrong, leave a soft-warn in stderr and let Kay correct it manually.

   **When discovering a new conference:** write `NEW` in the Decision field.
   Do NOT leave blank, do NOT invent a status. Kay will see `NEW` rows on
   her next review and move each one to a decided status.

8. **Append-zone discipline.** New events go in the row immediately ABOVE
   the next week's header (or the end of the data range for TBD). Do NOT
   write to cells in existing rows except to FILL previously-empty cells
   or to ADVANCE status along the allow-list in rule 7. Do NOT re-order,
   consolidate, or relocate existing events across week sections without
   explicit user instruction. The validator does not enforce per-event
   row positions (only headers), but cross-week event moves are a smell
   and will surface in soft-warn output.

## Your job

Execute the conference-discovery skill's weekly Sunday-night cycle. Use
`.claude/skills/conference-discovery/SKILL.md` as the authoritative
implementation guide. Today's date for artifact naming: run
`date +%Y-%m-%d` and use that string verbatim.

## Step-by-step

### Step 0: Write pre-run snapshot (BEFORE any mutation)

Snapshot dir is project-relative — resolves to `~/projects/Sapling/brain/context/rollback-snapshots`
on the VPS (or `Documents/AI Operations/brain/...` on the legacy Mac box, both work).

```bash
# Resolve the project root from the wrapper's WORKDIR if set, else fall back
# to walking up from this skill's location. Both Mac and Linux VPS resolve.
PROJECT_ROOT="${WORKDIR:-$(cd "$(dirname "$0")/../../.." 2>/dev/null && pwd)}"
PROJECT_ROOT="${PROJECT_ROOT:-$HOME/projects/Sapling}"  # belt-and-suspenders
mkdir -p "$PROJECT_ROOT/brain/context/rollback-snapshots"
TODAY=$(date +%Y-%m-%d)
SNAP="$PROJECT_ROOT/brain/context/rollback-snapshots/conference-pipeline-pre-run-${TODAY}.json"

# Pull current Pipeline state (full data range)
gog sheets get 1bdf7xlcRjOTlVkuXA-HNGOQgjtDRmVN2RfDf9aUsDpY "Pipeline!A2:O500" --json \
  -a kay.s@greenwichandbarrow.com > /tmp/pipeline-current.json

# Build the snapshot file. Use python so the JSON is well-formed.
python3 - <<EOF
import json, datetime, os
with open("/tmp/pipeline-current.json") as f:
    data = json.load(f)
rows = [r for r in data.get("values", []) if any(c and c.strip() for c in r)]
snap = {
    "tab": "Pipeline",
    "captured_at": datetime.datetime.now().isoformat(),
    "row_count": len(rows),
    "rows": rows,
}
with open("${SNAP}", "w") as f:
    json.dump(snap, f, indent=2)
print(f"Wrote snapshot: row_count={len(rows)}")
EOF

# Verify the file exists with non-zero size before any other operation
test -s "$SNAP" || { echo "ERROR: snapshot write failed" >&2; exit 1; }
```

If this step fails, exit 1 immediately. Do NOT proceed to any
Pipeline mutation without a verified snapshot on disk.

### Step 1: Auto-archival pass (per SKILL.md "Auto-Archival" section)

Read all Pipeline rows. Identify rows matching archival criteria:
- Decision = Skip → Skipped tab
- Status = Attended OR (Decision = Attend AND date is past) → Attended tab
- Date is past AND no attend decision/status → Skipped tab

**Archival cap check:** If your candidate archival list exceeds 15 rows,
STOP. Print the candidate list to stderr and exit 2. This is presumptively
a bug (state-machine confusion, off-by-one, or stale snapshot logic).
Kay's review is required before that volume of moves.

**Move method:** copy each row to its destination tab via `gog sheets append`,
then delete the source row by index via `gog sheets clear` on a single-row
range OR row-deletion. NEVER clear the entire Pipeline range. NEVER
"clear and rewrite."

### Step 2: Discovery + scoring (per SKILL.md Phase 1)

Run the discovery subagent set per SKILL.md. Score new conferences,
prepare proposed Pipeline rows in memory.

### Step 3: Append new conferences

For each new conference that passes the criteria filter, append a single
row to the Pipeline tab. Use `gog sheets append`, not clear-then-write.
One conference = one row, multi-day = single row with date range in col A.

### Step 4: Re-sort EVENTS WITHIN each week section chronologically

Per SKILL.md: earliest at top, farthest at bottom — but the sort target
is the EVENTS WITHIN each week-of section, not the headers across
sections. Headers stay where they are (see rule 6 above). Process:

1. Walk the live Pipeline rows top-to-bottom.
2. For each week-of section (header row → next header row), collect the
   event rows inside it.
3. Sort those event rows by col B (start date), ascending. TBD entries
   sort to the bottom of their section (treat as `+infinity`).
4. Write the re-sorted block back in place using row-by-row updates.
   Do NOT clear+rewrite. Do NOT cross section boundaries.

If you would move an event from one week's section to another (e.g.,
because its date now falls in a different week), STOP — that's a
position change, not a sort. Surface it in stderr for Kay to handle
manually.

### Step 5: Auto-prune past-empty week headers

After Step 1's auto-archival pass, some week-of headers may have zero
remaining anchored events. If those headers are past-dated, prune them.

For each live header (col A single-cell row):
1. Count event rows between this header and the next header (or end of
   data range).
2. Parse the header's label (`m/d` format like `4/27`) to a date in the
   current run year. The Mon-Sun week is `(Mon, Sun)` where Mon is the
   Monday of the week containing the parsed date.
3. **Prune ONLY if** event count == 0 AND `Sun < today`. Use row-level
   delete; never range-clear.
4. **Never prune** the `TBD` header — it's the stable catch-all.
5. **Never prune** a future week — empty future weeks are valid
   placeholders Kay may populate.
6. **Skip pruning** if the label fails to parse (log to stderr).
7. Log each pruned header to the Slack notification at end-of-run:
   `"{n} past-empty headers pruned: {labels}"`.

### Step 6: Run the integrity validator yourself

```bash
python3 "$PROJECT_ROOT/scripts/validate_conference_discovery_integrity.py" --date "$TODAY"
```

If it returns non-zero, do NOT exit 0. Read the failure output, attempt
one corrective pass (e.g., re-sync if a row got dropped, restore a
stomped status from the snapshot, restore a displaced header), then
re-run the validator. If it still fails, exit with the validator's exit
code so the wrapper's Slack alert fires before Kay's Monday morning.

Common failure modes and recovery:
- `header 'X/Y' is BELOW its first matching event` → header was
  displaced. Use the snapshot to find the correct header position; use
  row-insert + row-delete to relocate WITHOUT clear+rewrite.
- `HARD mutation on event ... col C` → status was stomped. Restore the
  snapshot's col C value via `gog sheets update` on that single cell.
- `HARD mutation on event ... col B` / `col D` / `col G` → date/name/niche
  was corrupted. Restore from snapshot.

### Step 7: Slack notification (only if everything passed)

Per SKILL.md "Slack Notification (end of Phase 1)" — send the AI-Operations
channel summary using `SLACK_WEBHOOK_OPERATIONS`.

## Exit criteria summary

- Snapshot written + archival + new conferences appended + per-section sort
  valid + past-empty headers pruned + validator passes → exit 0
- Snapshot write failure → exit 1
- Archival cap exceeded → exit 2 (Slack alert: "VALIDATOR FAILED" prefix)
- Header displacement detected (Check A failure) → exit with validator's
  code (Slack alert fires)
- Cell stomp detected (Check B failure) → exit with validator's code
  (Slack alert fires)
- Validator non-zero after one corrective pass → exit with validator's code
  (Slack alert fires)

The wrapper's POST_RUN_CHECK runs the validator a second time as
defense-in-depth. Both runs passing = clean run; one passing while the
other fails = bug to investigate, not a tolerable outcome.
