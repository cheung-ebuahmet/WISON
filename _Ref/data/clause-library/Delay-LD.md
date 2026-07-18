# Delay Liquidated Damages — 误期违约金

> **Knowledge Object ID:** CL-LD-DELAY-001
> **商业优先级:** ⭐⭐⭐⭐⭐
> **最后更新:** 2026-07-09
> **数据来源:** `data/contracts/*.yaml`

---

## Summary

分包合同统一采用 **1‰/天** 的 Delay LD 费率（占合同价格的千分之一），上限为合同价的 **10%**。12.1 MEI 独有 Mechanical Completion 减免条款——若按期完成 MC，此前因中期间里程碑延误已扣减的 Delay LD 全额退还。EPC 主合同端待提取，背靠背匹配度目前无法验证。

---

## Contract References

| 合同 | 条款位置 | LD 依据 |
|------|---------|--------|
| EPC-ADNOC | GTC Article 18.4(e), A7 Schedule | ANX 05 Exh A.09 (15 milestones, 0.01167%-0.03333%/day) |
| 10.1 CCECC Civil II | Sub-Clause 10.7 | Att 04_Delay LD |
| 10.2 TCC Civil I/III | Sub-Clause 10.7 | Att 05 (Pkg I) + Att 06 (Pkg III) |
| 12.1 CCECC MEI I | SCS Clause 17 | Exh A_Work Schedule |
| 12.2 TCC MEI II | SCS Clause 17 / LOA | LOA Attachment 1 (7 milestones, 0.1%/day each) |

---

## Rates

| 合同 | LD/天 | LD 费率 | 合同价 | 上限 | 上限 % |
|------|------:|:---:|------:|------:|:---:|
| EPC-ADNOC | Varies (0.012%-0.033%/day) | Per milestone | USD 686.2M | USD 68.6M | 10% |
| **10.1 CCECC** | **AED 149,832** | 1‰ | 149,832,039 | 14,983,204 | 10% |
| **10.2 TCC** | **AED 162,120** | 1‰ | 162,119,510 | 16,211,951 | 10% |
| **12.1 CCECC** | **AED 160,892** | 1‰ | 160,891,988 | 16,089,199 | 10% |
| **12.2 TCC** | **AED 155,469** | 1‰ | 155,469,167 | 15,546,917 | 10% |

> **三份分包合同统一使用 1‰ (千分之一) 费率**。EPC 主合同使用按里程碑分档的每日百分比费率（0.01167%-0.03333%/天不等），总额上限均为 10%。
>
> **12.1 独有 MC Relief 减免机制**：若最终 Mechanical Completion 按期完成，此前扣除的中期 Delay LD 全额退还。
>
> **12.2 Delay LD** 按 LOA 附件的 7 个里程碑分别触发，不设中间退还机制。
>
> **EPC 数据已提取 (2026-07-18)** — 来自 FOA_Priced_Draft_ocred.pdf。15 个里程碑含具体费率。背靠背匹配现在可执行。

---

## Trigger Mechanism

### 共同触发条件

1. Subcontractor 未能在 Key Milestone Date 前完成任何 Key Milestone
2. Delay 归因于 Subcontractor（非 Force Majeure / Contractor Delay）
3. Contractor 先行发出 Delay LD Notice

### 关键时间节点 (10.1/10.2)

| Milestone | Deadline | 
|------|:---:|
| MAR/MS/ITP First Submission | 2025-12-15 |
| Excavation start for Sulphur Granulator | 2026-01-10 |
| Sulphur Granulator foundation complete | 2026-06-25 |
| All foundations complete | 2026-08-26 |
| All paving & road work complete | 2026-09-15 |

### 关键时间节点 (12.1)

*(待从 Exh A_Work Schedule 提取)*

---

## Special Provisions

### Mechanical Completion Relief (12.1 独有)

> If Subcontractor achieves Mechanical Completion on or before the relevant Scheduled Completion Date, any and all Delay Liquidated Damages deducted by Contractor in respect of delays occurring **prior to MC** shall be **refunded**.

**商业含义:** 12.1 的 Delay LD 有"全勤奖"机制——只要最终按时 MC，中间罚的全退。这给分包商提供了强烈的按时完工激励，也意味着 Contractor 在管理中期进度时不能过于依赖 LD 作为施压手段——如果对方最终赶回来，LD 会全部退还。

### Management System LD (12.1 独有，独立于 Delay LD)

- 未使用 Contractor SM 系统: **AED 10,000/次**
- 未参加管理层会议: 从保留金中扣减（金额由 Contractor 合理确定）
- Source: SCS Clause 8, Sub-Clause 4.9

---

## Notice Requirement

| 合同 | 要求 |
|------|------|
| 10.1 / 10.2 | Contractor **must serve notice** before deduction; no further notice required while LD period ongoing |
| 12.1 | Contractor shall deduct from payment; notice implied via IPC deduction |

> **操作要点:** 10.1/10.2 的 notice 是扣款前提条件，未发 notice 直接扣款有程序瑕疵风险。

---

## Recovery Method

| 方式 | 10.1/10.2 | 12.1 |
|------|:---:|:---:|
| IPC 直接扣减 | ✅ | ✅ |
| 保留金扣减 | ✅ | ✅ |
| 保函兑付 | ✅ (最后手段) | ✅ |
| 终止后追偿 | ✅ (Post-Termination Costs) | ✅ |

---

## Back-to-Back Position

| 维度 | EPC-ADNOC | Subcontracts | Gap |
|------|:---:|:---:|:---:|
| LD/天 | 0.012%-0.033%/day (按里程碑) | 1‰ 统一费率 | 🟡 结构不同，需按里程碑映射 |
| LD Cap | 10% | 10% | ✅ 一致 |
| Notice 要求 | GTC Article 18.4(e) | 10.1/10.2: serve notice; 12.1/12.2: IPC deduction | 🟡 程序不同 |
| MC Relief | 否 | 12.1 ✅ / 其他 否 | 🟡 12.1 更优惠 |
| LD 独立于其他赔偿 | GTC Article 18.4(e) | ✅ All subcons | ✅ 一致 |

> **更新 (2026-07-18):** EPC 数据已提取。EPC 使用粗细分档的里程碑 LD（PO 阶段 0.012%→施工阶段 0.02-0.025%→完工阶段 0.033%），
> 而分包合同统一使用简化的 1‰ (0.1%)。分包费率整体高于 EPC（1‰ vs 0.012%-0.033%），
> 形成有利的 LD 净差（flow-down margin）。但这意味着 EPC 端发生延误时，
> 分包合同端的 LD 罚款远高于主合同端——需要确保背靠背归因。

---

## Related

- **Clause Library:** [[Key-Personnel-LD]] | [[Payment]] | [[Variation]]
- **Analysis:** [[back-to-back-matrix]] | [[risk-register]]
- **Source YAML:** `10.1-CCECC-Civil-II.yaml`, `10.2-TCC-Civil-I-III.yaml`, `12.1-CCECC-MEI-I.yaml`
