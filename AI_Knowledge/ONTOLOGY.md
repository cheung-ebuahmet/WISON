# ONTOLOGY — 项目本体 / Project Ontology
`[Canonical Model · R1–R5 · 主轴 = Risk Flow · ✅ M1 冻结条件已达成 → v0.1.0 – Foundation]`

> **Mission**：**ADNOC EPC Commercial & Contract Manager Expert**——服务 Contract / Commercial Manager。
> 核心不是 Contract，而是 **Risk Pass-through**（Owner → Wison → External Contract）。这是一套 ADNOC **LSTK** 风险传递体系。
> 服从 [CONSTITUTION](CONSTITUTION.md)（尤其第八条）。**价值观** → [Commercial_Principles](Commercial_Principles.md)；**思维** → [Commercial_Philosophy](Commercial_Philosophy.md)；项目取值 → [PROFILE](PROFILE.md) / [COMMERCIAL_DNA](COMMERCIAL_DNA.md)；能力 → [CAPABILITIES](CAPABILITIES.md)。

> **推理次序（Commercial-Driven，非 Clause-Driven）★R5**：
> `Commercial Philosophy（价值观，无需合同）→ Commercial DNA（合同支撑的商业事实）→ Clause（最后才读，且是 Interpretation 非 Extraction）→ Evidence`

---

## 0. 主轴 / Main Axis = Risk Flow（非 Document Flow）★R4

```
Employer → Main Contract → Risk → Obligation → Pass-through → External Contract → Execution → Evidence → Payment → Claim → Dispute
```
**Contract 只是 Risk Allocation 的载体。** 真正的管理对象是 **Risk / Exposure**：它是否被 Back-to-Back 覆盖。

## 1. 本体的公民 / Citizens
`Object`（名词，含 Authority/**Exposure**/External Contract…） · `Event`（动词） · `State`（态，Event 改变） · `Decision`（裁定，须 Authority；产出 **Commercial Consequence**） · `Relation`（边，一等公民）。

## 2. 业务域 / Domains ★R4 重构

```
Project
├── Main Contract        Risk Allocation 载体
├── Party                Org × Role × Authority
├── Commercial Control ★ LD · Payment/IPC · Security(PBG/PCG) · Insurance · Warranty · Variation · Retention · Risk Register
├── External Contract ★  下游合同：Subcontract ∪ PO ∪ Vendor/Supplier/Inspection/Rental/Transportation
├── Execution            Construction · Commissioning · Closeout ＋ Evidence
├── Claim / Dispute      索赔与争议
├── HSE / Quality        横向域
└── Knowledge            本体自身（AI_Knowledge）
```
> **R4 变更（留痕）**：`Procurement`(R1 独立域) 与 `Subcontract`(R2) **合并**为 **External Contract**；新增 **Commercial Control** 一级域。理由：CM 视角下，一切下游合同都只有一个本质问题——是否承接主合同风险。
> **R5 变更（留痕）**：`Procurement` 进一步降为 **Process**（`04_Processes` 下 Procurement 流程），属 Execution 作业流，**非知识域**；风险承接归 `External Contract` 实体。

## 3. 主体 / Party = Org × Role × Authority × Person
`Organization has Role holds Authority (经 Delegation) → Person`；`Role responsible-for Requirement`（Accountability）。
Authority 一级对象（限额/专业/联签/委托/撤销）；Authority Constraint 独立（`requires … if …`）；Person 默认不参与推理。详见 [`Party.md`](01_Entities/Party.md)。

## 4. 风险与暴露 / Risk & Exposure ★R4 核心
- **Risk**：Main Contract 分配的风险本体（谁承担什么）。
- **Exposure（一级对象）**：CM 每天管理的"风险暴露"。类型：`Delay · LD · Warranty · Quality · Sanction · Export · Jurisdiction · Payment · Insurance Exposure …`
- **所有 Rule 围绕 Exposure。** 风险未经 Pass-through 覆盖 → `Uncovered Commercial Exposure`（Wison 自留）。详见 [`Exposure.md`](01_Entities/Exposure.md)。

## 5. Back-to-Back = Rule Engine ★R4 升级（不再只是关系）
见到 Main Contract 的 Clause，**第一反应不是解释，而是查 Flow-Down**：
```
Clause → 有无 flows-down 到 External Contract ？
   无         → Risk retained by Wison（提示）
   有但更弱   → High Risk Gap（如 Warranty 12mo vs 6mo，主动提示，不等人问）
   有且对等   → Covered
```
规则落 `03_Rules`，围绕 Exposure。对应能力 **C4 / C7**。

## 6. Contract 组合体 & 优先权
`Contract Package contains Document contains Clause`（Agreement/LOA/PCC/GCC/Scope/Spec/Drawings/BOQ/Exhibits/Clarifications/Amendments）。优先权关系：`overrides · takes-precedence-over · conflicts-with · supersedes`。详见 [`Contract.md`](01_Entities/Contract.md)。

