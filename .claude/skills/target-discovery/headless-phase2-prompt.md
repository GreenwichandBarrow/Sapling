# Headless Phase 2 — Sunday-Night JJ-Call-Only Owner Enrichment

**You are running as a non-interactive scheduled job.** No human is on the
other end of this conversation. Every choice you make happens silently and
must be defensible by output, not by clarifying question.

**Hard rules for this run (violations = silent failure):**

1. **No clarifying questions.** If you would normally ask "which niche?",
   "should I proceed?", or "YES/NO/DISCUSS" — answer it yourself from this
   prompt and continue. There is no operator to answer.
2. **Do not exit 0 unless every active JJ-Call-Only niche has a pool
   artifact written and integrity-validated.** A clean exit with zero
   work is the bug we are fixing. If a step blocks, exit non-zero with
   the reason in stderr.
3. **No duplicate-prevention shortcuts.** Do NOT invent reasons that
   another Phase 2 run is in flight. Do NOT call `ps` or `pgrep` to
   "check for duplicates." launchd ensures single-instance.
4. **Pool artifact gets written FIRST.** Before any Apollo call, before
   any sheet read past the row-selection query, the pool artifact for
   today must exist on disk. If you cannot write it, exit non-zero.

## Your job

Run target-discovery Phase 2 (Sunday-night pipeline) for every niche on
WEEKLY REVIEW where Status is `Active-Outreach` AND Outreach Channel
(Col D) is `JJ-Call-Only`. Use the calls-first-flow section in
`.claude/skills/target-discovery/SKILL.md` as the authoritative
implementation guide.

**Today's date (for artifact naming):** run `date +%Y-%m-%d` and use
that string. The integrity validator looks at
`brain/context/jj-week-pool-{YYYY-MM-DD}.md`.

## Step-by-step

### Step 0: Identify active JJ-Call-Only niches

```bash
gog sheets get 1vHx4E1tRTR6V3k7NQeHdCrUjDITJVtZA5YPSIFeSins "WEEKLY REVIEW!B4:K20" -a kay.s@greenwichandbarrow.com -j
```

Parse the response. For each row where Status (Col J or equivalent) is
`Active-Outreach` AND Outreach Channel (Col D) is `JJ-Call-Only`, record
the niche name. Map niche name → target sheet ID using the
`NICHE_SHEETS` dictionary in `scripts/refresh_jj_snapshot.py` (the
canonical map).

If zero niches match, this is a recoverable nothing-to-do state.
**Still write a stub pool artifact** at
`brain/context/jj-week-pool-{YYYY-MM-DD}.md` with a single line
`# No active JJ-Call-Only niches today` so the validator's
"missing artifact = silent failure" check passes. Then exit 0.

### Step 1: Per-niche pool selection (write artifact FIRST)

For each active JJ-Call-Only niche:

1. Read the niche's "Full Target List" tab via gog.
2. Filter rows where Col T (JJ: Call Status) is empty.
3. Sort by row number ascending.
4. Take the top 200 (fewer if the list is short).
5. Append the row numbers under a `## {Niche Name}` heading in
   `brain/context/jj-week-pool-{YYYY-MM-DD}.md`. Format:
   ```
   ## Premium Pest Management
   - row: 42
   - row: 43
   - row: 44
   ```
6. After writing, immediately verify the file exists with non-zero size
   and contains the expected row count. If verification fails, exit 1.

This artifact is the source of truth for Steps 2–4 and for the
post-run integrity validator. **Do not skip.**

### Step 2: Owner enrichment

Per SKILL.md `<calls_first_flow>` Phase 2 Step 2: for each pool row with
Col K (Owner Name) blank, run Apollo `/people/match` (via
`skill/list-builder` if helpful) by company domain. Write owner name
(K), title (L), owner LinkedIn (Q), email (M) from the response.

Apollo credit budget per run: ~200 credits per niche × N niches. If
remaining monthly credits would drop below 50 mid-run, log the partial
state and exit 1 — let Kay decide.

### Step 3: PE re-screen on newly enriched rows

Per SKILL.md Phase 2 Step 3. For each newly enriched row, search
`"{company name}" "acquired by" OR "portfolio company" OR "subsidiary"`.
PE-owned → move row to "Do Not Call" tab with Col S `PE-OWNED: {ev}`.
Remove from pool artifact and backfill from next-in-queue rows.

### Step 4: Warm intro check

Per SKILL.md Phase 2 Step 4. Run `warm-intro-finder` against every row
remaining in the post-Step-3 pool. Warm intro → move to Do Not Call,
backfill pool. Surface findings inline in the run log so Monday's
briefing can pick them up.

### Step 5: Mandatory integrity check (last action before exit)

After Steps 1–4 complete for every niche, run the integrity validator
for each niche's sheet. This is the same validator the wrapper runs as
POST_RUN_CHECK — running it inside the conversation lets you SEE the
failure and react before declaring done.

```bash
JJ_CALL_NICHES="<comma-separated active niche names>" \
  python3 scripts/validate_phase2_integrity.py
```

If the validator returns non-zero, do NOT exit 0. Read the failure
output, attempt one corrective pass (e.g., re-enrich a row whose Col K
ended up blank), then re-run the validator. If it still fails, exit
with the validator's exit code and let the Sunday Slack alert fire so
Kay can intervene before JJ's Monday 10am tab is built from a broken
pool.

### Step 6: Hand off to jj-operations

Once the validator passes, jj-operations Sunday-prep (separate launchd
job at the same time slot) reads the pool artifact and creates the
Mon–Fri Call Log tabs. Your job ends when the validator passes. Do
not invoke jj-operations from inside this prompt — the launchd job
sequence handles it.

## Exit criteria summary

- Pool artifact written for each active JJ-Call-Only niche → exit 0
- Zero active JJ-Call-Only niches today → stub artifact written, exit 0
- Any blocker (Apollo budget, sheet read failure, write failure) → exit
  non-zero with the failure mode in the final log line
- Integrity validator returned non-zero after one corrective pass →
  exit with the validator's code

The wrapper's POST_RUN_CHECK will re-run the validator independently as
defense-in-depth. Two failures (your in-loop check + the wrapper check)
is fine; one of them passing while the other fails would be a bug to
investigate, not a tolerable outcome.
