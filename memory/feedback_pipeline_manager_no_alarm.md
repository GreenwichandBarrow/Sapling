---
name: Pipeline manager — no alarm language
description: Don't announce pipeline-manager hasn't run yet during /start, just run it
type: feedback
---

Don't say "pipeline-manager hasn't run" or frame its absence as a warning during /start. It runs within the session, not overnight — so of course it hasn't run yet when /start kicks off.

**Why:** Makes Kay think something is broken when it's just normal sequencing.

**How to apply:** During /start, silently note email-scan-results aren't available yet, run pipeline-manager as part of the flow, and fold results into the daily note. No commentary needed.
