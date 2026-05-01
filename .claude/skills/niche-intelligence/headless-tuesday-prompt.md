# niche-intelligence — Headless Tuesday Run

You are running the `niche-intelligence` skill non-interactively under launchd at Tuesday 22:30 ET. There is no human in the loop. Do not ask clarifying questions, do not present YES/NO/DISCUSS gates, do not request approvals.

## Mandatory ordering — execute in this exact sequence

1. **Read SKILL.md fully** at `.claude/skills/niche-intelligence/SKILL.md`.
2. **Create the chatroom** at `brain/traces/agents/{TODAY}-niche-intelligence.md`.
3. **Step 1 — GATHER (parallel)**: spawn `niche-intel-recent` + `niche-intel-historical` agents per `references/sub-agents.md`. Wait for both to post to the chatroom before proceeding.
4. **Step 1b — SYNTHESIZE (sequential)**: run `niche-intel-synthesizer` to produce the 5 outputs (Cross-Source Signal Matrix, Named Company Registry, Contact-to-Niche Map, Lead Lifecycle Tracker, Convergence Report).
5. **Step 2 — IDENTIFY + INDUSTRY VALIDATION (sequential)**: run `niche-intel-identifier` to surface 1-5 new niche candidates with INITIAL SCREEN + TARGET TAM + MARKET TAM blocks per SKILL.md. Niche count of 0 is acceptable only if the synthesizer convergence report is empty — document the reason in the final report.
6. **Step 3 — ONE-PAGER (parallel)**: spawn `niche-intel-onepager` per identified niche. Each must produce a `.pptx` uploaded to the niche's Drive folder under ACTIVE SPRINTS, with a Sources section citing every source used (live hyperlinks per `feedback_onepager_must_cite_sources`).
7. **Step 4 — SCORE (sequential)**: run `niche-intel-scorer` against the G&B INDUSTRY scorecard (NOT the company scorecard).
8. **Step 5 — UPDATE (sequential)**: run `niche-intel-tracker` to write IDEATION rows + WEEKLY REVIEW promotions where warranted.
9. **Write the final artifact** at `brain/outputs/{TODAY}-niche-intelligence-report.md` — must contain frontmatter with `date: {TODAY}`, `type: output`, `output_type: niche-intelligence-report`, plus a machine-parseable summary block (see "Artifact contract" below).
10. **Write the integrity sidecar** at `brain/trackers/niches/niche-intel-{TODAY}.json` containing the validator-required fields (see "Artifact contract" below).

## Artifact contract (validator gate)

The wrapper-side validator (`scripts/validate_niche_intelligence_integrity.py`) reads BOTH:

1. The markdown report at `brain/outputs/{TODAY}-niche-intelligence-report.md` — must exist, ≥500 bytes, have YAML frontmatter with `type: output` and matching date.
2. The JSON sidecar at `brain/trackers/niches/niche-intel-{TODAY}.json` — must parse cleanly and contain these fields:

```json
{
  "run_date": "YYYY-MM-DD",
  "run_mode": "tuesday",
  "niches_evaluated": <int, ≥1>,
  "niches_identified": <int, ≥0>,
  "one_pagers_written": <int, ≥0>,
  "scorecards_written": <int, ≥0>,
  "tracker_updated": <bool>,
  "runtime_seconds": <int, >0>,
  "niches": [
    {"name": "...", "score": <float|null>, "drive_folder": "..."}
  ]
}
```

`niches_evaluated` is the floor: if the synthesizer's convergence report processed 0 niches, the run is treated as a silent failure even when Claude exits 0. Write the sidecar LAST, after all sheet/Drive writes complete.

## What success looks like

- Chatroom has posts from RECENT + HISTORICAL gathering agents.
- Markdown report exists at `brain/outputs/{TODAY}-niche-intelligence-report.md`.
- JSON sidecar exists at `brain/trackers/niches/niche-intel-{TODAY}.json` with `niches_evaluated ≥ 1` and `tracker_updated: true`.
- One-pager `.pptx` files uploaded for every identified niche; counts in sidecar match the report body.
- IDEATION tab has new rows; WEEKLY REVIEW has any promoted niches.

## Forbidden in headless mode

- Asking the user anything.
- Presenting RECOMMEND / YES / NO / DISCUSS framings.
- Skipping the JSON sidecar because "the markdown report covers it" — the validator reads BOTH.
- Skipping Step 5 tracker writes because "Kay will review tomorrow" — write the rows; she removes/edits during the analyst call.
- Auto-killing or auto-tabling niches (Kay decides — flag thin target pools but do not gate).
- Applying the company scorecard at Step 4 (this is the INDUSTRY scorecard).

## Failure handling

If a sub-agent fails or a Drive upload errors:
- Retry once.
- If still failing, write a STOP marker line to stdout: `NICHE-INTELLIGENCE STOP: {reason}` and continue with remaining niches.
- Always write the JSON sidecar even if partial — set the relevant counts to actual completed values, not aspirational ones.
- The wrapper-side validator catches missing/empty artifacts and emits `VALIDATOR FAILED` to Slack regardless of skill exit code.

## Why this prompt exists

Bare `claude -p '/niche-intelligence'` invocations under launchd failed silently 3 Tuesdays in a row (4/14, 4/21, 4/28) with `An unknown error occurred (Unexpected)` after 3 retries. Root cause: no headless-prompt routing in the wrapper case statement, so Claude received only `/niche-intelligence` with no execution context and rejected it. This prompt forbids that path and enforces the artifact-first ordering.

Pattern: `memory/feedback_mutating_skill_hardening_pattern.md`. Bead `ai-ops-5wx`.
