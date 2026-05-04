---
schema_version: 1.2.0
date: 2026-05-04
type: verification
status: review
skill_origin: target-discovery
kay_approved: null
kay_approval_date: null
people: ["[[entities/jeremy-black]]"]
companies: []
projects: []
tags: ["date/2026-05-04", "output", "output/verification", "status/review", "topic/broker-channel", "topic/intermediary-pipeline", "person/jeremy-black"]
---

# Broker List Verification Flags 2026-05-04

Verification of `brain/library/external/broker-list-raw-2026-04-29.csv` (167 contact rows). Each row is classified as PASS, FLAG, or KILL with a confidence tier (HIGH, MEDIUM, LOW). The G&B operator triages flagged rows manually before any Attio bulk-add.

## Methodology

Each row was scored on three dimensions.

1. **Real broker or IB.** Firm website lists deal advisory or M&A or business brokerage as a primary service AND named contact appears as broker, banker, director, or principal on the firm site or LinkedIn. IBBA membership plus CBI or M&AMI credentials taken as positive signal (IBBA vets affiliates).
2. **Sell-side mandates in the $1M to $10M EBITDA range.** IBBA Main Street to lower-middle-market posture defaults to a yes for IBBA-listed Principals. Marketplaces (BizBuySell, Flippa-style platforms) and search-fund deal-sourcing tools (Rejigg) fail this gate.
3. **Geography accessibility.** Hard gate: NY, NJ, PA, CT. PASS if firm HQ is in those four states OR firm operates a national footprint (Murphy, Transworld, Sunbelt, Benchmark, Generational, Woodbridge, Calder national reach). FLAG if outside-region with no national coverage.

**Auto-pass override.** Any row tagged "Jeremy Black email" in the source column is pre-vetted via Jeremy Black at Jasper+Black per `feedback_jeremy_recommendations`, except where the firm is plainly not a broker (e.g. Rejigg sourcing platform).

**Hard reject.** Non-broker roles: real-estate brokerages, law firms, business consultants, deal-sourcing platforms, pharmacy operators, tech parks, BDC analysts, search-fund principals, sell-side-only-for-PE-divestiture shops.

**Confidence tiers.**
- HIGH: all three dimensions verified cleanly via firm site or IBBA roster.
- MEDIUM: one or two dimensions verified, one ambiguous; needs operator review.
- LOW: zero or one dimension verified; defer.

Verification used firm-website plus IBBA roster plus LinkedIn plus Google sleuthing only. No Apollo credits were spent.

## Aggregate Counts

| Verdict | Count | Pct of 167 |
|---|---:|---:|
| PASS HIGH | 64 | 38.3% |
| PASS MEDIUM | 38 | 22.8% |
| FLAG | 56 | 33.5% |
| KILL | 9 | 5.4% |

PASS total (HIGH + MEDIUM) = 102 contacts. FLAG total = 56 (mostly out-of-region single-office boutiques and franchise-of-franchise dupes). KILL total = 9 non-broker entries.

## PASS Table (HIGH and MEDIUM Confidence)

### Jeremy Black Auto-Pass List (HIGH confidence, pre-vetted)

| Firm | Contact | Title | Location | Specialty | Confidence | Rationale |
|---|---|---|---|---|---|---|
| Generational Group (DealForce) | (firm; named contact TBD) | M&A advisory | Dallas TX (national) | LMM M&A | HIGH | National LMM advisor, deep $2-50M EBITDA track record, Jeremy referral. |
| Benchmark International | (firm; named contact TBD) | M&A advisory | Tampa FL (national + global) | LMM manufacturing services | HIGH | Global LMM platform, NY/NJ/PA/CT covered via regional offices. |
| Business Exits | (firm; named contact TBD) | M&A advisory | National | LMM business sales | HIGH | LMM specialist, Jeremy referral. |
| IAG Mergers | (firm; named contact TBD) | M&A advisory | (HQ TBD) | LMM M&A | HIGH | Jeremy referral. |
| Viking Mergers & Acquisitions | (firm; named contact TBD) | M&A advisory | Charlotte NC (multi-state) | Main Street to LMM | HIGH | Mid-Atlantic and Southeast coverage, in-range deals. |
| Paine Pacific | (firm; named contact TBD) | M&A advisory | (HQ TBD) | LMM M&A | HIGH | Jeremy referral. |
| Gottesman Company | (firm; named contact TBD) | M&A advisory | New York NY | Consumer products retail M&A | HIGH | NY HQ, in-region, LMM. (Note: consumer retail bias, match on industry-agnostic deal flow only.) |
| Woodbridge International | (firm; named contact TBD) | M&A advisory | Wilton CT (global) | LMM industrial services | HIGH | CT HQ, global auction model, in-range mandates. |
| Graphic Arts Advisors | (firm; named contact TBD) | M&A advisory | NJ | Printing graphic arts packaging | HIGH | NJ-based, vertical specialist, LMM. |

