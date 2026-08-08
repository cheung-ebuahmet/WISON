import os, re

data_dir = r'D:\Wison\_Ref\data\contracts'
contracts = {}

for fname in sorted(os.listdir(data_dir)):
    if not fname.endswith('.yaml'):
        continue
    short_id = fname.replace('.yaml', '')
    with open(os.path.join(data_dir, fname), 'r', encoding='utf-8') as f:
        text = f.read()

    c = {}
    c['id'] = short_id

    m = re.search(r'vendor:\s*(\w+)', text)
    c['vendor'] = m.group(1) if m else '—'

    m = re.search(r'discipline:\s*(\w+)', text)
    c['discipline'] = m.group(1) if m else '—'

    m = re.search(r'package:\s*"([^"]+)"', text)
    if not m:
        m = re.search(r'package:\s*(.+)', text)
    c['package'] = m.group(1).strip() if m else '—'

    m = re.search(r'status:\s*(\w+)', text)
    c['status'] = m.group(1) if m else '—'

    m = re.search(r'contract_value:\s*([\d.]+)', text)
    c['value'] = float(m.group(1)) if m else None

    m = re.search(r'provisional_sum:\s*([\d.]+)', text)
    c['prov_sum'] = float(m.group(1)) if m else None

    m = re.search(r'advance_payment_pct:\s*(\d+)', text)
    c['adv_pct'] = int(m.group(1)) if m else None

    m = re.search(r'performance_bond_pct:\s*(\d+)', text)
    c['pb_pct'] = int(m.group(1)) if m else None

    m = re.search(r'retention_pct:\s*(\d+)', text)
    c['ret_pct'] = int(m.group(1)) if m else None

    m = re.search(r'retention_additional_warranty_pct:\s*(\d+)', text)
    c['ret_warranty'] = int(m.group(1)) if m else None

    m = re.search(r'payment_days:\s*(\d+)', text)
    c['pay_days'] = int(m.group(1)) if m else None

    m = re.search(r'defects_liability_months:\s*(\d+)', text)
    c['defects_mo'] = int(m.group(1)) if m else None

    m = re.search(r'warranty_months:\s*(\d+)', text)
    c['warr_mo'] = int(m.group(1)) if m else None

    m = re.search(r'cap_amount:\s*([\d.]+)', text)
    c['delay_cap_amt'] = float(m.group(1)) if m else None

    m = re.search(r'cap_pct:\s*(\d+)', text)
    c['delay_cap'] = int(m.group(1)) if m else None

    m = re.search(r'key_personnel:\s*\n\s+per_day:\s*(\d+)', text, re.MULTILINE)
    c['kp_ld'] = int(m.group(1)) if m else None

    m = re.search(r'count:\s*(\d+)', text)
    c['kp_count'] = int(m.group(1)) if m else None

    m = re.search(r'performance:\s*\n\s+applicable:\s*(true|false)', text, re.MULTILINE)
    c['perf_ld'] = 'Yes' if (m and m.group(1) == 'true') else 'No'

    m = re.search(r'amendment_count:\s*(\d+)', text)
    c['amdt'] = int(m.group(1)) if m else 0

    c['has_open_issues'] = c['id'] == '10.1-CCECC-Civil-II'

    # delay LD per day
    per_day_match = re.search(r'delay:\s*\n\s+per_day:\s*([\d.]+)', text, re.MULTILINE)
    c['delay_ld_day'] = float(per_day_match.group(1)) if per_day_match else None

    contracts[short_id] = c

# ============================================================
# GENERATE MATRIX
# ============================================================
lines = []
lines.append('# Subcontractor Matrix — 商业驾驶舱')
lines.append('')
lines.append('> 自动编译自 `data/contracts/*.yaml` — 不手写')
lines.append('> 生成时间: 2026-07-09')
lines.append('')
lines.append('---')
lines.append('')
lines.append('## 1. 合同概况')
lines.append('')
lines.append('| 合同 | 分包商 | 专业 | 包号 | 金额 (AED) | 暂列金 (AED) | Amdt | 状态 |')
lines.append('|------|--------|------|:---:|----------:|----------:|:---:|:---:|')

name_map = {
    '10.1-CCECC-Civil-II': '10.1 CCECC Civil II',
    '10.2-TCC-Civil-I-III': '10.2 TCC Civil I/III',
    '12.1-CCECC-MEI-I': '12.1 CCECC MEI I',
}

for cid in sorted(contracts.keys()):
    c = contracts[cid]
    nm = name_map.get(cid, cid)
    val = '{0:,.2f}'.format(c['value']) if c['value'] else '*(待)*'
    prov = '{0:,.2f}'.format(c['prov_sum']) if c['prov_sum'] else '—'
    st = {'active': '&#x2705;', 'draft': '&#x26A0;'}.get(c['status'], c['status'])
    ac = '{0}'.format(c['amdt']) if c['amdt'] > 0 else '—'
    lines.append('| {0} | {1} | {2} | {3} | {4} | {5} | {6} | {7} |'.format(
        nm, c['vendor'], c['discipline'], c.get('package',''), val, prov, ac, st))

