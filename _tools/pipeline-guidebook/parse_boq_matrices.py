#!/usr/bin/env python3
"""
BOQ Matrix Pre-Processor — ADNOC Gas Sulfur Pipeline
=====================================================
Parses 6 raw BOQ Excel files, extracts structured material quantities,
and outputs an aggregated JSON dataset consumed by the BOQ Refined Guide.

Commercial Architecture:
  Civil Sub A (TCC)  — Pkg I + Pkg III  (2 sub-packages)
  Civil Sub B (CCECC) — Pkg II           (1 sub-package)
  MEI Sub C (CCECC)   — Pkg I-1 + I-3    (2 sub-packages)
  MEI Sub D (TCC)     — Pkg II           (1 sub-package)
"""

from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from pathlib import Path

import openpyxl

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
RAW_DIR = Path(__file__).resolve().parent / "raw_boqs"
OUT_JSON = Path(__file__).resolve().parent / "boq_extracted_data.json"

# ---------------------------------------------------------------------------
# Subcontractor file mapping  (source → (sub_label, pkg_label))
# ---------------------------------------------------------------------------
FILE_MAP = {
    "civil_sub_a_pkg1.xlsx":  ("Civil Sub A", "Pkg I"),
    "civil_sub_a_pkg3.xlsx":  ("Civil Sub A", "Pkg III"),
    "civil_sub_b_pkg2.xlsx":  ("Civil Sub B", "Pkg II"),
    "mei_sub_c_pkg1.xlsx":    ("MEI Sub C",   "Pkg I-3"),
    "mei_sub_c_pkg2.xlsx":    ("MEI Sub C",   "Pkg I-1"),
    "mei_sub_d_pkg1.xlsx":    ("MEI Sub D",   "Pkg II"),
}

# ---------------------------------------------------------------------------
# Unit / Zone column-name patterns (case-insensitive + whitespace-normalised)
# ---------------------------------------------------------------------------
UNIT_KEYWORDS = {
    "Unit 10":    ["unit 10",    "unit10",  "u10"],
    "Unit 10A":   ["unit 10a",   "unit10a", "u10a"],
    "Unit 20":    ["unit 20",    "unit20",  "u20"],
    "Unit 30":    ["unit 30",    "unit30",  "u30"],
    "Unit 40":    ["unit 40",    "unit40",  "u40"],
    "Unit 50":    ["unit 50",    "unit50",  "u50"],
    "Zone 210":   ["zone 210",   "zone210", "210"],
    "Zone 220":   ["zone 220",   "zone220", "220"],
    "Zone 230":   ["zone 230",   "zone230", "230"],
}


def _clean(text: str) -> str:
    """Normalise a cell value to a compact lowercase string."""
    return re.sub(r"\s+", " ", str(text).strip()).lower()


def _is_numeric(v) -> bool:
    """Return True if v is a number (int or float)."""
    if v is None:
        return False
    if isinstance(v, (int, float)):
        return True
    if isinstance(v, str):
        try:
            float(v.replace(",", ""))
            return True
        except (ValueError, TypeError):
            return False
    return False


def _to_num(v):
    """Convert to float if numeric, else return 0."""
    if v is None:
        return 0.0
    if isinstance(v, (int, float)):
        return float(v)
    if isinstance(v, str):
        try:
            return float(v.replace(",", "").strip())
        except (ValueError, TypeError):
            return 0.0
    return 0.0


def _match_unit(col_clean: str) -> str | None:
    """Return the canonical unit name if col_clean matches a known unit."""
    for canon, aliases in UNIT_KEYWORDS.items():
        for alias in aliases:
            if alias in col_clean:
                return canon
    return None