## 7. External Contract（外部合同，泛化）★R4
`Subcontract / PO / Vendor / Supplier / Inspection / Rental / Transportation` 统一为 **External Contract**。CM 只问：**是否承接 Main Contract 风险（flows-down 完整？）**。子类型差异属 Profile，风险承接逻辑属 Canonical。详见 [`External_Contract.md`](01_Entities/External_Contract.md)。

## 8. 对象层 / Objects
| 域 | 对象 |
|---|---|
| 主体 | Organization · Role · Authority · Authority Constraint · Delegation · Person |
| Main Contract | Contract Package · Document · Clause · Definition · **Requirement**(超类) · **Risk** · Time |
| Commercial Control | LD · Payment/IPC · Retention · Advance Payment · Guarantee(PBG/PCG/APG) · Insurance · **Exposure** · Risk Register |
| External Contract | External Contract(=Subcontract/PO/…) · Package · Scope · Vendor(Role) |
| 跨域·事件驱动 | Variation · Claim · Notice · **Decision** · Dispute |
| HSE/Quality | NCR · Observation · Audit · Inspection · Permit · Incident · CAR · PAR |
| 证据与记忆 | Evidence · Case · Contemporary Record |

## 9. 事件 × 状态 & 推理引擎 / Reasoning ★R4 加 Commercial Consequence
State：`Tendering→Awarded→Executing→Completed→Warranty→Closed`；Event 改变 State。
```
Event ─triggers─▶ Decision(须 Authority 合法) ─▶ Commercial Consequence ─▶ affects Exposure/Object ─▶ changes State ─▶ triggers Rule ─▶ produces Action
```
> **Decision 输出商业后果，不止有效性**。例：Engineer Instruction → Consequence：*具执行效力，但依主合同不当然构成可计价 Variation，须满足合同商业条件*。这是 Commercial AI 与"条款翻译机"的区别。
**宏链**：`Contract 定义规则 → Event 触发变化 → Decision 作出判断 → Rule 验证条件 → Object 更新状态 → Case 沉淀经验`。

## 10. 关系词表 / Relations
| 类别 | 关系 |
|---|---|
| 结构 | `has · contracts-with · subcontracts-to · purchases-from · splits-into · let-as · contains` |
| 权限/责任 | `holds · authorizes · delegates · revokes · responsible-for` |
| 合同/优先权 | `governs · flows-down · overrides · takes-precedence-over · conflicts-with · supersedes · requires` |
| 风险 ★ | `allocates`(合同分配风险) · `retained-by`(未流转→Wison) · `exposes-to`(→Exposure) · `covered-by`(被分包/保险/保函覆盖) |
| 因果 | `triggers · affects · changes · produces · based-on` |

## 11. 决策记录 / Decisions locked
| 轮 | 决策 |
|---|---|
| R1 | Procurement 独立 · Party=Org×Role · Engineer 独立 · HSE/Quality 横向 · Event 层 |
| R2 | Canonical+Profile · Contract Package · 优先权一级关系 · State×Event · Requirement 超类 · Decision |
| R3 | Authority 一级对象 · Constraint 独立 · Delegation · Person(不参与推理) · Accountability · Capability · 宪法第八条 |
| R4 | **Mission=Commercial/Contract Mgr** · **主轴=Risk Flow** · **Commercial Control 域** · **Procurement+Subcontract→External Contract** · **Exposure 一级对象** · **Back-to-Back=Rule Engine** · **Decision→Commercial Consequence** · **C7** · **Phase 3 改向 Commercial DNA** |
| R5 | **Phase 2 Freeze**（够用即冻） · **推理三层 Philosophy→DNA→Clause** · **Commercial_Principles/Philosophy 思维 OS** · **Procurement 降为 Process** · **Phase 3 更名 Contract Interpretation** |

## 12. 里程碑 M1 — ✅ PASSED (2026-07-13) → v0.1.0 – Foundation
条件全部满足：CONSTITUTION 定稿 · ONTOLOGY 定稿 · Phase 2 实体 ❄Freeze · index 与目录一致 · C1–C7 能力验收 PASS（[M1_VALIDATION](M1_VALIDATION.md) · [CAPABILITIES](CAPABILITIES.md)）。
**冻结 = 知识结构稳定，非所有知识完整。** 剩余区域（Insurance/Quality/HSE/Acceptance）属领域深化 → v0.2。

## 13. Next ★R5
- **Phase 2 Freeze**：够用即冻结，不追 100%；Variation/Claim/Payment **边学边补**。
- **下一步（最高价值）**：[`Commercial_Philosophy.md`](Commercial_Philosophy.md) + [`Commercial_Principles.md`](Commercial_Principles.md)——思维操作系统（已起草 v0.1，待红线）。
- **Phase 3 = Contract Interpretation**（非"读合同"）：每条 Clause 回答——改变哪个 Risk / Exposure / Decision / Requirement？有无 Back-to-Back？有无 Commercial Consequence？（协议见 `08_Prompts`）
