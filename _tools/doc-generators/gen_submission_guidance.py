# -*- coding: utf-8 -*-
"""生成 Submission Guidance HTML 到 REVISED 目录。
v5.0：只讲「必上传附件」，不再要求分包填写注册信息（Wison 内部自行填写）。
"""
import os

HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Subcontractor Registration — Document Submission Requirements</title>
<style>
  body { font-family: 'Segoe UI', Arial, sans-serif; color: #1f2937; margin: 0; background: #f4f7fb; }
  .wrap { max-width: 900px; margin: 0 auto; padding: 24px; }
  .card { background: #fff; border-radius: 10px; box-shadow: 0 2px 8px rgba(0,0,0,.08); padding: 24px; margin-bottom: 20px; }
  h1 { color: #1F4E79; font-size: 24px; margin: 0 0 4px; }
  h2 { color: #1F4E79; font-size: 18px; border-left: 4px solid #2E75B6; padding-left: 10px; margin: 24px 0 12px; }
  .sub { color: #6b7280; font-size: 13px; margin-top: 0; }
  table { border-collapse: collapse; width: 100%; font-size: 13px; }
  th { background: #2E75B6; color: #fff; padding: 8px 10px; text-align: left; }
  td { border: 1px solid #dbe5f1; padding: 8px 10px; vertical-align: top; }
  tr:nth-child(even) td { background: #f0f6fc; }
  .req { color: #c0392b; font-weight: bold; }
  .opt { color: #808080; }
  .note { background: #fff8e1; border-left: 4px solid #f0b429; padding: 10px 14px; border-radius: 6px; font-size: 13px; margin: 10px 0; }
  .warn { background: #fdecea; border-left: 4px solid #c0392b; padding: 10px 14px; border-radius: 6px; font-size: 13px; margin: 10px 0; }
  .file { font-family: Consolas, monospace; font-size: 12px; color: #1F4E79; background: #eef4fb; padding: 1px 6px; border-radius: 4px; }
  .folder { color: #7f6000; font-weight: bold; }
  ul { padding-left: 22px; }
  li { margin: 5px 0; }
  .tag { display: inline-block; padding: 1px 8px; border-radius: 10px; font-size: 11px; font-weight: bold; }
  .tag-tpl { background: #e8f5e9; color: #2e7d32; border: 1px solid #a5d6a7; }
  .tag-own { background: #fff2cc; color: #7f6000; border: 1px solid #f0b429; }
  .tag-ref { background: #e3f2fd; color: #1565c0; border: 1px solid #90caf9; }
</style>
</head>
<body>
<div class="wrap">

<div class="card">
  <h1>Subcontractor Registration — Document Submission Requirements</h1>
  <p class="sub">WISON — ADNOC RSGP Project · v5.0 (REVISED)</p>
  <p>To our valued Subcontractor / Supplier:</p>
  <p>Please provide the <b>supporting documents listed below</b>. The registration form itself will be completed by Wison; you only need to prepare and return the documents indicated.</p>
  <p class="warn">⚠️ Documents marked <span class="req">red</span> are <b>mandatory</b> and must not be omitted.</p>
</div>

<div class="card">
  <h2>Documents to provide</h2>
  <table>
    <tr><th>Ref</th><th>Document</th><th>Folder</th><th>How</th></tr>
    <tr><td><span class="req">A1</span></td><td>Business Registration Certificate</td><td><span class="folder">A - Company Information</span></td><td><span class="tag tag-own">Self-provided</span></td></tr>
    <tr><td><span class="req">A2</span></td><td>Type of Work / Activities — Qualification &amp; Licenses Certificate</td><td><span class="folder">A - Company Information</span></td><td><span class="tag tag-own">Self-provided</span></td></tr>
    <tr><td><span class="req">A3</span></td><td>Company profile (brochure / PDF / PPT)</td><td><span class="folder">A - Company Information</span></td><td><span class="tag tag-own">Self-provided</span></td></tr>
    <tr><td><span class="req">B1</span></td><td>Due Diligence Questionnaire (signed &amp; stamped)</td><td><span class="folder">B - Legal Compliance</span></td><td><span class="tag tag-tpl">Template provided</span></td></tr>
    <tr><td><span class="req">B2</span></td><td>Undertaking of Honest Conduct (signed &amp; stamped)</td><td><span class="folder">B - Legal Compliance</span></td><td><span class="tag tag-tpl">Template provided</span></td></tr>
    <tr><td><span class="req">C1</span></td><td>Certified financial statement (last 3 years)</td><td><span class="folder">C - Financial Information</span></td><td><span class="tag tag-own">Self-provided</span></td></tr>
    <tr><td><span class="req">C2</span></td><td>Supplier Receipt Account Confirmation Letter (stamped)</td><td><span class="folder">C - Financial Information</span></td><td><span class="tag tag-tpl">Template provided</span></td></tr>
    <tr><td><span class="req">C3</span></td><td>Bank account proof (bank-issued)</td><td><span class="folder">C - Financial Information</span></td><td><span class="tag tag-ref">Reference only</span></td></tr>
    <tr><td><span class="req">D1</span></td><td>Authorization Letter — Supplier Portal Account</td><td><span class="folder">D - Contact of Supplier</span></td><td><span class="tag tag-tpl">Template provided</span></td></tr>
    <tr><td><span class="req">D2</span></td><td>Authorization Letter — Business Leader</td><td><span class="folder">D - Contact of Supplier</span></td><td><span class="tag tag-tpl">Template provided</span></td></tr>
    <tr><td><span class="req">E1</span></td><td>QA Certificate (matching your Quality Standard)</td><td><span class="folder">E - Qualification Information</span></td><td><span class="tag tag-own">Self-provided</span></td></tr>
    <tr><td><span class="req">E2</span></td><td>Approval Certificate (3rd party) <b>or</b> Quality Manual</td><td><span class="folder">E - Qualification Information</span></td><td><span class="tag tag-own">Self-provided</span></td></tr>
    <tr><td><span class="req">F1</span></td><td>ICV Certificate <span class="opt">(only if applicable — non-UAE companies may skip)</span></td><td><span class="folder">F - ICV Certificate</span></td><td><span class="tag tag-own">Self-provided</span></td></tr>
  </table>
  <div class="warn">
    <b>⚠️ B1 &amp; B2 — legal documents (sign &amp; seal verification):</b>
    <ul style="margin:6px 0 0 18px;">
      <li>Use the <b>latest template downloaded from the system</b> and <b>do not modify</b> it.</li>
      <li>For an <b>electronic seal / signature</b>, attach the seal process of the electronic seal/signature platform or the auto-generated verification link.</li>
      <li>A <b>cut-and-paste seal or signature is invalid</b> — the seal/signature will be verified to prevent tampering.</li>
    </ul>
  </div>
  <p class="note">G / H / I modules (Construction Capacity, Equipment &amp; Tools, Experience) require <b>no documents</b> — those are handled by Wison.</p>
</div>

<div class="card">
  <h2>Templates provided (fill → print → sign → stamp → scan)</h2>
  <p>The following templates are included in the corresponding folders. Complete them on computer, then <b>print, sign, stamp</b> and scan to PDF. Name the PDF with your company name.</p>
  <table>
    <tr><th>Ref</th><th>Template file</th><th>Scan output (name it)</th></tr>
    <tr><td><b>B1</b></td><td><span class="file">B1 - Due Diligence Questionnaire (Template).xlsx</span></td><td><span class="file">DDQ_YourCompanyName.pdf</span></td></tr>
    <tr><td><b>B2</b></td><td><span class="file">B2 - Undertaking of Honest Conduct (Template).xlsx</span></td><td><span class="file">Integrity_Commitment_YourCompanyName.pdf</span></td></tr>
    <tr><td><b>C2</b></td><td><span class="file">C2 - Supplier Collection Account Confirmation Letter (Template).docx</span></td><td><span class="file">Bank_Account_Confirmation_YourCompanyName.pdf</span></td></tr>
    <tr><td><b>C3</b></td><td><span class="file">C3 - Bank Account Proof (Reference only).pdf</span> <span class="opt">(reference only — bank issues its own)</span></td><td><span class="file">Bank_Proof_YourCompanyName.pdf</span></td></tr>
    <tr><td><b>D1</b></td><td><span class="file">D1 - Authorization Letter - Supplier Portal Account.docx</span></td><td><span class="file">Authorization_Portal_YourCompanyName.pdf</span></td></tr>
    <tr><td><b>D2</b></td><td><span class="file">D2 - Authorization Letter - Business Leader.docx</span></td><td><span class="file">Authorization_BusinessLeader_YourCompanyName.pdf</span></td></tr>
  </table>
  <p class="warn">⚠️ <b>Do not modify the templates.</b> Seals and signatures are subject to verification; any tampered or cut-and-paste seal/signature will be rejected.</p>
</div>

<div class="card">
  <h2>Submission checklist</h2>
  <p>Return the following to Wison (place each file into its module folder, name the PDF with your company name):</p>
  <ul>
    <li><span class="req">A1</span> Business Registration Certificate</li>
    <li><span class="req">A2</span> Type of Work / Activities — Qualification &amp; Licenses Certificate</li>
    <li><span class="req">A3</span> Company profile</li>
    <li><span class="req">B1</span> Due Diligence Questionnaire — signed &amp; stamped</li>
    <li><span class="req">B2</span> Undertaking of Honest Conduct — signed &amp; stamped</li>
    <li><span class="req">C1</span> Certified financial statement (last 3 years)</li>
    <li><span class="req">C2</span> Supplier Receipt Account Confirmation Letter — stamped</li>
    <li><span class="req">C3</span> Bank account proof (bank-issued)</li>
    <li><span class="req">D1</span> / <span class="req">D2</span> Authorization Letters</li>
    <li><span class="req">E1</span> QA Certificate</li>
    <li><span class="req">E2</span> Approval Certificate <b>or</b> Quality Manual</li>
    <li><span class="req">F1</span> ICV Certificate <span class="opt">(only if applicable)</span></li>
  </ul>
</div>

</div>
</body>
</html>
"""


def main():
    base = r'D:/Wison/Project_Info/Wison Template'
    pq = None
    for name in os.listdir(base):
        if 'Pre-Qualification' in name:
            pq = os.path.join(base, name)
            break
    rev = os.path.join(pq, 'ADNOC WISON SGP Pre-Qualification Requirements (REVISED)')

    out = os.path.join(rev, '00 - Submission Guidance (REVISED).html')
    with open(out, 'w', encoding='utf-8') as f:
        f.write(HTML)
    print('WROTE:', out)
    print('SIZE:', os.path.getsize(out), 'bytes')


if __name__ == '__main__':
    main()
