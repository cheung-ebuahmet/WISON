# RULE-003 — Warranty Gap (Back-to-Back)
`[v0.2 首批规则 · Capability C7 · Risk: Commercial · HIGH]`

```yaml
Rule ID:     RULE-003
Name:        Warranty Gap — 主合同与 External Contract 质保期差异
Capability:  C7 (Risk Pass-through 验证)
Risk Type:   Commercial
Trigger:     存在 Main Contract WARRANTY PERIOD
             AND 存在一份 External Contract 含 warranty/缺陷责任条款
Condition:
  IF Main Contract.Warranty = 12 months (FOA p.5)
  AND External Contract.Warranty < 12 months
  THEN → Warranty Gap = 12 - External Contract.Warranty（月数）
       → Partial Warranty Exposure（差额期间 Wison 对 ADNOC 有责、对分包无追索权）

  IF Main Contract.Warranty = 12 months
  AND External Contract.Warranty >= 12 months
  AND External Contract.Warranty.start = PAC/ETC（对齐主合同起算点）
  THEN → Covered

  IF External Contract 无 Warranty 条款
  THEN → Uncovered Warranty Exposure
Decision:
  - Gap = N months → HIGH: Partial Exposure（差额期间缺陷返工由 Wison 承担）
  - No warranty   → CRITICAL: Uncovered Exposure
  - Equivalent    → Covered
Evidence:
  - Main Contract Warranty: FOA p.5（12 months from ETC/Partial PAC/PAC）
  - External Contract warranty clause（期限 + 起算点）
Risk Level: HIGH（有 Gap）/ CRITICAL（无 Warranty）
Output:     "主合同质保期 = 12 个月（自 ETC/PAC 起算）。
            External Contract [名称] 质保期 = [X] 个月。
            → Warranty Gap = [12-X] 个月 — Partial Warranty Exposure。
            Gap 期间出现的缺陷，Wison 对 ADNOC 承担修复责任，但无法向该分包商追偿。"
Action:
  1. [立即] 入 Risk Register
  2. [本周] 评估：该分包商的 work scope 在 Gap 期间出现缺陷的概率与修复成本
  3. [谈判] 如分包未签，争取将 Warranty 对齐到 12 个月
  4. [监控] 如已签，在 Gap 期间安排专项检查/预留 contingency
Clause:      Main: FOA p.5 · GTC Art 17 · Art 30.2(c)
             Flow-down 义务: GTC Art 20.3
DNA Zone:    DNA-10 (Warranty/DLP) · DNA B (Art 20 B2B)
```

---

## 商业背景 / Why this rule matters
12 个月 vs 6 个月——表面差 6 个月，实际差的是整个 DLP 后半段的缺陷风险。许多分包商（尤其设备供应商）的标准质保是 6–12 个月，但起算点往往是"交货"而非"PAC"——这意味着实际覆盖期可能比主合同要求的短得多。这是 Warranty Exposure 的核心来源。
