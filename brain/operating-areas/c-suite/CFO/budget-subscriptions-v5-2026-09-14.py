import calendar
import copy
import hashlib
import json
import math
from pathlib import Path
import sys

sys.path.insert(0, '/home/ubuntu/projects/Sapling/scripts')
from task_tracker import SheetsClient

root = Path(__file__).parent
prior = '2026-09-14-budget-subscriptions-v4'
prefix = '2026-09-14-budget-subscriptions-v5'
def read(suffix):
    return json.loads((root / (prior + suffix)).read_text())
def save(suffix, data):
    (root / (prefix + suffix)).write_text(json.dumps(data, indent=2) + '\n')
def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

originals = {str(p): digest(p) for p in root.iterdir() if p.is_file() and 'v5' not in p.name}
verify_only = '--verify-only' in sys.argv
assert verify_only or not (root / (prefix + '-calculations.json')).exists()
m = read('-calculations.json')
old = read('-cash-ledger.json')
ledger = copy.deepcopy(old)
fields = ['other_allowance', 'payroll', 'insurance', 'health', 'dealsx', 'conference', 'website']
def cost(d):
    return sum(d[k] for k in fields)
cash = m['cash']['total']
reserve = m['cash']['dd_reserve']
savings = 0
for d, previous in zip(ledger, old):
    year, month, _ = map(int, d['date'].split('-'))
    delta = 35 / calendar.monthrange(year, month)[1] if d['date'] >= '2026-12-14' else 0
    savings += delta
    d['other_allowance'] -= delta
    cash -= cost(d)
    d['end_cash'] = cash
    assert all(d[k] == previous[k] for k in fields if k != 'other_allowance')
    if d['date'] < '2026-12-14':
        assert d == previous
assert abs(savings - 35 * (18/31 + 1 + 7/28)) < 1e-8
assert abs(old[-1]['end_cash'] + savings - cash) < 1e-8
outflows = sum(cost(d) for d in ledger)
gap = outflows + reserve - m['cash']['total']
m.pop('validation', None)
m.update(version=5, status='calculated; live verification pending')
note = 'Howie permanently CANCELLED, user confirmed September14; supersedes three-month pause. Zero forward cost, no December14 restart. DocSend cancellation reconfirmed; already zero in v4, no additional savings or refund.'
howie_note = 'Howie permanently CANCELLED per user September14; supersedes three-month pause. Remove only35/month restart allowance from December14 onward; zero forward billing modeled.'
docsend_note = 'DocSend cancellation reconfirmed by user September14. Already zero in v4; incremental savings0. Historical August30 debit16.33 unchanged.'
m['after_pause'].update(howie_monthly_allowance=0, full_monthly_unrounded=m['normalized_monthly_burn_unrounded'], halfpay_monthly_unrounded=m['halfpay_monthly_equivalent_unrounded'], other_monthly_allowance=m['normalized_other_monthly_allowance'], status='permanent cancellation; no restart')
m['halfpay_rounding_note'] = 'Full18622.796667; hypothetical half11221.853333 monthly from September14 onward, including after December14. Howie permanently canceled; no restart. Weekly employer cash3415.82 unchanged.'
sc = m['subscription_changes']
assert sc['docsend']['monthly'] == 0
sc['docsend'].update(status='canceled; user reconfirmed', incremental_v5_savings=0)
sc['howie'] = dict(status='permanently canceled; user confirmed', monthly=0, effective='2026-09-14', resume_allowance=0, removed_restart_date='2026-12-14', incremental_v5_horizon_savings=round(savings, 2), evidence=howie_note)
sc['monthly_reduction_after_pause'] = sc['monthly_reduction_during_pause']
sc['horizon_savings'] = round(sc['horizon_savings'] + savings, 2)
m['approved_changes']['total_monthly_after_howie_pause'] = m['approved_changes']['total_monthly']
m['approved_changes']['horizon_savings'] = round(m['approved_changes']['horizon_savings'] + savings, 2)
m['approved_changes']['subscription_changes'] = sc
m['normalized_bridge'] = [[label.replace('Howie paused', 'Howie permanently canceled'), amount] for label, amount in m['normalized_bridge']]
m['timed'].update(other_total=round(sum(d['other_allowance'] for d in ledger), 2), total_outflows=round(outflows, 2), shortfall_to_protected_reserve=round(gap, 2), unfunded_end_cash=round(cash, 2), first_reserve_breach=next(d['date'] for d in ledger if d['end_cash'] < reserve), approved_cut_cash_savings=m['approved_changes']['horizon_savings'], incremental_subscription_cash_savings=sc['horizon_savings'], incremental_howie_permanent_cancel_cash_savings=round(savings, 2))
m['monthly_gap_to_target'] = round(gap / m['timed']['approved_savings_month_equivalents'], 2)
factor = m['payroll']['incremental_savings_factor']
for s in m['scenarios']:
    needed = gap - s['health_cash_savings']
    weekly = needed / s['reduced_payments'] / factor
    exact = weekly * 52/12
    s.update(gross_monthly_cut_exact=exact, gross_monthly_cut=round(exact, 2), gross_monthly_remaining=round(m['payroll']['weekly_gross']*52/12-exact, 2), gross_cut_percent=round(weekly/m['payroll']['weekly_gross']*100, 2), weekly_cut_rounded_up=math.ceil(weekly*100)/100, gross_monthly_cut_no_employer_tax_savings=round(needed/s['reduced_payments']*52/12, 2), employer_tax_savings_monthly=round(exact*(factor-1), 2))
    s['weekly_gross_remaining'] = round(m['payroll']['weekly_gross']-s['weekly_cut_rounded_up'], 2)
    assert abs(cash + weekly*factor*s['reduced_payments'] + s['health_cash_savings'] - reserve) < 1e-7
