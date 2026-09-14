import calendar
import copy
import hashlib
import json
import math
from pathlib import Path
import sys

sys.path.insert(0, '/home/ubuntu/projects/Sapling/scripts')
from task_tracker import SheetsClient as PythonSheetsClient

root = Path(__file__).parent
prior = '2026-09-14-budget-subscriptions-v3'
prefix = '2026-09-14-budget-subscriptions-v4'
def read(name):
    return json.loads((root / name).read_text())
def save(suffix, data):
    (root / (prefix + suffix)).write_text(json.dumps(data, indent=2) + '\n')
def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()
originals = {str(p): digest(p) for p in root.glob('2026-09-*-budget-*')}
assert not (root / (prefix + '-calculations.json')).exists()
m = read(prior + '-calculations.json')
old = read(prior + '-cash-ledger.json')
fields = ['other_allowance', 'payroll', 'insurance', 'health', 'dealsx', 'conference', 'website']
def cost(d):
    return sum(d[k] for k in fields)
cash = m['cash']['total']
ledger = copy.deepcopy(old)
savings = 0
for d in ledger:
    year, month, _ = map(int, d['date'].split('-'))
    saving = 24.72 / calendar.monthrange(year, month)[1] if d['date'] >= '2026-09-14' else 0
    savings += saving
    d['other_allowance'] -= saving
    cash -= cost(d)
    d['end_cash'] = cash
assert ledger[:13] == old[:13]
assert abs(savings - 24.72 * (17/30 + 4 + 7/28)) < 1e-8
for a, b in zip(old, ledger):
    assert all(a[k] == b[k] for k in fields if k != 'other_allowance')
outflows = sum(cost(d) for d in ledger)
gap = outflows + m['cash']['dd_reserve'] - m['cash']['total']
m.pop('validation', None)
m.update(version=4, status='calculated; live verification pending')
for k in ['normalized_monthly_burn_unrounded', 'halfpay_monthly_equivalent_unrounded']:
    m[k] -= 24.72
m['normalized_monthly_burn'] = round(m['normalized_monthly_burn_unrounded'], 2)
m['normalized_other_monthly_allowance'] = 1032.17
for k in ['full_monthly_unrounded', 'halfpay_monthly_unrounded', 'other_monthly_allowance']:
    m['after_pause'][k] -= 24.72
note = 'Art Newspaper cancellation confirmed by user September14. Remove24 subscription plus0.72 bank fee monthly from September14 modeled current date; no past refund or retroactive savings. DocSend remains canceled. Howie no-charge pause Sep14-Dec13 assumed; UNVERIFIED35 allowance resumes Dec14, not confirmed billing.'
m['halfpay_rounding_note'] = 'During pause full18622.796667; hypothetical half11221.853333. From Dec14 full18657.796667; half11256.853333 includes UNVERIFIED Howie35 allowance, not confirmed actual billing. Weekly employer cash3415.82 unchanged.'
sc = m['subscription_changes']
sc['newspaper'] = dict(status='canceled; user confirmed', monthly=0, bank_fee=0, retained=False, effective='2026-09-14', effective_basis='modeled current date', removed_monthly=24, removed_bank_fee=0.72, past_refund=0)
for k in ['monthly_reduction_during_pause', 'monthly_reduction_after_pause']:
    sc[k] = round(sc[k] + 24.72, 2)
sc['september_savings'] = round(sc['september_savings'] + 24.72*17/30, 2)
sc['horizon_savings'] = round(sc['horizon_savings'] + savings, 2)
for k in ['total_monthly', 'total_monthly_after_howie_pause']:
    m['approved_changes'][k] = round(m['approved_changes'][k]+24.72, 2)
for k, value in [('september_savings',24.72*17/30), ('horizon_savings',savings)]:
    m['approved_changes'][k] = round(m['approved_changes'][k]+value, 2)
