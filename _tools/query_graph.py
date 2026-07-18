#!/usr/bin/env python3
"""
query_graph.py — Wison Knowledge Graph Query Tool

Usage:
  python query_graph.py --stats
  python query_graph.py --node <node_id> [--depth 2]
  python query_graph.py --from <src> --to <tgt>
  python query_graph.py --impact <node_id>
  python query_graph.py --compare LD|KP|Payment [--contracts 10.1,12.1]
  python query_graph.py --report clause-history --clause <clause_ref>
  python query_graph.py --type clause|contract|exhibit|risk|correspondence|commercial_value
  python query_graph.py --search <keyword>
  python query_graph.py --list-types
"""
import sys, json, argparse
from pathlib import Path
from collections import defaultdict, deque

try:
    import yaml
except ImportError:
    print("ERROR: pyyaml required.")
    sys.exit(1)

GRAPH_DIR = Path(r"D:\Wison\_Ref\data\graph")

def load_graph():
    with open(GRAPH_DIR / "nodes.yaml", "r", encoding="utf-8") as f:
        nodes = yaml.safe_load(f) or {}
    with open(GRAPH_DIR / "edges.yaml", "r", encoding="utf-8") as f:
        edges = yaml.safe_load(f) or []
    # Build adjacency
    outgoing = defaultdict(list)
    incoming = defaultdict(list)
    for e in edges:
        outgoing[e["source"]].append(e)
        incoming[e["target"]].append(e)
    return nodes, edges, outgoing, incoming

def print_node(nid, ndata, indent=0):
    prefix = "  " * indent
    t = ndata.get("type", "?")
    label = ndata.get("label", nid)
    print(f"{prefix}[{t}] {label}")
    # Print key data fields
    for k, v in ndata.items():
        if k in ("type", "label"):
            continue
        if v and k not in ("topics",):
            print(f"{prefix}  {k}: {v}")

def print_edge(e, indent=0):
    prefix = "  " * indent
    print(f"{prefix}--[{e['type']}]--> {e['target']}")

def cmd_stats(nodes, edges):
    print(f"Nodes: {len(nodes)}")
    print(f"Edges: {len(edges)}")
    types = defaultdict(int)
    for nd in nodes.values():
        types[nd.get("type","?")] += 1
    print("\nBy type:")
    for t, c in sorted(types.items()):
        print(f"  {t:20s}: {c:4d}")
    etypes = defaultdict(int)
    for e in edges:
        etypes[e["type"]] += 1
    print("\nEdge types:")
    for t, c in sorted(etypes.items()):
        print(f"  {t:20s}: {c:4d}")

def cmd_node(nid, nodes, outgoing, incoming, depth):
    if nid not in nodes:
        print(f"Node '{nid}' not found. Try --search or --list-types.")
        # Fuzzy search
        matches = [(k, v.get("label","")) for k, v in nodes.items()
                   if nid.lower() in k.lower() or nid.lower() in v.get("label","").lower()]
        if matches:
            print(f"\nDid you mean?")
            for k, label in matches[:10]:
                print(f"  {k}: {label}")
        return

    print(f"\n{'='*60}")
    print_node(nid, nodes[nid])
    print(f"\n--- OUTGOING ({len(outgoing.get(nid,[]))}) ---")
    for e in outgoing.get(nid, []):
        tgt = e["target"]
        print_edge(e)
        if depth > 1 and tgt in nodes:
            print_node(tgt, nodes[tgt], indent=1)
    print(f"\n--- INCOMING ({len(incoming.get(nid,[]))}) ---")
    for e in incoming.get(nid, []):
        print_edge(e)

def cmd_path(src, tgt, nodes, outgoing):
    """BFS shortest path."""
    visited = {src: None}
    q = deque([src])
    while q:
        cur = q.popleft()
        if cur == tgt:
            # Reconstruct
            path = []
            while cur is not None:
                path.append(cur)
                cur = visited[cur]
            path.reverse()
            print(f"\nPath ({len(path)-1} hops):")
            for i, nid in enumerate(path):
                print_node(nid, nodes[nid], indent=i)
                if i < len(path) - 1:
                    # Find edge
                    for e in outgoing.get(nid, []):
                        if e["target"] == path[i+1]:
                            print_edge(e, indent=i+1)
                            break
            return
        for e in outgoing.get(cur, []):
            nxt = e["target"]
            if nxt not in visited:
                visited[nxt] = cur
                q.append(nxt)
    print(f"No path found from '{src}' to '{tgt}'.")

def cmd_impact(nid, nodes, outgoing):
    """All downstream effects (BFS)."""
    if nid not in nodes:
        print(f"Node '{nid}' not found.")
        return
    visited = set()
    q = deque([(nid, 0)])
    print(f"\nImpact analysis for: {nodes[nid].get('label', nid)}")
    print(f"{'Hops':5s} {'Type':20s} {'ID'}")
    print("-"*60)
    while q:
        cur, depth = q.popleft()
        visited.add(cur)
        for e in outgoing.get(cur, []):
            tgt = e["target"]
            if tgt not in visited:
                visited.add(tgt)
                q.append((tgt, depth+1))
                print(f"{depth+1:<5d} {nodes[tgt].get('type','?'):20s} {tgt}")
                visited.add(tgt)
    print(f"\nTotal downstream nodes: {len(visited)-1}")

