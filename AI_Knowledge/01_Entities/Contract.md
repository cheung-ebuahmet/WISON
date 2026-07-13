# Contract — 概念模型 / Concept Model
`[Phase 2 · 先概念，后字段 · 无项目数值（数值去 PROFILE.md）]`

> ★ **核心定位：Contract 不只是法律文件，而是整个项目的"约束系统 (Constraint System)"。**
> 它在专家系统中的职责**不是"存放条款"**，而是：
> 1. 定义参与方的**权利与义务**；
> 2. **分配风险**；
> 3. 建立**时间 / 成本 / 质量 / 安全**约束；
> 4. 规定**事件发生后的响应机制**（通知 / 变更 / 索赔 / 付款 / 争议）；
> 5. 为所有下游对象（Subcontract / PO / Variation / Claim / Payment / Decision）提供**规则来源**。
>
> ⚑ **本质（R4）**：Contract 是 **Risk Allocation 的载体**——它真正的产出是把 `Risk / Exposure` 分配给各方。Commercial Manager 管的是这些 Risk 是否被 Back-to-Back 覆盖（见 [`Exposure.md`](Exposure.md)），而非条款字面。

**专家思维主脉（本模型的设计目标）：**
```
Contract 定义规则 → Event 触发变化 → Decision 作出判断 → Rule 验证条件 → Object 更新状态 → Case 沉淀经验
```

---

## ① 是什么 / What
一组互相约束的**承诺集合**，把双方的义务、风险、时间、金钱绑定，并预先规定"现实偏离计划时如何调整、如何终局"。它是所有下游对象的**根（rules source）**。

## ② 产生什么 / generates
```
Contract
 ├─ generates ─▶ Requirement   （超类：Obligation / HSE / Quality / Insurance / Bond 皆是；状态 Satisfied|Outstanding）
 ├─ generates ─▶ Risk
 ├─ generates ─▶ Time          （基准工期 / Milestones）
 ├─ enables   ─▶ Payment       （付款权利）
 ├─ enables   ─▶ Variation     （变更机制）
 ├─ enables   ─▶ Claim         （索赔机制）
 └─ requires  ─▶ Guarantee / Insurance
```
> 关键：Contract 产生的是 **Requirement**，`Obligation` 只是其一种——这样 HSE/Quality/Insurance/Bond 的"要求—满足"状态可统一追踪。

## ③ 依赖什么 / depends-on
`Party`（Employer / Engineer / Contractor 角色） · `Scope` · `Definitions` · `Applicable Law` · **Order of Precedence**（一级关系） · **生效锚点**（Milestone Events）。

## ④ 生命周期 / Lifecycle（State × Event）
```
State:  Tendering ─▶ Awarded ─▶ Executing ─▶ Completed ─▶ Warranty ─▶ Closed
Event:      Award      NTP        (VO/Claim…)    MC/PAC       FAC        Closeout
```
- **Event 改变 State**；State 内不写 Event。
- 当前态靠"最近 Event + 尚未发生的 Event"推断（有 NTP 无 PAC → Executing，Warranty 未起算）。
- `Amendment` 可在任意点 `supersedes` 旧版——留版本，不覆盖。

---

## 边界 / Boundary（Contract Package）
Contract = **Contract Package（组合体）**，非单一 PDF：
```
Contract Package ─contains─▶ Document ─contains─▶ Clause
Document ∈ {Agreement, LOA, Acceptance, PCC, GCC, Scope, Spec, Drawings, BOQ, Exhibits, Clarifications, Amendments}
```
Clause 定位 = `Package ▸ Document ▸ Clause No.`

## 生效锚点 / Effective anchors（多个，可不同日 → 由 PROFILE 决定）
```
LOA → Contract Signing → Effective Date → NTP → Commencement → Site Access
```
哪个 Event 触发 **生效 / 起算工期 / 起算付款 / 起算保险 / 起算 Warranty**：见 [`PROFILE.md`](../PROFILE.md)。

---

## 待项目实例化 / To instantiate（→ PROFILE.md，Phase 3 读合同 / Phase 4 访谈填）
- 本项目 Contract Package 实际含哪些 Document
- 本项目 Order of Precedence 实际顺序
- 本项目各"起算"锚点分别是哪个 Event
- 本项目采用哪些完工里程碑（MC / Taking Over / PAC / FAC …）

_本文件只定概念，不填数值。数值有出处、留版本（宪法第一、二、六条）。_
