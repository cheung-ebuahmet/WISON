# -*- coding: utf-8 -*-
"""打包分包注册交付包：
  - 00 - Submission Guidance (REVISED).pdf  (指引)
  - A/B/C/D/E/F 六个附件文件夹（含模板）
打包成 ZIP，供发送给分包。"""
import os
import zipfile

base = r'D:/Wison/Project_Info/Wison Template'
pq = None
for name in os.listdir(base):
    if 'Pre-Qualification' in name:
        pq = os.path.join(base, name)
        break
rev = os.path.join(pq, 'ADNOC WISON RSGP Pre-Qualification Requirements (REVISED)')

zip_path = os.path.join(rev, 'Subcontractor Registration Package.zip')

guidance_pdf = os.path.join(rev, '00 - Submission Guidance (REVISED).pdf')
folders = ['A - Company Information', 'B - Legal Compliance', 'C - Financial Information',
           'D - Contact of Supplier', 'E - Qualification Information', 'F - ICV Certificate']

with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as z:
    # 指引 PDF 放根
    z.write(guidance_pdf, arcname='00 - Submission Guidance (REVISED).pdf')
    # 各文件夹 + 内容
    for folder in folders:
        fp = os.path.join(rev, folder)
        if os.path.isdir(fp):
            for f in sorted(os.listdir(fp)):
                full = os.path.join(fp, f)
                z.write(full, arcname=os.path.join(folder, f))
            # 空文件夹也保留（A/E/F 无模板但需占位）
            if not os.listdir(fp):
                z.writestr(folder + '/.keep', '')

print('ZIP OK:', zip_path, os.path.getsize(zip_path), 'bytes')

# 列出 ZIP 内容
with zipfile.ZipFile(zip_path) as z:
    print('\n=== ZIP 内容 ===')
    for n in z.namelist():
        print('  ', n)
