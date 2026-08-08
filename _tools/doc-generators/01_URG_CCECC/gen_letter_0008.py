"""
Generate SLT-5312-WSN-CCC-0008 — Final Cure Notice to CCECC for MEI Pkg I
Reads the template: Your-Letter-Number Letter-Title.docx
"""
import sys, os, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

import docx
from docx.shared import Pt, Inches
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.enum.text import WD_ALIGN_PARAGRAPH

TEMPLATE = r"D:\Wison\Subcon_Payments\12.1 CCECC - MEI Pkg I\Corres\URG\Your-Letter-Number Letter-Title.docx"
OUTPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                      "SLT-5312-WSN-CCC-0008_FINAL CURE NOTICE MEI PKG I.docx")

doc = docx.Document(TEMPLATE)

# ============================================================
# Helpers
# ============================================================

def clear_cell_paragraphs(cell):
    """Remove all paragraphs from a cell."""
    for p in cell.paragraphs:
        p._element.getparent().remove(p._element)

def set_cell_text(cell, text, bold=False, size=Pt(10.5), font_name='Arial'):
    """Set a table cell to a single run of text."""
    # Remove existing paragraphs
    for p in cell.paragraphs:
        p._element.getparent().remove(p._element)
    # Add new paragraph
    new_p = OxmlElement('w:p')
    pPr = OxmlElement('w:pPr')
    # Match template: left-aligned with small spacing
    spacing = OxmlElement('w:spacing')
    spacing.set(qn('w:before'), '0')
    spacing.set(qn('w:after'), '0')
    spacing.set(qn('w:line'), '240')
    spacing.set(qn('w:lineRule'), 'auto')
    pPr.append(spacing)
    new_p.append(pPr)
    # Run
    r = OxmlElement('w:r')
    rPr = OxmlElement('w:rPr')
    rFonts = OxmlElement('w:rFonts')
    rFonts.set(qn('w:ascii'), font_name)
    rFonts.set(qn('w:hAnsi'), font_name)
    rPr.append(rFonts)
    if bold:
        b = OxmlElement('w:b')
        rPr.append(b)
    sz = OxmlElement('w:sz')
    sz.set(qn('w:val'), str(int(size.pt * 2)))  # half-points
    rPr.append(sz)
    r.append(rPr)
    t = OxmlElement('w:t')
    t.text = text
    t.set(qn('xml:space'), 'preserve')
    r.append(t)
    new_p.append(r)
    cell._tc.append(new_p)


def add_cell_paragraph(cell, text, bold=False, size=Pt(10.5), font_name='Arial'):
    """Add an additional paragraph to a cell (appends after existing)."""
    new_p = OxmlElement('w:p')
    pPr = OxmlElement('w:pPr')
    spacing = OxmlElement('w:spacing')
    spacing.set(qn('w:before'), '0')
    spacing.set(qn('w:after'), '0')
    spacing.set(qn('w:line'), '240')
    spacing.set(qn('w:lineRule'), 'auto')
    pPr.append(spacing)
    new_p.append(pPr)
    r = OxmlElement('w:r')
    rPr = OxmlElement('w:rPr')
    rFonts = OxmlElement('w:rFonts')
    rFonts.set(qn('w:ascii'), font_name)
    rFonts.set(qn('w:hAnsi'), font_name)
    rPr.append(rFonts)
    if bold:
        b = OxmlElement('w:b')
        rPr.append(b)
    sz = OxmlElement('w:sz')
    sz.set(qn('w:val'), str(int(size.pt * 2)))
    rPr.append(sz)
    r.append(rPr)
    t = OxmlElement('w:t')
    t.text = text
    t.set(qn('xml:space'), 'preserve')
    r.append(t)
    new_p.append(r)
    cell._tc.append(new_p)


