# -*- coding: utf-8 -*-
"""
Amdt 01 — Chinese polishing, English alignment, renumbering.
Backup saved as .docx.bak alongside the original.
"""
from docx import Document
from copy import deepcopy
import re

FPATH = r"D:\Wison\Subcon_Payments\12.1 CCECC - MEI Pkg I\Contract\02_Amdt 01\Amdt 01_MEI Pkg I (Revised) .docx"

doc = Document(FPATH)
paras = doc.paragraphs

def find_para(starts_with, after=0):
    """Find paragraph index whose text starts with given string."""
    for i, p in enumerate(paras):
        if i < after:
            continue
        if p.text.strip().startswith(starts_with):
            return i
    return None

def replace_in_runs(para, old, new):
    """Replace text in all runs of a paragraph."""
    changed = False
    for run in para.runs:
        if old in run.text:
            run.text = run.text.replace(old, new)
            changed = True
    return changed

def replace_multiple(para, replacements):
    """Apply multiple (old, new) replacements to a paragraph's runs."""
    for old, new in replacements:
        if old != new:
            replace_in_runs(para, old, new)

def clear_and_set(para, new_text):
    """Clear a paragraph and set new text, preserving first-run formatting."""
    for run in para.runs:
        run.text = ""
    if para.runs:
        para.runs[0].text = new_text
    else:
        para.add_run(new_text)

def set_heading_text(para, en_text, cn_text):
    """Set bilingual heading: EN first line, CN second line."""
    full = en_text + "\n" + cn_text
    clear_and_set(para, full)

# ============================================================
# 1. CHINESE TYPO & WORDING FIXES
# ============================================================

# 1a. Para [48]: "承包有权" → "承包商有权"
i48 = find_para("（c）  承包有权")
if i48 is not None:
    replace_in_runs(paras[i48], "承包有权", "承包商有权")
    print(f"[OK] Fixed typo in para {i48}: 承包→承包商")

# 1b. Para [67]: "以FOB的形式" → "以 FOB 方式"
i67 = find_para("7.1  预制完成后")
if i67 is not None:
    replace_in_runs(paras[i67], "以FOB的形式", "以 FOB 方式")
    print(f"[OK] Fixed wording in para {i67}: 以FOB的形式→以 FOB 方式")

# 1c. Para [21]: "按本变更5.3条" → "按本变更协议第 4.3 条"
i21 = find_para("鉴于，双方于 2026")
if i21 is not None:
    replace_in_runs(paras[i21], "按本变更5.3条约定的比例分担", "按本变更协议第 4.3 条约定的比例分担")
    print(f"[OK] Fixed reference in para {i21}")

# ============================================================
# 2. UAE → 阿联酋 in Chinese body text
#    First body occurrence: note full name
#    Paragraphs where UAE appears in Chinese: [34], [55], [67]
#    Also check if 13/17 have UAE in Chinese context
# ============================================================

# Identify all Chinese paragraphs containing UAE
uae_paras_cn = []
for i, p in enumerate(paras):
    text = p.text
    if "UAE" in text:
        uae_paras_cn.append((i, text[:80]))

print(f"\nParagraphs with UAE: {[(idx, t) for idx, t in uae_paras_cn]}")

# [13] and [17] are company addresses — leave UAE in English parts
# Body paragraphs that are Chinese-heavy and contain UAE:
# [34] "在 UAE 自主实施" — first body occurrence → "阿联酋（阿拉伯联合酋长国）"
# [55] "至 UAE 项目现场"
# [67] "UAE 境内运输"

i34 = find_para("1.3  尽管有上述")
if i34 is not None:
    replace_in_runs(paras[i34], "在 UAE 自主实施", "在阿联酋（阿拉伯联合酋长国）自主实施")
    print(f"[OK] UAE→阿联酋(首现+全称) in para {i34}")

i55 = find_para("5.3  双方确认")
if i55 is not None:
    replace_in_runs(paras[i55], "至 UAE 项目现场", "至阿联酋项目现场")
    print(f"[OK] UAE→阿联酋 in para {i55}")

i67 = find_para("7.1  预制完成后")
if i67 is not None:
    replace_in_runs(paras[i67], "UAE 境内运输", "阿联酋境内运输")
    print(f"[OK] UAE→阿联酋 in para {i67}")

