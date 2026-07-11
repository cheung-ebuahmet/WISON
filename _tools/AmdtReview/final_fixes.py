# -*- coding: utf-8 -*-
"""Final batch of fixes per user instructions."""
from docx import Document

FPATH = r"D:\Wison\Subcon_Payments\12.1 CCECC - MEI Pkg I\Contract\02_Amdt 01\Amdt 01_MEI Pkg I (Revised) .docx"

doc = Document(FPATH)
paras = doc.paragraphs

def set_text(idx, new_text):
    for run in paras[idx].runs:
        run.text = ''
    paras[idx].runs[0].text = new_text

# ============================================================
# 1. EN [20] WHEREAS 1 -- delete region/personnel language
# ============================================================
old = ('thereafter, in light of the prevailing regional situation and '
       'difficulties in personnel mobilization, and in order')
new = 'thereafter, in order'
txt = paras[20].text.replace(old, new)
set_text(20, txt)
print('[20] EN: deleted region/personnel language')

# ============================================================
# 2. CN [21] WHEREAS 1 -- delete region/personnel + fix approval
# ============================================================
txt = paras[21].text.replace(
    '因地区形势及人员动迁困难，',
    '')
txt = txt.replace(
    '征询业主意见后',
    '经业主批准后')
set_text(21, txt)
print('[21] CN: deleted region/personnel + 征询业主→经业主批准')

# ============================================================
# 3. [13] U.A.E → UAE
# ============================================================
txt = paras[13].text.replace('U.A.E', 'UAE')
set_text(13, txt)
print('[13] U.A.E → UAE')

# ============================================================
# 4. CN [25] 委托业务→委托工程
# ============================================================
txt = paras[25].text.replace(
    '不对该委托业务承担',
    '不对该委托工程承担')
set_text(25, txt)
print('[25] CN: 委托业务→委托工程')

# ============================================================
# 5. CN [34] 各方→双方
# ============================================================
txt = paras[34].text.replace(
    '各方确认',
    '双方确认')
set_text(34, txt)
print('[34] CN: 各方→双方')

# ============================================================
# 6. EN [29] i.e.→i.e.,
# ============================================================
txt = paras[29].text.replace('i.e. Fusion', 'i.e., Fusion')
set_text(29, txt)
print('[29] EN: i.e.→i.e.,')

# ============================================================
# 7. CN [30] 5.3万→5.3 万 (add space)
# ============================================================
txt = paras[30].text.replace('5.3万', '5.3 万')
set_text(30, txt)
print('[30] CN: 5.3万→5.3 万')

# ============================================================
# 8. EN [39] 3.1 -- define Delegated Services at first occurrence
# ============================================================
old = ('in connection with the Delegated Works and Delegated Services, '
       'Contractor shall merely make payment')
new = ('in connection with the Delegated Works and the logistics, customs, '
       'and delivery services described in Clauses 6 and 7 '
       '(the "Delegated Services"), Contractor shall merely make payment')
txt = paras[39].text.replace(old, new)
set_text(39, txt)
print('[39] EN: defined Delegated Services')

# ============================================================
# 9. CN [40] 3.1 -- define 委托服务 at first occurrence
# ============================================================
old = ('就应付第三方的与委托工程'
       '及委托服务相关的所有费用')
new = ('就应付第三方的与委托工程'
       '及第 6 条和第 7 条所述物流、'
       '海关及交付服务（下称“委'
       '托服务”）相关的所有费用')
txt = paras[40].text.replace(old, new)
set_text(40, txt)
print('[40] CN: defined 委托服务')

# ============================================================
# 10. EN [52] 4.2 -- Third Party expenses → Third Party Costs
# ============================================================
txt = paras[52].text.replace('Third Party expenses', 'Third Party Costs')
set_text(52, txt)
print('[52] EN: Third Party expenses→Third Party Costs')

# ============================================================
# 11. CN [59] 4.5 -- 代付→抵扣 + add 书面
# ============================================================
txt = paras[59].text.replace(
    '不足以全额代付第三方费用',
    '不足以全额抵扣第三方费用')
txt = txt.replace(
    '自承包商发出要求之日起',
    '自承包商发出书面要求之日起')
set_text(59, txt)
print('[59] CN: 代付→抵扣 + 书面要求')

# ============================================================
# 12. CN [62] 5.1 -- 及其→与
# ============================================================
txt = paras[62].text.replace(
    '分包商及其第三方应负责',
    '分包商与第三方应负责')
set_text(62, txt)
print('[62] CN: 及其→与')

# ============================================================
# 13. EN [68] 6.2 -- add "For the avoidance of doubt, "
# ============================================================
txt = 'For the avoidance of doubt, ' + paras[68].text
set_text(68, txt)
print('[68] EN: added For the avoidance of doubt')

# ============================================================
# 14. EN [82] 8.1(iii) -- add risk-sharing carve-out
# ============================================================
new_en = (
    'Risk — All contractual and legal risks arising from the Delegated '
    'Works, including without limitation delay, non-performance, defective '
    'performance, quality failure, loss or damage in transit, regulatory '
    'non-compliance, and disputes, shall be borne fully, unconditionally, and '
    'exclusively by Subcontractor; provided, however, that the risk of loss of '
    'or damage to the finished products during the international sea freight '
    'segment arranged by Contractor pursuant to Clause 4.3 shall be shared '
    'between Subcontractor and Contractor in the same proportion as the costs '
    'thereof, i.e., twenty-five percent (25%) by Subcontractor and seventy-five '
    'percent (75%) by Contractor.'
)
set_text(82, new_en)
print('[82] EN: added risk sharing 25/75 for intl sea freight')

# ============================================================
# 15. CN [83] 8.1(iii) -- add risk-sharing carve-out
# ============================================================
new_cn = (
    '风险承担——因委托工程产'
    '生的所有合同及法律风险（'
    '包括但不限于延误、不履约'
    '、履约缺陷、质量不合格、'
    '运输途中灭失或损坏、监管'
    '不合规及争议），均由分包'
    '商全额、无条件且排他地承'
    '担；但是，承包商依据第 4.3 '
    '条安排的国际海运段期间成'
    '品灭失或损坏的风险，由分'
    '包商与承包商按费用分摊的'
    '同等比例承担，即分包商承'
    '担百分之二十五（25%）、承包'
    '商承担百分之七十五（75%）。'
)
set_text(83, new_cn)
print('[83] CN: added risk sharing 25/75 for intl sea freight')

# ============================================================
# 16. Unify CN brackets: fullwidth （x）→ halfwidth (x)
# ============================================================
bracket_map = {
    '（a）': '(a)',
    '（b）': '(b)',
    '（c）': '(c)',
    '（i）': '(i)',
    '（ii）': '(ii)',
    '（iii）': '(iii)',
}
for idx in [44, 46, 48, 79, 81, 87, 89, 91]:
    txt = paras[idx].text
    for old_b, new_b in bracket_map.items():
        if txt.strip().startswith(old_b):
            txt = txt.replace(old_b, new_b, 1)
            set_text(idx, txt)
            print(f'  [{idx}] bracket unified: {old_b}->{new_b}')
            break

doc.save(FPATH)
print()
print('[DONE] All fixes saved')
