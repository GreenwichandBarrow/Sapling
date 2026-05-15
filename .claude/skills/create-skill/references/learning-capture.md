# Learning Capture

Every generated skill must include this block in its main `SKILL.md`:

```xml
<learning_capture>
A learning is an actionable discovery from executing this skill that should change future runs. Save one dated, atomic entry to `learnings.md` when execution hits friction: repeated failed searches, changed data/tool structure, unexpected behavior, resolved errors, or a user correction/preference signal. Include the trigger, what failed or changed, the successful resolution, and the future rule. Do not save project facts, transient task details, or outputs that belong in deliverables.
</learning_capture>
```

Every generated skill must also include a root `learnings.md`:

```markdown
# Learnings

Append entries in this parseable shape:

- date: YYYY-MM-DD
  trigger: What happened during execution
  issue: What failed, changed, surprised the agent, or upset the user
  resolution: What worked
  future_rule: What to do differently next time
```

Use learning capture for execution knowledge: hard-won search patterns, changed data/tool structures, unexpected behavior, resolved tool errors, or user corrections about how the skill should operate.

Do not use learning capture for task memory: client facts, project facts, temporary scope decisions, or deliverable content.
