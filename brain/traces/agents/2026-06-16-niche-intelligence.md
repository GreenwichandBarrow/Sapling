---
schema_version: 1.0.0
date: 2026-06-16
task: Tuesday headless niche-intelligence run
agents: [niche-intel-recent, niche-intel-historical, niche-intel-synthesizer, niche-intel-identifier, niche-intel-onepager, niche-intel-scorer, niche-intel-tracker]
status: completed
linked_trace: brain/outputs/2026-06-16-niche-intelligence-report.md
---

# Agent Chatroom: Niche Intelligence

## Coordination Log

## [orchestrator] — 2026-06-16T22:30:00-04:00
Headless Codex/systemd Tuesday run started. Credentials resolved through `scripts/op-env.sh`; `gog auth list --check` passed for `kay.s@greenwichandbarrow.com`.

Pipeline order for this run follows the systemd prompt: RECENT + HISTORICAL gather, synthesizer, identifier, one-pagers, industry scorecards, tracker update, final report, JSON sidecar.
→ READY

---
## [niche-intel-onepager] — 2026-06-16T22:48:35-04:00

Niche: Sign and Lighting Maintenance Programs for Multi-Location Commercial Brands

Local artifact:
- `/tmp/sign-and-lighting-maintenance-programs-onepager.pptx`

Drive folder:
- ID: `1JmJ14tmXrwIDRH8Hi-CeabitLlBEVR8v`
- Link: https://drive.google.com/drive/folders/1JmJ14tmXrwIDRH8Hi-CeabitLlBEVR8v

Uploaded file:
- ID: `1DaHJUvtzrJZyUswbQhkTD1lNZf7HQWH8`
- Name: `Sign and Lighting Maintenance Programs for Multi-Location Commercial Brands June 2026.pptx`
- Link: https://docs.google.com/presentation/d/1DaHJUvtzrJZyUswbQhkTD1lNZf7HQWH8/edit?usp=drivesdk&ouid=108110832334532716154&rtpof=true&sd=true

Key sources:
- Chatroom identifier/synthesizer block: `/home/ubuntu/projects/Sapling/brain/traces/agents/2026-06-16-niche-intelligence.md`
- IBISWorld Billboard & Sign Manufacturing: https://www.ibisworld.com/united-states/industry/billboard-sign-manufacturing/902/
- IBISWorld market size FAQ: https://www.ibisworld.com/united-states/market-size/billboard-sign-manufacturing/902/
- International Sign Association: https://signs.org/
- SICCODE SIC 3993: https://siccode.com/sic-code/3993/signs-advertising-specialties
- PSCO maintenance: https://www.pscosigngroup.com/maintenance/
- Shamrock Signs: https://www.shamrocksigns.net/
- National Sign Co. maintenance: https://nationalsignco.com/sign-solutions/sign-maintenance-service-company/
- Carolina Signs: https://carolinasignsnc.com/
- Florida Lighting Maintenance contracts: https://floridalightingmaintenance.com/led-lighting-products-and-maintenance-in-florida/
- TM Capital / MC Sign: https://www.tmcapital.com/transactions/mc-sign-acquired-by-caltius-equity-partners/
- TM Capital MC Sign press release: https://www.tmcapital.com/tm-capital-advises-mc-sign-company-in-sale-to-caltius-equity-partners/
- Caltius MC Sign sale: https://www.caltius.com/equity-partners/news/caltius-equity-partners-completes-sale-of-mc-sign/
- Vestar / Stratus: https://www.vestarcapital.com/vestar-capital-partners-acquires-stratus-a-global-leader-in-brand-implementation-and-facilities-services-from-arcapita/
- Exeter / Persona-Triangle: https://exeterstreetcapital.com/exeter-image-holdings-announces-second-platform-acquisition-with-recapitalization-of-persona-signs/
- Federal Heath sale: https://federalheath.com/company/news-insights/diane-hendricks-chairperson-of-diane-m-hendricks-enterprises-inc-announced-the-sale-of-federal-heath-sign-company-llc-to-federal-heath-holdings-limited-t
- Stratus / Priority: https://stratusunlimited.com/resources/blog/stratus-acquires-priority-llc-formerly-priority-sign/

Verification:
- Cloned local template `brain/library/internal/one-pager-template/customs-bonds-template.pptx`.
- Final deck has 2 slides: one-pager plus Sources slide.
- First slide preserves the template's 6 shapes.
- Assessment/Status says `Pending Scoring`; no score added.
- Drive folder contains one uploaded one-pager.

→ READY

---
## [niche-intel-synthesizer] — 2026-06-16T23:42:00-04:00

### 1. Cross-Source Signal Matrix.

| Niche/Industry | RECENT Sources | HISTORICAL Sources | Total Source Count | Strength | Tracker/Lifecycle Read |
|---------------|----------------|-------------------|-------------------|----------|------------------------|
| Premium / specialty pest management | web, newsletter, granola, gmail, vault | calls/tracker context via prior pest work | 5+ | VERY STRONG | ACTIVE/WEEKLY REVIEW duplicate: reinforce `Premium Pest Management`; do not create generic pest row. Specialty/premium wedge only. |
| Fine-art logistics / art services infrastructure | web, granola, vault | calls, tracker | 4 | VERY STRONG | ACTIVE duplicate. Keep services-only vs storage-heavy split; storage has capital/insurance constraints. |
| HNW / fine-art / specialty insurance brokerage | web, granola, gmail, vault | calls, email, tracker | 5+ | VERY STRONG | ACTIVE duplicate across Specialty Insurance, HNW Personal Lines, trade-credit/customs/cargo, surplus-lines, FMO/IMO. Do not revive broad insurance brokerage. |
| HOA / community association management | web, newsletter/conference, vault | tracker | 3 | STRONG | ACTIVE duplicate. New evidence raises PE-heat caution; warm sourcing matters. |
| Building energy & emissions compliance / LL97 | web, vault | tracker / prior RE-services work | 3 | STRONG | ACTIVE duplicate. 2026 NYC deadlines strengthen timing; no new row. |
| Facilities management / commercial building services / high-end cleaning | gmail metadata, web, vault | email, calls, tracker | 4 | VERY STRONG | ACTIVE duplicate. Reinforces existing High-End Commercial Cleaning and Facilities Management rows; broker visibility rising. |
| Truck licensing & compliance services | gmail/deal flow | email, tracker | 2 | STRONG | ACTIVE duplicate. Still single-deal-origin caveat despite recurring filing logic. |
| Fire protection / life-safety inspection/compliance | vault/tracker context | calls, tracker | 2 | STRONG | ACTIVE duplicate. Historical evidence supports fire-protection core, not necessarily EV-garage wedge. |
| NY Metro multi-location auto repair succession | gmail weak repeat signal, vault | tracker | 2 | STRONG | ACTIVE duplicate. Respect 2026-06-10 correction; do not morph into tire/fleet without Kay approval. |
| Property tax appeal services | web | tracker | 2 | STRONG | ACTIVE duplicate. Seasonal/regulatory reinforcement, no named company signal. |
| Commercial sign manufacturing + maintenance / lighting service | none | email | 1 quantitative | MODERATE | Potential overlooked adjacency to Commercial Equipment Maintenance / Facilities; needs maintenance revenue mix proof. |
| Heat-transfer / resort-apparel customization manufacturing | none | calls | 1.5 | MODERATE | Warm one-off deal lead, not a niche yet; investor fit questioned. |
| Healthcare environment-of-care compliance SaaS | none | email | 1 quantitative | MODERATE | Caution: SaaS/healthcare software retired/tabled-style risk; only viable if reframed as compliance infrastructure. |
| Structural engineering / inspection / code-violation consulting | none | email / tracker adjacency | 1.5 | MODERATE | Reinforces Reserve Study / Building Engineering / FISP; specific E&K company too small. |
| Specialty coffee equipment service | none | calls, tracker | 2 | STRONG | TABLED. Only revisit if outsourcing density and contract-quality questions are resolved. |
| Art advisory + collection management / appraisal services | none | calls, tracker | 2 | STRONG | TABLED/caution. Pure advisory structurally weak; services/appraisal angle only. |
| Aerospace / defense opportunity | vault recent calls | calls, tracker | 2 | STRONG | KILLED/DEAD for niche-pipeline purposes despite active-row artifact; treat as decline/live-deal exception. |
| Warranty/insurance-funded residential services | granola | none | 1 qualitative | WEAK | Watch item only; residential/single-source. |
| Medical-grade HBOT with insurance contracts | gmail | none | 1 quantitative | MODERATE | Off-buy-box healthcare/provider; do not advance absent second source. |
| Managed cybersecurity compliance / cyber software | gmail | none | 1 qualitative | WEAK | No-proceed: software/product-led, no G&B edge. |
| Dairy equipment sales & service | none | email | 1 quantitative | MODERATE | Pattern evidence for specialized equipment service, not actionable without right-to-win. |

### 2. Named Company Registry with outreach routing flags. Avoid unsafe secret-file reads; if Attio API credentials are unavailable, use vault/tracker/Gmail evidence and state the gap.

Attio gap: I did not read secret files and did not run the Attio API because credentials were not safely available in this subagent context. Routing flags below use chatroom evidence plus vault cross-reference (`brain/entities`, `brain/calls`, `brain/outputs`, `brain/inbox`). Before any outreach, run a proper Attio check through the approved credential path.

