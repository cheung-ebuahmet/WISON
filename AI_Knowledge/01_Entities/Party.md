# Party — 概念模型 / Concept Model
`[Phase 2 · 先概念，后字段 · 具体人/组织去 PROFILE.md]`

> ★ **核心定位：Party 是项目里一切 Event 与 Decision 的"施动者"，也是权限与责任的载体。**
> Party 的价值不在"名录"，而在回答两类问题：**谁有权做这件事？谁该为这件事负责？**

## 结构 / Structure（四层 + 两个横切概念）
```
Organization ─has─▶ Role ─holds─▶ Authority ─(经 Delegation)─▶ Person
                     │
                     └─responsible-for─▶ Requirement        (Accountability)
Authority ─受─▶ Authority Constraint                         (条件/阈值)
```

| 层 | 是什么 | 参与推理 |
|---|---|---|
| **Organization** | 现实公司/机构（ADNOC、Wison、Engineer公司、Vendor） | 是 |
| **Role** | 合同身份 = 权限载体（Employer/Engineer/Contractor/Subcontractor/Vendor/Consultant/Authority） | 是（首选） |
| **Authority** | **可做什么**（签发 Instruction / 认定 Variation / 审批 Payment / 签发 Completion / 回复 Claim / 签发 NCR），带生命周期与限制 | 是 |
| **Person** | Role 的具名实例（张三）。**默认不参与推理**，只在追溯"谁签/谁授权/谁发信"时用 | 否（默认） |

**推理优先级**：永远先 `Role`；`Person` 只用于溯源。人换、Role 不变、知识库不动。

## Authority（一级对象，非 Role 的属性）
Authority 有自己的生命周期与维度：`永久/临时` · `金额上限` · `专业范围` · `需联签` · `可委托(Delegation)` · `可撤销(revoke)`。
> "PM 能不能批 500 万美元的 Variation？"——这不是 Role 能答的，是 Authority（含金额上限 + 是否需联签/上批）。

## Authority Constraint（约束，独立，不写死）
```
Engineer  can  Issue Instruction
   BUT  Instruction  requires  Employer Approval   IF  Cost Impact > Threshold
Engineer  may  Assess Claim ；Final Approval = Employer
```
存在性属 Canonical；阈值/清单属 `PROFILE.md`（ADNOC 的具体门槛在那里配）。

## Delegation（授权链）
```
Director ─delegates(≤$500k)─▶ Construction Manager
```
决定 Decision 是否**合法**：`作出者是否持有（含委托来的）对应 Authority 且满足 Constraint`。
→ "为什么这签字有效？—— Delegation No. xxxx。"

## Accountability（责任）
```
Role  responsible-for  Requirement
QA Manager → NCR Close ; Contracts Manager → Claim Notice ; CM → Site Progress
```
→ "谁该发 Notice？"直接查，不搜合同。

## 与 Decision 的闭环 / Link to Decision
> **一个 Decision 有效 ⇔ 其作出者的 Role 持有对应 Authority（含 Delegation）且满足 Constraint。**
> 否则 Decision 无效、不改变 State。这让"这个 VO 为什么无效？——批的人没权限"成为可推理结论。

## 待项目实例化 / To instantiate（→ PROFILE.md）
- 本项目各 Organization ↔ Role 映射（ADNOC 哪家任 Employer、Engineer 是否第三方/PMC）
- 各 Role 的 Authority 阈值与联签规则
- Engineer 受限行为清单（哪些 `requires Employer approval`）
- 关键 Delegation（谁授权谁、限额）

_本文件只定概念，不填具名人员与项目阈值。_
