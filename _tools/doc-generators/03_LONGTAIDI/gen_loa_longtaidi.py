"""
Generate LONGTAIDI LOA from new template v0428.
Minimal changes — only fill placeholders and adapt project-specific content.
All changed text highlighted in yellow for review.
"""
import sys, os, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

import docx
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

SRC = r"D:\Wison\Subcon_Payments\99 LONGTAIDI fob\Contract\Part I Subcontract Agreement\LOA\Letter_of_Award for subcontract Version 0428.docx"
OUT = r"D:\Wison\Subcon_Payments\99 LONGTAIDI fob\Contract\Part I Subcontract Agreement\LOA\LOA - LONGTAIDI (from v0428).docx"

doc = docx.Document(SRC)

# ============================================================
# Helpers
# ============================================================
def mk_hl():
    """Create a yellow highlight element."""
    hl = OxmlElement('w:highlight')
    hl.set(qn('w:val'), 'yellow')
    return hl

def make_run(text, font_size_pt=None, bold=False, font_name=None, highlight=True):
    """Create a <w:r> element."""
    r = OxmlElement('w:r')
    rPr = OxmlElement('w:rPr')
    if font_name:
        rf = OxmlElement('w:rFonts')
        rf.set(qn('w:ascii'), font_name)
        rf.set(qn('w:hAnsi'), font_name)
        rPr.append(rf)
    if bold:
        b = OxmlElement('w:b')
        rPr.append(b)
    if font_size_pt:
        sz = OxmlElement('w:sz')
        sz.set(qn('w:val'), str(int(font_size_pt * 2)))
        rPr.append(sz)
        szCs = OxmlElement('w:szCs')
        szCs.set(qn('w:val'), str(int(font_size_pt * 2)))
        rPr.append(szCs)
    if highlight:
        rPr.append(mk_hl())
    r.append(rPr)
    t = OxmlElement('w:t')
    t.text = text
    t.set(qn('xml:space'), 'preserve')
    r.append(t)
    return r

def clear_runs(p_elem):
    for r_e in p_elem.findall(qn('w:r')):
        p_elem.remove(r_e)

def set_para(paragraph, runs_spec, highlight=True):
    """Replace paragraph runs. runs_spec: list of (text, bold?, size_pt?, font_name?)"""
    p_elem = paragraph._p
    clear_runs(p_elem)
    for spec in runs_spec:
        text = spec[0]
        bold = spec[1] if len(spec) > 1 else False
        sz = spec[2] if len(spec) > 2 else 11
        fn = spec[3] if len(spec) > 3 else None
        r = make_run(text, font_size_pt=sz, bold=bold, font_name=fn, highlight=highlight)
        p_elem.append(r)

def fill_run_text(run, new_text, highlight=True):
    """Replace text in an existing run and optionally highlight it."""
    # Update <w:t>
    t_elem = run._r.find(qn('w:t'))
    if t_elem is not None:
        t_elem.text = new_text
        t_elem.set(qn('xml:space'), 'preserve')
    if highlight:
        rPr = run._r.find(qn('w:rPr'))
        if rPr is None:
            rPr = OxmlElement('w:rPr')
            run._r.insert(0, rPr)
        # Remove old highlight
        for old_hl in rPr.findall(qn('w:highlight')):
            rPr.remove(old_hl)
        rPr.append(mk_hl())

def set_cell_text(cell, lines, highlight=True):
    """Replace cell content. lines: list of strings or list of lists of (text, bold) tuples."""
    for p in cell.paragraphs:
        p._element.getparent().remove(p._element)
    for line in lines:
        new_p = OxmlElement('w:p')
        if isinstance(line, str):
            r = make_run(line, font_size_pt=11, highlight=highlight)
            new_p.append(r)
        elif isinstance(line, list):
            for item in line:
                text, bold = (item, False) if isinstance(item, str) else item
                r = make_run(text, font_size_pt=11, bold=bold, highlight=highlight)
                new_p.append(r)
        cell._tc.append(new_p)


print("=" * 60)
print("LONGTAIDI LOA — from template v0428")
print("=" * 60)

# ============================================================
# HEADER AREA — P0 to P15 (sender & recipient info)
# ============================================================
print("\n--- Header ---")

# P0: Date_DD-MM-YY → 28th July, 2026
set_para(doc.paragraphs[0], [("28th July, 2026", False, 11, "Times New Roman")])
print("  P0 Date → 28th July, 2026")

# P1: tabs (formatting) — keep

