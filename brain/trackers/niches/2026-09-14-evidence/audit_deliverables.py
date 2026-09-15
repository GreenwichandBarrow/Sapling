import json,pathlib,shutil,hashlib,re
from openpyxl import load_workbook
from pptx import Presentation
b=pathlib.Path('/tmp/niche-intel-2026-09-14');dur=pathlib.Path('brain/trackers/niches/2026-09-14-evidence');dur.mkdir(exist_ok=True,parents=True)
d=json.load(open(b/'scores.json'));records=[]
for n in d['niches']:
 nd=dur/n['slug'];nd.mkdir(exist_ok=True)
 paths={}
 for kind,key in [('pptx','pptx_local_path'),('xlsx','xlsx_local_path')]:
  origin=pathlib.Path(n[key]);dest=nd/origin.name;shutil.copy2(origin,dest);assert origin.read_bytes()==dest.read_bytes();paths[kind]=dest
 w=load_workbook(paths['xlsx'],data_only=True);f=load_workbook(paths['xlsx'],data_only=False);s=w['Industry Scorecard'];sf=f['Industry Scorecard']
 assert len(n['criteria'])==27 and len(n['categories'])==8
 for c in n['criteria']:
  assert s[f"D{c['row']}"].value==c['numeric_score'];assert s[f"E{c['row']}"].value==c['rating'];assert sf[f"D{c['row']}"].data_type=='f'
 total=0
 for cat in n['categories']:
  row=cat['row'];v=s[f'C{row}'].value;assert abs(v-cat['score'])<1e-10;assert s[f'D{row}'].value==cat['weight'];total+=v*cat['weight']
 assert abs(total-n['score'])<1e-10 and abs(s['C43'].value-n['score'])<1e-10
 assert sf['C43'].value=='=SUMPRODUCT(C8:C42,D8:D42)'
 assert all(c.value is None for row in sf.iter_rows(min_row=45) for c in row)
 assert all('#REF!' not in str(c.value) for row in sf for c in row)
 pp=Presentation(paths['pptx']);assert len(pp.slides[0].shapes)==6
 table=next(sh.table for sh in pp.slides[0].shapes if sh.has_table);assessment=table.cell(1,0).text;assert f"{n['score']:.2f} / 3.0" in assessment
 assert 'incomplete' in table.cell(1,1).text.lower()
 links=[]
 for sl in pp.slides:
  for sh in sl.shapes:
   if sh.has_text_frame:
    links += [run.hyperlink.address for para in sh.text_frame.paragraphs for run in para.runs if run.hyperlink.address]
 manifest=json.load(open(b/('onepager-calibration.json' if n['slug'].startswith('dimensional') else 'onepager-dairy.json')))
 missing=[x['url'] for x in manifest['sources'] if x['url'] not in links];assert not missing,missing
 assert not any(url.startswith('/tmp/') for url in links)
 records.append({'slug':n['slug'],'score':n['score'],'cached_score':s['C43'].value,'pptx_assessment':assessment,'criteria_verified':27,'categories_verified':8,'pptx_slides':len(pp.slides),'template_shapes_preserved':6,'manifest_sources':len(manifest['sources']),'missing_source_links':missing,'hyperlink_count':len(links),'source_links_complete':True,'durable_files':{k:str(v) for k,v in paths.items()},'sha256':{k:hashlib.sha256(v.read_bytes()).hexdigest() for k,v in paths.items()},'drive_folder':n['drive_folder'],'folder_verified_exact_one_each':n['folder_verified']})
for name in ['scores.json','identified.json','build_scorecards.py','audit_deliverables.py','onepager-calibration.json','onepager-dairy.json','active-sprints-parent.json']:
 shutil.copy2(b/name,dur/name)
shutil.copy2(b/'scored-summary.md',dur/'scored-summary.txt')
shutil.copy2(b/'deliverable-preflight.md',dur/'deliverable-preflight.txt')
for n in d['niches']:
 name=n['slug']+'-postscore-files.json';shutil.copy2(b/name,dur/name)
audit={'run_date':'2026-09-14','runtime':'Codex/systemd','status':'passed','one_pagers_written':2,'scorecards_written':2,'niches_scored':2,'all_formula_caches_verified':True,'all_pptx_scores_match':True,'all_sources_linked':True,'all_folders_exact_one_each':True,'verification':'Local copies refreshed from final scored artifacts, SHA256 identical;27 cached criteria/eight category scores/weighted total each compared independently against scores.json; PPTX assessment and source manifests verified. External folder listings preserved from post-write verification.','niches':records}
path=dur/'deliverable-audit.json';path.write_text(json.dumps(audit,indent=2));print(path);print(json.dumps({k:audit[k] for k in ['status','one_pagers_written','scorecards_written','all_formula_caches_verified','all_sources_linked']}))