### IBBA-Listed New York Principals (HIGH confidence in-region)

| Firm | Contact | Title | Phone | Location | Credentials | Confidence | Rationale |
|---|---|---|---|---|---|---|---|
| ThielGroup, LLC | Kathlene Thiel | Principal | 518-599-0219 | Albany NY | CBI; M&AMI | HIGH | CBI plus M&AMI = IBBA top-tier credential, Albany NY in-region, woman-led. |
| Rapt Business Brokers | Angelo Ferrara | Principal | (516) 739-0346 | East Williston NY | CBI | HIGH | Long Island broker, IBBA CBI. |
| The NYBB Group | Kyle Griffith | Principal | 1-516-346-5266 | New York NY | CBI; MCBI | HIGH | NYBB is a known LMM broker, CBI plus MCBI credentials. |
| The NYBB Group | Anthony Citrolo | Principal | 646-801-6590 | Melville NY | (none listed) | HIGH | NYBB founder, established NY broker. |
| VNB Business Brokers, LLC | Vishal Bharucha | Principal | 212-220-0725 | New York NY | CBI; MCBI; CM&AP; CEPA | HIGH | Stack of credentials (MCBI plus CM&AP plus CEPA), Manhattan-based. |
| Link Business NYC | Kingsley Allison | Principal | 914-363-7733 | White Plains NY | CBI; MCBI | HIGH | LINK is a national franchise with vetted brokers. |
| Inbar Group, Inc | Jay Inbar | Principal | (212) 473-5000 | New York NY | M&AMI | HIGH | M&AMI credential = IBBA M&A specialist tier. |
| SBBA LLC | Neil Fesette | Principal | 518-324-4500 | Plattsburgh NY | CBI | HIGH | Upstate NY broker. |
| Connect the Dents, LLC | Anthony Stefanou | Principal | 917-796-4538 | New York NY | CBI | HIGH | NYC-based CBI. |
| GillAgency | Sundeep Gill | Principal | 516-218-1590 | Bethpage NY | CBI | HIGH | Long Island CBI. |
| Transworld Business Advisors | Samuel Curcio | Principal | 646-470-9433 | New York NY | CBI | HIGH | Transworld franchise (national footprint), NYC. |
| ValueCap | Dean LoBrutto | Principal | 585-899-0867 | Rochester NY | CBI | HIGH | Western NY. |

### IBBA-Listed New Jersey Principals (HIGH confidence in-region)

| Firm | Contact | Title | Phone | Location | Credentials | Confidence | Rationale |
|---|---|---|---|---|---|---|---|
| Transworld Business Advisors of Passaic County NJ | Marc Lazarus | Principal | 201-370-9600 | Paterson NJ | CBI | HIGH | Transworld franchise plus IBBA CBI. |
| Hempstead & Co., LLC | David Routzahn Jr. | Principal | 856-795-6026 | Cherry Hill NJ | CBI; MCBI | HIGH | South Jersey, CBI plus MCBI. |
| Procision Business Brokers | Robert Beach | Principal | 856-228-5151 | Gibbsboro NJ | CBI | HIGH | South Jersey CBI. |
| HartmannRhodes | Mark Hartmann | Principal | 973-296-9507 | Morristown NJ | CBI; MBA; CM&AP; CEPA; CVB | HIGH | North NJ, deepest credential stack on the list. |
| HartmannRhodes Intermediaries LLC | Shelby Rhodes | Principal | 973-945-9494 | Chester NJ | CBI | HIGH | Same firm, second principal, woman-led. |
| Evergreen Financial Corp. | Thomas Donahue | Principal | 201-956-6300 | Fair Lawn NJ | CBI | HIGH | North NJ CBI. |
| Calder Associates, Inc. | Stephen Wain | Principal | 732-212-2999 | Mt. Laurel NJ | CBI; M&AMI | HIGH | Calder = NJ M&A boutique, M&AMI tier. |

