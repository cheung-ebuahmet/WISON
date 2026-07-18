#!/usr/bin/env python3
"""Align English to Chinese in Amdt 01. Reads Chinese/English text from align-data.json."""
import json, re
from docx import Document
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
SRC = Path(r"D:\Wison\Subcon_Payments\12.1 CCECC - MEI Pkg I\Contract\02_Amdt 01\Amdt 01_MEI Pkg I (Revised) V2 _CORRECTED_v2.docx")
DST = SRC.parent / "Amdt 01_MEI Pkg I (Revised) V2 _ALIGNED.docx"

with open(SCRIPT_DIR / "align-data.json", "r", encoding="utf-8") as f:
    D = json.load(f)

doc = Document(str(SRC))


def write_para(para, text):
    for run in para.runs:
        run.text = ""
    if para.runs:
        para.runs[0].text = text
    else:
        r = para.add_run(text)


def align(para, cn, en):
    write_para(para, en + "\n" + cn)


# ── P13: Recitals 1 ──
align(doc.paragraphs[13], D["p13_cn"], D["p13_en"])
print("P13: English expanded to match Chinese")

# ── P19: 1.3 — add English ──
cn19 = doc.paragraphs[19].text.strip()
align(doc.paragraphs[19], cn19, D["p19_en"])
print("P19: English added")

# ── P21: 2.1 ──
cn21 = doc.paragraphs[21].text.split('\n')[-1].strip()
align(doc.paragraphs[21], cn21, D["p21_en"])
print("P21: English rewritten to match Chinese")

# ── P23: 3.1 — fix duplicate Chinese, align English ──
cn23 = doc.paragraphs[23].text.split('\n')[-1].strip()
# Remove duplicate: "...第 6 条执行。分包商确认...不负...责任，分包商对加工商的管理责任按照本协议第 6 条执行。"
# → "...第 6 条执行。分包商确认...不负...责任。"
cn23 = re.sub(
    r'。分包商对加工商的管理责任按照本协议第 6 条执行。$',
    '。',
    cn23
)
align(doc.paragraphs[23], cn23, D["p23_en"])
print("P23: Duplicate Chinese removed; English aligned")

# ── P24: 3.2 intro ──
cn24 = doc.paragraphs[24].text.split('\n')[-1].strip()
align(doc.paragraphs[24], cn24, D["p24_en"])
print("P24: English simplified")

# ── P25: 3.2(a) ──
cn25 = doc.paragraphs[25].text.split('\n')[-1].strip()
align(doc.paragraphs[25], cn25, D["p25_en"])
print("P25: English aligned with 7-day review clause")

# ── P28: 4.1 — Chinese was missing ──
align(doc.paragraphs[28], D["p28_cn"], D["p28_en"])
print("P28: Chinese added")

# ── P29: 4.2 — fix capitalization ──
cn29 = doc.paragraphs[29].text.split('\n')[-1].strip()
align(doc.paragraphs[29], cn29, D["p29_en"])
print("P29: English cleaned up")

# ── P36: 6.1 — trim English ──
cn36 = doc.paragraphs[36].text.split('\n')[-1].strip()
align(doc.paragraphs[36], cn36, D["p36_en"])
print("P36: English trimmed")

# ── P38: 6.1(b) — fix Chinese punctuation, clean English ──
cn38 = doc.paragraphs[38].text.split('\n')[-1].strip()
# Fix: （IRN/QRC). with half-width period → （IRN/QRC）。
cn38 = re.sub(r'（IRN/QRC\)\.$', '（IRN/QRC）。', cn38)
cn38 = re.sub(r'\(IRN/QRC\)\.$', '（IRN/QRC）。', cn38)
align(doc.paragraphs[38], cn38, D["p38_en"])
print("P38: Punctuation fixed")

# ── Global: RSHT dash ──
for para in doc.paragraphs:
    t = para.text
    f = re.sub(r'RSHT\s*[–—―−]\s*2', 'RSHT - 2', t)
    f = re.sub(r'RSHT\s+-\s+2', 'RSHT - 2', f)
    if f != t:
        for run in para.runs:
            run.text = ""
        if para.runs:
            para.runs[0].text = f
print("Global: RSHT dash standardized")

doc.save(str(DST))
print(f"\nSaved: {DST}")
