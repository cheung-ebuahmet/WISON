# Exposure — 概念模型 / Concept Model
`[Phase 2 · 一级对象 · R4 核心 · 先概念后字段]`

> ★ **核心定位：Contract Manager 每天真正管理的不是 Clause，而是 Exposure（风险暴露）。**
> Exposure = 某项 Risk 在"Main Contract 承担 vs 是否已 Pass-through 覆盖"之间的**净敞口**。

## 是什么 / What
一条 Risk 从主合同落到 Wison 后，减去已通过 External Contract / 保险 / 保函覆盖的部分，剩下的就是 **Exposure**——Wison 实际自留、要花钱或担责的风险。

## 类型 / Types（Canonical，清单可扩展）
`Delay Exposure · LD Exposure · Warranty Exposure · Quality Exposure · Sanction Exposure · Export Exposure · Jurisdiction Exposure · Payment Exposure · Insurance Exposure …`

## 关系 / Relations
```
Main Contract  ─allocates─▶  Risk  ─exposes-to─▶  Exposure
Exposure       ─covered-by─▶  External Contract / Insurance / Guarantee     （覆盖 → 敞口↓）
Risk           ─retained-by─▶ Wison                                          （未覆盖 → Uncovered Exposure）
```

## 状态 / State
`Covered`（已对等流转/已保险） · `Partially Covered`（流转更弱，如 Warranty 12→6mo） · `Uncovered`（自留） · `Crystallised`（已发生，转为实际损失/Claim）。

## 与规则的关系 / Rules
**所有 03_Rules 围绕 Exposure。** 典型：
```
IF  Main Contract 有 LD  AND  External Contract 无对应 LD
THEN Exposure = Uncovered Commercial Exposure（Wison 承担）  →  提示 + 入 Risk Register
```

## 与能力 / Capabilities
直接支撑 **C7 Risk Pass-through Verification**：给出主合同某条款 → 判定其 Exposure 是 Covered / Partial / Uncovered，并指出缺口。

## 待项目实例化 / To instantiate（→ PROFILE / COMMERCIAL_DNA）
- 本项目实际存在哪些 Exposure（LSTK 下通常 Delay/LD/Warranty/Sanction/Export 最重）
- 各 Exposure 的覆盖来源与缺口（Risk Register）

_只定概念，不填项目数值。_
