# RULE-004 — Payment Precondition
`[v0.2 首批规则 · Capability C3 · Risk: Financial · MEDIUM]`

```yaml
Rule ID:     RULE-004
Name:        Payment Precondition — 付款先决条件检查
Capability:  C3 (验证 Requirement 是否满足)
Risk Type:   Financial
Trigger:     Contractor 准备提交首次 Invoice 或 Company 即将付款
Condition:
  Payment 可进行 ⇔ ALL OF:
    [✓] COMMENCEMENT DATE 已到 (13 Feb 2025)
    [✓] PERFORMANCE BANK GUARANTEE 已提交 (USD 68,620,528.60, ANX8-B)
    [✓] PARENT COMPANY GUARANTEE 已提交 (ANX8-A)
    [✓] ADVANCE PAYMENT GUARANTEE 已提交 (如申请预付, ANX8-C)
    [✓] FEED ENDORSEMENT 已签署 (Art 5.1(b)(iii) / SC item 8 删为 Not used → 此项不适用)

  IF 任一条件未满足 AND 非 ADVANCE PAYMENT
  THEN → Company 无付款义务（Art 23.1）

  IF ADVANCE PAYMENT
  THEN → 须在 Effective Date 后立即提交 APG(ANX8-C)
        → Company 在收到 APG 后 14 天 + 收到 Advance Payment Invoice 后 30 天（较晚者）支付
Decision:
  - All conditions met → Payment can proceed
  - Missing condition  → Payment obligation not yet triggered
Evidence:
  - PBG 副本 · PCG 副本 · APG 副本（如适用）
  - Commencement Date 确认（FOA p.4）
  - FEED Endorsement 状态（SC item 8: Not used）
Risk Level: MEDIUM（可补救：补交保函即可）/ HIGH（如长期未交→ Company 可终止 Art 35.3）
Output:     "付款先决条件检查：
            ✅ Commencement Date = 13 Feb 2025
            [✓/✗] PBG (10%) — [状态]
            [✓/✗] PCG — [状态]
            [✓/✗] APG — [状态]（仅预付需要）
            → 结论：[可付款 / 尚缺 X，Company 无付款义务]"
Action:
  1. [立即] 补齐缺失的保函
  2. [本周] 确认所有保函有效期覆盖要求期限（PBG→FA+最后Warranty+45d；APG→PAC+45d）
  3. [流程] 建立保函到期前自动提醒（PBG 到期前 45d 须续；APG 到期前 60d 须续）
Clause:      GTC Art 23.1 · Art 30.1/30.2/30.3 · FOA p.5-6 · SC item 8
DNA Zone:    DNA-4 (Payment) · DNA-5 (Advance) · DNA-8 (Security)
```

---

## 商业背景 / Why this rule matters
看起来是行政性的——交保函才能付款——但在 ADNOC 合同下，缺失保函不仅阻塞付款，还是**终止事件**（Art 35.3(b)(iv)：未提供/维持 PCG → Company 可终止）。保函管理不是后台事务，是 Contract Manager 的支付生命线。
