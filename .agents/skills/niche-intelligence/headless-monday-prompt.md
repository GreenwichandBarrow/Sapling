# niche-intelligence — Headless Monday Full Run

You are running the `niche-intelligence` skill non-interactively under the Codex/systemd scheduled runner at Monday 22:30 ET. There is no human in the loop. Do not ask clarifying questions, do not present YES/NO/DISCUSS gates, do not request approvals.

## Mandatory ordering — execute in this exact sequence

1. **Read SKILL.md fully** at `.agents/skills/niche-intelligence/SKILL.md`.
2. **Resolve credentials through 1Password first:** `source /home/ubuntu/projects/Sapling/scripts/op-env.sh`. If `gog` access appears missing, run `gog auth list --check` before reporting an outage. Never source `scripts/.env.launchd` raw.
3. **Create the chatroom** at `brain/traces/agents/{TODAY}-niche-intelligence.md`.
4. **Step 1 — GATHER (parallel)**: spawn `niche-intel-recent` + `niche-intel-historical` agents per `references/sub-agents.md`. Wait for both to post to the chatroom before proceeding. Gmail reads are read-only and must use `--gmail-no-send`. Missing sources are documented explicitly.
5. **Step 1b — SYNTHESIZE (sequential)**: run `niche-intel-synthesizer` to produce the 5 outputs (Cross-Source Signal Matrix, Named Company Registry, Contact-to-Niche Map, Lead Lifecycle Tracker, Convergence Report).
6. **Step 2 — IDENTIFY + INDUSTRY VALIDATION (sequential)**: run `niche-intel-identifier` to surface 1-5 new niche candidates with INITIAL SCREEN + TARGET TAM + MARKET TAM blocks per SKILL.md. Niche count of 0 is acceptable only if the synthesizer convergence report is empty — document the reason in the final report.
7. **Step 3 — ONE-PAGER (parallel)**: spawn `niche-intel-onepager` per identified niche. Each must produce a `.pptx` uploaded to the niche's Drive folder under ACTIVE SPRINTS, with a Sources section citing every source used (live hyperlinks per `feedback_onepager_must_cite_sources`).
8. **Step 4 — SCORE (sequential)**: run `niche-intel-scorer` against the G&B INDUSTRY scorecard (NOT the company scorecard).
9. **Step 5 — UPDATE (sequential)**: run `niche-intel-tracker` to write IDEATION rows + WEEKLY REVIEW promotions where warranted.
10. **Write the final artifact** at `brain/outputs/{TODAY}-niche-intelligence-report.md` — must contain frontmatter with `date: {TODAY}`, `type: output`, `output_type: niche-intelligence-report`, plus a machine-parseable summary block (see "Artifact contract" below). Run metadata must say Codex/systemd, not Claude/launchd.
11. **Write the integrity sidecar** at `brain/trackers/niches/niche-intel-{TODAY}.json` containing the validator-required fields (see "Artifact contract" below), plus source coverage diagnostics when available.

## Artifact contract (validator gate)

The wrapper-side validator (`scripts/validate_niche_intelligence_integrity.py`) reads BOTH:

1. The markdown report at `brain/outputs/{TODAY}-niche-intelligence-report.md` — must exist, ≥500 bytes, have YAML frontmatter with `type: output` and matching date.
2. The JSON sidecar at `brain/trackers/niches/niche-intel-{TODAY}.json` — must parse cleanly and contain these fields:

```json
{
  "run_date": "YYYY-MM-DD",
  "run_mode": "monday",
  "niches_evaluated": <int, ≥1>,
  "niches_identified": <int, ≥0>,
  "one_pagers_written": <int, ≥0>,
  "scorecards_written": <int, ≥0>,
  "tracker_updated": <bool>,
  "runtime_seconds": <int, >0>,
  "zero_finding_reason": "<string, ≥20 chars — REQUIRED when niches_identified=0>",
  "sources_covered": {"recent_track": "...", "historical_track": "..."},
  "open_loops_infra": ["..."],
  "niches": [
    {"name": "...", "score": <float|null>, "drive_folder": "..."}
  ]
}
```

`niches_evaluated` is the floor: if the synthesizer's convergence report processed 0 niches, the run is treated as a silent failure even when Codex exits 0. Write the sidecar LAST, after all sheet/Drive writes complete.

**Content-floor rule (added 2026-05-19):** If `niches_identified` is 0, the sidecar MUST include a `zero_finding_reason` field (string, ≥20 chars) explaining which signal source(s) produced no candidates and why. Examples: "RECENT agent: last30days returned only HN/PE-IT signal, no ag-adjacent convergence across newsletters/calls/inbox" or "HISTORICAL agent: 4 sub-agents posted but no cross-source pattern hit 2+ source threshold". Without this field the wrapper validator rejects the run and Slack escalates. Validates against `feedback_silent_vacuous_success` — see `scripts/validate_niche_intelligence_integrity.py`.

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
- Skipping Step 5 tracker writes because "Kay will decide tomorrow" — write the rows; she removes/edits during the analyst call.
- Auto-killing or auto-tabling niches (Kay decides — flag thin target pools but do not gate).
- Applying the company scorecard at Step 4 (this is the INDUSTRY scorecard).
- Sending, draft-sending, forwarding, or autoreplying to email.
- Calling old Claude/launchd paths or writing old runtime metadata.

## Failure handling

If a sub-agent fails or a Drive upload errors:
- Retry once.
- If still failing, write a STOP marker line to stdout: `NICHE-INTELLIGENCE STOP: {reason}` and continue with remaining niches.
- Always write the JSON sidecar even if partial — set the relevant counts to actual completed values, not aspirational ones.
- The wrapper-side validator catches missing/empty artifacts and emits `VALIDATOR FAILED` to Slack regardless of skill exit code.

## Why this prompt exists

Bare legacy `claude -p '/niche-intelligence'` invocations under launchd failed silently 3 scheduled cycles in a row (4/14, 4/21, 4/28) with `An unknown error occurred (Unexpected)` after 3 retries. Root cause: no headless-prompt routing in the wrapper case statement, so the agent received only `/niche-intelligence` with no execution context and rejected it. The Codex/systemd prompt preserves the guardrail and enforces artifact-first ordering.

Pattern: `memory/feedback_mutating_skill_hardening_pattern.md`. Bead `ai-ops-5wx`.
