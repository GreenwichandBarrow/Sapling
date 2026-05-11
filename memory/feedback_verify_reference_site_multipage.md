---
name: Verify reference-site structure by fetching nav links directly
description: WebFetch on a home page can mislabel a multipage site as single-page. Always fetch nav-item URLs directly before locking structural claims about a reference site.
type: feedback
originSessionId: 05f676c6-e88a-4857-a9aa-5a7c7a202d34
---
When Kay shares a reference site (Shoreham, a competitor, a brand reference), the first WebFetch on the home page describes what's on that one URL. It does NOT reliably describe whether the nav items are anchor-link sections of one long scroll OR distinct pages. Modern marketing sites blur the line because long-scroll homes mimic multi-page experience.

**Why:** On 2026-05-04 I called WebFetch on shorehampartners.com home and got back: *"Single-page website with a modular scrolling design... Navigation menu includes About, What We Value, Insights, Contact pages (suggesting multi-page capability)."* I treated this as authoritative and locked single-page modular scroll into the framing brief. Kay caught it the next day: *"the reference website is not one page, it has 3 (actually 4)."* Refetching `/about` confirmed Shoreham is multipage. Required restructuring all 5 mockup HTML files.

**How to apply:** Before locking any structural claim about a reference site:
1. Fetch home page (gets hero copy, aesthetic, top-level voice).
2. Fetch each nav-item URL directly (`/about`, `/services`, etc.). Quick parallel WebFetch calls.
3. Compare. If each nav URL returns distinct content with its own hero/sections, it's multipage. If they 404 or redirect to home with `#anchor`, it's anchor-link single-page.
4. Only THEN write the structural decision into the brief / plan.

The cost is 3-5 extra WebFetch calls (~30 seconds). The cost of locking the wrong structure into a multi-day plan is hours of rebuild.

Same discipline applies to:
- SaaS marketing sites being researched as competitors
- GitHub repos with multiple READMEs / wikis
- Documentation sites with sidebar nav
- Notion pages with toggles
- Any external system where one URL might summarize "the whole thing" but the actual structure is multipage / multi-tab / multi-section

**One fetch describes one URL, not the site.**

Source trace: `brain/traces/2026-05-04-verify-reference-site-structure-multipage.md`.
