# One-Pager Template Reference

## Source
- **Master template:** G&B Niche One-Pager Template (in G&B MASTER TEMPLATES folder)
- **Drive ID:** `1HfhQkl1-0iAZKIb7pIdIGEjw_o90DkaZ`
- **Local copy:** `brain/library/internal/one-pager-template/customs-bonds-template.pptx`
- **Built with:** python-pptx library

## Title Formatting (CRITICAL)
Row 0 of the table is the niche title. When replacing text, preserve the template run's font properties — especially the explicit `solidFill` with `srgbClr val="000000"` (black). If you create a new run instead of reusing the template's existing run, the text renders invisible (white on white). Always set `run.font.color.rgb = RGBColor(0, 0, 0)` and `run.font.size = Pt(16)` on Row 0.

## Sections (in order on the slide)

1. **Title** — Niche name + date
2. **Assessment / Status** — Quick verdict (Promising / Needs More Research / Concerns)
3. **Industry Overview** — What the industry is, key players, market size
4. **Industry Thesis** — Why this niche fits G&B's search criteria
5. **Macro Trends & Growth Drivers | Risks & Concerns** — Split column: tailwinds on left, risks on right
6. **Economics & Pricing | Competitive Landscape** — Split column: margins/pricing on left, competition on right
7. **Customers | Barriers to Entry** — Split column: who buys on left, moats on right
8. **Key Success Factors** — What matters for operating in this niche
9. **Exit** — Who would buy this business (PE firms, strategics, roll-ups)

## Output Specifications
- Format: .pptx (PowerPoint)
- Structure: Single slide, table-based layout
- Naming: `{Niche Name} {Month} {Year}.pptx`
- Save to: New subfolder in Industry Research Drive folder (parent: `1tiAc7lVveBwi_DlYcFUX2tFP6FVwYKmQ`)

## Drive Folder Structure

Industry Research parent folder: `1tiAc7lVveBwi_DlYcFUX2tFP6FVwYKmQ`
**Location:** `ANALYST / INDUSTRY RESEARCH`

Subfolders by status (niche folders go INSIDE these):
| Status | Folder ID |
|--------|-----------|
| WEEKLY REVIEW | `1eq7FjekjFhkV0RoBfgr9n6AXPtENEenT` |
| IDEATION | `1fQNl6mogJW-6u5XJeE5uYQGsDPx495_O` |
| TABLED | `1_k_c1F11ZNrv4MilATFrURLHdkNx0kRx` |
| KILLED | `19xsNk5KTVHF2jb6m_li8IAGjcw34nlMX` |

When creating a new niche folder, place it directly under the WEEKLY REVIEW subfolder (new niches skip IDEATION). When a niche is killed or tabled, move the folder to the corresponding status subfolder.

### Current Niche Folders
**WEEKLY REVIEW:**
| Niche | Folder ID |
|-------|-----------|
| Trust Administration | `1kStCWA4JQ31tzsOMqume2XEeeoaT0fWi` |
| Estate Management | `1mGXkPKF98KsNIR5vRrEl4SZaOqGUrCPa` |
| Trade Credit Insurance | `1WDy3v08zPxR7oGpTQ0B3rUdrgCV5qy7V` |
| Insurance Producer License Compliance | `1pjOHPBLxly2PsUnd8hmxVZOsfboRB7hH` |
| Art Insurance Brokerage (SPECIALTY INSURANCE) | `18Rv_m76SPsVZgUv6-yHCKH-sv1Cnwmm7` |

**TABLED:**
| Niche | Folder ID |
|-------|-----------|
| Art Storage | `1yFRqoTgTXViZdk6Lg6gQzOgOd1PpYFjF` |
| Estate Planning | `1-upIdD7QrGZUQIcqq1jrHsCJ7s-KiVO0` |
