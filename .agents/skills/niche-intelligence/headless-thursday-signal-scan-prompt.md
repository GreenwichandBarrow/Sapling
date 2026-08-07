# niche-intelligence — Headless Thursday Thesis Signal Scan

You are running the `niche-intelligence` light signal scan non-interactively under the Codex/systemd scheduled runner at Thursday 22:30 ET. There is no human in the loop. Do not ask clarifying questions, do not present approval gates, and never send email.

## Purpose

This is a lightweight strategic scan, not the Monday full Niche Intelligence pipeline. Its job is to make sure Kay is not relying on memory to surface new thesis signals.

## Mandatory ordering

1. Read `.agents/skills/niche-intelligence/SKILL.md` fully.
2. Resolve credentials through 1Password first: `source /home/ubuntu/projects/Sapling/scripts/op-env.sh`.
3. Scan only for thesis signals that changed since the Monday full run or the last seven days, whichever is tighter:
   - PE activity/news and last-30-days market signals relevant to G&B thesis areas.
   - Gmail/deal-flow/investor/broker comments using read-only access and `--gmail-no-send`.
   - Granola/Fireflies/vault call notes when available.
   - `brain/inbox/` niche ideas and active-thesis signals.
   - Conference-discovery outputs and active conference pipeline changes.
4. For each signal, run a light picks-and-shovels expansion: identify the visible end-market, the operational complexity created by the trend, and at least one second-order beneficiary or explain why none is visible. Then classify it into exactly one bucket:
   - `urgent_fast_sprint`: time-sensitive enough to consider before Monday.
   - `queue_for_monday`: worth full Niche Intel next Monday.
   - `park`: interesting but below current G&B/Deal 1 bar.
   - `no_signal`: no meaningful new signal.
5. Apply the Deal 1 thesis gate: any `urgent_fast_sprint` or `queue_for_monday` item must include an explicit tailwind or growth trend and a plausible picks-and-shovels / edge-niche path. No tailwind means `park`; no edge path means `queue_for_monday` at most, not urgent execution.
6. Write markdown artifact at `brain/outputs/{TODAY}-thesis-signal-scan.md`.
7. Write JSON sidecar at `brain/trackers/niches/thesis-signal-scan-{TODAY}.json`.

## Markdown artifact contract

The markdown file must be >=300 bytes and include YAML frontmatter:

```yaml
---
date: {TODAY}
type: output
output_type: thesis-signal-scan
tags: [output, output/thesis-signal-scan, topic/niche-signal, date/{TODAY}]
---
```

The body must contain:

- `## Executive Decision Surface` with 0-3 Friday Good Morning-ready recommendations.
- `## Signals Reviewed` with source coverage and gaps.
- `## Edge-Niche Expansion Notes` covering visible end-market, operational complexity, and second-order beneficiaries.
- `## Queue For Monday Full Run`.
- `## Urgent Fast Sprint`.
- `## Park / No Action`.
- `## System Gaps` if any source failed.

## JSON sidecar contract

```json
{
  "run_date": "YYYY-MM-DD",
  "run_mode": "thursday_signal_scan",
  "signals_reviewed": 1,
  "recommendations_count": 0,
  "urgent_fast_sprint_count": 0,
  "queue_for_monday_count": 0,
  "park_count": 0,
  "zero_signal_reason": "Required when recommendations_count is 0",
  "sources_covered": {"pe_news": "...", "email": "...", "calls": "...", "inbox": "...", "conferences": "..."},
  "edge_niches_considered": 0,
  "recommendations": []
}
```

Write the sidecar last. If sources fail, write the artifact and sidecar anyway and document the gap.
