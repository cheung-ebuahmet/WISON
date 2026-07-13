# DECISION_CORPUS — 决策语料库 / Decision Corpus
`[v0.3.5 · 结构化真实商业事件 · Decision Engine 训练数据基础 · 目标 ≥30 事件 → v0.4]`

> **这不是案例库。这是 Decision Engine 的训练集。** 每个事件按统一结构记录：Event → Timeline → Triggered Rules → Evidence → Decision → Outcome → Lessons → DNA Δ。
> 当前语料：2 个活跃商业事件（来自本项目 2026 年 6-7 月信函 + 分包合同数据）。
> 目标：积累 ≥30 个结构化事件后，Decision Engine 可从数据中自主发现 Decision Pattern。

---

## 事件结构 / Event Schema

```yaml
event_id:       EVENT-XXX
type:           [Delay | Claim | Variation | Defect | Payment | KP-Breach | Notice | …]
contract:       [10.1 | 10.2 | 12.1 | 12.2 | EPC]
status:         [open | resolved | escalated | settled]
trigger_date:   YYYY-MM-DD
resolution_date: YYYY-MM-DD (or null)
cost_impact:    金额 + 币种
commercial_domains: [LD | Warranty | Payment | Insurance | Acceptance | …]

timeline:       # 事件时间线
  - {date: …, event: …, evidence: …}

triggered_rules:
  - {rule_id: RULE-XXX, clause: …, triggered: true/false, outcome: …}

decisions:
  - {date: …, decision: …, by: (Role), basis: (clause), consequence: …}

evidence_chain:
  - {type: [Notice | Email | Minutes | Report | Certificate | …], source: …, date: …}

gap_discovered:  # 事件中暴露的合同/Mapping 缺口（如有）
  - {type: …, description: …, severity: …}

lessons:
  - {principle: (P1-P7), lesson: …, dna_candidate: true/false}
```

---

## 事件库 / Event Library

### EVENT-001 · MEI Pkg I Milestone #2 逾期 — Delay LD 触发
`Type: Delay | Contract: 12.1 CCECC MEI I | Status: open | 截止: 2026-07-16`

```yaml
event_id:       EVENT-001
type:           Delay
contract:       12.1 CCECC MEI Pkg I
status:         open
trigger_date:   2026-06-01 (Pkg3) / 2026-06-15 (Pkg1)
resolution_date: null  # 等待 2026-07-16 整改截止日
cost_impact:    AED 160,892/day
                Pkg1: 25d × AED 160,892 = AED 4.02M (as of 07-13)
                Pkg3: 39d × AED 160,892 = AED 6.27M
                Total accrued: ~AED 10.3M (≈USD 2.8M)
commercial_domains: [LD, Acceptance, Schedule]

timeline:
  - {date: "2026-04-24", event: "MEI Kick-off Meeting", evidence: "SLT-5312-WSN-CCC-0003 ref"}
  - {date: "2026-05-21", event: "Senior Management Meeting", evidence: "同上"}
  - {date: "2026-06-01", event: "MEI Pkg 3 Milestone #2 到期 — 未完成", evidence: "ANX5 A.09 · FOA p.4"}
  - {date: "2026-06-04", event: "Wison 发 CCC-0003: Serious Delay in Mobilization", evidence: "SLT-5312-WSN-CCC-0003"}
  - {date: "2026-06-15", event: "MEI Pkg 1 Milestone #2 到期 — 未完成", evidence: "同上"}
  - {date: "2026-07-10", event: "Wison 发 CCC-0006: NOTICE OF DELAY — LD 已起算", evidence: "SLT-5312-WSN-CCC-0006"}
  - {date: "2026-07-16", event: "整改截止日 — 待 CCECC 提交 Recovery Schedule", evidence: "CCC-0006 deadline"}

triggered_rules:
  - {rule_id: "RULE-002", clause: "SCS Clause 17 + Exh A Work Schedule", triggered: true,
     outcome: "LD accruing at AED 160,892/day. Cap: 10% = AED 16.1M. Single milestone cap: 9% = AED 14.5M."}
  - {rule_id: "RULE-001", clause: "GTC Art 24.4 (14d CVR)", triggered: false,
     note: "此系分包 Delay LD，非 EPC Variation 路径——但分包延误可能触发后续 EPC CVR"}

decisions:
  - {date: "2026-07-10", decision: "正式发出 Delay LD Notice · 保留扣款权 · 保留 ADNOC 升级权",
     by: "Feng Guoling (Wison Contractor Representative)", basis: "SCS Clause 17 · Sub-Clause 10.7 · Art 5.6",
     consequence: "LD 持续计罚 · IPC 扣款待 07-16 后执行"}

evidence_chain:
  - {type: "Notice", source: "SLT-5312-WSN-CCC-0006 (3pp, bilingual)", date: "2026-07-10"}
  - {type: "Letter", source: "SLT-5312-WSN-CCC-0003 (3pp, mobilization status)", date: "2026-06-04"}
  - {type: "Contract", source: "ANX5 A.09 + SCS Clause 17 + Exh A Work Schedule", date: "2025"}
  - {type: "Site Verification", source: "CCC-0006: Site verification confirmed milestone not achieved", date: "2026-07-10"}

gap_discovered:
  - {type: "12.1 MC Relief Risk", description: "若 12.1 最终按期 MC → 前期 LD 须全额退还 → Wison 失去 LD 收入",
     severity: "MEDIUM", cf_ref: "CF-AC-005"}
  - {type: "Notice 语言", description: "分包合同 LD Notice 系 IPC 直接扣减（隐含），而 EPC LD 经 Variation 路径",
     severity: "LOW"}

lessons:
  - {principle: "P4: Operational ≠ Commercial", lesson: "Mobilization delay 是执行问题，但触发的是商业后果（LD）。
     商业经理须确保执行问题→商业后果的映射准确且及时执行。", dna_candidate: true}
  - {principle: "P6: Evidence is continuous", lesson: "CCC-0003 (6/4) → CCC-0006 (7/10) 之间 36 天——
     中间的证据积累（daily reports, site photos）决定了 LD 起算日能否被有效抗辩。", dna_candidate: false}
  - {principle: "P2: Check upstream before committing downstream", lesson: "12.1 MC Relief = EPC 主合同无对应机制。
     这是分包谈判时未完全 B2B 的结果——教训：异常的 LD 退还条款须评估主合同对应性。", dna_candidate: true}
```

