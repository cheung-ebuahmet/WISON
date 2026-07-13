# Insurance_Mapping — 保险 主合同⇄分包映射
`[v0.3.2 · 🟢 Active · Risk Transfer Engine — Stage 1: Insurance · Coverage: 78% · Confidence: 71%]`

> **Coverage 78%** ████████░░ · **Confidence 71%** ███████░░░ · **Validation 30%** ███░░░░░░░
> EPC Art 41 全文已读 · ANX7 Company CAR 已读 · 分包 5/5 合同 Insurance Requirements 已确认
> 未验证：实际保险凭证 · 免赔额具体数值 · 索赔历史

---

## Round 1 — Insurance Inventory（有哪些保险？）

### Company-Provided (EPC · ANX7-1)
| 险种 | 承保方 | 保额/基础 | 被保方 | 出处 |
|---|---|---|---|---|
| **CAR** (Construction All Risks) | **ADNOC** | Full AGREEMENT PRICE (USD 686M) | ADNOC Group + Contractor + Subcontractors(all tiers) + Vendors + Consultants | ANX7-1 §1-3 |
| CAR — TPL 扩展 | ADNOC | **USD 20,000,000** / occurrence | 同上 | ANX7-1 §2 |
| CAR — Existing Property | ADNOC | **USD 20,000,000** / occurrence/aggregate | 同上 | ANX7-1 §2 |
| CAR — Transit | ADNOC | CIF+10% or FOB+10% | 同上 | ANX7-1 §2 |
| CAR — Terrorism | ADNOC | Included | 同上 | ANX7-1 §6 |

### Contractor-Provided (EPC · Art 41.1–41.5)
| 险种 | 承保方 | 保额 | Additional Insured? | Waiver of Subrogation? |
|---|---|---|---|---|
| **Workmen's Comp** (Employer's Liability) | Wison | **USD 1,000,000** / occurrence | ❌ (excluded per 41.6) | ❌ |
| **Motor Vehicle TPL** | Wison | UAE law + **USD 1,000,000** property | ✅ | ✅ |
| **All Risk — Equipment** | Wison | Full value of Contractor Equipment | ✅ | ✅ |
| **Third Party Liability** | Wison | **USD 10,000,000** / occurrence | ✅ | ✅ |
| **Pollution Liability** | Wison | **USD 10,000,000** / occurrence | ✅ | ✅ |
| **Additional** (FOA) | Wison | **None** specified (FOA p.6: "None") | — | — |

### 关键条款
| 条款 | 内容 | 出处 |
|---|---|---|
| Deductibles | **全部由 Contractor 承担**（含针对 Company 的索赔免赔额） | Art 41.9 |
| Insurer Rating | S&P / AM Best **≥ A−** | Art 41.17(a)(i) |
| Certificates | Company 要求时提供；Company 审查不构成弃权 | Art 41.7–41.8 |
| 保险失效 | Company 可自行投保并追偿 | Art 41.10 |
| Claims 通知 | 尽快书面通知 Company + 持续更新 | Art 41.13 |
| UAE Law | 优先当地注册保险公司 (Federal Law No.6/2007) | Art 41.14 |
| PAC 过渡 | 施工期→运营期保险切换；承包商须提交 INSURANCE DECLARATION | Art 41.16(e) · ANX7-3 |

---

## Round 2 — Risk Allocation（每种保险：谁做/谁付/谁受益/谁担免赔？）

| 险种 | Who Procures | Who Pays | Who Benefits | Who Bears Deductible | Who Files Claim |
|---|---|---|---|---|---|
| **CAR** | ADNOC (ANX7-1) | ADNOC | All parties (incl. Wison + Subs) | **Wison** (Art 41.16(c)) | ADNOC-driven (Art 41.19) |
| **Workmen's Comp** | Wison | Wison | Wison employees | Wison | Wison |
| **Motor TPL** | Wison | Wison | Third parties + Wison | Wison | Wison |
| **Equipment AR** | Wison | Wison | Wison | Wison | Wison |
| **TPL** | Wison | Wison | Third parties + Wison (additional insured) | Wison | Wison |
| **Pollution** | Wison | Wison | Third parties + Wison (additional insured) | Wison | Wison |

> ⚠ **核心发现**：CAR 由 ADNOC 投保，但**免赔额由 Wison 承担**——这是 LSTK 风险分配的保险镜像：Company 提供保障壳，Contractor 填免赔额的坑。

---

## Round 3 — Back-to-Back Mapping（分包是否承接？）

| 险种 | EPC Contractor 义务 | 分包要求 (10.1/10.2/12.1/12.2/99) | 流转类型 | Gap |
|---|---|---|---|---|
| **Workmen's Comp** | USD 1M/occ | ✅ USD 1M/occ — verbatim | **Covered** | 无 |
| **Motor TPL** | USD 1M property | ✅ USD 1M property — verbatim | **Covered** | 无 |
| **Equipment AR** | Full value | ✅ Full value — verbatim | **Covered** | 无 |
| **TPL** | USD 10M/occ | ✅ USD 10M/occ — verbatim | **Covered** | 无 |
| **Pollution** | USD 10M/occ | ✅ USD 10M/occ — verbatim | **Covered** | 无 |
| **Additional Insured** | ✅ Required | ✅ Required — Wison + ADNOC as co-insured | **Covered** | 无 |
| **Waiver of Subrogation** | ✅ Required | ✅ Required — against Owner Indemnified Parties | **Covered** | 无 |
| **Deductibles** | Subcon bears own | ✅ Subcon bears own — verbatim | **Covered** | 无 |
| **Sub-sub flow-down** | Required (41.11) | ✅ Required — same level or covered under Subcon policies | **Covered** | 无 |
| **CAR (by ADNOC)** | ADNOC provides | ✅ Acknowledged — Subcon named as insured under Company CAR | **Covered** | 无 |
| **Insurance Declaration** | At PAC (41.16(e)) | ✅ Required from Subcon | **Covered** | 无 |
| **Insurer Rating** | S&P/AM Best ≥ A− | ✅ Required — insurers qualified & acceptable to Owner | **Covered** | 无 |
| **Certificates** | On request | ✅ On request — verbatim | **Covered** | 无 |