def make_body_paragraph(text, font_name='Arial', font_size=Pt(11), bold=False,
                        space_after=Pt(6), alignment='both'):
    """Create a w:p OxmlElement for a body paragraph."""
    new_p = OxmlElement('w:p')
    pPr = OxmlElement('w:pPr')
    # Justification
    if alignment:
        jc = OxmlElement('w:jc')
        jc.set(qn('w:val'), alignment)
        pPr.append(jc)
    # Spacing
    spacing = OxmlElement('w:spacing')
    spacing.set(qn('w:after'), str(int(space_after.pt * 20)))  # twips
    spacing.set(qn('w:line'), '276')  # 1.15 line spacing (240 = single)
    spacing.set(qn('w:lineRule'), 'auto')
    pPr.append(spacing)
    new_p.append(pPr)
    # Run
    r = OxmlElement('w:r')
    rPr = OxmlElement('w:rPr')
    rFonts = OxmlElement('w:rFonts')
    rFonts.set(qn('w:ascii'), font_name)
    rFonts.set(qn('w:hAnsi'), font_name)
    rFonts.set(qn('w:eastAsia'), 'SimSun')
    rPr.append(rFonts)
    if bold:
        b = OxmlElement('w:b')
        rPr.append(b)
    sz = OxmlElement('w:sz')
    sz.set(qn('w:val'), str(int(font_size.pt * 2)))
    rPr.append(sz)
    szCs = OxmlElement('w:szCs')
    szCs.set(qn('w:val'), str(int(font_size.pt * 2)))
    rPr.append(szCs)
    r.append(rPr)
    t = OxmlElement('w:t')
    t.text = text
    t.set(qn('xml:space'), 'preserve')
    r.append(t)
    new_p.append(r)
    return new_p


# ============================================================
# 1. Fill Table 0 — Letterhead Info (7 rows x 3 cols)
# ============================================================
t0 = doc.tables[0]

# Row 0: ATTN: | Date: | 20 July 2026
# Keep ATTN label, clear name placeholder
set_cell_text(t0.rows[0].cells[0], "ATTN:", bold=True, size=Pt(9))
set_cell_text(t0.rows[0].cells[2], "20 July 2026", size=Pt(10))

# Row 1: (empty name field) | Our ref. No.: | SLT-5312-WSN-CCC-0008
set_cell_text(t0.rows[1].cells[0], "", size=Pt(10))
set_cell_text(t0.rows[1].cells[2], "SLT-5312-WSN-CCC-0008", size=Pt(10))

# Row 2: (empty title field) | Your ref. No.: | CCECC Ref: ...
set_cell_text(t0.rows[2].cells[0], "", size=Pt(10))
set_cell_text(t0.rows[2].cells[2],
              "CCECC Ref: SLT-5312-CCC-WSN-0003 (dated 17 July 2026)", size=Pt(10))

# Row 3: (empty) | Answer Required: | Yes
set_cell_text(t0.rows[3].cells[0], "", size=Pt(10))
set_cell_text(t0.rows[3].cells[2], "Yes", size=Pt(10))

# Row 4: (empty company field) | Response Date: | On or before 25 July 2026
set_cell_text(t0.rows[4].cells[0], "", size=Pt(10))
set_cell_text(t0.rows[4].cells[2], "On or before 25 July 2026", size=Pt(10))

# Row 5: (empty company field) | Page: | 1 of 3
set_cell_text(t0.rows[5].cells[0], "", size=Pt(10))
set_cell_text(t0.rows[5].cells[2], "1 of 3", size=Pt(10))

# Row 6: empty — leave as-is

# ============================================================
# 2. Fill Table 1 — Project / Subject (2 rows x 2 cols)
# ============================================================
t1 = doc.tables[1]

set_cell_text(t1.rows[0].cells[1],
    "RUWAIS SULPHUR GRANULATION PLANT AT RSHT - 2 "
    "FOR HAIL & GHASHA PROJECT (1005312)",
    size=Pt(10.5), bold=True)

set_cell_text(t1.rows[1].cells[1],
    "REJECTION OF SUBCONTRACTOR'S CLARIFICATION AND FINAL CURE NOTICE: "
    "MANDATORY CORRECTIVE ACTIONS FOR MEI PACKAGE I BY 30 JULY 2026",
    size=Pt(10.5), bold=True)
add_cell_paragraph(t1.rows[1].cells[1],
    "主题：对分包商澄清的驳回及最终整改通知：勒令MEI包件I于2026年7月30日前完成全部纠正措施",
    size=Pt(10.5))


