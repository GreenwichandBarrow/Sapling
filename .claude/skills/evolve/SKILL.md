---
name: evolve
description: Evolve one or more Claude Code skills from their learnings without damaging routing or execution behavior. Use when the user says to run Evolve on a skill, improve skills based on learnings, update SKILL.md files, promote learnings into workflows or references, clear learnings after incorporating them, or batch-evolve several named skills.
context_budget:
  skill_md: 240
  learnings_md: 40
---

<objective>
Turn each target skill's accumulated `learnings.md` entries into durable improvements while preserving the skill as a functional agent artifact. Evolve may update `SKILL.md`, workflows, references, templates, scripts, or validation docs, then reset each target's `learnings.md` only after useful knowledge has been promoted or explicitly dismissed.
</objective>

<skill_model>
Treat the target skill as a working system:

1. Frontmatter routes the skill. `name`, `description`, and `context_budget` are functional, not decorative.
2. `SKILL.md` is the stable core: objective, principles, routing, process, validation, and learning capture.
3. `workflows/` holds step-by-step procedures for distinct paths.
4. `references/` holds durable knowledge that is too detailed for `SKILL.md`.
5. `templates/`, `scripts/`, and other assets may need updates when learnings reveal output or tooling drift.
6. `learnings.md` is a temporary inbox for execution knowledge, not a permanent knowledge base.
</skill_model>

<target_resolution>
If the user provides paths, use them. If the user provides skill names, look in likely skill roots:

1. Current repo skill/plugin directories
2. `.claude/skills/<skill-name>`
3. `~/.claude/skills/<skill-name>`
4. `~/plugins/*/claude-skills/<skill-name>`
5. `~/plugins/*/skills/<skill-name>`

Build `target_queue` from every requested skill. Stop and ask for clarification only for ambiguous or missing targets; keep already-resolved targets queued. If the user asks to evolve a folder of skills, enumerate only direct child directories that contain `SKILL.md`.
</target_resolution>

<context_boundaries>
For each queued target, set `target_skill_dir` to the directory containing that target's `SKILL.md`. Only inspect files inside the active `target_skill_dir`: `SKILL.md`, root `learnings.md`, and direct subdirectories such as `workflows/`, `references/`, `templates/`, `scripts/`, or `agents/`.

Do not scan sibling skills, project-wide `skills/` folders, example outputs, or skills that Create Skill generated. If the target skill creates other skills, those generated skills are outputs, not context for evolving the target. Inspect an output skill only when the user explicitly names that output skill as the target.

`target_queue` and `target_skill_dir` are transient labels for the current run only. Do not write queue files, target files, evolution logs, archives, registries, status files, or other tracking artifacts unless the user explicitly asks. Persist only the intended edits to target skill files and the reset of that target's `learnings.md`.
</context_boundaries>

<process>
1. Resolve all requested skill names or paths into `target_queue`.
2. Process `target_queue` sequentially, one skill at a time. Do not merge learnings across skills.
3. For the active target, read `SKILL.md` and root `learnings.md`.
4. If the active target's `learnings.md` has no dated entries, record "no learnings" for that target and leave the file unchanged.
5. Inspect the active target skill shape before editing: frontmatter, objective, routing/trigger logic, process steps, success criteria, learning capture, and relevant files inside `target_skill_dir`.
6. Classify each learning:
   - Promote: durable routing text, instruction, validation step, process change, workflow update, reference note, template adjustment, script/tooling note, or gotcha
   - Discard: task fact, project fact, output content, duplicate, or stale entry
   - Needs user judgment: ambiguous preference or behavior-changing rule with meaningful tradeoffs
7. Decide the smallest functional change that prevents the issue from recurring for that target.
8. Apply low-risk changes directly when the user asked to evolve the skill. Stop the batch for user judgment when a learning implies a major behavior change, contradicts existing design, or would make the skill more complex without clear payoff.
9. Validate that the active target still has clear trigger text, a coherent process, valid context budget, learning capture, and success criteria.
10. Clear the active target's `learnings.md` back to the standard template only after its promoted or discarded entries are accounted for.
11. Continue to the next queued target.
12. Report changed files grouped by skill, what changed functionally, skipped targets, and any entries that were not incorporated.
</process>

<change_targets>
Choose the target file by the kind of learning:

1. Update frontmatter `description` when trigger matching or intended use was wrong.
2. Update frontmatter `context_budget` when the skill now requires more or less loaded context.
3. Update `SKILL.md` objective, principles, routing, process, or success criteria when the learning affects every run or changes the skill's core behavior.
4. Update a workflow when the learning changes one path through the skill.
5. Update a reference when the learning is durable domain/tool knowledge too detailed for `SKILL.md`.
6. Update templates when generated outputs should change.
7. Update scripts or script-facing docs when file formats, command behavior, or tool I/O changed.
</change_targets>

<preservation_rules>
Evolve and Create Skill must work in tandem:

1. Preserve the skill's existing archetype unless the learnings clearly prove it should change.
2. Keep `SKILL.md` concise; promote detail outward to workflows or references when the stable core would become noisy.
3. Do not bury trigger rules outside frontmatter when they affect skill activation.
4. Do not convert crisp process steps into vague advice.
5. Do not remove learning capture from a learning-enabled skill.
6. Do not add broad abstractions from one isolated learning.
7. Prefer targeted patches over rewrites. Rewrite only when the current structure is already incoherent.
</preservation_rules>

<functional_validation>
Before clearing learnings, verify:

1. Frontmatter remains parseable and includes `name`, `description`, and `context_budget`.
2. `description` still says when to use the skill in concrete trigger language.
3. The body still tells an agent what to do, in what order, and how to know it is done.
4. Any moved knowledge is reachable from `SKILL.md` through explicit required reading, routing, or process instructions.
5. The evolved behavior addresses each promoted learning.
6. No non-target skills or generated skill outputs were loaded as context.
7. No temporary queue, target, log, archive, registry, or status files were created.
</functional_validation>

<reset_template>
After evolution is complete, reset the target `learnings.md` to:

```markdown
# Learnings

Append entries in this parseable shape:

- date: YYYY-MM-DD
  trigger: What happened during execution
  issue: What failed, changed, surprised the agent, or upset the user
  resolution: What worked
  future_rule: What to do differently next time
```
</reset_template>

<success_criteria>
- [ ] Target skill was unambiguous
- [ ] All requested targets were resolved into `target_queue` or reported as ambiguous/missing
- [ ] Each target was processed sequentially
- [ ] Context stayed inside the active `target_skill_dir`
- [ ] Each target's `SKILL.md` and `learnings.md` were read
- [ ] Related workflows, references, templates, or scripts were inspected when relevant
- [ ] Each learning was promoted, discarded, or flagged for user judgment
- [ ] Durable improvements were applied to the correct skill surface
- [ ] `SKILL.md` still routes and executes clearly
- [ ] Each `learnings.md` was reset only after that target's entries were handled
- [ ] Final response lists changed files and unincorporated entries grouped by skill
- [ ] No temporary tracking artifacts were left behind
</success_criteria>

<learning_capture>
A learning is an actionable discovery from executing this skill that should change future runs. Save one dated, atomic entry to this skill's `learnings.md` when execution hits friction: repeated failed searches, changed data/tool structure, unexpected behavior, resolved errors, or a user correction/preference signal. Include the trigger, what failed or changed, the successful resolution, and the future rule. Do not save project facts, transient task details, or outputs that belong in deliverables.
</learning_capture>