def cmd_compare(topic, contract_ids, nodes, outgoing):
    """Compare clause values across contracts."""
    topic_map = {"LD": "liquidated_damages", "KP": "key_personnel", "Payment": "payment"}
    key = topic_map.get(topic, topic.lower())
    print(f"\n=== {topic} Comparison ===")
    print(f"{'Contract':12s} {'Node ID':30s} {'Key Values'}")
    print("-"*80)
    for nid, nd in sorted(nodes.items()):
        if nd.get("type") != "commercial_value":
            continue
        cat = nd.get("category", "")
        if key.lower() in cat.lower() or topic.lower() in cat.lower():
            contract = nid.split("-")[1] if "-" in nid else "?"
            if contract_ids and contract not in contract_ids:
                continue
            vals = ", ".join(f"{k}={v}" for k, v in nd.items()
                           if k not in ("type","label","category","currency") and v is not None)
            print(f"{contract:12s} {nid:30s} {vals[:120]}")

def cmd_report(report_type, clause_ref, nodes, outgoing, incoming):
    """Generate a structured report."""
    if report_type == "clause-history":
        # Find all nodes matching clause_ref
        matches = [(k, v) for k, v in nodes.items()
                   if clause_ref.lower() in k.lower() or clause_ref.lower() in v.get("label","").lower()]
        if not matches:
            print(f"No clause matching '{clause_ref}'.")
            return
        for nid, nd in matches:
            print(f"\n{'='*60}")
            print(f"Clause: {nd.get('label', nid)} ({nid})")
            print(f"  Type: {nd.get('type')} | Contract: {nd.get('contract','?')} | Framework: {nd.get('framework','?')}")
            # Incoming edges (what references this)
            inc = incoming.get(nid, [])
            if inc:
                print(f"\n  Referenced by ({len(inc)}):")
                for e in inc:
                    src = e["source"]
                    src_label = nodes.get(src, {}).get("label", src)
                    print(f"    ← [{e['type']}] {src_label} ({src})")
            # Outgoing edges
            out = outgoing.get(nid, [])
            if out:
                print(f"\n  Points to ({len(out)}):")
                for e in out:
                    tgt = e["target"]
                    tgt_label = nodes.get(tgt, {}).get("label", tgt)
                    print(f"    → [{e['type']}] {tgt_label} ({tgt})")
            # Find any amendments
            for e in inc:
                if e["type"] == "affects" and "AMDT" in e["source"]:
                    print(f"\n  ★ AMENDED BY: {e['source']}")

def cmd_search(keyword, nodes):
    kw = keyword.lower()
    matches = [(k, v) for k, v in nodes.items()
               if kw in k.lower() or kw in v.get("label","").lower()]
    if not matches:
        print(f"No nodes matching '{keyword}'.")
        return
    print(f"\n{len(matches)} matches for '{keyword}':")
    for k, v in sorted(matches):
        print(f"  [{v.get('type','?')}] {k}: {v.get('label','')}")

def cmd_type(ntype, nodes):
    matches = [(k, v) for k, v in nodes.items() if v.get("type") == ntype]
    if not matches:
        print(f"No nodes of type '{ntype}'.")
        return
    print(f"\n{len(matches)} nodes of type '{ntype}':")
    for k, v in sorted(matches):
        extra = ""
        if v.get("contract"): extra += f" | {v['contract']}"
        if v.get("framework"): extra += f" | {v['framework']}"
        if v.get("status"): extra += f" | status={v['status']}"
        if v.get("severity"): extra += f" | {v['severity']}"
        print(f"  {k:35s} {v.get('label','')}{extra}")

def cmd_list_types(nodes):
    types = defaultdict(int)
    for nd in nodes.values():
        types[nd.get("type","?")] += 1
    print("Available node types:")
    for t, c in sorted(types.items()):
        print(f"  {t:20s} ({c})")

# ============================================================
def main():
    parser = argparse.ArgumentParser(description="Wison Knowledge Graph Query Tool")
    parser.add_argument("--stats", action="store_true")
    parser.add_argument("--node", type=str)
    parser.add_argument("--depth", type=int, default=1)
    parser.add_argument("--from", dest="src", type=str)
    parser.add_argument("--to", dest="tgt", type=str)
    parser.add_argument("--impact", type=str)
    parser.add_argument("--compare", type=str, choices=["LD","KP","Payment","Retention","Bond","Warranty"])
    parser.add_argument("--contracts", type=str, help="Comma-separated: 10.1,12.1")
    parser.add_argument("--report", type=str, choices=["clause-history"])
    parser.add_argument("--clause", type=str, help="Clause reference for report")
    parser.add_argument("--type", dest="ntype", type=str)
    parser.add_argument("--search", type=str)
    parser.add_argument("--list-types", action="store_true")
    args = parser.parse_args()

    nodes, edges, outgoing, incoming = load_graph()

    if args.stats:
        cmd_stats(nodes, edges)
    elif args.node:
        cmd_node(args.node, nodes, outgoing, incoming, args.depth)
    elif args.src and args.tgt:
        cmd_path(args.src, args.tgt, nodes, outgoing)
    elif args.impact:
        cmd_impact(args.impact, nodes, outgoing)
    elif args.compare:
        contracts = args.contracts.split(",") if args.contracts else []
        cmd_compare(args.compare, contracts, nodes, outgoing)
    elif args.report:
        cmd_report(args.report, args.clause or "", nodes, outgoing, incoming)
    elif args.ntype:
        cmd_type(args.ntype, nodes)
    elif args.search:
        cmd_search(args.search, nodes)
    elif args.list_types:
        cmd_list_types(nodes)
    else:
        parser.print_help()
        print("\nQuick start:")
        print("  python query_graph.py --stats")
        print("  python query_graph.py --node 12.1 --depth 2")
        print("  python query_graph.py --impact AMDT-12.1-01")
        print("  python query_graph.py --compare LD")
        print("  python query_graph.py --report clause-history --clause GCS-17")
        print("  python query_graph.py --search 'Delay LD'")

if __name__ == "__main__":
    main()