# ============================================================
# 3. Replace body paragraphs
# ============================================================

# Find the "Sincerely yours," paragraph
sincerely_idx = None
for i, p in enumerate(doc.paragraphs):
    if "Sincerely yours" in p.text:
        sincerely_idx = i
        break

if sincerely_idx is None:
    raise SystemExit("ERROR: Could not find 'Sincerely yours,' paragraph in template.")

sig_elem = doc.paragraphs[sincerely_idx]._p

# Remove old body placeholder paragraphs (indices 0 to sincerely_idx - 1)
old_elems = []
for i in range(sincerely_idx):
    old_elems.append(doc.paragraphs[i]._p)

for elem in old_elems:
    doc.element.body.remove(elem)

# Body paragraphs in order (EN-CN paired, bilingual letter)
body_texts = [
    # --- Salutation ---
    "Dear Sirs,",

    # --- Para 1 EN: Escalation + Attachments 1 & 2 ---
    ("The Subcontractor is solemnly notified that both the Employer (ADNOC GAS) and "
     "CONTRACTOR's senior corporate management have expressed the gravest concern and "
     "absolute dissatisfaction with CCECC's ongoing non-performance. Your failure to "
     "establish execution readiness has triggered critical escalation under the Main "
     "Contract. For direct reference regarding the Employer's severe positioning and "
     "our formal prior warnings, please refer to Attachment 1 (ADNOC Directive Ref: "
     "AG/PT2-3/OUT/2026/6980) and Attachment 2 (WISON Urgency Letter Ref: "
     "SLT-5312-WSN-CCC-0005) attached hereto."),

    # --- Para 1 CN ---
    ("贵司须严肃知悉，业主（ADNOC GAS）及我司高层管理团队对贵司持续性的不履约行为"
     "表示最严厉的关切与极度不满。贵司未能建立基本的开工就绪状态，已引发了主合同项下"
     "的严重管理升级。关于业主的严厉立场及我司前期的正式书面警告，详见本函后附的附件一"
     "（业主ADNOC指令，文号：AG/PT2-3/OUT/2026/6980）及附件二（总包商紧急敦促函，"
     "文号：SLT-5312-WSN-CCC-0005）。"),

    # --- Para 2 EN: Rejection of CCECC's reply + Attachment 3 ---
    ("CONTRACTOR hereby formally acknowledges receipt of your letter Ref: "
     "SLT-5312-CCC-WSN-0003 dated 17 July 2026. Following a rigorous review, "
     "CONTRACTOR categorically rejects all arguments, excuses, and the reservation "
     "of rights put forward by the Subcontractor—including your claims regarding "
     "engineering deliverables and workfront handovers. Factual evidence and site "
     "data conclusively demonstrate that the severe delays to the Key Milestone "
     "stem entirely from your own resource shortages and organizational deficiencies. "
     "The comprehensive matrix of defaults and contractual risks is definitively "
     "cataloged in Attachment 3 (Performance Deficiency Report dated 20 July 2026). "
     "This letter stands as a formal notification and final warning; specific "
     "operational details shall be reviewed exclusively via the attached report."),

    # --- Para 2 CN ---
    ("同时，总包商特此正式确认收到贵司于2026年7月17日发出的回函（文号："
     "SLT-5312-CCC-WSN-0003）。经严格核实，总包商坚决驳回贵司就关键里程碑"
     "严重逾期所提出的全部辩解、推诿借口及权利保留主张——包括贵司关于图纸未出全"
     "及工作面未移交的说辞。事实证据与现场数据确凿表明，当前的严重延误完全源于"
     "贵司自身的资源动员不力和组织管理缺陷。具体的违约矩阵及合同风险已完整收录于"
     "附件三（《现场履约缺陷专项报告》，日期为2026年7月20日）。本函重点在于"
     "正式陈述与严肃警告，相关具体事实与细节以该附件报告为准。"),

    # --- Para 3 EN: Mandatory cure period ---
    ("The Subcontractor is hereby given a MANDATORY AND FINAL CURE PERIOD UNTIL "
     "30 JULY 2026 to completely rectify all management, manpower, technical "
     "documentation, site infrastructure, and equipment deficiencies detailed "
     "in the Attachments."),

    # --- Para 3 CN ---
    ("总包商特此向贵司下达强制性最终整改期限，限贵司于2026年7月30日前，必须将"
     "附件中所列的所有关于管理体系、人力资源、技术文件、临时设施及施工机具的缺陷"
     "全面整改并闭合到位。"),

    # --- Para 4 EN: Consequences of failure ---
    ("Should the Subcontractor fail to achieve full compliance and remedy all "
     "defaults within this mandatory timeframe, CONTRACTOR shall, without further "
     "notice, proceed to exercise any or all contractual rights and remedies "
     "available under the Subcontract Agreement, at law or in equity. This includes, "
     "but is not limited to, the immediate initiation of Clause 33 (Termination for "
     "Default), partial or total omission of the Scope of Works pursuant to Clause "
     "5.6, and calls on the Performance Guarantees. CCECC shall be held solely and "
     "exclusively liable for all associated liquidated damages, cost overruns, "
     "third-party replacement costs, and critical path impacts to the overall "
     "Project schedule."),

    # --- Para 4 CN ---
    ("若贵司未能在此强制时限内达到完全合规要求并纠正所有违约行为，总包商将无需"
     "另行通知，立即采取《分包合同》项下、适用法律或衡平法赋予的所有合同权利与"
     "救济措施。这包括但不限于：立即启动第33条违约终止合同程序、依据第5.6条剥离"
     "或部分/全部削减工程范围，以及没收履约保函。贵司（中土）将独立且无条件地承担"
     "由此引发的所有误期违约金、成本超支、第三方替代成本以及对项目整体关键路径"
     "造成的全部工期损失责任。"),

    # --- Para 5 EN: Without prejudice ---
    ("This Notice is issued strictly without prejudice to any rights, claims, and "
     "remedies available to CONTRACTOR under the Subcontract, at law or in equity."),

    # --- Para 5 CN ---
    ("本通知的发出绝不损害总包商依据分包合同、适用法律或衡平法所享有的任何其他"
     "权利、索赔与救济。"),
]