m['approved_changes']['subscription_changes'] = sc
m['normalized_bridge'].append(['Art Newspaper canceled; subscription24 plus bank fee0.72 removed September14', -24.72])
m['timed'].update(other_total=round(sum(d['other_allowance'] for d in ledger),2), total_outflows=round(outflows,2), shortfall_to_protected_reserve=round(gap,2), unfunded_end_cash=round(cash,2), first_reserve_breach=next(d['date'] for d in ledger if d['end_cash'] < m['cash']['dd_reserve']), approved_cut_cash_savings=m['approved_changes']['horizon_savings'], incremental_subscription_cash_savings=sc['horizon_savings'], incremental_newspaper_cash_savings=round(savings,2))
m['monthly_gap_to_target'] = round(gap/m['timed']['approved_savings_month_equivalents'],2)
m['normalized_runway_months_comparison'] = round(m['cash']['operations_before_commitments']/m['normalized_monthly_burn_unrounded'],2)
factor = m['payroll']['incremental_savings_factor']
for s in m['scenarios']:
    needed = gap-s['health_cash_savings']
    weekly = needed/s['reduced_payments']/factor
    exact = weekly*52/12
    s.update(gross_monthly_cut_exact=exact, gross_monthly_cut=round(exact,2), gross_monthly_remaining=round(m['payroll']['weekly_gross']*52/12-exact,2), gross_cut_percent=round(weekly/m['payroll']['weekly_gross']*100,2), weekly_cut_rounded_up=math.ceil(weekly*100)/100, gross_monthly_cut_no_employer_tax_savings=round(needed/s['reduced_payments']*52/12,2), employer_tax_savings_monthly=round(exact*(factor-1),2))
    s['weekly_gross_remaining'] = round(m['payroll']['weekly_gross']-s['weekly_cut_rounded_up'],2)
    assert abs(cash+weekly*factor*s['reduced_payments']+s['health_cash_savings']-38000)<1e-7
for a in m['alternating_paychecks']:
    balance = m['cash']['total']
    breach = None
    for d in ledger:
        balance -= cost(d)
        if d['date'] in a['skipped_dates']:
            balance += d['payroll']
        if breach is None and balance < 38000:
            breach = d['date']
        if d['date'] == '2027-01-23':
            a.update(jan23_cash=round(balance,2), jan23_reserve_shortfall=round(38000-balance,2))
    a.update(ending_cash=round(balance,2), reserve_shortfall=round(38000-balance,2), first_reserve_breach=breach)
for h in m['health_only']:
    h['residual_gap'] = round(gap-h['total_maximum'],2)
m['assumptions'][0] += ' V4 removes newspaper24 and fee0.72 from September14, no refund.'
m['assumptions'][3] = m['assumptions'][3].replace('1056.89','1032.17').replace('1091.89','1067.17')
m['assumptions'][7] = note+' Voice10 and Slack15 unverified allowances retained; Voice may overlap Workspace.'
m['assumptions'][12] = m['halfpay_rounding_note']
m['pending_cancellations'] = []
for x in m['monthly_itemization']:
    if x['item'] == 'Art Newspaper':
        x.update(monthly=0, basis=note)
    if x['item'] == 'Bank fees':
        x.update(monthly=3.09, basis='Allowance after removal of newspaper0.72 fee September14; historical fees unchanged')
for x in m['inventory_audit']:
    if x['tool'] == 'The Art Newspaper':
        x.update(status='CANCELED', monthly_equivalent=0, evidence=note)
assert abs(sum(x['monthly'] for x in m['monthly_itemization'])-m['normalized_monthly_burn_unrounded'])<1e-8
assert abs(m['normalized_monthly_burn_unrounded']-18622.796667)<1e-6
assert abs(m['halfpay_monthly_equivalent_unrounded']-11221.853333)<1e-6
sheet = '1vTeGviuQk9zLqacJrdBZS2Bopk8kQZtmEHWheqpCdq0'
c = PythonSheetsClient(sheet)
ranges = {'runway': "'Runway Forecast'!A1:Z", 'tech': "'Tech Stack Inventory'!A1:Z100"}
def fetch():
    return {k: {'values': c.get_values(v)} for k,v in ranges.items()}
before = fetch()
save('-prewrite.json', before)
values = copy.deepcopy(before['runway']['values'])
def setcell(r,col,v):
    while len(values[r-1])<col:
        values[r-1].append('')
    values[r-1][col-1]=str(v)
def b(r,v):
    setcell(r,2,v)
