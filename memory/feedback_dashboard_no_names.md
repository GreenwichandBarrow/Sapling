---
name: Dashboard surfaces use roles, never names
description: User-visible dashboard labels (channel rows, table headers, zone sublabels, page notes) use roles (CEO, Operations, Operator) instead of personal names (Kay, JJ).
type: feedback
originSessionId: 765f2769-0c68-4590-b466-5773bf5b3d4e
---
User-visible dashboard labels use ROLES, never personal names. Kay → "CEO". JJ → "Operations". "Kay's stack" → "operator stack".

**Why:** Kay surfaced this 2026-04-26 during Phase A of the dashboard-as-source pivot — when she saw "Kay email" / "JJ calls" in Zone 3 channel rows. Reasoning: dashboards should describe FUNCTIONS not PEOPLE so they generalize as the team grows and don't read as a personal log. The same logic underlies `feedback_no_name_in_deliverables` for one-pagers/scorecards.

**How to apply:**
- ChannelRow labels, table column headers, zone sublabels, page-note copy: use roles (CEO, Operations, Operator, Intermediary)
- CSS hook class names (`dot_class="kay"`, `dot_class="jj"`) can stay as internal identifiers — invisible to user
- Code comments, docstrings, internal class fields (`jj_active`, `JJActivity`) stay as-is — refactoring is invasive and not user-visible
- New panel/zone copy must follow this rule from the start
- When cleaning up old surfaces, scope-creep cautiously: check what's user-visible vs internal before mass-renaming