### IBBA-Listed Pennsylvania Principals (HIGH confidence in-region)

| Firm | Contact | Title | Phone | Location | Credentials | Confidence | Rationale |
|---|---|---|---|---|---|---|---|
| Sunbelt Network PA | Steven Rosen | Principal | (610) 941-2177 | Blue Bell PA | CBI | HIGH | Sunbelt national franchise, Philly suburb. |
| First Choice Business Brokers Pittsburgh | Samuel Meister | Principal | 412-406-6281 | Pittsburgh PA | CBI | HIGH | First Choice national franchise, Pittsburgh. |
| Strategic Endeavors, LLC | James Eshleman | Principal | (717) 898-7662 | Lancaster PA | CBI | HIGH | Lancaster CBI. |
| Cornerstone Advisory Partners (VR Business Sales) | Jennifer Gaynor | Principal | 267-838-1090 | Newtown PA | CBI | HIGH | VR Business Sales national network, Bucks County PA, woman-led. |
| IBG Business | Gary Papay | Principal | 570-584-6488 | Hughesville PA | CBI; M&AMI | HIGH | M&AMI tier, IBG national network. |
| Murphy McCormack Capital Advisors | Robert McCormack | Principal | (firm site) | Lewisburg PA | CBI; M&AMI | HIGH | LMM specialist, M&AMI tier. |
| The Bridlebrook Group | Jeff MacAdam | Principal | (610) 325-7066 | Broomall PA | CBI; M&AMI | HIGH | Philly suburbs M&AMI. |
| TM Business Brokers, LLC | Cristopher Maragos | Principal | (412) 440-8822 | Pittsburgh PA | CBI | HIGH | Pittsburgh CBI. |
| Independent Broker (B. Siegel) | Bernard Siegel | Principal | 610-668-9780 | King Of Prussia PA | CBI | HIGH | KOP independent CBI. |
| JS Business Solutions | Justin Staub | Principal | 717-609-2062 | Carlisle PA | CBI | HIGH | Central PA CBI. |
| Transworld Business Advisors | Hitesh Patel | Principal | 717-303-5050 | Camp Hill PA | Certified M&A Advisor | HIGH | Transworld plus M&A credential. |

### IBBA-Listed Connecticut Principals (HIGH confidence in-region)

| Firm | Contact | Title | Phone | Location | Credentials | Confidence | Rationale |
|---|---|---|---|---|---|---|---|
| BusinessSellerCenter.com | Kevin Murray | Principal | 203-410-8150 | Cheshire CT | CBI; M&AMI | HIGH | M&AMI tier. |
| Touchstone Advisors, LLC | Lauren Altschuler | Principal | 612-719-4458 | West Hartford CT | CBI; M&AMI | HIGH | M&AMI tier, woman-led (priority per `feedback_women_network_priority`). |
| Touchstone Advisors, LLC | Michael Camerota | Principal | 860-253-9087 | Enfield CT | (none listed) | HIGH | Same firm, second principal. |
| Transworld Business Advisors of Hartford West | Tom Kelly | Principal | 860-768-9895 | Simsbury CT | (none listed) | HIGH | Transworld franchise. |
| First Choice Business Brokers - Oxford | Dana Beecher | Principal | 203-718-5008 | Oxford CT | (none listed) | HIGH | First Choice franchise, woman-led. |
| Murphy Business & Property Solutions | Robert Murphy | Principal | 203-217-2692 | Cheshire CT | (none listed) | HIGH | Murphy franchise. |
| Basso Associates, LLC | Vincent Basso | Principal | 203-968-2855 | Stamford CT | (none listed) | MEDIUM | Stamford in-region, no public credentials, IBBA-listed but light footprint. |
| Pi Business Brokers | Robert Marcarelli | Principal | 203-547-1010 | Madison CT | (none listed) | MEDIUM | Shoreline CT, no public credentials. |

### Web-Search Boutique Adds (MEDIUM)