for a in m['alternating_paychecks']:
    balance = m['cash']['total']
    breach = None
    for d in ledger:
        balance -= cost(d)
        if d['date'] in a['skipped_dates']:
            balance += d['payroll']
        if breach is None and balance < reserve:
            breach = d['date']
        if d['date'] == '2027-01-23':
            a.update(jan23_cash=round(balance, 2), jan23_reserve_shortfall=round(reserve-balance, 2))
    a.update(ending_cash=round(balance, 2), reserve_shortfall=round(reserve-balance, 2), first_reserve_breach=breach)
for h in m['health_only']:
    h['residual_gap'] = round(gap-h['total_maximum'], 2)

# Half-pay applies to every modeled payroll payment after the existing effective date.
balance = m['cash']['total']
breach = None
for d in ledger:
    balance -= cost(d)
    if d['date'] >= '2026-09-14':
        balance += d['payroll']/2
    if breach is None and balance < reserve:
        breach = d['date']
m['halfpay_dated_runway'] = dict(effective='2026-09-14', first_reduced_payment='2026-09-15', first_reserve_breach=breach, ending_cash=round(balance, 2), reserve_shortfall=round(reserve-balance, 2), basis='Hypothetical half of each weekly employer payroll cash payment; fixed Gusto fee unchanged')
m['assumptions'][0] = m['assumptions'][0].replace('restoring Howie35 allowance Dec14', 'v5 permanently removes the previously assumed Howie35 restart Dec14')
m['assumptions'][3] = m['assumptions'][3].replace('1032.17/month Sep14-Dec13;1067.17 from Dec14', '1032.17/month from Sep14 onward; no Howie restart')
m['assumptions'][7] = note + ' Art Newspaper24 and bank fee0.72 cancellation already reflected in v4. Voice10 and Slack15 unverified allowances retained; Voice may overlap Workspace.'
m['assumptions'][12] = m['halfpay_rounding_note']
for x in m['monthly_itemization']:
    if x['item'] == 'Howie':
        x.update(monthly=0, basis=howie_note)
    if x['item'] == 'Art Newspaper':
        x['basis'] = 'Art Newspaper cancellation confirmed September14;24 subscription plus0.72 bank fee already removed in v4, no refund.'
for x in m['inventory_audit']:
    if x['tool'] in ['Howie', 'DocSend']:
        x.update(status='PERMANENTLY CANCELLED' if x['tool']=='Howie' else 'CANCELED', monthly_equivalent=0, evidence=howie_note if x['tool']=='Howie' else docsend_note)
    if x['tool'] == 'The Art Newspaper':
        x['evidence'] = 'Art Newspaper24 plus bank fee0.72 cancellation already reflected in v4; no additional savings.'
assert abs(sum(x['monthly'] for x in m['monthly_itemization']) - m['normalized_monthly_burn_unrounded']) < 1e-8
assert abs(m['normalized_monthly_burn_unrounded']-18622.796667) < 1e-6
assert abs(m['halfpay_monthly_equivalent_unrounded']-11221.853333) < 1e-6
save('-cash-ledger.json', ledger)

