# DECISION_INPUT_SCHEMA — 决策输入契约 / Decision Input Schema
`[v0.3.6 · Frozen · 所有未来 Decision 必须满足的 8 字段输入结构 · Decision Engine 的 API 契约]`

> **这不是模板。这是 Decision Engine 的输入协议。** 任何一个商业事件要进入 Decision Engine，必须先在这 8 个字段上完成 Calibration。字段不全 = Decision 不能产出。
> 本 Schema 冻结后，v0.4 Decision Engine 的所有推理都以此为输入边界。

---

## 8 字段决策输入 / The 8-Field Decision Input

```yaml
decision_input:
  # ── 1. EVENT ──
  event:
    id:            DEC-XXX
    type:          [Delay | Variation | Claim | Payment | Defect | KP-Breach | NCR | HSE | Insurance | Acceptance | Termination | Force Majeure | …]
    date:          YYYY-MM-DD
    contract:      [EPC | 10.1 | 10.2 | 12.1 | 12.2 | …]
    description:   <1-paragraph factual summary>

  # ── 2. CONTRACT POSITION ──
  contract_position:
    entitlement:   [YES | NO | CONDITIONAL]
    clause_ref:    <GTC Art XX / SCS Clause Y / COC Sub-Clause Z>
    key_terms:     <引用关键条款原文或准确摘要>
    time_bar:      [NOT TRIGGERED | TRIGGERED | PENDING — 截止日 YYYY-MM-DD]
    authority:     <谁有权做出这个 Decision？Role + Clause 依据>

  # ── 3. FLOW-DOWN POSITION ──
  flow_down_position:
    status:        [COVERED | PARTIAL | UNCOVERED | INVERSE | NOT APPLICABLE]
    subcontract_ref: <涉及的 External Contract>
    gap_detail:    <如有 Gap，量化>
    recovery_probability: [HIGH | MEDIUM | LOW | ZERO]  # Wison 能否从分包追偿
    mapping_ref:   <04_Mapping/xxx_Mapping.md 引用>

  # ── 4. EVIDENCE STATUS ──
  evidence_status:
    completeness:  [FULL | PARTIAL | MISSING]
    has_contemporary_record: [YES | NO]
    items:
      - {type: [Notice | Email | Minutes | Daily Report | Photo | Certificate | Test Report | Invoice | Letter | …],
         source: …, date: …, weight: [HIGH | MEDIUM | LOW]}
    missing_evidence:
      - {type: …, risk_if_missing: …}

  # ── 5. EXPOSURE ──
  exposure:
    type:          [Delay | LD | Warranty | Payment | Insurance | Quality | Sanction | …]
    status:        [COVERED | PARTIAL | UNCOVERED | CRYSTALLISED]
    quantified:    <金额 + 币种 · 或 "无法量化——参数缺失">
    time_impact:   <天数 · 或 "N/A">
    risk_level:    [CRITICAL | HIGH | MEDIUM | LOW]

  # ── 6. AVAILABLE ACTIONS ──
  available_actions:
    - {action: …, basis: <clause>, probability_of_success: [HIGH | MEDIUM | LOW], constraints: […]}
    - {action: …, basis: …, probability_of_success: …, constraints: […]}

  # ── 7. RECOMMENDED ACTION ──
  recommended_action:
    primary:       <具体行动>
    deadline:      YYYY-MM-DD（如有合同时限）
    escalation:    <如不执行 → 后果>
    principle_ref: [P1-P7]  # 对应哪条商业原则

  # ── 8. LEARNING OUTPUT ──
  learning_output:
    dna_candidate:          [YES | NO]
    dna_zone:               [DNA-XX]（如 YES）
    failure_pattern_match:  [FP-XXX]（如匹配已知失败模式）
    advantage_pattern_match: [ADV-XXX]（如匹配已知优势模式）
    lesson:                 <一句话教训——可进 Philosophy>
```

---

## 字段依赖与验证链 / Field Dependency

```
EVENT (1)
  │
  ├── CONTRACT POSITION (2)  ← 依赖：COMMERCIAL_DNA + PROFILE + 已读 Clause
  │
  ├── FLOW-DOWN POSITION (3) ← 依赖：04_Mapping + _Ref YAML
  │
  ├── EVIDENCE STATUS (4)     ← 依赖：Corres/函件/证书/现场记录
  │
  ├── EXPOSURE (5)           ← 依赖：EXPOSURE 实体 + RULE 判定 + Mapping Gap
  │
  ├── AVAILABLE ACTIONS (6)  ← 依赖：Contract Position + Flow-down + Evidence
  │
  ├── RECOMMENDED ACTION (7) ← 依赖：以上全部 + Commercial Principles
  │
  └── LEARNING OUTPUT (8)    ← 依赖：Decision Corpus 历史对比 + Failure/Advantage Pattern
```

**Decision Engine 的前置检查**：若字段 2/3/4 任一项为空白或置信度 <60%，Decision Engine **拒绝产出** Decision——只产出"信息不足，需要补充 XXX"。

---

## 当前验证 / Calibration Check

> 用现有 EVENT-001 + EVENT-002 跑一遍 Schema，检验哪些字段已可填、哪些还缺。

| 字段 | EVENT-001 (MEI Delay) | EVENT-002 (PM 缺位) |
|---|---|---|
| 1. Event | ✅ | ✅ |
| 2. Contract Position | ✅ SCS Clause 17 + Exh A | ✅ COC Sub-Clause 4.2.4/4.3.7 |
| 3. Flow-down | ✅ Inverse (LD favorable) | ✅ N/A (EPC 无 KP-LD) |
| 4. Evidence | 🟡 Notice ✅ · Site records ❌ | 🟡 Notice ✅ · Departure proof ❌ |
| 5. Exposure | ✅ AED 10.3M | ✅ AED 190K |
| 6. Available Actions | ✅ Deduct · Escalate · Terminate | ✅ Deduct · Suspend payment · Terminate |
| 7. Recommended Action | ✅ Await 07-16 → deduct | ✅ Await 07-16 → escalate |
| 8. Learning Output | ✅ FP-002 match · DNA candidate | ✅ FP-000 · DNA candidate (KP monitoring) |

> **Schema 验证通过**——两个现有事件可完整填入 8 字段。但 Evidence (字段 4) 的 Partial 状态提示：真实 Decision Engine 需要比当前更完整的证据链。
