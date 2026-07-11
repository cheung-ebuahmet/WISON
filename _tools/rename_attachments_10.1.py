"""
Rename/cleanup Part II Attachments for 10.1 CCECC - Civil II.
Does NOT rename the 7 top-level Attachment folders.
Operations: delete temp files, delete exact duplicates, rename for clarity.
"""
import os, shutil, hashlib

ROOT = r"D:\Wison\Subcon_Payments\10.1 CCECC - Civil II\Contract\Part II Attachments"

def md5(p):
    with open(p, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

def mv(old, new):
    """Rename file. old/new relative to ROOT."""
    src = os.path.join(ROOT, old)
    dst = os.path.join(ROOT, new)
    if os.path.exists(src):
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        os.rename(src, dst)
        print(f"  RENAME: {old}\n       -> {new}")
    else:
        print(f"  SKIP (not found): {old}")

def rm(path):
    """Delete file or directory."""
    full = os.path.join(ROOT, path)
    if os.path.isfile(full):
        os.remove(full)
        print(f"  DEL FILE: {path}")
    elif os.path.isdir(full):
        shutil.rmtree(full)
        print(f"  DEL DIR:  {path}")
    else:
        print(f"  SKIP (not found): {path}")

def verify_same(p1, p2):
    """Verify two files are identical before deleting one."""
    f1 = os.path.join(ROOT, p1)
    f2 = os.path.join(ROOT, p2)
    if os.path.isfile(f1) and os.path.isfile(f2):
        if md5(f1) == md5(f2):
            return True
        else:
            print(f"  ⚠ NOT SAME (skipping): {p1} vs {p2}")
            return False
    return None  # one doesn't exist

print("=" * 70)
print("PHASE 1: Delete temp files (~$*)")
print("=" * 70)

# Word temp lock files
for root_dir, dirs, files in os.walk(ROOT):
    for f in files:
        if f.startswith('~$'):
            full = os.path.join(root_dir, f)
            rel = os.path.relpath(full, ROOT)
            rm(rel)

print()
print("=" * 70)
print("PHASE 2: Attachment 1 — Communication Procedures")
print("=" * 70)

A1 = "Attachment 1 - Communication Procedures"

# 2a. Delete nested DC Procedure duplicates (same as top-level DC Procedure/)
dup_dirs = [
    f"{A1}/DCC requirements/DC Procedure/PR-5312-1000-PM-0009 Project Document Control Procedure",
    f"{A1}/DCC requirements/DC Procedure/PR-5312-1000-PM-0010 Document Numbering Procedure",
    f"{A1}/DCC requirements/DC Procedure/PR-5312-1000-PM-0012 Vendor Documentation Control Procedure",
]
for d in dup_dirs:
    rm(d)

# 2b. Delete top-level duplicates of Guideline and SUBCON templates (DCC versions are the originals)
# Verify same content first, then delete top-level copies
top_dups = [
    (f"{A1}/Guideline for Subcontractor's Document Management_20250618.docx",
     f"{A1}/DCC requirements/Guideline for Subcontractor's Document Management_20250618.docx"),
    (f"{A1}/SUBCON Project Management Doc Template-General.docx",
     f"{A1}/DCC requirements/SUBCON Project Management Doc Template-General.docx"),
    (f"{A1}/SUBCON Project Management Doc Template-ITP.docx",
     f"{A1}/DCC requirements/SUBCON Project Management Doc Template-ITP.docx"),
]
for top, dcc in top_dups:
    if verify_same(top, dcc):
        rm(top)

# 2c. Rename files in DCC requirements/
mv(f"{A1}/DCC requirements/CRS Template - PR-5312-1000-PM-0001 Rev.A_CRS.xlsx",
   f"{A1}/DCC requirements/CRS Template_PR-5312-1000-PM-0001 Rev.A.xlsx")

mv(f"{A1}/DCC requirements/Guideline for Subcontractor's Document Management_20250618.docx",
   f"{A1}/DCC requirements/Guideline - Subcontractors Document Management.docx")

mv(f"{A1}/DCC requirements/SUBCON Project Management Doc Template-General.docx",
   f"{A1}/DCC requirements/Subcon PM Doc Template - General.docx")

mv(f"{A1}/DCC requirements/SUBCON Project Management Doc Template-ITP.docx",
   f"{A1}/DCC requirements/Subcon PM Doc Template - ITP.docx")

# PM-0010 dated version has different content from DC Procedure version — keep, rename
mv(f"{A1}/DCC requirements/PR-5312-1000-PM-0010_0 Document Numbering Procedure_20250618.pdf",
   f"{A1}/DCC requirements/PR-5312-1000-PM-0010_Document Numbering Procedure_2025-06-18.pdf")

# 2d. Rename Subcontract Template files
ST = f"{A1}/DCC requirements/Subcontract Template"
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

# 2e. Move docweb_help files up to DC Procedure, delete empty WISON subfolder
docweb_files = [
    f"{A1}/DCC requirements/DC Procedure/WISON DC Portal Operation manual/docweb_help.pdf",
    f"{A1}/DCC requirements/DC Procedure/WISON DC Portal Operation manual/docweb_help_en.pdf",
]
for f in docweb_files:
    src = os.path.join(ROOT, f)
    if os.path.exists(src):
        dst = os.path.join(ROOT, A1, "DC Procedure", os.path.basename(f))
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        os.rename(src, dst)
        print(f"  MOVE: {f}\n     -> {A1}/DC Procedure/{os.path.basename(f)}")

# Delete empty WISON DC Portal Operation manual dir
rm(f"{A1}/DCC requirements/DC Procedure/WISON DC Portal Operation manual")
# Delete empty DC Procedure under DCC (should be empty now)
dc_proc_dcc = os.path.join(ROOT, A1, "DCC requirements", "DC Procedure")
if os.path.isdir(dc_proc_dcc) and not os.listdir(dc_proc_dcc):
    rm(f"{A1}/DCC requirements/DC Procedure")

print()
print("=" * 70)
print("PHASE 3: Attachment 2 — Change Management")
print("=" * 70)

A2 = "Attachment 2 - Change Management"
mv(f"{A2}/CHANGE management.docx", f"{A2}/Change Management Procedure.docx")
mv(f"{A2}/CHANGE management.pdf", f"{A2}/Change Management Procedure_Signed.pdf")

print()
print("=" * 70)
print("PHASE 4: Attachment 3 — HSE Requirements")
print("=" * 70)

A3 = "Attachment 3 - HSE requirements"

# 4a. Rename scattered files at HSE Requirements Attachments root
HRA = f"{A3}/HSE Requirements Attachments"

# Check if "1 HSE Requirements.pdf" is same as top-level "HSE Requirements.pdf"
top_hse_pdf = f"{A3}/HSE Requirements.pdf"
sub1_hse_pdf = f"{HRA}/1  HSE Requirements.pdf"
hse_same = verify_same(top_hse_pdf, sub1_hse_pdf)
if hse_same:
    rm(sub1_hse_pdf)  # delete duplicate
elif hse_same is False:
    print("  ⚠ HSE Requirements top vs sub differ — keeping both")

# Numbered files — remove number prefix, use proper ordering
mv(f"{HRA}/3 ADR002 - Updated HSE Requirements.pdf",
   f"{HRA}/ADR-002_Updated HSE Requirements.pdf")
mv(f"{HRA}/4 ADR003 - Asset Integrity.pdf",
   f"{HRA}/ADR-003_Asset Integrity.pdf")
mv(f"{HRA}/5 ADNOC Group Medical Fitness Guidelines for Contractors-1 APR 2023.pdf",
   f"{HRA}/ADNOC Group Medical Fitness Guidelines for Contractors_2023-04-01.pdf")

# Move HSE audit register to APPENDIX area
mv(f"{HRA}/2025 Camp  Welfare Audit Register 1.pdf",
   f"{HRA}/APPENDIX 4-Pre Mobilization Audit and Pre-Execution Audit Checklist/Camp Welfare Audit Register_2025.pdf")

# ADNOC Vehicle Inspection — keep in root, rename
mv(f"{HRA}/ADNOC Unified Vehicle Inspection Guidelines.pdf",
   f"{HRA}/ADNOC Unified Vehicle Inspection Guidelines.pdf")  # already good

# Contractor Onboarding — keep, rename
mv(f"{HRA}/Contractor Onboarding Guidelines.pdf",
   f"{HRA}/Contractor Onboarding Guidelines.pdf")  # already good

# 4b. Rename APPENDIX folders
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

# 4c. Rename "2 HSE requirements Attachments" → clean
mv(f"{HRA}/2 HSE requirements Attachments",
   f"{HRA}/Att A-D_HSE Standards")

# 4d. Rename "1  HSE Requirements.pdf" if not deleted as duplicate
sub1 = os.path.join(ROOT, sub1_hse_pdf)
if os.path.exists(sub1):
    mv(sub1_hse_pdf, f"{HRA}/Att 00_HSE Requirements - Main Body.pdf")

# 4e. Rename top-level HSE Requirements docs
mv(f"{A3}/HSE Requirements.docx",
   f"{A3}/HSE Requirements.docx")  # good as-is (contract docx master)
mv(f"{A3}/HSE Requirements.pdf",
   f"{A3}/HSE Requirements_Signed.pdf")

# 4f. Rename files in App 01 (Contractor Management Procedures)
AP1 = f"{HRA}/App 01_Contractor Management Procedures"
# PR-5312-1000-SA-0001~0008 — already good names, just clean up extra spaces
for old_name in os.listdir(os.path.join(ROOT, AP1)):
    if old_name.startswith('PR-5312'):
        new_name = old_name.replace('  ', ' ').replace('\xa0', ' ')
        if new_name != old_name:
            mv(f"{AP1}/{old_name}", f"{AP1}/{new_name}")

# 4g. Rename files in App 03 (HSE Assurance)
AP3 = f"{HRA}/App 03_HSE Assurance Program"
mv(f"{AP3}/CONTRACTOR HSE ASSURANCE PROGRAM.pdf",
   f"{AP3}/Contractor HSE Assurance Program.pdf")
mv(f"{AP3}/HSE PERFORMANCE CONTRACT.pdf",
   f"{AP3}/HSE Performance Contract.pdf")

# 4h. Rename files in App 04 (Pre-Mob Audit)
AP4 = f"{HRA}/App 04_Pre-Mob - Pre-Execution Audit Checklists"
mv(f"{AP4}/Mobilization (Pre-Execution) Audit Checklist.xlsx",
   f"{AP4}/Mobilization Pre-Execution Audit Checklist.xlsx")
mv(f"{AP4}/Pre Mobilization Audit Checklist.xlsx",
   f"{AP4}/Pre-Mobilization Audit Checklist.xlsx")
# HSE-GA-ST05 in App 04 — also exists in ATTACH-A; check if duplicate
ap4_ga = f"{AP4}/HSE-GA-ST05_V1 Contractor HSE Mgmt.pdf"
att_a_ga = f"{HRA}/Att A-D_HSE Standards/ATTACH-A/HSE-GA-ST05_V1 Contractor HSE Mgmt.pdf"
if verify_same(ap4_ga, att_a_ga):
    rm(ap4_ga)  # duplicate of ATTACH-A copy
elif os.path.exists(os.path.join(ROOT, ap4_ga)) and os.path.exists(os.path.join(ROOT, att_a_ga)):
    # different — keep both, rename the App 04 one
    mv(ap4_ga, f"{AP4}/HSE-GA-ST05_V1 Contractor HSE Mgmt_App 04 copy.pdf")

# 4i. Rename files in App 02
AP2 = f"{HRA}/App 02_ADNOC HSEWM Min Requirements in Contracts"
mv(f"{AP2}/ADNOC HSEWM Min Reqts in Contracts.pdf",
   f"{AP2}/ADNOC HSEWM Min Requirements in Contracts.pdf")

# 4j. Rename files in App 05
AP5 = f"{HRA}/App 05_ADNOC Approved Training Providers"
mv(f"{AP5}/ADNOC Approved Training Providers October 2025 V3.pdf",
   f"{AP5}/ADNOC Approved Training Providers_2025-10_V3.pdf")

print()
print("=" * 70)
print("PHASE 5: Attachment 4 — Quality Management")
print("=" * 70)

A4 = "Attachment 4 - Quality Management"
QM = f"{A4}/Quality Management Requirements"

# QAQC files — different content, keep both, rename poorly-named one
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

# Top-level quality docs
mv(f"{A4}/QUALITY REQUIREMENTS FOR SUBCONTRACTORS.docx",
   f"{A4}/Quality Requirements for Subcontractors.docx")
mv(f"{A4}/QUALITY REQUIREMENTS FOR SUBCONTRACTORS.pdf",
   f"{A4}/Quality Requirements for Subcontractors_Signed.pdf")

print()
print("=" * 70)
print("PHASE 6: Attachment 5 — Scope of Work")
print("=" * 70)

A5 = "Attachment 5 - Scope of Work"

# 6a. Rename numbered files
mv(f"{A5}/1. Scope of Work for Package 2.docx",
   f"{A5}/Att 01_Scope of Work - Civil Pkg II.docx")
mv(f"{A5}/1. Scope of Work for Package 2.pdf",
   f"{A5}/Att 01_Scope of Work - Civil Pkg II_Signed.pdf")

mv(f"{A5}/2. Responsibility Matrix.docx",
   f"{A5}/Att 02_Responsibility Matrix.docx")
mv(f"{A5}/2. Responsibility Matrix.pdf",
   f"{A5}/Att 02_Responsibility Matrix_Signed.pdf")

# 6b. Schedule Requirements
SR = f"{A5}/3. Schedule Requirements"
mv(f"{SR}/SCHEDULE AND REPORTING REQUIREMENT.docx",
   f"{A5}/Att 03_Schedule - Reporting Requirement.docx")
mv(f"{SR}/SCHEDULE AND REPORTING REQUIREMENT.pdf",
   f"{A5}/Att 03_Schedule - Reporting Requirement_Signed.pdf")

mv(f"{SR}/DELAY LIQUIDATED DAMAGES - PACKAGE 2.docx",
   f"{A5}/Att 04_Delay LD - Civil Pkg II.docx")
mv(f"{SR}/DELAY LIQUIDATED DAMAGES - PACKAGE 2.pdf",
   f"{A5}/Att 04_Delay LD - Civil Pkg II_Signed.pdf")

# Rename Annexes folder
mv(f"{SR}/Annexes to SCHEDULE AND REPORTING REQUIREMENT",
   f"{SR}/Annexes_Schedule - Reporting")

# Rename Annex files
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
    if os.path.exists(os.path.join(ROOT, ANN, old)):
        mv(f"{ANN}/{old}", f"{ANN}/{new}")

# 6c. Key Personnel
KP = f"{A5}/4. Key Personnel"
mv(f"{KP}/Appendix - Key Personnel & Liquidated Damages.docx",
   f"{A5}/Att 05_Key Personnel - LD.docx")
mv(f"{KP}/Appendix - Key Personnel & Liquidated Damages.pdf",
   f"{A5}/Att 05_Key Personnel - LD_Signed.pdf")

# 6d. Approved Vendor & Contractor List
AV = f"{A5}/5. Approved Vendor & Contractor List"
mv(f"{AV}/ACL updated   07 2025.xlsx",
   f"{AV}/Approved Contractor List_2025-07.xlsx")
mv(f"{AV}/AVL_26022025.xlsx",
   f"{AV}/Approved Vendor List_2025-02-26.xlsx")

# 6e. Rename subfolders (after files moved out)
mv(f"{A5}/3. Schedule Requirements", f"{A5}/03_Schedule - Reporting")
mv(f"{A5}/4. Key Personnel", f"{A5}/04_Key Personnel")
mv(f"{A5}/5. Approved Vendor & Contractor List", f"{A5}/05_Approved Vendor - Contractor List")

print()
print("=" * 70)
print("PHASE 7: Attachment 6 — Commercials")
print("=" * 70)

A6 = "Attachment 6 - Commercials"

mv(f"{A6}/Exhibit A BOQ For CIVIL AND BLDG_Rev.B-PACKAGE II.pdf",
   f"{A6}/Att 01_BOQ - Civil - BLDG Pkg II_Rev.B_Signed.pdf")

# Exhibit B Measurement Method files
EB = f"{A6}/Exhibit B Measurement Method"
mv(f"{EB}/01. General-Subcontractor Pricing Instructions_Rev.A.docx",
   f"{EB}/01_General - Subcontractor Pricing Instructions_Rev.A.docx")
mv(f"{EB}/01. General-Subcontractor Pricing Instructions_Rev.A.pdf",
   f"{EB}/01_General - Subcontractor Pricing Instructions_Rev.A_Signed.pdf")

# Rename numbered measurement method files (& → -)
for old_name in os.listdir(os.path.join(ROOT, EB)):
    if old_name.startswith(('02.', '03.', '10.')):
        new_name = old_name.replace('&', '-')
        if new_name != old_name:
            mv(f"{EB}/{old_name}", f"{EB}/{new_name}")

# Exhibit C Bank Bond Template
mv(f"{A6}/Exhibit C Bank Bond Template/Bank Bond Format-ADNOC.docx",
   f"{A6}/Att 02_Bank Bond Format - ADNOC.docx")
# Remove empty Exhibit C folder
bank_dir = os.path.join(ROOT, A6, "Exhibit C Bank Bond Template")
if os.path.isdir(bank_dir) and not os.listdir(bank_dir):
    rm(f"{A6}/Exhibit C Bank Bond Template")

print()
print("=" * 70)
print("PHASE 8: Attachment 7 — Owner's Special Requirements")
print("=" * 70)

A7 = "Attachment 7 - Owner's Special Requirements &Reference"

# 8a. Delete B.16 duplicate (same MD5, keep the one with full title)
b16_full = f"{A7}/5. Subcontracting/EXHIBIT-B.16 SELECTION OF SUBCONTRACTORS AND VENDORS.pdf"
b16_short = f"{A7}/5. Subcontracting/EXHIBIT-B.16.pdf"
if verify_same(b16_full, b16_short):
    rm(b16_short)

# 8b. Rename folder "1. COMPANY's code and standard Draw"
mv(f"{A7}/1. COMPANY's code and standard Draw",
   f"{A7}/01_Company Codes - Standard Drawings")

# 8c. Rename AGES-Reference files for readability
AGES = f"{A7}/01_Company Codes - Standard Drawings/AGES-Reference"
for old_name in os.listdir(os.path.join(ROOT, AGES)):
    if old_name.startswith('AGES-SP-') and old_name.endswith('.pdf'):
        # Insert _ after the spec number
        parts = old_name.split(' ', 1)
        if len(parts) == 2:
            new_name = f"{parts[0]}_{parts[1]}"
            if new_name != old_name:
                mv(f"{AGES}/{old_name}", f"{AGES}/{new_name}")

# 8d. Rename AGES-ST Draw file
STD = f"{A7}/01_Company Codes - Standard Drawings/AGES-ST Draw"
mv(f"{STD}/AGES STD dwgs - Consolidated-CV AR.pdf",
   f"{STD}/AGES STD Drawings - Consolidated - Civil_AR.pdf")

# 8e. Rename compliance/ethics files
CMP = f"{A7}/2. Compliance and ethics code"
mv(f"{CMP}/2022 ADNOC Group Code of Conduct Employee- En.pdf",
   f"{CMP}/ADNOC Group Code of Conduct - Employee_2022_EN.pdf")
mv(f"{CMP}/Supplier Code of Ethics En.pdf",
   f"{CMP}/ADNOC Group Supplier Code of Business Ethics_EN.pdf")

# 8f. Rename ICV files
ICV = f"{A7}/3. ICV requirements"
mv(f"{ICV}/ADNOC ICV  Implementation Guideline - Rev.3.1.pdf",
   f"{ICV}/ADNOC ICV Implementation Guideline_Rev.3.1.pdf")
mv(f"{ICV}/ICV Improvement Plan Template - Agreement Specific R1.xlsx",
   f"{ICV}/ICV Improvement Plan Template_Agreement Specific_R1.xlsx")

# 8g. Rename Insurance
INS = f"{A7}/4. Insurance Requirements"
mv(f"{INS}/Insurance Requirements.docx",
   f"{INS}/Insurance Requirements.docx")  # already good

# 8h. Rename Subcontracting files
SUB = f"{A7}/5. Subcontracting"
# B.16 with full title is already good
mv(f"{SUB}/EXHIBIT-B.16 SELECTION OF SUBCONTRACTORS AND VENDORS.pdf",
   f"{SUB}/Exh B.16_Selection of Subcontractors and Vendors.pdf")

# 8i. Rename remaining numbered folders
mv(f"{A7}/2. Compliance and ethics code",
   f"{A7}/02_Compliance - Ethics Code")
mv(f"{A7}/3. ICV requirements",
   f"{A7}/03_ICV Requirements")
mv(f"{A7}/4. Insurance Requirements",
   f"{A7}/04_Insurance Requirements")
mv(f"{A7}/5. Subcontracting",
   f"{A7}/05_Subcontracting")

print()
print("=" * 70)
print("DONE — All operations completed.")
print("=" * 70)
