---
name: Command Center visual language locked (dark theme, Avenir, tile grid)
description: Kay validated the dashboard visual direction on 4/24 via HTML mockup. Dark background, Avenir font, subtle panels with 1px borders, status dots with colored glow, thin type for primary metrics. Use this as the visual reference when building the Streamlit version.
type: feedback
originSessionId: ebd58436-6958-4e18-98eb-a6797b0d0b46
---
On 4/24, Kay reacted to the HTML landing-page mockup with "WOW I am blown away, this looks amazing." Treat that as validation of the visual direction — do not diverge from it when building the real Streamlit dashboard.

**Reference files:**
- `dashboard/mockup-landing.html` — tile grid pattern (for Dashboard landing + any tile-based page)
- `dashboard/mockup-deal-aggregator.html` — data table pattern (for Deal Aggregator, Deal Pipeline, C-Suite & Skills, Tech Stack — any page showing rows of entities)

Both validated by Kay 4/24 with "blown away" reactions.

**Locked design elements (shared across all pages):**
- **Background:** near-black (#0B0D12), panels one step up (#141821), subtle 1px borders (#242A36)
- **Typography:** Avenir Next / Avenir stack (matches G&B brand per `feedback_doc_formatting`)
- **Label treatment:** 10.5px, uppercase, letter-spaced, muted color — Pober-style section heads
- **Status dots:** 8px colored dots with a soft glow (box-shadow) — functional, not emoji
- **Sidebar:** 240px, left-aligned, active item has accent-blue background wash + matching dot

**Tile-grid pattern (Dashboard landing):**
- Primary metric: 36px, weight 300, tight letter-spacing — feels premium, not loud
- 3 cols × 2 rows on desktop, 16px gap, 10px border-radius on tiles
- Trend arrows: HTML entities (↑ ↓ →), color-coded green/red/neutral
- Time-horizon labels: small uppercase in footer row (TODAY / NOW / THIS WEEK)
- Full tile clickable, subtle translateY(-1px) + border brighten on hover

**Data-table pattern (Deal Aggregator and similar list pages):**
- Summary strip at top: 4 inline stats with bold numbers + muted labels (e.g. "3 new today / 12 this week / 2 pursuing / 0 awaiting CIM")
- Filter bar: time-tab buttons (Today / This week / All) + dropdowns for source/industry/status + search box
- Table inside a panel with 10px radius, thin row dividers (#1C212C)
- Column headers: 10.5px uppercase letter-spaced, muted — matches tile label treatment
- Rows hover highlight (subtle row background shift) + cursor pointer — full row clickable
- Source tags: inline colored dot + small text (each source gets a distinct hue)
- Industry tags: small purple-on-purple chip below company name
- Status badges: pill-shaped, semantic colors (blue=new, muted=reviewed, green=pursuing, dim=passed)
- Numeric cells: tabular-nums + right-aligned for clean scanning
- External-link arrow (↗) in last column, brightens to accent blue on row hover

**Why:** 4/24 dashboard scoping session — Kay had requested visual clarity twice before I built this mockup; once she saw it, she was fully bought in. Do not re-litigate visual direction in subsequent sessions. If future design decisions contradict this language, pause and ask — don't rebuild.

**How to apply:**
- When building the Streamlit version, match this palette and type scale exactly — Streamlit's `st.markdown` with injected CSS is the path.
- Subsequent page mockups (Deal Aggregator, Deal Pipeline, etc.) must use the same palette, type scale, and spacing.
- Status dots (not emojis) for health/state indicators, per `feedback_silent_failures_are_the_core_concern` — the dots carry real meaning.