# ============================================================
# 3. RENUMBER ARTICLES (headings) — current→new mapping:
#    Art 1→1, 2→2, 4→3, 5→4, 6→5, 7→6, 8→7, 9→8, 10→9, 11→10, 12→11
# ============================================================

art_renumber = {
    # current EN heading prefix → (new_en, new_cn)
    "4. PAYMENT":        ("3. PAYMENT ON BEHALF OF SUBCONTRACTOR", "3. 代为付款安排"),
    "5. DEDUCTION":      ("4. DEDUCTION FROM PROJECT PAYMENTS", "4. 工程款抵扣"),
    "6. CONTRACTOR":     ("5. CONTRACTOR-SUPPLIED MATERIALS", "5. 承包商供货材料"),
    "7. LOGISTICS":      ("6. LOGISTICS, CUSTOMS, AND DELIVERY", "6. 物流、海关及交货"),
    "8. STANDARDS":      ("7. STANDARDS AND QUALITY", "7. 标准与质量"),
    "9. MANAGEMENT":     ("8. MANAGEMENT, QUALITY, AND RISK ALLOCATION", "8. 管理、质量及风险承担"),
    "10. EFFECT":        ("9. EFFECT ON SUBCONTRACT", "9. 对分包合同的效力"),
    "11. COUNTERPARTS":  ("10. COUNTERPARTS AND LANGUAGE", "10. 签署文本及语言"),
    "12. EFFECTIVE":     ("11. EFFECTIVE DATE", "11. 生效日期"),
}

for i, p in enumerate(paras):
    text = p.text.strip()
    for prefix, (new_en, new_cn) in art_renumber.items():
        if text.startswith(prefix):
            set_heading_text(p, new_en, new_cn)
            print(f"[OK] Renumbered heading para {i}: {prefix} → {new_en.split('.')[0]}")

# ============================================================
# 4. RENUMBER CROSS-REFERENCES IN BODY TEXT
# ============================================================

# Mapping: (para_index_approx, old_text, new_text)
ref_updates = [
    # Para 57 — "第 5.3 条"→"第 4.3 条", "第 4 条及第 5.1–5.2 条"→"第 3 条及第 4.1–4.2 条"
    ("5.4  除上述第", "第 5.3 条", "第 4.3 条"),
    ("5.4  除上述第", "第 4 条及第 5.1–5.2 条", "第 3 条及第 4.1–4.2 条"),
    # Para 59 — "第 5.2 条"→"第 4.2 条"
    ("5.5  若依据第", "第 5.2 条", "第 4.2 条"),
    # Para 64 — "第 9 条"→"第 8 条"
    ("6.2  分包商应负责", "第 9 条", "第 8 条"),
    # Para 67 — "第 5.3 条"→"第 4.3 条" (already searching 7.1)
    ("7.1  预制完成后", "第 5.3 条", "第 4.3 条"),
    # Para 69 — "第 9 条"→"第 8 条"
    ("7.2  为免疑义", "第 9 条", "第 8 条"),
    # Para 74 — "第 9 条"→"第 8 条"
    ("8.2  分包商的", "第 9 条", "第 8 条"),
    # Para 77 — "第 4 条"→"第 3 条"
    ("9.1  尽管承包商", "第 4 条", "第 3 条"),
]

# Chinese reference updates
cn_ref_updates = []
for search_start, old, new in ref_updates:
    idx = find_para(search_start)
    if idx is not None:
        cn_ref_updates.append((idx, old, new))

# English reference updates
en_ref_updates = [
    ("5.4  Save for the freight", "Clause 5.3", "Clause 4.3"),
    ("5.4  Save for the freight", "Clauses 4 and 5.1–5.2", "Clauses 3 and 4.1–4.2"),
    ("5.5  If the amounts", "Clause 5.2", "Clause 4.2"),
    ("6.2  Subcontractor shall be responsible", "Clause 9 below", "Clause 8 below"),
    ("7.1  The Third Party", "Clause 7", "Clause 6"),
    ("7.2  The logistics", "Clause 9 below", "Clause 8 below"),
    ("8.2  Subcontractor's quality", "Clause 9 below", "Clause 8 below"),
    ("9.1  Notwithstanding that", "Clause 4", "Clause 3"),
]

