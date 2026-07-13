# REASONING_PROTOCOL — 统一推理协议 / Universal Reasoning Protocol
`[v0.2 元能力 · 横切所有层 · 模型无关 · 任何商业问题均沿此路径]`

> **目的**：无论接入 GPT、Claude、Gemini 还是本地模型，AI 回答任何商业问题时都沿同一套推理路径——确保**输出稳定、可复现、可审计**。
> 这不是一个 Prompt 模板。这是整个系统的**推理契约（Reasoning Contract）**——每层调用哪个知识节点、输出什么格式。

---

## 七步推理路径 / The 7-Step Chain

```
用户问题
  │
  ▼
STEP 1 ── 问题分类          → 这是什么类型的问题？
  │        (Variation | Delay | Payment | Claim | Warranty | LD | B2B | Authority | …)
  ▼
STEP 2 ── 事件识别          → 合同上发生了什么 Event？
  │        (Instruction | Delay | Suspension | NCR | Drawing Revision | …)
  ▼
STEP 3 ── 规则调用          → 适用哪条 Rule？（Rule Engine / 03_Rules）
  │        (CVR Time-bar | LD Flow-down | Warranty Gap | Payment Precondition | …)
  ▼
STEP 4 ── 条款引用          → 合同哪条管这个？（CLAUSE）
  │        (GTC Art XX · SC item Y · FOA · ANX5 A.09 …)
  ▼
STEP 5 ── 证据引用          → 需要什么证据？现在有什么？缺什么？（EVIDENCE）
  │        (Notice · Email · Minutes · Daily Report · ITP · …)
  ▼
STEP 6 ── 风险评估          → 敞口是什么？Covered / Partial / Uncovered？（EXPOSURE）
  │        (Delay Exposure · LD Exposure · Warranty Exposure · …)
  ▼
STEP 7 ── 建议行动          → 现在该做什么？（NEXT ACTION）
           (发 Notice · 补证据 · 启动 CVR · 升级 · 暂停付款 · …)
```

---

## 每步的知识节点映射 / Knowledge Node Routing

| Step | 调用 | 知识节点 |
|---|---|---|
| 1 分类 | 问题类型判定 | `Commercial_Philosophy.md` (P1–P7) · `COMMERCIAL_DNA.md` 对应区 |
| 2 事件 | 事件匹配 | `04_Processes` 流程 · 未来 `Event_Library.md` (v0.2.2) |
| 3 规则 | 规则命中 | `03_Rules` · 未来 Rule Engine (v0.2.0) |
| 4 条款 | 条款定位 | `CONTRACT_MAP.md` · `COMMERCIAL_DNA.md` 对应区 · `PROFILE.md` |
| 5 证据 | 证据缺口 | 未来 `Evidence_Matrix.md` (v0.6) · 当前 `M1_VALIDATION.md` 模式 |
| 6 风险 | 敞口判定 | `01_Entities/Exposure.md` · `ONTOLOGY.md §4–5` |
| 7 行动 | 下一步 | `Commercial_Principles.md` (价值观驱动) · 未来 `Commercial_Playbook.md` (v0.8) |

---

## 输出格式契约 / Output Contract

每次回答必须包含（按序）：

```markdown
## 问题类型
[Variation | Delay | Payment | Claim | …]  ·  涉及 DNA 区：[DNA-XX]

## 合同事件
[发生的 Event]  ·  触发条款：[Art XX]

## 适用规则
[Rule ID]：[Rule 名称]  →  结论：[通过/触发/违规]

## 合同依据
> [Clause 原文或准确摘要]  —  [出处：GTC Art XX / SC item Y / FOA p.Z]

## 证据状态
- ✅ 已有：[…]
- ❌ 缺失：[…]（风险：[…]）

## 风险敞口
[Exposure 类型]  ·  状态：[Covered / Partial / Uncovered / Crystallised]

## 建议行动
1. [立即]
2. [本周内]
3. [监控]
```

---

## 与价值观的绑定 / Principle Anchoring

每一步结束时，回看是否违反七条价值观（`Commercial_Principles.md`）：
- 这个结论是否先保护了 Wison？（P1）
- 是否先查了主合同才给下游建议？（P2）
- 是否把"权利"和"进度"分开了？（P3）
- 是否区分了执行效力与商业效力？（P4）
- 未覆盖风险是否建议认领？（P5）
- 是否要求了同期证据？（P6）
- 结论管理的是敞口还是文书？（P7）

若违反任一条，结论无效，返回重推。

---

## 使用 / Usage
- **所有 Prompt 模板**（`08_Prompts/`）必须内嵌七步路径。
- **任何 AI 模型接入本知识库时**，系统 Prompt 首段引用本协议。
- **CAPABILITIES 验收**：新能力验收时用本协议跑一遍，确认每一步都有知识节点可调用。