---

### EVENT-002 · CCECC Civil II PM 缺位 — Material Breach
`Type: KP-Breach | Contract: 10.1 CCECC Civil II | Status: open | 截止: 2026-07-16`

```yaml
event_id:       EVENT-002
type:           KP-Breach
contract:       10.1 CCECC Civil II
status:         open
trigger_date:   2026-06-24
resolution_date: null  # 等待 2026-07-16 整改截止日
cost_impact:    AED 10,000/day from 2026-06-24
                19 days × AED 10,000 = AED 190,000 (as of 07-13)
commercial_domains: [KP, LD, Authority, Notice]

timeline:
  - {date: "2025-12-04", event: "10.1 CCECC Civil Pkg II 签署 · 陈志明 = PM", evidence: "10.1 YAML"}
  - {date: "2026-05-25", event: "陈志明离岗休假（30天）", evidence: "10.1 YAML issues + timeline.md"}
  - {date: "2026-05-28", event: "SLT-5312-WSN-CCE-0019 仍致陈志明（Grating Covers Re-scope）",
     evidence: "SLT-5312-WSN-CCE-0019.yaml ⚠ 日期异常"}
  - {date: "2026-06-24", event: "假期届满未归 → KP-LD 起算 AED 10,000/天", evidence: "timeline.md"}
  - {date: "2026-07-09", event: "Wison 发 CCE-0020: MATERIAL BREACH NOTICE — PM Absence",
     evidence: "SLT-5312-WSN-CCE-0020"}
  - {date: "2026-07-16", event: "整改截止日 — 待 CCECC 提供替代 PM", evidence: "CCE-0020 deadline"}

triggered_rules:
  - {rule_id: "C1 Authority", clause: "Sub-Clause 4.3.3 + 4.3.7 + 4.2.4 + Att 5 Appendix",
     triggered: true, outcome: "KP-LD AED 10K/day · Material Breach — 可触发暂停付款 + Termination (Art 21.2)"}

decisions:
  - {date: "2026-07-09", decision: "发 Breach Notice · 要求 7 天内提供替代 PM · 保留 KP-LD 扣款 · 保留 Termination",
     by: "Feng Guoling (Wison Contractor Representative)", basis: "COC Sub-Clause 4.3.3/4.3.6/4.3.7/4.2.4",
     consequence: "KP-LD 持续计罚 · CCE-0020 deadline = 07-16"}

evidence_chain:
  - {type: "Notice", source: "SLT-5312-WSN-CCE-0020 (Notice of Material Breach)", date: "2026-07-09"}
  - {type: "Contract", source: "COC Sub-Clause 4.3.3/4.3.6/4.3.7/4.2.4 · Att 5 Appendix",
     date: "2025-12-04"}
  - {type: "YAML", source: "_Ref/data/contracts/10.1-CCECC-Civil-II.yaml (KP section)",
     date: "2026-07-09"}
  - {type: "Entity", source: "_Ref/data/people/Chen-Zhiming.yaml", date: "2026-07-09"}

gap_discovered:
  - {type: "0019 Date Anomaly", description: "SLT-5312-WSN-CCE-0019 在 5-28 致陈志明，但其宣称离岗自 5-25 起。
     可能: (a)离岗实际晚于 5-25 (b)发函人不知 (c)交接过渡 → 若 dispute 需核实。",
     severity: "LOW"}
  - {type: "KP-LD vs Delay LD 叠加", description: "PM 缺位 = Material Breach → KP-LD + 可触发暂停/Termination。
     但 KP-LD 与 Delay LD 是否可叠加扣款？条款未明确禁止——实践上可叠加。",
     severity: "LOW"}

lessons:
  - {principle: "P7: Manage exposure, not paperwork", lesson: "PM 缺位不是 HR 问题——是 Commercial Exposure。
     一个 7 人 KP 名单的 LD 合计 AED 70,000/天——月度可达 AED 2.1M。这份敞口需要主动监控。",
     dna_candidate: true}
  - {principle: "P2: Check upstream before committing downstream", lesson: "EPC 无 KP-LD——
     Wison 自创的下行管控工具。但若 Wison 自身 KP 不稳定，上行也有风险（Art 19 人员变更限制）。
     KP 稳定性是双向敞口。", dna_candidate: false}
```

