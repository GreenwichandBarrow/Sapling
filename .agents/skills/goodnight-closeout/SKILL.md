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

Own the end-of-day closeout for the Sapling operating system. This is the Codex-native successor to the preserved Claude `/goodnight` command. `task-tracker-manager` only handles task carry-forward; this skill owns the whole closeout contract.

## Non-negotiables

- Never send emails.
- Never commit secrets, copied credentials, raw tokens, or unreviewed `.env` changes.
- Use 1Password-backed helpers before diagnosing missing OAuth/API access.
- Preserve user work. Do not revert unrelated dirty files.
- Use logical commits. Do not make one giant "everything" commit unless Kay explicitly asks.
- Report whether changes were pushed. A closeout is incomplete if push status is unknown.
- Do not silently skip traces, memories, hook checks, skill-evolution candidates, thread inventory, or dirty-tree review. If the answer is zero, say zero and why.

## Closeout Flow

1. **Snapshot repo state**
   - Record branch, upstream, ahead/behind, and `git status --short`.
   - Identify unpushed commits with `git cherry -v origin/$(git branch --show-current)` when upstream exists.

2. **Run daily task carry-forward**
   - Invoke `task-tracker-manager` `carry-forward-day` for `/goodnight`.
   - Use `--dry-run` first when the tracker pointer, Google auth, or sheet state looks uncertain.
   - Do not ask Kay to approve routine unfinished-task carry-forward.

3. **Inventory the full day**
   - Inventory this thread plus other active/recent Codex threads/worktrees before writing the closeout.
   - Prefer Codex thread tools when available (`tool_search` for `list_threads`, `read_thread`, etc.).
   - If thread tools are unavailable, fall back to repo evidence: `git status --short`, today's continuation files, verb logs, files changed today, and scheduled job outputs.
   - For each thread or workstream, mark one outcome in the session-decision source notes:
     - Included
     - No repo delta
     - Excluded with reason
   - If another thread produced repo changes, either include them in the commit plan or state why they remain dirty.

4. **Gather closeout signals**
   - Read today's `brain/context/continuation-{date}*.md` files.
   - Scan the day for APPROVE / REJECT / PASS / SENT / CREATED / UPDATED / DELETED / DRAFTED / DEFER outcomes.
   - Read today's `brain/context/email-scan-results-{date}.md`, `brain/context/deal-aggregator-scan-{date}*.md`, and other scheduled-skill outputs when present.
   - Read the prior session-decisions file to carry unresolved open loops forward.

5. **Write session decisions**
   - Write `brain/context/session-decisions-{date}.md`.
   - Required frontmatter: `date`, `type`, `title`, `tags` with inline array tags.
   - Required sections:
     - `## Decisions`
     - `## Actions Taken`
     - `## Deferred`
     - `## Open Loops`
     - `## Sources Reviewed`
   - Convert relative dates to absolute dates.
   - Do not silently drop carried deferrals; resolve them, carry them forward, or mark them blocked.

6. **Decision trace sweep**
   - Use `decision-traces`.
   - Review each APPROVE/REJECT or non-obvious judgment call.
   - Write traces only when a future agent would act differently from the reasoning.
   - Do not write receipt traces for mechanical task moves, scans, or scheduled job runs.
   - If zero traces qualify, the final summary must say how many candidates were reviewed and why zero qualified.

7. **Memory, learning, and skill-evolution sweep**
   - Scan for durable user preferences, project facts, feedback rules, reference pointers, and repeated corrections.
   - Update existing memory files before creating new ones.
   - Update a skill or `learnings.md` only when the rule is clearly durable, low-risk, and directly tied to the affected workflow.
   - Larger existing-skill rewrites belong to Phase 2.5 / `evolve`; record them as evolve candidates instead of doing ad hoc night edits.
   - New skill candidates should be listed, not created, unless Kay already approved the skill during the day.
   - Do not add transient facts, one-off meeting details, or normal execution logs to skill learnings.

8. **Hook and guardrail sweep**
   - If the day exposed a reusable safety check, missing preflight, or recurring failure mode, add or update the hook/runner guardrail when it is confirmed and low-risk.
   - If the guardrail is not safe to implement immediately, record it as a deferred item with owner and reason.
   - Do not rely on Codex Stop/PreCompact hooks as the only closeout mechanism; hooks are a safety net, not the Good Night contract.

9. **Classify dirty tree**
   - Group changes into:
     - operating artifacts to commit now
     - skill/docs/process updates to commit now
     - product/code changes needing review
     - generated runtime noise to leave alone
     - sensitive files never to stage
   - Use explicit pathspecs when staging. Never `git add .` during closeout.

10. **Commit logical groups**
   - Prefer small commits with clear messages:
     - `goodnight: close YYYY-MM-DD operating state`
     - `skills: codify {workflow} learning`
     - `docs: record {migration/process} decision`
   - Before committing, show the staged diff summary and verify no secret-looking files are staged.

11. **Push policy**
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

12. **Final ledger**
    - Report:
      - carry-forward count or blocker
      - thread inventory counts
      - decisions logged
      - traces written or explicit zero-trace reason
      - memory delta
      - skill/hook/evolve candidates
      - commits created
      - pushed vs not pushed, with reason
      - files intentionally left dirty
      - next morning inheritance notes

## Success Criteria

- Task carry-forward either ran or a blocker is recorded.
- Multi-thread inventory ran or the fallback evidence path is documented.
- Session-decisions file exists for the day.
- Durable decisions are in traces or daily session notes.
- Trace sweep reports files written or explicit zero-trace reason.
- Memory, skill-learning, hook, and evolve candidates are applied or explicitly deferred.
- Logical commits are created for closeout-owned changes.
- Push status is explicit.
- Remaining dirty files are listed with reasons.
