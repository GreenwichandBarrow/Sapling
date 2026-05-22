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

(All 2026-05-03 entries pruned 2026-05-21 — graduated to global memory + CLAUDE.md, observed 18+ clean runs without violation per lifecycle rule. Originals preserved in git history. Re-add only if violated in next 30 days.)

## Watching for

(Anti-patterns suspected but not yet documented as anti-patterns. Promote to "Active learnings" once observed twice.)

- (none yet)

---

## Append protocol

When a run produces a new learning:
1. Add an entry under "Active learnings" with `[YYYY-MM-DD]` prefix.
2. Cite the source (decision trace, incident, Kay correction).
3. If the learning is general enough to apply to 3+ skills, ALSO graduate to `memory/feedback_*.md` and note "graduated to global memory" inline here.
4. If the learning is too uncertain (one observation), file under "Watching for" instead.

Do NOT append entries that just rephrase existing rules — only NEW anti-patterns.