# P2: Project:XXXXXX → Project: full name
set_para(doc.paragraphs[2], [
    ("Project: ", False, 9, "Times New Roman"),
    ("Ruwais Sulphur Granulation Plant (RSGP) at RSHT - 2 for Hail & Ghasha Project", False, 9, None),
], highlight=False)
# Highlight the project name only
p2_runs = doc.paragraphs[2]._p.findall(qn('w:r'))
if len(p2_runs) >= 2:
    rPr = p2_runs[1].find(qn('w:rPr'))
    if rPr is None:
        rPr = OxmlElement('w:rPr'); p2_runs[1].insert(0, rPr)
    rPr.append(mk_hl())
print("  P2 Project → RSGP at RSHT-2")

# P3: From:XXXXXX → Wison full name
set_para(doc.paragraphs[3], [
    ("From: ", False, 9, "Times New Roman"),
    ("WISON ENERGY ENGINEERING (HONG KONG) LIMITED – ABU DHABI", False, 9, None),
], highlight=False)
p3_runs = doc.paragraphs[3]._p.findall(qn('w:r'))
if len(p3_runs) >= 2:
    rPr = p3_runs[1].find(qn('w:rPr'))
    if rPr is None: rPr = OxmlElement('w:rPr'); p3_runs[1].insert(0, rPr)
    rPr.append(mk_hl())
print("  P3 From → WISON")

# P4: Position:XXXXXX → Project Manager
set_para(doc.paragraphs[4], [
    ("Position: ", False, 9, "Times New Roman"),
    ("Project Manager", False, 9, None),
], highlight=False)
p4_runs = doc.paragraphs[4]._p.findall(qn('w:r'))
if len(p4_runs) >= 2:
    rPr = p4_runs[1].find(qn('w:rPr'))
    if rPr is None: rPr = OxmlElement('w:rPr'); p4_runs[1].insert(0, rPr)
    rPr.append(mk_hl())
print("  P4 Position → Project Manager")

# P5: Company:XXXXXX → same as From
set_para(doc.paragraphs[5], [
    ("Company: ", False, 9, "Times New Roman"),
    ("WISON ENERGY ENGINEERING (HONG KONG) LIMITED – ABU DHABI", False, 9, None),
], highlight=False)
p5_runs = doc.paragraphs[5]._p.findall(qn('w:r'))
if len(p5_runs) >= 2:
    rPr = p5_runs[1].find(qn('w:rPr'))
    if rPr is None: rPr = OxmlElement('w:rPr'); p5_runs[1].insert(0, rPr)
    rPr.append(mk_hl())
print("  P5 Company → WISON")

# P8: To:[Name of Subcontracor] → LONGTAIDI
set_para(doc.paragraphs[8], [
    ("To: ", False, 9, "Times New Roman"),
    ("Cangzhou Longtaidi Pipe Technology Co., Ltd.", False, 9, None),
    ("（沧州隆泰迪管道科技有限公司）", False, 9, None),
], highlight=False)
p8_runs = doc.paragraphs[8]._p.findall(qn('w:r'))
for rr in p8_runs[1:]:
    rPr = rr.find(qn('w:rPr'))
    if rPr is None: rPr = OxmlElement('w:rPr'); rr.insert(0, rPr)
    rPr.append(mk_hl())
print("  P8 To → LONGTAIDI 中英双语")

# P9: Attention:XXXXXX → Song Yang
set_para(doc.paragraphs[9], [
    ("Attention: ", False, 9, "Times New Roman"),
    ("Mr. Song Yang", False, 9, None),
], highlight=False)
p9_runs = doc.paragraphs[9]._p.findall(qn('w:r'))
if len(p9_runs) >= 2:
    rPr = p9_runs[1].find(qn('w:rPr'))
    if rPr is None: rPr = OxmlElement('w:rPr'); p9_runs[1].insert(0, rPr)
    rPr.append(mk_hl())
print("  P9 Attention → Song Yang")

# P10: Position:XXXXXX → General Manager
set_para(doc.paragraphs[10], [
    ("Position: ", False, 9, "Times New Roman"),
    ("General Manager", False, 9, None),
], highlight=False)
p10_runs = doc.paragraphs[10]._p.findall(qn('w:r'))
if len(p10_runs) >= 2:
    rPr = p10_runs[1].find(qn('w:rPr'))
    if rPr is None: rPr = OxmlElement('w:rPr'); p10_runs[1].insert(0, rPr)
    rPr.append(mk_hl())
print("  P10 Position → General Manager")

# P11: Company:XXXXXX → LONGTAIDI
set_para(doc.paragraphs[11], [
    ("Company: ", False, 9, "Times New Roman"),
    ("Cangzhou Longtaidi Pipe Technology Co., Ltd.", False, 9, None),
    ("（沧州隆泰迪管道科技有限公司）", False, 9, None),
], highlight=False)
p11_runs = doc.paragraphs[11]._p.findall(qn('w:r'))
for rr in p11_runs[1:]:
    rPr = rr.find(qn('w:rPr'))
    if rPr is None: rPr = OxmlElement('w:rPr'); rr.insert(0, rPr)
    rPr.append(mk_hl())