sheet = '1vTeGviuQk9zLqacJrdBZS2Bopk8kQZtmEHWheqpCdq0'
c = SheetsClient(sheet)
ranges = {'runway': "'Runway Forecast'!A1:Z", 'tech': "'Tech Stack Inventory'!A1:Z100"}
def fetch():
    return {k: {'values': c.get_values(v)} for k, v in ranges.items()}
before = json.loads((root / (prefix + '-prewrite.json')).read_text()) if verify_only else fetch()
expected = copy.deepcopy(before)
def setcell(r, col, value, tab='runway'):
    row = expected[tab]['values'][r-1]
    while len(row) < col:
        row.append('')
    row[col-1] = str(value)
def b(r, value):
    setcell(r, 2, value)
b(3, 'Aug31 VERIFIED cash; Sep14 subscription v5 MODEL; no September feed')
for r in [9, 32]: b(r, m['timed']['first_reserve_breach'])
for r in [10, 47]: b(r, round(gap, 2))
for r in [11, 34]: b(r, m['monthly_gap_to_target'])
b(12, 'August bank statements + v4 model + user-confirmed permanent Howie cancellation; DocSend reconfirmed zero')
b(13, note + ' Other prior cuts retained; historical actuals unchanged.')
setcell(41, 1, 'Other allowance:2798.12 to Sep13;1032.17 Sep14 onward; no Howie restart')
b(41, m['timed']['other_total'])
b(45, m['timed']['total_outflows'])
for i, s in enumerate(m['scenarios']):
    for j, k in enumerate(['gross_monthly_cut', 'gross_monthly_remaining', 'employer_tax_savings_monthly', 'health_cash_savings', 'first_reduced_payment', 'reduced_payments']): setcell(51+i, 2+j, s[k])
for i, a in enumerate(m['alternating_paychecks']):
    for j, k in enumerate(['skipped_count', 'retained_count', 'savings', 'ending_cash', 'reserve_shortfall', 'first_reserve_breach']): setcell(61+i, 2+j, a[k])
for i, h in enumerate(m['health_only']): setcell(66+i, 3, h['residual_gap'])
setcell(78, 1, 'Rebuilt monthly base: v4 unchanged; Howie permanently canceled, no December restart')
for i in range(11): setcell(83+i, 1, m['assumptions'][i])
setcell(92, 1, m['assumptions'][9] + ' ' + m['halfpay_rounding_note'])
b(94, '; '.join(f"{a['first_skipped']}: ${a['jan23_cash']:,.2f} / ${a['jan23_reserve_shortfall']:,.2f}" for a in m['alternating_paychecks']))
b(95, m['monthly_gap_basis'] + ' ' + m['halfpay_rounding_note'] + f' Half of each weekly payroll from Sep15: first DD reserve breach {breach}. No actual payroll changes; parent owns task updates.')
tech_rows = {}
for tool, status, evidence in [('Howie', 'PERMANENTLY CANCELLED', howie_note), ('DocSend', 'CANCELED', docsend_note)]:
    matches = [i+1 for i, row in enumerate(before['tech']['values']) if row and row[0] == tool]
    assert len(matches) == 1
    r = tech_rows[tool] = matches[0]
    for col in [4, 5, 6, 10, 11]:
        assert float(before['tech']['values'][r-1][col-1]) == 0
    for col in [3, 9]: setcell(r, col, evidence, 'tech')
    setcell(r, 7, status, 'tech')
plan = []
for tab, title in [('runway', 'Runway Forecast'), ('tech', 'Tech Stack Inventory')]:
    for i, row in enumerate(expected[tab]['values']):
        prev = before[tab]['values'][i]
        for j in range(max(len(row), len(prev))):
            a = prev[j] if j < len(prev) else ''
            v = row[j] if j < len(row) else ''
            if str(a) != str(v):
                assert v != ''
                assert (i < 95 and not 15 <= i < 24) if tab == 'runway' else (i+1 in tech_rows.values() and j in [2, 6, 8])
                plan.append({'range': f"'{title}'!{chr(65+j)}{i+1}", 'values': [[v]]})