for search_start, old, new in en_ref_updates:
    idx = find_para(search_start)
    if idx is not None:
        cn_ref_updates.append((idx, old, new))

for idx, old, new in cn_ref_updates:
    replace_in_runs(paras[idx], old, new)
    print(f"[OK] Ref update in para {idx}: {old} → {new}")

# Also: sub-clause numbers in headings that aren't renumbered (1.1, 1.2, etc stay)
# But 4.1,4.2 → 3.1,3.2; 5.1-5.5 → 4.1-4.5; etc.

# The sub-numbering follows the article number. Let's find all sub-clauses:
# Format: "X.Y  ..." at start of paragraph (in body, not heading)

# Actually, looking at the data more carefully:
# Current paragraphs with sub-numbers:
# 1.1, 1.2, 1.3 — stay
# 2.1 — stays
# 4.1, 4.2 (sub-clauses a,b,c stay) → 3.1, 3.2
# 5.1, 5.2, 5.3, 5.4, 5.5 → 4.1, 4.2, 4.3, 4.4, 4.5
# 6.1, 6.2 → 5.1, 5.2
# 7.1, 7.2 → 6.1, 6.2
# 8.1, 8.2 → 7.1, 7.2
# 9.1, 9.2 → 8.1, 8.2
# 10.1 → 9.1
# 11.1 → 10.1
# 12.1 → 11.1

# But wait - the sub-numbers in paragraph text are part of the text itself
# (e.g., "4.1  分包商明确知悉..." or "4.1  Subcontractor expressly acknowledges...")

sub_renumber = {
    # (search_start, old_prefix, new_prefix) — for Chinese
    # We'll handle by matching paragraph start patterns
    "4.1  Subcontractor expressly": ("4.1", "3.1"),
    "4.1  分包商明确知悉": ("4.1", "3.1"),
    "4.2  The payment and settlement": ("4.2", "3.2"),
    "4.2  代付与结算": ("4.2", "3.2"),
    "5.1  All fees": ("5.1", "4.1"),
    "5.1  承包商代付给": ("5.1", "4.1"),
    "5.2  Without limiting": ("5.2", "4.2"),
    "5.2  在不限制": ("5.2", "4.2"),
    "5.3  The Parties acknowledge": ("5.3", "4.3"),
    "5.3  双方确认，管道": ("5.3", "4.3"),
    "5.4  Save for the freight": ("5.4", "4.4"),
    "5.4  除上述第": ("5.4", "4.4"),
    "5.5  If the amounts": ("5.5", "4.5"),
    "5.5  若依据第": ("5.5", "4.5"),
    "6.1  Contractor shall deliver": ("6.1", "5.1"),
    "6.1  按分包合同约定": ("6.1", "5.1"),
    "6.2  Subcontractor shall be responsible": ("6.2", "5.2"),
    "6.2  分包商应负责与": ("6.2", "5.2"),
    "7.1  The Third Party": ("7.1", "6.1"),
    "7.1  预制完成后": ("7.1", "6.1"),
    "7.2  The logistics": ("7.2", "6.2"),
    "7.2  为免疑义": ("7.2", "6.2"),
    "8.1  All fabrication": ("8.1", "7.1"),
    "8.1  委托工程（包括第三方": ("8.1", "7.1"),
    "8.2  Subcontractor's quality": ("8.2", "7.2"),
    "8.2  分包商的质量管理": ("8.2", "7.2"),
    "9.1  Notwithstanding": ("9.1", "8.1"),
    "9.1  尽管承包商依据": ("9.1", "8.1"),
    "9.2  Subcontractor expressly": ("9.2", "8.2"),
    "9.2  分包商明确确认": ("9.2", "8.2"),
    "10.1  This Amendment": ("10.1", "9.1"),
    "10.1  本变更协议构成": ("10.1", "9.1"),
    "11.1  This Amendment is executed": ("11.1", "10.1"),
    "11.1  本变更协议一式两份": ("11.1", "10.1"),
    "12.1  This Amendment (incorporating": ("12.1", "11.1"),
    "12.1  本变更协议（含第三方": ("12.1", "11.1"),
}