---

## 事件统计 / Corpus Stats

| 指标 | 当前值 | 目标 (v0.4) |
|---|---|---|
| Total Events | **2** | ≥30 |
| Open | 2 | — |
| Resolved | 0 | ≥20 |
| Domains Covered | LD · KP · Authority · Notice | All 7 |
| DNA Candidates Generated | 3 | ≥15 |
| Gap Discoveries | 3 | ≥20 |

---

## Failure Pattern Library / 失败模式库

> 商业智慧不是从成功中学的。是从失败中学的。每个 Failure Pattern = 一个"下次不要再犯"的可执行教训。

### FP-001 · Notice Late — "等 cost impact 确认再发 Notice"

```
Pattern:        Notice Late
Status:         🟡 理论推导（基于 CVR 14d 刚性时限 + 行业通用失败模式）
Real Event:     ❌ 本项目尚无已确认的 Notice 迟延案例

Cause:          Commercial team 等待 cost impact 确定后再发 Notice
                认为"不确定金额就不能发 Notice"
Result:         14 天超时 → Entitlement Lost (Art 24.4(b))
                已执行的工作不得计价

DNA:            "Notice first, quantify later."
                CVR 14 天的起算点是"收到指令/知悉事件"——
                不是"cost impact 算清楚"。
                先发 Notice 保权利，再慢慢算账。

Related Rule:   RULE-001 CVR Time-bar
Related DNA:    DNA-11 (Variation Logic) · DNA-12 (Notice/Time-bar)
Principle:      P4: Operational ≠ Commercial
                P6: Evidence is continuous
```

### FP-002 · Subcontract LD Not Back-to-Back — "以为复制了条款就够了"

```
Pattern:        Subcontract LD Not Back-to-Back
Status:         🟢 本项目已验证（LD 全 3/4 分包 Covered · Inverse favorable）
Real Event:     ❌ 本项目无此失败——但行业常见

Cause:          Contract Manager 签分包时复制了 LD 条款
                但未验证 (a)费率是否对等 (b)Cap 是否对等 (c)触发事件是否对齐 (d)MC Relief 等特别条款
Result:         分包 LD < 主合同 LD → Wison 自留差额
                或分包 LD > 主合同 LD → 可执行性存疑（penalty vs liquidated damages）

DNA:            "Back-to-Back is control, not copy-paste."
                LD 是三参数匹配：费率 + Cap + 触发条件。
                任何一个参数不对齐 = Exposure。

Related Rule:   RULE-002 LD Flow-down
Related DNA:    DNA-6 (LD Logic)
Principle:      P2: Check upstream before committing downstream
                P5: Own what you cannot flow down
```

---

## v0.3.5 Corpus Gate
- [x] EVENT-001 + EVENT-002 结构化（完整 schema · 时间线 · 证据链 · Lessons · DNA candidates）
- [x] Failure Pattern Library 启动（2 patterns）
- [x] Decision Corpus schema 定型
- [ ] 累计 ≥30 事件后 → v0.4 Decision Engine 激活
