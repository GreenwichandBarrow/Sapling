---
schema_version: 1.2.0
date: 2026-05-04
type: diagnosis
status: review
skill_origin: deal-aggregator
kay_approved: null
kay_approval_date: null
people: ["[[entities/kay-schneider]]"]
companies: []
projects: []
tags: ["date/2026-05-04", "output", "output/diagnosis", "status/review", "topic/deal-aggregator", "topic/reliability", "topic/launchd"]
---

# Deal-Aggregator Failure-Mode Diagnosis. Block 2 of Mon 5/4

One-pager artifact for the Mon 5/4 9:30am sit-down. Captures the two distinct failure modes observed in the last 8 scheduled fires, separates skill-level from system-level, names the open questions, and records the proposed wrapper-level mitigation that does not require waiting on the Anthropic side.

## Observed fires (last 8 scheduled mornings)

| Date | Day | Wrapper exit | Artifact written | Mode |
|---|---|---|---|---|
| 2026-04-27 | Mon | 0 (false success) | MISSING | Silent-success. Operator-question framing |
| 2026-04-28 | Tue | 0 (false success) | written 14:03 ET (afternoon top-up backfilled) | Silent-success. RECOMMEND ... YES/NO/DISCUSS framing emitted into a non-interactive wrapper |
| 2026-04-29 | Wed | 0 (real success) | 6166b @ 08:25 ET | OK |
| 2026-04-30 | Thu | 1 after 3 attempts | MISSING | Stream-idle-timeout. All 3 attempts API-killed |
| 2026-05-01 | Fri | 0 (real success) | 6333b @ 07:23 ET | OK |
| 2026-05-02 | Sat | not scheduled | n/a | n/a |
| 2026-05-03 | Sun | not scheduled | n/a | n/a |
| 2026-05-04 | Mon | 0 (real success) | 6715b @ 07:09 ET | OK. First run with new validator, PASSED |

## Two distinct failure modes

### Mode A. Silent-success (skill-level, G&B owns)

Cause. Claude treated an ambiguous headless prompt as an interactive conversation, emitted operator-question framings (RECOMMEND: Let attempt 2 run, monitor for artifact, YES / NO / DISCUSS), and exited 0 without performing the scan. The launchd wrapper saw exit 0 and did not Slack-alert. Artifact was missing or written hours later by an unrelated afternoon top-up run.

Evidence.
- 2026-04-27 0600 log opened with: Good morning. The 6:00 AM ET launchd run is in flight right now. Language addressed to a human operator, not a scan plan.
- 2026-04-28 0600 log emitted: RECOMMEND: Let attempt 2 run, monitor for artifact (~45 min), YES / NO / DISCUSS.
- Both. Artifact integrity audit shows MISSING for the canonical morning timestamp window.

Fix shipped. Sat 2026-05-03. Three changes, recorded in `session-decisions-2026-05-03.md` lines 39-43.
1. `scripts/validate_deal_aggregator_integrity.py`. POST_RUN_CHECK validator. Three modes (morning, afternoon, digest). Checks artifact at least 200 bytes, frontmatter present, section headers present.
2. `scripts/run-skill.sh`. POST_RUN_CHECK env var wired into all three deal-aggregator wrapper branches with a VALIDATOR FAILED Slack alert. Retired the dead 2026-04-30-only experimental-prompt date gate.
3. `.claude/skills/deal-aggregator/headless-morning-prompt.md`. Added a forbidden-pattern banning the "ask the operator if I should proceed" branch with citations to the 4/27 and 4/28 incidents.

Validation. Today 2026-05-04 0600 fire was the first run under the new validator. Exit 0. Artifact written 0709 ET, 6715 bytes. Validator PASSED. N=1 evidence the fix works in production.

### Mode B. Stream-idle-timeout (system-level, route to Harrison)

Cause. Anthropic API stream stalls mid-response. Wrapper retries 3 times, every attempt dies the same way, wrapper exits 1.

Evidence.
- 2026-04-30 0600 log. Three attempts, each "API Error: Stream idle timeout. Partial response received." Final wrapper exit 1, runtime 87 minutes, no artifact written.
- No client-side mitigation worked. Re-prompt, retry-on-fresh-context, and longer attempt budget all died the same way.

Why it surfaces. The launchd wrapper currently Slack-alerts only on VALIDATOR FAILED, not on generic exit not-equal-to-0. So 4/30's hard failure was silent until the artifact-freshness audit caught it that evening. A 12-hour blind spot for a same-day reliability concern.

Two paths forward, tracked separately.

A. Wrapper-level mitigation we can ship today. No Anthropic dependency. See Open Question 2 below.

B. Anthropic system question for Harrison. Frame: Anthropic stream idle timeouts on long headless runs, observed roughly 1 in 8 fires, no client-side mitigation works (3 retries all die), wrapper budget already 90 plus minutes per attempt. What is the right pattern? Shorter prompt? Streaming heartbeat? Different model surface?

## Open questions for the sit-down

1. Treat the validator and forbidden-pattern fix as N=1 sufficient. Monitor in production for 2 weeks. Revisit Mode A only if it recurs. Adding more guards before we see the fix break is premature optimization. Recommend YES.

2. Add wrapper Slack alert on exit not-equal-to-0 (not just on validator-fail). Three-line patch to `scripts/run-skill.sh`. Adds a generic exit-code branch in the deal-aggregator section that posts the message "deal-aggregator exit code N after K attempts. Investigate logs/scheduled/$LOG" to #operations. Catches Mode B (stream timeout) and any future infra failure without waiting on Harrison. Recommend YES.

3. Route Mode B to Harrison as the system-level item. Frame above. Recommend YES.

## Out of scope for this one-pager (separate threads)

- Empty fingerprint store from 2026-04-22. Separate retirement-gate question, you rejected backfill on 5/3 (`session-decisions-2026-05-03` line 44).
- Zero-match volume trend. Today: 0 matches, 7-day rolling 0/day per validator. Sourcing question (broker-channel build will rebalance), not reliability.
- Forbidden-pattern coverage beyond 4/27 and 4/28. Wait for next failure before pre-listing more patterns.

## Files referenced

- `logs/scheduled/deal-aggregator-2026-04-27-0600.log`
- `logs/scheduled/deal-aggregator-2026-04-28-0600.log`
- `logs/scheduled/deal-aggregator-2026-04-30-0600.log`
- `logs/scheduled/deal-aggregator-2026-05-04-0600.log`
- `brain/context/deal-aggregator-scan-{date}.md` (artifact freshness audit)
- `scripts/run-skill.sh`
- `scripts/validate_deal_aggregator_integrity.py`
- `.claude/skills/deal-aggregator/headless-morning-prompt.md`
- `brain/context/session-decisions-2026-05-03.md` lines 36-44