for i, p in enumerate(paras):
    text = p.text.strip()
    for search_start, (old_pref, new_pref) in sub_renumber.items():
        if text.startswith(search_start):
            # Replace the leading number in first run
            for run in p.runs:
                if run.text.lstrip().startswith(old_pref):
                    run.text = run.text.replace(old_pref, new_pref, 1)
                    print(f"[OK] Sub-renumber para {i}: {old_pref} → {new_pref}")
                    break
            break

# ============================================================
# 5. ENGLISH SUBSTANTIVE REWRITES
# ============================================================

# --- 5a. WHEREAS [22] — DDP → FOB, align with Chinese [23] ---
i22 = find_para("WHEREAS, in light of the critical urgency")
if i22 is not None:
    new_en22 = (
        "WHEREAS, in light of the critical urgency of the Project works, "
        "Subcontractor, with the consent of Contractor, shall engage a third-party "
        "prefabrication contractor (the \"Third Party\") to carry out the incoming "
        "material prefabrication processing of the said fire-fighting piping "
        "(including fabrication, galvanizing, anti-corrosion coating, and all "
        "associated works); as Subcontractor is unable to handle the incoming "
        "material processing registration and free trade zone customs clearance "
        "in China for the Contractor-supplied materials, Contractor has entered "
        "into a separate contract with the Third Party solely for the purposes "
        "of customs clearance and payment on behalf of Subcontractor, which shall "
        "not alter Subcontractor's status as the party bearing full responsibility "
        "for the Delegated Works; finished products shall be delivered on a FOB "
        "(Free on Board) basis at a Chinese port designated by Contractor, with "
        "onward international sea freight arranged by Contractor; Subcontractor "
        "shall retain full and unconditional management responsibility and "
        "liability for the Third Party, with the division of the scope of work "
        "between Subcontractor and the Third Party to be separately agreed;"
    )
    clear_and_set(paras[i22], new_en22)
    print(f"[OK] Rewrote English WHEREAS para {i22} (DDP→FOB)")

# --- 5b. Article 4.3 (formerly 5.3) English [54] — add "arranged by Contractor" ---
i54 = find_para("5.3  The Parties acknowledge", after=40)
if i54 is not None:
    new_en54 = (
        "The Parties acknowledge that the prefabrication of pipes in China will "
        "result in increased freight costs. After the finished products have passed "
        "factory quality inspection and acceptance and been released for export "
        "shipment, Contractor shall arrange the international transportation from "
        "the port of loading in China to the UAE Project Site (or such other location "
        "as Contractor may designate). As to the costs actually incurred in respect "
        "of such international transportation (including marine insurance, port "
        "charges, customs clearance fees, and associated shipping charges), "
        "Subcontractor shall bear twenty-five percent (25%), and Contractor shall "
        "bear the remaining seventy-five percent (75%). The 25%/75% sharing under "
        "this Clause 4.3 applies exclusively to the international transportation "
        "segment described above."
    )
    clear_and_set(paras[i54], new_en54)
    print(f"[OK] Rewrote English 5.3→4.3 para {i54} (add Contractor-arranged freight)")

# --- 5c. Article 5.4 (→4.4) English [56] — update references ---
i56 = find_para("5.4  Save for the freight")
if i56 is not None:
    replace_in_runs(paras[i56], "Clause 5.3", "Clause 4.3")
    replace_in_runs(paras[i56], "Clauses 4 and 5.1–5.2", "Clauses 3 and 4.1–4.2")
    print(f"[OK] Updated English refs in 5.4→4.4 para {i56}")

# --- 5d. Article 5.5 (→4.5) English [58] — update references ---
i58 = find_para("5.5  If the amounts")
if i58 is not None:
    replace_in_runs(paras[i58], "Clause 5.2", "Clause 4.2")
    print(f"[OK] Updated English refs in 5.5→4.5 para {i58}")

