# ADVANTAGE_LIBRARY — 商业优势模式库 / Commercial Advantage Library
`[v0.3.6 · 不止管理风险——管理优势 · 总包商业优化的正向知识]`

> **传统合同管理只找风险。优秀总包管理寻找优势。**
> 每个 Advantage Pattern = 一个已被验证的"Wison 比主合同要求更有利"的位置。
> 这不是 Gap——这是 **Inverse Mapping** 的商业价值兑现。

---

## 优势模式库 / Advantage Library

### ADV-001 · Subcontract LD > EPC LD — Margin Protection ✅ Validated

```
Pattern ID:     ADV-001
Status:         ✅ Validated (LD_Mapping — 3/3 分包验证)
Domain:         LD
Value Type:     Margin Protection（利润保护）

Position:
  EPC LD:    0.01167%–0.03333% / day (15 milestones, Cap 10%)
  Subcon LD: 0.1% / day (all 3 subs, Cap 10%)
  Ratio:     ~8.6× (subcon min) to ~3× (subcon max)

Commercial Logic:
  分包延误 → Wison 从分包收取 AED 150K–162K/天
  → Wison 向 ADNOC 支付 ~USD 80K–228K/天（取决于延误的里程碑）
  → 净效应取决于具体里程碑对价——但费率差为 Wison 提供了管理缓冲

Action to Preserve:
  1. 不主动修改分包 LD 费率（这是已 locked-in 的优势）
  2. 新分包谈判中，LD 费率不低于 EPC 对应里程碑费率
  3. 监控 12.1 MC Relief——若按期 MC 则前期 LD 退还，此优势暂时失效

Related Mapping:  LD_Mapping
Related Rule:     RULE-002 (LD Flow-down)
```

### ADV-002 · Payment Float — Cash Flow Advantage ✅ Validated

```
Pattern ID:     ADV-002
Status:         ✅ Validated (Payment_Mapping — 3/3 分包验证)
Domain:         Payment
Value Type:     Cash Flow Protection（现金流优势）

Position:
  EPC Payment:  30 days from valid invoice (Art 23.2(b))
  Subcon Pay:   45 days from correct invoice (COC Art 11 · SCS Clause 19)
  Float:        15 days

Commercial Logic:
  Wison 从 ADNOC 收款（30d）→ 15 天后再付分包（45d）
  → 正向现金流——Wison 不必垫资
  → 若项目月度 IPC 约 USD 15M，15 天 float 价值 ≈ USD 7.5M 平均余额

Action to Preserve:
  1. 新分包谈判中保持 45d 付款周期（不低于 EPC 30d）
  2. 实际执行中确保 ADNOC 付款到账后再释放分包 IPC
  3. 监控：若 ADNOC 延迟付款 → 分包 45d 倒计时从 ADNOC 到账日起算

Related Mapping:  Payment_Mapping
Related Rule:     RULE-004 (Payment Precondition)
```

### ADV-003 · KP-LD — Self-Created Downstream Control ✅ Validated

```
Pattern ID:     ADV-003
Status:         ✅ Validated (KP_Mapping — 2/2 分包全有人名+LD)
Domain:         KP / Authority
Value Type:     Management Leverage（管理杠杆）

Position:
  EPC:          No KP-LD mechanism（ADNOC 通过 PBG + Termination 管理）
  Subcon:       AED 10,000 / person / day × 7 positions
  Annualized:   Up to AED 25.5M / year if all 7 positions vacant

Commercial Logic:
  Wison 在 EPC 主合同没有 KP-LD 义务的情况下，在分包中创设了这个下行管控。
  → 纯收益——对上是零成本，对下是可执行的履约杠杆。
  → 行业智慧：把主合同的管理需求，转化为对下的合同条款。

Action to Preserve:
  1. 新分包持续加入 KP-LD（7 positions × AED 10K/day）
  2. 严格执行——PM 缺位即触发，不发 Notice 即失去威慑力
  3. 监控 Wison 自身 KP 稳定性——Art 19 虽无 LD 但有 Termination 风险

Related Mapping:  KP_Mapping
Related Issue:    EVENT-002 (PM 缺位 · AED 10K/day 已触发)
```

### ADV-004 · Advance Payment Staging — Risk Reduction ✅ Validated

```
Pattern ID:     ADV-004
Status:         ✅ Validated (Payment_Mapping — 12.1 MEI)
Domain:         Payment / Security
Value Type:     Risk Reduction（风险降低）

Position:
  EPC Advance:  10% — 一次性释放（凭 APG）
  12.1 MEI:     10% — 分 2 期释放（50% on APG+PB · 50% on mobilization complete）

Commercial Logic:
  Wison 从 ADNOC 收到 10% 预付（一次性）→ 仅需先释放 5% 给 12.1
  → 另 5% 锁在分包动员完成之后
  → 降低了分包预付款风险——若 12.1 未按期动员，Wison 不必释放第二期

Action to Preserve:
  1. 新分包谈判中争取预付款分期（与关键履约节点挂钩）
  2. 监控 12.1 动员进度——第二期释放的触发条件

Related Mapping:  Payment_Mapping
```

### ADV-005 · Insurance B2B — Cleanest Pass-Through ✅ Validated

```
Pattern ID:     ADV-005
Status:         ✅ Validated (Insurance_Mapping — 5/5 分包 verbatim)
Domain:         Insurance
Value Type:     Structural Integrity（结构完整）

Position:
  All 12 insurance clauses in all 5 subcontracts = verbatim Art 41.
  Zero gaps. Zero partials. 100% Covered.

Commercial Logic:
  保险是迄今 Back-to-Back 最完整的域——因为分包 Ins Requirements
  直接引用主合同 Art 41 全文。这意味着保险敞口的法律基础是零。
  （证据层——实际凭证——仍是 Confidence Debt，但条款层 100% clean。）

Action to Preserve:
  1. 保持新分包 Insurance Requirements 的 verbatim 结构
  2. 定期验证实际保险凭证 ≠ 仅信条款

Related Mapping:  Insurance_Mapping
```

---

## 优势统计 / Advantage Stats

| 指标 | 值 |
|---|---|
| Total Advantages | **5** |
| Validated | 5 |
| Value Types | Margin Protection (1) · Cash Flow (1) · Leverage (1) · Risk Reduction (1) · Structural Integrity (1) |
| Mapped to | LD · Payment · KP · Insurance |
| Monetizable | ADV-001 (LD 费率差 ≈ management buffer) · ADV-002 (15d float ≈ USD 7.5M avg balance) |

---

## 优势 vs 风险的平衡 / Advantage-Risk Balance

```
商业位置总览：

  ADVANTAGES (Wison 比主合同更有利):
    ADV-001  LD 费率差       🟢 Margin Protection
    ADV-002  Payment Float    🟢 Cash Flow
    ADV-003  KP-LD 下行管控   🟢 Leverage
    ADV-004  Advance Staging  🟢 Risk Reduction
    ADV-005  Insurance B2B    🟢 Structural Integrity

  RISKS (Wison 自留敞口):
    CF-AC-001  Warranty Gap   🔴 4-month exposure
    CF-AC-004  PBG Gap        🔴 2-year exposure
    CF-AC-005  LD Asymmetry   🟡 MC Relief risk
    Art 41.16(d) CAR Vitation 🔴 USD 686M tail risk
```

> **商业经理的日常 = 守住优势 + 管理风险。** 这个库存让系统不只是"防御工具"——它能告诉 Wison 在什么位置是主动方。