b(3,'Aug31 VERIFIED cash; Sep14 subscription v4 MODEL; no September feed')
for r in [7,25,30,78]: b(r,m['normalized_monthly_burn'])
for r in [8,31]: b(r,m['normalized_runway_months_comparison'])
for r in [9,32]: b(r,m['timed']['first_reserve_breach'])
for r in [10,47]: b(r,round(gap,2))
for r in [11,34]: b(r,m['monthly_gap_to_target'])
b(12,'August bank statements + v3 model + user-confirmed Art Newspaper cancellation Sep14')
b(13,note+' Prior cuts retained; historical actuals unchanged.')
setcell(41,1,'Other allowance:2798.12 to Sep13;1032.17 Sep14-Dec13;1067.17 Dec14 onward')
b(41,m['timed']['other_total'])
b(45,m['timed']['total_outflows'])
for i,s in enumerate(m['scenarios']):
    for j,k in enumerate(['gross_monthly_cut','gross_monthly_remaining','employer_tax_savings_monthly','health_cash_savings','first_reduced_payment','reduced_payments']): setcell(51+i,2+j,s[k])
for i,a in enumerate(m['alternating_paychecks']):
    for j,k in enumerate(['skipped_count','retained_count','savings','ending_cash','reserve_shortfall','first_reserve_breach']): setcell(61+i,2+j,a[k])
for i,h in enumerate(m['health_only']): setcell(66+i,3,h['residual_gap'])
setcell(78,1,'Rebuilt monthly base: v3 cuts plus canceled newspaper24 and bank fee0.72')
b(80,round(m['normalized_monthly_burn_unrounded']-19635.76,2))
b(81,m['halfpay_monthly_equivalent_unrounded'])
for i in range(11): setcell(83+i,1,m['assumptions'][i])
setcell(92,1,m['assumptions'][9]+' '+m['halfpay_rounding_note'])
b(94,'; '.join(f"{a['first_skipped']}: ${a['jan23_cash']:,.2f} / ${a['jan23_reserve_shortfall']:,.2f}" for a in m['alternating_paychecks']))
b(95,m['monthly_gap_basis']+' '+m['halfpay_rounding_note']+' Newspaper24.72 removed from Sep14; cancellation confirmed, no past refund. No actual payroll changes; parent owns tracker note confirmation.')
plan=[]
for i in range(95):
    for j in range(26):
        prev=before['runway']['values'][i][j] if j<len(before['runway']['values'][i]) else ''
        new=values[i][j] if j<len(values[i]) else ''
        if str(prev)!=str(new): plan.append({'range':f"'Runway Forecast'!{chr(65+j)}{i+1}", 'values':[[new]]})
assert plan
save('-write-plan.json',plan)
m.update(rollback_snapshot=str(root/(prefix+'-prewrite.json')),report_path=str(root/(prefix+'-report.md')))
save('-calculations.json',m)
save('-cash-ledger.json',ledger)
assert fetch()==before, 'Concurrent edit; refusing stale write'
response=c.session.post(f'https://sheets.googleapis.com/v4/spreadsheets/{sheet}/values:batchUpdate', json={'valueInputOption':'RAW','data':plan}, timeout=60)
assert response.status_code==200, f'Batch failed: HTTP {response.status_code}'
save('-batch-response.json',response.json())
after=fetch()
save('-postverify.json',after)
assert after['tech']==before['tech']
for i,row in enumerate(values):
    for j in range(26):
        expected=row[j] if j<len(row) else ''
        actual=after['runway']['values'][i][j] if j<len(after['runway']['values'][i]) else ''
        assert str(expected)==str(actual), (i+1,j+1)
assert after['runway']['values'][95:]==before['runway']['values'][95:]
assert after['runway']['values'][15:24]==before['runway']['values'][15:24]
assert all(digest(Path(p))==h for p,h in originals.items())
m['status']='complete; live verified'
m['validation']=dict(live_cells_match=True,historical_rows_96_onward_preserved=True,historical_actuals_preserved=True,v3_and_prior_hashes_unchanged=True,original_hashes=originals,september_1_to_13_unchanged=True,itemization_reconciles=True,tech_unchanged=True,newspaper_row_not_added=True,batch_write_requests=1,changed_ranges=len(plan),no_emails_slack_payroll_tasks_commits=True,parent_owns_tracker_note_confirmation=True)
save('-calculations.json',m)
def table(head,rows):
    return '| '+' | '.join(head)+' |\n| '+' | '.join(['---']*len(head))+' |\n'+'\n'.join('| '+' | '.join(map(str,r))+' |' for r in rows)
