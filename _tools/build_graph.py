#!/usr/bin/env python3
"""
build_graph.py — Wison Knowledge Graph Compiler
Reads all existing YAML/MD/DOCX data assets and compiles:
  - _Ref/data/graph/nodes.yaml
  - _Ref/data/graph/edges.yaml
  - _Ref/data/graph/graph.json

Usage: python build_graph.py [--validate]
"""
import os, sys, json, re
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: pyyaml required. Install: pip install pyyaml")
    sys.exit(1)

BASE = Path(r"D:\Wison")
REF_DATA = BASE / "_Ref" / "data"
OUT_DIR = REF_DATA / "graph"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# ============================================================
# DATA STRUCTURES
# ============================================================
nodes = {}   # node_id → {type, label, data}
edges = []   # [{source, target, type, metadata}]
def normalize_clause_id(framework, raw_ref):
    """Normalize a raw clause reference into a consistent graph node ID.

    Examples:
      CIVIL, "Sub-Clause 4.2.4"     → CIVIL-COC-4-2-4
      CIVIL, "Sub-Clause 4.3.7"     → CIVIL-COC-4-3-7
      CIVIL, "Article 21.2"         → CIVIL-COC-21-2
      CIVIL, "Attachment 5"         → CIVIL-COC-Att-5
      MEI,   "SCS Clause 17"        → MEI-SCS-17
      MEI,   "SCS Clause 5.6"       → MEI-SCS-5-6
      MEI,   "Exhibit A.2"          → MEI-Exh-A-2
      MEI,   "Clause 17"            → MEI-GCS-17
      EPC,   "Article 18.4(e)"      → EPC-18-4-e
    """
    ref = raw_ref.strip()
    # Remove common prefixes
    for prefix in ["Sub-Clause ", "Sub-Clause", "Clause ", "Clause", "Article ", "Article"]:
        if ref.startswith(prefix):
            ref = ref[len(prefix):].strip()
            break
    # Handle SCS/GCS/COC prefixes already present
    for prefix in ["SCS ", "SCS", "GCS ", "GCS", "COC ", "COC", "Exhibit ", "Exhibit", "Attachment ", "Attachment"]:
        if ref.startswith(prefix):
            doc = prefix.strip()
            ref = ref[len(prefix):].strip()
            return f"{framework}-{doc}-{ref.replace(' ','-').replace('.','-').replace('(','').replace(')','')}"
    # Default: no explicit document prefix detected
    if framework == "CIVIL":
        doc = "COC"
    elif framework == "MEI":
        doc = "GCS"
    else:
        doc = "DOC"
    return f"{framework}-{doc}-{ref.replace(' ','-').replace('.','-').replace('(','').replace(')','')}"

def add_node(node_id, node_type, label, **data):
    """Add or update a node."""
    if node_id not in nodes:
        nodes[node_id] = {"type": node_type, "label": label, "data": data}
    else:
        nodes[node_id]["data"].update(data)

def add_edge(source, target, edge_type, **meta):
    """Add a directed edge."""
    edges.append({
        "source": source,
        "target": target,
        "type": edge_type,
        "metadata": meta
    })

# ============================================================
# SOURCE 1: Contract YAMLs → contract + commercial-value + clause nodes
# ============================================================
CONTRACTS_DIR = REF_DATA / "contracts"