| Company Name | Niche | Source(s) | Independence / Size Read | Outreach Flag | Warm Contact | Notes |
|-------------|-------|-----------|--------------------------|---------------|--------------|-------|
| Total Extermination | Premium pest | recent granola/gmail/vault | Independent/live inbound lead | ACTIVE_DEAL | Juan Restrepo; David mutual friend; Camilla/DealsX | Vault entity/call exists. Do not add to cold outreach. |
| Romex Pest Control | Pest comp | recent web | Acquired by Rollins; top-40 PCT 100, 200+ employees | COMP_ONLY | none | Comp for market heat, not target. |
| Guardian Pest Control / Modern Pest Services / Anticimex | Pest comp | recent web | Guardian acquired by Modern/Anticimex | COMP_ONLY | none | Comp for PE/strategic consolidation. |
| EcoShield | Pest comp/caution | recent calls/vault | Large pest company; possible MLM-style sales model to verify | VAULT_HISTORY | Harrison Wells / Camilla context | Use as business-model caution, not target. |
| Cadogan Tate | Fine-art logistics | recent/historical/vault | Large/acquired comp | COMP_ONLY / VAULT_HISTORY | art network | Existing comp; not cold target. |
| Crozier | Fine-art logistics | recent/historical/vault | Iron Mountain/large comp | COMP_ONLY / VAULT_HISTORY | art network | Service degradation comp; not target. |
| DIETL | Fine-art logistics | recent | Unknown from chatroom | NEW_TARGET_PENDING_ATTIO | art network possible | Requires Attio/vault deeper check before outreach. |
| Rock-It Company | Fine-art logistics | recent | Unknown from chatroom | NEW_TARGET_PENDING_ATTIO | art network possible | Requires target validation. |
| Atelier4 | Fine-art logistics | recent/vault | Prior outreach evidence in vault | VAULT_HISTORY | prior art-logistics outreach | Do not cold-add without reviewing prior context. |
| ArtBox Logistics | Fine-art logistics | recent | Unknown from chatroom | NEW_TARGET_PENDING_ATTIO | art network possible | Requires target validation. |
| Acumen International / Acumen Fine Art Logistics | Fine-art logistics/storage | historical/vault | Prior engaged deal; LOI history | ACTIVE_DEAL / VAULT_HISTORY | Levi Phelps | Do not cold outreach. Rich diligence comp. |
| UOVO | Fine-art logistics/storage | historical/vault | Large/PE-style comp | COMP_ONLY / WARM_INTRO | Alexandra Kelly via Margot Romano | Warm network/comp, not cold target. |
| Maquette Fine Art Services | Fine-art logistics | historical/vault | Prior outreach/list evidence | VAULT_HISTORY | prior outreach contact | Check history before any re-engagement. |
| Safe Art Transport | Fine-art logistics | historical/vault | Specialty comp | VAULT_HISTORY | Levi/Acumen context | Comp/possible target; needs Attio check. |
| Art Crating | Fine-art logistics | historical/vault | Specialty comp | VAULT_HISTORY | Levi/Acumen context | Comp/possible target; needs Attio check. |
| Voxme | Art-logistics vertical software | historical/vault | Software vendor used by Acumen | VAULT_HISTORY / COMP_ONLY | Levi Phelps | Potential software comp, not current outreach target. |
| Brown & Brown | Insurance | recent/vault | Public/large broker | COMP_ONLY | none | Not target. |
| Accession Risk Management | Insurance | recent | Unknown from chatroom | NEW_TARGET_PENDING_ATTIO | possible insurance network | Validate sub-niche and ownership. |
| Sterling Risk Insurance | Insurance | recent | Unknown from chatroom | NEW_TARGET_PENDING_ATTIO | possible insurance network | Validate against HNW/art fit and Attio. |
| ASZ International | Insurance | recent | Unknown from chatroom | NEW_TARGET_PENDING_ATTIO | possible insurance network | Validate ownership/sub-niche. |
| Agent Brokers United | Insurance FMO/IMO | recent | Unknown from chatroom | NEW_TARGET_PENDING_ATTIO | possible insurance network | Existing active niche duplicate; validate. |
| Trade Risk Group | Trade credit/customs/cargo insurance | historical/vault | May be Acrisure partner/PE-affiliated per vault | VAULT_HISTORY / WARM_INTRO | Jeremy Black | Do not cold-add; verify ownership and use Jeremy context. |
| Trade Acceptance Group | Trade credit/customs/cargo insurance | historical/vault | Specialist target; owner unknown | WARM_INTRO / VAULT_HISTORY | Jeremy Black used TAG | Best routed via Jeremy, not cold. |
| Allianz Trade / Euler Hermes | Trade credit carrier | historical/vault | Global carrier/public-scale | COMP_ONLY | none | Carrier/reference only. |
| Atradius | Trade credit carrier | historical/vault | Global carrier | COMP_ONLY | none | Carrier/reference only. |
| Coface | Trade credit carrier | historical/vault | Public/global carrier | COMP_ONLY | none | Carrier/reference only. |
| Texel / Meridian | Trade credit/cargo insurance | historical | Likely larger/acquired or carrier/broker comp | COMP_ONLY_PENDING_CHECK | Jeremy Black | Reference/source validation. |
| FirstService Residential | HOA | recent | Large consolidator | COMP_ONLY | CAI/Guillermo network | Market comp, not target. |
| Associa | HOA | recent | Large consolidator | COMP_ONLY | CAI/Guillermo network | Market comp, not target. |
| Pioneer HOA | HOA | recent | Unknown independent status | NEW_TARGET_PENDING_ATTIO | CAI/Guillermo network possible | Validate geography/ownership. |
| RealManage | HOA | recent | Large platform | COMP_ONLY | CAI/Guillermo network | Not target. |
| Community Association Management | HOA | recent | Generic/name ambiguous | NEW_TARGET_PENDING_ATTIO | CAI/Guillermo network possible | Needs disambiguation. |
| IntelliGreen Partners | Building energy/LL97 | recent | Unknown | NEW_TARGET_PENDING_ATTIO | RE-services network possible | Validate target status. |
| NYC Accelerator / NYC DOB | LL97 ecosystem | recent web | Public/non-target orgs | COMP_ONLY / SOURCE_ONLY | none | Source/river-guide context, not target. |
| Reserve Advisors | Reserve studies/building engineering | recent | Larger specialist comp | COMP_ONLY_PENDING_CHECK | RE-services network possible | Active-row comp; validate before target list use. |
| Milrose | Permit expediting / compliance | recent | Known sector platform | COMP_ONLY | RE-services network possible | Comp, likely too large/platform. |
| Conservice / RealPage / Metergy | Submetering/utility billing | recent | Large platforms | COMP_ONLY | none | Market comps, not targets. |
| RE BackOffice | Lease admin/back office | recent | Named comp | NEW_TARGET_PENDING_ATTIO | RE-services network possible | Validate scale/ownership. |
| M Wheat Air | HVAC/government preferred contractor | recent deal flow | Deal-flow company; not auto-repair | NEW_TARGET_PENDING_ATTIO | SMB Deal Hunter/Helen Guo | Do not merge into auto repair. |
| Love Unlimited NY | Heat-transfer/resort apparel | historical/vault | ~$3.2M-$3.5M revenue, ~30% profitability | WARM_INTRO / VAULT_HISTORY | Tom and Jennifer Perino; Jeremy Black | Opportunistic warm deal; not thesis yet. |
| Schwartzman & Associates | Art advisory/appraisal/services | historical | Possibly small (~4 people) | WARM_INTRO_PENDING_ATTIO | Margot Romano / BofA Art Services | Only services/appraisal angle; pure advisory tabled. |
| E&K healthcare/regulatory compliance SaaS target | Healthcare compliance SaaS | historical email | ~$700K revenue; 1,500+ facilities; too small/software | BROKER_DEAL_CAUTION | Everingham & Kerr | Do not advance as G&B niche without reframing. |
| E&K structural engineering/inspection firm | Structural engineering/code violation | historical email | ~$200K revenue / ~$100K cash flow; too small | BROKER_DEAL_CAUTION | Everingham & Kerr | Category validation only. |
| SMB Deal Hunter facility-maintenance contractor | Facilities | historical email | ~$4.5M revenue / ~$838K EBITDA | BROKER_DEAL_PENDING_ATTIO | Helen Guo | Validates category; broker-visible. |
| SMB Deal Hunter truck licensing platform | Truck licensing/compliance | historical email | ~$1.039M revenue / ~$412K EBITDA | BROKER_DEAL_PENDING_ATTIO | Helen Guo | Existing row support; thin-pool caveat remains. |
| SMB Deal Hunter commercial sign company | Commercial sign/lighting maintenance | historical email | ~$4.364M revenue / ~$661K EBITDA | NEW_TARGET_PENDING_ATTIO | Helen Guo | Most interesting overlooked deal-flow adjacency. |
| SMB Deal Hunter dairy equipment service company | Specialized equipment service | historical email | ~$443K EBITDA | BROKER_DEAL_CAUTION | Helen Guo | Pattern evidence, weak G&B edge. |
| Medical-grade HBOT provider | Healthcare/provider | recent gmail | $754,850 revenue / $369,451 profit | OFF_BUY_BOX | Business Exits | Watch only; not outreach. |

### 3. Contact-to-Niche Map.

| Contact | Relationship Warmth | Niches They Can Help With | What to Ask Them | Last Contact |
|---------|---------------------|--------------------------|------------------|--------------|
| Juan Restrepo | WARM | Premium pest / Total Extermination | Qualify owner interest, revenue mix, commercial/luxury exposure, recurring contracts | Callback attempt 2026-06-15 |
| David mutual friend | WARM | Premium pest | Intro/context for Juan and Total Extermination | Mentioned in Total Extermination vault note |
| Jay Davis | HOT/WARM | Pest, specialty pest wedges | Pressure-test premium/specialty pest target types and valuation | Recent Granola call within 14 days |
| Camilla de Sanna | HOT | Pest strategy, aerospace-defense lifecycle, owner-succession framing | Keep pest wedge disciplined; confirm aerospace decline status | Multiple calls through 2026-06 |
| Warren Chan / Anacapa | HOT/WARM | Fine-art logistics, art services, fine-art insurance | Identify experienced insurance operators and targetable art-services businesses | Recent Granola call |
| Margot Romano / BofA Art Services | WARM | HNW/fine-art insurance, art advisory, collection management, UOVO intro path | Ask for service/appraisal operators, not pure advisory; validate Schwartzman | 2026-04-04 historical call context |
| Alexandra Kelly / UOVO | WARM via Margot | Fine-art logistics/storage | Comp/market diligence; service degradation and storage constraints | Prior Margot intro |
| Levi Phelps / Acumen | HOT/WARM | Fine-art logistics/storage, customs brokerage, Voxme/software | Use diligence learnings; possible river guide for services-only art logistics | 2025 Acumen calls/LOI history |
| Jeremy Black | HOT/WARM | Trade credit/customs/cargo insurance, Love Unlimited, specialty insurance | Ask for TAG/TRG principal intro; pressure-test repeatable target pool; Love deal status | 2026-02 historical thread/call |
| Kay's brother in marine logistics | WARM | Cargo/customs/trade credit insurance | Validate marine-logistics buyer pain and broker referral channels | Mentioned in Jeremy thread |
| August Felker | WARM | HNW personal lines / fine-art insurance | Revisit investor objections, operator profile, target economics | 2025-11-19 call |
| Anna Raginskaya / Morgan Stanley | WARM/COOL | Art insurance, HNW network | Potential insurance/art services intro path | Historical intro thread |
| Ryan LaMay | WARM/COOL | Business insurance | Insurance-market diligence and intros | Historical thread |
| Richard Augustine | COOL | HNW/specialty insurance | Specialist perspective via August path | Referenced by August |
| Guillermo Lavergne | HOT | HOA/CAI network, specialty coffee caution | Use CAI access for HOA warm sourcing; only revive coffee with density proof | Recent investor cadence / historical calls |
| Jeff Stevens | HOT | Aerospace-defense rejection, specialty coffee challenge, art services pressure-test | Validate kill/tabled decisions and investor fit | 2026-05/06 calls |
| Erika Teresko | WARM | Aerospace-defense referral/lifecycle | Confirm no further action if declined | 2026-05-28 call |
| Helen Guo / SMB Deal Hunter | COOL/WARM | Truck licensing, commercial sign maintenance, facilities, dairy equipment | Request details only where niche has second-source potential; avoid broad broker-chasing | May 2026 deal emails |
| Andrew Lowis / Axial | COOL/WARM | Commercial cleaning/facilities, commercial property management, deal-flow comps | Retrieve unavailable deal bodies if useful; treat as broker-visible comp channel | Recent deal-flow metadata |
| Everingham & Kerr | COOL/WARM | Healthcare compliance SaaS, structural engineering | No immediate ask unless category is revived; deals are small/cautionary | Historical deal emails |
| Dino Beslic | WARM/COOL | Fire sprinkler/fire protection | Use for association/source map if fire-protection row advances | 2025-10-21 call |
| Harrison Wells | HOT | Search strategy, fire-protection brainstorm, pest business-model caution | Pressure-test whether signals warrant action vs research | 2025-10 / 2026-06 calls |
| Tom and Jennifer Perino | WARM | Love Unlimited / heat-transfer resort apparel | Deal-specific owner diligence, not thesis sourcing | 2026-01-18 call |

### 4. Lead Lifecycle Tracker.