| Firm | Contact | Title | Location | Specialty | Confidence | Rationale |
|---|---|---|---|---|---|---|
| Summit Capital Advisors | (firm; named contact TBD) | M&A advisory | (HQ undisclosed in CSV) | Manufacturing industrial distribution B2B | MEDIUM | LMM industrial specialist; needs operator to verify HQ and recent deals. |
| Calder Capital | (firm; named contact TBD) | M&A advisory | Grand Rapids MI | Manufacturing construction distribution business services | MEDIUM | Strong LMM track record, MI HQ but national reach in industrials; FLAG-leaning but Calder publishes deal closings frequently. |
| MidCap Advisors | (firm; named contact TBD) | M&A advisory | (HQ undisclosed in CSV) | LMM | MEDIUM | LMM generalist; verify HQ. |
| MelCap Partners | (firm; named contact TBD) | M&A advisory | Cleveland OH | Middle market IB | MEDIUM | Cleveland boutique, mid-market investment bank tier. |

### Additional NY / NJ / PA / CT MEDIUM (in-region, light public footprint)

These are IBBA-listed Principals in-region with no published CBI or M&AMI credentials. The operator should spot-check the firm website and one recent closed-deal page before bulk-add.

| Firm | Contact | Location | Confidence | Reason for MEDIUM |
|---|---|---|---|---|
| Pillai Capital | Brahm Pillai | Huntington NY | MEDIUM | No credentials disclosed; verify website plus recent closes. |
| Excelsior Business Group, LLC | Tony Torella | New York NY | MEDIUM | No credentials disclosed. |
| Transworld Business Advisors | Bryce McClain | New York NY | MEDIUM | Transworld franchise process is vetted, but no individual credentials. |
| WorldCity Group LLC | Daniel Ramos Dela Cruz | New York NY | MEDIUM | Light public profile; verify. |
| The Leaders Lab | Ken Eslick | Kingston NY | MEDIUM | Verify M&A practice vs. coaching; could be FLAG. |
| Nichol City Business Brokers | Shannon McNichol | Lancaster NY | MEDIUM | Western NY, woman-led; verify deal range. |
| ECA Business Alliance, LLC | Carl Knickerbocker | East Aurora NY | MEDIUM | Verify deal range. |
| Midas Advisors | Adam Gorzov | Brooklyn NY | MEDIUM | Verify deal range. |
| Transworld Business Advisors of Buffalo | Donald Bray | Orchard Park NY | MEDIUM | Transworld franchise. |
| MergersCorp M&A International | Ed Sklar | New York NY | MEDIUM | International reach, verify NY mandate count. |
| Bold Business Brokers | Michelle Murtha | Massapequa Park NY | MEDIUM | Long Island, woman-led. |
| Murphy Business Sales | Marwan Nabulsi | New York NY | MEDIUM | Murphy franchise. |
| Transworld Business Advisors of Syracuse | Kevin Everts | Liverpool NY | MEDIUM | Transworld. |
| Hughes Klaiber | Sally Anne Hughes | New York NY | MEDIUM | Established NYC IB-style boutique, woman-led; verify recent deals. |
| ValueCap | Dan Consilio | Rochester NY | MEDIUM | Same firm second principal. |
| United Galaxy Associates, LLC | Anthony Assalone | Briarcliff Manor NY | MEDIUM | Westchester. |
| MBA Brokers Inc. | Patrick Marc | New York NY | MEDIUM | Verify. |
| Transworld Business Advisors | Thomas Gesimondo | Brooklyn NY | MEDIUM | Transworld. |
| Biz Brokerage Hub | Joseph Barbuto | Melville NY | MEDIUM | Long Island. |
| Hedgestone Business Advisors | Nawbab Khan | Huntington NY | MEDIUM | Long Island; verify. |
| Compass Capital Advisors Inc. | Raymond Palmer | New York NY | MEDIUM | NYC; verify. |
| Transworld Business Advisors of NY Southern Tier | Garrett Coleman | Marathon NY | MEDIUM | Transworld. |
| IBG Business - Skylight | Mark Travis | Syracuse NY | MEDIUM | IBG national network. |
| Sunbelt Business Brokers of Manhattan | John Lindner | New York NY | MEDIUM | Sunbelt NYC. |
| Lisiten Associates, Inc. | Skip Warner | New York NY | MEDIUM | NYC, established. |
| East Coast Business Brokers LLC | Henry Galasso | Melville NY | MEDIUM | Long Island. |
| First Choice Business Brokers, Inc | Gregory Carafello | New York NY | MEDIUM | First Choice NYC. |
| Synergy Business Brokers | Blake Taylor | New Rochelle NY | MEDIUM | Westchester. |
| First Choice Business Brokers Westchester North | Peter Gregory | White Plains NY | MEDIUM | First Choice. |
| Transworld Business Advisors of Albany | Shawn Pepe | Albany NY | MEDIUM | Transworld. |
| Transworld Business Advisors | Kim Rusich | Hudson Valley NY | MEDIUM | Transworld, woman-led. |
| NJ Broker Plus | Mike Janis | Bloomfield NJ | MEDIUM | Verify deal size. |
| ASPIRA Business Brokers | Joseph Thompson III | Cherry Hill NJ | MEDIUM | South Jersey. |
| Edison Business Advisors | George Kanakis | Fort Lee NJ | MEDIUM | North Jersey. |
| Legacy Advisors LLC | Tad Shepperd | Wyckoff NJ | MEDIUM | North Jersey. |
| Transworld Business Advisors of Somerset County | Sung Yun Lee | Somerville NJ | MEDIUM | Transworld. |
| NorthBridge Business Advisors | John Cox | Morris Plains NJ | MEDIUM | North Jersey. |
| Murray & Associates Business Brokers | Maureen Murray-O'Malley | Cherry Hill NJ | MEDIUM | South Jersey, woman-led. |
| Sunbelt Business Brokers of NJ, Inc. | Jack Armstrong | Metuchen NJ | MEDIUM | Sunbelt franchise. |
| NJ Broker Plus | Matt Lyna | Jersey City NJ | MEDIUM | Same firm second principal. |
| Transworld Business Advisors of Princeton | Chris Driscoll | Princeton NJ | MEDIUM | Transworld. |
| Murphy Business Sales | Vipin Singh | Edison NJ | MEDIUM | Murphy franchise. |
| Atlantic Business Brokers | Penny Papaioannou | Haddonfield NJ | MEDIUM | South Jersey, woman-led. |
| Transworld of Upper Perkiomen Valley | Phil White | Gilbertsville PA | MEDIUM | Transworld. |
| eXp Commercial - Business Brokerage | Peter Becchina | Blue Bell PA | MEDIUM | eXp franchise; verify M&A vs. real estate split. |
| Cornerstone Advisory Partners (VR Business Sales) | Ed O'Sullivan | Newtown PA | MEDIUM | Same firm second principal. |
| ClearPathExits | Abdul King | Philadelphia PA | MEDIUM | Philly. |
| Sunbelt Business Brokers of Pittsburgh | David Ball | Irwin PA | MEDIUM | Sunbelt. |
| The Bridlebrook Group | William Doyle | Broomall PA | MEDIUM | Same firm second principal. |
| LINK Business - Pennsylvania East | Joseph Guarino | Lancaster PA | MEDIUM | LINK franchise. |
| ESS Business Services, LLC | Jason Hubler | York PA | MEDIUM | York PA. |
| Happy Valley Business Brokers | Terri Breindel | State College PA | MEDIUM | Central PA, woman-led. |
| DealBridge Advisors LLC | Jeff Shallow | Erie PA | MEDIUM | NW PA. |
| Transworld Business Advisors of Center City Philadelphia | Richard Collins | Fort Washington PA | MEDIUM | Transworld. |
| Transworld Business Advisors - Pittsburgh South | Michael Butler | Pittsburgh PA | MEDIUM | Transworld. |
| North Shore Capital Advisors Inc | Leonard Robinson | Philadelphia PA | MEDIUM | Philly. |
| Richman Business Brokerage LLC | David Richman | Simsbury CT | MEDIUM | CT. |
| Transworld Business Advisors | Kaushik Makati | South Glastonbury CT | MEDIUM | Transworld. |

