---
name: When mockups exist, they ARE the spec — match them faithfully
description: Locked mockup HTML files are the source of truth for visual implementation. Don't treat them as reference; treat them as binding spec. Compare side-by-side before declaring a page done.
type: feedback
originSessionId: 53e20cb7-f6e0-4235-94aa-3e4f9050dc57
---
When `dashboard/mockup-*.html` (or any equivalent locked design artifact)
exists, it is the BINDING specification for the live implementation — not a
loose reference. Live UI must match the mockup faithfully: typography,
spacing, color coding, layout structure, active-state styling, urgency
emojis, header alignment.

**Why:** 2026-04-25 polish sweep: Kay sent ~6 screenshot pairs of
mockup-vs-live across the dashboard, each catching a visual drift (font
cascade, sidebar spacing, hero tile missing, filter pill row missing,
column-count badges missing, summary-strip color coding missing, topbar
alignment, blue active-state). Every drift was Claude having shipped
"close enough" rather than "matches mockup." Kay's reframe: *"the mockups
were amazing, we just needed them live."* The mockups had been LOCKED in
Session 4 PM as the design surface; subsequent sessions were supposed to
ship to-spec, not approximate.

**How to apply:**
- Before declaring any UI work done, open the mockup file alongside the
  live render. Visual diff each section: typography, spacing, color, state.
- If the live diverges from the mockup in any visible way, that's a bug to
  fix in this session, not a follow-up.
- When Streamlit (or any framework) defaults override our styling
  (Emotion CSS-in-JS, default fonts, etc.), use the framework's theme system
  before hand-rolling overrides — see `feedback_streamlit_theme_config_for_chrome`.
- "Visual fidelity sweep" is its own task type — schedule it after every
  page ships, not as an afterthought when Kay catches drift.
- Locked mockups can change, but the change goes through Kay first and
  produces a new mockup file. Live should never silently diverge.

**Pairs with `feedback_build_new_before_sunset_old`:** the mockup IS the
new design; the old format/styling lives until the new is verified
matching the mockup faithfully.