| Niche/Strategy | Proposed By | When | Challenged By | When | Reason | Status |
|---------------|-------------|------|---------------|------|--------|--------|
| Generic pest management | Multiple recent sources / market | 2026-06 | Jay Davis, Camilla/Kay strategy, tracker caution | 2026-06 | Too liquid/crowded; strategics and PE active; broad pest not differentiated | KILLED as generic; LIVE only as premium/specialty wedge |
| Premium pest for luxury hospitality/commercial properties | Camilla/Kay, Jay Davis, DealsX/Juan | 2026-06 | Market M&A caution | 2026-06 | Need first target around ~$500K EBITDA and specialty/premium proof | LIVE / ACTIVE |
| Fine-art storage-heavy model | Art network / Acumen diligence | 2025-2026 | Investors/learnings, Acumen diligence | 2025-2026 | Balance-sheet/capex/insurance constraints; storage revenue not enough | TABLED/CAUTION |
| Fine-art logistics services-only | Warren Chan, Acumen/Margot context | 2025-2026 | Capital intensity caution | 2026 | Attractive if asset-light services/installation/crating/logistics, not warehouse-first | LIVE / ACTIVE |
| Broad insurance brokerage | Multiple sources | 2026 | Tracker cautions / investor feedback | 2026 | Too broad, M&A crowded, needs sub-niche | KILLED as broad; sub-niches LIVE |
| HNW personal lines / fine-art insurance | August Felker, Jeremy Black, Warren/Margot network | 2025-2026 | August/investor feedback | 2025-2026 | Multiples, QSBS, operator experience; still sticky/renewal-rich | LIVE / ACTIVE |
| Trade credit/customs/cargo insurance brokerage | Jeremy Black | 2026-02 | Target-pool uncertainty | 2026 | Recurring and compelling but must find agency with sufficient numbers | LIVE / ACTIVE |
| HOA/community association management | RE-services run / Guillermo CAI edge | 2026-06 | Recent PE heat | 2026-06 | Attractive score but off-market sourcing required | LIVE / ACTIVE |
| Building energy & emissions compliance / LL97 | RE-services run / recent web | 2026-06 | None material | 2026-06 | Strong regulatory deadlines; already active | LIVE / ACTIVE |
| Specialty coffee equipment service | Guillermo/Jeff/Carlos discussions | 2026-04/05 | Guillermo, Jeff | 2026-04/06 | Need proof outsourced service density and contract quality; mom-and-pop ceiling risk | TABLED |
| Pure art advisory | Margot/Kay art network | 2026-04 | Margot Romano / Jeff pressure-test | 2026-04 | Banks provide advisory free; weak regulatory moat; variable fees | TABLED/KILLED as pure advisory |
| Collection management / appraisal / art services | Margot / tracker ideation | 2026-04/06 | Pure advisory concerns | 2026 | Viable only with defensible service/valuation/appraisal layer | TABLED / WATCH |
| Aerospace/defense | XPX/corporate-advisor referral via Camilla/Erika | 2026-04/05 | Jeff/Camilla/Kay | 2026-05/06 | Fails buy-box/investor-funding fit despite woman-owned transition angle | DEAD/KILLED for niche pipeline |
| Heat-transfer/resort apparel customization | Tom/Jennifer; Jeremy Black | 2026-01/02 | Jeremy Black | 2026-02 | Attractive profitability/right-to-win, but weak contracted recurring revenue and limited growth | LIVE as opportunistic deal; not niche |
| Healthcare/regulatory compliance SaaS | Everingham & Kerr | 2026-03/05 | Tracker software caution / buy-box learnings | 2026 | Small, SaaS/product-led, healthcare software de-emphasized | TABLED/CAUTION |
| Commercial sign manufacturing + maintenance | SMB Deal Hunter | 2026-05 | No direct challenge yet | 2026-06 | Needs proof maintenance/lighting recurring layer dominates fabrication | LIVE as watchlist candidate |
| Dairy equipment sales/service | SMB Deal Hunter | 2026-05 | Right-to-win screen | 2026-06 | Geography/agriculture exposure; no G&B edge | DEAD unless more sources emerge |
| HBOT provider | Business Exits | 2026-06 | Buy-box screen | 2026-06 | Healthcare provider/off-buy-box, small | DEAD/WATCH only |
| Cybersecurity software | E&K | 2026-06 | Buy-box screen | 2026-06 | Software/product-led, no services/owner-succession edge | DEAD |

### 5. Convergence Report ranked top 3-5 signals.

| Rank | Signal | Why It Ranks | Action for Identifier |
|------|--------|--------------|-----------------------|
| 1 | Premium / specialty pest management | Most current operating momentum: live inbound Total Extermination lead, recent calls, association/newsletter signal, and explicit G&B wedge refinement. Exit market is liquid but broad-pest price risk is real. | Do not identify as new. Recommend reinforced active priority with specialty/premium target filters and no generic pest row. |
| 2 | Fine-art logistics services-only / art services infrastructure | Strongest G&B right-to-win plus multiple historical and recent sources. However, learnings are clear that storage-heavy models are capital-intensive and structurally weaker. | Treat as active-row refinement: prioritize asset-light logistics/install/crating/services, not warehouse/storage-first. |
| 3 | Specialty insurance sub-niches: HNW/fine-art and trade credit/customs/cargo | Very strong source convergence, recurring revenue, renewal stickiness, clear exit path, and warm contacts. Broad insurance is too crowded, but sub-niches remain live. | Reinforce existing rows; route target discovery through Jeremy/August/Margot/Warren, not generic cold insurance outreach. |
| 4 | HOA/community association management + LL97/building compliance | Both have strong RE-services scores and fresh regulatory/market validation. HOA has CAI/Guillermo access but rising PE heat; LL97 has immediate 2026 deadline pressure. | Keep both active; prioritize warm river-guide sourcing over broad list build. |
| 5 | Commercial sign manufacturing + maintenance / lighting service | Best overlooked moderate signal: quantitative broker deal with recurring maintenance/lighting layer, adjacent to facilities/commercial equipment maintenance, but only one source. | Consider as a watchlist/identifier candidate only if a second source confirms recurring maintenance economics and target pool. |

→ READY

---
## [niche-intel-recent] — 2026-06-16T22:45:00-04:00
**Source:** RECENT intelligence sweep, last 14 days ending 2026-06-16
**Status:** complete_with_source_gaps

### Sources Covered
- Web/social: ran `last30days` for the three required general queries plus sampled active-niche queries for pest, HOA, fine-art logistics, and fire/life-safety; supplemented with current web search for pest M&A, HOA/community-association management, fine-art logistics, facilities services, specialty insurance, LL97/building energy compliance, property-tax appeal, and truck licensing/IFTA/IRP.
- Newsletters: Gmail read-only searches with `--gmail-no-send` for `label:"auto/subscriptions & education" newer_than:7d` and `label:"auto/industry research" newer_than:14d`; selected messages read for Acquiring Minds, PE Hub, NPMA, NYPMA, Amboy Street, SMBootcamp, and XPX.
- Granola calls: `~/.local/bin/granola-api since 2026-06-02T04:00:00Z`, with selected notes pulled for Jay Davis, Warren Chan, Camilla/Kay pest strategy, Acquiring Minds franchising webinar, Sam/DealsX strategy reset, and Mind Your Business & Legacy.
- Gmail deal flow: read-only searches with `--gmail-no-send` for `label:"auto/deal flow" newer_than:14d` and `label:"auto/investors" newer_than:14d`; selected messages read for DealsX leads, Business Exits, E&K, Axial, SMB Deal Hunter, Transworld, QuietLight, and investor-art/pest threads.
- Vault research: scanned `brain/outputs/` and `brain/calls/` files from 2026-06-02 through 2026-06-16, including the 2026-06-09 niche-intelligence report, HOA report, RE-services report, Jay Davis, Warren Chan, Laura/Randi lunch, Total Extermination, and Camilla/Kay pest syncs.
- Passive signals: checked `brain/inbox/` for created-or-tagged `niche-signal` items since 2026-06-09; none found.

### Missing Sources
- `last30days` was degraded: Reddit public search returned 403 for every query; HN and Polymarket returned 0 usable items; X/Twitter and YouTube were unavailable per tool output. Treat social signal as no-data, not negative evidence.
- Supplemental web was broad but not exhaustive across all 25+ active niches; coverage focused on active signals and high-probability tracked niches rather than every row equally.
- Some Gmail message bodies were body-empty through `gog gmail get` despite search metadata showing relevant Axial subjects (`Commercial Property Management`, `Institutional commercial facility services provider`). Marked as limited-read evidence.
- No passive `brain/inbox/*niche-signal*` files found since last Tuesday.

### Signals Found
- **Premium / specialty pest management - strong existing-row reinforcement.** Four independent recent channels converged: Jay Davis call, Camilla/Kay internal strategy sessions, NPMA/NYPMA newsletters, and DealsX inbound. Jay's read was that broad pest is too liquid and expensive for a searcher, but bird control, rat-only, aquatic weed management, mosquito control, and white-glove/premium wedges can sit below major-platform pricing. Camilla/Kay narrowed the live thesis toward premium, discreet pest for luxury retail/hospitality, with a roughly $500K EBITDA first target and possible municipal-contract upside. NPMA newsletter reinforced bed-bug recurring-service model and allergen/bed-bug specialization. DealsX surfaced Juan Restrepo / Total Extermination as an interested lead, followed by a 2026-06-15 callback attempt.
- **Pest M&A caution - do not overgeneralize.** Web search showed fresh pest consolidation evidence: Rollins acquired Romex Pest Control in April 2026; CT Acquisitions and Main Street Wealth both frame 2026 pest as active PE/strategic roll-up territory; PCT/Facebook surfaced Guardian Pest Control to Modern Pest Services / Anticimex within the last week. This validates exit-channel liquidity but raises entry-price risk. Best lifecycle position remains specialty/premium wedge, not generic pest platform.
- **Fine-art logistics / art services - strong existing-row reinforcement, possible re-scope caution.** Warren Chan / Anacapa call validated that art storage, transport, installation, crating, and international shipping remain the cleanest art-world operating-services fit; fine-art insurance remains second priority with two experienced insurance operators available. Web search reinforces market size: Dimension Market Research estimates global fine-art logistics at ~$2.47B in 2026 and ~$4.65B by 2035, with U.S. at ~$752.6M in 2026 and ~$1.37B by 2035; Business Research Insights gives a higher 2026 global estimate of ~$4.06B and 4.7% CAGR to 2035. Recent web/social found Instagram activity from Atelier4/ArtBox but no meaningful last30days social evidence. Duplicate caution: this is already in WEEKLY REVIEW as Fine-Art Logistics Services and overlaps the older Storage & Related Services for HVA row; do not double-count storage-heavy and services-only versions.
- **Specialty insurance / HNW and art/collectibles insurance - reinforcing, but M&A crowded.** Warren call kept fine-art insurance alive as a target-dependent thread. PwC's 2026 insurance deals outlook reports $29.6B announced insurance deal value across 191 disclosed transactions for Dec. 1, 2025 to May 31, 2026. MarshBerry says specialty intermediary M&A surged in Q1 2026. Fortune Business Insights projects specialty insurance from $126.15B in 2026 to $337.89B by 2034 at 13.10% CAGR. Strong demand/exit backdrop, but duplicate caution with existing Specialty Insurance Brokerage, Trade Credit/Cargo, HNW Personal Lines, Surplus Lines, and FMO/IMO rows; any new candidate needs a sub-niche, not "insurance brokerage" broadly.
- **HOA / community-association management - strong validation, but PE heat rising.** 2026-06-03 internal report already scored HOA management 2.45/3. Recent web adds a WSJ Pro item from ~2 weeks ago that PE is acquiring condo managers in a local/fragmented market, plus CINC Systems' 2026 state-of-industry report on a "value, capacity, and trust squeeze" in community association management. CAI 2026 annual conference occurred June 3-5. Signal is still attractive for G&B because of Guillermo/CAI network access, but lifecycle caution increased: rising PE visibility means off-market warm sourcing matters more than broad outreach.
- **Building energy & emissions compliance / LL97 - strong regulatory timing signal.** Recent web reinforces the 2026 filing and penalty window: NYC DOB published the 2026 covered-building list; NYC Accelerator says covered buildings need LL97 compliance help to avoid annual fines; RAN PC lists 2026 deadlines, including May 1 LL97 emissions reporting, June 30 extension request, and Aug. 29 if approved. Energo's June 2026 LL97 article reiterates 25,000+ SF covered-building threshold and stricter 2030 caps. This is already in WEEKLY REVIEW from the 2026-06-03 RE-services run and remains one of the cleaner recent signals.
- **Commercial property tax appeal - seasonal/regulatory but likely service-adjacent, not net-new.** Recent web shows 2026 appeal deadlines and valuation-window pressure in NJ and other states. Brache Eichler, Cole Schotz, and Genova Burns all published 2026 commercial-property tax appeal alerts around filing deadlines; San Mateo has 2026 assessment appeal windows. Validates recurring seasonal demand for the existing Property Tax Appeal Services row; no company-specific acquisition signal found.
- **Facilities management / commercial building services - deal-flow reinforcement.** Gmail deal flow included Axial subjects `Commercial Property Management` and `Institutional commercial facility services provider`; body reads were unavailable, so treat as metadata-only. Facilities Dive's 2026 outlook flags energy efficiency/electrification, AI, security threats, and labor pressure as defining FM trends. NEBFM 2026 listed 240+ companies serving building operation, management, maintenance, and renovation. Existing-row validation, not net-new.
- **NY Metro auto repair succession - repeat signal, but correction caution.** 2026-06-09 run advanced NY Metro Multi-Location Independent Auto Repair Succession at 1.92/3 after correcting a mistaken fleet/tire narrowing. Current Gmail deal flow again includes SMB Deal Hunter subject `semi-absentee tire shop, government-preferred HVAC contractor`, but this should not override the corrected canonical niche. Treat tire/fleet as a separate possible future tangent only with explicit approval.
- **Warranty/insurance-funded residential services - weak potential new adjacency.** Matt Luczyk's 2026-06-02 call surfaced a warranty-driven pipe installation company where insurance companies supply the leads; he offered to share warranty companies and approved service providers. This has G&B fit attributes (insurance-funded demand, lead-source moat) but is currently single-source, residential, and not enough to advance.
- **Medical-grade hyperbaric oxygen therapy with insurance contracts - interesting but off-buy-box.** Business Exits listed a medical-grade HBOT provider with 2025 revenue $754,850, profit $369,451, asking price $1.2M, and 3.2x multiple; contracts with Medicare, Aetna, Anthem BCBS, Cigna, and UnitedHealthcare. Strong reimbursement/contract barrier, but healthcare/provider model and small size make it a watch item, not a G&B niche candidate.
- **Managed cybersecurity compliance / cyber software - weak/no-proceed.** E&K circulated a provider of cybersecurity software focused on near-immediate attack detection, DLP support, firewalls, and EDR. This is software/product-led rather than managed compliance service; no evidence of recurring services, owner succession, or G&B sourcing edge. Do not advance from this alone.
- **Owner succession as a horizontal sourcing lens - strong messaging input, not a niche.** Mind Your Business & Legacy webinar reinforced that owners delay transition because of identity, family, employees, and "next chapter" concerns; privately held businesses account for 99% of U.S. businesses and about half of employees per webinar transcript. Use as owner-conversation framing, not a standalone industry.

