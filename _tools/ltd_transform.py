#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, copy, re, zipfile
from lxml import etree

W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
XML = 'http://www.w3.org/XML/1998/namespace'
def q(t): return f'{{{W}}}{t}'

# Rules applied to the concatenated w:t text of each paragraph.
# Optional surrounding [] brackets are consumed so output is always the bracketed placeholder.
RULES = [
    (re.compile(r'\[?Cangzhou Longtaidi Pipe Technology Co\., Ltd\.?\]?'), '[Company Name]',      'name'),
    (re.compile(r'沧州隆泰迪管道科技有限公司'),                                '[公司名称]',         'cn'),
    (re.compile(r'\[?沧州经济开发区黄河东路33号\]?'),                          '[Registered Address]','addr'),
]

def make_ph_rpr(orig_rpr):
    rpr = copy.deepcopy(orig_rpr) if orig_rpr is not None else etree.Element(q('rPr'))
    for tag in ('shd', 'highlight'):
        for el in rpr.findall(q(tag)):
            rpr.remove(el)
    shd = etree.Element(q('shd'))
    shd.set(q('val'), 'clear'); shd.set(q('color'), 'auto'); shd.set(q('fill'), 'FFFF00')
    lang = rpr.find(q('lang'))
    if lang is not None:
        rpr.insert(list(rpr).index(lang), shd)
    else:
        rpr.append(shd)
    return rpr

def realize(run, s, e, txt, start_map, covered):
    """Rebuild one run that overlaps a token region. Returns #placeholders emitted."""
    # guard: target runs must be simple rPr+t (no br/tab inside)
    for c in run:
        if c.tag not in (q('rPr'), q('t')):
            raise RuntimeError(f'unexpected child {c.tag} in modified run')
    pieces = []; cur = []; i = s
    while i < e:
        if i in start_map:
            if cur: pieces.append(('keep', ''.join(cur))); cur = []
            pieces.append(('ph', start_map[i]))
            i += 1
            while i < e and (i in covered) and (i not in start_map):
                i += 1
            continue
        if i in covered:
            if cur: pieces.append(('keep', ''.join(cur))); cur = []
            i += 1; continue
        cur.append(txt[i - s]); i += 1
    if cur: pieces.append(('keep', ''.join(cur)))
    if len(pieces) == 1 and pieces[0] == ('keep', txt):
        return 0
    parent = run.getparent()
    idx = list(parent).index(run)
    orig_rpr = run.find(q('rPr'))
    new_runs = []; ph = 0
    for kind, text in pieces:
        r_el = etree.Element(q('r'))
        if kind == 'keep':
            if orig_rpr is not None:
                r_el.append(copy.deepcopy(orig_rpr))
        else:
            r_el.append(make_ph_rpr(orig_rpr)); ph += 1
        t_el = etree.SubElement(r_el, q('t'))
        t_el.set(f'{{{XML}}}space', 'preserve')
        t_el.text = text
        new_runs.append(r_el)
    parent.remove(run)
    for k, nr in enumerate(new_runs):
        parent.insert(idx + k, nr)
    return ph

def transform_document(doc_bytes):
    tree = etree.fromstring(doc_bytes).getroottree()
    root = tree.getroot()
    counts = {'name': 0, 'cn': 0, 'addr': 0}
    for p in root.iter(q('p')):
        runs = list(p.iter(q('r')))
        run_spans = []; pos = 0
        for r in runs:
            ts = r.findall(q('t'))
            rtxt = ''.join(x.text or '' for x in ts)
            run_spans.append((r, pos, pos + len(rtxt), rtxt))
            pos += len(rtxt)
        S = ''.join(rs[3] for rs in run_spans)
        if not S:
            continue
        ops = []
        for rx, rep, kind in RULES:
            for m in rx.finditer(S):
                ops.append((m.start(), m.end(), rep, kind))
        if not ops:
            continue
        ops.sort()
        # disjoint check
        for a, b in zip(ops, ops[1:]):
            if a[1] > b[0]:
                raise RuntimeError(f'overlapping matches {a} {b} in paragraph {S[:60]!r}')
        start_map = {a: rep for (a, b, rep, kind) in ops}
        covered = set()
        for a, b, rep, kind in ops:
            for i in range(a, b):
                covered.add(i)
            counts[kind] += 1
        # realize each overlapping run
        for (r, s, e, rtxt) in run_spans:
            if any(s <= i < e for i in covered) or any(s <= a < e for a in start_map):
                realize(r, s, e, rtxt, start_map, covered)
    new_bytes = etree.tostring(tree, xml_declaration=True, encoding='UTF-8', standalone=True)
    return new_bytes, counts

def build_copy(src, dst):
    zin = zipfile.ZipFile(src, 'r')
    new_doc, counts = transform_document(zin.read('word/document.xml'))
    zout = zipfile.ZipFile(dst, 'w')
    for item in zin.infolist():
        data = zin.read(item.filename)
        if item.filename == 'word/document.xml':
            data = new_doc
        # preserve original per-entry compression type
        zi = zipfile.ZipInfo(item.filename, date_time=item.date_time)
        zi.compress_type = item.compress_type
        zi.external_attr = item.external_attr
        zi.internal_attr = item.internal_attr
        zi.create_system = item.create_system
        zout.writestr(zi, data)
    zout.close(); zin.close()
    return counts

if __name__ == '__main__':
    src, dst = sys.argv[1], sys.argv[2]
    c = build_copy(src, dst)
    print(f'OK  name={c["name"]} cn={c["cn"]} addr={c["addr"]}  -> {dst}')