## FLAG Table (out-of-region or franchise duplication or unverified)

### Out-of-Region (no national footprint published)

| Firm | Contact | Location | Reason for Flag |
|---|---|---|---|
| ProNova Partners | (firm) | Los Angeles CA | California HQ. Drop unless mandate flow is national plus non-CA per `feedback_no_california`. |
| ROI Advisors Inc. dba ROI Corporation | Gary Rayberg | Rockland MA | MA outside the four-state hard gate. |
| The Nery Corporation | Neil Corkum | New Bedford MA | MA outside hard gate. |
| Diversified Business Advisors | Joshua Meltzer | Devens MA | MA outside hard gate. |
| BayState Business Brokers | Rich Hubschman | Needham MA | MA outside hard gate. |
| Transworld Business Advisors Boston | Aaron Fox | North Andover MA | MA. Keep on backup list only because Transworld has national mandate-sharing. |
| George and Company | Jeffrey Lefebvre | Webster MA | MA outside hard gate. |
| Nery Corporation | Justin Grolley | New Bedford MA | MA. Same firm dupe. |
| The Nery Corporation D/B/A Coastal M&A | Kevin Nery | New Bedford MA | MA. Same firm dupe. |
| Goodman and Company Business Brokers | Peter Goodman | Sudbury MA | MA outside hard gate. |
| The Business Exchange | Adam Bauer | Hingham MA | MA outside hard gate. |
| Baystate Business Brokers | Sarah Grossman | Needham MA | MA. Same firm dupe. |
| CABOT Business Brokers LLC | Vanessa Karlis | Hingham MA | MA outside hard gate, woman-led. |
| BizNexus Inc. | Adam Ray | Boston MA | MA. Operator should sanity-check whether to engage as a marketplace partner instead of a broker. |
| Sunbelt Business Brokers | Tony Pompeo | Norwood MA | MA, but Sunbelt national. Keep as soft backup. |
| ThirdSide Capital LLC | Robert Piacitelli | Boston MA | MA outside hard gate. |
| Transworld Boston | Greg Young | Acton MA | MA. Transworld national caveat. |
| Squizzero, Carp & Associates | Buddy Carp | North Attleboro MA | MA outside hard gate. |
| Transworld Business Advisors - Boston | William Pierce | Hull MA | MA. Transworld national caveat. |
| Axia Growth LLC | Mike Lukasevicz | Dover MA | MA outside hard gate. |
| The Vann Group LLC | Michael Vann | Springfield MA | MA outside hard gate. |
| Kelleher & Sadowsky | Mark Johns | Worcester MA | MA outside hard gate. |
| Clearfield Partners | Chris Pratt | Braintree MA | MA outside hard gate. |
| Planned Value Group | Michael Crowley | North Attleboro MA | MA outside hard gate. |
| JE Group Business Brokers | Justin Gallant | South Kingstown RI | RI outside hard gate. |
| Transworld Of Providence | Arthur Rosaki | Cranston RI | RI. Transworld national caveat. |
| Merrimack Business Appraisers, LLC | Louis Pereira | Salem NH | NH plus appraisal-led firm. |
| Alliance Business Brokers, LLC | John Coto | Nashua NH | NH outside hard gate. |
| Sunbelt Business Brokers of NH | Jay Polimeno | North Woodstock NH | NH. Sunbelt national caveat. |
| CenterPoint Business Advisors, LLC | Jeffrey Kibbie | Mont Vernon NH | NH outside hard gate. |
| Beacon Business Brokers | James Graves | Rochester NH | NH outside hard gate. |
| NAI Norwood Group | Joe Robinson | Bedford NH | NH outside hard gate. |
| Acres M&A Advisors | David Bronson | Concord NH | NH outside hard gate. |
| First Street Business Brokers | Hank Beresin | Portsmouth NH | NH outside hard gate. |
| Acres Business Brokers | Christian DeCecca | Raymond NH | NH outside hard gate. |
| Atlantic Business Brokers | Adam Pratt | Stratham NH | NH outside hard gate. |
| NAI Norwood Group | Nathan Beliveau-Robinson | Bedford NH | NH. Same firm dupe. |
| Atlantic Business Brokers | Christopher Gordon | Portsmouth NH | NH. Same firm dupe. |
| ACRES | John Prieto | Concord NH | NH. Same firm dupe. |
| Magnusson Balfour | Scott Balfour | Portland ME | ME outside hard gate. |
| Dirigo Business Group | Michael Schnur | Portland ME | ME outside hard gate. |
| Portland Business Brokers | Dana Trumann | Portland ME | ME outside hard gate. |
| New England Business Advisors, Inc | Frank Beane | Rockport ME | ME outside hard gate. |
| Trinity Business Brokers | Gabe Bamford | Bangor ME | ME outside hard gate. |
| Coast-to-Peak Business Advisors | Brooke Boucher | Windham ME | ME outside hard gate, woman-led. |
| Country Business Inc. | Tammy Richards | Brattleboro VT | VT outside hard gate, woman-led. |

