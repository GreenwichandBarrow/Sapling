# Website Mockup — greenwichandbarrow.com Rebuild

**Status:** Day 1 of 5 (Mon May 4 → Fri May 8 2026)
**Plan:** `~/.claude/plans/please-share-the-plan-iridescent-bee.md`
**Brief:** `brain/outputs/2026-05-04-discussion-website-revamp.md`

## What this is

Off-platform HTML/CSS mockup for the greenwichandbarrow.com rebuild. Iterated by screenshot review through the week. Translated to Squarespace on Friday May 8, then this directory is archived or deleted.

## Stack

- Plain HTML
- Tailwind CSS via CDN (`https://cdn.tailwindcss.com`)
- Google Fonts (Cormorant Garamond serif + Inter sans)
- Local serve via `python3 -m http.server 8765` from this directory

## Run locally

```
cd "/Users/kaycschneider/Documents/AI Operations/scratch/website-mockup-2026-05"
python3 -m http.server 8765
# open http://localhost:8765/
```

## Squarespace translation notes (for Friday)

Approach: native section editor in current Squarespace template + targeted CSS injection (Settings > Advanced > Code Injection).

Translation order:
1. Pull all section copy verbatim from `index.html` and `insights/*.html`
2. Recreate section structure in Squarespace as separate sections (Hero, Three Pillars, Niche frame, Insights, Contact)
3. Inject ~30-60 lines of CSS for fonts, letter-spacing, max-widths, anchor smooth-scroll
4. Upload Insights essays as individual blog or page entries
5. QA staging URL on desktop + mobile before publish
6. Publish (no DNS change required)

Fallback (if current template too restrictive): swap to Squarespace 7.1 "Pacific" or "Tudor" template family. Template swap on 7.1 preserves content. Decision point: 11am Friday.

## Files

- `index.html` — single-page modular scroll with all sections
- `insights/essay-1-buyer-matters.html` — first transition essay (Wed)
- `insights/essay-2-*.html` — second essay (Thu)
- `insights/essay-3-*.html` — third essay (Thu)
- `assets/images/` — photography (sourced Tue or Thu)

## Constraints (from brief)

- No principal name, photo, LinkedIn link, or About-section anywhere
- No "fund / search fund / holding company / vehicle" in any copy
- No revenue / employee / financial references
- Email-only contact: contact@greenwichandbarrow.com
- Three pillars (Engage Community, Exceptional Service, Trust) thread through hero + sections
- Hoffman-register, not consulting voice
