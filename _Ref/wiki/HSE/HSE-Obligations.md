# HSE Obligations — 健康安全环境义务

> **合同依据：** EPC Agrmt ANX 12 (HSE Requirements)
> **分包背靠背：** 各分包合同均含 HSE Attachment，核心标准引用自 ADNOC HSE 体系

---

## 1. 业主→Wison (EPC Agrmt — ANX 12)

### 关键文件

| 文件 | 路径 | OCR |
|------|------|-----|
| ANX 12 正文 | → `Main_Contract\01_EPC Agrmt\ANX 12_HSE Requirements\ANX 12_HSE Requirements_ocred.pdf` | ✅ |
| ANX 12 签章 | → `Main_Contract\01_EPC Agrmt\ANX 12_HSE Requirements\ANX 12_HSE Requirements_Signed.pdf` | — |
| Att 1: HSE Studies | → `Main_Contract\01_EPC Agrmt\ANX 12_HSE Requirements\ANX 12_HSE Requirements_Att 1_HSE Studies_ocred.pdf` | ✅ |
| Att 2: Company HSE Standards | → `Main_Contract\01_EPC Agrmt\ANX 12_HSE Requirements\ANX 12_HSE Requirements_Att 2_COMPANY HSE STANDARDS.zip` | 📦 |
| ADR-002: Updated HSE Requirements | → `Main_Contract\01_EPC Agrmt\ANX 12_HSE Requirements\ANX 12_HSE Requirements_ADR-002_Updated HSE Requirements_ocred.pdf` | ✅ |
| ADR-003: Asset Integrity | → `Main_Contract\01_EPC Agrmt\ANX 12_HSE Requirements\ANX 12_HSE Requirements_ADR-003_Asset Integrity_ocred.pdf` | ✅ |
| Project HSE Plan | → `Main_Contract\01_EPC Agrmt\ANX 12_HSE Requirements\ANX 12_HSE Requirements_PR-5312-1000-SA-0001 Project HSE Plan_Signed.pdf` | ❌ |

### ADNOC HSE 标准体系

> Att 2 压缩包内含全套 ADNOC HSE 标准，分四大类：

| 类别 | Code | 涵盖 |
|------|------|------|
| **CE** — Crisis & Emergency | HSE-CE-ST01~03 | 应急管理、溢油、消防 |
| **EN** — Environment | HSE-EN-ST01~07 | 环评、废物、生物多样性、空气 |
| **GA** — General Admin | HSE-GA-ST02~11 | HSE 管理体系、审计、救生规则 |
| **OH** — Occupational Health | HSE-OH-ST01~12 | 职业健康、化学品、人因工程 |
| **OS** — Operational Safety | HSE-OS-ST01~31 | PTW、JSA、电气安全、高空作业等 |
| **RM** — Risk Management | HSE-RM-ST01~14 | HAZID、QRA、SIL、PSSR |

---

## 2. Wison→分包商 (Subcontract HSE)

### 分包 HSE 文件位置