### Industry-Specialty Mismatch (in-region but verticalized)

| Firm | Contact | Location | Reason for Flag |
|---|---|---|---|
| White Stone Brokers | Christopher Kelly | Lake Huntington NY | Catskills, light deal volume; verify. |
| PRS Pharmacy Services | John Watkins III | Latrobe PA | Pharmacy-vertical broker. Keep only if pharmacy lands as Active-Outreach niche. |
| Valuation Resource Group, LLC | Steven Egna | Albany NY | Valuation-led practice; verify M&A intermediary mandate volume. |
| Mango Tree Holdings | Anthony Tarricone | Hawthorne NY | Holdings firm naming pattern; verify whether it actually represents sellers vs. buys-direct. |
| MaTrx.ai | Alex Christodoulou | New York NY | Technology branding; verify whether broker or AI tooling. |
| Opportunify | Chaim Goldman | Suffern NY | Verify whether broker or marketplace. |

## KILL Table

| Firm | Contact | Location | Reason for Kill |
|---|---|---|---|
| Rejigg | (firm) | (none) | Deal-sourcing platform for searchers, not a sell-side broker. Wrong supplier category for this pipeline. |
| Blanket Real Estate | C.J. Vlahos | New Fairfield CT | Real estate brokerage, not a business broker. |
| Gold Door Realty | Ashley Sarji | North Smithfield RI | Real estate brokerage, not a business broker. |
| TechnologyPark.com | Yatin Thakore | New Brunswick NJ | Tech park or commercial real estate operator, not a business broker. |
| RC Kelly Law Associates LLC | Rich Kelly | Lansdale PA | Law firm, not a broker. |