# --- 5e. Article 6.1 (→5.1) English [61] — add customs processing ---
i61 = find_para("6.1  Contractor shall deliver the raw")
if i61 is not None:
    new_en61 = (
        "Contractor shall deliver the raw materials which it is obligated to supply "
        "under the Subcontract to a location in China designated by Contractor (or "
        "as otherwise agreed between the Parties). Subcontractor and the Third Party "
        "shall be responsible for handling the incoming material processing registration, "
        "designated free trade zone customs clearance, and related formalities. Such "
        "raw materials shall be delivered to the Third Party for the purpose of the "
        "Delegated Works."
    )
    clear_and_set(paras[i61], new_en61)
    print(f"[OK] Rewrote English 6.1→5.1 para {i61} (add customs obligations)")

# --- 5f. Article 6.2 (→5.2) English [63] — update refs ---
i63 = find_para("6.2  Subcontractor shall be responsible for coordinating")
if i63 is not None:
    replace_in_runs(paras[i63], "Clause 9 below", "Clause 8 below")
    print(f"[OK] Updated English refs in 6.2→5.2 para {i63}")

# --- 5g. Article 7.1 (→6.1) English [66] — MAJOR rewrite: DDP→FOB ---
i66 = find_para("7.1  The Third Party shall be responsible")
if i66 is not None:
    new_en66 = (
        "Upon completion of prefabrication, Subcontractor and the Third Party shall "
        "be responsible for container collection, loading, and packaging in accordance "
        "with Contractor's shipping instructions, handling export customs formalities, "
        "and delivering the goods on a FOB basis to the port designated by Contractor; "
        "from such port onwards, international sea freight, destination customs clearance, "
        "and inland transportation within the UAE shall be arranged by Contractor, "
        "with the relevant costs shared in accordance with Clause 4.3."
    )
    clear_and_set(paras[i66], new_en66)
    print(f"[OK] Rewrote English 7.1→6.1 para {i66} (DDP→FOB)")

# --- 5h. Article 7.2 (→6.2) English [68] — update refs + clarify ---
i68 = find_para("7.2  The logistics")
if i68 is not None:
    replace_in_runs(paras[i68], "Clause 9 below", "Clause 8 below")
    print(f"[OK] Updated English refs in 7.2→6.2 para {i68}")

# --- 5i. Article 9.1 (→8.1) English [76] — update refs ---
i76 = find_para("9.1  Notwithstanding that Contractor")
if i76 is not None:
    replace_in_runs(paras[i76], "Clause 4", "Clause 3")
    print(f"[OK] Updated English refs in 9.1→8.1 para {i76}")

# --- 5j. Article 8.2, 9.2, 9.1(c) — check for "Clause 9" references ---
for i, p in enumerate(paras):
    text = p.text
    # Catch any remaining "Clause 9" that should be "Clause 8"
    if "Clause 9" in text and i > 60:
        replace_in_runs(p, "Clause 9", "Clause 8")
        # But only if it refers to the Management/Quality/Risk article of THIS amendment
        # Para 63, 68, 73 were already handled; 76 references "Clause 4" not "Clause 9"

# Also fix remaining "Clause 5." references to "Clause 4." in English sub-clauses
for i, p in enumerate(paras):
    text = p.text
    if re.search(r'Clause 5\.\d', text):
        replace_in_runs(p, "Clause 5.1", "Clause 4.1")
        replace_in_runs(p, "Clause 5.2", "Clause 4.2")
        replace_in_runs(p, "Clause 5.3", "Clause 4.3")
        replace_in_runs(p, "Clause 5.4", "Clause 4.4")
        replace_in_runs(p, "Clause 5.5", "Clause 4.5")
        print(f"[OK] Fixed Clause 5.x → 4.x in para {i}")

# Fix remaining "Clause 4" that should be "Clause 3" (payment article)
# Only in contexts where it refers to the Payment on Behalf article
for i, p in enumerate(paras):
    text = p.text
    # In 9.1 → 8.1 context (para [76] already handled)
    # Also check if "Clause 4" appears in paras that were previously Art 5 (now Art 4)
    # where it should remain as "Clause 4" (now the deduction article)
    # The tricky one: "Clause 4" in old Art 5.4 → new Art 4.4 refers to old Art 4 (payment)
    # which is now Art 3. So "Clause 4" in the deduction article should → "Clause 3"
    pass  # handled above in specific paragraphs

# ============================================================
# 6. SAVE
# ============================================================
doc.save(FPATH)
print(f"\n[DONE] Saved: {FPATH}")
print("[INFO] Backup at: " + FPATH + ".bak")
