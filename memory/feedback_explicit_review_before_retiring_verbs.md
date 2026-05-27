---
name: feedback-explicit-review-before-retiring-verbs
description: "No verb / skill / feature / system component may be retired, deprecated, or removed without Kay's explicit review and approval. Codified 2026-05-26."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 37de3c90-d2d0-44f1-9b4b-ddb0727158c9
---

Any item to retire (verb / skill / feature / scheduled job / config / file) without a checkmark confirming completion of its replacement must be reviewed with Kay before retiring. Do NOT auto-deprecate or soft-remove, even when a clear replacement exists and the verb is no longer functionally necessary.

**Why:** Kay 2026-05-26 during the task-tracker-manager refactor plan: *"Any item to retire without a checkmark to confirm completion must be reviewed with me before retiring."* The risk is silent breakage: an "obviously redundant" verb might be called by a stale wrapper, by Kay's muscle memory, by a scheduled job we haven't fully audited, or by a future-self workflow that's not in the current codebase. Even well-intentioned auto-retirement creates surface area for surprise. Kay reviews and approves retirements explicitly — same gate as new mutations.

**How to apply:**

1. **Default behavior on architectural refactors:** when a refactor renders a verb / skill / feature functionally redundant, leave it CALLABLE in place. Add a docstring note ("functionally redundant under {new architecture} — pending Kay retirement review"). Do NOT change behavior to no-op + stderr deprecation notice without explicit approval.

2. **When proposing retirement:** surface to Kay with USAGE DATA where available (e.g., "distribute-week has been called 0 times since 5/31 rollover; functionally redundant; OK to retire?"). She decides per-item. Default answer: keep callable until the next migration cycle.

3. **Prior precedents this rule supersedes:** the `archive-todo` retirement pattern (no-op + stderr after replacement) was the OLD doctrine. Going forward, even matching that pattern requires Kay's explicit review before the no-op + stderr edit ships.

4. **Hard removal:** never. Removal of a verb's code path always requires explicit Kay sign-off, separate from soft-deprecation sign-off.

5. **Exception — broken / dangerous code:** if a verb is actively causing harm (data loss, security issue, validator failures every run), surface as a fix-or-retire decision to Kay same-session. Don't wait, but also don't auto-retire — present the choice.

6. **In refactor plans:** explicitly list "items pending Kay retirement review" as a separate section. The plan itself does NOT auto-retire anything in scope.

**Edge case — helper functions (private, leading underscore):** these are internal implementation detail, not user-facing verbs. Replacing or removing a `_helper_function` during a refactor is OK without separate review — it's part of the refactor itself, not a retirement. The doctrine applies to USER-VISIBLE surfaces (CLI verbs, slash commands, skills, config flags).

See also: [[feedback-build-new-before-sunset-old]] (related — build the replacement BEFORE retiring the original; both rules combine to "build new, ship live, then explicitly review-and-retire the old").
