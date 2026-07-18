"""分包价格数据库查询工具
用法: python _query.py <keyword> [keyword2 ...]
示例: python _query.py "DUCT BANK"
      python _query.py "MANHOLE" "CONCRETE"
      python _query.py --list                   # 列出所有工作表
      python _query.py --cat MANHOLE            # 按 Category 精确搜
"""

import csv, json, os, sys, glob
from pathlib import Path

BASE = Path(__file__).parent

def load_manifest():
    with open(BASE / '_manifest.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def find_matching_rows(csv_path, keywords, search_cat=None):
    """Search CSV for rows where Description (or Category if --cat) contains any keyword."""
    results = []
    with open(csv_path, 'r', encoding='utf-8-sig') as f:
        reader = list(csv.reader(f))

    # Find header row (row with 'Description' or 'Item')
    for i, row in enumerate(reader):
        row_text = '|'.join(str(c).upper() for c in row)
        # Find the row containing column labels
        if any(h in row_text for h in ['MANHOURS', 'LABOR COST', 'DIRECT COST']):
            # This is header row; data starts after it
            # Also check row+1 for formula row (has '=Q*a')
            data_start = i + 1
            formula_row = reader[i+1] if i+1 < len(reader) else []
            formula_text = '|'.join(str(c) for c in formula_row)
            if '=Q*a' in formula_text or '=Q' in formula_text:
                data_start = i + 2  # skip formula row too
            break
    else:
        # No pricing header found, search all rows
        data_start = 0

    for row in reader[data_start:]:
        row_text = '|'.join(str(c).upper() for c in row)
        if search_cat:
            # Category is column 2 (index 1)
            cat = str(row[1]).strip().upper() if len(row) > 1 else ''
            if cat == search_cat.upper():
                results.append(row)
        else:
            if all(kw.upper() in row_text for kw in keywords):
                results.append(row)
    return results

def main():
    if '--list' in sys.argv:
        manifest = load_manifest()
        for m in manifest:
            print(f"[{m['tag']}] {m['sheet']}  ({m['rows']}r x {m['cols']}c)")
        return

    search_cat = None
    args = sys.argv[1:]
    if '--cat' in args:
        idx = args.index('--cat')
        if idx + 1 < len(args):
            search_cat = args[idx + 1]
            args.pop(idx)  # remove --cat
            args.pop(idx)  # remove value
        else:
            print("ERROR: --cat requires a value")
            return

    if not args and not search_cat:
        print("Usage: python _query.py [--cat CATEGORY] <keyword> [keyword2 ...]")
        print("       python _query.py --list")
        return

    keywords = args if args else ['']  # empty keyword ok when --cat specified
    manifest = load_manifest()

    for m in manifest:
        csv_path = m['csv_file']
        rows = find_matching_rows(csv_path, keywords, search_cat)
        if rows:
            print(f"\n{'='*80}")
            print(f"[{m['tag']}] Sheet: {m['sheet']}")
            print(f"{'='*80}")
            for row in rows:
                # Print compact: first 6 cols + last few meaningful cols
                desc = row[2] if len(row) > 2 else ''
                unit = row[3] if len(row) > 3 else ''
                # Print full row on one line, truncating long values
                compact = [str(c)[:60] for c in row if str(c).strip()]
                print(f"  {' | '.join(compact)}")

if __name__ == '__main__':
    main()
