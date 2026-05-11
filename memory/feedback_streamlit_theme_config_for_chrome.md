---
name: Streamlit chrome — use .streamlit/config.toml, not external CSS overrides
description: Streamlit's built-in widgets (page_link active state, segmented_control selected, sidebar nav) use Emotion CSS-in-JS that beats external CSS even with !important. Use the theme provider via .streamlit/config.toml instead.
type: feedback
originSessionId: 53e20cb7-f6e0-4235-94aa-3e4f9050dc57
---
For Streamlit's built-in widgets, the **theme provider** (set via
`.streamlit/config.toml` `[theme]` section) reliably controls visual
properties that external CSS cannot override.

**Why:** 2026-04-25 dashboard build. Sidebar's active page_link should
render in accent blue per mockup. External CSS rules
`a[data-testid="stPageLink"][aria-current="page"] { color: var(--accent)
!important }` and a descendant `*` variant both failed because:
1. Streamlit doesn't actually emit `aria-current="page"` on the active
   `<a>` — it uses a React `isCurrentPage` prop with no DOM attribute.
2. Streamlit's internal styling uses Emotion CSS-in-JS class hashes that
   beat external `[data-testid]` selectors at runtime.

Fix: added `dashboard/.streamlit/config.toml` with `primaryColor=#4A9EFF`.
The Streamlit theme provider injected the accent into its built-in
widgets directly. One config line replaced ~30 lines of CSS overrides
that didn't work.

**How to apply:**
- For Streamlit-emitted widgets (page_link, button, segmented_control,
  pills, tabs, selectbox, multiselect): set `primaryColor`,
  `backgroundColor`, `secondaryBackgroundColor`, `textColor`, `font` in
  `.streamlit/config.toml`. The theme provider wins.
- For custom HTML zones (anything you wrote with `st.markdown(...,
  unsafe_allow_html=True)`): use external CSS in `theme.GLOBAL_CSS`
  with the `gb-` class prefix.
- Hybrid pattern works fine — config.toml for chrome, GLOBAL_CSS for
  custom HTML. Don't try to fight Emotion with `!important` chains.
- The config.toml file MUST live in `.streamlit/` relative to the
  Streamlit run directory. Won't be picked up if moved.

**Verification:** restart Streamlit (config is read at boot, not hot-
reloaded) after editing config.toml. Then check the active page_link
in browser — text + dot should pick up the theme color.
