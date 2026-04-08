---
name: river-guide-builder
description: "Proactive ecosystem mapping per niche — find association leaders, industry CPAs, M&A lawyers, consultants, and adjacent operators who can introduce Kay to business owners. Output: ranked coffee chat targets."
user_invocable: true
context_budget:
  skill_md: 2000
  max_references: 2
  sub_agent_limit: 2000
---

<objective>
Map the professional ecosystem around each active niche to identify people who know business owners and can make introductions. These are "river guides" — people who touch deal flow before it gets listed.

**This is PROACTIVE relationship building** — distinct from intermediary-manager (passive deal scanning) and outreach-manager (direct owner outreach).

**Proof of concept: Margot Romano.** She introduced Kay to Alexandra Kelly (UOVO), Sarah De Blasio (Chartwell Insurance), and Christopher Wise (Risk Strategies). Every conversation produced at least one high-quality introduction. This skill systematizes finding more Margots.

**This skill does NOT:**
- Scan broker platforms for posted deals (intermediary-manager)
- Draft outreach emails to business owners (outreach-manager)
- Create or manage target sheets (target-discovery)
- Track nurture cadences (relationship-manager)

**This skill DOES:**
- Research ecosystem contacts per niche across 5 categories
- Score and rank contacts by proximity to deal flow
- Check warm intro paths via Attio and vault
- Output ranked "coffee chat menu" for Kay
- Feed new contacts into Attio intermediary pipeline
- Trigger meeting-brief-manager for coffee chat prep

**Tracking:** Uses existing Attio intermediary pipeline. Does NOT create a separate tracking system. New contacts enter as "Identified" with relationship_type: "River Guide".
</objective>

<ecosystem_categories>
## 5 Ecosystem Categories

For each active niche, research and identify contacts in these categories:

### 1. Association Leaders
Officers, board members, committee chairs of industry associations. They know every member, see industry dynamics, and know who's growing or struggling.

**Per niche:**
- Pest Management: NPMA board, state PMA presidents, NPMA committees (M&A, business development)
- Insurance: PIA chapter heads, Big I (IIABA) state leaders, NAIA officers
- Fractional CFO: AICPA leadership, state CPA society officers, IMA chapter heads
- Estate Management: IREM officers, CAI chapter presidents, BOMA local leaders

### 2. Industry CPAs
Accounting firms specializing in that industry. They see the financials, know who's profitable, and hear "I'm thinking about selling" before anyone else.

**Per niche:**
- Pest Management: PCO Bookkeepers (Dan Gordon, $1B+ in pest M&A transactions), industry-specific accounting firms
- Insurance: Reagan Consulting, MarshBerry (valuation side), insurance-specific CPA firms
- Fractional CFO: Poe Group Advisors (accounting practice transitions), Accounting Practice Sales
- Estate Management: Property management accounting specialists

### 3. Industry M&A Lawyers
Attorneys who handle transactions in that space. They know what's trading, at what multiples, and who's looking.

**Per niche:**
- Pest Management: Attorneys specializing in pest/environmental services M&A
- Insurance: Insurance agency M&A attorneys (book-of-business transfers, carrier appointment law)
- Fractional CFO: Accounting practice transition attorneys
- Estate Management: Property management M&A attorneys

### 4. Consultants & Advisors
Management consultants, valuation firms, industry advisors who work with owners on operational health, growth, and succession planning.

**Per niche:**
- Pest Management: Keystone Business Advisors, PCT consultants, NPMA business management consultants
- Insurance: Sica Fletcher (advisory, $19B+ since 2014), Agency Consulting Group, Optis Partners
- Fractional CFO: Practice management consultants, succession planning specialists
- Estate Management: Property management consulting firms, community association advisors

### 5. Adjacent Operators
Owners of related businesses who know the competitive landscape and hear about deals through industry networks.

**Per niche:**
- Pest Management: Lawn care operators, environmental services owners, janitorial franchise owners
- Insurance: Benefits brokers, financial planners serving same HNWI clients, wealth managers
- Fractional CFO: Bookkeeping firm owners, payroll service operators, tax prep chain owners
- Estate Management: Concierge service operators, luxury property maintenance owners
</ecosystem_categories>

<workflow>
## Workflow

### Step 1: Load Active Niches
Read Industry Research Tracker WEEKLY REVIEW tab for niches with status "Active-Outreach" or "Active-Long Term":
```bash
gog sheets get 1vHx4E1tRTR6V3k7NQeHdCrUjDITJVtZA5YPSIFeSins "'WEEKLY REVIEW'!A3:D20" --json
```