# ---------------------------------------------------------------------------
# Category classifiers
# ---------------------------------------------------------------------------
CONCRETE_KW = [
    "concrete", "conc", "blinding", "lean con", "grout", "grouting",
    "screed", "waterstop", "formwork", "rebar", "reinforcement",
    "reinforcing", "re-bar", "mesh", "precast", "pre-cast",
    "pile cap", "pilecap", "pile capping", "tie beam", "grade beam",
    "raft", "footing", "pedestal", "column", "slab", "wall",
    "retaining wall", "ring beam", "ring-beam", "base slab",
    "pile cut", "anchor bolt", "embed", "embedded",
    "blast", "blast-resistant", "blast resistant",
]
EXCAVATION_KW = [
    "excavation", "excav", "backfill", "fill", "compaction",
    "dewatering", "shoring", "sheet pile", "trench",
]
STEEL_KW = [
    "structural steel", "steel structure", "steel beam", "steel column",
    "steel frame", "steel truss", "space frame", "space truss",
    "space-frame", "space-truss", "roof structure", "canopy",
    "handrail", "grating", "chequered plate", "checkered plate",
    "ladder", "stair", "platform", "monorail", "insert plate",
]
PIPING_KW = [
    "piping", "pipe", "tube", "fitting", "flange", "valve",
    "gasket", "bolt", "nut", "stud", "steam", "jacketed",
    "underground pipe", "ug pipe", "ug pip", "aboveground pipe",
    "ag pipe", "pipeline",
]
CABLE_KW = [
    "cable", "wire", "conduit", "tray", "trunking", "cable gland",
    "cable ladder", "bus duct", "busduct", "busway", "power cable",
    "control cable", "instrument cable", "fiber optic", "fibre optic",
    "hv cable", "mv cable", "lv cable", "cable pulling",
    "earthing", "grounding", "lightning", "surge",
]
INSTRUMENT_KW = [
    "instrument", "transmitter", "sensor", "gauge", "meter",
    "switch", "controller", "indicator", "recorder", "analyser",
    "analyzer", "transducer", "thermowell", "orifice", "flow",
    "level", "pressure", "temperature", "temp", "rtd", "thermocouple",
    "control valve", "actuator", "positioner", "solenoid",
    "junction box", "jb", "loop", "i/o", "cabinet", "panel",
    "dcs", "plc", "scada", "esd", "fg", "fire & gas",
    "fire and gas", "telecom", "telecommunication", "cctv",
    "pa/ga", "paga", "access control", "lan", "wan", "network",
    "hvac", "duct", "diffuser", "damper", "chiller", "ahu",
    "fan", "exhaust", "ventilation", "air conditioning",
]


def classify_item(description: str) -> str:
    """Return a high-level category for a BOQ line item."""
    d = _clean(description)
    # Order matters — check concrete first (most specific)
    if any(kw in d for kw in CONCRETE_KW):
        return "Concrete & Civils"
    if any(kw in d for kw in STEEL_KW):
        return "Structural Steel"
    if any(kw in d for kw in PIPING_KW):
        return "Piping"
    if any(kw in d for kw in CABLE_KW):
        return "Electrical (Cable/Containment)"
    if any(kw in d for kw in INSTRUMENT_KW):
        return "Instrumentation & Controls"
    if any(kw in d for kw in EXCAVATION_KW):
        return "Earthworks & Excavation"
    return "Other"


