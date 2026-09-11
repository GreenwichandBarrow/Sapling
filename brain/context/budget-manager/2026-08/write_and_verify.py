import json, subprocess, pathlib, datetime, shutil
P=pathlib.Path('/tmp/budget-manager-2026-08'); D=pathlib.Path('brain/context/budget-manager/2026-08');D.mkdir(parents=True,exist_ok=True)
S='1vTeGviuQk9zLqacJrdBZS2Bopk8kQZtmEHWheqpCdq0'
plan=json.loads((P/'write-plan.json').read_text())
def get(r,render='FORMATTED_VALUE'):
 return json.loads(subprocess.check_output(['gog','sheets','get',S,r,'--json','--render',render],text=True))
def padded(v,h,w):return [(v[i] if i<len(v) else [])[:w]+['']*(w-len((v[i] if i<len(v) else [])[:w])) for i in range(h)]
def norm(v):
 if v is None:return ''
 try:return float(str(v).replace(',','').replace('$',''))
 except:return v
stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%SZ')
pre=[get(p['range']) for p in plan]
# Read-only reconciliation source must remain unchanged.
for idx,name,h,w in [(0,'live-tab1.json',39,24),(2,'live-tab2.json',80,6)]:
 old=json.loads((P/name).read_text())['values'];new=pre[idx].get('values') or []
 assert padded(old,h,w)==padded(new,h,w), 'Live reconciliation assumptions changed: '+name
assert not any(any(c not in ('',None) for c in row) for row in (pre[1].get('values') or [])), 'Category destination occupied'
assert not any(any(c not in ('',None) for c in row) for row in (pre[2].get('values') or [])[80:]), 'Runway extension occupied'
R=pathlib.Path('brain/context/rollback-snapshots')/f'budget-dashboard-2026-08-{stamp}.json';R.parent.mkdir(parents=True,exist_ok=True)
R.write_text(json.dumps({'period':'2026-08','sheet_id':S,'captured_at':stamp,'ranges':pre},indent=2))
(D/'rollback-path.json').write_text(json.dumps({'path':str(R)}))
for i,p in enumerate(plan):
 # Fresh target fetch directly precedes each update; compare with saved pre-write snapshot.
 now=get(p['range']);assert (now.get('values') or [])==(pre[i].get('values') or []),'Concurrent edit before '+p['range']
 width=[24,8,6][i];vals=padded(p['values'],len(p['values']),width);vals=[[('' if x is None else x) for x in row] for row in vals]
 result=subprocess.check_output(['gog','sheets','update',S,p['range'],'--values-json',json.dumps(vals),'--input','RAW','--json'],text=True)
 (D/f'write-{i+1}.json').write_text(result)
post=[get(p['range'],'UNFORMATTED_VALUE') for p in plan]
checks=[]
for i,(p,live) in enumerate(zip(plan,post)):
 width=[24,8,6][i];a=padded(p['values'],len(p['values']),width);b=padded(live.get('values') or [],len(a),width)
 mismatches=[(r+1,c+1,a[r][c],b[r][c]) for r in range(len(a)) for c in range(width) if norm(a[r][c])!=norm(b[r][c])]
 checks.append({'range':p['range'],'cells_checked':len(a)*width,'mismatches':mismatches,'passed':not mismatches})
(D/'post-write-live.json').write_text(json.dumps(post,indent=2));(D/'cell-validation.json').write_text(json.dumps(checks,indent=2))
assert all(x['passed'] for x in checks),checks
for f in P.iterdir():
 if f.is_file():shutil.copy2(f,D/f.name)
print(json.dumps({'rollback':str(R),'cell_validation':checks}))