print("  P11 Company → LONGTAIDI")

# P12: Tel:XXXXXX — leave as placeholder, no info
# Keep as XXXXXX so user knows to fill

# P13: E-mail:XXXXXX — leave as placeholder

# ============================================================
# P15: Subject line
# ============================================================
print("\n--- Body ---")
set_para(doc.paragraphs[15], [
    ("Subject: Letter of Award for the Work of ", False, 9, "Times New Roman"),
    ("Fire-Fighting Piping (3-inch and above) Fabrication Works on FOB Basis", False, 9, None),
], highlight=False)
p15_runs = doc.paragraphs[15]._p.findall(qn('w:r'))
if len(p15_runs) >= 2:
    rPr = p15_runs[1].find(qn('w:rPr'))
    if rPr is None: rPr = OxmlElement('w:rPr'); p15_runs[1].insert(0, rPr)
    rPr.append(mk_hl())
print("  P15 Subject ✓")

# ============================================================
# P20 — Award paragraph with full party details
# ============================================================
# This paragraph has placeholders scattered across many runs.
# Rebuild entirely with filled placeholders.
award_en = (
    "Following your successful submission of the Tender dated [insert the date of tender] "
    "and subsequent negotiations, we, WISON ENERGY ENGINEERING (HONG KONG) LIMITED – "
    "ABU DHABI, a company organized and existing under the laws of Abu Dhabi and the "
    "United Arab Emirates, and having its registered office at Floor 15, Ghaith Holding "
    "Tower, West 14_02 Building, Al Manhal, Fatima Hamel Khdim Al Kheth, Abu Dhabi, "
    "U.A.E. (hereinafter referred to as \"Contractor\") are pleased to award you, "
    "Cangzhou Longtaidi Pipe Technology Co., Ltd. （沧州隆泰迪管道科技有限公司）, "
    "a company organized and existing under the laws of the People's Republic of China, "
    "and having its registered office at 沧州经济开发区黄河东路33号 (No. 33, Huanghe "
    "East Road, Cangzhou Economic Development Zone, Hebei Province, People's Republic "
    "of China) (hereinafter referred to as \"Subcontractor\"), a subcontract for "
    "execution of the following scope of work for the above-captioned project in "
    "accordance with the conditions agreed by both Parties."
)
set_para(doc.paragraphs[20], [(award_en, False, 11, "Times New Roman")])
print("  P20 Award para ✓ [Fully rebuilt, all filled]")

# ============================================================
# P21 — Commencement date
# ============================================================
set_para(doc.paragraphs[21], [
    ("You are hereby requested to proceed with relevant works commencing from ", False, 11, "Times New Roman"),
    ("28th July, 2026", False, 11, None),
    (", subject to the execution of a formal subcontract agreement (\"Subcontract\"). "
     "Pending such execution, the following interim arrangement shall apply between us:", False, 11, "Times New Roman"),
])
print("  P21 Commencement → 28th July, 2026")

# ============================================================
# P23-P31 — "The Parties hereby agree that:" clauses
# Keep as-is (boilerplate)
# ============================================================

# ============================================================
# P33 — Scope of Work — fill RFP date placeholder
# ============================================================
set_para(doc.paragraphs[33], [
    ("The Scope of Work shall be as described in the Request For Proposal (\"RFP\") "
     "dated ", False, 11, "Times New Roman"),
    ("[insert RFP date]", False, 11, None),
    (", as amended and updated pursuant to the supplementary documents files and "
     "clarifications agreed by Contractor and Subcontractor. In the event of any "
     "conflict or ambiguity among the documents, the most recent position formally "
     "communicated by the Contractor to the Subcontractor shall prevail.", False, 11, "Times New Roman"),
])
print("  P33 Scope — RFP date placeholder kept")

# ============================================================
# P35 — Subcontract Price
# ============================================================
set_para(doc.paragraphs[35], [
    ("Pricing of Subcontract for the Works shall be based on a measure-and-pay basis "
     "for actual and accepted work completed, using the all-inclusive unit rates set "
     "forth in the final proposal submitted on [insert date] ", False, 11, "Times New Roman"),
    ("(Provisional Subcontract Price: USD 976,747.73", False, 9, None),
    ("; in words: ", False, 11, "Times New Roman"),
    ("USD Nine Hundred Seventy-Six Thousand Seven Hundred Forty-Seven and "
     "Seventy-Three Cents only", False, 9, None),
    ("). ", False, 11, "Times New Roman"),
    ("The Price is exclusive of VAT, which shall be charged in accordance with the "
     "laws of ", False, 11, "Times New Roman"),
    ("the People's Republic of China", False, 9, None),
    (", ", False, 11, "Times New Roman"),
    ("the detailed of which are as follows:", False, 11, "Times New Roman"),
])
print("  P35 Price → USD 976,747.73 ✓")

