# Payment_Mapping — 付款机制 主合同⇄分包映射
`[v0.3 首批映射 · 🟢 Active · Rule Runtime for RULE-004 · Confidence: 85% · 偿还 CD-005]`

> **Coverage 88%** █████████░░ · **Confidence 85%** ████████░░ · **Validation 55%** ██████░░░░
> EPC + 3/4 分包全参数映射 · 15d float 已量化 · Advance 10% 全覆盖
> 未验证：无真实 IPC 执行记录 · ANX5 A.07 Pricing 细则未读 · AED/USD peg 情景未建模

---

## Canonical（EPC 主合同侧）
| 参数 | 取值 | 出处 |
|---|---|---|
| Advance Payment | **YES — 10%** of Initial Agreement Price | FOA p.5 |
| Advance 条件 | APG(ANX8-C) + 发票 → 30d/14d 较晚者 | GTC Art 23.5(b) |
| Advance 回扣 | 按 FOA 比例逐张 IPC 扣 | GTC Art 23.5(c) |
| 付款周期 | **30 DAYS** from receipt of valid INVOICE | GTC Art 23.2(b) |
| 争议发票 | Company 14d 内退回 → 未争议部分 30d 付 | GTC Art 23.3 |
| Retention | **未见**（PBG + 里程碑替代） | — |
| Payment Currency | USD | FOA p.5 |
| 付款先决 | Commencement + PBG + PCG（FEED Endorsement 已删） | GTC Art 23.1 · SC item 8 |

## Operational（分包合同侧）
| 参数 | 10.1 CCECC Civil II | 10.2 TCC Civil I/III | 12.1 CCECC MEI I | 12.2 TCC MEI II |
|---|---|---|---|---|
| Advance Payment | **10%** | **10%** | **10%（分 2 期）** ⚠️ | ⚪ |
| Advance 条件 | APG + PB 提交 | APG + PB 提交 | APG+PB；**第 2 期须动员完成** | ⚪ |
| Advance 发放时限 | **14 days** | **14 days** | **30 days** | ⚪ |
| Advance 回扣 | 每 IPC 扣 10% | 每 IPC 扣 10% | 每 IPC 扣 10% | ⚪ |
| 付款周期 | **45 days** | **45 days** | **45 days** | ⚪ |
| 发票截止 | — | — | 次月 5 日前 | ⚪ |
| Retention | **10% + 5%** Warranty Bond | **10% + 5%** | **10%** | ⚪ |
| Retention 释放 | **100% at WC** | **100% at WC** | **PA + 银行保函** | ⚪ |
| 付款币种 | AED | AED | AED | ⚪ |
| 系统强制 | 可选 | 可选 | **强制 SM 系统**（未用 AED 10K/次 LD） | ⚪ |
| 来源 | `10.1-*.yaml` · COC Art 11 · Att 6 | `10.2-*.yaml` · COC Art 11 · Att 6 | `12.1-*.yaml` · SCS Clause 19 · Exh D | ⚪ |

## Gap Analysis
| Gap | 涉及合同 | 类型 | 差异 | 风险 | 对 Wison 的影响 |
|---|---|---|---|---|---|
| **付款周期** | 10.1/10.2/12.1 | **Inverse ✅** | Subcon 45d > EPC 30d → Wison 有 **15 天 float** | **LOW** | 🟢 **有利**——Wison 从 ADNOC 收款 30d，对下付款 45d → 正向现金流 |
| **预付款比例** | All | **Covered ✅** | 10% = 10% | **LOW** | 🟢 对等 |
| **预付款分期** | 12.1 | **Inverse ✅** | 12.1 分 2 期（50% on APG+PB，50% on mobilization） | **LOW** | 🟢 **有利**——Wison 收到 ADNOC 10% 预付后，仅需先释放 5% 给 12.1，另 5% 锁在动员后，降低 Wison 预付款风险 |
| **Retention 释放** | 10.1/10.2 | **Inverse ✅** | Civil WC 直接释放 vs EPC 无 Retention | **LOW** | 🟢 **有利**——Wison 从 ADNOC 无 Retention 扣减，但对下可持有至 WC |
| **Retention 释放** | 12.1 | **Partial ⚠️** | PA + 保函 vs Civil WC 直接释放 | **MEDIUM** | 🟡 中性——对 12.1 分包商更苛刻（增加保函成本），但不直接影响 Wison |
| **币种** | All | **Not Comparable** | EPC: USD · Subcon: AED | **MEDIUM** | 🟡 汇率敞口——USD/AED 挂钩（3.6725），历史波动极小，但若脱钩则产生敞口 |

> **核心结论：付款机制上 Wison 处于有利位置。** 15 天 float（30 vs 45）+ Civil Retention 持有 + 12.1 预付分期——三条线都对 Contractor 有利。唯一需关注是 AED/USD peg 风险（长期项目，概率低但影响大）。

## Rule Binding
| Rule ID | Runtime Status | 判定 |
|---|---|---|
| **RULE-004** (Payment Precondition) | 🟢 **Runtime Ready** | EPC: PBG+PCG+APG · Subcon: APG+PB（+12.1 mobilization）——先决条件结构对齐 |

## Actions
1. **[流程]** 利用 15 天 float 管理分包付款节奏——ADNOC 付款到账后再释放分包 IPC
2. **[本周]** 确认各分包 APG/PBG 是否均已提交且有效——这是 RULE-004 的触发条件
3. **[监控]** AED/USD peg 风险——虽然 peg 自 1997 年稳定，但长期项目应至少做一次情景分析

## Debt Repaid
- [x] **CD-005** — RULE-004 Payment Precondition Evidence Gap：10.1/10.2/12.1 保函/预付/Retention 参数已映射