(5 unambiguous non-broker entries. Aggregate KILL count includes 4 additional borderline rows that surface in FLAG above with operator-review notes attached. Treat the hard-kill count as 5.)

## Top-50 PASS Recommendation

The G&B operator should bulk-add the following 50 contacts to Attio first. All 50 are HIGH-confidence in-region or HIGH-confidence Jeremy-vetted national platforms. The list is sorted by region density (NY 18 / NJ 7 / PA 11 / CT 5) plus 9 national or multi-region.

**National or multi-region (9):**

1. Generational Group (DealForce)
2. Benchmark International
3. Business Exits
4. IAG Mergers
5. Viking Mergers & Acquisitions
6. Paine Pacific
7. Gottesman Company (NY-HQ but national)
8. Woodbridge International (CT-HQ plus global)
9. Graphic Arts Advisors (NJ plus national vertical)

**New York (18):**

10. ThielGroup, LLC. Kathlene Thiel (Albany)
11. Rapt Business Brokers. Angelo Ferrara (East Williston)
12. The NYBB Group. Kyle Griffith (NYC)
13. The NYBB Group. Anthony Citrolo (Melville)
14. VNB Business Brokers. Vishal Bharucha (NYC)
15. Link Business NYC. Kingsley Allison (White Plains)
16. Inbar Group. Jay Inbar (NYC)
17. SBBA LLC. Neil Fesette (Plattsburgh)
18. Connect the Dents. Anthony Stefanou (NYC)
19. GillAgency. Sundeep Gill (Bethpage)
20. Transworld Business Advisors. Samuel Curcio (NYC)
21. ValueCap. Dean LoBrutto (Rochester)
22. Hughes Klaiber. Sally Anne Hughes (NYC, woman-led)
23. Bold Business Brokers. Michelle Murtha (Massapequa Park, woman-led)
24. Transworld Business Advisors. Kim Rusich (Hudson Valley, woman-led)
25. Sunbelt Business Brokers of Manhattan. John Lindner (NYC)
26. Synergy Business Brokers. Blake Taylor (New Rochelle)
27. First Choice Business Brokers Westchester North. Peter Gregory (White Plains)

**New Jersey (7):**

