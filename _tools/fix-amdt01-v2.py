#!/usr/bin/env python3
"""
Amdt 01 corrections v2 — paragraph full-text level approach.
Solves run-splitting issue where "第" + "?" + "条" are in separate runs.
"""
import re, copy
from docx import Document
from docx.shared import Pt
from pathlib import Path

SRC = Path(r"D:\Wison\Subcon_Payments\12.1 CCECC - MEI Pkg I\Contract\02_Amdt 01\Amdt 01_MEI Pkg I (Revised) V2 .docx")
DST = SRC.parent / (SRC.stem + "_CORRECTED_v2.docx")

doc = Document(str(SRC))


def apply_to_para(para, old, new):
    """Reduce all runs to one with full text, then replace old→new in it."""
    old_text = para.text
    if old not in old_text:
        return False
    new_text = old_text.replace(old, new)
    # Clear all runs
    for run in para.runs:
        run.text = ""
    # Place entire corrected text in first run, preserving its font
    if para.runs:
        para.runs[0].text = new_text
    else:
        r = para.add_run(new_text)
        r.font.size = Pt(10)
    return True


def apply_to_para_multi(para, replacements):
    """Apply multiple old→new replacements on paragraph full text."""
    text = para.text
    modified = False
    for old, new in replacements:
        if old in text:
            text = text.replace(old, new)
            modified = True
    if not modified:
        return False
    for run in para.runs:
        run.text = ""
    if para.runs:
        para.runs[0].text = text
    else:
        r = para.add_run(text)
        r.font.size = Pt(10)
    return True


changes = []

# ============================================================
# CATEGORY 1: CROSS-REFERENCE NUMBERING
# ============================================================

# 1. P13: Recitals 1 — 第 4.3 条 → 第 3.2(b) 条
if apply_to_para(doc.paragraphs[13], "第 4.3 条", "第 3.2(b) 条"):
    changes.append("P13: 第 4.3 条 → 第 3.2(b) 条")

# Also P13 English: Clause 4.3 → Clause 3.2(b)
if apply_to_para(doc.paragraphs[13], "Clause 4.3", "Clause 3.2(b)"):
    changes.append("P13: Clause 4.3 → Clause 3.2(b)")

# 2. P14: Recitals 2 — 第 ?条 → 第 6 条  (check full text for "第?条" or "第 ? 条" variants)
for old, new in [("第 ?条", "第 6 条"), ("第 ? 条", "第 6 条"), ("第?条", "第 6 条")]:
    if apply_to_para(doc.paragraphs[14], old, new):
        changes.append(f"P14: '{old}' → '{new}'")
        break

# 3. P23: 3.1 — 第 ?条 → 第 6 条 (multiple variants)
for old, new in [("第 ?条", "第 6 条"), ("第 ? 条", "第 6 条"), ("第?条", "第 6 条"), ("?条执行", "第 6 条执行"), ("? 条执行", "第 6 条执行")]:
    if apply_to_para(doc.paragraphs[23], old, new):
        changes.append(f"P23: '{old}' → '{new}'")
        break

# 4. P28: 6.1 → 4.1 (the paragraph starts with "6.1" in English)
if apply_to_para(doc.paragraphs[28], "6.1  Upon completion", "4.1  Upon completion"):
    changes.append("P28: 6.1 → 4.1")

# 5. P29: 6.2 → 4.2 + Clause 6 → Clause 4 + Clause 8 → Clause 6 + 第 ? 条 → 第 6 条
apply_to_para_multi(doc.paragraphs[29], [
    ("6.2  For the avoidance", "4.2  For the avoidance"),
    ("this Clause 6 ", "this Clause 4 "),
    ("this Clause 6.", "this Clause 4."),
    ("Clause 8 below", "Clause 6 below"),
    ("第 ? 条", "第 6 条"),
    ("第 ?条", "第 6 条"),
])
changes.append("P29: 6.2→4.2, Clause 6→4, Clause 8→6, 第 ? 条→第 6 条")

