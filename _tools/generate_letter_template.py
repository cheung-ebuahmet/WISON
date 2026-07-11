# -*- coding: utf-8 -*-
"""
Generate the Wison bilingual formal-letter TEMPLATE.

Base = SLT-5312-WSN-CCC-0006_NOTICE-DEF-MEI I.docx (an actual, well-formatted
letter). We copy it and convert the filled content back into template
placeholders:
  - Header variable fields  -> [bracketed placeholder] + YELLOW highlight
  - Project (Owner info)    -> kept STATIC (unchanged)
  - Subject                 -> bilingual placeholder + YELLOW highlight (reminder)
  - Body (7 paras)          -> Notice-letter structure, bilingual placeholders
  - Signature block         -> kept as-is
Formatting (Arial, sizes, line spacing 1.2, space-before 5pt, letterhead
tables, logo header/footer) is inherited unchanged from the base.

Output overwrites: Your-Letter-Number Letter-Title.docx  (old one backed up).
"""
import os
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_COLOR_INDEX

# Scripts are centralized under D:\Documents\My Projects\scripts\docgen\ ;
# they operate on the deliverable folder via an absolute path.
TEMPLATE_DIR = r"D:\Wison\Project_Info\Wison Template"
BASE = os.path.join(TEMPLATE_DIR, "SLT-5312-WSN-CCC-0006_NOTICE-DEF-MEI I.docx")
OUT  = os.path.join(TEMPLATE_DIR, "Your-Letter-Number Letter-Title.docx")

doc = Document(BASE)

# ---------- helpers ----------
def _clear_runs(paras):
    for p in paras:
        for r in list(p.runs):
            r._element.getparent().remove(r._element)

def set_cell(cell, text, size_pt, highlight=False, bold=None):
    """Replace a table cell's text with one placeholder run, keep para format."""
    paras = cell.paragraphs
    _clear_runs(paras)
    run = paras[0].add_run(text)
    run.font.size = Pt(size_pt)
    if bold is not None:
        run.bold = bold
    if highlight:
        run.font.highlight_color = WD_COLOR_INDEX.YELLOW
    return run

def set_cell_bilingual(cell, en, cn, size_pt, highlight=False, bold=None):
    paras = cell.paragraphs
    _clear_runs(paras)
    r1 = paras[0].add_run(en)
    r1.font.size = Pt(size_pt)
    if bold is not None: r1.bold = bold
    if highlight: r1.font.highlight_color = WD_COLOR_INDEX.YELLOW
    r1.add_break()
    r2 = paras[0].add_run(cn)
    r2.font.size = Pt(size_pt)
    if bold is not None: r2.bold = bold
    if highlight: r2.font.highlight_color = WD_COLOR_INDEX.YELLOW

def set_para_bilingual(para, en, cn, size_pt=11):
    """Body paragraph: EN line + line-break + CN line, matching base runs."""
    _clear_runs([para])
    r1 = para.add_run(en); r1.font.size = Pt(size_pt)
    r1.add_break()
    r2 = para.add_run(cn); r2.font.size = Pt(size_pt)

# ======================================================================
# HEADER TABLE 0  (address / reference block, 10pt)
# ======================================================================
t0 = doc.tables[0]
S0 = 10
# Date value
set_cell(t0.rows[0].cells[2], "[DD-Month-YYYY]", S0, highlight=True, bold=True)
# Recipient name
set_cell(t0.rows[1].cells[0], "[Recipient Name / 收件人姓名]", S0, highlight=True, bold=True)
# Our ref. No.
set_cell(t0.rows[1].cells[2], "[Our Ref. No. / 我方文号]", S0, highlight=True, bold=True)
# Recipient title
set_cell(t0.rows[2].cells[0], "[Title / 职务]", S0, highlight=True, bold=False)
# Your ref. No. (default N/A - left as is, not highlighted)
set_cell(t0.rows[2].cells[2], "N/A", S0, highlight=False, bold=True)
# Answer Required (default Yes - left as is)
set_cell(t0.rows[3].cells[2], "Yes", S0, highlight=False, bold=True)
# Recipient company (r4c0; may be vertically merged with r5c0)
c_r4 = t0.rows[4].cells[0]
set_cell(c_r4, "[Recipient Company / 收件公司]", S0, highlight=True, bold=True)
c_r5 = t0.rows[5].cells[0]
if c_r5._tc is not c_r4._tc:   # not merged -> set separately
    set_cell(c_r5, "[Recipient Company / 收件公司]", S0, highlight=True, bold=True)
# Response Date
set_cell(t0.rows[4].cells[2], "[DD-Month-YYYY]", S0, highlight=True, bold=True)
# Page (total pages)
set_cell(t0.rows[5].cells[2], "[#]", S0, highlight=True, bold=True)

