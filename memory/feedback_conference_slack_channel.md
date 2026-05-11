---
name: Conference notifications go to AI-Operations, not SVA
description: Conference pipeline Slack messages go to SLACK_WEBHOOK_OPERATIONS, not SVA. Kay attends conferences, not JJ.
type: feedback
---

Conference pipeline Slack notifications go to the **AI-Operations** channel (`$SLACK_WEBHOOK_OPERATIONS`), NOT the SVA channel.

**Why:** Kay is the one who attends conferences, not JJ. SVA is JJ's channel for cold calling operations. Conference discovery, registration, and follow-ups are Kay's workflow.

**How to apply:** In conference-discovery skill, all Slack notifications use `$SLACK_WEBHOOK_OPERATIONS`. Update the skill's validation section accordingly.
