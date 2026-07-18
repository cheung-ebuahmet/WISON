# 分包合同价格表 — 列映射参考

## 适用文件
- CCECC Pkg II (标2) Rev.B 2025/12/2
- TCC Pkg I (标段1) Rev.A 2025/09/05
- TCC Pkg III (标3) Rev.A 2025/09/05

## 通用工作表结构

所有文件的定价表均使用以下统一列公式：
- a = Manhours U/Rate（参考用，不计入总价）
- b = Labor Cost U/Rate
- c = Material Cost U/Rate
- d = Tools & Consumable Cost U/Rate
- e = Equipment Cost U/Rate
- **f = DIRECT COST TOTAL U/Rate = b + c + d + e**

## 各工作表列号映射

### CIVIL（Green）— 29列 (CCECC) / 27列 (TCC Pkg I) / 26列 (TCC Pkg III)
Row 7 = 表头, Row 8 = WBS 分区, Row 9 = 公式行, Row 10+ = 数据

| 内容 | CCECC Pkg II | TCC Pkg I | TCC Pkg III |
|------|:-----------:|:---------:|:-----------:|
| Item No | C1 | C1 | C1 |
| Category | C2 | C2 | C2 |
| Description | C3 | C3 | C3 |
| Unit | C4 | C4 | C4 |
| Qty | C5 | C5 | C5 |
| Qty by WBS | C6-C14 | C6-C14 | C6-C13 |
| **Manhours U/Rate (a)** | **C15** | **C15** | **C14** |
| Manhours Amount | C16 | C16 | C15 |
| **Labor U/Rate (b)** | **C17** | **C17** | **C16** |
| Labor Amount | C18 | C18 | C17 |
| **Material U/Rate (c)** | **C19** | **C19** | **C18** |
| Material Amount | C20 | C20 | C19 |
| **Tools U/Rate (d)** | **C21** | **C21** | **C20** |
| Tools Amount | C22 | C22 | C21 |
| **Equipment U/Rate (e)** | **C23** | **C23** | **C22** |
| Equipment Amount | C24 | C24 | C23 |
| **DIRECT COST TOTAL U/Rate (f)** | **C25** | **C25** | **C24** |
| Total Amount | C26 | C26 | C25 |
| Remarks | C27 | C27 | C26 |

### CIVIL（Brown）— 21列 (CCECC) / 20列 (TCC)
Row 7 = 表头, Row 8 = WBS, Row 9 = 公式, Row 10+ = 数据

| 内容 | CCECC Pkg II | TCC Pkg I |
|------|:-----------:|:---------:|
| Qty by WBS | C6-C7 | C6-C7 |
| **Manhours U/Rate (a)** | **C8** | **C8** |
| Manhours Amount | C9 | C9 |
| **Labor U/Rate (b)** | **C10** | **C10** |
| Labor Amount | C11 | C11 |
| **Material U/Rate (c)** | **C12** | **C12** |
| Material Amount | C13 | C13 |
| **Tools U/Rate (d)** | **C14** | **C14** |
| Tools Amount | C15 | C15 |
| **Equipment U/Rate (e)** | **C16** | **C16** |
| Equipment Amount | C17 | C17 |
| **DIRECT COST TOTAL U/Rate (f)** | **C18** | **C18** |
| Total Amount | C19 | C19 |

### UG PIP（Green）— 21列 (三者一致)
Row 7 = 表头, Row 8 = WBS (UNIT 10 General), Row 9 = 公式, Row 10+ = 数据

| 内容 | 列号 |
|------|:---:|
| Description | C3 |
| Size | C4 |
| Material Spec | C5 |
| Unit | C6 |
| Qty | C7 |
| Qty by WBS | C8 |
| **Manhours U/Rate (a)** | **C9** |
| Manhours Amount | C10 |
| **Labor U/Rate (b)** | **C11** |
| Labor Amount | C12 |
| **Material U/Rate (c)** | **C13** |
| Material Amount | C14 |
| **Tools U/Rate (d)** | **C15** |
| Tools Amount | C16 |
| **Equipment U/Rate (e)** | **C17** |
| Equipment Amount | C18 |
| **DIRECT COST TOTAL U/Rate (f)** | **C19** |
| Total Amount | C20 |

### UG PIP（Brown）— 25列 (CCECC) / 21列 (TCC)
结构同 UG PIP Green，WBS 仅 UNIT 50 一列。

### PLOT PLAN（Green/Brown）
结构与对应 CIVIL 表一致，额外包含 Reference 列 (C4)。

### CMS（Green）
结构与 CIVIL/UG PIP 相同，含 Manhours/Labor/Material 三档 U/Rate → Total。

### 汇总表 (A-Summary, A.1-INDIRECTS BREAKDOWN)
无统一列映射，各文件结构类似但列数不同。

### Labor Rates
固定列：CLASS | Classification | RATE (AED/HR) | OVERTIME RATE (AED/HR)

### Equipment Rates
固定列：SR. NO. | DESCRIPTION | MONTHLY RATE (AED) | DAY RATE WORK (AED) | DAY RATE STAND-BY (AED)
