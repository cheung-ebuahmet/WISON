# 04_Processes — 流程 / Processes

**目的**：记录每个业务流程的步骤、时限、审批权限。规则(03)判断"能不能"，流程(04)描述"怎么走"。

## 流程模板 / Template
```
流程名：Variation / Payment / Claim / EOT ...
触发：...
步骤：① … → ② … → ③ …（每步：责任人 / 输入 / 输出 / 时限 / 审批权限）
产出物：...
关联规则：R-xxx
```

## 待建流程 / To build
- **Procurement 流程 ★R5**：`RFQ → Bid → Evaluation → PR → PO → Expediting → Inspection/FAT → Shipping/Customs → Delivery → Warranty`。
  > R5 定位：**采购是一条 Execution 作业流 (Process)，不是知识域**。风险承接逻辑归 `External Contract`（实体），作业步骤归这里。
- **Variation 变更流程**：Instruction → VO Request → Estimate → Approval → Execution → Final Adjustment（标注各步签发权限）。
- **Payment 付款流程**：Progress% / Milestone → Invoice → Engineer Approval → Employer Approval → Payment Certificate → Payment within XX Days。
- **Claim 索赔流程**：事件 → Notice(时限) → Detailed Claim → 评估 → 谈判/裁决。
- **EOT 流程**：延误事件 → 通知 → 申请 → 审核 → 批复。

> 审批权限（谁能签 VO、谁能批付款）单列，是 Back-to-Back 与授权风险的关键。