# ======================================================================
# HEADER TABLE 1  (Project = STATIC owner info ; Subject = placeholder)
# ======================================================================
t1 = doc.tables[1]
S1 = 11
# r0c1 Project -> LEAVE UNCHANGED (owner's project info stays static)
# r1c1 Subject -> bilingual placeholder + highlight (reminder)
set_cell_bilingual(
    t1.rows[1].cells[1],
    "[Subject / 主题 — concise letter title in ALL CAPS, "
    "e.g. NOTICE OF DELAY: … OVERDUE]",
    "[主题 — 简明信函标题，例如：延误通知：…逾期]",
    S1, highlight=True, bold=True)

# ======================================================================
# BODY  (paragraphs 0..6 -> Notice-letter structure, bilingual placeholders)
# ======================================================================
body = [
    # 0 Basis / 依据
    ("[Basis / 依据 — Cite the governing contract, the specific clause(s) "
     "and exhibit(s), and the obligation or entitlement relied upon. "
     "e.g., Pursuant to the Subcontract Agreement (Ref. No. ___), Clause ___ "
     "and Exhibit ___, the Subcontractor is required to ___.]",
     "[依据 — 引述所依据的合同、具体条款及附件，以及所据以主张的义务或权利。"
     "例如：根据《分包合同》（编号：___）第___条及附件___，贵司须___。]"),
    # 1 Facts / 事实
    ("[Facts / 事实 — Set out the relevant dates, the current status, and the "
     "factual basis for the breach or claim, verified as at the date of this "
     "letter. State whether any notice of Force Majeure / Time Adjustment "
     "Event has been given.]",
     "[事实 — 载明相关日期、当前状态及违约或主张的事实依据（截至本函之日核实）。"
     "说明对方是否已就此发出不可抗力或工期调整事件通知。]"),
    # 2 Contractor's position / 承包商立场
    ("[Contractor's position / 承包商立场 — Give formal notice of the "
     "consequence (e.g., Delay Liquidated Damages are accruing from the day "
     "after the Completion Date) and reserve the right to deduct or recover "
     "from sums due, Interim Payment Certificates, Retention Money, etc.]",
     "[承包商立场 — 正式通知相应后果（如：自完成日期次日起误期违约金持续累计），"
     "并保留从应付款项、中期付款证书、保留金等中扣减或追偿的权利。]"),
    # 3 Escalation warning / 升级警示
    ("[Escalation warning / 升级警示 — State the further consequences if the "
     "default is not immediately remedied, including escalation to the "
     "Employer (e.g., ADNOC) and the exercise of further rights and remedies "
     "under the Subcontract.]",
     "[升级警示 — 说明如不立即纠正违约将产生的进一步后果，包括上报业主（如 ADNOC）"
     "及根据《分包合同》行使进一步权利与救济。]"),
    # 4 Required action / 要求
    ("[Required action / 要求 — Require the recipient to respond within a set "
     "period (e.g., seven (7) calendar days of this letter, i.e., on or "
     "before ___), providing a formal written statement setting out:]",
     "[要求 — 要求对方于限定期限内（如：本函发出之日起七（7）个日历日内，即___或之前）"
     "提供一份正式书面说明，载明：]"),
    # 5 Itemised requirements / 列项要求
    ("[Itemised requirements / 列项要求 — (i) the root cause(s) of the "
     "delay; (ii) the remedial measures taken or being taken; (iii) "
     "confirmation of commitment to the remaining Key Milestone Dates; and "
     "(iv) the accountable senior management representative (name & contact).]",
     "[列项要求 —（i）延误的根本原因；（ii）已采取或正在采取的纠正措施；"
     "（iii）对剩余关键里程碑日期的履约确认；（iv）负责的高管代表姓名及联系方式。]"),
    # 6 Reservation of rights / 权利保留
    ("[Reservation of rights / 权利保留 — This notice is without prejudice "
     "to all rights and remedies under the Subcontract, at law or in equity. "
     "Expressly reserve rights (e.g., levy Delay LDs; termination for default; "
     "decrease/omit/delete Works; escalate to the Employer). State the "
     "consequence of a failure to respond within the timeframe.]",
     "[权利保留 — 本通知的发出不影响承包商依据《分包合同》、适用法律或衡平法享有的一切权利与救济。"
     "明确保留相关权利（如：计收误期违约金；违约终止；缩减、删除工程；上报业主）。"
     "说明逾期未回应的后果。]"),
]
for i, (en, cn) in enumerate(body):
    set_para_bilingual(doc.paragraphs[i], en, cn, size_pt=11)

# Signature block (paras 8+) left unchanged.

doc.save(OUT)
print("Saved template ->", OUT)
