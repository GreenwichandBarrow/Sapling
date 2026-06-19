# pipeline-manager learnings

Skill-local feedback loop per Harrison Wells coaching session 4/30. Pilot skill for the `learnings.md` pattern. Read at start of every run, append at end if anything was learned.

**Bias toward NEGATIVE directives.** Per Harrison: "do NOT do X because Y" outperforms "do A then B." The model is sharper at avoiding flagged anti-patterns than remembering positive instructions.

**Format per entry:**
```
- [YYYY-MM-DD] Do NOT {action}. Reason: {why}. Source: {trace, decision, incident}.
```

**Scope:** pipeline-manager-specific. Cross-skill rules belong in `memory/feedback_*.md`. If a learning here applies to 3+ skills, graduate it to global memory and remove the local entry.

**Lifecycle:** entries that have been honored across 5+ runs without violation can be pruned. Never delete an entry that's been violated within the last 30 days.

---

## Active learnings

- [2026-06-18] Do NOT treat Attio as self-maintaining pipeline truth. Reason: Kay-confirmed pipeline facts plus call/email/Drive evidence are the source truth; pipeline-manager must reconcile Attio and the dashboard snapshot to that truth. Source: G&B Dashboard thread correction on Project Drone / Total Extermination / BTEC.

(All 2026-05-03 entries pruned 2026-05-21 — graduated to global memory + CLAUDE.md, observed 18+ clean runs without violation per lifecycle rule. Originals preserved in git history. Re-add only if violated in next 30 days.)

## Watching for

(Anti-patterns suspected but not yet documented as anti-patterns. Promote to "Active learnings" once observed twice.)

- [2026-05-30] `gog gmail search --json` returns THREAD-level objects (keys: id/date/from/subject/labels/messageCount) with NO `to`/recipient field. The outbound-email→list-entry coverage net (hook 11) parses recipients from `to` — that field is absent at thread granularity, so a naive parse silently yields 0 recipients and the safety net no-ops without flagging. To actually run coverage, fetch per-message detail (e.g. `gog gmail get <id>`) or a message-level query. Observed once; promote if it recurs. (This run: confirmed coverage manually via subject inspection — all 14d outbound mapped to existing relationship/intermediary/deal contacts, no new deal company missing an entry.)

---

## Append protocol

When a run produces a new learning:
1. Add an entry under "Active learnings" with `[YYYY-MM-DD]` prefix.
2. Cite the source (decision trace, incident, Kay correction).
3. If the learning is general enough to apply to 3+ skills, ALSO graduate to `memory/feedback_*.md` and note "graduated to global memory" inline here.
4. If the learning is too uncertain (one observation), file under "Watching for" instead.

Do NOT append entries that just rephrase existing rules — only NEW anti-patterns.