### Step 2: Read Existing Data
For each niche, check:
- **Associations tab** on the target sheet (already has some contacts)
- **Attio intermediary pipeline** — existing river guides and their status
- **Vault entities** — any existing river guide relationships (search for relationship_type or tags)

### Step 3: Research New Contacts
For each niche x category combination:
1. Web search for association leadership rosters
2. Apollo search for industry-specific CPAs and lawyers
3. LinkedIn research for consultants and adjacent operators
4. Cross-reference against Attio to avoid duplicates

### Step 4: Score Contacts
Rate each contact on 3 dimensions (1-3 scale):

| Dimension | 3 (High) | 2 (Medium) | 1 (Low) |
|-----------|----------|------------|---------|
| **Deal Flow Proximity** | Directly advises owners on exits/succession | Sees financials or industry data | Knows the industry generally |
| **Accessibility** | Warm intro path exists | Cold but likely to respond (same networks) | Cold, unclear response likelihood |
| **Niche Alignment** | Works exclusively in this niche | Works in adjacent space | General practice with some exposure |

**Total score 7-9:** Priority coffee chat target
**Total score 4-6:** Worth an intro email
**Total score 1-3:** Monitor only

### Step 5: Check Warm Intro Paths
For priority targets (7-9), run warm-intro-finder:
- Check Attio for shared connections
- Check vault calls for name mentions
- Check LinkedIn for 2nd degree connections
- Note the path in the output

### Step 6: Output Coffee Chat Menu
Produce a ranked list for Kay, organized by niche:

```
## Pest Management — River Guide Targets

1. [Name] — [Role, Firm] — Score: 8/9
   Why: [1 line — what they know, why they're valuable]
   Warm path: [connection or "Cold"]
   Suggested approach: [coffee invite / intro request / conference meetup]

2. ...
```

### Step 7: Create Attio Records
For approved targets, create People records in Attio with:
- relationship_type: "River Guide"
- nurture_cadence: as appropriate
- how_introduced: source of discovery
- next_action: Kay's chosen approach

### Step 8: Trigger Meeting Brief
When Kay schedules a coffee chat, meeting-brief-manager generates prep automatically.
</workflow>

<finder_fee_program>
## Finder's Fee Program

**Template:** MANAGER DOCUMENTS / LEGAL / CONTRACTS (existing template on Drive — needs Andy Lock review before use)

**Structure (TBD — needs Kay's decision):**
- Fee amount: $_____ per qualified introduction leading to signed LOI (or NDA?)
- Simple 1-page agreement
- Tracked in Attio on the river guide's People record
- Formalize only with high-value, repeat river guides (not every coffee chat)

**Open questions for Kay:**
1. What fee amount? ($5K? $10K? Percentage?)
2. Trigger event — signed LOI or signed NDA?
3. Start offering immediately or wait until first organic referral proves the relationship?
4. Andy Lock review timeline?
</finder_fee_program>

<integrations>
## Integration Points

| Skill | Integration |
|-------|------------|
| **niche-intelligence** | Provides niche context, association data, industry dynamics |
| **warm-intro-finder** | Checks Kay's network for paths to identified targets |
| **meeting-brief-manager** | Generates prep for coffee chats with river guides |
| **relationship-manager** | Tracks nurture cadence after first contact |
| **intermediary-manager** | When a river guide surfaces a deal, it enters the intermediary pipeline |
| **outreach-manager** | Initial outreach to new river guide targets (via Kay Email channel) |
| **Attio** | Uses existing intermediary pipeline for tracking. relationship_type: "River Guide" |
</integrations>

<schedule>
## Run Schedule

**Trigger:** Manual invocation or when a new niche enters Active-Outreach on the tracker.

**Cadence:** Run ecosystem research when:
1. New niche activated — full 5-category research
2. Monthly refresh — check for new association leadership, new firms, new contacts
3. Post-conference — mine attendee lists for river guide candidates
4. Post-coffee-chat — if a river guide introduces new contacts, add them

**Output location:** `brain/context/river-guide-menu-{date}.md`
</schedule>

<success_criteria>
## Success Criteria

- [ ] All active niches have contacts in at least 3 of 5 categories
- [ ] Each contact scored on the 3-dimension framework
- [ ] Warm intro paths checked for all priority targets (score 7+)
- [ ] Coffee chat menu produced with ranked targets
- [ ] New contacts entered in Attio intermediary pipeline as "Identified"
- [ ] No duplicate contacts (verified against Attio before creating)
- [ ] Finder's fee template referenced (not recreated)
</success_criteria>
