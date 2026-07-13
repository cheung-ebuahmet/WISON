# External Contract — 概念模型 / Concept Model
`[Phase 2 · R4 泛化 · 取代原 Procurement.md 计划 · 先概念后字段]`

> ★ **核心定位：一切 Wison 对外的下游合同都是 External Contract。** Contract Manager 只问一个问题：
> **它是否承接了 Main Contract 的风险（Back-to-Back 是否完整）？** ——不问它叫 Subcontract 还是 PO。

## 子类型 / Subtypes（差异属 Profile）
`Subcontract（施工/劳务）· PO（采购）· Vendor/Supplier Contract · Inspection Contract · Rental · Transportation …`
> R4 合并：原 **Procurement**(R1 独立域) 与 **Subcontract**(R2) 统一到此。PO 与 Subcontract **同构**——都是下游风险承接载体。

## 是什么 / What
把 Main Contract 分配给 Wison 的 **Risk / Requirement** 向下转移的载体。理想状态：主合同的每条义务/风险都 `flows-down` 到某个 External Contract；未流转的即 `retained-by` Wison。

## 产生什么 / generates
承接来的 `Requirement`（Warranty/Inspection/HSE/Quality…）· `Payment`(对下付款) · `Variation`(对下变更) · `Claim`(对下索赔) · `Guarantee`(要求 Vendor/Subcon 提供的保函)。

## 生命周期（采购子类型示例）
`RFQ → Bid → Evaluation → PR → PO → Expediting → Inspection/FAT → Shipping/Customs → Delivery → Warranty`
- 检验**双建模**：`Inspection Requirement`（Satisfied/Outstanding） + `FAT Passed/Failed`（Event，改状态、可触发 Notice）。
- Vendor **复用 Party 的 Role=Vendor**（单一事实源，不另造主体）。

## 核心关系 / Relations
```
Main Contract   ─flows-down─▶   External Contract        （风险/义务下传）
External Contract ─purchases-from / subcontracts-to ─▶ Party(Role=Vendor/Subcontractor)
未流转项 ─retained-by─▶ Wison ─exposes-to─▶ Exposure
```

## 与能力 / Capabilities
支撑 **C4 Back-to-Back 完整性** 与 **C7 Pass-through Verification**：逐条比对主合同 vs External Contract，标出 Gap。

## 待项目实例化 / To instantiate（→ PROFILE）
- 本项目有哪些 External Contract、各属什么子类型
- 每份的 Back-to-Back 覆盖情况（对齐 / 更弱 / 缺失）→ 汇入 Risk Register

_只定概念，不填具名分包/供应商。_