# ---------------------------------------------------------------------------
# Core parser
# ---------------------------------------------------------------------------
def parse_workbook(filepath: str, sub_label: str, pkg_label: str) -> dict:
    """Parse one BOQ Excel file and return structured extraction."""
    wb = openpyxl.load_workbook(filepath, data_only=True)
    result = {
        "file": Path(filepath).name,
        "subcontractor": sub_label,
        "package": pkg_label,
        "sheets_parsed": [],
        "summary_total": 0.0,
        "categories": defaultdict(lambda: {"total_qty": 0.0, "units": defaultdict(float), "items": []}),
        "by_unit": defaultdict(lambda: {"Concrete & Civils": 0.0, "Structural Steel": 0.0,
                                          "Piping": 0.0, "Electrical (Cable/Containment)": 0.0,
                                          "Instrumentation & Controls": 0.0,
                                          "Earthworks & Excavation": 0.0, "Other": 0.0}),
        "detailed": [],  # per-item structured rows
    }

    # ── A-Summary: extract total price ──
    if "A-Summary" in wb.sheetnames:
        ws = wb["A-Summary"]
        for row in ws.iter_rows(min_row=1, max_row=ws.max_row, values_only=True):
            row_text = " ".join([str(c) for c in row if c is not None])
            if "TOTA" in row_text.upper() and "SUBCONTRACT" in row_text.upper():
                # Pick last numeric in row
                nums = [_to_num(c) for c in row if _is_numeric(c)]
                if nums:
                    result["summary_total"] = max(nums)
                break

    # ── Process all data sheets ──
    data_sheets = [
        s for s in wb.sheetnames
        if s not in ("COVER", "A-Summary", "A.1-INDIRECTS BREAKDOWN",
                      "Labor Rates", "Equipment Rates", "Provisional Sum")
    ]

    for sn in data_sheets:
        ws = wb[sn]
        if ws.max_row < 10:
            continue

        # Build column map: find header rows (usually R7-R9)
        col_map = {}          # col_idx → unit_name
        wbs_start_col = None  # first WBS quantity column
        header_rows_data = []

        for r in range(1, min(12, ws.max_row + 1)):
            row_vals = []
            for c in range(1, ws.max_column + 1):
                v = ws.cell(row=r, column=c).value
                row_vals.append(v)
            header_rows_data.append(row_vals)

        # Identify the item-description columns (standard: C1=Item, C2=Category, C3=Description, C4=Unit, C5=Qty)
        # WBS starts from C6 or C7 depending on sheet
        # Scan rows 7-10 for unit/zone name patterns
        for row_vals in header_rows_data:
            for c_idx, val in enumerate(row_vals):
                if val is None:
                    continue
                cv = _clean(str(val))
                matched = _match_unit(cv)
                if matched:
                    col_map[c_idx] = matched
                    if wbs_start_col is None or c_idx < wbs_start_col:
                        wbs_start_col = c_idx

        if wbs_start_col is None:
            wbs_start_col = 6  # default: C6+ is WBS

        # Also check rows with merged unit references like "UNIT 10 General"
        for row_vals in header_rows_data:
            line = " ".join([str(v) for v in row_vals if v is not None])
            for canon in UNIT_KEYWORDS:
                if canon.upper() in line.upper():
                    # find which column has this
                    for c_idx, val in enumerate(row_vals):
                        if val and canon.upper() in str(val).upper():
                            col_map[c_idx] = canon

        result["sheets_parsed"].append(sn)

        # ── Parse data rows (R10+) ──
        for r in range(10, ws.max_row + 1):
            item_no = ws.cell(row=r, column=1).value
            category = ws.cell(row=r, column=2).value
            description = ws.cell(row=r, column=3).value
            unit = ws.cell(row=r, column=4).value
            total_qty = ws.cell(row=r, column=5).value

            if description is None or str(description).strip() == "":
                continue
            if not _is_numeric(total_qty) and total_qty not in (None, "Q", "q", ""):
                continue
            if str(description).strip().lower() in ("no.", "item", "description", ""):
                continue

            desc_str = str(description).strip()
            unit_str = str(unit).strip() if unit else ""
            qty_val = _to_num(total_qty) if _is_numeric(total_qty) else 0.0
            cat = classify_item(desc_str)

            # Collect per-unit quantities from WBS columns
            unit_qties = {}
            for c_idx in range(wbs_start_col, ws.max_column + 1):
                v = ws.cell(row=r, column=c_idx).value
                if _is_numeric(v):
                    mapped_unit = col_map.get(c_idx)
                    if mapped_unit:
                        unit_qties[mapped_unit] = _to_num(v)
                    else:
                        # Try reading column header directly
                        for hr in header_rows_data:
                            if len(hr) > c_idx and hr[c_idx] is not None:
                                mu = _match_unit(_clean(str(hr[c_idx])))
                                if mu:
                                    unit_qties[mu] = _to_num(v)
                                    col_map[c_idx] = mu
                                    break

            # Aggregate
            result["categories"][cat]["total_qty"] += qty_val
            for u, uq in unit_qties.items():
                result["by_unit"][u][cat] += uq

            # Detailed item
            if cat != "Other" or qty_val > 0:
                result["detailed"].append({
                    "sheet": sn,
                    "row": r,
                    "item": str(item_no)[:20] if item_no else "",
                    "category": category,
                    "description": desc_str[:120],
                    "unit": unit_str,
                    "total_qty": qty_val,
                    "class": cat,
                    "unit_breakdown": {u: round(v, 3) for u, v in unit_qties.items() if v > 0},
                })

    wb.close()

    # Convert defaultdicts
    result["categories"] = dict(result["categories"])
    result["by_unit"] = dict(result["by_unit"])
    return result