### Industries/Companies Mentioned
- Pest: Total Extermination; Juan Restrepo; Rollins; Romex Pest Control; Rentokil/Terminix; Anticimex; Modern Pest Services; Guardian Pest Control; EcoShield; bird control; rat-only pest; mosquito control; aquatic weed management; bed-bug recurring service.
- Art / HVA: Warren Chan; Anacapa Partners; Cadogan Tate; Crozier; DIETL; Rock-It Company; Atelier4; ArtBox Logistics; fine-art insurance operators (unnamed); Bank of America Art Services contact; Art Basel strategy contact.
- Insurance: Brown & Brown; Accession Risk Management; MarshBerry; PwC; Sterling Risk Insurance; ASZ International; Agent Brokers United; specialty insurance; fine-art/collectibles; trade credit/customs/cargo; HNW personal lines; FMO/IMO.
- Real estate services: HOA/community association management; CAI; CINC Systems; FirstService Residential; Associa; Pioneer HOA; RealManage; Community Association Management; Building Energy & Emissions Compliance; NYC Accelerator; NYC DOB; Local Law 97; IntelliGreen Partners; Reserve Advisors; Milrose; Littlejohn; Conservice; RealPage; Metergy; RE BackOffice.
- Facilities / property services: institutional commercial facility services provider (Axial metadata only); commercial property management (Axial metadata only); NEBFM; facilities management; commercial building services; government-preferred HVAC contractor; M Wheat Air.
- Auto / fleet: NY Metro Multi-Location Independent Auto Repair Succession; semi-absentee tire shop; commercial fleet maintenance/tire service as a caution-only tangent.
- Other deal-flow: Business Exits medical-grade hyperbaric oxygen therapy provider; Everingham & Kerr provider of cybersecurity software; Saltwater Fishing Tackle Company; Consumer-Facing Health Information Management App; landscaping/material production; business/institutional catering; manufacturer of cultured marble vanity tops; Transworld Business Advisors NY.

### Data Points for Scoring
- Pest: Total Extermination is a live inbound DealsX lead; Camilla/Kay target profile discussed around ~$500K EBITDA first pest target. Rollins/Romex: Romex is top-40 PCT 100 and 200+ employees. 2026 pest roll-up market described as one of the most active home-services consolidation categories. NPMA newsletter promotes bed-bug recurring-service model.
- Fine-art logistics: Dimension Market Research estimates global fine-art logistics at ~$2.47B in 2026, growing 7.3% CAGR to ~$4.65B by 2035; U.S. market ~$752.6M in 2026 growing 6.9% CAGR to ~$1.37B by 2035. Business Research Insights estimates global fine-art handling/logistics at ~$4.06B in 2026 and ~$6.13B by 2035 at 4.7% CAGR.
- Insurance: PwC reports $29.6B announced deal value across 191 disclosed insurance transactions from 2025-12-01 to 2026-05-31. Fortune Business Insights projects specialty insurance at $126.15B in 2026 and $337.89B by 2034, 13.10% CAGR. PrivSource web result shows ~97 tracked insurance acquisitions in 2026 year-to-date / 213 estimated full-year, but use cautiously as secondary web data.
- HOA: Existing internal score 2.45/3; market ~$54B in 2024 projected ~$73B by 2030; ~365,000 U.S. community associations; ~90% small/regional independents; CAI Long Island and Guillermo edge remain decisive.
- Building energy compliance: existing internal score 2.55/3; NYC covered-building threshold generally 25,000+ SF; DOB published 2026 covered-building list; LL97 emissions-reporting 2026 deadline May 1, extension request by June 30 and possible Aug. 29 extension; prior internal estimate says NYC sub-niche includes ~50,000 buildings.
- Auto repair: existing corrected internal score 1.92/3; target pool likely 100+ NY Metro independents, but buy-box-scale multi-location pool unproven.
- HBOT deal: 2025 revenue $754,850; 2025 profit $369,451; asking price $1,200,000; 3.2x multiple; contracts with Medicare, Aetna, Anthem BCBS, Cigna, UnitedHealthcare.
- Axial printing deal as general ETA signal: commercial printing company $15M-$18M revenue, $2M-$3M EBITDA; 958 recommended buyers, 32 buyer pursuits, 5 PE firms, 11 independent sponsors, 106 days pursuit-to-LOI, 400 days LOI-to-close. Useful deal-process benchmark, not a niche signal.

### Duplicate / Lifecycle Cautions
- Do not resurface generic pest as a new niche. Current live thesis is `Premium Pest Management (Luxury Hospitality & Commercial Properties)` with possible specialty sub-wedges. Broad pest is crowded/liquid; premium/specialty is the actual open question.
- Do not double-count Fine-Art Logistics Services against `Storage & Related Services for High Value Assets`; services-only vs storage-heavy must stay explicit.
- Do not revive broad insurance brokerage. Only sub-niche insurance signals count: art/collectibles, HNW personal lines, trade credit/customs/cargo, surplus lines compliance, or FMO/IMO infrastructure.
- HOA management is already in WEEKLY REVIEW; new evidence should adjust lifecycle/priority and sourcing channel, not create a duplicate row.
- Building Energy & Emissions Compliance, Reserve Study, Submetering, Permit Expediting, and Lease Administration were already scored in the 2026-06-03 RE-services run. Current LL97 evidence reinforces energy compliance only.
- Auto repair correction from 2026-06-10 is binding: do not convert it back into commercial fleet maintenance or tire service without explicit Kay approval.
- HBOT, cybersecurity software, saltwater tackle, health app, catering, cultured marble, landscaping, and digital/media e-commerce deal-flow are one-off/off-buy-box unless another source independently ties them to G&B's recurring services thesis.

→ READY

---
## [niche-intel-historical] — 2026-06-16T23:18:00-04:00
**Source:** historical calls + Gmail + tracker refresh + availability checks
**Status:** partial; calls/Gmail/tracker covered, OneNote and ChatGPT export unavailable in this runtime

### Coverage Notes
- Tracker tabs refreshed live before extraction: WEEKLY REVIEW, IDEATION, KILLED, TABLED. Dedupe respected against current rows, including newer rows not in the prompt such as Luxury residence concierge operators, Private art advisory firms, Collection management consultants, and Commercial Equipment Maintenance.
- `brain/calls/*.md`: 132 call notes present. Read targeted full-context call notes and searched all call notes for niche terms. Fireflies-vault and older Granola notes appear co-mingled in `brain/calls/`; Granola CLI was available but `since 2023-09-01` returned only the latest-page notes, so historical Granola coverage is primarily through synced vault files.
- Gmail: ran the five required historical queries with installed `gog` syntax and `--gmail-no-send`; read selected high-signal threads.
- OneNote: no OneNote MCP/resources were available in this Codex runtime. SEARCH FUND notebook not mined.
- ChatGPT export: `/home/ubuntu/Downloads` does not exist and `selected_business_conversations.json` / `031aafe3*` were not found under `/home/ubuntu`. ChatGPT raw conversations not mined.

### Niche Findings

#### Heat-Transfer / Resort-Apparel Customization Manufacturing
- **Sources:** calls (`2026-01-18 Tom/Jennifer`, `2026-02-02 Jeremy Black`).
- **Key intelligence:** Love Unlimited NY is a narrow B2B apparel-input manufacturer serving beachwear/resort retail, not broad apparel. Reported revenue grew from ~$1.7M in 2010 to ~$3.2M in 2022 / ~$3.5M referenced later; roughly 30% profitability; no losses in 18 years; made-to-order model limits inventory risk; ~30% custom design revenue; strong recurring orders but weak/no formal contracts.
- **People/contacts:** Tom and Jennifer Perino; Jeremy Black as advisor/referral source.
- **Kay sentiment:** Kay found seller transparency, legacy motivation, US-based production, and Chanel/fashion right-to-win compelling. She also acknowledged she had not been looking in apparel broadly.
- **Lifecycle warning:** Jeremy explicitly pressured the investor-fit issue: limited growth and insufficient contracted recurring revenue may make it hard for G&B investors despite attractive margins. Treat as a deal-level opportunistic lead, not a broad thesis unless repeatable target pool and recurring/service layer are proven.
- **Why overlooked:** It does not map neatly to the current luxury/compliance tracker taxonomy; it is a warm one-off operating-company lead inside fashion rather than a scored niche.