# Insert all body paragraphs in reverse order (each goes before the signature)
for text in body_texts:
    is_salutation = text.startswith("Dear Sirs")
    new_p = make_body_paragraph(
        text,
        bold=is_salutation,
        space_after=Pt(4) if not is_salutation else Pt(10)
    )
    sig_elem.addprevious(new_p)

# ============================================================
# 4. Update CC line and add Enclosures
# ============================================================

# Find CC paragraph (last paragraph in signature block)
cc_idx = None
for i, p in enumerate(doc.paragraphs):
    if p.text.strip().startswith("CC:"):
        cc_idx = i
        break

if cc_idx:
    # Clear old CC content
    for run in doc.paragraphs[cc_idx].runs:
        run._r.getparent().remove(run._r)
    # We'll add enclosure after CC — insert new paragraphs after CC para
    cc_elem = doc.paragraphs[cc_idx]._p

    # CC line
    cc_para = make_body_paragraph("CC: N/A", font_size=Pt(10), space_after=Pt(2))
    cc_elem.addnext(cc_para)

    # Enclosures header
    encl_head = make_body_paragraph("Encl / 附件:", font_size=Pt(10),
                                    bold=True, space_after=Pt(2))
    cc_para.addnext(encl_head)

    # Attachment lines
    attachments = [
        "Attachment 1: Employer (ADNOC GAS) Letter Ref: AG/PT2-3/OUT/2026/6980",
        "Attachment 2: CONTRACTOR (WISON) Letter Ref: SLT-5312-WSN-CCC-0005",
        "Attachment 3: Performance Deficiency Report (Dated 20/07/2026)",
    ]
    prev = encl_head
    for att_text in attachments:
        att_para = make_body_paragraph(att_text, font_size=Pt(10), space_after=Pt(1))
        prev.addnext(att_para)
        prev = att_para

    # Remove the old CC paragraph element
    doc.element.body.remove(cc_elem)

# ============================================================
# 5. Save
# ============================================================
doc.save(OUTPUT)
print(f"文档生成成功：{OUTPUT}")
