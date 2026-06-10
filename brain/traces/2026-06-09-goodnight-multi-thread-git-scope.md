---
schema_version: 1.1.0
date: 2026-06-09
type: trace
tags: [date/2026-06-09, trace, topic/goodnight, topic/git, topic/codex-migration, status/pending]
had_human_override: true
importance: medium
target: skill:goodnight
---

# Decision Trace: Goodnight Needs Multi-Thread-Aware Git Scope

## Context

Kay established separate canonical Codex threads for different operating surfaces. During goodnight, she asked whether the skill needs to update so it commits all threads. The repo is canonical, but chat threads themselves are not repo objects.

## Decisions

### Commit repo artifacts, not chat threads
**AI proposed:** The current goodnight flow stages broad repo paths and commits evening artifacts.
**Chosen:** Update the goodnight concept to be multi-thread-aware: sweep canonical repo changes produced by any thread, classify them by owner/surface, commit safe completed artifacts, and flag ambiguous/unowned changes. Do not literally commit chat threads.
**Reasoning:** Separate threads can produce repo artifacts concurrently. Blindly staging everything risks committing unrelated or incomplete work; ignoring other-thread artifacts risks leaving the VPS canonical backend uncommitted. The skill needs a classification step.
**Pattern:** #multi-thread-repo-hygiene

## Learnings

- Goodnight should start with a git status classification by operating surface/thread owner.
- Safe completed artifacts can ride the evening commit; unclear changes should be surfaced instead of staged blindly.
- The skill update belongs in `evolve`/skill-maintenance, not ad-hoc editing inside goodnight.