#### Trade Credit, Customs Bonds & Cargo Insurance Brokerage
- **Sources:** Gmail (`Jeremy Black — Insurance Contact & Two Insurance Ideas`, Feb 2026), tracker (already WEEKLY REVIEW), calls (`2026-02-02 Jeremy Black` context around specialty insurance).
- **Key intelligence:** Jeremy identified Trade Risk Group for customs bonds/cargo insurance and trade credit insurance as specialized, recurring, under-utilized in the US, and potentially improved by banker/CFO education. Kay replied that the recurring nature and banker/CFO education component were compelling and that she would explore further; Jeremy followed up that he was bullish if an agency with sufficient numbers could be found.
- **People/contacts:** Jeremy Black; Kay's brother in marine logistics mentioned as perspective source; named firms/carriers include Trade Risk Group, Trade Acceptance Group, Texel/Meridian, Euler Hermes/Allianz Trade, Atradius, Coface, Ex-Im.
- **Kay sentiment:** Positive. Explicitly called it an area she was going to explore further.
- **Lifecycle warning:** Already surfaced in WEEKLY REVIEW as "Trade Credit, Customs Bonds & Cargo Insurance Brokerage" with bundled cross-sell rationale. Do not duplicate; use email thread as strong source validation and Kay-sentiment evidence.
- **Why overlooked:** It was initially buried in a relationship email, not a formal deal memo; the tracker now captures it.

#### HNW Personal Lines / Fine-Art Specialty Insurance Brokerage
- **Sources:** calls (`2025-11-19 August Felker`, `2026-02-02 Jeremy Black`, `2026-04-04 Margot Romano`), Gmail (art insurance intro/search threads), tracker (already active/new rows).
- **Key intelligence:** August validated HNW personal lines as sticky and valuable, with near-100% renewal dynamics, but flagged high multiples, QSBS concerns, and operator-experience skepticism. Wealth transfer + climate premium increases are demand tailwinds; PE roll-up service degradation creates an independent-buyer angle. Margot added a geographic-arbitrage idea: buy a Midwest brokerage and open/expand into NY where consolidation is heavy.
- **People/contacts:** August Felker, Margot Romano/BofA Art Services, Anna Raginskaya/Morgan Stanley intro thread, Ryan LaMay business-insurance thread, Richard Augustine referenced by August.
- **Kay sentiment:** High conviction but tempered by investor feedback. She had narrowed a target list from thousands to hundreds to ~30 and had at least one women-run HNW personal-lines target.
- **Lifecycle warning:** Already tracked as Specialty Insurance Brokerage and HNW Personal Lines. New historical value is the Midwest-to-NY acquisition angle and explicit investor objections, not net-new promotion.
- **Why overlooked:** Some strategic detail lives in calls rather than the scorecard row.

#### Art Advisory + Collection Management / Appraisal Services
- **Sources:** calls (`2026-04-04 Margot Romano`, `2026-04-22 Jeff-Kay` search pressure-test), tracker (IDEATION/TABLED).
- **Key intelligence:** Pure art advisory is structurally weak: banks provide advisory free for private-bank clients, independent advisor fee models vary, and there is no regulatory moat. More promising angle is advisory plus defensible services: valuation, appraisal, collection management, or similar. Schwartzman & Associates may be smaller than expected (~4 people) and right-sized for G&B, but likely target-specific.
- **People/contacts:** Margot Romano, Bank of America Art Services, Schwartzman & Associates, Morgan Stanley Blue Rider Team, UBS art team.
- **Kay sentiment:** Interested because of art/luxury right-to-win, but Margot's feedback materially cooled pure advisory.
- **Lifecycle warning:** Pure advisory has been tabled/soft-killed by structural concerns. Only re-surface as an "advisory + services" model or named-target diligence item.
- **Why overlooked:** Current tracker rows separate Private art advisory and Collection management; the historical call shows why those should not be pursued as pure advisory.

#### Fine-Art Logistics / Storage / Art Services Infrastructure
- **Sources:** calls (`2025-10-30 Levi/Acumen`, `2026-02-02 Jeremy Black`, `2026-04-04 Margot Romano`), tracker (already storage/fine-art logistics rows).
- **Key intelligence:** Acumen deep dive confirms sticky storage but also capex/insurance constraints: Poughkeepsie 90-95% full, Queens 16% storage margin, high-value-per-building insurance limits, truck insurance roughly doubled, CA truck regulation risk, art-handler labor is the bottleneck. Customs brokerage has modest margin but drives airport trucking. Corporate/PE roll-ups can degrade service quality, leaving room for mid-sized high-touch operators.
- **People/contacts:** Levi Phelps/Acumen, Jeremy Black, Margot Romano; comps include Crozier, UOVO, Maquette, Safe Art Transport, Art Crating; Voxme noted as vertical software used by Acumen.
- **Kay sentiment:** Strong historical interest, but she has shifted toward asset-light services and operational/AI-efficiency upside rather than capital-heavy storage.
- **Lifecycle warning:** Already tracked. Do not promote storage again without acknowledging the capital intensity and insurance-capacity constraints; services-only scope is the cleaner version.
- **Why overlooked:** Acumen diligence has rich operator data that may not be fully reflected in the current fine-art logistics row.

#### Healthcare / Regulatory Compliance SaaS, Especially Environment-of-Care Automation
- **Sources:** Gmail (`E&K Cloud-Based SaaS Healthcare / Regulatory Compliance Software Company`, Mar-May 2026), tracker (IDEATION retired SaaS / medical credentialing / healthcare compliance adjacent).
- **Key intelligence:** E&K repeatedly circulated a virtual healthcare/regulatory-compliance SaaS company with ~$700K revenue, mostly recurring; serves 1,500+ healthcare facilities; purpose-built for Environment of Care automation, compliance data management, reporting, and patient-care-environment risk reduction. Product also monitors temperature-sensitive assets and is reportedly used for aerospace composite-manufacturing materials.
- **People/contacts:** Everingham & Kerr.
- **Kay sentiment:** No direct Kay sentiment found in read threads.
- **Lifecycle warning:** SaaS category has been retired/treated cautiously because of AI/software risk. This one is small and mostly recurring but likely too small as a standalone and not aligned unless reframed as compliance infrastructure or asset-monitoring service+software.
- **Why overlooked:** It arrived as broker deal flow, not thesis research, and healthcare SaaS is currently de-emphasized.

#### Structural Engineering / Inspection / Code-Violation Consulting
- **Sources:** Gmail (`E&K Full-service Structural Engineering, Inspection & Consulting Firm`, May 2026), calls search overlap with reserve/facade engineering rows.
- **Key intelligence:** NJ structural engineering/inspection/consulting firm, very small at ~$200K revenue / ~$100K normalized cash flow. Services include building structural problems, inspections, review/correction of existing code violations, and structural-deficiency correction for homeowners, business owners, lawyers, realtors, contractors.
- **People/contacts:** Everingham & Kerr.
- **Kay sentiment:** No direct Kay sentiment found.
- **Lifecycle warning:** Too small as a platform. Useful only as corroborating evidence for the broader Reserve Study / Building Engineering / FISP thesis, where target pool and licensed-engineer key-person risk are already known issues.
- **Why overlooked:** Broker blast was below buy-box scale; the signal is category validation, not a target.

#### Commercial Cleaning / Facility Maintenance Services
- **Sources:** Gmail (Axial `Multi-Market Commercial Cleaning Services Provider`, SMB Deal Hunter facility-maintenance contractor), calls (`2026-05-29 Megan Lawlor` channel note, `2026-04-23 XPX panel` AI-proof service-company macro), tracker (already High-End Commercial Cleaning and Facilities Management rows).
- **Key intelligence:** Axial pushed a multi-market commercial cleaning provider to Kay based on criteria; SMB Deal Hunter highlighted a Utah facility-maintenance contractor with national grocery/convenience-chain contracts and ~$4.5M revenue / ~$838K EBITDA. These validate recurring/repeat facilities demand, but also show this lane is broker-visible and not proprietary.
- **People/contacts:** Axial / Andrew Lowis platform relationship; SMB Deal Hunter / Helen Guo.
- **Kay sentiment:** No direct pursuit found for the specific blasts. Strategic interest already exists through tracker rows.
- **Lifecycle warning:** Already tracked. Use as market-confirmation, not new idea. Watch labor-heavy margins and increasing broker/PE visibility.
- **Why overlooked:** Signals came through generic deal flow and could be treated as noise because current tracker already has adjacent rows.

#### Truck Licensing & Compliance Services
- **Sources:** Gmail (SMB Deal Hunter May 26 deal), tracker (already WEEKLY REVIEW).
- **Key intelligence:** CA/remote trucking licensing and compliance services/platform: $1.039M revenue, $412K EBITDA, $1.425M ask, established 2021. Annual filings create natural recurring work; services include federal/state registrations, business formations, drug/alcohol testing programs, truck plates, and driver-qualification documentation. Same-day filing and compliance tracking create a moat versus phone-and-paper shops.
- **People/contacts:** Helen Guo / SMB Deal Hunter.
- **Kay sentiment:** No direct Kay sentiment found in Gmail; current tracker flags this as single-source with thin-pool/network caveat.
- **Lifecycle warning:** Already in WEEKLY REVIEW. Historical email confirms original source and economics but also reinforces single-source nature.
- **Why overlooked:** Newsletter deal format, not a formal niche memo; now captured.

#### Commercial Sign Manufacturing + Maintenance / Lighting Service
- **Sources:** Gmail (SMB Deal Hunter May 26 deal).
- **Key intelligence:** Absentee-run MO commercial sign manufacturer: $4.364M revenue, $661K EBITDA, $2.95M ask, established 1978. Interesting because maintenance and lighting service create a reoccurring layer on top of project-based fabrication; LED retrofit cycle adds multi-year tailwind; approved-vendor-list relationships with multi-location chains could be sticky.
- **People/contacts:** Helen Guo / SMB Deal Hunter.
- **Kay sentiment:** No direct Kay sentiment found.
- **Lifecycle warning:** Not in tracker except possibly adjacent to commercial equipment maintenance/facilities. Needs diligence on percentage of revenue from maintenance/lighting vs one-time fabrication and any license/capex/union constraints.
- **Why overlooked:** It was one item in a multi-deal newsletter and does not use the current luxury/compliance labels, but the recurring maintenance layer is relevant.

#### Dairy Equipment Sales & Service
- **Sources:** Gmail (SMB Deal Hunter May 26 deal).
- **Key intelligence:** UT dairy equipment sales/service company with 50 years of farm relationships and ~$443K EBITDA. Relevance is service/maintenance relationship stickiness in a specialized equipment vertical.
- **People/contacts:** Helen Guo / SMB Deal Hunter.
- **Kay sentiment:** No direct Kay sentiment found.
- **Lifecycle warning:** Likely geographically narrow and agriculture-exposed; no G&B right-to-win found. Treat as pattern evidence for specialized equipment service, not an actionable niche absent more signals.
- **Why overlooked:** Hidden in newsletter deal flow and outside Kay's network/right-to-win.

#### Aerospace / Defense Opportunity
- **Sources:** calls (`2026-04-30 Camilla`, `2026-05-27 Jeff`, `2026-05-27 Camilla pest/drone review`, `2026-05-28 Erika`, `2026-06-01 Camilla strategy`), tracker (WEEKLY REVIEW row exists).
- **Key intelligence:** Woman-owned aerospace/defense business referral from XPX/corporate-advisor network; owner inherited business from husband, not deeply operational, possibly wants to sell. Later calls label aerospace/defense as a hard-exclude / decline candidate because it fails buy-box or investor-funding fit.
- **People/contacts:** Camilla de Sanna, Jeff Stevens, Erika Teresko; corporate-advisor referrer not fully identified in historical notes.
- **Kay sentiment:** Initially open ("interested in anything") because woman-owned transition angle, then moved toward hard-exclude/decline framing.
- **Lifecycle warning:** Do not surface as a live attractive niche without the rejection. Full lifecycle is proposed -> examined -> hard-exclude / decline framing.
- **Why overlooked:** It appears in WEEKLY REVIEW as "AEROSPACE DEFENSE" but historical calls show it should probably be treated as a dead/live-deal exception, not a niche-pipeline candidate.

