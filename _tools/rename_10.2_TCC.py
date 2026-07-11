"""
Rename/cleanup Part I + Part II Atchments for 10.2 TCC - Civil I_III.
Does NOT rename the 7 top-level Attachment folders.
Adapted from 10.1 logic; handles TCC-specific: two packages (I+III).
"""
import os, shutil, hashlib

ROOT = r"D:\Wison\Subcon_Payments\10.2 TCC - Civil I_III\Contract"

def md5(p):
    with open(p, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

def mv(old, new):
    src = os.path.join(ROOT, old)
    dst = os.path.join(ROOT, new)
    if os.path.exists(src):
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        if os.path.exists(dst):
            print(f"  COLLISION: {new} (already exists — skipping)")
        else:
            os.rename(src, dst)
            print(f"  RENAME: {old}\n       -> {new}")
    else:
        print(f"  NOT FOUND: {old}")

def rm(path):
    full = os.path.join(ROOT, path)
    if os.path.isfile(full):
        os.remove(full); print(f"  DEL FILE: {path}")
    elif os.path.isdir(full):
        shutil.rmtree(full); print(f"  DEL DIR:  {path}")

def verify_same(p1, p2):
    f1 = os.path.join(ROOT, p1); f2 = os.path.join(ROOT, p2)
    if os.path.isfile(f1) and os.path.isfile(f2):
        return md5(f1) == md5(f2)
    return None

print("=" * 70)
print("PHASE 0: Part I — FOA_LOA_CF_COC")
print("=" * 70)

P1 = "Part I FOA_LOA_CF_COC"
mv(f"{P1}/FOA - COC_Draft.docx",
   f"{P1}/WISON24108C25007_Agrmt - FOA - COC_Draft.docx")
mv(f"{P1}/LOA_Signed.pdf",
   f"{P1}/LOA_Civil Pkg I - III_Signed.pdf")

# =====================================================================
# PART II
# =====================================================================
BASE = "Part II Atchments"

print()
print("=" * 70)
print("PHASE 1: Delete temp files (~$*)")
print("=" * 70)
for root_dir, dirs, files in os.walk(os.path.join(ROOT, BASE)):
    for f in files:
        if f.startswith('~$'):
            rel = os.path.relpath(os.path.join(root_dir, f), ROOT)
            rm(rel)

print()
print("=" * 70)
print("PHASE 2: Attachment 1 — Communication Procedures")
print("=" * 70)
A1 = f"{BASE}/Attachment 1 - Communication Procedures"
A1D = f"{A1}/DCC requirements"

# 2a. Create DC Procedure at Att 1 root, move root-level PR-5312 PDFs there
mv(f"{A1}/PR-5312-1000-PM-0009_0 Project Document Control Procedure.pdf",
   f"{A1}/DC Procedure/PR-5312-1000-PM-0009_0 Project Document Control Procedure.pdf")
mv(f"{A1}/PR-5312-1000-PM-0010_0 DOCUMENT NUMBERING PROCEDURE.pdf",
   f"{A1}/DC Procedure/PR-5312-1000-PM-0010_0 DOCUMENT NUMBERING PROCEDURE.pdf")
mv(f"{A1}/PR-5312-1000-PM-0012_0 Vendor Documentation Control Procedure.pdf",
   f"{A1}/DC Procedure/PR-5312-1000-PM-0012_0 Vendor Documentation Control Procedure.pdf")

# 2b. Move WISON DC Portal manual + docweb files to DC Procedure
mv(f"{A1}/WISON DC Portal Operation manual.pdf",
   f"{A1}/DC Procedure/WISON DC Portal Operation manual.pdf")

# Move docweb files from nested DCC up
docweb_src = f"{A1D}/DC Procedure/WISON DC Portal Operation manual"
for f in ["docweb_help.pdf", "docweb_help_en.pdf"]:
    mv(f"{docweb_src}/{f}", f"{A1}/DC Procedure/{f}")
rm(docweb_src)

# 2c. Delete nested DCC/DC Procedure duplicates (PR-5312 subdirs)
for sub in ["PR-5312-1000-PM-0009 Project Document Control Procedure",
            "PR-5312-1000-PM-0010 Document Numbering Procedure",
            "PR-5312-1000-PM-0012 Vendor Documentation Control Procedure"]:
    rm(f"{A1D}/DC Procedure/{sub}")

# 2d. Delete empty DCC/DC Procedure
rm(f"{A1D}/DC Procedure")

# 2e. Delete top-level duplicates (keep DCC copies)
for top_file in [
    f"{A1}/Guideline for Subcontractor's Document Management_20250618.docx",
    f"{A1}/SUBCON Project Management Doc Template-General.docx",
    f"{A1}/SUBCON Project Management Doc Template-ITP.docx",
]:
    # Build matching DCC path
    fname = os.path.basename(top_file.split('/')[-1])
    dcc_f = os.path.join(ROOT, A1D, fname)
    top_f = os.path.join(ROOT, top_file)
    if os.path.exists(top_f) and os.path.exists(dcc_f):
        if md5(top_f) == md5(dcc_f):
            rm(top_file)
            print(f"    (duplicate of DCC copy)")

# 2f. Rename files in DCC requirements
mv(f"{A1D}/CRS Template - PR-5312-1000-PM-0001 Rev.A_CRS.xlsx",
   f"{A1D}/CRS Template_PR-5312-1000-PM-0001 Rev.A.xlsx")
mv(f"{A1D}/Guideline for Subcontractor's Document Management_20250618.docx",
   f"{A1D}/Guideline - Subcontractors Document Management.docx")
mv(f"{A1D}/PR-5312-1000-PM-0010_0 Document Numbering Procedure_20250618.pdf",
   f"{A1D}/PR-5312-1000-PM-0010_Document Numbering Procedure_2025-06-18.pdf")
mv(f"{A1D}/SUBCON Project Management Doc Template-General.docx",
   f"{A1D}/Subcon PM Doc Template - General.docx")
mv(f"{A1D}/SUBCON Project Management Doc Template-ITP.docx",
   f"{A1D}/Subcon PM Doc Template - ITP.docx")

# Delete orphaned PM-0010 dated at root (already in DCC)
for f in os.listdir(os.path.join(ROOT, A1)):
    if "PM-0010" in f and "20250618" in f:
        rm(f"{A1}/{f}")

# 2g. Rename Subcontract Template files
ST = f"{A1D}/Subcontract Template"
mv(f"{ST}/Appendix -1 Subcontractor Template for ITP Doc.docx",
   f"{ST}/App 01_Subcontractor Template - ITP.docx")
mv(f"{ST}/Appendix -2 Subcontractor Template for General Doc.docx",
   f"{ST}/App 02_Subcontractor Template - General.docx")
mv(f"{ST}/Appendix -3 SDDR Template (SUBCONTRACTOR DELIVERABLE DOCUMENT REGISTER).xlsx",
   f"{ST}/App 03_SDDR Template.xlsx")
mv(f"{ST}/Appendix -4 MOM Template.DOCX",
   f"{ST}/App 04_MOM Template.docx")
mv(f"{ST}/Appendix -5 Transmittal Template.xlsx",
   f"{ST}/App 05_Transmittal Template.xlsx")
mv(f"{ST}/Appendix -6 CRS Teamplate (Comments resolution sheet).xlsx",
   f"{ST}/App 06_CRS Template.xlsx")
mv(f"{ST}/Appendix -7 Template of title block_A0-A4 for drawing.zip",
   f"{ST}/App 07_Title Block Template - A0-A4.zip")

print()
print("=" * 70)
print("PHASE 3: Attachment 2 — Change Management")
print("=" * 70)
A2 = f"{BASE}/Attachment 2 - Change Management"
mv(f"{A2}/CHANGE management.docx", f"{A2}/Change Management Procedure.docx")
mv(f"{A2}/CHANGE management.pdf", f"{A2}/Change Management Procedure_Signed.pdf")

print()
print("=" * 70)
print("PHASE 4: Attachment 3 — HSE Requirements")
print("=" * 70)
A3 = f"{BASE}/Attachment 3 - HSE requirements"
HRA = f"{A3}/HSE Requirements Attachments"

# 4a. Top-level HSE docs
mv(f"{A3}/HSE Requirements.docx", f"{A3}/HSE Requirements.docx")  # clean unicode
mv(f"{A3}/HSE Requirements.pdf", f"{A3}/HSE Requirements_Signed.pdf")  # clean unicode

# 4b. Rename "1 HSE Requirements.pdf"
mv(f"{HRA}/1  HSE Requirements.pdf", f"{HRA}/Att 00_HSE Requirements - Main Body.pdf")

# 4c. Rename numbered files (remove prefix)
mv(f"{HRA}/3 ADR002 - Updated HSE Requirements.pdf",
   f"{HRA}/ADR-002_Updated HSE Requirements.pdf")
mv(f"{HRA}/4 ADR003 - Asset Integrity.pdf",
   f"{HRA}/ADR-003_Asset Integrity.pdf")
mv(f"{HRA}/5 ADNOC Group Medical Fitness Guidelines for Contractors-1 APR 2023.pdf",
   f"{HRA}/ADNOC Group Medical Fitness Guidelines for Contractors_2023-04-01.pdf")

# 4d. Move Camp Welfare to App 04
mv(f"{HRA}/2025 Camp  Welfare Audit Register 1.pdf",
   f"{HRA}/APPENDIX 4-Pre Mobilization Audit and Pre-Execution Audit Checklist/Camp Welfare Audit Register_2025.pdf")

# 4e. Rename APPENDIX folders
mv(f"{HRA}/APPENDIX 1-Contractor Management Procedure",
   f"{HRA}/App 01_Contractor Management Procedures")
mv(f"{HRA}/APPENDIX 2-ADNOC HSEWM Min Reqts in Contracts",
   f"{HRA}/App 02_ADNOC HSEWM Min Requirements in Contracts")
mv(f"{HRA}/APPENDIX 3-HSE ASSURANCE PROGRAM",
   f"{HRA}/App 03_HSE Assurance Program")
mv(f"{HRA}/APPENDIX 4-Pre Mobilization Audit and Pre-Execution Audit Checklist",
   f"{HRA}/App 04_Pre-Mob - Pre-Execution Audit Checklists")
mv(f"{HRA}/APPENDIX 5-ADNOC Approved Training Providers",
   f"{HRA}/App 05_ADNOC Approved Training Providers")

# 4f. Rename "2 HSE requirements Attachments"
mv(f"{HRA}/2 HSE requirements Attachments",
   f"{HRA}/Att A-D_HSE Standards")

# 4g. Rename App 01 internal files (clean unicode spaces)
AP1 = f"{HRA}/App 01_Contractor Management Procedures"
for f in os.listdir(os.path.join(ROOT, AP1)):
    if '\xa0' in f:
        mv(f"{AP1}/{f}", f"{AP1}/{f.replace(chr(0xa0), ' ')}")

# 4h. Rename App 02 file
mv(f"{HRA}/App 02_ADNOC HSEWM Min Requirements in Contracts/ADNOC HSEWM Min Reqts in Contracts.pdf",
   f"{HRA}/App 02_ADNOC HSEWM Min Requirements in Contracts/ADNOC HSEWM Min Requirements in Contracts.pdf")

# 4i. Rename App 03 files
AP3 = f"{HRA}/App 03_HSE Assurance Program"
mv(f"{AP3}/CONTRACTOR HSE ASSURANCE PROGRAM.pdf",
   f"{AP3}/Contractor HSE Assurance Program.pdf")
mv(f"{AP3}/HSE PERFORMANCE CONTRACT.pdf",
   f"{AP3}/HSE Performance Contract.pdf")

# 4j. Rename App 04 files + duplicate check
AP4 = f"{HRA}/App 04_Pre-Mob - Pre-Execution Audit Checklists"
mv(f"{AP4}/Mobilization (Pre-Execution) Audit Checklist.xlsx",
   f"{AP4}/Mobilization Pre-Execution Audit Checklist.xlsx")
mv(f"{AP4}/Pre Mobilization Audit Checklist.xlsx",
   f"{AP4}/Pre-Mobilization Audit Checklist.xlsx")

# HSE-GA-ST05 in App 04 — if same as ATTACH-A copy, delete
ap4_ga = f"{AP4}/HSE-GA-ST05_V1 Contractor HSE Mgmt.pdf"
att_a_ga = f"{HRA}/Att A-D_HSE Standards/ATTACH-A/HSE-GA-ST05_V1 Contractor HSE Mgmt.pdf"
if verify_same(ap4_ga, att_a_ga):
    rm(ap4_ga)  # duplicate

# 4k. Rename App 05 file
mv(f"{HRA}/App 05_ADNOC Approved Training Providers/ADNOC Approved Training Providers October 2025 V3.pdf",
   f"{HRA}/App 05_ADNOC Approved Training Providers/ADNOC Approved Training Providers_2025-10_V3.pdf")

print()
print("=" * 70)
print("PHASE 5: Attachment 4 — Quality Management")
print("=" * 70)
A4 = f"{BASE}/Attachment 4 - Quality Management"
QM = f"{A4}/Quality Management Requirements"

mv(f"{QM}/Contractors QAQC Requirement.pdf",
   f"{QM}/WISON_Contractors QAQC Requirement.pdf")
mv(f"{QM}/EXHIBIT-B.10 Quality Requirement.pdf",
   f"{QM}/Exh B.10_Quality Requirement.pdf")
mv(f"{QM}/AGES-GL-13-001 Contractors QAQC Requirement.pdf",
   f"{QM}/AGES-GL-13-001_Contractors QAQC Requirement.pdf")
mv(f"{QM}/AGES-SP-07-007 Welding and Non Destructive Examination (NDE).pdf",
   f"{QM}/AGES-SP-07-007_Welding - NDE.pdf")
mv(f"{QM}/AGES-SP-13-002 Procurement Inspection and Certification Requirement in Projects.pdf",
   f"{QM}/AGES-SP-13-002_Procurement Inspection - Certification.pdf")
mv(f"{A4}/QUALITY REQUIREMENTS FOR SUBCONTRACTORS.docx",
   f"{A4}/Quality Requirements for Subcontractors.docx")
mv(f"{A4}/QUALITY REQUIREMENTS FOR SUBCONTRACTORS.pdf",
   f"{A4}/Quality Requirements for Subcontractors_Signed.pdf")

print()
print("=" * 70)
print("PHASE 6: Attachment 5 — Scope of Work")
print("=" * 70)
A5 = f"{BASE}/Attachment 5 - Scope of Work"

# 6a. Two SOW files (Pkg I + Pkg III)
mv(f"{A5}/1.1 Scope of Work for Package 1.docx",
   f"{A5}/Att 01_Scope of Work - Civil Pkg I.docx")
mv(f"{A5}/1.1 Scope of Work for Package 1.pdf",
   f"{A5}/Att 01_Scope of Work - Civil Pkg I_Signed.pdf")
mv(f"{A5}/1.2 Scope of Work for Package 3.docx",
   f"{A5}/Att 02_Scope of Work - Civil Pkg III.docx")
mv(f"{A5}/1.2 Scope of Work for Package 3.pdf",
   f"{A5}/Att 02_Scope of Work - Civil Pkg III_Signed.pdf")

# 6b. Responsibility Matrix
mv(f"{A5}/2. Responsibility Matrix.docx",
   f"{A5}/Att 03_Responsibility Matrix.docx")
mv(f"{A5}/2. Responsibility Matrix.pdf",
   f"{A5}/Att 03_Responsibility Matrix_Signed.pdf")

# 6c. Schedule — move main doc out, rename annexes
SR = f"{A5}/3. Schedule Requirements"
mv(f"{SR}/SCHEDULE AND REPORTING REQUIREMENT.docx",
   f"{A5}/Att 04_Schedule - Reporting Requirement.docx")
mv(f"{SR}/SCHEDULE AND REPORTING REQUIREMENT.pdf",
   f"{A5}/Att 04_Schedule - Reporting Requirement_Signed.pdf")

# 6d. Delay LD (two packages)
mv(f"{SR}/DELAY LIQUIDATED DAMAGES - PACKAGE 1.docx",
   f"{A5}/Att 05_Delay LD - Civil Pkg I.docx")
mv(f"{SR}/DELAY LIQUIDATED DAMAGES - PACKAGE 1.pdf",
   f"{A5}/Att 05_Delay LD - Civil Pkg I_Signed.pdf")
mv(f"{SR}/DELAY LIQUIDATED DAMAGES - PACKAGE 3.docx",
   f"{A5}/Att 06_Delay LD - Civil Pkg III.docx")
mv(f"{SR}/DELAY LIQUIDATED DAMAGES - PACKAGE 3.pdf",
   f"{A5}/Att 06_Delay LD - Civil Pkg III_Signed.pdf")

# 6e. Rename Annexes folder + files
mv(f"{SR}/Annexes to SCHEDULE AND REPORTING REQUIREMENT",
   f"{SR}/Annexes_Schedule - Reporting")
ANN = f"{SR}/Annexes_Schedule - Reporting"
for old, new in [
    ("ATT1-Planning and Scheduling Procedure.pdf", "ATT 01_Planning - Scheduling Procedure.pdf"),
    ("ATT2-Work Breakdown Structure (WBS).pdf", "ATT 02_Work Breakdown Structure.pdf"),
    ("ATT3-Work Schedule - SCHEDULE REQUIREMENT - Package 2.pdf", "ATT 03_Work Schedule - Civil Pkg II.pdf"),
    ("ATT4-Basis of Construction & Pre-Commissioning Progress Measurement.pdf", "ATT 04_Basis of Construction - Pre-Commissioning Progress Measurement.pdf"),
    ("ATT5-Project Calendar.pdf", "ATT 05_Project Calendar.pdf"),
    ("ATT6-Project Reporting Procedure.pdf", "ATT 06_Project Reporting Procedure.pdf"),
    ("ATT7-Progress Measurement Procedure.pdf", "ATT 07_Progress Measurement Procedure.pdf"),
]:
    old_full = os.path.join(ROOT, ANN, old)
    new_full = os.path.join(ROOT, ANN, new)
    if os.path.exists(old_full):
        mv(f"{ANN}/{old}", f"{ANN}/{new}")
    # Try with unicode space
    old_unicode = old.replace(' ', '\xa0')
    old_full_u = os.path.join(ROOT, ANN, old_unicode)
    if os.path.exists(old_full_u):
        mv(f"{ANN}/{old_unicode}", f"{ANN}/{new}")

# 6f. Key Personnel
KP = f"{A5}/4. Key Personnel"
mv(f"{KP}/Appendix - Key Personnel & Liquidated Damages.docx",
   f"{A5}/Att 07_Key Personnel - LD.docx")
mv(f"{KP}/Appendix - Key Personnel & Liquidated Damages.pdf",
   f"{A5}/Att 07_Key Personnel - LD_Signed.pdf")

# 6g. Approved Vendor & Contractor List
AV = f"{A5}/5. Approved Vendor & Contractor List"
mv(f"{AV}/ACL updated   07 2025.xlsx",
   f"{AV}/Approved Contractor List_2025-07.xlsx")
mv(f"{AV}/AVL_26022025.xlsx",
   f"{AV}/Approved Vendor List_2025-02-26.xlsx")

# 6h. Rename subfolders (after files moved out)
mv(f"{A5}/3. Schedule Requirements", f"{A5}/03_Schedule - Reporting")
mv(f"{A5}/4. Key Personnel", f"{A5}/04_Key Personnel")
mv(f"{A5}/5. Approved Vendor & Contractor List", f"{A5}/05_Approved Vendor - Contractor List")

# Clean empty Key Personnel folder if still exists
kp_path = os.path.join(ROOT, A5, "04_Key Personnel")
if os.path.isdir(kp_path) and not os.listdir(kp_path):
    rm(f"{A5}/04_Key Personnel")

print()
print("=" * 70)
print("PHASE 7: Attachment 6 — Commercials")
print("=" * 70)
A6 = f"{BASE}/Attachment 6 - Commercials"

mv(f"{A6}/Exhibit A.1 BOQ For CIVIL AND BLDG_Rev.A-PACKAGE I.pdf",
   f"{A6}/Att 01_BOQ - Civil - BLDG Pkg I_Rev.A_Signed.pdf")
mv(f"{A6}/Exhibit A.1.1 Addendum01-1.Exhibit A BOQ For CIVIL AND BLDG-PACKAGE I.pdf",
   f"{A6}/Att 01.1_BOQ Addendum - Civil - BLDG Pkg I_Signed.pdf")
mv(f"{A6}/Exhibit A.2 BOQ For CIVIL AND BLDG_Rev.A-PACKAGE III.pdf",
   f"{A6}/Att 02_BOQ - Civil - BLDG Pkg III_Rev.A_Signed.pdf")

# Exhibit B Measurement Method
EB = f"{A6}/Exhibit B Measurement Method"
mv(f"{EB}/01. General-Subcontractor Pricing Instructions_Rev.A.docx",
   f"{EB}/01_General - Subcontractor Pricing Instructions_Rev.A.docx")
mv(f"{EB}/01. General-Subcontractor Pricing Instructions_Rev.A.pdf",
   f"{EB}/01_General - Subcontractor Pricing Instructions_Rev.A_Signed.pdf")

# Rename numbered files (& → -)
for old_name in os.listdir(os.path.join(ROOT, EB)):
    if old_name.startswith(('02.', '03.', '10.')):
        new_name = old_name.replace('&', '-').replace('\xa0', ' ')
        if new_name != old_name:
            mv(f"{EB}/{old_name}", f"{EB}/{new_name}")

# Exhibit C Bank Bond Template
mv(f"{A6}/Exhibit C Bank Bond Template/Bank Bond Format with Schedules.docx",
   f"{A6}/Att 03_Bank Bond Format - ADNOC.docx")
bank_dir = os.path.join(ROOT, A6, "Exhibit C Bank Bond Template")
if os.path.isdir(bank_dir) and not os.listdir(bank_dir):
    rm(f"{A6}/Exhibit C Bank Bond Template")

print()
print("=" * 70)
print("PHASE 8: Attachment 7 — Owner's Special Requirements")
print("=" * 70)
A7 = f"{BASE}/Attachment 7 - Owner's Special Requirements &Reference"

# 8a. Rename B.16 (same content as 10.1, use our naming)
mv(f"{A7}/5. Subcontracting/EXHIBIT-B.16.pdf",
   f"{A7}/5. Subcontracting/Exh B.16_Selection of Subcontractors and Vendors.pdf")

# 8b. Rename folder
mv(f"{A7}/1. COMPANY's code and standard Draw",
   f"{A7}/01_Company Codes - Standard Drawings")

# 8c. Rename AGES-Reference files
AGES = f"{A7}/01_Company Codes - Standard Drawings/AGES-Reference"
for old_name in os.listdir(os.path.join(ROOT, AGES)):
    if old_name.startswith('AGES-SP-') and old_name.endswith('.pdf'):
        if ' ' in old_name and '_' not in old_name.split(' ', 1)[1][:3]:
            parts = old_name.split(' ', 1)
            if len(parts) == 2:
                new_name = f"{parts[0]}_{parts[1]}"
                mv(f"{AGES}/{old_name}", f"{AGES}/{new_name}")

# Fix leading space in 01-012 and trailing space in 01-015
for f in os.listdir(os.path.join(ROOT, AGES)):
    if '01-012' in f and '  ' in f:
        mv(f"{AGES}/{f}", f"{AGES}/{f.replace('_  ', '_').replace('  ', ' ')}")
    if '01-015' in f and ' .pdf' in f:
        new = f.replace('Specialities, Metal, Wood and Plastics .pdf',
                        'Architectural Specialities - Metal, Wood and Plastics.pdf')
        mv(f"{AGES}/{f}", f"{AGES}/{new}")

# 8d. Rename AGES-ST Draw file
STD = f"{A7}/01_Company Codes - Standard Drawings/AGES-ST Draw"
mv(f"{STD}/AGES STD dwgs - Consolidated-CV AR.pdf",
   f"{STD}/AGES STD Drawings - Consolidated - Civil_AR.pdf")

# 8e. Rename compliance files
CMP = f"{A7}/2. Compliance and ethics code"
mv(f"{CMP}/2022 ADNOC Group Code of Conduct Employee- En.pdf",
   f"{CMP}/ADNOC Group Code of Conduct - Employee_2022_EN.pdf")
mv(f"{CMP}/Supplier Code of Ethics En.pdf",
   f"{CMP}/ADNOC Group Supplier Code of Business Ethics_EN.pdf")

# 8f. Rename ICV files (two packages with - separator)
ICV = f"{A7}/3. ICV requirements"
mv(f"{ICV}/ADNOC ICV  Implementation Guideline - Rev.3.1.pdf",
   f"{ICV}/ADNOC ICV Implementation Guideline_Rev.3.1.pdf")
mv(f"{ICV}/ICV Improvement Plan - Agreement Specfic PKG 1.pdf",
   f"{ICV}/ICV Improvement Plan - Civil Pkg I_Signed.pdf")
mv(f"{ICV}/ICV Improvement Plan - Agreement Specfic PKG 3.pdf",
   f"{ICV}/ICV Improvement Plan - Civil Pkg III_Signed.pdf")

# 8g. Rename numbered subfolders
mv(f"{A7}/2. Compliance and ethics code", f"{A7}/02_Compliance - Ethics Code")
mv(f"{A7}/3. ICV requirements", f"{A7}/03_ICV Requirements")
mv(f"{A7}/4. Insurance Requirements", f"{A7}/04_Insurance Requirements")
mv(f"{A7}/5. Subcontracting", f"{A7}/05_Subcontracting")

print()
print("=" * 70)
print("PHASE 9: Final Unicode cleanup")
print("=" * 70)
for root_dir, dirs, files in os.walk(os.path.join(ROOT, BASE)):
    for f in files + dirs:
        if '\xa0' in f:
            old = os.path.join(root_dir, f)
            new = os.path.join(root_dir, f.replace('\xa0', ' '))
            if old != new and not os.path.exists(new):
                os.rename(old, new)
                rel = os.path.relpath(old, ROOT)
                print(f"  UNICODE FIX: {rel}")

print()
print("=" * 70)
print("DONE")
print("=" * 70)

# Quick stats
fc = sum(1 for r,d,fs in os.walk(ROOT) for f in fs)
dc = sum(1 for r,d,fs in os.walk(ROOT) for d in fs)
print(f"Total: {fc} files, {dc} dirs under 10.2 TCC")
