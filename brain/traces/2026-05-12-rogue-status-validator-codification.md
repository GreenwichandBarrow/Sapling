---
date: 2026-05-12
type: trace
title: "Rogue agent-invented values get codified by later validator hardening — Future/Map-Only pattern"
tags:
  - date/2026-05-12
  - trace
  - topic/conference-discovery
  - topic/validator-design
  - topic/agent-invention
  - topic/dropdown-enforcement
schema_version: 1.1.0
---

# Rogue agent-invented values get codified by later validator hardening — Future/Map-Only pattern

## Trigger

When triaging the 2026-05-10 Conference Pipeline regression, the agent investigation found the validator was hardened on 2026-05-11 (commits `cf70d64`, `c5b402a`, `c043fc0`) to forbid status stomps. The hardening codified `Future / Map-Only` as a legal status transition source.

Kay asked: "Ive never heard of future/map only. what does that mean?"

Investigation revealed: `Future / Map-Only` was NEVER in Kay's actual dropdown on the Pipeline tab's Decision field. The 6 authorized dropdown values were: Need to Book / Attending / Need to Register / Registered Only / Skip / Evaluating. The `Future / Map-Only` value was AGENT-INVENTED at some prior run, written to live cells bypassing the dropdown, then later validator hardening looked at the resulting state and codified the rogue value as legitimate.

## Decision

Three-part fix:

1. **Reconcile the live data**: remap the 2 live rows with `Future / Map-Only` (AM&AA Chicago row 42, NPMA Orlando row 57) → `NEW` (Kay added `NEW` to the dropdown as the canonical agent-discovery marker).
2. **Reconcile the validator**: strip all 3 `Future / Map-Only` transitions from `ALLOWED_STATUS_PROGRESSIONS`; add `AUTHORIZED_STATUSES` set + new `check_c` function that fails on any cell value outside Kay's dropdown.
3. **Reconcile the skill**: update SKILL.md + headless-sunday-prompt to instruct agents to write `NEW` (not blank, not invented) on discovery; `NEW` → {Evaluating, Need to Book, Need to Register, Registered Only, Attending, Skip} as Kay-review transitions.

Authorize-list pattern: validator now references Kay's actual dropdown as the source of truth for legal values, not an implicit allowlist accumulated from observed runs.

## Alternatives Considered

1. **Accept current state** — codify `Future / Map-Only` as a legitimate Kay-authored status. (Rejected — it was never Kay's; this is the silent-drift failure mode.)
2. **Reconcile data only** — remap rogue rows but leave validator allowing the rogue value. (Rejected — would let the value re-emerge.)
3. **Add `NEW` + strip rogue + add validator dropdown-conformance check** — adopted.

## Reasoning

The 2026-05-10 regression that triggered hardening was real (row movement, dropdown stomps). But the hardening looked at the post-regression state of the sheet and treated everything present as legitimate, including the agent-invented value. Validators that observe-and-codify suffer this drift: they cement whatever they find, even if what they find is wrong.

Fix: validators must reference the AUTHORITATIVE SOURCE (Kay's dropdown) for the legal set, not the OBSERVED set. The `AUTHORIZED_STATUSES` constant in the validator should be kept in sync with the dropdown manually OR (better) read from the dropdown's data-validation rule at validator-load time.

For the data: agents need a designated "newly discovered, not yet decided" value. That's `NEW`. Without it, agents either (a) leave blank (visually invisible — Kay can't tell what needs review), (b) invent values (the failure mode we just hit), or (c) prematurely assign a decided status. `NEW` solves (a) by being visually distinct and (b) by giving agents a legitimate placeholder.

## Why This Trace Matters

The pattern — agent invents value, later validator codifies — is generalizable across any skill that mutates a sheet with constrained values. Future skills must:

1. **Reference Kay's data-validation rule** (or other authoritative source) for the legal value set, not observed values.
2. **Provide a designated "needs review" marker** (`NEW`, `PENDING_REVIEW`, etc.) so agents don't invent values to fill the gap.
3. **Reject writes outside the authoritative set** as hard failures, not soft warnings.

When hardening a validator on a sheet, ALWAYS check whether the values being "protected" are actually in the user's dropdown / authoritative source. If not, treat them as rogue and reconcile (don't codify).

## Key Insight

Validators that learn from observed state propagate whatever they observe — including drift. The fix is to anchor validators to the AUTHORITATIVE source of truth (Kay's UI-defined dropdown), not the historical state. This is a small architectural change with large drift-prevention payoff.
