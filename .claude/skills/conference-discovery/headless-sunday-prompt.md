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

## Your job

Execute the conference-discovery skill's weekly Sunday-night cycle. Use
`.claude/skills/conference-discovery/SKILL.md` as the authoritative
implementation guide. Today's date for artifact naming: run
`date +%Y-%m-%d` and use that string verbatim.

## Step-by-step

### Step 0: Write pre-run snapshot (BEFORE any mutation)

```bash
mkdir -p "/Users/kaycschneider/Documents/AI Operations/brain/context/rollback-snapshots"
TODAY=$(date +%Y-%m-%d)
SNAP="/Users/kaycschneider/Documents/AI Operations/brain/context/rollback-snapshots/conference-pipeline-pre-run-${TODAY}.json"

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

### Step 4: Re-sort Pipeline tab chronologically

Per SKILL.md: earliest at top, farthest at bottom. Sort in place — read
all rows, sort in memory, write back via row-by-row update (NOT clear+
rewrite). If you must use a batch update, ensure the destination range
matches the source range exactly so no row gets dropped.

### Step 5: Run the integrity validator yourself

```bash
python3 "/Users/kaycschneider/Documents/AI Operations/scripts/validate_conference_discovery_integrity.py"
```

If it returns non-zero, do NOT exit 0. Read the failure output, attempt
one corrective pass (e.g., re-sync if a row got dropped), then re-run
the validator. If it still fails, exit with the validator's exit code
so the wrapper's Slack alert fires before Kay's Monday morning.

### Step 6: Slack notification (only if everything passed)

Per SKILL.md "Slack Notification (end of Phase 1)" — send the AI-Operations
channel summary using `SLACK_WEBHOOK_OPERATIONS`.

## Exit criteria summary

- Snapshot written + new conferences appended + sort valid + validator passes
  → exit 0
- Snapshot write failure → exit 1
- Archival cap exceeded → exit 2 (Slack alert: "VALIDATOR FAILED" prefix)
- Validator non-zero after one corrective pass → exit with validator's code
  (Slack alert fires)

The wrapper's POST_RUN_CHECK runs the validator a second time as
defense-in-depth. Both runs passing = clean run; one passing while the
other fails = bug to investigate, not a tolerable outcome.