# ---------------------------------------------------------------------------
# Aggregation across all files
# ---------------------------------------------------------------------------
def aggregate(all_results: list[dict]) -> dict:
    """Merge per-file results into cross-subcontractor summaries."""
    agg = {
        "subcontractors": defaultdict(lambda: {
            "packages": [],
            "total_value": 0.0,
            "categories": defaultdict(float),
            "by_unit": defaultdict(lambda: defaultdict(float)),
        }),
        "global": {
            "total_concrete_m3": 0.0,
            "total_steel_ton": 0.0,
            "total_piping_m": 0.0,
            "total_cable_m": 0.0,
            "total_instrument_loops": 0.0,
            "by_unit": defaultdict(lambda: defaultdict(float)),
            "by_category": defaultdict(float),
        },
        "all_items": [],
    }

    for r in all_results:
        sub = r["subcontractor"]
        agg["subcontractors"][sub]["packages"].append(r["package"])
        agg["subcontractors"][sub]["total_value"] += r["summary_total"]

        for cat, data in r["categories"].items():
            agg["subcontractors"][sub]["categories"][cat] += data["total_qty"]
            agg["global"]["by_category"][cat] += data["total_qty"]

        for unit, cats in r["by_unit"].items():
            for cat, qty in cats.items():
                agg["subcontractors"][sub]["by_unit"][unit][cat] += qty
                agg["global"]["by_unit"][unit][cat] += qty

        agg["all_items"].extend(r["detailed"])

    # Estimate key metrics
    for item in agg["all_items"]:
        d = _clean(item["description"])
        u = _clean(item["unit"])
        q = item["total_qty"]
        # Concrete in M3
        if u in ("m3", "m³", "cu.m", "cum") and any(kw in d for kw in ("concrete", "conc", "blinding", "lean", "screed", "grout")):
            agg["global"]["total_concrete_m3"] += q
        # Steel in TON
        if u in ("ton", "t", "tonne", "mt") and ("steel" in d or "structural" in d):
            agg["global"]["total_steel_ton"] += q
        # Piping in M
        if u in ("m", "lm", "mtr", "meter") and any(kw in d for kw in ("pipe", "piping", "tube")):
            agg["global"]["total_piping_m"] += q
        # Cable in M
        if u in ("m", "lm", "mtr", "meter") and any(kw in d for kw in ("cable", "wire")):
            agg["global"]["total_cable_m"] += q
        # Instrument loops
        if u in ("ea", "each", "no", "nos", "loop") and any(kw in d for kw in ("transmitter", "instrument", "control valve", "switch", "gauge", "loop")):
            agg["global"]["total_instrument_loops"] += q

    # Convert defaultdicts
    agg["subcontractors"] = dict(agg["subcontractors"])
    agg["global"]["by_unit"] = dict(agg["global"]["by_unit"])
    agg["global"]["by_category"] = dict(agg["global"]["by_category"])

    return agg


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> None:
    print("=" * 68)
    print("  BOQ Matrix Pre-Processor — ADNOC Gas Sulfur Pipeline")
    print("=" * 68)
    print(f"\n  Input  : {RAW_DIR}")
    print(f"  Output : {OUT_JSON}\n")

    if not RAW_DIR.exists():
        print("  ❌ raw_boqs/ directory not found. Please stage the 6 Excel files.")
        sys.exit(1)

    all_results = []
    for fname, (sub, pkg) in FILE_MAP.items():
        fp = RAW_DIR / fname
        if not fp.exists():
            print(f"  ⚠   SKIP: {fname} not found — continuing")
            continue
        print(f"  📄  Parsing {fname} …")
        try:
            res = parse_workbook(str(fp), sub, pkg)
            cats = res["categories"]
            units = res["by_unit"]
            print(f"      Sub: {sub} | Pkg: {pkg}")
            print(f"      Summary Value: AED {res['summary_total']:,.0f}")
            cat_strs = []
            for k, v in sorted(cats.items()):
                if v["total_qty"] > 0:
                    cat_strs.append('{} ({:.0f})'.format(k, v["total_qty"]))
            print("      Categories: " + ", ".join(cat_strs))
            print("      Units mapped: " + ", ".join(sorted(units.keys())))
            print("      Detail items: " + str(len(res["detailed"])))
            all_results.append(res)
        except Exception as exc:
            print("      ERROR: " + str(exc))
        print()

    if not all_results:
        print("  ❌ No files parsed. Aborting.")
        sys.exit(1)

    # Aggregate
    print("  🔄  Aggregating cross-subcontractor data …")
    agg = aggregate(all_results)

    # Print summary
    print(f"\n  ── Subcontractor Summary ──")
    for sub, data in agg["subcontractors"].items():
        pkgs = ", ".join(data["packages"])
        print(f"  {sub}: {pkgs} → AED {data['total_value']:,.0f}")
        for cat, qty in sorted(data["categories"].items()):
            if qty > 0:
                print(f"    {cat}: {qty:,.0f}")

    print(f"\n  ── Global Totals ──")
    g = agg["global"]
    print(f"  Concrete (est. M³):      {g['total_concrete_m3']:,.0f}")
    print(f"  Structural Steel (est.T): {g['total_steel_ton']:,.0f}")
    print(f"  Piping (est.M):           {g['total_piping_m']:,.0f}")
    print(f"  Cable (est.M):            {g['total_cable_m']:,.0f}")
    print(f"  Instrument Items (est.):  {g['total_instrument_loops']:,.0f}")

    # Per-unit totals
    print(f"\n  ── Per-Unit Category Totals ──")
    for unit in sorted(g["by_unit"].keys()):
        cats = g["by_unit"][unit]
        summary = " + ".join(f"{cat}: {qty:,.1f}" for cat, qty in sorted(cats.items()) if qty > 0)
        print(f"  {unit}: {summary}")

    # Write JSON
    OUT_JSON.write_text(json.dumps(agg, indent=2, ensure_ascii=False, default=str), encoding="utf-8")
    print(f"\n  ✅  Aggregated data written to {OUT_JSON}")
    print(f"      ({OUT_JSON.stat().st_size / 1024:.1f} KB, {len(agg['all_items'])} items)")
    print(f"\n{'=' * 68}")
    print("  Pre-processing complete. Ready for BOQ Refined Guide generation.")
    print("=" * 68)


if __name__ == "__main__":
    main()