report=f'''---
schema_version: 1.1.0
date: 2026-09-14
type: budget-report
status: published
skill_origin: budget-manager
kay_approved: null
kay_approval_date: null
people: []
companies: []
projects: []
published_url: null
tags: [date/2026-09-14, output, output/budget-report, status/published]
---

# September 14 Subscription Update, Version 4

Source: [[operating-areas/c-suite/CFO/{prior}-report|V3 report]]. V4 [[operating-areas/c-suite/CFO/{prefix}-calculations.json|model]] and [[operating-areas/c-suite/CFO/{prefix}-cash-ledger.json|dated ledger]].

## Confirmed Change

{note}

During Howie pause: full **${m['normalized_monthly_burn_unrounded']:,.2f}/month**, hypothetical half-pay **${m['halfpay_monthly_equivalent_unrounded']:,.2f}/month**. From December 14: **${m['after_pause']['full_monthly_unrounded']:,.2f} / ${m['after_pause']['halfpay_monthly_unrounded']:,.2f}**. Exact components: {m['halfpay_rounding_note']}

Incremental September savings ${24.72*17/30:,.2f}; through February 7 ${savings:,.2f}. Bank fees fall from $3.81 to $3.09; subscription falls from $24 to zero. No double-counting or past refund.

## Monthly Itemization

{table(['Item','Monthly','Basis'],[(x['item'],f"${x['monthly']:,.2f}",x['basis']) for x in m['monthly_itemization']])}

## Dated Forecast

August31 verified cash ${m['cash']['total']:,.2f}; protected DD reserve ${m['cash']['dd_reserve']:,.2f}. Modeled outflows ${outflows:,.2f}; February7 ending cash ${cash:,.2f}; reserve funding gap ${gap:,.2f}. Full-pay first reserve breach **{m['timed']['first_reserve_breach']}**. Additional monthly savings required ${m['monthly_gap_to_target']:,.2f}; normalized comparison {m['normalized_runway_months_comparison']} months, not a verified current cash balance.

{table(['Alternate: first skipped','Ending cash','Reserve gap','First breach'],[(a['first_skipped'],a['ending_cash'],a['reserve_shortfall'],a['first_reserve_breach']) for a in m['alternating_paychecks']])}

{table(['Hypothetical scenario','Effective','Gross monthly cut','Gross remaining','Tax savings/month','Health savings'],[(s['label'],s['effective'],s['gross_monthly_cut'],s['gross_monthly_remaining'],s['employer_tax_savings_monthly'],s['health_cash_savings']) for s in m['scenarios']])}

Health-only residual gaps: {', '.join(str(h['residual_gap']) for h in m['health_only'])}. All payroll/health alternatives remain hypothetical.

## Assumptions

'''+ '\n'.join('- '+s for s in m['assumptions'])+f'''

## Verification

[[operating-areas/c-suite/CFO/{prefix}-prewrite.json|Live prewrite snapshot]] and [[operating-areas/c-suite/CFO/{prefix}-postverify.json|Live read-back]] saved. One structured values batchUpdate request; {len(plan)} changed ranges within current rows1:95. All dependent metrics/scenarios and pending notes updated and verified. Historical actuals, rows96 onward, September1-13 ledger and tech inventory unchanged. No newspaper tech row invented. V3 and all prior artifacts hash-verified unchanged. No email, Slack, payroll actions, tasks or commits. Parent owns tracker note confirmation.
'''
Path(m['report_path']).write_text(report)
print(json.dumps({'status':m['status'],'full':m['normalized_monthly_burn_unrounded'],'half':m['halfpay_monthly_equivalent_unrounded'],'first_breach_full':m['timed']['first_reserve_breach'],'alternates':[{k:a[k] for k in ['first_skipped','first_reserve_breach']} for a in m['alternating_paychecks']],'report':m['report_path'],'changed_ranges':len(plan)},indent=2))
