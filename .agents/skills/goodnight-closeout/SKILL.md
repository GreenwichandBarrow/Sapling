---
name: goodnight-closeout
description: End-of-day operating-system closeout for Kay. Use when Kay says goodnight, /goodnight, close out the day, save state, or asks to finish the operating day. Carries tasks forward, captures durable decisions and learnings, checks whether hooks or skill updates are needed, commits logical changes, and reports push/dirty-tree status.
archetype: orchestrator
context_budget:
  skill_md: 220
  max_references: 8
  learnings_md: 40
  sub_agent_limit: 500
---

# Goodnight Closeout

Own the end-of-day closeout for the Sapling operating system. This skill is the repo steward for Good Night; `task-tracker-manager` only handles task carry-forward.

## Non-negotiables

- Never send emails.
- Never commit secrets, copied credentials, raw tokens, or unreviewed `.env` changes.
- Use 1Password-backed helpers before diagnosing missing OAuth/API access.
- Preserve user work. Do not revert unrelated dirty files.
- Use logical commits. Do not make one giant "everything" commit unless Kay explicitly asks.
- Report whether changes were pushed. A closeout is incomplete if push status is unknown.

## Closeout Flow

1. **Snapshot repo state**
   - Record branch, upstream, ahead/behind, and `git status --short`.
   - Identify unpushed commits with `git cherry -v origin/$(git branch --show-current)` when upstream exists.

2. **Run daily task carry-forward**
   - Invoke `task-tracker-manager` `carry-forward-day` for `/goodnight`.
   - Use `--dry-run` first when the tracker pointer, Google auth, or sheet state looks uncertain.
   - Do not ask Kay to approve routine unfinished-task carry-forward.

3. **Capture operating state**
   - Write or update the daily session decision note under `brain/context/`.
   - Capture what changed, what is blocked, what is deferred, and what tomorrow should inherit.

4. **Decision trace sweep**
   - Use `decision-traces`.
   - Write a trace only for choices that change future behavior.
   - Do not write receipt traces for mechanical task moves, scans, or scheduled job runs.

5. **Learning and skill sweep**
   - If Kay corrected a workflow or a repeated failure revealed a durable rule, update the relevant skill or its `learnings.md`.
   - Do not add transient facts, one-off meeting details, or normal execution logs to skill learnings.
   - If a new skill is needed, create a small repo-backed skill rather than burying the rule in chat.

6. **Hook and guardrail sweep**
   - If the day exposed a reusable safety check, missing preflight, or recurring failure mode, add or update the hook/runner guardrail.
   - If the guardrail is not safe to implement immediately, record it as a deferred item with owner and reason.

7. **Classify dirty tree**
   - Group changes into:
     - operating artifacts to commit now
     - skill/docs/process updates to commit now
     - product/code changes needing review
     - generated runtime noise to leave alone
     - sensitive files never to stage
   - Use explicit pathspecs when staging. Never `git add .` during closeout.

8. **Commit logical groups**
   - Prefer small commits with clear messages:
     - `goodnight: close YYYY-MM-DD operating state`
     - `skills: codify {workflow} learning`
     - `docs: record {migration/process} decision`
   - Before committing, show the staged diff summary and verify no secret-looking files are staged.

9. **Push policy**
   - Auto-push only when:
     - upstream exists,
     - commits are closeout/process artifacts or already-reviewed work,
     - the staged set excludes secrets and unreviewed `.env` changes,
     - there are no unresolved product/code changes that would be misleading to push.
   - Hold push and report clearly when:
     - branch has unreviewed development commits,
     - dirty tree contains dashboard/product/code changes still being worked,
     - remote status is uncertain,
     - push requires approval outside the current policy.

10. **Final ledger**
    - Report:
      - commits created
      - pushed vs not pushed, with reason
      - files intentionally left dirty
      - skill/hook/trace updates made
      - next morning inheritance notes

## Success Criteria

- Task carry-forward either ran or a blocker is recorded.
- Durable decisions are in traces or daily session notes.
- Skill/hook updates from the day are applied or explicitly deferred.
- Logical commits are created for closeout-owned changes.
- Push status is explicit.
- Remaining dirty files are listed with reasons.
