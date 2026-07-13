# LD_Mapping — 误期损害赔偿 主合同⇄分包映射
`[v0.3 首批映射 · 🟢 Active · Rule Runtime for RULE-002 · Confidence: 92% · 偿还 CD-003]`

> **Coverage 93%** █████████░ · **Confidence 92%** █████████░ · **Validation 85%** ████████░░
> EPC 15 里程碑全 · 3/4 分包全参数 · 2 个真实 Issue 触发 (MEI Milestone #2 + PM KP-LD)
> 未覆盖：12.2 TCC MEI II LD 参数 · MC Relief 实际执行后果 · LD Notice 模板

---

## Canonical（EPC 主合同侧）
| 参数 | 取值 | 出处 |
|---|---|---|
| LD 触发 | 15 个 MC 里程碑逐日计，按各自 Completion Date | ANX5 Exh A.09 §A.9.1 |
| LD 日费率 | **0.01167%–0.03333%/天** of Lump Sum Price（按里程碑） | FOA p.4-5 · ANX5 A.09 §A.9.2.1 |
| LD 费率基准 | Lump Sum Price | FOA p.5 |
| LD 单里程碑上限 | 0.35%–1.0%（按里程碑） | FOA p.4-5 |
| LD 总上限 | **10% Agg** of AGREEMENT PRICE | ANX5 A.09 §A.9.2.3 · FOA p.5 |
| LD Bonus | **NOT USED** | ANX5 A.09 §A.9.3 |
| 计价币种 | USD | FOA p.5 |
| 总价 | USD 686,205,286 | FOA p.5 |

## Operational（分包合同侧）
| 参数 | 10.1 CCECC Civil II | 10.2 TCC Civil I/III | 12.1 CCECC MEI I | 12.2 TCC MEI II |
|---|---|---|---|---|
| LD 触发 | Key Milestones missed | Key Milestones missed | Key Milestones missed (Exh A Work Schedule) | ⚪ 待提取 |
| LD 日费率 | **0.1%/天 (1‰)** of contract price | **0.1%/天 (1‰)** | **0.1%/天 (1‰)** | ⚪ |
| LD 费率基准 | Subcontract Price (AED 149.8M) | Subcontract Price (AED 162.1M) | Provisional Subcontract Price (AED 160.9M) | ⚪ |
| LD 单里程碑上限 | 10% (per milestone cap) | 10% | **9%** (per milestone) | ⚪ |
| LD 总上限 | **10%** | **10%** | **10%** | ⚪ |
| LD 日金额 (AED) | **AED 149,832/天** | **AED 162,120/天** | **AED 160,892/天** | ⚪ |
| LD 日金额 (USD equiv) | ~USD 40,825/天 | ~USD 44,175/天 | ~USD 43,840/天 | ⚪ |
| MC Relief | ❌ | ❌ | **✅** 按期 MC → 前期 Delay LD 全额退还 | ⚪ |
| Notice 要求 | **须先发 Notice** | **须先发 Notice** | IPC 直接扣减（隐含 Notice） | ⚪ |
| 来源 | `_Ref/data/contracts/10.1-*.yaml` · Sub-Clause 10.7 | `_Ref/data/contracts/10.2-*.yaml` · Sub-Clause 10.7 | `_Ref/data/contracts/12.1-*.yaml` · SCS Clause 17 | ⚪ |

## Gap Analysis
| Gap | 涉及合同 | 类型 | 差异 | 风险 | 对 Wison 的影响 |
|---|---|---|---|---|---|
| **LD 费率** | 10.1/10.2/12.1 | **Inverse ✅** | 分包 0.1%/天 >> EPC 最低 0.01167%/天（约 8.6×） | **LOW** | 🟢 **有利**—— 对下 LD 费率远超对上，差额覆盖管理成本 |
| **LD 总上限** | 10.1/10.2/12.1 | **Covered ✅** | 10% = 10% | **LOW** | 🟢 对等——分包延误赔款上限等于主合同 LD 上限 |
| **单里程碑上限** | 12.1 | **Covered ✅** | 9% < 10% (差 1%, 对分包商略宽松) | **LOW** | 🟢 对 Wison 影响极小——总量仍受 10% Cap 约束 |
| **MC Relief** | 12.1 | **Inverse ⚠️** | EPC 无此机制，12.1 独有——按期 MC 前期 LD 全退 | **MEDIUM** | 🟡 若 12.1 按期 MC：前期扣的 Delay LD 必须退还 → Wison 失去 LD 收入但 EPC 无相应退还 → Wison 自留 LD 差额（有利）。若最终未按期 MC：LD 照扣，无影响 |
| **Notice 要求** | 10.1/10.2 | **Inverse ⚠️** | Civil 须先发 Notice 才能扣 LD；EPC CVR 14d 时限系 Variation 入口，非 LD 扣款前提 | **LOW** | 🟡 操作差异——Civil 扣款前必须记着发 Notice，程序瑕疵可导致扣款无效 |
| **LD 费率基准** | All | **Not Comparable** | EPC 以 Lump Sum (USD 686M) 为基；Subcon 以各自 Subcontract Price 为基 | — | 中性——不同合同规模的不同费率基准是正常商业安排 |

> **核心结论：LD 在三个分包合同中**全覆盖且对等或更优**。Wison 的最大风险不是 LD Gap，而是 12.1 的 MC Relief——如果 12.1 最终按期 MC，前期 LD 须全额退还。但即使退还，Wison 在此期间的 EPC LD 风险也被分包 LD 覆盖且有盈余。

## Rule Binding
| Rule ID | Runtime Status | 判定 | 备注 |
|---|---|---|---|
| **RULE-002** (LD Flow-down) | 🟢 **Runtime Ready** | **Covered**（Cap 对等 + 费率对 Wison 有利） | 12.1 MC Relief 作为 Exception 标注 |

## Active Issue
| Issue | 合同 | LD 状态 | 累积金额 (2026-07-13) |
|---|---|---|---|
| Milestone No.2 逾期 | 12.1 CCECC MEI I | LD 已触发 | Pkg1 25天 × AED 160,892 = **AED 4.02M** · Pkg3 39天 × AED 160,892 = **AED 6.27M** · 合计 **~AED 10.3M (≈USD 2.8M)** |
| PM 缺位 | 10.1 CCECC Civil II | KP-LD 已触发 | 2026-06-24 起 AED 10,000/天 × 19天 = **AED 190,000**（叠加，非替代 Delay LD） |

## Actions
1. **[立即]** 07-16 截止日后：若 12.1 无有效 Recovery Schedule → 执行 IPC LD 扣减（SCS Clause 17）+ 保留 ADNOC 升级权
2. **[本周]** 确认 10.1/10.2 的 Delay LD Notice 是否已按 Sub-Clause 10.7 正式发出（Civil 扣款前提）
3. **[监控]** 12.1 MC 进度——若分包商开始加速赶工，评估其按期 MC 概率，预判 LD 退还敞口

## Debt Repaid
- [x] **CD-003** — RULE-002 LD Flow-down Data Gap：10.1/10.2/12.1 LD 全参数已映射，RULE-002 现可产出量化 Gap 判定而不仅是"缺/不缺"
