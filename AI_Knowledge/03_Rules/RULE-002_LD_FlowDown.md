# RULE-002 — LD Flow-down (Back-to-Back)
`[v0.2 首批规则 · Capability C7 · Risk: Commercial · CRITICAL]`

```yaml
Rule ID:     RULE-002
Name:        LD Flow-down — 主合同 LD 是否已流转到 External Contract
Capability:  C7 (Risk Pass-through 验证)
Risk Type:   Commercial
Trigger:     存在 Main Contract 的 LD 义务（ANX5 A.09 · FOA p.4-5 · GTC Art 18.4）
             AND 存在一份 External Contract（Subcontract / PO / Vendor Agreement）
Condition:
  IF Main Contract.LD.exists = TRUE
  AND External Contract.LD.exists = FALSE
  THEN → Uncovered LD Exposure

  IF Main Contract.LD.exists = TRUE
  AND External Contract.LD.exists = TRUE
  AND External Contract.LD.cap < Main Contract.LD.cap (10%)
  THEN → Partial LD Exposure

  IF Main Contract.LD.exists = TRUE
  AND External Contract.LD.exists = TRUE
  AND External Contract.LD.cap >= Main Contract.LD.cap
  AND External Contract.LD.triggers 覆盖 Main Contract.LD.milestones
  THEN → Covered
Decision:
  - Full absence → CRITICAL: Uncovered Commercial Exposure（Wison 自留全部 LD 风险）
  - Weaker terms → HIGH: Partial Exposure（差额由 Wison 承担）
  - Equivalent   → Covered
Evidence:
  - Main Contract: ANX5 Exh A.09（15 里程碑 · 0.01167%–0.03333%/天 · 总上限 10%Agg）
  - External Contract 中 LD 条款（或缺失证明）
  - FOA p.4-5（LD 里程碑与费率表）
Risk Level: CRITICAL（若无）/ HIGH（若弱于主合同）
Output:     "主合同含 LD：总上限 10% Agg，15 个里程碑各有日费率与单上限。
            External Contract [名称] 中 [无 LD 条款 / LD 上限仅 X% / 未覆盖里程碑 Y]。
            → [Uncovered / Partial] LD Exposure — Wison 承担 [全部 / 差额] 延误赔偿风险。"
Action:
  1. [立即] 将该 Exposure 录入 Risk Register，指定 Owner
  2. [本周] 评估能否在 External Contract 中补入 LD 条款（如尚未签署）
  3. [监控] 如分包已签且无法修改 → 该敞口须在项目执行中持续监控（P5：认领并管理）
Clause:      Main: ANX5 Exh A.09 · FOA p.4-5 · GTC Art 18.4
             Flow-down 义务: GTC Art 20.3 (Contractor 对 Subcontractor 全部行为承担全部责任)
DNA Zone:    DNA-6 (LD) · DNA B (Art 20 B2B 法律基础)
```

---

## 商业背景 / Why this rule matters
这是 C7 Risk Pass-through 的旗舰规则。主合同有 10% Agg LD，如果分包合同完全没有 LD——这意味着任何分包造成的延误，Wison 对 ADNOC 要赔 LD，但对分包商无法 back-to-back 追偿。这是最典型的 Uncovered Commercial Exposure，也是 Contract Manager 签任何下游合同前必须扫的第一条。