| 分包 | HSE 文件 | 路径 |
|------|---------|------|
| 12.1 CCECC MEI I | Exhibit H: HSE Requirements | → `Subcon_Payments\12.1 CCECC - MEI Pkg I\Contract\01_Subcon\Part II_Exhibits\Exh H_HSE Requirements\` |
| 10.1 CCECC Civil II | Attachment 3: HSE Requirements | → `Subcon_Payments\10.1 CCECC - Civil II\Contract\Part II Exhibits\Attachment 3 - HSE requirements\` |
| 10.2 TCC Civil I/III | Atch. 3: HSE Requirements | → `Subcon_Payments\10.2 TCC - Civil I_III\Contract\Part II Atchments\Atch. 3 - HSE requirements\` |
| 12.2 TCC MEI II | 🔴 缺失 | — |

### 分包 HSE 通用结构

每个分包的 HSE Requirements 均包含：
```
HSE Requirements.pdf              ← 主文件
├── 1 HSE Requirements.pdf        ← 一级 HSE 要求
├── 2 HSE requirements Attachments/
│   ├── ATTACH-A/  ← ADNOC HSE 标准 (~115 个 PDF，与 EPC Att 2 相同体系)
│   ├── ATTACH-B/  ← ADNOC 补充文件 (HSE Policy 等, ~19 个)
│   ├── ATTACH-C/  ← 技术指南 (EIA TOR, 认可机构等)
│   └── ATTACH-D/  ← HSE 投标评估问卷
├── 3 ADR002 - Updated HSE Requirements.pdf
├── 4 ADR003 - Asset Integrity.pdf
├── 5 ADNOC Group Medical Fitness Guidelines.pdf
├── App 01_Contractor Management Procedure/  ← PR-5312 SA-0001~0008
├── App 02_ADNOC HSEWM Min Reqts/
├── App 03_HSE Assurance Program/
├── App 04_Pre-Mob Audit Checklists/
└── App 05_Approved Training Providers/
```

---

## 3. HSE 背靠背检查清单

| 检查项 | EPC 要求 | 12.1 | 10.1 | 10.2 | 12.2 |
|--------|---------|------|------|------|------|
| Project HSE Plan (SA-0001) | ✅ | ✅ | ✅ | ✅ | 🔴 |
| Emergency Response Plan (SA-0002) | ✅ | ✅ | ✅ | ✅ | 🔴 |
| Construction HSE Plan (SA-0003) | ✅ | ✅ | ✅ | ✅ | 🔴 |
| Permit to Work (SA-0004) | ✅ | ✅ | ✅ | ✅ | 🔴 |
| Environment Management Plan (SA-0005) | ✅ | ✅ | ✅ | ✅ | 🔴 |
| Waste Management (SA-0006) | ✅ | ✅ | ✅ | ✅ | 🔴 |
| Transportation Plan (SA-0007) | ✅ | ✅ | ✅ | ✅ | 🔴 |
| Welfare Management (SA-0008) | ✅ | ✅ | ✅ | ✅ | 🔴 |
| ADR-002 (Updated HSE) | ✅ | ✅ | ✅ | ✅ | 🔴 |
| ADR-003 (Asset Integrity) | ✅ | ✅ | ✅ | ✅ | 🔴 |
| Camp Welfare Audit | ✅ | ✅ | ✅ | ✅ | 🔴 |
| Pre-Mob Audit Checklist | ✅ | ✅ | ✅ | ✅ | 🔴 |
| Contractor Onboarding Guidelines | ✅ | ✅ | ✅ | ✅ | 🔴 |

> ✅ = 有对应文件，🔴 = 缺失

---

## 4. 关键 ADNOC HSE 政策文件（分包合同内）

### ATTACH-B — ADNOC 通用 HSE 政策
| 序号 | 文件 | 主题 |
|------|------|------|
| 01 | HSE Policy | ADNOC HSE 方针 |
| 02 | HSE-MAN-003 | HSE 管理手册 |
| 03 | HSE-ST-029 | *(待确认)* |
| 04 | HSE-GU-019 | *(待确认)* |
| 05 | HSE-ST-009 | *(待确认)* |
| 06 | HSE-ST-007 | *(待确认)* |
| 07 | GS-MAN-003 | 通用规范 |
| 08 | IA_HSECES-GU-016 | HSECES (安全关键要素) |
| 09 | HSE-ST-071 | *(待确认)* |
| 10 | HSE-ST-001 | *(待确认)* |
| 11 | HSE-ST-023 | *(待确认)* |
| 12 | HSE-ST-017 | *(待确认)* |
| 13 | HSE-ST-018 | *(待确认)* |
| 14 | HSE-ST-016-A/B | *(待确认)* |
| 15 | HSE-ST-008 | *(待确认)* |
| 16 | HSE-ST-002 | *(待确认)* |
| 17 | TE-ST-002 | *(待确认)* |
| 18 | HSE-GU-055 | *(待确认)* |
| 19 | AHQ-HSE-HPG-GID-006 | ADNOC HQ HSE 指南 |

---

## 相关 Wiki 页面
- [[Insurance-Requirements]] — 保险与 HSE 的交叉（Workmen's Comp, Liability）
- [[EPC-Contract-Structure]] — ANX 12 完整文件清单
- [[Subcontractor-Matrix]] — 各分包 HSE 义务对比