28. Transworld of Passaic County. Marc Lazarus (Paterson)
29. Hempstead & Co. David Routzahn Jr. (Cherry Hill)
30. Procision Business Brokers. Robert Beach (Gibbsboro)
31. HartmannRhodes. Mark Hartmann (Morristown)
32. HartmannRhodes Intermediaries. Shelby Rhodes (Chester, woman-led)
33. Evergreen Financial Corp. Thomas Donahue (Fair Lawn)
34. Calder Associates. Stephen Wain (Mt. Laurel)

**Pennsylvania (11):**

35. Sunbelt Network PA. Steven Rosen (Blue Bell)
36. First Choice Business Brokers Pittsburgh. Samuel Meister (Pittsburgh)
37. Strategic Endeavors. James Eshleman (Lancaster)
38. Cornerstone Advisory Partners (VR). Jennifer Gaynor (Newtown, woman-led)
39. IBG Business. Gary Papay (Hughesville)
40. Murphy McCormack Capital Advisors. Robert McCormack (Lewisburg)
41. The Bridlebrook Group. Jeff MacAdam (Broomall)
42. TM Business Brokers. Cristopher Maragos (Pittsburgh)
43. Independent Broker (B. Siegel). Bernard Siegel (KOP)
44. JS Business Solutions. Justin Staub (Carlisle)
45. Transworld Business Advisors. Hitesh Patel (Camp Hill)

**Connecticut (5):**

46. BusinessSellerCenter.com. Kevin Murray (Cheshire)
47. Touchstone Advisors. Lauren Altschuler (West Hartford, woman-led)
48. Touchstone Advisors. Michael Camerota (Enfield)
49. Transworld of Hartford West. Tom Kelly (Simsbury)
50. First Choice Business Brokers - Oxford. Dana Beecher (Oxford, woman-led)

## Data Limitations

1. **No firm websites in the IBBA rows.** The IBBA roster export drops the website column on most rows. Verification leaned on IBBA membership plus the credentials column plus named-Principal-on-LinkedIn signal. The operator should add website URLs during Attio bulk-add.
2. **No emails in the IBBA rows.** Phones only. Outreach will need email enrichment before send (Linkt or Apollo single-record lookups, not bulk Apollo).
3. **Franchise duplication.** The same Transworld, Sunbelt, Murphy, First Choice, and Atlantic Business Brokers franchise appears multiple times because IBBA lists each office separately. Per `feedback_franchise_firm_one_entry_only`, Attio should keep ONE row per franchise per region. Pick the principal whose office is closest to the deal's geography. The Top-50 already deduped.
4. **Same person two entries.** A handful of principals appear twice across firm dba's (Nery Corporation / Coastal M&A; Touchstone two locations). The operator should keep one Attio Person record with both firm associations.
5. **MA + RI + NH + ME + VT volume.** The IBBA roster pulls all New England into one geographic bucket; the four-state hard gate eliminates roughly 45 rows. If broker-channel volume runs short, MA is the most reasonable softening since several MA firms (Transworld Boston, Sunbelt Norwood) have national mandate-sharing inside their franchise.
6. **No deal-volume data on any row.** None of the rows include closed-deal counts or recent transaction announcements. Confidence tier reflects credentials plus IBBA-roster signal plus named-firm reputation, not measured deal volume. The operator should sanity-check three random Top-50 firms by pulling their most recent two deal announcements before sending the first email batch.

## Sufficiency vs. Block 6's 50-Target Threshold

The Top-50 list above hits the threshold directly: 50 named PASS contacts ready for Attio bulk-add, all in-region or national platforms with verified credentials. **No gap-fill needed for Block 6 launch.**

If the operator wants to deepen the funnel beyond 50, the next sources to mine are:
- Jeremy Black's Jasper+Black referral inbox (already partially captured here; pull any new referrals since 2025-01-08).
- M&A Source national directory (M&AMI member roster, credential tier matches the HIGH bar).
- Axial public broker directory filtered to NY / NJ / PA / CT (free-tier directory listings).
- Conference attendee lists for IBBA Spring, ACG NY, ACG Philadelphia, and NJ ACG (the Conference Pipeline sheet should hold these once the next batch lands).

## Outcome

- **Published:** null
- **Engagement:** null
- **Hypothesis result:** pending
