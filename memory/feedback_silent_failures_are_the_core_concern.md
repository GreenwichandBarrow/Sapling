---
name: Silent failures are Kay's core operational concern
description: Across dashboards, skills, tools, and workflows, Kay's load-bearing worry is things that fail WITHOUT SCREAMING — launchd skills not firing, OAuth tokens expiring, MCP servers dropping, API credits exhausting, webhooks breaking. When scoping any surface, ask first "what fails silently here?"
type: feedback
originSessionId: ebd58436-6958-4e18-98eb-a6797b0d0b46
---
Across every operational surface Kay touches, her number-one concern is **silent failure** — not suboptimal outcomes, not missing features, but things that stop working WITHOUT a visible alarm. She has been burned by these repeatedly.

**Examples of silent failures she's hit:**
- launchd plists that didn't fire (Mac shut down vs. sleeping, dependency broken, plist malformed)
- OAuth tokens expiring mid-week
- MCP servers disconnecting without an error message
- API keys revoked or credit balances depleted
- Slack webhook URLs rotated without notification
- Skills producing empty output that looked like "nothing happened" when it was actually broken

**Why:** 4/24 dashboard scoping — Kay said twice in one session that she doesn't want silent failures and they've been happening. She explicitly validated the meta-pattern after I surfaced it from two separate under-scoping corrections (C-Suite & Skills page, Tech Stack page).

**How to apply:**
- **When scoping any new surface, skill, or workflow, ask first: "what CAN fail silently here?" That's the load-bearing job.** Build the canary before the feature.
- When building monitoring, default to fire/no-fire / connected/disconnected signals — vanity metrics (override rates, invocation counts, trend charts) are secondary.
- When proposing a dashboard page, a skill, or a workflow step, if it doesn't answer "is something wrong?" at a glance, reconsider whether it earns its slot.
- Dashboard's three canary pages codify this: C-Suite & Skills (did scheduled work fire), Tech Stack (are dependencies alive), Infrastructure (is internal data healthy). Three distinct silent-failure domains.
- Extends to `feedback_staleness_check_schedule_first.md` and `feedback_close_out_executes_mutation.md` — both are flavors of "catch silent gaps."
