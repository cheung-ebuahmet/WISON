# 03_Rules — 规则引擎 / Rule Engine

**目的**：把合同条款变成 AI 能执行的 IF/THEN 规则。这是"专家系统"的判断核心。

## ★ 首要引擎：Back-to-Back / Pass-through（R4）
规则库的**第一优先**不是解释条款，而是验证风险传递。见到 Main Contract 的 Clause：
```
查 flows-down 到 External Contract？
   无        → Risk retained by Wison → Uncovered Exposure（提示 + 入 Risk Register）
   有但更弱  → High Risk Gap（如 Warranty 12mo vs 6mo，主动提示）
   有且对等  → Covered
```
**所有规则围绕 [`Exposure`](../01_Entities/Exposure.md)**（Covered / Partial / Uncovered）。对应能力 C4 / C7。

## 规则模板 / Rule template
```
规则ID：R-<域>-<序号>
领域：Payment / Variation / EOT / Claim / Insurance / Guarantee / Back-to-Back
条件 IF：...
结论 THEN：...
依据：<合同条款号 + 出处>
例外：...
```

## 待建规则域 / Domains to build
- **Payment 付款**：进度% / 里程碑 → 发票 → Engineer 批 → Employer 批 → 付款证书 → XX 天内付款；Retention / Advance 回扣。
- **Variation 变更**：Instruction → Estimate → Approval → Execution → Final Adjustment；谁有权签发。
- **EOT / Delay**：通知时限（7/14/28 天？）→ 详细申请 → 同期记录 → 批准。
- **Claim 索赔**：Notice within X days（Time-bar）→ Detailed Claim → Contemporary Records。
- **Back-to-Back**：主合同义务是否流转至分包；Flow-Down Matrix / Risk Allocation Matrix。
- **Insurance / Guarantee**：险种保额、保函类型(APG/PBG)与有效期。

## 示例 / Example
```
规则ID：R-PAY-01
领域：Payment
条件 IF：VO 无 Engineer 的 Instruction 或无 Approval
结论 THEN：不满足付款条件 → 本期不可计量支付
依据：<待填 主合同 Variation/Payment 条款号>
```

> 每条规则必须能溯源到条款；无出处的规则标 `[未核实]`。
