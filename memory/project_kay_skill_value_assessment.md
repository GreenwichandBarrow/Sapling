---
name: project_kay_skill_value_assessment
description: "Kay's qualitative value ranking of scheduled skills — overrides log-reliability as the definition of \"best\""
metadata: 
  node_type: memory
  type: feedback
  originSessionId: cc437d80-1fd0-4dc2-b6ae-f46822a21e4a
---

When ranking which scheduled skills are "best," use Kay's **value** judgment, not log-reliability ("runs clean"). Stated 2026-05-31:

- **conference-discovery (Conference Pipeline) — HIGH value.** Kay rates this as one of the best-performing skills. Do NOT cut/degrade it in cost-trimming.
- **deal-aggregator — NOT top-value** in Kay's view, despite being 20/20 reliable. Notably it is also the **single most expensive programmatic job (~$630/mo)** while conference-discovery is cheap (~$75/mo) — spend is inversely correlated with Kay's perceived value here. deal-aggregator is therefore a candidate for scope/frequency/model downgrade.

**Why:** "reliable" ≠ "valuable." A skill that runs clean but surfaces little Kay acts on is not a top skill. Cost-cutting should protect high-value skills and target high-cost/low-value ones.

**How to apply:** When listing best skills or deciding what to trim for the June-15 cost work, weight by Kay's value assessment. Protect conference pipeline; scrutinize deal-aggregator's spend. Confirm value with Kay rather than inferring from clean logs. Related: [[feedback_decision_fatigue_minimization]].