def load_yaml(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

contract_files = sorted(CONTRACTS_DIR.glob("*.yaml"))
print(f"[1/6] Reading {len(contract_files)} contract YAMLs...")

FRAMEWORK_MAP = {
    "10.1": "CIVIL", "10.2": "CIVIL",
    "12.1": "MEI",   "12.2": "MEI",
    "99": "MEI"
}

for cf in contract_files:
    c = load_yaml(cf)
    cx = c.get("contract", {})
    cid = cx.get("id", cf.stem)

    # Contract node
    framework = FRAMEWORK_MAP.get(cid, "UNKNOWN")
    add_node(cid, "contract", cx.get("name", cid),
             vendor=cx.get("vendor"), discipline=cx.get("discipline"),
             package=cx.get("package"), ref=cx.get("contract_ref"),
             framework=framework, parent=cx.get("parent_contract"),
             value=cx.get("commercial", {}).get("contract_value"))

    # Financial value nodes
    comm = cx.get("commercial", {})
    ld = cx.get("liquidated_damages", {})
    pay = cx.get("payment_terms", {})

    if comm.get("contract_value"):
        val_id = f"VALUE-{cid}"
        add_node(val_id, "commercial_value", f"{cid} Contract Value",
                 amount=comm["contract_value"], currency=comm.get("currency", "AED"),
                 category="contract_value")
        add_edge(cid, val_id, "has_value", unit=comm.get("currency"))

    if ld.get("delay") and ld["delay"].get("per_day"):
        ld_id = f"LD-DELAY-{cid}"
        add_node(ld_id, "commercial_value", f"{cid} Delay LD",
                 per_day=ld["delay"]["per_day"],
                 cap_pct=ld["delay"].get("cap_pct"),
                 cap_amount=ld["delay"].get("cap_amount"),
                 currency=comm.get("currency", "AED"),
                 category="liquidated_damages")
        add_edge(cid, ld_id, "has_value", unit=comm.get("currency","AED"))

    if ld.get("key_personnel") and ld["key_personnel"].get("per_day"):
        kp_id = f"LD-KP-{cid}"
        add_node(kp_id, "commercial_value", f"{cid} KP LD",
                 per_day=ld["key_personnel"]["per_day"],
                 count=ld["key_personnel"].get("count", 0),
                 currency=comm.get("currency", "AED"),
                 category="key_personnel_ld")
        add_edge(cid, kp_id, "has_value")

    if comm.get("advance_payment_pct"):
        adv_id = f"ADVANCE-{cid}"
        add_node(adv_id, "commercial_value", f"{cid} Advance Payment",
                 pct=comm["advance_payment_pct"],
                 currency=comm.get("currency", "AED"),
                 category="advance_payment")
        add_edge(cid, adv_id, "has_value")

    if comm.get("retention_pct"):
        ret_id = f"RETENTION-{cid}"
        add_node(ret_id, "commercial_value", f"{cid} Retention",
                 pct=comm["retention_pct"],
                 currency=comm.get("currency", "AED"),
                 category="retention")
        add_edge(cid, ret_id, "has_value")

    if comm.get("performance_bond_pct"):
        pb_id = f"PB-{cid}"
        add_node(pb_id, "commercial_value", f"{cid} Performance Bond",
                 pct=comm["performance_bond_pct"],
                 currency=comm.get("currency", "AED"),
                 category="performance_bond")
        add_edge(cid, pb_id, "has_value")

    # Exhibit nodes
    exhibits = cx.get("structure", {}).get("exhibits", [])
    for exh in exhibits:
        eref = exh.get("exhibit_ref", "").replace(" ", "-").replace(".", "")
        if not eref:
            continue
        exh_id = f"{cid}-EXH-{eref}"
        add_node(exh_id, "exhibit", f"{cid} {exh.get('exhibit_ref')}",
                 title=exh.get("title", ""),
                 relevance=exh.get("commercial_relevance", {}).get("level", ""),
                 topics=exh.get("primary_topics", []))
        add_edge(cid, exh_id, "has_exhibit")

    # Clause nodes from linked.clauses
    for cl in cx.get("linked", {}).get("clauses", []):
        cref = cl.get("clause_ref", "")
        if not cref:
            continue
        # Normalize clause ID
        cl_id = normalize_clause_id(framework, cref)
        add_node(cl_id, "clause", cref,
                 topic=cl.get("topic", ""),
                 library_link=cl.get("ko", ""),
                 contract=cid, framework=framework)
        add_edge(cid, cl_id, "has_clause", topic=cl.get("topic"))

    # Issues
    for iss in cx.get("issues", []):
        iss_title = iss.get("title", "")
        if not iss_title:
            continue
        iss_id = f"ISSUE-{iss_title[:40].replace(' ','-')}"
        add_node(iss_id, "issue", iss_title,
                 status=iss.get("status", "open"),
                 cost_impact=iss.get("cost_impact", ""),
                 deadline=iss.get("deadline", ""))
        add_edge(cid, iss_id, "has_issue")

print(f"  → {len(nodes)} nodes, {len(edges)} edges so far")

# ============================================================
# SOURCE 2: Correspondence YAMLs → letter + clause-reference edges
# ============================================================
CORR_DIR = REF_DATA / "correspondence"
corr_files = sorted(CORR_DIR.glob("*.yaml"))
print(f"[2/6] Reading {len(corr_files)} correspondence YAMLs...")

for cf in corr_files:
    if cf.stem == "index":
        continue
    data = load_yaml(cf)
    corr = data.get("correspondence", {})
    corr_id = corr.get("id", cf.stem)
    add_node(corr_id, "correspondence", corr.get("subject", corr_id),
             date=str(corr.get("date", "")), direction=corr.get("direction", ""),
             contract=corr.get("related", {}).get("contract", ""))

    # Link to clauses referenced
    for cl in corr.get("related", {}).get("clauses", []):
        cref = cl.get("clause_ref", "")
        if not cref:
            continue
        parent_c = corr.get("related", {}).get("contract", "")
        fw = FRAMEWORK_MAP.get(parent_c, "UNKNOWN")
        cl_id = normalize_clause_id(fw, cref)
        add_node(cl_id, "clause", cref,
                 topic=cl.get("topic",""), contract=parent_c, framework=fw)
        add_edge(corr_id, cl_id, "references", topic=cl.get("topic"))
        add_edge(parent_c, cl_id, "has_clause", topic=cl.get("topic"))

    # Link to contracts
    rel_contract = corr.get("related", {}).get("contract", "")
    if rel_contract:
        add_edge(corr_id, rel_contract, "relates_to")

    # Link to entities
    for ent in corr.get("related", {}).get("entities", {}).get("companies", []):
        add_edge(corr_id, ent, "involves")

print(f"  → {len(nodes)} nodes, {len(edges)} edges so far")

# ============================================================
# SOURCE 3: Clause Library → cross-contract clause mappings
# ============================================================
CL_DIR = REF_DATA / "clause-library"
cl_files = sorted(CL_DIR.glob("*.md"))
print(f"[3/6] Reading {len(cl_files)} clause-library files...")

for clf in cl_files:
    ko_id = f"KO-{clf.stem}"
    with open(clf, "r", encoding="utf-8") as f:
        text = f.read()
    # Extract contract references table
    ref_section = re.search(r'## Contract References(.*?)(?=## |\Z)', text, re.DOTALL)
    if ref_section:
        # Parse the markdown table for contract→clause mappings
        rows = re.findall(r'\|\s*([\w.-]+)\s*\|\s*([\w\s.-]+)\s*\|', ref_section.group(1))
        for contract_id, clause_ref in rows:
            if contract_id.strip() == '---' or 'Contract' in contract_id:
                continue
            fw = FRAMEWORK_MAP.get(contract_id.strip(), "UNKNOWN")
            cl_id = normalize_clause_id(fw, clause_ref.strip())
            add_node(cl_id, "clause", clause_ref.strip(),
                     contract=contract_id.strip(), framework=fw,
                     library=ko_id)
            add_edge(contract_id.strip(), cl_id, "has_clause", library=ko_id)

    add_node(ko_id, "clause_library", clf.stem.replace("-", " ").replace("_", " "))

print(f"  → {len(nodes)} nodes, {len(edges)} edges so far")

# ============================================================
# SOURCE 4: Back-to-Back Matrix → flows_down edges
# ============================================================
BTB = REF_DATA / "commercial-analysis" / "back-to-back-matrix.md"
print(f"[4/6] Processing back-to-back matrix...")

if BTB.exists():
    with open(BTB, "r", encoding="utf-8") as f:
        btb_text = f.read()

    # EPC Delay LD flows down to subcon Delay LD clauses
    # Known mappings from the matrix:
    flows = [
        ("EPC-18.4(e)", "CIVIL-COC-10-7", "Delay LD", {"confidence": "high"}),
        ("EPC-18.4(e)", "MEI-GCS-17", "Delay LD", {"confidence": "high"}),
        ("EPC-LD-KP", "CIVIL-COC-4-2-4", "KP LD", {"confidence": "high"}),
        ("EPC-LD-KP", "MEI-GCS-8", "KP LD", {"confidence": "medium"}),
    ]
    for src, tgt, topic, meta in flows:
        add_node(src, "clause", f"EPC {topic}", framework="EPC")
        add_node(tgt, "clause", tgt, framework=tgt.split("-")[0])
        add_edge(src, tgt, "flows_down", topic=topic, **meta)

print(f"  → {len(nodes)} nodes, {len(edges)} edges so far")

# ============================================================
# SOURCE 5: Amdt 01 .docx → amended_by / affects edges
# ============================================================
AMDT_PATH = BASE / "Subcon_Payments" / "12.1 CCECC - MEI Pkg I" / "Contract" / "02_Amdt 01" / "Amdt 01_MEI Pkg I (Revised) .docx"
print(f"[5/6] Processing Amdt 01 .docx...")

add_node("AMDT-12.1-01", "amendment", "Amdt 01 — Tripartite Fabricator Framework",
         date="2026-07", contract="12.1", framework="MEI")
add_edge("AMDT-12.1-01", "12.1", "amends")

if AMDT_PATH.exists():
    try:
        from docx import Document
        doc = Document(str(AMDT_PATH))
        amdt_clauses = set()
        for p in doc.paragraphs:
            t = p.text.strip()
            # Match clause references to MEI framework
            # e.g., "Clause 3.2", "Clause 4.3", "Clause 6.1", "Clause 8"
            for m in re.finditer(r'(?:Clause|第)\s*(\d+[\.\d]*)', t):
                clause_num = m.group(1)
                cl_id = f"MEI-GCS-{clause_num.replace('.','-')}"
                amdt_clauses.add(cl_id)
            # Also match Exhibit references
            for m in re.finditer(r'Exhibit\s+([A-K])', t):
                exh_letter = m.group(1)
                exh_id = f"12.1-EXH-Exh{m.group(1)}"
                add_node(exh_id, "exhibit", f"12.1 Exhibit {exh_letter}",
                         contract="12.1")
                add_edge("AMDT-12.1-01", exh_id, "affects", clause=f"Exh {exh_letter}")

        for cl_id in amdt_clauses:
            add_node(cl_id, "clause", cl_id, framework="MEI", contract="12.1")
            add_edge("12.1", cl_id, "has_clause")
            add_edge("AMDT-12.1-01", cl_id, "affects", amended=True)

        print(f"  → Amdt affects {len(amdt_clauses)} clauses + {len([e for e in edges if e['source']=='AMDT-12.1-01' and 'Exh' in e.get('target','')])} exhibits")
    except Exception as e:
        print(f"  → WARNING: Could not parse Amdt .docx: {e}")
else:
    print(f"  → WARNING: Amdt 01 .docx not found at {AMDT_PATH}")

# ============================================================
# SOURCE 6: Risk Register → exposes_to edges
# ============================================================
RISK = REF_DATA / "commercial-analysis" / "risk-register.md"
print(f"[6/6] Processing risk register...")

if RISK.exists():
    with open(RISK, "r", encoding="utf-8") as f:
        risk_text = f.read()
    # Extract risk items
    for m in re.finditer(r'\|\s*R\d+\s*\|\s*\*\*(.+?)\*\*\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|', risk_text):
        risk_name = m.group(1).strip()
        severity = m.group(2).strip()
        contract_ids = m.group(3).strip()
        risk_id = f"RISK-{risk_name[:50].replace(' ','-')}"
        add_node(risk_id, "risk", risk_name, severity=severity, contracts=contract_ids)
        for cid in contract_ids.split(","):
            cid = cid.strip()
            if cid in FRAMEWORK_MAP or cid == "All":
                add_edge(cid, risk_id, "exposes_to", severity=severity)

print(f"  → {len(nodes)} nodes, {len(edges)} edges so far")

# ============================================================
# ALSO: Add framework nodes
# ============================================================
add_node("FRAMEWORK-MEI", "framework", "MEI Framework (GCS 1.0-50.0 + SCS 1-7 + Agrmt 1-13)")
add_node("FRAMEWORK-CIVIL", "framework", "Civil Framework (COC 29 sections + FOA 1-3)")
for nid, ndata in nodes.items():
    cid = ndata.get("data", {}).get("contract", "")
    fw = ndata.get("data", {}).get("framework", "")
    if cid and fw:
        add_edge(cid, f"FRAMEWORK-{fw}", "uses_framework")

# ============================================================
# WRITE OUTPUT
# ============================================================
nodes_out = {nid: {"type": nd["type"], "label": nd["label"], **nd["data"]}
             for nid, nd in sorted(nodes.items())}

# Deduplicate edges
seen = set()
edges_dedup = []
for e in edges:
    key = (e["source"], e["target"], e["type"])
    if key not in seen:
        seen.add(key)
        edges_dedup.append(e)

out_n = OUT_DIR / "nodes.yaml"
out_e = OUT_DIR / "edges.yaml"
out_j = OUT_DIR / "graph.json"

with open(out_n, "w", encoding="utf-8") as f:
    yaml.dump(nodes_out, f, allow_unicode=True, default_flow_style=False, sort_keys=True)

with open(out_e, "w", encoding="utf-8") as f:
    yaml.dump(edges_dedup, f, allow_unicode=True, default_flow_style=False)

with open(out_j, "w", encoding="utf-8") as f:
    json.dump({"nodes": {nid: nd for nid, nd in nodes_out.items()},
               "edges": edges_dedup}, f, ensure_ascii=False, indent=2)

# Stats
types = {}
for nd in nodes.values():
    t = nd["type"]
    types[t] = types.get(t, 0) + 1
edge_types = {}
for e in edges_dedup:
    t = e["type"]
    edge_types[t] = edge_types.get(t, 0) + 1

print(f"\n{'='*50}")
print(f"GRAPH COMPILED: {len(nodes)} nodes, {len(edges_dedup)} edges (deduped from {len(edges)})")
print(f"\nNodes by type:")
for t, c in sorted(types.items()):
    print(f"  {t:20s}: {c:4d}")
print(f"\nEdges by type:")
for t, c in sorted(edge_types.items()):
    print(f"  {t:20s}: {c:4d}")
print(f"\nOutput:")
print(f"  {out_n}")
print(f"  {out_e}")
print(f"  {out_j}")
