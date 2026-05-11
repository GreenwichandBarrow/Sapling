---
name: franchise_firm_one_entry_only
description: For franchised intermediary firms (Transworld, Sunbelt, Murphy, etc.), keep ONE entry per firm — the local branch Kay engages with — never multiple location-rows.
type: feedback
originSessionId: a7305dfd-d3d9-44c7-840b-f8de8eb9bfd8
---
When a franchise broker / advisor / lender network has multiple regional branches, the Intermediary Target List should have **exactly one row per franchise firm**, not one per location.

**The rule:** For any franchise/affiliate network on Kay's intermediary target sheets (Brokers, IBs, Lawyers, CPAs, Lenders, Advisors), keep ONE entry. Pick the local branch Kay actually engages with. Drop all other regional duplicates.

**Examples of franchise networks that follow this rule:**
- Transworld Business Advisors (national franchise — many regional branches)
- Sunbelt Business Brokers (national franchise)
- Murphy Business & Financial
- Calhoun Companies
- VR Business Brokers
- First Choice Business Brokers
- Any "[Firm Name] of [City/County]" pattern is a tell

**Why:** Multi-location entries waste outreach calories (we'd contact two strangers at the same parent firm), break Attio dedup logic (same firm appears twice), and dilute relationship signal (Kay's already in the door at one branch — different branch contact looks like a different relationship). One row per franchise, owned by the local branch contact, lets future cleanups + outreach be coherent.

**How to apply:**
- During any intermediary list cleanup or import: detect franchise patterns ("[Firm] of [City/County]", explicit mentions of franchise/affiliate, multiple rows for same parent brand). Collapse to ONE row per firm.
- Choosing which branch to keep: priority order = (1) the one Kay has already contacted, (2) the one closest to Kay's region (NY/NJ/PA/CT), (3) the corporate HQ contact.
- Document the choice rationale in the row's Notes column.
- Apply silently during routine cleanup — don't surface as a Decision unless the choice between branches is non-obvious.
- Same rule applies to franchise lender networks, accounting firm regional offices, and association chapters with national parents.

**Source:** Kay 2026-05-01, after the cleanup pass left two Transworld rows (Albany + Passaic County NJ). Kay had already reached out to Transworld West Village NYC and that's the row that should be on the sheet. "We had said we would not repeat firms, just find the local one and keep only one."
