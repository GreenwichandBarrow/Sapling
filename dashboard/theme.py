"""Visual tokens and CSS for G&B Command Center.

Palette and type scale mirror dashboard/mockup-landing.html — validated 2026-04-24.
Do not diverge without Kay's sign-off (see memory/feedback_dashboard_visual_language_locked.md).
"""

REFRESH_SECONDS = 60

PALETTE = {
    "bg": "#0B0D12",
    "panel": "#141821",
    "panel_hover": "#1A1F2A",
    "row_hover": "#181C26",
    "border": "#242A36",
    "border_bright": "#2E3647",
    "border_soft": "#1C212C",
    "divider": "#1C212C",
    "text": "#E8ECF3",
    "text_muted": "#8B93A7",
    "text_dim": "#5B6378",
    "accent": "#4A9EFF",
    "green": "#3FD17F",
    "yellow": "#F5C451",
    "red": "#FF5A5A",
    "neutral": "#6B7280",
    "purple": "#B084F0",
}

# (label, url_path, implemented) — st.navigation uses implemented==True pages;
# unimplemented items render as disabled sidebar entries.
# Order validated 2026-04-24: deal-flow surfaces grouped above system-internals.
# Tech Stack retired (merged into Infrastructure).
NAV_ITEMS = [
    ("Dashboard", "dashboard", True),
    ("Deal Aggregator", "deal-aggregator", True),
    ("Active Deal Pipeline", "deal-pipeline", True),
    ("M&A Analytics", "ma-analytics", False),
    ("C-Suite & Skills", "c-suite-skills", True),
    ("Infrastructure", "infrastructure", True),
]


