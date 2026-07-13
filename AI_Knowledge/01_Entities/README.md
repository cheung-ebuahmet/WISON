# 01_Entities — 知识对象 / Knowledge Objects

**核心思想**：AI 学的不是 PDF，是**对象**。每个对象是一组字段，PDF 只是某字段值的出处（citation）。
每个实体建议一个文件：`Contract-<编号>.md`、`VO-<编号>.md` …，字段用 YAML frontmatter，正文写要点+引用。

> 下面是**字段草案**（来自你的蓝图），待你确认/增删后定为正式 schema。合同具体数值一律留空，一起填。

> **本体决策（Phase 1）对实体的影响**（Phase 2 展开）：
> - `Party` 拆为 **Organization（谁）× Role（合同角色/权限）**——见 `ONTOLOGY.md §2`。
> - 新增 **Event（事件）** 作为一等实体：Contract Award / NTP / Instruction / VO Approval / PAC / FAC …，是推理链 `Event→Object→State→Rule→Action` 的起点。
> - `Procurement` 域实体（RFQ/PO/Vendor/FAT/Delivery…）与 `HSE/Quality` 域实体（NCR/CAR/PAR/Permit…）均为独立域，非 Contract 子对象。
> - 新增 **Requirement（超类）**：Contract 产生的是 Requirement，`Obligation` 仅是其一种；统一 HSE/Quality/Insurance/Bond；状态 `Satisfied|Outstanding`。
> - 新增 **Decision（判断）**：由 Role 作出（Approve/Reject/Determine），带 Reason+Evidence(Clause)，改变 State——见 `ONTOLOGY.md §6`。
> - **Contract = Contract Package**：`Package → contains → Document → contains → Clause`；`State` 与 `Event` 分层（Event 改变 State）。
> - 📄 Contract 概念模型已建：见 [`Contract.md`](Contract.md)。项目具体取值去 [`PROFILE.md`](../PROFILE.md)。
> - 新增 **Authority（一级对象）/ Authority Constraint / Delegation / Person**：Party 的权限层——`Role holds Authority authorizes Decision`；`Person` 是 Role 实例、默认不参与推理。
> - 新增 **Accountability 关系**：`Role responsible-for Requirement`（谁该发 Notice / 关 NCR）。
> - 📄 Party 概念模型已建：见 [`Party.md`](Party.md)。

## Contract（主合同）
```
编号 / Contract No.
名称 / Title
双方 / Parties (Employer, Contractor)
合同金额 / Contract Price
开始日期 / Commencement Date
完成日期 / Completion Date
LD（误期赔偿：费率/上限）
Retention（质保金：比例/释放）
Advance Payment（预付款：比例/担保/回扣）
Variation（变更机制条款号）
Claims（索赔条款号 + 通知时限）
Termination（终止条款号）
Insurance（险种/保额）
Applicable Law（适用法）
Dispute（争议解决：DAB/仲裁/法院）
出处 / Source (原始文件路径 + 条款号)
```

## Subcontract（分包合同）
```
包名称 / Package
Scope（工作范围）
Back-to-Back（与主合同流转情况）
Risk（风险分配）
Payment（付款条件）
LD / Warranty / Insurance / Guarantee
Notice（通知义务/时限）
Claims（索赔机制）
出处 / Source
```

## Variation（变更）
```
编号 / VO No.
来源 / Origin（谁发起）
原因 / Reason
影响 / Impact
Cost（费用影响）
Time（工期影响）
Status（状态：Instruction / Estimate / Approval / Executed / Paid）
Evidence（证据）
Notice（是否已发通知/时限）
Approval（审批人/是否已批）
Payment（是否可付/已付）
出处 / Source
```

## Claim（索赔）
```
编号 / Claim No.
性质 / Type（EOT / Cost / both）
事件 / Event + 日期
通知 / Notice（是否在时限内、Time-bar）
详细索赔 / Detailed Claim（是否提交）
同期记录 / Contemporary Records
金额/工期主张、状态、结果、出处
```

## 其他实体（同样字段化）
`Payment`(进度/里程碑/发票/证书/付款期/Retention/Advance) ·
`Party`(业主/承包商/分包/供应商) · `Insurance` · `Guarantee/Bond`(APG/PBG/银行保函) · `Notice`(时限台账)
