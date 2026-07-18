# 分包合同价格数据库

## 来源

| 标签 | 分包商 | 包号 | 原始文件 | 版本 |
|------|--------|------|----------|------|
| `CCECC_PkgII` | CCECC | Civil Pkg II (标2) | 土建标2合同价格表.xlsx | Rev.B 2025/12/2 |
| `TCC_PkgI` | TCC | Civil Pkg I (标段1) | 土建标段1合同价格表.xlsx | Rev.A 2025/09/05 |
| `TCC_PkgIII` | TCC | Civil Pkg III (标3) | 土建标3合同价格表.xlsx | Rev.A 2025/09/05 |

项目：EPC Works of the Sulfur Granulator Plant For ADNOC Gas Processing

## 目录结构

```
price-database/
├── _manifest.json          # 所有 CSV 的完整清单（机器可读）
├── _column-mapping.md      # 各工作表列号→含义对照
├── _query.py               # Python 查询工具脚本
├── README.md               # 本文件
├── CCECC_PkgII/            # 12 个工作表 → CSV
├── TCC_PkgI/               # 12 个工作表 → CSV
└── TCC_PkgIII/             # 8 个工作表 → CSV
```

## 所有工作表一览

| 工作表 | CCECC | TCC I | TCC III | 说明 |
|--------|:-----:|:-----:|:-------:|------|
| A-Summary | ✓ | ✓ | ✓ | 合同价汇总 |
| A.1-INDIRECTS BREAKDOWN | ✓ | ✓ | ✓ | 间接费细目 |
| PLOT PLAN（Green） | ✓ | ✓ | ✓ | 总图 Green 区 |
| PLOT PLAN (Brown) | ✓ | ✓ | — | 总图 Brown 区 |
| CIVIL（Green） | ✓ | ✓ | ✓ | 土建 Green 区单价表 |
| CIVIL（Brown) | ✓ | ✓ | — | 土建 Brown 区单价表 |
| BLDG（Green) | — | ✓ | ✓ | 房建 Green 区（仅 TCC） |
| UG PIP（Green） | ✓ | ✓ | ✓ | 地下管线 Green 区 |
| UG PIP（Brown) | ✓ | ✓ | — | 地下管线 Brown 区 |
| CMS (Green) | ✓ | ✓ | — | 施工管理服务 |
| Provisional Sum | ✓ | — | — | 暂列金（仅 CCECC） |
| Labor Rates | ✓ | ✓ | ✓ | 全包人工费率 |
| Equipment Rates | ✓ | ✓ | ✓ | 全包设备费率 |

## 快速查询

用 `_query.py` 按关键字搜所有 CSV：

```bash
cd D:\Wison\_tools\price-database
python _query.py "DUCT BANK"    # 搜 duct bank
python _query.py "MANHOLE"      # 搜 manhole
python _query.py "CONCRETE"     # 搜所有混凝土项
```

## 单价解读要点

1. **Manhours U/Rate (a) 不计入 Direct Cost Total** — 总价公式为 f = b + c + d + e（人工+材料+工具+设备）
2. **所有价格单位 = AED**（阿联酋迪拉姆）
3. **CCECC 与 TCC 的 Material U/Rate 差异极大**（如 DUCT BANK 混凝土：CCECC 2,510 vs TCC 466 AED/M3），对比时需核实双方对工作范围定义是否一致
4. 详细列映射见 `_column-mapping.md`