> **结论：保险是迄今 Back-to-Back 最完整的域。** 分包合同逐字复制了 Art 41 的所有条款，仅替换了 party names。**无 Gap、无 Partial——全部 Covered。**

---

## Round 4 — Commercial Exposure（如果某层缺了，谁亏？）

| 情景 | EPC | 分包 | 敞口归谁 | 量化 |
|---|---|---|---|---|
| 分包未投保 TPL | ✅ Wison 有 | ❌ 分包无 | **Wison** (Art 41.12 indemnity for shortfall) | USD 10M/occ + 法律费用 |
| Wison 未投保 TPL | ❌ | ✅ 分包有 | **Wison** — ADNOC 可自行投保并追偿 (Art 41.10) | 保费 + 可能 termination |
| CAR 免赔额触发 | ADNOC 提供但免赔 | — | **Wison** (Art 41.16(c)) | 免赔额具体数值 ⚪ 待提取（取决于 ADNOC 与保险公司 tender 结果·ANX7-1 §10） |
| Wison 的 vitiating act 使 CAR 失效 | ADNOC 无法获赔 | — | **Wison** — 全额 indemnify ADNOC (Art 41.16(d)) | **USD 686M**（整个 Agreement Price） |
| PAC 后保险未过渡 | ADNOC 运营险未生效 | — | **Wison** — 承担 gap 期间全部损失 (Art 41.16(e)) | 取决于 gap 时长 |

> **最大敞口（CRITICAL）**：Art 41.16(d)——Wison 的任何作为或不作为导致 CAR 保险失效→ Wison 赔偿 ADNOC 全部无法获赔的损失。这是 USD 686M 级别的敞口。

---

## Round 5 — Decision Rule（可执行规则）

```yaml
Rule ID:     RULE-005 (候选)
Name:        Insurance Gap — 保险覆盖完整性检查
Capability:  C3 (Requirement) · C7 (Pass-through)
Risk Type:   Insurance
Trigger:     新分包合同签署 OR 现有分包合同续保周期 OR PAC 临近
Condition:
  FOR each insurance type (WC / Motor / Equipment / TPL / Pollution):
    IF EPC.required = TRUE
    AND Subcon.procured = TRUE
    AND Subcon.limit >= EPC.limit
    AND Subcon.additional_insured = TRUE
    AND Subcon.waiver_subrogation = TRUE
    THEN → Covered

    IF Subcon.procured = FALSE
    THEN → CRITICAL: Uncovered Insurance Exposure
          → Wison bears full risk per Art 41.12

    IF Subcon.procured = TRUE AND (limit < EPC.limit OR no waiver OR no additional insured)
    THEN → HIGH: Partial Insurance Exposure

  Special check: CAR deductibles
    IF CAR claim occurs → Wison bears deductible
    → Ensure deductible amount is known and reserved

  Special check: Insurance Declaration at PAC
    IF PAC approaching AND Insurance Declaration not submitted
    THEN → MEDIUM: PAC may be delayed
Decision:
  - All 5 types + all clauses → Covered ✅
  - Missing type → CRITICAL ⚠
  - Weaker terms → HIGH ⚠
Evidence:
  - Insurance certificates (all 5 types × 5 subs = 25 certificates)
  - Policy wordings (确认 waiver of subrogation + additional insured clauses)
  - CAR deductible schedule (ANX7-1 §10 ⚪ 待 ADNOC tender 结果)
  - Insurance Declaration form (ANX7-3) at PAC
Risk Level: CRITICAL (if uncovered) / MEDIUM (certificates not verified)
```

---

## Confidence 分解

```
Clause Mapping      █████████░  95%  Art 41 全文 · ANX7-1 §1-12 · ANX7-3 · 分包 5/5 Insurance Requirements
Evidence Mapping    ████░░░░░░  35%  条款要求已知 · 实际保险凭证未收集 ⚪
Runtime Mapping     ██████░░░░  62%  Back-to-Back 比对可执行 · 无证书验证
Issue Validation    ██░░░░░░░░  20%  无 Insurance Claim 事件
─────────────────────────────────
Overall Confidence  ███████░░░  71%
```

---

## Actions
1. **[本周·CRITICAL]** 确认现有保险凭证——5 家分包商 × 5 种保险 = 25 份凭证是否齐全且在有效期内
2. **[本周]** 获取 ADNOC CAR 保单当前的免赔额表（ANX7-1 §10——取决于 competitive tender，非固定值）
3. **[PAC 前 6 个月]** 启动 Insurance Declaration (ANX7-3) 准备——施工→运营保险过渡
4. **[流程]** 建立保险到期日历——每份保单到期前 60 天提醒续保（Art 41.17(c): 取消通知须提前 30 天给 Company）
5. **[监控]** Art 41.16(d) 敞口——确保 Wison 及分包商不触发 CAR 保单的 vitiating act

## Debt Repaid
- [x] **CD-010** — DNA-9 Insurance Full Gap：Art 41 + ANX7 已制造，保险 Back-to-Back 已映射
- [x] **CF-005** — Insurance Confidence Debt：Coverage 从 <20% → 78%
