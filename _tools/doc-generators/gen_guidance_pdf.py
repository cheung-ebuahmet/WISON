# -*- coding: utf-8 -*-
"""把 Guidance HTML 用 Edge headless 转成 PDF（本地，不联网）。"""
import os
import subprocess

base = r'D:/Wison/Project_Info/Wison Template'
pq = None
for name in os.listdir(base):
    if 'Pre-Qualification' in name:
        pq = os.path.join(base, name)
        break
rev = os.path.join(pq, 'ADNOC WISON RSGP Pre-Qualification Requirements (REVISED)')

html_path = os.path.join(rev, '00 - Submission Guidance (REVISED).html')
pdf_path = os.path.join(rev, '00 - Submission Guidance (REVISED).pdf')

edge = r'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'
html_uri = 'file:///' + html_path.replace('\\', '/')

r = subprocess.run([
    edge, '--headless', '--disable-gpu', '--no-sandbox',
    '--print-to-pdf=' + pdf_path,
    html_uri
], capture_output=True, text=True, timeout=60)

if os.path.exists(pdf_path):
    print('PDF OK:', pdf_path, os.path.getsize(pdf_path), 'bytes')
else:
    print('PDF FAILED')
    print('stdout:', r.stdout[:300])
    print('stderr:', r.stderr[:800])