#### Specialty Coffee Equipment Service
- **Sources:** calls (`2026-04-21 Guillermo`, `2026-04-22 Jeff`, `2026-05-13 Carlos`), tracker (TABLED).
- **Key intelligence:** Italian OEM authorized-dealer moat and service/maintenance contracts were compelling; Guillermo's key diligence question was whether the equipment is complex enough to avoid commodity margins and whether mid-sized premium chains outsource or insource service. Jeff saw one PE acquisition as validation but pushed on NYC market depth and mom-and-pop ceiling risk.
- **People/contacts:** Guillermo Lavergne, Jeff Stevens, Carlos Nieto.
- **Kay sentiment:** Interested enough to research, then tabled.
- **Lifecycle warning:** Tabled as of 2026-06-15; only revisit if new evidence resolves outsourcing, density, and contract-quality questions.
- **Why overlooked:** It emerged from call discussion and may not have had enough target discovery before tabling.

#### Fire Protection / Fire Sprinkler Services
- **Sources:** calls (`2025-10-21 Using AI to Improve Your Search`), tracker (current fire/life-safety row).
- **Key intelligence:** Early brainstorm explicitly named fire sprinkler annual inspections/service repairs and broader fire protection (alarms, extinguishers) as a PE-roll-up/target-landscape research candidate.
- **People/contacts:** Dino Beslic, Harrison Wells.
- **Kay sentiment:** No strong Kay sentiment found in that old call beyond exploration.
- **Lifecycle warning:** Already in WEEKLY REVIEW as Commercial Fire & Life Safety Inspection/Compliance + EV-charging wedge. Historical source supports the core fire-protection lane, not the EV wedge.
- **Why overlooked:** It started as an AI-search exercise rather than a human river-guide signal.

### Cross-Source Strength Notes
- **Strong / already tracked:** Trade Credit + Customs/Cargo Insurance, HNW/Fine-Art Insurance, Fine-Art Logistics, Commercial Cleaning/Facilities, Truck Licensing, Fire Protection, Specialty Coffee Equipment.
- **Potential overlooked but needs caution:** Heat-transfer/resort apparel customization; commercial sign manufacturing + maintenance/lighting; healthcare Environment-of-Care compliance SaaS.
- **Do not resurface as live without lifecycle warning:** Aerospace/defense, pure art advisory, specialty coffee equipment service, broad SaaS.

→ READY

---
## [niche-intel-synthesizer] — 2026-06-16T23:50:00-04:00

### 1. Cross-Source Signal Matrix.

| Niche/Industry | RECENT Sources | HISTORICAL Sources | Total Source Count | Strength | Tracker/Lifecycle Read |
|---------------|----------------|-------------------|-------------------|----------|------------------------|
| Premium / specialty pest management | web, newsletter, granola, gmail, vault | prior calls/tracker context | 5+ | VERY STRONG | ACTIVE duplicate: reinforce `Premium Pest Management`; do not create generic pest row. |
| Fine-art logistics / art services infrastructure | web, granola, vault | calls, tracker | 4 | VERY STRONG | ACTIVE duplicate; prioritize services-only, not storage-heavy. |
| HNW / fine-art / specialty insurance brokerage | web, granola, gmail, vault | calls, email, tracker | 5+ | VERY STRONG | ACTIVE duplicate across HNW, fine-art, trade-credit/customs/cargo, surplus-lines, FMO/IMO; no broad insurance row. |
| HOA / community association management | web, newsletter/conference, vault | tracker | 3 | STRONG | ACTIVE duplicate; rising PE heat means warm sourcing matters. |
| Building energy & emissions compliance / LL97 | web, vault | tracker / prior RE-services work | 3 | STRONG | ACTIVE duplicate; 2026 NYC deadline timing reinforces priority. |
| Facilities management / commercial building services / high-end cleaning | gmail metadata, web, vault | email, calls, tracker | 4 | VERY STRONG | ACTIVE duplicate; category validated but broker-visible/labor-heavy. |
| Truck licensing & compliance services | gmail/deal flow | email, tracker | 2 | STRONG | ACTIVE duplicate; recurring filing logic but thin-pool caveat remains. |
| Fire protection / life-safety inspection/compliance | vault/tracker context | calls, tracker | 2 | STRONG | ACTIVE duplicate; historical source supports fire-protection core more than EV wedge. |
| NY Metro multi-location auto repair succession | gmail weak repeat signal, vault | tracker | 2 | STRONG | ACTIVE duplicate; do not convert into tire/fleet without Kay approval. |
| Property tax appeal services | web | tracker | 2 | STRONG | ACTIVE duplicate; seasonal/regulatory reinforcement only. |
| Commercial sign manufacturing + maintenance / lighting service | none | email | 1 quantitative | MODERATE | Best overlooked adjacency; needs proof maintenance/lighting revenue is recurring and material. |
| Heat-transfer / resort-apparel customization manufacturing | none | calls | 1.5 | MODERATE | Warm one-off Love Unlimited lead; not a thesis until repeatable pool/recurring layer proven. |
| Healthcare environment-of-care compliance SaaS | none | email | 1 quantitative | MODERATE | Caution: software/healthcare category de-emphasized; only viable if reframed as compliance infrastructure. |
| Structural engineering / inspection / code-violation consulting | none | email / tracker adjacency | 1.5 | MODERATE | Supports Reserve Study / Building Engineering / FISP; specific E&K target too small. |
| Specialty coffee equipment service | none | calls, tracker | 2 | STRONG | TABLED; revive only with outsourcing-density and contract-quality evidence. |
| Art advisory + collection management / appraisal services | none | calls, tracker | 2 | STRONG | TABLED/caution; pure advisory structurally weak, service/appraisal layer only. |
| Aerospace / defense opportunity | vault recent calls | calls, tracker | 2 | STRONG | KILLED/DEAD for niche pipeline despite active-row artifact; treat as decline/live-deal exception. |
| Warranty/insurance-funded residential services | granola | none | 1 qualitative | WEAK | Watch item only; residential/single-source. |
| Medical-grade HBOT with insurance contracts | gmail | none | 1 quantitative | MODERATE | Off-buy-box healthcare/provider; do not advance. |
| Managed cybersecurity compliance / cyber software | gmail | none | 1 qualitative | WEAK | No-proceed: software/product-led, no services/owner-succession edge. |
| Dairy equipment sales & service | none | email | 1 quantitative | MODERATE | Pattern evidence for specialized equipment service, weak G&B edge. |

### 2. Named Company Registry with outreach routing flags. Avoid unsafe secret-file reads; if Attio API credentials are unavailable, use vault/tracker/Gmail evidence and state the gap.

Attio gap: I did not read secret files and did not run the Attio API because credentials were not safely available in this subagent context. Routing flags below use chatroom evidence plus vault cross-reference across `brain/entities`, `brain/calls`, `brain/outputs`, and `brain/inbox`. Before any outreach, run approved Attio checks through the credential ladder.

| Company Name | Niche | Source(s) | Independence / Size Read | Outreach Flag | Warm Contact | Notes |
|-------------|-------|-----------|--------------------------|---------------|--------------|-------|
| Total Extermination | Premium pest | recent granola/gmail/vault | Independent/live inbound lead | ACTIVE_DEAL | Juan Restrepo; David mutual friend; Camilla/DealsX | Vault entity/call exists; do not cold-add. |
| Romex Pest Control | Pest comp | recent web | Acquired by Rollins; top-40 PCT 100 | COMP_ONLY | none | Market-heat comp only. |
| Guardian Pest Control / Modern Pest Services / Anticimex | Pest comp | recent web | Guardian acquired by Modern/Anticimex | COMP_ONLY | none | Consolidation comp only. |
| EcoShield | Pest comp/caution | recent calls/vault | Large pest company; MLM-style sales model to verify | VAULT_HISTORY | Harrison Wells / Camilla context | Business-model caution. |
| Cadogan Tate; Crozier; UOVO; Maquette; Safe Art Transport; Art Crating; Atelier4; ArtBox; DIETL; Rock-It Company | Fine-art logistics | recent/historical/vault | Mix of large/acquired comps and possible specialists | COMP_ONLY / VAULT_HISTORY / NEW_TARGET_PENDING_ATTIO | Margot Romano, Alexandra Kelly, Levi Phelps, art network | Acumen/UOVO/Crozier/Cadogan/Maquette/SAT/Art Crating/Atelier4 have vault history or comp status; DIETL/ArtBox/Rock-It need Attio/ownership checks. |
| Acumen International / Acumen Fine Art Logistics | Fine-art logistics/storage | historical/vault | Prior engaged deal; LOI history | ACTIVE_DEAL / VAULT_HISTORY | Levi Phelps | Do not cold outreach; use as diligence comp. |
| Voxme | Art-logistics vertical software | historical/vault | Vendor used by Acumen | VAULT_HISTORY / COMP_ONLY | Levi Phelps | Software comp, not current outreach target. |
| Brown & Brown; Allianz Trade/Euler Hermes; Atradius; Coface | Insurance/carriers | recent/historical/vault | Public/global/large | COMP_ONLY | none | Reference/comps, not targets. |
| Accession Risk Management; Sterling Risk Insurance; ASZ International; Agent Brokers United | Specialty insurance | recent | Unknown from chatroom | NEW_TARGET_PENDING_ATTIO | possible insurance network | Validate ownership, sub-niche, and CRM status. |
| Trade Risk Group | Trade credit/customs/cargo | historical/vault | May be Acrisure partner/PE-affiliated per vault | VAULT_HISTORY / WARM_INTRO | Jeremy Black | Verify ownership; do not cold-add. |
| Trade Acceptance Group | Trade credit/customs/cargo | historical/vault | Specialist target; owner unknown | WARM_INTRO / VAULT_HISTORY | Jeremy Black | Route via Jeremy if pursued. |
| Texel / Meridian | Trade credit/cargo | historical | Likely larger/acquired or carrier/broker comp | COMP_ONLY_PENDING_CHECK | Jeremy Black | Reference/source validation. |
| FirstService Residential; Associa; RealManage | HOA | recent | Large platforms | COMP_ONLY | Guillermo/CAI network | Market comps, not targets. |
| Pioneer HOA; Community Association Management | HOA | recent | Unknown/ambiguous | NEW_TARGET_PENDING_ATTIO | Guillermo/CAI network possible | Needs disambiguation and ownership check. |
| IntelliGreen Partners | LL97/building energy | recent | Unknown | NEW_TARGET_PENDING_ATTIO | RE-services network possible | Validate target status. |
| NYC Accelerator / NYC DOB | LL97 ecosystem | recent web | Public/non-target orgs | SOURCE_ONLY | none | Source/river-guide context. |
| Reserve Advisors; Milrose; Conservice; RealPage; Metergy; RE BackOffice | RE-services comps/targets | recent | Mix of platforms and named providers | COMP_ONLY / NEW_TARGET_PENDING_ATTIO | RE-services network possible | Large platforms likely comps; RE BackOffice needs validation. |
| M Wheat Air | HVAC/government contractor | recent deal flow | Deal-flow company; not auto repair | NEW_TARGET_PENDING_ATTIO | SMB Deal Hunter/Helen Guo | Do not merge into auto repair. |
| Love Unlimited NY | Heat-transfer/resort apparel | historical/vault | ~$3.2M-$3.5M revenue, ~30% profitability | WARM_INTRO / VAULT_HISTORY | Tom and Jennifer Perino; Jeremy Black | Opportunistic warm deal, not thesis. |
| Schwartzman & Associates | Art advisory/appraisal/services | historical | Possibly small (~4 people) | WARM_INTRO_PENDING_ATTIO | Margot Romano / BofA Art Services | Only service/appraisal angle; pure advisory tabled. |
| E&K healthcare/regulatory compliance SaaS target | Healthcare compliance SaaS | historical email | ~$700K revenue; 1,500+ facilities | BROKER_DEAL_CAUTION | Everingham & Kerr | Too small/software-led unless reframed. |
| E&K structural engineering/inspection firm | Structural engineering/code violation | historical email | ~$200K revenue / ~$100K cash flow | BROKER_DEAL_CAUTION | Everingham & Kerr | Category validation only. |
| SMB Deal Hunter facility-maintenance contractor | Facilities | historical email | ~$4.5M revenue / ~$838K EBITDA | BROKER_DEAL_PENDING_ATTIO | Helen Guo | Validates category; broker-visible. |
| SMB Deal Hunter truck licensing platform | Truck licensing/compliance | historical email | ~$1.039M revenue / ~$412K EBITDA | BROKER_DEAL_PENDING_ATTIO | Helen Guo | Existing-row support; thin-pool caveat. |
| SMB Deal Hunter commercial sign company | Commercial sign/lighting maintenance | historical email | ~$4.364M revenue / ~$661K EBITDA | NEW_TARGET_PENDING_ATTIO | Helen Guo | Most interesting overlooked adjacency. |
| SMB Deal Hunter dairy equipment service company | Specialized equipment service | historical email | ~$443K EBITDA | BROKER_DEAL_CAUTION | Helen Guo | Pattern evidence, weak G&B edge. |
| Medical-grade HBOT provider | Healthcare/provider | recent gmail | $754,850 revenue / $369,451 profit | OFF_BUY_BOX | Business Exits | Watch only. |