# 6. P31: Clause 8 → Clause 6
if apply_to_para(doc.paragraphs[31], "Clause 8", "Clause 6"):
    changes.append("P31: Clause 8 → Clause 6")

# 7. P33: Clause 8 → Clause 6; Clause 6.1 → Clause 4.1
apply_to_para_multi(doc.paragraphs[33], [
    ("Clause 8 hereof", "Clause 6 hereof"),
    ("Clause 6.1", "Clause 4.1"),
])
changes.append("P33: Clause 8→6, Clause 6.1→4.1")

# 8. P34: 7.3.3 → 5.1.2
if apply_to_para(doc.paragraphs[34], "7.3.3", "5.1.2"):
    changes.append("P34: 7.3.3 → 5.1.2")
elif apply_to_para(doc.paragraphs[34], "7 .3 .3", "5.1.2"):
    changes.append("P34: 7.3.3 → 5.1.2 (spaced)")

# 9. P36: 8.1 → 6.1
if apply_to_para(doc.paragraphs[36], "8.1 ", "6.1 "):
    changes.append("P36: 8.1 → 6.1")

# 10. P41: (c) → (b) at start
if apply_to_para(doc.paragraphs[41], "(c)  nothing in this Amendment", "(b)  nothing in this Amendment"):
    changes.append("P41: (c) → (b)")

# 11. P43: 9.1 → 7.1
if apply_to_para(doc.paragraphs[43], "9.1  This Amendment constitutes", "7.1  This Amendment constitutes"):
    changes.append("P43: 9.1 → 7.1")

# 12. P45: 10.1 → 8.1
if apply_to_para(doc.paragraphs[45], "10.1  This Amendment is executed", "8.1  This Amendment is executed"):
    changes.append("P45: 10.1 → 8.1")

# ============================================================
# CATEGORY 2: CHINESE LOGIC IMPROVEMENTS
# ============================================================

# 1. P23 (3.1): Add evidence chain sentence after "第 6 条执行。"
text = doc.paragraphs[23].text
if "第 6 条执行" in text and "不免除" not in text:
    new_text = text.replace(
        "第 6 条执行。",
        "第 6 条执行。分包商确认，上述范围核减剥离不免除、不减轻其作为本工程总实施方对预制全过程的全面管理与终局质量责任，分包商对加工商的管理责任按照本协议第 6 条执行。"
    )
    for run in doc.paragraphs[23].runs:
        run.text = ""
    if doc.paragraphs[23].runs:
        doc.paragraphs[23].runs[0].text = new_text
    changes.append("P23: Added evidence chain sentence to 3.1")

# 2. P25 (3.2a): Add time limit for confirmation
text = doc.paragraphs[25].text
if "三方确认无异议" in text and "7 个工作日" not in text:
    new_text = text.replace(
        "三方确认无异议",
        "三方确认无异议。（分包商应在收到结算报告后 7 个工作日内完成复核并提出书面意见，逾期未提出视为无异议。经确认或视为无异议的最终金额，承包商有权直接从分包商任何应付款项中扣除。）"
    )
    for run in doc.paragraphs[25].runs:
        run.text = ""
    if doc.paragraphs[25].runs:
        doc.paragraphs[25].runs[0].text = new_text
    changes.append("P25: Added time limit to 3.2(a)")

# 3. P38 (6.1b): Fix (IRN? Qrc?) or similar patterns
text = doc.paragraphs[38].text
if "IRN?" in text or "Qrc?" in text or "IRN / QRC" in text:
    new_text = re.sub(r'IRN\s*\?\s*(Qrc|QRC)\s*\?', 'IRN/QRC', text)
    new_text = re.sub(r'（\s*IRN\s*\?\s*(?:Qrc|QRC)\s*\?\s*）', '（IRN/QRC）', new_text)
    # Also fix the half-width parenthesis variants
    new_text = re.sub(r'\(IRN/QRC\)', '(IRN/QRC)', new_text)
    # Fix: （IRN） (QRC) → （IRN/QRC）
    new_text = re.sub(r'（\s*IRN\s*）\s*\(\s*QRC\s*\)', '（IRN/QRC）', new_text)
    new_text = re.sub(r'IRN\s*\?\s*Q\s*rc\s*\?', 'IRN/QRC', new_text)
    for run in doc.paragraphs[38].runs:
        run.text = ""
    if doc.paragraphs[38].runs:
        doc.paragraphs[38].runs[0].text = new_text
    changes.append("P38: Fixed IRN?/Qrc? → IRN/QRC")

