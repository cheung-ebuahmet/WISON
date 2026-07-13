# PROJECT PROFILE — 项目实例层 / Instantiation Layer
`[待填 · Phase 3 读合同 / Phase 4 访谈 填入 · 每格标出处]`

> Canonical 本体（[ONTOLOGY](ONTOLOGY.md)）通用；**本项目特定取值全部放这里**。换项目只换本文件，本体不动。
> 服从 [CONSTITUTION](CONSTITUTION.md)：单一事实源、每项有出处、留版本。现全为空槽，勿臆填。

## 项目标识 / Identity
> 来源：`00_PROJECT_CONTEXT.md`（用户提供）。标 `⚑待条款核实` 者仍须在合同读取阶段绑定 Clause 出处。

| 项 | 取值 | 出处 |
|---|---|---|
| 项目名 Project | **WISON ADNOC EPC Contract Intelligence System**（系统）；标的：**Ruwais Sulphur Granulation Plant (RSGP) Upgrade**，Hail & Ghasha Project No.**1005312**，EPC Onshore Works | 00_PROJECT_CONTEXT |
| 合同号 Contract No | **6000066707** | 00_PROJECT_CONTEXT |
| 业主 Employer（Org） | **ADNOC GAS OPERATIONS AND MARKETING – L.L.C.** | **FOA Cl.1** |
| 承包商 Contractor（Org） | **WISON ENERGY ENGINEERING (HONG KONG) LIMITED – ABU DHABI** | **FOA Cl.1** |
| Engineer（Org + 是否第三方/PMC） | **☐ 合同未设独立 Engineer**；COMPANY REPRESENTATIVE = **Mr. Jasem Al Hosani** (VP/A)；CONTRACTOR REPRESENTATIVE = **Mr. Feng Guoling** (Project Manager) | **FOA p.5** |
| 合同类型 | **LSTK (Lump Sum Turnkey)** | 00_PROJECT_CONTEXT |
| 合同标准/环境 | **AGES**（ADNOC Group Engineering Standards）；表单 **ADNOC-CICV-505A (v6)**；Highly protective Owner model | 00_PROJECT_CONTEXT · 合同抬头 |
| 项目模式（几层） | Employer(ADNOC) → WISON → External Contract(Subcontractor/Third Party) | 00_PROJECT_CONTEXT |

> **Alias RSGP ↔ SGP — 已解决（2026-07-13）**：主合同 ANX5 A.09 标题行 "EPC WORK FOR **RUWAIS SULPHUR GRANULATION PLANT** AT RSHT-2"；合同简称 **SGP**（每页抬头 `AG_Wison_SGP at RSHT2`）；**RSGP** = 正式全称 "Ruwais Sulphur Granulation Plant" 之简写；二者指同一设施，无冲突。**定本字**：引用合同条款/正式文件用全称或 SGP，不强调 RSGP 为独立缩写。见 [`CONTRACT_MAP.md`](CONTRACT_MAP.md) §0。

## Contract Package 成员 / Documents present
> 已实例化，详见 [`CONTRACT_MAP.md`](CONTRACT_MAP.md)。来源：`00_Contract Master Index_6000066707.xlsx`。
- **FOA**（Form of Agreement）✓ · **ANX 1 Special Conditions (PCC)** ✓ · **ANX 2 General T&C (GTC, 50 条)** ✓
- ANX 3 SOW · ANX 4 Completion Schedule · ANX 5 Pricing（含 Exh A.09 LD）· ANX 6 Facilities · ANX 7 Insurance · ANX 8 Securities(PCG/PBG/APG) · ANX 9 Submissions · ANX 10 Execution Req · ANX 11 Completion-Acceptance · ANX 12 HSE · ANX 13 ICV · ANX 14 Export Control
- 表单 **ADNOC-CICV-505A(v6)**；协议号 **4700025948**（vs 合同号 6000066707，待厘清 ⚑）。
- 商业核心（FOA/ANX1/2/4/5/7/8/11/14）均已 OCR、可溯；缺失/未 OCR 集中于 ANX 10 技术执行 exhibits。

## Order of Precedence / 文件优先权（本项目实际顺序）
```
1. FOA > 2. SC(PCC) > 3. GTC > 4. Insurance(ANX7) > 5. ICV(ANX13) > 6. HSE(ANX12) > 7. SOW(ANX3) > 8. Pricing(ANX5) > 9. Schedule(ANX4) > 10. Execution(ANX10) > 11. Completion-Acceptance(ANX11) > 12. Submissions(ANX9) > 13. Facilities(ANX6) > 14. Securities(ANX8)
```
依据：**FOA Cl.1.6**

## 起算锚点 / Anchor events（哪个 Event 触发什么，可不同日）
| 起算什么 | 触发 Event | 出处 |
|---|---|---|
| 生效 Effective | **EFFECTIVE DATE = 14 Feb 2025**（LOA 载明日） | **FOA p.2** |
| 工期起算 Time baseline | **COMMENCEMENT DATE = 13 Feb 2025** | **FOA p.4** |
| 付款起算 Payment start | 同 Commencement Date + 收讫 PBG/PCG | Art 23.1 |
| 保险起算 Insurance start | ___ | ⚑待 Art 41/ANX7 |
| Warranty 起算 | ETC / Partial PAC / PAC 签发日起 **12 个月** | **FOA p.5** |

## 完工里程碑 / Completion milestones（本项目采用哪些、叫什么）
`[x] Mechanical Completion  [ ] Taking Over  [x] Provisional Acceptance (PA)  [x] Final Acceptance (FA)`　≡ Ready For Start-Up (RFSU) 在 Art 15

## 关键商务参数 / Key commercials（Phase 3 填，带条款出处）
| 项 | 取值 | 条款/出处 |
|---|---|---|
| Contract Price | **USD 686,205,286**（Lump Sum 682,754,729 + PS 3,450,557 + Opt 13,770,337） | **FOA p.5** |
| LD（费率 / 上限） | 15 里程碑 0.01167%–0.03333%/天；每里程碑有单上限；**总上限 10%Agg** | **FOA p.4-5 · ANX5 A.09** |
| Retention | 未见（ADNOC 以 PBG+里程碑替代） | — |
| Advance Payment | **YES — USD 68,620,528.60（10%）**；按发票 % 回扣；APG(ANX8-C) | **FOA p.5 · Art 23.5/30.1** |
| 保函 Bonds | **PBG=USD 68,620,528.60(10%)**；PA 降 50%；**PCG=Required**；APG=预付额 | **FOA p.5-6 · Art 30 · ANX8** |
| Insurance | Company CAR (Full AgP + TPL $20M + Prop $20M) · Contractor WC $1M + TPL $10M + Pollution $10M + Motor $1M + Equipment AR · Deductible=Wison · Subcon 100% B2B | **Art 41 · ANX7-1 · ANX7-3 · 分包 Insurance Requirements** |
| 适用法 | **Abu Dhabi 法 + UAE 联邦法** | **Art 46.1** |
| 争议解决 | **ICC 仲裁 · Abu Dhabi seat · 英文 · 3 仲裁员** · 60d 友好和解 · 终局 · 严格保密 | **Art 46.2** |