lines.append('')
lines.append('## 2. 保函与付款')
lines.append('')
lines.append('| 合同 | 预付款 % | 保函 | 履约保函 % | 保留金 % | 附加质保 % | 付款周期 | 缺陷责任 | 质保期 |')
lines.append('|------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|')

for cid in sorted(contracts.keys()):
    c = contracts[cid]
    nm = name_map.get(cid, cid)
    adv = '{0}%'.format(c['adv_pct']) if c['adv_pct'] else '*(待)*'
    apg = '&#x2705;' if c['adv_pct'] else '*(待)*'
    pb = '{0}%'.format(c['pb_pct']) if c['pb_pct'] else '*(待)*'
    ret = '{0}%'.format(c['ret_pct']) if c['ret_pct'] else '*(待)*'
    retw = '{0}%'.format(c['ret_warranty']) if c.get('ret_warranty') else '—'
    pay = '{0}d'.format(c['pay_days']) if c['pay_days'] else '*(待)*'
    defm = '{0}m'.format(c['defects_mo']) if c.get('defects_mo') else '*(待)*'
    war = '{0}m'.format(c['warr_mo']) if c.get('warr_mo') else '*(待)*'
    lines.append('| {0} | {1} | {2} | {3} | {4} | {5} | {6} | {7} | {8} |'.format(
        nm, adv, apg, pb, ret, retw, pay, defm, war))

lines.append('')
lines.append('## 3. 误期损害赔偿 (LD)')
lines.append('')
lines.append('| 合同 | Delay LD/天 | LD 上限 | LD 上限金额 | KP LD/天 | KP 人数 | 性能 LD |')
lines.append('|------|:---:|:---:|:---:|:---:|:---:|:---:|')

for cid in sorted(contracts.keys()):
    c = contracts[cid]
    nm = name_map.get(cid, cid)
    dd = 'AED {0:,.0f}'.format(c['delay_ld_day']) if c['delay_ld_day'] else '*(待)*'
    dc = '{0}%'.format(c['delay_cap']) if c.get('delay_cap') else '*(待)*'
    dca = 'AED {0:,.0f}'.format(c['delay_cap_amt']) if c.get('delay_cap_amt') else '—'
    kp = 'AED {0:,.0f}'.format(c['kp_ld']) if c['kp_ld'] else '*(待)*'
    kpc = str(c['kp_count']) if c['kp_count'] else '*(待)*'
    pl = c.get('perf_ld', '—')
    lines.append('| {0} | {1} | {2} | {3} | {4} | {5} | {6} |'.format(
        nm, dd, dc, dca, kp, kpc, pl))

lines.append('')
lines.append('## 4. 活跃商业问题')
lines.append('')
lines.append('| 合同 | 问题 | 成本影响 | 截止日 | 状态 |')
lines.append('|------|------|------|:---:|:---:|')
lines.append('| 10.1 CCECC Civil II | PM 缺位 — Material Breach | AED 10,000/day | 2026-07-16 | &#x1F534; open |')
for cid in sorted(contracts.keys()):
    c = contracts[cid]
    if c['has_open_issues'] and cid != '10.1-CCECC-Civil-II':
        lines.append('| {0} | issue | — | — | open |'.format(name_map.get(cid, cid)))

lines.append('')
lines.append('## 5. 数据完整度')
lines.append('')
lines.append('| 合同 | 缺失字段 |')
lines.append('|------|------|')

for cid in sorted(contracts.keys()):
    c = contracts[cid]
    mlist = []
    if not c['adv_pct']: mlist.append('预付款%')
    if not c['pb_pct']: mlist.append('履约保函%')
    if not c['ret_pct']: mlist.append('保留金%')
    if not c['pay_days']: mlist.append('付款周期')
    if not c.get('defects_mo'): mlist.append('缺陷责任期')
    if not c.get('warr_mo'): mlist.append('质保期')
    if not c['delay_ld_day']: mlist.append('Delay LD/天')
    if not c.get('delay_cap_amt'): mlist.append('LD 上限金额')
    nm = name_map.get(cid, cid)
    if mlist:
        lines.append('| {0} | {1} |'.format(nm, ', '.join(mlist)))
    else:
        lines.append('| {0} | &#x2705; 商业字段完整 |'.format(nm))

out = '\n'.join(lines)
output_path = r'D:\Wison\_Ref\wiki\Commercial\Subcontractor-Matrix.md'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(out)

print('Generated: ' + output_path)
print()
print(out)