# ============================================================
# CATEGORY 3: ENGLISH ALIGNMENT
# ============================================================

# 1. P26 (3.2b): Ensure English includes dead freight, port demurrage etc.
text = doc.paragraphs[26].text
if "25% of All Actually Incurred Logistics" in text and "dead freight" not in text:
    # Replace the English portion
    old_en = "international transportation segment expenditures (explicitly including, without limitation, all real-world marine cargo insurance, loading port"
    new_en = (
        "international transportation segment expenditures "
        "(explicitly including, without limitation, all real-world marine cargo insurance, "
        "loading port terminal handling charges, destination customs clearance fees, "
        "UAE import regulatory duties, as well as any and all actually occurring dead freight, "
        "port demurrage, container detention, or shipping re-booking and cancellation charges"
    )
    if old_en in text:
        new_text = text.replace(old_en, new_en)
        for run in doc.paragraphs[26].runs:
            run.text = ""
        if doc.paragraphs[26].runs:
            doc.paragraphs[26].runs[0].text = new_text
        changes.append("P26: Expanded English 3.2(b) logistics text")

# 2. P28 (4.1): Replace English with simplified version
text = doc.paragraphs[28].text
new_eng = (
    "4.1  Upon completion of prefabrication, the Fabricator shall be responsible for "
    "container collection, stuffing, and packaging in accordance with the Contractor's "
    "shipping instructions on an FOB basis, and handling export customs formalities; "
    "international sea freight, destination customs clearance, and inland transportation "
    "within the UAE shall be arranged by the Contractor, with the relevant costs shared "
    "in accordance with Clause 3.2(b).\n"
)
# Find where Chinese starts and prepend new English
cn_marker = "加工完成后，加工商须按照"
if cn_marker in text:
    idx = text.index(cn_marker)
    new_text = new_eng + text[idx:]
    for run in doc.paragraphs[28].runs:
        run.text = ""
    if doc.paragraphs[28].runs:
        doc.paragraphs[28].runs[0].text = new_text
    changes.append("P28: Replaced English 4.1 with simplified version")

# ============================================================
# CATEGORY 4: PUNCTUATION & FORMATTING GLOBAL FIXES
# ============================================================

for idx, para in enumerate(doc.paragraphs):
    text = para.text
    if not text.strip():
        continue

    # Fix RSHT variants (em-dash, en-dash → standard hyphen)
    fixed = re.sub(r'RSHT\s*[–—―]\s*2', 'RSHT - 2', text)
    fixed = re.sub(r'RSHT\s+[-‐]\s+2', 'RSHT - 2', fixed)

    # Fix half-width Chinese parentheses in Chinese-dominant runs
    # Only apply to paragraphs that have Chinese content
    if any('一' <= c <= '鿿' for c in fixed):
        # Chinese: fix half-width semicolon
        fixed = re.sub(r'(?<=[一-鿿]);(?=\s*[一-鿿])', '；', fixed)
        fixed = re.sub(r'(?<=[一-鿿]);(?=$)', '；', fixed)

    if fixed != text:
        for run in para.runs:
            run.text = ""
        if para.runs:
            para.runs[0].text = fixed

# ============================================================
# SAVE
# ============================================================
doc.save(str(DST))

print("=== CORRECTIONS APPLIED ===")
for c in changes:
    print(f"  ✓ {c}")
print(f"\nSaved to: {DST}")
print("=" * 40)
print(f"Total corrections: {len(changes)}")