### 3. Contact-to-Niche Map.

| Contact | Relationship Warmth | Niches They Can Help With | What to Ask Them | Last Contact |
|---------|---------------------|--------------------------|------------------|--------------|
| Juan Restrepo | WARM | Premium pest / Total Extermination | Qualify owner interest, revenue mix, commercial/luxury exposure, recurring contracts | Callback attempt 2026-06-15 |
| David mutual friend | WARM | Premium pest | Intro/context for Juan and Total Extermination | Mentioned in Total Extermination vault note |
| Jay Davis | HOT/WARM | Pest, specialty pest wedges | Pressure-test premium/specialty pest target types and valuation | Recent Granola call |
| Camilla de Sanna | HOT | Pest strategy, aerospace-defense lifecycle, owner-succession framing | Keep pest wedge disciplined; confirm aerospace decline status | Multiple calls through 2026-06 |
| Warren Chan / Anacapa | HOT/WARM | Fine-art logistics, art services, fine-art insurance | Identify experienced insurance operators and targetable art-services businesses | Recent Granola call |
| Margot Romano / BofA Art Services | WARM | HNW/fine-art insurance, art advisory, collection management, UOVO intro path | Ask for service/appraisal operators, not pure advisory; validate Schwartzman | 2026-04 historical call |
| Alexandra Kelly / UOVO | WARM via Margot | Fine-art logistics/storage | Comp/market diligence; storage constraints | Prior Margot intro |
| Levi Phelps / Acumen | HOT/WARM | Fine-art logistics/storage, customs brokerage, Voxme/software | Use diligence learnings; possible river guide for services-only art logistics | 2025 Acumen calls/LOI history |
| Jeremy Black | HOT/WARM | Trade credit/customs/cargo insurance, Love Unlimited, specialty insurance | Ask for TAG/TRG principal intro; pressure-test repeatable target pool; Love deal status | 2026-02 thread/call |
| Kay's brother in marine logistics | WARM | Cargo/customs/trade credit insurance | Validate marine-logistics buyer pain and broker referral channels | Mentioned in Jeremy thread |
| August Felker | WARM | HNW personal lines / fine-art insurance | Revisit investor objections, operator profile, target economics | 2025-11-19 call |
| Anna Raginskaya / Morgan Stanley | WARM/COOL | Art insurance, HNW network | Insurance/art services intro path | Historical intro thread |
| Ryan LaMay | WARM/COOL | Business insurance | Insurance-market diligence and intros | Historical thread |
| Richard Augustine | COOL | HNW/specialty insurance | Specialist perspective via August path | Referenced by August |
| Guillermo Lavergne | HOT | HOA/CAI network, specialty coffee caution | Use CAI access for HOA warm sourcing; only revive coffee with density proof | Recent investor cadence / historical calls |
| Jeff Stevens | HOT | Aerospace-defense rejection, specialty coffee challenge, art services pressure-test | Validate kill/tabled decisions and investor fit | 2026-05/06 calls |
| Erika Teresko | WARM | Aerospace-defense referral/lifecycle | Confirm no further action if declined | 2026-05-28 call |
| Helen Guo / SMB Deal Hunter | COOL/WARM | Truck licensing, commercial sign maintenance, facilities, dairy equipment | Request details only where niche has second-source potential | May 2026 deal emails |
| Andrew Lowis / Axial | COOL/WARM | Commercial cleaning/facilities, commercial property management | Retrieve unavailable deal bodies if useful; treat as broker-visible comp channel | Recent deal-flow metadata |
| Everingham & Kerr | COOL/WARM | Healthcare compliance SaaS, structural engineering | No immediate ask unless category is revived | Historical deal emails |
| Dino Beslic | WARM/COOL | Fire sprinkler/fire protection | Use for association/source map if fire-protection row advances | 2025-10-21 call |
| Harrison Wells | HOT | Search strategy, fire-protection brainstorm, pest business-model caution | Pressure-test whether signals warrant action vs research | 2025-10 / 2026-06 calls |
| Tom and Jennifer Perino | WARM | Love Unlimited / heat-transfer resort apparel | Deal-specific owner diligence, not thesis sourcing | 2026-01-18 call |

### 4. Lead Lifecycle Tracker.

| Niche/Strategy | Proposed By | When | Challenged By | When | Reason | Status |
|---------------|-------------|------|---------------|------|--------|--------|
| Generic pest management | Market/recent sources | 2026-06 | Jay Davis, Camilla/Kay strategy, tracker caution | 2026-06 | Too liquid/crowded; broad pest not differentiated | KILLED as generic; LIVE only as premium/specialty wedge |
| Premium pest for luxury hospitality/commercial properties | Camilla/Kay, Jay Davis, DealsX/Juan | 2026-06 | Market M&A caution | 2026-06 | Need first target around ~$500K EBITDA and specialty/premium proof | LIVE / ACTIVE |
| Fine-art storage-heavy model | Art network / Acumen diligence | 2025-2026 | Investors/learnings, Acumen diligence | 2025-2026 | Balance-sheet/capex/insurance constraints | TABLED/CAUTION |
| Fine-art logistics services-only | Warren Chan, Acumen/Margot context | 2025-2026 | Capital intensity caution | 2026 | Attractive if asset-light services/installation/crating/logistics | LIVE / ACTIVE |
| Broad insurance brokerage | Multiple sources | 2026 | Tracker cautions / investor feedback | 2026 | Too broad, M&A crowded, needs sub-niche | KILLED as broad; sub-niches LIVE |
| HNW personal lines / fine-art insurance | August Felker, Jeremy Black, Warren/Margot network | 2025-2026 | August/investor feedback | 2025-2026 | Multiples, QSBS, operator experience; still sticky/renewal-rich | LIVE / ACTIVE |
| Trade credit/customs/cargo insurance brokerage | Jeremy Black | 2026-02 | Target-pool uncertainty | 2026 | Recurring and compelling but needs agency with sufficient numbers | LIVE / ACTIVE |
| HOA/community association management | RE-services run / Guillermo CAI edge | 2026-06 | Recent PE heat | 2026-06 | Attractive score but needs off-market sourcing | LIVE / ACTIVE |
| Building energy & emissions compliance / LL97 | RE-services run / recent web | 2026-06 | None material | 2026-06 | Strong regulatory deadlines | LIVE / ACTIVE |
| Specialty coffee equipment service | Guillermo/Jeff/Carlos | 2026-04/05 | Guillermo, Jeff | 2026-04/06 | Need outsourced service density and contract quality; mom-and-pop ceiling risk | TABLED |
| Pure art advisory | Margot/Kay art network | 2026-04 | Margot Romano / Jeff pressure-test | 2026-04 | Banks provide advisory free; weak regulatory moat; variable fees | TABLED/KILLED as pure advisory |
| Collection management / appraisal / art services | Margot / tracker ideation | 2026-04/06 | Pure advisory concerns | 2026 | Viable only with defensible service/valuation/appraisal layer | TABLED / WATCH |
| Aerospace/defense | XPX/corporate-advisor referral via Camilla/Erika | 2026-04/05 | Jeff/Camilla/Kay | 2026-05/06 | Fails buy-box/investor-funding fit | DEAD/KILLED for niche pipeline |
| Heat-transfer/resort apparel customization | Tom/Jennifer; Jeremy Black | 2026-01/02 | Jeremy Black | 2026-02 | Weak contracted recurring revenue and limited growth | LIVE as opportunistic deal; not niche |
| Healthcare/regulatory compliance SaaS | Everingham & Kerr | 2026-03/05 | Tracker software caution / buy-box learnings | 2026 | Small, SaaS/product-led, healthcare software de-emphasized | TABLED/CAUTION |
| Commercial sign manufacturing + maintenance | SMB Deal Hunter | 2026-05 | No direct challenge yet | 2026-06 | Needs proof recurring maintenance/lighting dominates fabrication | LIVE as watchlist candidate |
| Dairy equipment sales/service | SMB Deal Hunter | 2026-05 | Right-to-win screen | 2026-06 | Geography/agriculture exposure; no G&B edge | DEAD unless more sources emerge |
| HBOT provider | Business Exits | 2026-06 | Buy-box screen | 2026-06 | Healthcare provider/off-buy-box, small | DEAD/WATCH only |
| Cybersecurity software | E&K | 2026-06 | Buy-box screen | 2026-06 | Software/product-led, no services/owner-succession edge | DEAD |

### 5. Convergence Report ranked top 3-5 signals.

| Rank | Signal | Why It Ranks | Action for Identifier |
|------|--------|--------------|-----------------------|
| 1 | Premium / specialty pest management | Most current operating momentum: live inbound Total Extermination lead, recent calls, association/newsletter signal, and explicit G&B wedge refinement. Exit market is liquid but broad-pest price risk is real. | Do not identify as new. Reinforce active priority with specialty/premium target filters and no generic pest row. |
| 2 | Fine-art logistics services-only / art services infrastructure | Strong G&B right-to-win plus multiple historical and recent sources. Storage-heavy model is constrained by capital and insurance. | Refine active row toward asset-light logistics/install/crating/services, not warehouse/storage-first. |
| 3 | Specialty insurance sub-niches: HNW/fine-art and trade credit/customs/cargo | Strong source convergence, recurring revenue, renewal stickiness, exit path, and warm contacts. Broad insurance is too crowded. | Reinforce existing rows; route through Jeremy/August/Margot/Warren, not generic cold insurance outreach. |
| 4 | HOA/community association management + LL97/building compliance | Both have strong RE-services scores and fresh regulatory/market validation. HOA has CAI/Guillermo access but rising PE heat; LL97 has immediate 2026 deadline pressure. | Keep active; prioritize warm river-guide sourcing over broad list build. |
| 5 | Commercial sign manufacturing + maintenance / lighting service | Best overlooked moderate signal: quantitative broker deal with recurring maintenance/lighting layer, adjacent to facilities/commercial equipment maintenance, but only one source. | Consider watchlist/identifier candidate only if a second source confirms recurring maintenance economics and target pool. |

→ READY

---
## [niche-intel-identifier] — 2026-06-16T23:59:00-04:00

### Duplicate / Lifecycle Filter

