#!/usr/bin/env python
"""Extract text from .docx files. Usage: python extract_docx.py <path> [max_paras]"""
import sys, zipfile, xml.etree.ElementTree as ET

def main():
    path = sys.argv[1]
    limit = int(sys.argv[2]) if len(sys.argv) > 2 else 100
    z = zipfile.ZipFile(path)
    xml = z.read('word/document.xml')
    tree = ET.fromstring(xml)
    ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    paras = tree.findall('.//w:p', ns)
    for p in paras[:limit]:
        texts = [t.text for t in p.findall('.//w:t', ns) if t.text]
        line = ''.join(texts).strip()
        if line:
            print(line)

if __name__ == "__main__":
    main()