GLOBAL_CSS = f"""
<style>
  :root {{
    --bg: {PALETTE["bg"]};
    --panel: {PALETTE["panel"]};
    --panel-hover: {PALETTE["panel_hover"]};
    --row-hover: {PALETTE["row_hover"]};
    --border: {PALETTE["border"]};
    --border-bright: {PALETTE["border_bright"]};
    --border-soft: {PALETTE["border_soft"]};
    --divider: {PALETTE["divider"]};
    --text: {PALETTE["text"]};
    --text-muted: {PALETTE["text_muted"]};
    --text-dim: {PALETTE["text_dim"]};
    --accent: {PALETTE["accent"]};
    --green: {PALETTE["green"]};
    --yellow: {PALETTE["yellow"]};
    --red: {PALETTE["red"]};
    --neutral: {PALETTE["neutral"]};
    --purple: {PALETTE["purple"]};
  }}

  /* Hide Streamlit chrome that fights our design */
  header[data-testid="stHeader"] {{ display: none; }}
  div[data-testid="stToolbar"] {{ display: none; }}
  #MainMenu {{ visibility: hidden; }}
  footer {{ visibility: hidden; }}
  div[data-testid="stDecoration"] {{ display: none; }}
  div[data-testid="stStatusWidget"] {{ display: none; }}

  html, body, [data-testid="stAppViewContainer"], [data-testid="stMain"] {{
    background: var(--bg) !important;
    color: var(--text);
    font-family: "Avenir Next", "Avenir", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    font-size: 14px;
    line-height: 1.45;
    -webkit-font-smoothing: antialiased;
  }}

  /* Main content padding — match mockup's 24/32/40 */
  [data-testid="stMain"] .stMainBlockContainer,
  section.main > div.block-container,
  [data-testid="stAppViewBlockContainer"] {{
    padding: 24px 32px 40px !important;
    max-width: none !important;
  }}

  /* Remove default vertical gap between Streamlit elements so our HTML carries the spacing */
  [data-testid="stVerticalBlock"] {{ gap: 0 !important; }}

  /* -------- SIDEBAR -------- */
  [data-testid="stSidebar"] {{
    background: var(--panel) !important;
    border-right: 1px solid var(--border);
    width: 240px !important;
    min-width: 240px !important;
  }}
  [data-testid="stSidebar"] > div:first-child {{
    background: var(--panel) !important;
    padding: 20px 0 !important;
  }}
  [data-testid="stSidebarContent"] {{ padding: 20px 0 !important; }}
  [data-testid="stSidebarHeader"] {{ display: none !important; }}
  [data-testid="stSidebarCollapseButton"] {{ display: none !important; }}

  .gb-brand {{
    padding: 0 20px 24px;
    border-bottom: 1px solid var(--border);
    margin-bottom: 16px;
  }}
  .gb-brand .logo {{
    font-size: 15px;
    font-weight: 600;
    letter-spacing: 0.02em;
    color: var(--text);
  }}
  .gb-brand .sub {{
    font-size: 11px;
    color: var(--text-dim);
    margin-top: 2px;
    letter-spacing: 0.06em;
    text-transform: uppercase;
  }}

  .gb-nav {{ padding: 0 12px; }}
  .gb-nav-item {{
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 9px 12px;
    border-radius: 6px;
    color: var(--text-muted);
    font-size: 13px;
    margin-bottom: 2px;
    transition: all 0.15s;
  }}
  .gb-nav-item.active {{
    background: rgba(74, 158, 255, 0.12);
    color: var(--accent);
    font-weight: 500;
  }}
  .gb-nav-item.disabled {{ color: var(--text-dim); cursor: not-allowed; }}
  .gb-nav-item .dot {{
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background: var(--text-dim);
  }}
  .gb-nav-item.active .dot {{ background: var(--accent); }}

  /* Style Streamlit's st.page_link to match our custom nav items. */
  [data-testid="stSidebar"] a[data-testid="stPageLink"],
  [data-testid="stSidebar"] a[data-testid="stPageLink-NavLink"] {{
    display: flex !important;
    align-items: center !important;
    gap: 10px !important;
    padding: 9px 12px !important;
    border-radius: 6px !important;
    color: var(--text-muted) !important;
    font-size: 13px !important;
    margin-bottom: 2px !important;
    text-decoration: none !important;
    background: transparent !important;
    transition: all 0.15s !important;
  }}
  [data-testid="stSidebar"] a[data-testid="stPageLink"]:hover,
  [data-testid="stSidebar"] a[data-testid="stPageLink-NavLink"]:hover {{
    background: var(--panel-hover) !important;
    color: var(--text) !important;
  }}
  [data-testid="stSidebar"] a[data-testid="stPageLink"][aria-current="page"],
  [data-testid="stSidebar"] a[data-testid="stPageLink-NavLink"][aria-current="page"] {{
    background: rgba(74, 158, 255, 0.12) !important;
    color: var(--accent) !important;
    font-weight: 500 !important;
  }}
  /* Leading dot injected via ::before so labels match the HTML mockup. */
  [data-testid="stSidebar"] a[data-testid="stPageLink"]::before,
  [data-testid="stSidebar"] a[data-testid="stPageLink-NavLink"]::before {{
    content: "";
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background: var(--text-dim);
    flex-shrink: 0;
  }}
  [data-testid="stSidebar"] a[data-testid="stPageLink"][aria-current="page"]::before,
  [data-testid="stSidebar"] a[data-testid="stPageLink-NavLink"][aria-current="page"]::before {{
    background: var(--accent);
  }}
  /* Streamlit sometimes wraps page_link labels in an extra span — strip its own padding. */
  [data-testid="stSidebar"] a[data-testid="stPageLink"] > div,
  [data-testid="stSidebar"] a[data-testid="stPageLink"] p,
  [data-testid="stSidebar"] a[data-testid="stPageLink-NavLink"] > div,
  [data-testid="stSidebar"] a[data-testid="stPageLink-NavLink"] p {{
    margin: 0 !important;
    padding: 0 !important;
    font-size: 13px !important;
    line-height: 1 !important;
  }}

  /* -------- TOPBAR -------- */
  .gb-topbar {{
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    margin-bottom: 28px;
    padding-bottom: 16px;
    border-bottom: 1px solid var(--border);
  }}
  .gb-topbar h1 {{
    font-size: 20px;
    font-weight: 500;
    letter-spacing: -0.01em;
    margin: 0;
    color: var(--text);
  }}
  .gb-topbar .meta {{
    font-size: 12px;
    color: var(--text-dim);
  }}
  .gb-topbar .meta .sep {{ margin: 0 8px; color: var(--border); }}

  /* -------- TILE GRID -------- */
  .gb-grid {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 16px;
  }}
  .gb-tile {{
    background: var(--panel);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 20px;
    min-height: 160px;
    display: flex;
    flex-direction: column;
    cursor: pointer;
    transition: all 0.18s;
  }}
  .gb-tile:hover {{
    background: var(--panel-hover);
    border-color: var(--border-bright);
    transform: translateY(-1px);
  }}
  .gb-tile .label {{
    font-size: 10.5px;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--text-dim);
    margin-bottom: 14px;
  }}
  .gb-tile .primary {{
    font-size: 36px;
    font-weight: 300;
    letter-spacing: -0.02em;
    color: var(--text);
    line-height: 1.1;
  }}
  .gb-tile .primary .unit {{
    font-size: 14px;
    color: var(--text-muted);
    margin-left: 6px;
    font-weight: 400;
  }}
  .gb-tile .footer {{
    margin-top: auto;
    padding-top: 12px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }}
  .gb-trend {{
    font-size: 12px;
    display: flex;
    align-items: center;
    gap: 5px;
  }}
  .gb-trend.up {{ color: var(--green); }}
  .gb-trend.down {{ color: var(--red); }}
  .gb-trend.flat {{ color: var(--neutral); }}
  .gb-horizon {{
    font-size: 11px;
    color: var(--text-dim);
    letter-spacing: 0.04em;
  }}

  /* Status dots */
  .gb-status-row {{
    display: flex;
    align-items: center;
    gap: 8px;
    margin-top: 8px;
  }}
  .gb-status-dot {{
    width: 8px;
    height: 8px;
    border-radius: 50%;
  }}
  .gb-status-dot.green {{
    background: var(--green);
    box-shadow: 0 0 8px rgba(63, 209, 127, 0.3);
  }}
  .gb-status-dot.yellow {{
    background: var(--yellow);
    box-shadow: 0 0 8px rgba(245, 196, 81, 0.3);
  }}
  .gb-status-dot.red {{
    background: var(--red);
    box-shadow: 0 0 8px rgba(255, 90, 90, 0.3);
  }}
  .gb-status-text {{
    font-size: 12px;
    color: var(--text-muted);
  }}

  /* M&A stacked tile list */
  .gb-ma-list {{
    display: grid;
    grid-template-columns: 1fr auto;
    gap: 6px 14px;
    margin-top: 4px;
  }}
  .gb-ma-label {{
    font-size: 12.5px;
    color: var(--text-muted);
  }}
  .gb-ma-value {{
    font-size: 14px;
    font-weight: 500;
    color: var(--text);
    text-align: right;
    font-variant-numeric: tabular-nums;
  }}

  .gb-page-note {{
    margin-top: 32px;
    font-size: 11px;
    color: var(--text-dim);
    text-align: center;
    letter-spacing: 0.04em;
  }}

  /* -------- PAGE SUBTITLE -------- */
  .gb-subtitle {{
    font-size: 13px;
    color: var(--text-muted);
    margin-top: -16px;
    margin-bottom: 24px;
  }}
  .gb-subtitle .highlight {{ color: var(--text); font-weight: 500; }}

  /* -------- SUMMARY STRIP -------- */
  .gb-summary {{
    display: flex;
    gap: 28px;
    padding: 10px 0 20px;
    font-size: 12px;
    color: var(--text-muted);
    flex-wrap: wrap;
  }}
  .gb-summary .num {{
    color: var(--text);
    font-weight: 500;
    margin-right: 5px;
    font-variant-numeric: tabular-nums;
  }}

  /* -------- FILTER BAR -------- */
  .gb-filter-bar {{
    display: flex;
    gap: 10px;
    align-items: center;
    margin-bottom: 20px;
    padding-bottom: 20px;
    border-bottom: 1px solid var(--border);
    flex-wrap: wrap;
  }}
  .gb-filter-tabs {{ display: flex; gap: 4px; }}
  .gb-filter-tab {{
    padding: 6px 12px;
    font-size: 12px;
    color: var(--text-muted);
    background: transparent;
    border: 1px solid var(--border);
    border-radius: 6px;
    transition: all 0.15s;
  }}
  .gb-filter-tab.active {{
    background: rgba(74, 158, 255, 0.1);
    border-color: var(--accent);
    color: var(--accent);
  }}
  .gb-filter-select {{
    padding: 6px 10px;
    font-size: 12px;
    background: var(--panel);
    border: 1px solid var(--border);
    border-radius: 6px;
    color: var(--text-muted);
    font-family: inherit;
  }}
  .gb-filter-search {{
    flex: 1;
    max-width: 260px;
    padding: 6px 12px;
    font-size: 12px;
    background: var(--panel);
    border: 1px solid var(--border);
    border-radius: 6px;
    color: var(--text);
    font-family: inherit;
  }}
  .gb-filter-search::placeholder {{ color: var(--text-dim); }}

  /* -------- DATA TABLE -------- */
  .gb-table-wrap {{
    background: var(--panel);
    border: 1px solid var(--border);
    border-radius: 10px;
    overflow: hidden;
  }}
  .gb-table {{ width: 100%; border-collapse: collapse; }}
  .gb-table thead th {{
    text-align: left;
    padding: 12px 14px;
    font-size: 10.5px;
    font-weight: 500;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--text-dim);
    border-bottom: 1px solid var(--border);
    background: rgba(255,255,255,0.01);
  }}
  .gb-table tbody td {{
    padding: 14px;
    font-size: 13px;
    border-bottom: 1px solid var(--border-soft);
    color: var(--text);
    vertical-align: middle;
  }}
  .gb-table tbody tr {{ transition: background 0.15s; }}
  .gb-table tbody tr:hover {{ background: var(--row-hover); }}
  .gb-table tbody tr:last-child td {{ border-bottom: none; }}

  .gb-company {{ font-weight: 500; }}
  .gb-industry-tag {{
    display: inline-block;
    font-size: 11px;
    padding: 2px 8px;
    background: rgba(176, 132, 240, 0.12);
    color: var(--purple);
    border-radius: 4px;
    margin-top: 3px;
    letter-spacing: 0.02em;
  }}
  .gb-owner, .gb-location {{ color: var(--text-muted); }}
  .gb-location {{ font-variant-numeric: tabular-nums; }}
  .gb-num {{
    font-variant-numeric: tabular-nums;
    text-align: right;
  }}
  .gb-num.dim {{ color: var(--text-dim); }}

  .gb-source-tag {{
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-size: 11px;
    color: var(--text-muted);
  }}
  .gb-source-tag .src-dot {{
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background: var(--accent);
  }}
  .gb-source-tag .src-dot.axial      {{ background: var(--green); }}
  .gb-source-tag .src-dot.bizbuysell {{ background: var(--accent); }}
  .gb-source-tag .src-dot.email      {{ background: var(--yellow); }}
  .gb-source-tag .src-dot.assoc      {{ background: var(--purple); }}
  .gb-source-tag .src-dot.dealsx     {{ background: var(--red); }}
  .gb-source-tag .src-dot.other      {{ background: var(--neutral); }}

  .gb-status-badge {{
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-size: 11.5px;
    padding: 3px 10px;
    border-radius: 12px;
    font-weight: 500;
  }}
  .gb-status-badge.new      {{ background: rgba(74, 158, 255, 0.12); color: var(--accent); }}
  .gb-status-badge.reviewed {{ background: rgba(139, 147, 167, 0.14); color: var(--text-muted); }}
  .gb-status-badge.pursuing {{ background: rgba(63, 209, 127, 0.12); color: var(--green); }}
  .gb-status-badge.passed   {{ background: rgba(107, 114, 128, 0.14); color: var(--text-dim); }}

  .gb-link-cell {{ text-align: center; width: 40px; }}
  .gb-link-icon {{
    display: inline-block;
    color: var(--text-dim);
    font-size: 14px;
    transition: color 0.15s;
    text-decoration: none;
  }}
  .gb-link-icon:hover {{ color: var(--accent); }}

  .gb-empty {{
    padding: 40px 20px;
    text-align: center;
    color: var(--text-dim);
    font-size: 13px;
  }}

  /* -------- KANBAN BOARD (Active Deal Pipeline) -------- */
  /* 4 columns (NDA forward) — fits typical desktop without horizontal scroll. */
  .gb-kanban-wrap {{
    overflow-x: auto;
    padding-bottom: 8px;
    margin-bottom: 20px;
  }}
  .gb-kanban {{
    display: grid;
    grid-template-columns: repeat(4, minmax(240px, 1fr));
    gap: 12px;
  }}
  .gb-kanban-col {{
    background: var(--panel);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 0;
    min-height: 220px;
    display: flex;
    flex-direction: column;
    overflow: hidden;
  }}
  .gb-kanban-col-header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 12px 14px;
    border-bottom: 1px solid var(--border-soft);
  }}
  .gb-kanban-col-name {{
    font-size: 10.5px;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--text);
    font-weight: 600;
  }}
  .gb-kanban-col-count {{
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-size: 11px;
    color: var(--text-muted);
    font-variant-numeric: tabular-nums;
  }}
  .gb-kanban-col-count .n {{
    font-size: 12px;
    font-weight: 500;
    color: var(--text);
    background: rgba(255,255,255,0.05);
    padding: 1px 7px;
    border-radius: 8px;
  }}
  .gb-kanban-col-dot {{
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: var(--neutral);
  }}
  .gb-kanban-col-dot.green {{
    background: var(--green);
    box-shadow: 0 0 6px rgba(63,209,127,0.4);
  }}
  .gb-kanban-col-dot.grey {{ background: var(--text-dim); }}
  .gb-kanban-bar {{
    height: 2px;
    background: var(--border-soft);
    width: 100%;
  }}
  .gb-kanban-bar-fill {{
    height: 100%;
    background: var(--accent);
    transition: width 0.25s;
  }}
  .gb-kanban-bar-fill.empty {{ background: var(--border-soft); }}

  .gb-kanban-cards {{
    padding: 10px;
    display: flex;
    flex-direction: column;
    gap: 8px;
    flex: 1;
  }}
  .gb-kanban-card {{
    display: block;
    background: var(--row-hover);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 11px 12px;
    text-decoration: none !important;
    color: inherit !important;
    transition: all 0.15s;
    position: relative;
  }}
  .gb-kanban-card:hover {{
    background: var(--panel-hover);
    border-color: var(--border-bright);
    transform: translateY(-1px);
  }}
  .gb-kanban-card .company {{
    font-size: 12.5px;
    font-weight: 500;
    color: var(--text);
    line-height: 1.35;
    margin-bottom: 6px;
    padding-right: 10px;
  }}
  .gb-kanban-card .meta {{
    font-size: 11px;
    color: var(--text-muted);
    margin-bottom: 6px;
    line-height: 1.4;
  }}
  .gb-kanban-card .meta .sep {{
    color: var(--text-dim);
    margin: 0 4px;
  }}
  .gb-kanban-card .footer {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    font-size: 10.5px;
    color: var(--text-dim);
    font-variant-numeric: tabular-nums;
  }}
  .gb-kanban-card .footer .age {{
    display: inline-flex;
    align-items: center;
    gap: 4px;
  }}
  .gb-kanban-card .footer .age-dot {{
    width: 5px;
    height: 5px;
    border-radius: 50%;
    background: var(--text-dim);
  }}
  .gb-kanban-card .footer .age-dot.green {{ background: var(--green); }}
  .gb-kanban-card .footer .age-dot.yellow {{ background: var(--yellow); }}
  .gb-kanban-card .footer .age-dot.red {{ background: var(--red); }}
  .gb-kanban-card .footer .age-dot.grey {{ background: var(--text-dim); }}
  .gb-kanban-card .footer .last-touch {{ font-size: 10px; }}

  /* Category chip on cards — color-coded for at-a-glance scanning. */
  .gb-cat {{
    display: inline-block;
    font-size: 10px;
    padding: 2px 7px;
    border-radius: 3px;
    margin-bottom: 8px;
    letter-spacing: 0.02em;
    background: rgba(139, 147, 167, 0.12);
    color: var(--text-muted);
  }}
  .gb-cat.insurance {{ background: rgba(74, 158, 255, 0.12); color: var(--accent); }}
  .gb-cat.fineart {{ background: rgba(176, 132, 240, 0.14); color: var(--purple); }}
  .gb-cat.shipping {{ background: rgba(245, 196, 81, 0.12); color: var(--yellow); }}
  .gb-cat.consulting {{ background: rgba(63, 209, 127, 0.12); color: var(--green); }}

  .gb-kanban-col-empty {{
    color: var(--text-dim);
    font-size: 11.5px;
    padding: 16px 8px;
    font-style: italic;
    text-align: center;
  }}

  /* -------- CLOSED STRIP -------- */
  .gb-closed-strip {{
    background: var(--panel);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 16px 20px;
    margin-top: 4px;
  }}
  .gb-closed-header {{
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    margin-bottom: 12px;
  }}
  .gb-closed-title {{
    font-size: 10.5px;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--text-muted);
    font-weight: 500;
  }}
  .gb-closed-total {{
    font-size: 12px;
    color: var(--text-dim);
  }}
  .gb-closed-total strong {{
    color: var(--text-muted);
    font-weight: 500;
  }}
  .gb-closed-list {{
    display: flex;
    gap: 6px;
    flex-wrap: wrap;
  }}
  .gb-closed-item {{
    font-size: 11.5px;
    color: var(--text-muted) !important;
    text-decoration: none !important;
    padding: 4px 10px;
    background: var(--bg);
    border: 1px solid var(--border-soft);
    border-radius: 4px;
    transition: all 0.15s;
  }}
  .gb-closed-item:hover {{
    color: var(--text) !important;
    border-color: var(--border-bright);
  }}

  /* -------- C-SUITE & SKILLS PAGE -------- */
  .gb-csuite {{
    background: var(--panel);
    border: 1px solid var(--border);
    border-radius: 10px;
    margin-bottom: 16px;
    overflow: hidden;
  }}
  .gb-csuite-head {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 14px 18px;
    border-bottom: 1px solid var(--border);
    background: rgba(255,255,255,0.01);
  }}
  .gb-csuite-head-left {{
    display: flex;
    align-items: baseline;
    gap: 12px;
  }}
  .gb-csuite-label {{
    font-size: 10.5px;
    font-weight: 600;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: var(--text);
  }}
  .gb-csuite-sublabel {{
    font-size: 10.5px;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: var(--text-dim);
  }}
  .gb-csuite-meta {{
    font-size: 11px;
    color: var(--text-muted);
    font-variant-numeric: tabular-nums;
    letter-spacing: 0.02em;
  }}
  .gb-csuite-meta .pill {{
    display: inline-block;
    margin-left: 8px;
    padding: 2px 8px;
    background: rgba(63, 209, 127, 0.10);
    color: var(--green);
    border-radius: 4px;
    font-size: 10.5px;
    font-weight: 500;
  }}
  .gb-csuite-meta .pill.red {{ background: rgba(255, 90, 90, 0.12); color: var(--red); }}
  .gb-csuite-meta .pill.neutral {{ background: rgba(139, 147, 167, 0.14); color: var(--text-muted); }}

  .gb-skill-row {{
    display: grid;
    grid-template-columns: 28px 1fr 200px 150px 96px;
    align-items: center;
    gap: 14px;
    padding: 14px 18px;
    font-size: 13px;
    border-bottom: 1px solid var(--border-soft);
  }}
  .gb-skill-row:last-child {{ border-bottom: none; }}
  .gb-skill-row:hover {{ background: var(--row-hover); }}

  .gb-skill-cell {{ min-width: 0; }}
  .gb-skill-name {{
    font-weight: 500;
    font-family: "SF Mono", "Menlo", "Monaco", monospace;
    font-size: 12.5px;
    color: var(--text);
    letter-spacing: -0.01em;
  }}
  .gb-skill-desc {{
    font-size: 11.5px;
    color: var(--text-muted);
    margin-top: 3px;
    line-height: 1.4;
  }}

  .gb-skill-schedule {{
    font-size: 11.5px;
    color: var(--text-muted);
    font-variant-numeric: tabular-nums;
  }}
  .gb-skill-schedule.dim {{ color: var(--text-dim); }}

  .gb-skill-last-run {{
    font-size: 11.5px;
    color: var(--text-muted);
    font-variant-numeric: tabular-nums;
  }}
  .gb-skill-last-run.green {{ color: var(--green); }}
  .gb-skill-last-run.yellow {{ color: var(--yellow); }}
  .gb-skill-last-run.red {{ color: var(--red); }}
  .gb-skill-last-run.dim {{ color: var(--text-dim); }}

  .gb-skill-badge {{
    font-size: 10px;
    padding: 3px 8px;
    border-radius: 10px;
    font-weight: 500;
    text-align: center;
    letter-spacing: 0.06em;
    text-transform: uppercase;
  }}
  .gb-skill-badge.scheduled {{
    background: rgba(176, 132, 240, 0.12);
    color: var(--purple);
  }}
  .gb-skill-badge.ondemand {{
    background: rgba(139, 147, 167, 0.10);
    color: var(--text-muted);
  }}
  .gb-skill-badge.gap {{
    background: rgba(255, 90, 90, 0.14);
    color: var(--red);
  }}

  /* Status dot variants for the skill row (extends shared .gb-status-dot). */
  .gb-status-dot.grey {{ background: var(--text-dim); }}
  .gb-status-dot.ondemand {{
    background: transparent;
    border: 1px dashed var(--text-dim);
    box-shadow: none;
  }}

  /* Make the bare 8px status dot scale up to 10px on this page so it sits
     visually centered in the 28px gutter. */
  .gb-skill-row .gb-status-dot {{ width: 10px; height: 10px; }}

  .gb-csuite-empty {{
    padding: 18px;
    font-size: 12.5px;
    color: var(--text-dim);
    font-style: italic;
    text-align: center;
  }}
  .gb-csuite-empty .candidates {{
    display: block;
    margin-top: 6px;
    font-style: normal;
    font-size: 11px;
    color: var(--text-muted);
    font-family: "SF Mono", "Menlo", monospace;
  }}

  /* -------- INFRASTRUCTURE PAGE -------- */
  .gb-zone {{
    background: var(--panel);
    border: 1px solid var(--border);
    border-radius: 10px;
    margin-bottom: 16px;
    overflow: hidden;
  }}
  .gb-zone.gb-zone-pending {{ opacity: 0.65; }}
  .gb-zone-head {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 14px 18px;
    border-bottom: 1px solid var(--border);
    background: rgba(255,255,255,0.01);
  }}
  .gb-zone-label {{
    font-size: 10.5px;
    font-weight: 600;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: var(--text);
  }}
  .gb-zone-sublabel {{
    font-size: 11px;
    color: var(--text-muted);
    letter-spacing: 0.02em;
    margin-top: 3px;
  }}
  .gb-zone-meta {{
    font-size: 11px;
    color: var(--text-muted);
    font-variant-numeric: tabular-nums;
  }}
  .gb-zone-meta .pill {{
    display: inline-block;
    margin-left: 8px;
    padding: 2px 8px;
    background: rgba(63, 209, 127, 0.10);
    color: var(--green);
    border-radius: 4px;
    font-size: 10.5px;
    font-weight: 500;
  }}
  .gb-zone-meta .pill.red {{ background: rgba(255, 90, 90, 0.12); color: var(--red); }}
  .gb-zone-meta .pill.yellow {{ background: rgba(245, 196, 81, 0.12); color: var(--yellow); }}
  .gb-zone-meta .pill.neutral {{ background: rgba(139, 147, 167, 0.14); color: var(--text-muted); }}
  .gb-zone-empty {{
    padding: 18px;
    font-size: 12px;
    color: var(--text-dim);
    font-style: italic;
    text-align: center;
  }}

  /* Zone 1: System Health tile grid */
  .gb-health-grid {{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1px;
    background: var(--border);
  }}
  .gb-health-tile {{
    background: var(--panel);
    padding: 16px 18px;
    display: flex;
    flex-direction: column;
    gap: 8px;
  }}
  .gb-health-tile.alert {{ background: rgba(255, 90, 90, 0.04); }}
  .gb-health-tile.warn {{ background: rgba(245, 196, 81, 0.03); }}
  .gb-health-tile-label {{
    font-size: 10.5px;
    font-weight: 500;
    letter-spacing: 0.10em;
    text-transform: uppercase;
    color: var(--text-dim);
  }}
  .gb-health-tile-value {{
    display: flex;
    align-items: center;
    gap: 10px;
    font-size: 18px;
    font-weight: 300;
    color: var(--text);
    font-variant-numeric: tabular-nums;
    letter-spacing: -0.01em;
  }}
  .gb-health-tile-value .gb-status-dot {{ width: 10px; height: 10px; }}
  .gb-health-tile-detail {{
    font-size: 11.5px;
    color: var(--text-muted);
    line-height: 1.35;
  }}

  /* Zone 5: Tech Stack inventory */
  .gb-stack-list {{}}
  .gb-stack-row {{
    display: grid;
    grid-template-columns: 200px 1fr;
    align-items: flex-start;
    gap: 18px;
    padding: 12px 18px;
    border-bottom: 1px solid var(--border-soft);
  }}
  .gb-stack-row:last-child {{ border-bottom: none; }}
  .gb-stack-cat {{
    font-size: 10.5px;
    font-weight: 600;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--text-dim);
    padding-top: 6px;
  }}
  .gb-stack-chips {{ display: flex; flex-wrap: wrap; gap: 6px; }}
  .gb-stack-chip {{
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 5px 11px;
    font-size: 11.5px;
    font-family: "SF Mono", "Menlo", monospace;
    color: var(--text);
    background: rgba(255,255,255,0.03);
    border: 1px solid var(--border);
    border-radius: 14px;
    letter-spacing: -0.01em;
  }}
  .gb-stack-dot {{
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background: var(--green);
  }}
  .gb-stack-dot.yellow {{ background: var(--yellow); }}
  .gb-stack-dot.red {{ background: var(--red); }}
  .gb-stack-dot.dim {{ background: var(--text-dim); }}
  .gb-stack-chip .note {{
    font-size: 10px;
    color: var(--text-dim);
    font-family: inherit;
    margin-left: 4px;
  }}
</style>
"""
