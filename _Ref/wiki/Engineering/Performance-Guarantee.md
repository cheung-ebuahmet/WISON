# Performance Guarantee — 性能保证

> **定义：** 承包商保证工程在完工测试中达到的最低性能指标。未达标 → 违约金或补救义务。
> **合同层级：** EPC Agrmt (业主→Wison) → 各分包 Subcon (Wison→Subcontractor)

---

## 1. 业主→Wison (EPC Agrmt)

### 关键文件

| 文件 | 路径 | OCR |
|------|------|-----|
| Performance Guarantees | → `Main_Contract\01_EPC Agrmt\ANX 10_Execution Requirements\ANX 10_Execution Requirements_Exh A.11_Performance Guarantees_Signed.pdf` | ❌ |
| Performance Test Run Conditions | → `Main_Contract\01_EPC Agrmt\ANX 10_Execution Requirements\ANX 10_Execution Requirements_Exh A.10_Performance Test Run Conditions_Signed.pdf` | ❌ |
| LD & Bonus Provisions | → `Main_Contract\01_EPC Agrmt\ANX 05_Pricing Schedule_Exh A.09_Liquidated Damages - Bonus Provisions_ocred.pdf` | ✅ |
| Commissioning & Test Run | → `Main_Contract\01_EPC Agrmt\ANX 10_Execution Requirements\ANX 10_Execution Requirements_Exh B.52_Commissioning and Test Run_Signed.pdf` | ❌ |
| Mechanical Completion & Commissioning | → `Main_Contract\01_EPC Agrmt\ANX 10_Execution Requirements\ANX 10_Execution Requirements_Exh B.50_Mechanical Completion and Commissioning Planning and Documentation_Signed.pdf` | ❌ |

### 性能保证体系（待从文件中提取）

> ⚠️ **需 OCR ANX 10 Exh A.10 + A.11 后填充具体数值**

| 保证项目 | 保证值 | 测试标准 | 违约后果 |
|----------|--------|---------|---------|
| *(待提取)* | | | |
| *(待提取)* | | | |

### Performance Test Run (Exh A.10)
- 测试条件 → 待从 A.10 提取
- 测试程序参考 → Exh B.52 (Commissioning and Test Run)

---

## 2. Wison→分包商 (Subcontract Back-to-Back)

### 2.1 12.1 CCECC — MEI Pkg I
| 文件 | 路径 |
|------|------|
| SOW | → `Subcon_Payments\12.1 CCECC - MEI Pkg I\Contract\01_Subcon\Part II_Exhibits\Exh A_Work Scope - Schedule\A 1.1 Scope of Work-Rev.0.doc` |
| Quality Requirements | → `Subcon_Payments\12.1 CCECC - MEI Pkg I\Contract\01_Subcon\Part II_Exhibits\Exh E_Quality Requirements\` |
| Commissioning | → `Subcon_Payments\12.1 CCECC - MEI Pkg I\Contract\01_Subcon\Part II_Exhibits\Exh B_Method of Measurement\13.N-Commissionning and Start up.pdf` |

### 2.2 10.1 CCECC — Civil Pkg II
| 文件 | 路径 |
|------|------|
| SOW | → `Subcon_Payments\10.1 CCECC - Civil II\Contract\Part II Exhibits\Attachment 5 - Scope of Work\1. Scope of Work for Package 2.pdf` |
| Quality | → `Subcon_Payments\10.1 CCECC - Civil II\Contract\Part II Exhibits\Attachment 4 - Quality Management\` |

### 2.3 10.2 TCC — Civil Pkg I & III
| 文件 | 路径 |
|------|------|
| SOW | → `Subcon_Payments\10.2 TCC - Civil I_III\Contract\Part II Atchments\Atch. 5 - Scope of Work\` |
| Quality | → `Subcon_Payments\10.2 TCC - Civil I_III\Contract\Part II Atchments\Atch. 4 - Quality Management\` |

### 2.4 12.2 TCC — MEI Pkg II
> 🔴 **严重残缺** — 仅主合同 PDF (`WISON24108C26003_SubCon MEI Pkg II.pdf`)，Part II 全缺

---

## 3. 背靠背差距分析

> ⚠️ **待完成：** 需逐个对比 EPC ANX 10 Exh A.10/A.11 的每项保证值与各分包 SOW 中的对应条款，识别：
> - 完全背靠背的条款（分包完全承接）
> - 有差额的条款（Wison 自留风险）
> - 分包合同中缺失的条款（Wison 完全自担）

| EPC 保证项 | 12.1 MEI I | 10.1 Civil II | 10.2 Civil I/III | 12.2 MEI II |
|-----------|------------|---------------|-------------------|-------------|
| *(待提取)* | | | | |

---

## 4. 关键日期与触发点

> ⚠️ **需从 ANX 04 Schedule (Exh A.06) 提取**

| 里程碑 | 日期 | 相关保证 |
|--------|------|---------|
| Mechanical Completion | *(待提取)* | 触发 Performance Test |
| Performance Test 完成 | *(待提取)* | 触发保证值判定 |
| 保证期 (Defects Notification Period) | *(待提取)* | FIDIC Sub-Clause 11 |

---

## 相关 Wiki 页面
- [[Liquidated-Damages]] — 性能不达标的 LD 计算
- [[EPC-Contract-Structure]] — ANX 10 完整子文件清单
- [[Subcontractor-Matrix]] — 各分包对比一览
