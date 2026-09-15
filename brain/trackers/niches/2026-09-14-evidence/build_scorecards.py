import json,pathlib,zipfile,xml.etree.ElementTree as ET,copy,shutil
from openpyxl import load_workbook
from openpyxl.worksheet.formula import ArrayFormula
from openpyxl.styles import Alignment,Font
from pptx import Presentation
from pptx.util import Pt
from pptx.dml.color import RGBColor
b=pathlib.Path('/tmp/niche-intel-2026-09-14');niches=json.load(open(b/'identified.json'))['niches']
groups=[(8,[9,10,11,12],.25),(13,[14,15],.10),(16,[17,18,19],.10),(20,[21,22,23],.15),(24,[25,26,27,28,29],.10),(30,[31,32,33,34,35,36],.15),(37,[38,39],.10),(40,[41,42],.05)]
rows=[r for _,rs,_ in groups for r in rs]
policy='Provisional evidence-weighted research score, not an activation decision. Missing quantitative facts receive - (1) as an uncertainty penalty, not a measured adverse result. +/- (2) and + (3) express explicit source-supported judgments; operator claims are labeled. Unknown initial-screen facts remain Unknown. Template category weights and rating mapping unchanged. Target TAM and G&B fit are informational, not extra weighted score inputs.'
cal={9:(1,'Unknown exact dimensional-service CAGR. Broad Transcat company growth is not market growth. C6/C7'),10:(2,'Judgment: repeat quality/documentation work is a potential catalyst; penetration unknown. C1/C2/C8/C9'),11:(2,'Judgment: precision requirements supportive; competing in-house/OEM options and unverified niche outlook temper tailwinds. C6/C8/C11'),12:(2,'Provider records and corporate demand establish need, not a quantified catalyst for this precise niche. C1/C2/C6'),14:(1,'Unknown independent national population. Three ownership claims among five examples are not market size. C1-C5/C10'),15:(1,'Unknown largest-player share; consolidation proves presence, not concentration percentage. C5/C11'),17:(1,'Unknown typical niche gross margin. Broad-company service gross margin33.4% is only a proxy. C6'),18:(1,'Unknown typical niche EBITDA margin; no public peer sample. C6/C7'),19:(1,'Unknown typical industry return on tangible capital; reference equipment requires investment. No measured ROTC.'),21:(1,'No independently collected representative customer feedback. Provider testimonials not an industry survey. C1/C2'),22:(3,'Judgment: trustworthy dimensional measurement and certificates directly support manufacturing quality decisions. C3/C8/C9'),23:(2,'Judgment: replacing a qualified lab requires scope/quality and records checks but alternatives exist. C1/C2/C9'),25:(2,'Judgment: physical measurement and repair protected from text automation; documentation/productivity tools changing. C2/C6'),26:(2,'Judgment: accreditation/quality requirements support demand but require continuing technical compliance. C8/C9'),27:(2,'Judgment: bad measurements may propagate quality errors; liability is material and not measured. C8'),28:(2,'Judgment: repeat measurement persists but manufacturing volumes/capex are cyclical. C1/C6'),29:(3,'Judgment: physical measurement confidence is durable across product fashions. C8/C9'),31:(1,'Unknown prevalence of VC-backed startups; PE examples do not prove absence. C5/C11'),32:(1,'Judgment: established national and sponsor-backed buyers compete with local labs. C5/C6/C11'),33:(2,'Judgment: accreditation/technical standards constrain entry without preventing local providers. C1/C9'),34:(2,'Judgment: standards/equipment and specialist labor needed; no evidence of extreme supplier concentration. C1/C8/C9'),35:(2,'Judgment: manufacturing buyers can qualify alternatives; trust and turnaround moderate bargaining power. C1/C2'),36:(2,'Judgment: OEM/in-house calibration substitutes for third-party work; trust/capability differentiates. C6'),38:(2,'Judgment: specialist metrology and quality systems create moderate technical complexity. C1/C9'),39:(2,'Judgment: repeat scheduling, certificate records and turnaround are tangible process levers; not a proven turnaround plan. C1/C2'),41:(3,'Judgment: reliable measurements support product quality and safety. C8/C9'),42:(2,'Judgment: quality benefits possible; no measured environmental/social externality study. C8/C9')}
dairy={9:(1,'Unknown current service-market CAGR;2016-21 robot adoption is not service growth. D1'),10:(3,'Judgment: independently measured historic automation uptake expands installed technical support needs. D1/D2'),11:(2,'Judgment: automation supportive, but farm consolidation/financial conditions may offset dealer expansion. D1/D10'),12:(3,'USDA primary evidence of adoption plus observed maintenance providers establish installed-base catalyst; old-data limitation explicit. D1/D3/D5'),14:(1,'Unknown independent national vendor count;39 OEM directory locations are not39 firms. D2'),15:(1,'Unknown service-provider market shares. OEM dealer territories not measured concentration. D2'),17:(1,'Unknown typical standalone service gross margins; product/dealer mix differs. D11'),18:(1,'Unknown typical service EBITDA; one anonymous17.7% dealer listing is not industry proof. D11'),19:(1,'Unknown industry ROTC; spares/vehicles/working capital vary. D3/D5'),21:(1,'No independent representative customer-feedback dataset; vendor descriptions are not satisfaction measurements. D3/D5'),22:(3,'Judgment: robot uptime and hygiene support continuing milking operations. D5/D9'),23:(2,'Judgment: local trained technicians and installed OEM systems create switching effort; provider contracts unknown. D2/D5/D7'),25:(2,'Judgment: robot complexity/software evolves; hands-on repair persists. D2/D5'),26:(2,'Judgment: hygiene and machine-service protocols create ongoing obligations; no specific new legal claim. D5/D9'),27:(1,'Judgment: service failures threaten herd/milk quality and uptime; significant liability and emergency coverage. D5/D9'),28:(2,'Judgment: installed servicing persists but farm financial cycles can pressure spend and losses. D1/D5'),29:(2,'Judgment: automation trend supports demand but equipment/commodity customer exposure persists. D1/D2'),31:(1,'Unknown VC provider prevalence; cannot infer absence from directory. D2/D10'),32:(2,'Judgment: regional service territories/local response differentiate, but OEM dealers compete; pricing data unknown. D2/D3/D5'),33:(2,'Judgment: certification, parts and local technician footprint limit entry. D2/D7'),34:(1,'Judgment: OEM parts/software/training and dealer consent create supplier power. D2/D7'),35:(2,'Judgment: downtime makes service critical; concentrated farm/customer dependence not measured. D5/D9'),36:(2,'Judgment: trained farm staff can do daily care, but faults/parts still need specialist support. D9'),38:(1,'Judgment:24/7 rural dispatch, technical staff, spares and robot protocols are complex. D5/D9'),39:(2,'Judgment: planned service agreements and routes offer levers but flat-fee repair risks must be priced. D5/D9'),41:(2,'Judgment: labor support/uptime benefit farms; broader environmental/welfare outcomes not established. D1'),42:(2,'Unknown net externality; no quantified effect inferred from dairy automation. D1')}
results=[]
for idx,(n,ratings) in enumerate(zip(niches,[cal,dairy])):
 assert set(ratings)==set(rows)
 key='calibration' if idx==0 else 'dairy';m=json.load(open(b/f'onepager-{key}.json'))
 folder=m.get('folder_id',m.get('drive_folder'));outname=('Dimensional Metrology and Gauge Calibration' if idx==0 else 'Robotic-Milking Maintenance and Consumables')+' Scorecard September 2026.xlsx';path=b/outname
 w=load_workbook('brain/library/internal/scorecard/G&B Industry & Company Scorecard Template.xlsx');s=w['TEMPLATE'];s.title='Industry Scorecard';s.delete_rows(45,55)
 for name in list(w.defined_names):del w.defined_names[name]
 w.properties.title=n['name']+' — Industry Scorecard';w.properties.subject='Provisional industry evaluation';w.properties.creator='G&B / Codex';w.properties.lastModifiedBy='G&B / Codex';w.properties.description=policy
 sc=w['INITIAL SCREEN'];sc['B3']=n['name']
 for r,k in [(6,'margins'),(7,'recurring_revenue'),(8,'industry_growth'),(9,'growth_tam')]:
  sc[f'C{r}']=n['initial_screen'][k]['status'];sc[f'E{r}']=n['initial_screen'][k]['evidence']
 sc['D11']='INCOMPLETE — review only';sc['E11']='Missing facts not forced to Pass; no activation.';sc['C14']='Unknown';sc['E14']=n['target_tam']['target_pool_text'];sc['C15']='Unassigned';sc['E15']='Directory/examples do not establish acquisition-ready pool.'
 for row in sc:
  for c in row:c.alignment=Alignment(wrap_text=True,vertical='top')
 sc.column_dimensions['B'].width=45;sc.column_dimensions['C'].width=18;sc.column_dimensions['D'].width=42;sc.column_dimensions['E'].width=90
 for r in [6,7,8,9,14]:sc.row_dimensions[r].height=55
 sc.row_dimensions[3].height=45
 s['B3']=n['name'];s['B5']='G&B INDUSTRY SCORECARD';s['F10']=None;s['D43']='Provisional; see methodology. /3 scale.'
 s['D34']=ArrayFormula(ref='D34',text='=_xlfn.SWITCH(E34,"+",3,"+/-",2,"-",1)')
 criteria=[];cache={}
 for r,(rating,note) in ratings.items():
  mark={1:'-',2:'+/-',3:'+'}[rating];s[f'E{r}']=mark;s[f'J{r}']=note;cache[f'D{r}']=rating
  criteria.append({'row':r,'criterion':s[f'B{r}'].value,'rating':mark,'numeric_score':rating,'evidence':note})
 categories=[]
 for row,subs,weight in groups:
  avg=sum(ratings[r][0] for r in subs)/len(subs);cache[f'C{row}']=avg;categories.append({'row':row,'category':s[f'B{row}'].value,'weight':weight,'score':avg,'weighted_score':avg*weight})
 score=sum(c['weighted_score'] for c in categories);cache['C43']=score
 s.row_dimensions[3].height=45;s.column_dimensions['J'].width=90
 for row in s.iter_rows(min_row=8,max_row=42):
  for c in row:c.alignment=Alignment(wrap_text=True,vertical='top')
  s.row_dimensions[row[0].row].height=52 if row[0].row in rows else 26
 meta=w.create_sheet('Methodology and Sources');meta.append(['Policy',policy]);meta.append(['Repair','Output-only D34 mapped-rating formula restored; template missing supplier-power numeric rating. Original template unchanged.']);meta.append(['Scope','Eight groups,27 subcriteria. Company examples rows45:99 removed. Target TAM/searcher fit informational.']);meta.append(['Formula caches','Preserved original industry formulas; numeric caches injected and independently verified because local LibreOffice Calc unavailable.']);meta.append(['Scale','C43 SUMPRODUCT already /3; percentage=score/3*100.']);meta.append(['Initial screen',n['initial_screen']['verdict']]);meta.append(['Source ID','Title / evidence','URL'])
 for source in n['sources']:
  u=source['url']
  if u.startswith('/tmp/'):u='brain/traces/agents/2026-09-14-niche-intelligence.md'
  meta.append([source['id'],source['title']+' — '+source['evidence'],u]);meta.cell(meta.max_row,3).hyperlink=u;meta.cell(meta.max_row,3).style='Hyperlink'
 meta.column_dimensions['A'].width=24;meta.column_dimensions['B'].width=115;meta.column_dimensions['C'].width=65
 for row in meta:
  for c in row:c.alignment=Alignment(wrap_text=True,vertical='top')
  meta.row_dimensions[row[0].row].height=65
 w.save(path)
 ns={'m':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
 with zipfile.ZipFile(path) as z:parts={i.filename:z.read(i.filename) for i in z.infolist()}
 tree=ET.fromstring(parts['xl/worksheets/sheet2.xml'])
 for cell in tree.findall('.//m:c',ns):
  addr=cell.attrib['r']
  if addr in cache:
   assert cell.find('m:f',ns) is not None,addr
   val=cell.find('m:v',ns)
   if val is None:val=ET.SubElement(cell,'{'+ns['m']+'}v')
   val.text=repr(cache[addr])
 parts['xl/worksheets/sheet2.xml']=ET.tostring(tree,encoding='utf-8',xml_declaration=True)
 with zipfile.ZipFile(path,'w',zipfile.ZIP_DEFLATED) as z:
  for name,data in parts.items():z.writestr(name,data)
 check=load_workbook(path,data_only=True)['Industry Scorecard'];formula=load_workbook(path,data_only=False)['Industry Scorecard']
 for addr,val in cache.items():assert abs(check[addr].value-val)<1e-10,(addr,check[addr].value,val)
 assert formula['C43'].value=='=SUMPRODUCT(C8:C42,D8:D42)'
 assert abs(sum(check[f'C{r}'].value*check[f'D{r}'].value for r,_,_ in groups)-score)<1e-10
 pp=Presentation(m['local_path']);t=next(sh.table for sh in pp.slides[0].shapes if sh.has_table)
 for ci,text in [(0,f'Assessment: {score:.2f} / 3.0 ({score/3:.0%})'),(1,'Pending analyst review | Screen incomplete')]:
  tf=t.cell(1,ci).text_frame;para=tf.paragraphs[0];rr=para.runs[0] if para.runs else para.add_run();rr.text=text
  for extra in list(para.runs)[1:]:extra.text=''
  for extra in list(tf.paragraphs)[1:]:extra._p.getparent().remove(extra._p)
  rr.font.size=Pt(10);rr.font.color.rgb=RGBColor(0,0,0)
 # Add methodology citation to last Sources slide (spare lower space).
 from pptx.util import Inches
 box=pp.slides[-1].shapes.add_textbox(Inches(.4),Inches(8.8),Inches(6.6),Inches(.8));para=box.text_frame.paragraphs[0];rr=para.add_run();rr.text='Scoring: provisional evidence-weighted industry assessment. Missing facts penalized, not asserted adverse facts. Full methodology and criteria in companion scorecard.';rr.font.size=Pt(9);rr.font.color.rgb=RGBColor(35,35,35)
 pp.save(m['local_path'])
 results.append({'name':n['name'],'slug':n['slug'],'score':score,'score_display':round(score,2),'score_percent':score/3*100,'categories':categories,'criteria':criteria,'initial_screen':n['initial_screen'],'target_pool':n['target_tam']['target_pool_text'],'target_tam':n['target_tam'],'margins':'Unknown','recurring_revenue':'Repeat service supported; contracted share unknown','ai_defensibility':'Medium/High physical service; documentation automation possible','right_to_win':n['searcher_fit']['rating'],'network_access':'No verified warm owner path','qsbs':'Unverified','recommendation':'Review only; no activation','channel':n['channel'],'risks':n['risks'],'section':n['section'],'xlsx_local_path':str(path),'pptx_local_path':m['local_path'],'pptx_file_id':m['file_id'],'pptx_url':m['file_url'],'drive_folder':folder,'drive_folder_url':'https://drive.google.com/drive/folders/'+folder,'scorecard_uploaded':False,'pptx_updated':False,'sources':n['sources']})
json.dump({'run_date':'2026-09-14','scoring_policy':policy,'category_count':8,'subcriteria_count':27,'niches':results},open(b/'scores.json','w'),indent=2)
print([(r['slug'],r['score_display'],len(r['criteria'])) for r in results])