assert plan
save('-write-plan.json', plan)
m.update(rollback_snapshot=str(root/(prefix+'-prewrite.json')), report_path=str(root/(prefix+'-report.md')))
save('-calculations.json', m)
# Refetch immediately before the single write; persist that exact rollback state.
if not verify_only:
    fresh = fetch()
    assert fresh == before, 'Concurrent edit; refusing stale write'
    save('-prewrite.json', fresh)
    response = c.session.post(f'https://sheets.googleapis.com/v4/spreadsheets/{sheet}/values:batchUpdate', json={'valueInputOption': 'RAW', 'data': plan}, timeout=60)
    assert response.status_code == 200, f'Batch failed: HTTP {response.status_code}'
    save('-batch-response.json', response.json())
after = fetch()
save('-postverify.json', after)
for tab in expected:
    assert len(after[tab]['values']) == len(expected[tab]['values'])
    for actual, wanted in zip(after[tab]['values'], expected[tab]['values']):
        for j in range(max(len(actual), len(wanted))):
            assert str(actual[j] if j < len(actual) else '') == str(wanted[j] if j < len(wanted) else ''), 'Live cell differs from expected state'
assert after['runway']['values'][95:] == before['runway']['values'][95:]
assert after['runway']['values'][15:24] == before['runway']['values'][15:24]
assert all(digest(Path(p)) == h for p, h in originals.items())
m['status'] = 'complete; live verified'
m['validation'] = dict(live_cells_match=True, historical_rows_96_onward_preserved=True, actuals_rows_16_to_24_preserved=True, v4_and_history_hashes_unchanged=True, original_hashes=originals, ledger_before_dec14_unchanged=True, only_howie_35_restart_removed=True, docsend_incremental_savings=0, batch_write_requests=1, changed_ranges=len(plan), no_emails_slack_payroll_tasks_commits=True)
save('-calculations.json', m)
report = f'''---
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

# September 14 Subscription Update, Version 5

Source: [[operating-areas/c-suite/CFO/{prior}-report|V4 report]]. Updated [[operating-areas/c-suite/CFO/{prefix}-calculations.json|model and scenarios]] and [[operating-areas/c-suite/CFO/{prefix}-cash-ledger.json|dated ledger]].

{note}

- Incremental savings versus v4: $35/month from December14; $35*(18/31+1+7/28) = **${savings:.2f} through February7**. September savings unchanged; DocSend incremental savings $0.
- Current and post-December14 monthly burn: full **${m['normalized_monthly_burn_unrounded']:,.2f}**, hypothetical half **${m['halfpay_monthly_equivalent_unrounded']:,.2f}**. Exact: {m['halfpay_rounding_note']}
- Dated full-pay forecast: first protected-reserve breach **{m['timed']['first_reserve_breach']}**; February7 ending cash ${cash:,.2f}; reserve shortfall **${gap:,.2f}**.
- Half of each weekly payroll from September15: first reserve breach **{breach}**; February7 ending cash ${balance:,.2f}; shortfall ${reserve-balance:,.2f}.
- Every-other-paycheck alternatives (first skipped / first reserve breach): {', '.join(a['first_skipped']+' / '+str(a['first_reserve_breach']) for a in m['alternating_paychecks'])}.
- Additional monthly savings needed ${m['monthly_gap_to_target']:,.2f}. All salary and health alternatives remain hypothetical; no payroll action.

Runway dates mean first breach of the protected ${reserve:,.0f} DD reserve, not bank-account exhaustion. Cash anchor remains August31 verified ${m['cash']['total']:,.2f}; no September bank feed. All other v4 assumptions retained except the superseded Howie restart.

## Verification

[[operating-areas/c-suite/CFO/{prefix}-prewrite.json|Immediate prewrite snapshot]] and [[operating-areas/c-suite/CFO/{prefix}-postverify.json|live readback]] saved. One structured batch, {len(plan)} changed cells. Full fetched state matches expected; rows96 onward, actuals rows16:24, all unrelated tech rows and all pre-December14 ledger entries unchanged. V4 and historical files hash-verified unchanged. No email, Slack, tasks, payroll actions or commits; parent owns task updates.
'''
Path(m['report_path']).write_text(report)
print(json.dumps(dict(status=m['status'], savings=round(savings, 2), full_runway=m['timed']['first_reserve_breach'], half_runway=breach, full_shortfall=round(gap, 2), half_shortfall=round(reserve-balance, 2), changed_ranges=len(plan), report=m['report_path']), indent=2))
