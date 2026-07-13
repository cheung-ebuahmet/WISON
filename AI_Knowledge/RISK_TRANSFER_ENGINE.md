# RISK_TRANSFER_ENGINE — 风险转移引擎 / Risk Transfer Engine
`[v0.3.2 · 第一版 · 保险为第一阶段 · 可复用于 Warranty/Testing/Acceptance/Performance]`

> **这不是一个新的引擎。这是已有四个引擎（Knowledge → Rule → Mapping → Confidence）在"风险转移"这个商业视角下的协同运转。**
>
> 对 EPC 总包来说，Insurance 不是独立模块——它是 **Risk Allocation 最后的保障层**。保险前面还有三层：合同 indemnity → 分包 Flow-down → 保函。保险是第四层——前三层都失效时的最后兜底。
>
> **本引擎的职责**：追踪每项风险在四层保障链中的落点，回答"这个风险最终由谁买单"。

---

## 风险转移四层链 / The 4-Layer Risk Transfer Chain

```
Risk (e.g. Property Damage from Storm)
  │
  ├── Layer 1: Contractual Indemnity
  │     Who bears it under the EPC contract? → Art 42
  │     Covered? → Yes: Contractor indemnifies Company
  │
  ├── Layer 2: Subcontract Flow-down
  │     Has it been passed to a Subcontractor? → Art 20
  │     Covered? → Partial: Civil may not cover weather damage
  │
  ├── Layer 3: Security / Guarantees
  │     Is there a bond/guarantee backing it? → Art 30
  │     Covered? → No: PBG/PCG don't cover weather
  │
  └── Layer 4: Insurance ★ ← 本阶段聚焦
        Is there a policy? Who pays the deductible?
        Covered? → CAR (by ADNOC) covers physical damage
                   but deductible borne by Contractor
        → Net Risk to Wison = Deductible Amount
```

---

## 保险在四层链中的位置 / Insurance Position

```
Layer 1: Indemnity     —— EPC 合同约定"谁赔谁"
Layer 2: Flow-down     —— 分包是否承接同一义务
Layer 3: Security      —— 保函是否覆盖
Layer 4: Insurance ★   —— 保单是否兜底
         ├── Who procures?
         ├── Who pays premium?
         ├── Who bears deductible?
         ├── Who is insured?
         └── Who files/manages claim?
```

---

## Risk Transfer Matrix / 风险转移矩阵

> **商业经理每天看的就是这张表。** 每项风险追踪它在四层链中的落点，最终回答"这个风险有没有人买单"。

| # | 风险 | Layer 1 Indemnity | Layer 2 Flow-down | Layer 3 Security | Layer 4 Insurance | 最终承担方 | 闭环 |
|---|---|---|---|---|---|---|---|
| R1 | Property Damage (storm/fire) | Contractor → Company | Partial (Civil scope gap) | ❌ | **CAR** (ADNOC, deductible=Wison) | **Wison** (deductible) | ⚠ |
| R2 | Third Party Bodily Injury | Contractor indemnifies | ✅ (TPL verbatim) | ❌ | **TPL** (Wison, USD 10M) | Insurance | ✅ |
| R3 | Worker Injury/Death | Contractor indemnifies | ✅ (WC verbatim) | ❌ | **WC** (Wison, USD 1M) | Insurance | ✅ |
| R4 | Pollution from Contractor Ops | Contractor indemnifies | ✅ (Pollution verbatim) | ❌ | **Pollution** (Wison, USD 10M) | Insurance | ✅ |
| R5 | Motor Vehicle Accident | Contractor indemnifies | ✅ (Motor verbatim) | ❌ | **Motor TPL** (Wison, USD 1M) | Insurance | ✅ |
| R6 | Damage to Contractor Equipment | Contractor bears | ✅ (Equipment AR verbatim) | ❌ | **Equipment AR** (Wison, full value) | Insurance | ✅ |
| R7 | Damage to Existing ADNOC Property | Contractor indemnifies (capped USD 1M/occ) | Partial | ❌ | **CAR — Existing Property** (ADNOC, USD 20M) | Insurance (above USD 1M) | ⚠ |
| R8 | Design Defect (LEG 3) | Contractor bears | Partial (design sub risk) | ❌ | **CAR — LEG 3 extension** (ADNOC) | Insurance | ✅ |
| R9 | Terrorism | Contractor (FM → EOT only) | Partial | ❌ | **CAR — Terrorism** (ADNOC) | Insurance | ✅ |
| R10 | CAR Deductible | — | — | — | **Wison** (Art 41.16(c)) | **Wison** | ❌ |
| R11 | CAR Policy Vitation | — | — | — | **Wison** — full indemnity (Art 41.16(d)) | **Wison** | ❌ |
| R12 | Post-PAC Insurance Gap | — | — | — | **Wison** — ensure transition (Art 41.16(e)) | **Wison** | ❌ |

---

## Insurance Risk Posture（保险域）

```
Total Insurance-related Risks: 12
  ✅ Closed (fully transferred):      6  (R2–R6, R8)
  ⚠ Partial (Wison retains tail):     3  (R1, R7, R9)
  ❌ Retained (Wison bears fully):     3  (R10, R11, R12)
─────────────────────────────────────────
Risk Closure Rate: 50% (6/12 closed)
```

---

## 跨域扩展性 / Applicability to Other Domains

**本引擎的框架（四层链 + 风险转移矩阵）可直接复用于：**

| 域 | Layer 1 | Layer 2 | Layer 3 | Layer 4 | 状态 |
|---|---|---|---|---|---|
| **Insurance** | ✅ Art 42 | ✅ Art 20/41.11 | ✅ Art 30 | ✅ Art 41/ANX7 | 🟢 Active (v0.3.2) |
| **Acceptance** | ✅ Art 15/17 | 🟡 Civil WC≠EPC PAC | ✅ Art 30 | ⚠ CAR transition gap | 🟡 Active (v0.3.3) |
| Warranty | ✅ Art 17/22 | 🟡 已映射 · 时间差敞口 | ✅ Art 30 | ❌ 无保险覆盖 | 🟡 |
| Performance | ✅ Art 16 | ⚪ 待映射 | ✅ Art 30 | ⚪ | ⚪ |
| Testing | ✅ Art 13/16 | ⚪ | ❌ | ⚪ | ⚪ |
| Delay LD | ✅ Art 18 | ✅ RULE-002 | ❌ | ❌ | 🟢 Active |

---

## Decision Rule — Risk Transfer 版 / Upgraded Rule Pattern

未来规则不再只是"有没有保险"，而是：

```yaml
IF
  Risk exists (from Contract DNA)
  AND Layer 1 (Indemnity) = Contractor
  AND Layer 2 (Flow-down) = Missing OR Partial
  AND Layer 3 (Security) = Not Applicable
  AND Layer 4 (Insurance) = Missing OR Partial
THEN
  Exposure = HIGH or CRITICAL
  Action = "此风险四层全裸——须在签分包/续保前解决"
  Recommend = "优先 Flow-down（最便宜）> 其次保险（可保的话）> 最后自留（需明确预算）"
```

---

## v0.3.3 门 / Gate (Stage 2: Acceptance)
- [x] Acceptance_Mapping 完成 — Event→Effect chain · PAC/FAC blocker analysis
- [x] 分包验收对比 — Civil WC vs MEI PA vs EPC PAC timing gaps quantified
- [x] Cross-Domain Conflict Engine 启用 — 5 个冲突识别
- [ ] CF-AC-001/004 Mitigation Strategy（v0.3.x）
- [ ] Civil WC→PAC gap 实际时长数据（需项目进度数据）
