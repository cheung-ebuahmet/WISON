# Liquidated Damages — 误期损害赔偿

> **定义 (FIDIC Sub-Clause 8.7):** 承包商未能按期竣工时，向业主支付的每日固定金额赔偿。不是罚款，是预先约定的损害赔偿。
> **核心原则：** LD 是 Employer 的唯一金钱救济（除非合同另有约定）。

---

## 1. 业主→Wison (EPC Agrmt)

### 关键文件

| 文件 | 路径 | OCR |
|------|------|-----|
| LD & Bonus Provisions | → `Main_Contract\01_EPC Agrmt\ANX 05_Pricing Schedule_Exh A.09_Liquidated Damages - Bonus Provisions_ocred.pdf` | ✅ |
| Schedule | → `Main_Contract\01_EPC Agrmt\ANX 04_Schedule_Exh A.06_Project Completion Schedule - Atts 1-6_Signed.pdf` | ❌ |
| Performance Guarantees | → `Main_Contract\01_EPC Agrmt\ANX 10_Execution Requirements\ANX 10_Execution Requirements_Exh A.11_Performance Guarantees_Signed.pdf` | ❌ |

### LD 结构（待从 A.09 OCR 提取具体数值）

> ⚠️ **需精读 ANX 05 Exh A.09 OCR 后填充**

| LD 类型 | 每日费率 | 上限 (Cap) | 触发条件 |
|---------|---------|-----------|---------|
| **Delay LD** (工期延误) | *(待提取)* | *(待提取)* | 未在竣工日期前完成 |
| **Performance LD** (性能不达标) | *(待提取)* | *(待提取)* | Performance Test 未达到保证值 |
| *(其他类型)* | | | |

### LD 总计上限 (Overall Cap)
> *(待从合同提取 — 通常为合同价格的 X%)*

### Bonus 条款
> ANX 05 Exh A.09 同时涵盖 Bonus（提前竣工奖金）条款

---

## 2. Wison→分包商 (Subcontract Back-to-Back)

### 2.1 12.1 CCECC — MEI Pkg I

| 文件 | 路径 |
|------|------|
| Key Personnel LD | → `Subcon_Payments\12.1 CCECC - MEI Pkg I\Contract\01_Subcon\Part II_Exhibits\Exh E_Quality Requirements\Appendix - Key Personnel & Liquidated Damages.docx` |
| Schedule LD | → `Subcon_Payments\12.1 CCECC - MEI Pkg I\Contract\01_Subcon\Part II_Exhibits\Exh A_Work Scope - Schedule\A 2 Work Schedule_（MEI Package 1）.doc` |
| Amdt 01 | → `Subcon_Payments\12.1 CCECC - MEI Pkg I\Contract\02_Amdt 01\Amdt 01_MEI Pkg I (Revised) .pdf` |

### 2.2 10.1 CCECC — Civil Pkg II

| 文件 | 路径 |
|------|------|
| Delay LD | → `Subcon_Payments\10.1 CCECC - Civil II\Contract\Part II Exhibits\Attachment 5 - Scope of Work\3. Schedule Requirements\DELAY LIQUIDATED DAMAGES - PACKAGE 2.pdf` |
| Key Personnel LD | → `Subcon_Payments\10.1 CCECC - Civil II\Contract\Part II Exhibits\Attachment 5 - Scope of Work\4. Key Personnel\Appendix - Key Personnel & Liquidated Damages.pdf` |

### 2.3 10.2 TCC — Civil Pkg I & III
| 文件 | 路径 |
|------|------|
| Schedule Requirements | → `Subcon_Payments\10.2 TCC - Civil I_III\Contract\Part II Atchments\Atch. 5 - Scope of Work\3. Schedule Requirements\` |

### 2.4 12.2 TCC — MEI Pkg II
> 🔴 Part II 全缺 — LD 条款待补

---

## 3. LD 多层级对比表

> ⚠️ **核心分析工具 — 待填充数据后使用**

| 维度 | EPC (业主→Wison) | 12.1 MEI I | 10.1 Civil II | 10.2 Civil I/III | 12.2 MEI II |
|------|-------------------|------------|---------------|-------------------|-------------|
| **Delay LD / 天** | *(待提取)* | *(待提取)* | *(待提取)* | *(待提取)* | 🔴 |
| **Delay LD 上限** | *(待提取)* | *(待提取)* | *(待提取)* | *(待提取)* | 🔴 |
| **Performance LD** | *(待提取)* | *(待提取)* | N/A (Civil?) | N/A (Civil?) | 🔴 |
| **Key Personnel LD** | *(待提取)* | *(待提取)* | *(待提取)* | *(待提取)* | 🔴 |
| **Overall LD Cap** | *(待提取)* | *(待提取)* | *(待提取)* | *(待提取)* | 🔴 |
| **合同金额** | *(待提取)* | *(待提取)* | *(待提取)* | *(待提取)* | 🔴 |

### 背靠背差距警戒线
- 🟢 **完全背靠背：** 分包 LD ≥ EPC LD 同等比例（Wison 无净风险）
- 🟡 **小差距：** 分包 LD < EPC LD（Wison 自留差额）
- 🔴 **大缺口：** 分包无对应 LD 条款（Wison 完全自担）

---

## 4. 关键概念

### Delay LD vs Performance LD
- **Delay LD：** 没按时完成（时间维度）
- **Performance LD：** 完成了但性能不达标（质量/产出维度）
- 两者**可叠加**，但有各自的上限和总计上限

### Key Personnel LD
- 分包合同中常见的单独 LD 类型
- 触发条件：关键人员未到位、未经批准替换、在岗时间不足
- 通常按人/天计

### FIDIC 关键条款
- Sub-Clause 8.7: Delay Damages
- Sub-Clause 11.4: Failure to Remedy Defects
- Sub-Clause 15.2: Termination for Contractor's Default (Employer's Entitlements)

---

## 相关 Wiki 页面
- [[Performance-Guarantee]] — Performance LD 的技术指标基准
- [[Subcontractor-Matrix]] — 各分包商业条款对比
- [[EPC-Contract-Structure]] — ANX 04/05/10 完整结构