High-strength signals not advanced because they are already active, tabled, killed, or semantic duplicates:
- Premium / specialty pest management — active duplicate of `Premium Pest Management`; new evidence should refine the premium/specialty wedge, not create a generic pest row.
- Fine-art logistics / art services infrastructure — active duplicate of `Fine-Art Logistics Services` and related high-value asset storage/services rows; storage-heavy version remains constrained by capex and insurance.
- HNW/fine-art/specialty insurance and trade credit/customs/cargo brokerage — active duplicates of existing specialty insurance rows; use as validation and warm-routing context only.
- HOA/community association management and LL97/building compliance — active duplicates of `HOA / Community Association Management` and `Building Energy & Emissions Compliance Services`.
- Facilities management / commercial building services / high-end cleaning — active duplicate of existing facilities and cleaning rows.
- Truck licensing & compliance, fire/life-safety, property tax appeal, auto repair succession — active duplicates.
- Specialty coffee equipment service, art advisory / collection management, healthcare compliance SaaS, aerospace/defense, dairy equipment service, HBOT, and cybersecurity software — tabled/killed/off-buy-box or insufficiently changed by new evidence.

### Candidate 1

Niche: Sign and Lighting Maintenance Programs for Multi-Location Commercial Brands

Thesis: The attractive version is not broad sign manufacturing; it is outsourced maintenance, repair, LED retrofit, inspection, and program management for illuminated signs, parking-lot lighting, and brand assets across multi-location commercial customers. The recurring or reoccurring layer comes from planned/preventive maintenance, national-account service programs, emergency repair response, LED conversion cycles, and brand-refresh programs, which distinguishes it from one-time fabrication and from generic facilities management.

Source Signal: SMB Deal Hunter surfaced an absentee-run MO commercial sign manufacturer with $4.364M revenue and $661K EBITDA where maintenance and lighting service appeared to create a repeat layer. Independent validation found multiple operators explicitly marketing planned/preventive sign maintenance, national sign/lighting service programs, LED retrofits, monthly inspections, and maintenance contracts; PE has also backed scaled sign-and-lighting services platforms such as MC Sign, Stratus, and Persona/Triangle.

Checked against active niches — not a duplicate of:
- `Facilities Management / Commercial Building Services`: this is narrower and sign/lighting-specific, with its own specialized technicians, sign contractors, bucket-truck/aerial service needs, permitting, brand-standard work, and national sign-program buyer set.
- `Commercial Equipment Maintenance`: signage/lighting is a branded exterior-asset and visual-compliance service, not general production or foodservice equipment repair.
- `High-End Commercial Cleaning`: same property/customer universe, different service line, labor/equipment base, buyer pain, and competitive set.
- `Commercial Fire & Life Safety Inspection/Compliance`: both touch commercial property compliance/maintenance, but signs/lighting are brand/safety/energy-maintenance assets, not mandated life-safety inspection.

Key Question: What percentage of revenue at targetable independents is true planned/preventive maintenance, national-account recurring service, or high-frequency reoccurring repair/retrofit work versus lower-quality one-time fabrication/install projects?

Preliminary Fit Assessment: Meets B2B services, asset-light relative to storage/real estate, fragmented target pool, repeat/reoccurring service behavior, and visible PE exit pathway. Needs validation on maintenance revenue mix, electrician/sign-contractor licensing constraints, bucket-truck/fleet intensity, customer concentration in national accounts, and whether Kay has a credible operating/right-to-win angle beyond general B2B service management.

QUICK SCREEN:
- Margins: Moderate — broker/deal example implied ~15.1% EBITDA ($661K / $4.364M); industry rule-of-thumb sources indicate recurring maintenance/service contracts can improve stability and valuation, but broad sign manufacturing margins may be mixed and fabrication-heavy operators may fall below the 15% target.
- Recurring / Reoccurring Revenue: Moderate — not necessarily subscription-like, but operators advertise planned/preventive maintenance, monthly inspections, maintenance contracts, emergency service, LED retrofits, repair programs, and national-account maintenance support. Revenue quality is strongest only where service/maintenance is >30% of revenue or where multi-location customers use the company as an ongoing program manager.
- Industry Growth: Moderate — IBISWorld reports U.S. billboard/sign manufacturing at $16.4B in 2026 with 2.4% CAGR from 2021-2026 and expected growth over the next five years; service demand is supported by LED retrofit cycles, weather exposure, digital signage, brand refreshes, and multi-location operators outsourcing consistency.

TARGET TAM:
- Total firms in market: ~5,702 U.S. billboard/sign manufacturing businesses per IBISWorld 2026; ISA publicly cites a broader U.S. sign ecosystem of ~14,000 firms; SICCODE lists 11,782 active NAICS 339950 companies. The practical serviceable universe is smaller because many shops are print/sign design firms without lighting maintenance capability.
- Independently owned (potential targets): likely 200-500+ with meaningful illuminated-sign, lighting, installation, repair, or maintenance capability; state association directories show many local/regional sign companies, but the subset with recurring multi-location maintenance programs needs list-build verification.
- Already PE-backed/acquired: visible platforms and roll-ups include MC Sign, Stratus, Persona/Triangle, Federal Heath, Comet Signs, Priority, and related add-ons; count of known PE/strategic-acquired platforms from this pass is at least 6-10.
- PE consolidation risk: Medium — enough PE activity to validate exit path, but local/regional sign-and-lighting service remains fragmented; risk is higher for national-account platforms and lower for regional owner-operated service providers.
- Named examples: PSCO Sign Group (PA / national service programs); Shamrock Signs (PA, maintenance contracts and lighting retrofits); National Sign Co. (OH, sign maintenance and lighting services); Carolina Signs (NC, sign maintenance, repairs, and lighting replacement); Florida Lighting Maintenance (FL, commercial lighting/signage preventative maintenance contracts). Additional comps: Federal Heath, Stratus, MC Sign, Persona/Triangle, Atlas Sign Industries.

MARKET TAM:
- Market size: $16.4B U.S. billboard/sign manufacturing market in 2026 (IBISWorld/NAICS 339950). Sign maintenance/lighting service is a subset; no reliable standalone public TAM found in this pass, but the market clears the $500M growth-TAM floor if even a mid-single-digit share of the broader sign ecosystem is recurring maintenance/service.
- Growth rate: 2.4% CAGR for the broader market from 2021-2026, with forecast growth over the next five years per IBISWorld; maintenance/retrofit demand may grow faster where LED conversion, digital signage, energy efficiency, and national-account outsourcing are present.
- Key demand drivers: multi-location brand consistency; illuminated sign uptime; safety/liability and code concerns; weather exposure; LED energy retrofits; digital signage repair; parking-lot/exterior lighting maintenance; brand refresh/reimaging programs; national customers preferring outsourced program management over reactive local vendor searches.

Sources used for validation:
- Chatroom synthesizer convergence report and named-company registry, 2026-06-16.
- `brain/context/learnings.md` for fit criteria and pitfalls.
- IBISWorld public pages for Billboard & Sign Manufacturing / NAICS 339950 market size, business count, and growth.
- ISA public membership/industry pages for broader firm-count context.
- Operator/service examples: PSCO Sign Group, Shamrock Signs, National Sign Co., Carolina Signs, Florida Lighting Maintenance, Federal Heath, Stratus.
- PE/transaction examples: TM Capital / MC Sign sale to Caltius, Arcapita / MC Sign, Stratus acquisitions, Exeter / Persona-Triangle, Federal Heath sale.

→ READY

---
## [niche-intel-scorer] — 2026-06-16T22:52:56-04:00

### Sign and Lighting Maintenance Programs for Multi-Location Commercial Brands — Scoring Summary

**Overall score:** 2.13/3.0 (Moderate / Watchlist)

**Initial Screen:** Partial fail. Margins, recurring/reoccurring revenue, and Growth TAM pass; Industry Growth fails because the broader public sign market CAGR is ~2.4% from 2021-2026, below the ~3% GDP gate. Scoring completed because the repeat-service maintenance wedge remains potentially attractive, but promotion should wait for validation that maintenance/lighting service is a material revenue share.

**Category scores (/3):**
- Growth, Penetration & Catalyst: 1.75 — broader market growth below GDP; LED, digital signage, weather exposure, brand refresh, and outsourced national-account maintenance are real but unproven as a faster-growth service subset.
- Size & Fragmentation: 3.00 — 5,702 NAICS businesses and broader ISA/SICCODE counts of ~11,782-14,000 support a fragmented market; likely 200-500+ practical service-capable independents pending list-build.
- Industry Economics: 2.00 — broker example clears 15% EBITDA at ~15.1%, but fabrication-heavy work, subcontracting, fleet, and bucket-truck intensity limit margin quality.
- Mission Criticality: 2.33 — clear brand-uptime, lighting, safety, and multi-location vendor-management value prop; switching costs are moderate, not deep.
- Exogenous Risks: 2.20 — LED/digital tailwinds help, but electrical/sign licensing, permitting, OSHA/aerial work, liability, and capex-sensitive retrofit cycles remain real.
- Porter's Five Forces: 1.83 — low VC disruption, but high competition from sign shops, lighting/electrical contractors, facilities vendors, and national platforms; customer power is meaningful in multi-location/national accounts.
- Value Creation Opportunities: 2.50 — strong levers in recurring service contracts, route density, dispatch/CRM, national-account program management, LED retrofit cross-sell, and tuck-in acquisitions.
- Impact & Externalities: 2.00 — neutral overall; safety/visibility and energy-efficient LED retrofits offset light pollution and fleet miles.

**Explicit weighted math:** (1.75*25%) + (3.00*10%) + (2.00*10%) + (2.33*15%) + (2.20*10%) + (1.83*15%) + (2.50*10%) + (2.00*5%) = **2.13/3.0**.

**Weekly-review columns:**
- QSBS: Likely yes if structured as QSBS-eligible C-corp; confirm service/manufacturing assets and exclusions with counsel.
- Target Pool: Likely 200-500+ independents with meaningful sign/lighting maintenance capability; list-build required.
- Quick notes: Repeat-service sign/lighting maintenance wedge is attractive, but broader growth is only ~2.4%, recurring mix is unproven, and national-account concentration/fleet/licensing need diligence.

**Uploaded scorecard:** `Sign and Lighting Maintenance Programs Scorecard June 2026.xlsx` — file ID `14KKJBwuUecRoHrDBH2Xbm-XJOe_Shjdh` — https://docs.google.com/spreadsheets/d/14KKJBwuUecRoHrDBH2Xbm-XJOe_Shjdh/edit?usp=drivesdk

**Local scorecard:** `/tmp/sign-and-lighting-maintenance-programs-scorecard.xlsx`

**One-pager update:** Updated Assessment/Status and replaced existing Drive file without creating a duplicate — file ID `1DaHJUvtzrJZyUswbQhkTD1lNZf7HQWH8` — https://docs.google.com/presentation/d/1DaHJUvtzrJZyUswbQhkTD1lNZf7HQWH8/edit?usp=drivesdk

**Hard blockers / diligence gaps:** standalone maintenance-service TAM not publicly verified; recurring/service revenue mix at targetable independents is unproven; licensing/electrical constraints, fleet intensity, customer concentration, and G&B right-to-win need validation.

→ READY

---
## [niche-intel-tracker] — 2026-06-16T22:57:11-04:00

Updated Industry Research Tracker `WEEKLY REVIEW` for **Sign and Lighting Maintenance Programs for Multi-Location Commercial Brands**.

- Snapshot: `/tmp/weekly-review-pre-sign-lighting-2026-06-16.json`
- Append range: `'WEEKLY REVIEW'!A30:K30`
- Row: 30
- Rank: 27
- Verification: re-read `WEEKLY REVIEW`; niche appears exactly once after write.

→ READY

---
## [orchestrator] — 2026-06-16T23:03:00-04:00
Final report and JSON sidecar written. Drive folder verified with exactly one `.pptx` one-pager and one `.xlsx` scorecard. Tracker row verified once at `WEEKLY REVIEW!A30:K30`.
→ CLOSE
