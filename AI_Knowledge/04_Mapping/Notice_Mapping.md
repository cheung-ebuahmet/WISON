# Notice_Mapping — 通知与时限 主合同⇄分包映射
`[v0.3.1 · 🟡 Active · Rule Runtime for RULE-001 · Confidence: 68%]`

---

## Canonical（EPC 主合同侧）
| 参数 | 取值 | 出处 | Confidence |
|---|---|---|---|
| CVR 通知 | **14 calendar days** from instruction/awareness | GTC Art 24.4(a) | 🟢 99% |
| CVR 未发后果 | **Entitlement Lost** — 不构成 Variation，无调价/调期/救济 | GTC Art 24.4(b) | 🟢 99% |
| Variation 裁定争议 | **60 calendar days** — 逾期终局并弃权 | GTC Art 24.5(e) | 🟢 99% |
| 设计文件视同批准 | **10 working days** — Company 未复 + Contractor 书面告知 → deemed approved | GTC Art 9.2(c) · SC item 5 | 🟢 99% |
| 争议发票退回 | **14 calendar days** — Company 退回 + 说明理由 | GTC Art 23.3(a) | 🟢 99% |
| Delay LD Notice | EPC 端 LD 触发机制 = Variation 路径（CVR 14d），非独立 LD Notice | GTC Art 18.4 → Art 24.4 | 🟡 85% |
| EOT 通知 | 经 CVR 路径（14d）+ Art 25.4 同期记录要求 ⚪ 待精读 | GTC Art 25.1/25.4 | 🟡 70% |
| Suspension 成本通知 | ⚪ Art 34.6 引 ANX5，待读 | GTC Art 34.6 · SC item 11/12 | ⚪ 30% |

## Operational（分包合同侧）
| 参数 | 10.1 CCECC Civil II | 10.2 TCC Civil I/III | 12.1 CCECC MEI I | 12.2 TCC MEI II |
|---|---|---|---|---|
| Variation 通知 | ⚪ 待提取 (COC) | ⚪ 待提取 (COC) | **5 working days** | ⚪ |
| Variation 报价 | ⚪ | ⚪ | **10 working days** | ⚪ |
| EOT 通知 | ⚪ | ⚪ | **10 calendar days** from occurrence | ⚪ |
| Claim 通知 | ⚪ | ⚪ | **5 working days** | ⚪ |
| 争议谈判 | ⚪ | ⚪ | **14 calendar days** | ⚪ |
| Delay LD Notice | **须先发 Notice**（扣款前提） | **须先发 Notice** | **IPC 直接扣减**（隐含 Notice） | ⚪ |
| KP 缺位通知 | ⚪ 待提取 | ⚪ | ⚪ | ⚪ |
| 来源 | `10.1-*.yaml` · COC | `10.2-*.yaml` · COC | `12.1-*.yaml` (claims section) | ⚪ |
| Corres 数量 | 4 letters | 5 letters | 5 letters | 3 letters |

## Gap Analysis
| Gap | 涉及 | 类型 | 差异 | 风险 | 影响 |
|---|---|---|---|---|---|
| **Var 通知时限** | 12.1 | **Inverse ✅** | Subcon 5 WD < EPC 14 cal → 分包商须更快通知 Wison | **LOW** | 🟢 **有利** — Wison 从分包商处早获信息，有 9+ 天缓冲用于自身 CVR |
| **Var 报价时限** | 12.1 | **Inverse ✅** | Subcon 10 WD < EPC 14 cal | **LOW** | 🟢 分包商须更快报价 |
| **EOT 通知** | 12.1 | **Inverse ✅** | Subcon 10 cal < EPC 14 cal | **LOW** | 🟢 有利 |
| **Claim 通知** | 12.1 | **Inverse ✅** | Subcon 5 WD < EPC 14 cal（经 CVR） | **LOW** | 🟢 有利 — 但须注意：Subcon Claim 通知的 5 WD 比 EPC Variation 的 14d 短得多，Wison 收到分包 Claim 后有约 9 天来评估是否需转为主合同 CVR |
| **Delay LD Notice** | 10.1/10.2 | **Inverse ⚠️** | Civil 须先发 Notice 才能扣 LD — 这是门坎，不是时限 | **LOW** | 🟡 操作风险：若漏发 Notice 直接扣款 → 程序瑕疵。EPC 端 LD 经 Variation 路径更复杂 |
| **争议时限** | 12.1 | **Covered ✅** | 14d = 14d | **LOW** | 🟢 对等 |
| **Corres 证据** | 10.1/10.2/12.1 | **Partial** | 共 17 封商业信函已存档（OCR'd），但仅 5 封有结构化 YAML | **MEDIUM** | 🟡 信函数据未被系统消费 — 17 封中的 Notice 类型可增强 RULE-001 Evidence 绑定 |

## Rule Binding
| Rule ID | Runtime Status | Confidence | 判定 |
|---|---|---|---|
| **RULE-001** (CVR Time-bar) | 🟢 Active | 🟢 90% (EPC side) · 🟡 68% (subcon side due to Civil COC gaps) | 14d 时限清晰；Civil 端的 LD Notice 机制独立于 Variation 路径 |

## Confidence 分解

```
Clause Mapping      ████████░░  82%  EPC: 完整 · 12.1: 完整 · 10.1/10.2: COC 条款待提取
Evidence Mapping    ██████░░░░  55%  17 封函件中仅 5 封结构化 · Notice 模板未提取
Runtime Mapping     ████████░░  78%  RULE-001 可判定"是否逾限" · 无法判定"Notice 是否有效"
Issue Validation    ████░░░░░░  42%  SLT-5312-WSN-CCC-0006 (MEI Delay LD Notice) 已读 · Issue #1 PM Notice 已读 · Issue #2 Delay Notice 已读
─────────────────────────────────
Overall Confidence  ██████░░░░  68%
```

## Actions
1. **[本周]** 从 10.1/10.2 COC 提取 Variation/EOT/Claim Notice 时限 → 消除 Civil side gap
2. **[本周]** 结构化剩余 12 封未处理的 Corres 信函 → 提升 Evidence Mapping
3. **[流程]** 建立 Notice 日历：CVR 14d 倒计时从收到分包通知起算（而非从 ADNOC 指令起算——因为分包先知道）
4. **[07-16 截止]** Issue #1 (PM KP-LD) + Issue #2 (MEI Delay LD) 截止日后 → 信函升级/扣款执行

## Debt Repaid
- [x] **CD-001 部分偿还** — Notice 时限映射完成（EPC + 12.1），Evidence Gap 缩小