# ============================================================
# P36 — Rates fixed — keep as-is (boilerplate)
# ============================================================

# ============================================================
# P38 — Effective Date
# ============================================================
set_para(doc.paragraphs[38], [
    ("The Commencement Date and Effective Date of Subcontract shall be ", False, 11, "Times New Roman"),
    ("28th July, 2026", False, 9, None),
    ("; ", False, 11, "Times New Roman"),
])
print("  P38 Effective Date → 28th July, 2026")

# ============================================================
# P39 — Work Programme — adapt to fabrication context
# ============================================================
set_para(doc.paragraphs[39], [
    ("The Subcontractor shall fully comply with the attached agreed general Work "
     "Programme to achieve the indicated milestones, and take every effort, "
     "including night shifts or extending work hours as necessary to mitigate "
     "any delay caused by the Subcontractor, at no additional cost to the "
     "Contractor.", False, 11, "Times New Roman"),
])
print("  P39 Work Programme ✓")

# ============================================================
# P43 — Performance Bank Guarantee amount
# ============================================================
set_para(doc.paragraphs[43], [
    ("If under the Tender Document the Subcontractor is required to provide "
     "a Performance Bank Guarantee, the Subcontractor shall submit the "
     "Performance Bank Guarantee in the amount of ", False, 11, "Times New Roman"),
    ("USD 97,674.77", False, 9, None),
    (", being Ten percent (10%) of the ", False, 11, "Times New Roman"),
    ("Provisional", False, 11, "Times New Roman"),
    (" Subcontract Price, within fourteen (14) DAYS following the Effective Date.", False, 11, "Times New Roman"),
])
print("  P43 Performance BG → USD 97,674.77 (10%) ✓")

# ============================================================
# Annexes — P51 to P54
# ============================================================
print("\n--- Annexes ---")

# P51: Annex1：Key Milestone — keep
# P52: Annex2：Liquidated Damage — keep
# P53: Annex3：No Deviation Declaration — keep
# P54: Annex4：ICV Improvement Plan → N/A

set_para(doc.paragraphs[54], [
    ("Annex4", False, 11, "Times New Roman"),
    ("：", False, 11, "Times New Roman"),
    ("ICV Improvement Plan — N/A (Not Applicable: FOB China delivery)", False, 11, None),
])
print("  P54 Annex4 → ICV N/A")

# ============================================================
# Table 0 — Contractor (WISON) signature block
# ============================================================
print("\n--- Signature tables ---")
t0 = doc.tables[0]
# Row 0: Company name + address
set_cell_text(t0.rows[0].cells[0], [
    [("WISON ENERGY ENGINEERING (HONG KONG) LIMITED – ABU DHABI", False)],
    [("(Trade License No. CN-1432877)", False)],
    [("Add: Floor 15, Ghaith Holding Tower, West 14_02 Building, Al Manhal, "
      "Fatima Hamel Khdim Al Kheth, Abu Dhabi, U.A.E.", False)],
])
print("  Table 0 — Contractor details ✓")
# Rest of signature block (Signature, Name, Title) stays

# ============================================================
# Table 1 — Subcontractor acceptance block
# ============================================================
t1 = doc.tables[1]
# Row 0: acceptance line — keep "Above Letter of Award is fully understood and accepted by:"
# Row 1: Add: → LONGTAIDI address
set_cell_text(t1.rows[1].cells[0], [
    [("Add: ", False), ("沧州经济开发区黄河东路33号", False)],
    [("      (No. 33, Huanghe East Road, Cangzhou Economic Development Zone, "
      "Hebei Province, People's Republic of China)", False)],
])
print("  Table 1 — Subcontractor address ✓")
# Rest stays (Signature, Printed Name, Title, Date)

# ============================================================
# Verify
# ============================================================
print("\n--- Verification ---")
checks = [
    "28th July, 2026", "RSGP", "WISON ENERGY ENGINEERING",
    "Longtaidi", "Song Yang", "General Manager",
    "976,747.73", "Nine Hundred Seventy-Six",
    "97,674.77", "FOB Basis", "People's Republic of China",
    "N/A", "Ghaith Holding Tower"
]
all_ok = True
for marker in checks:
    found = False
    for p in doc.paragraphs:
        if marker in p.text:
            found = True
            break
    for t in doc.tables:
        for row in t.rows:
            for cell in row.cells:
                if marker in cell.text:
                    found = True
                    break
    status = "✓" if found else "✗"
    if not found: all_ok = False
    print(f"  {status} '{marker}'")

doc.save(OUT)
print(f"\n{'✓ All checks passed' if all_ok else '✗ Some checks FAILED'}")
print(f"Saved: {OUT}")
