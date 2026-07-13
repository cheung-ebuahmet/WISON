# AI_Knowledge — ADNOC EPC Commercial & Contract Manager Expert

> **This is not a contract document repository. It is a Commercial Risk Intelligence System for ADNOC EPC Contract Management.**
> **这不是一个合同资料库，而是一套围绕 ADNOC EPC 项目构建的商业风险与合同管理专家系统。**
>
> 重心：**Contract** = 规则来源 · **Risk** = 管理对象 · **Back-to-Back** = 风险传递机制 · **Commercial Control** = 日常管理手段 · **Evidence** = 索赔与争议基础。
> 主轴 = **Risk Flow**（Owner → Wison → External Contract）；这是一套 ADNOC **LSTK** 风险传递体系。
>
> 核心原则：不是整理文件，而是训练一位资深 ADNOC EPC 合同经理——每份资料问"它教会专家什么？"

> 📜 **最高约束**：[`CONSTITUTION.md`](CONSTITUTION.md)（知识库宪法，8 条元规则，含 Canonical Before Instance）— 一切内容服从它。
> 🌍 **通用模型**：[`ONTOLOGY.md`](ONTOLOGY.md)（Canonical 本体：域 / Party·Authority / Package / Event·State·Decision / Requirement）。
> 🧠 **思维 OS**：[`Commercial_Philosophy.md`](Commercial_Philosophy.md) + [`Commercial_Principles.md`](Commercial_Principles.md)（价值观与思维；一切推理先过这里）。
> 🧩 **项目实例**：[`PROFILE.md`](PROFILE.md)（本项目取值层；换项目只换它，本体不动）。
> 🧬 **商业基因**：[`COMMERCIAL_DNA.md`](COMMERCIAL_DNA.md)（推理三层第 2 层：合同支撑的商业事实）。
> 🎯 **能力验收**：[`CAPABILITIES.md`](CAPABILITIES.md)（M1 门槛：专家会做哪些事、还缺什么）。
>
> **推理次序**：`Philosophy（价值观）→ DNA（商业事实）→ Clause（Interpretation）→ Evidence`（Commercial-Driven）。

---

## 三层架构 / Three layers

| 层 | 位置 | 性质 | 规则 |
|---|---|---|---|
| **Raw Data 原始资料** | `D:\Wison\Main_Contract`, `Project_Info`, `Subcon_Payments`, `_Ref` | 事实来源（PDF/邮件/红线版/IFC…） | **只读**：不删、不移、不改名 |
| **Knowledge 知识层** | `D:\Wison\AI_Knowledge\` (本目录) | 由人+AI 提炼的对象 / 规则 / 关系 / 案例 | 每条都引用 Raw Data 出处（citation） |
| **Expert 推理层** | 运行时（Copilot） | 基于知识层做审查 / 风险 / 索赔 / Back-to-Back 比对 | 结论必须可溯源到条款或案例 |

原始资料是**原材料**，不是知识。知识是从原材料里蒸馏出来的对象和规则。

---

## 目录地图 / Folder map

| 文件夹 | 内容 | 回答什么问题 |
|---|---|---|
| `00_Glossary` | 术语库（FIDIC / ADNOC / 项目缩写） | "IFC 是什么？""SGP vs RSGP？" |
| `01_Entities` | 知识对象：Contract / Subcontract / Variation / Claim / Payment / Party / Insurance / Guarantee / Notice | "这份合同的 LD 是多少？" |
| `02_Relationships` | 知识图谱：governs / includes / affects / impacts / flows-down | "这个 VO 影响哪笔付款？" |
| `03_Rules` | 规则引擎：IF/THEN 条款规则（付款、变更、EOT、索赔时效、Back-to-Back） | "满足付款条件了吗？" |
| `04_Processes` | 流程图：Variation / Payment / Claim / EOT 的步骤与审批权限 | "VO 走到哪一步了？" |
| `05_Playbooks` | 行动手册：推理链模板（如"VO 为何不能付款"） | "现在该发什么通知、补什么证据？" |
| `06_Case_Studies` | 真实案例：RFI/TQ/VO/Claim/NCR + 处理 + 结果 | "上次类似情况怎么处理的？" |
| `07_QA` | 问答对：沉淀的专家问答 | 快速检索既有结论 |
| `08_Prompts` | Copilot 的系统提示 / 推理指令 | 定义专家如何思考与引用 |

---

## 建设阶段 / Roadmap（宪法 → 本体 → 实体 → 合同 → 访谈 → 规则 → 案例；OCR/RAG 最后）

```
Phase 0  骨架 ................................................. ✅ 完成
宪法     Meta Rules → CONSTITUTION.md ........................ ✅ 完成（8 条）
Phase 1  本体 Ontology → ONTOLOGY.md ........................... ✅ M1 冻结 (v0.1.0)
Phase 2  实体概念 → Contract·Party·Exposure·External Contract ... ❄ Freeze (v0.1.0)
DNA      COMMERCIAL_DNA 21 区 .................................. 🟢 17/21 证据绑定 (v0.1.0)
M1 验收  M1_VALIDATION.md ..................................... ✅ C1–C7 全验 PASS
Phase 3  Contract Interpretation（续）........................... → v0.2（Insurance/Quality/HSE/Acceptance）
Phase 5  规则引擎（形式化 03_Rules）............................ → v0.2（Time-bar/B2B/Warranty gap）
Phase 6  案例库（真实 VO/Claim/付款/争议）...................... → v0.2+
──────────────────────────────────────────────────
后续     命名规范 → 索引 → 标签 → 元数据 → OCR → Embedding → RAG
```

关键判断：**合同是事实（What），不是专家知识（Why）**。先建模型和关系让 AI 变聪明；OCR 只是把图片变文字，故排最后。

---

## 现有可复用资产 / Reuse (不重复造轮子)

- `_Ref/` 与 `_tools/guides/` → 喂给 `00_Glossary` 与 `03_Rules`
- `_tools/consolidate_master_index.py`, `normalize_naming.py`, `gen_subcontractor_matrix.py` → 索引 / 命名 / Back-to-Back 矩阵的现成工具

## 状态 / Status
- [x] Phase 0 — 大脑骨架
- [x] 知识库宪法 CONSTITUTION.md（7 条元规则，最高约束）
- [✅] Phase 1 — ONTOLOGY.md（R1–R5 · M1 冻结 ✓）
- [❄] Phase 2 — 实体概念 **Freeze**（v0.1.0）
- [✅] M1 验收 — **C1–C7 七问全验 PASS**（[`M1_VALIDATION.md`](M1_VALIDATION.md)）
- [🟢] DNA — 17/21 区证据绑定；剩余 v0.2
- [◐] Philosophy — 随用演化，等案例沉淀后红线整理
- [ ] v0.2 — Insurance/Quality/HSE/Acceptance 深化 + 03_Rules 形式化 + 首份 External Contract C7 逐包验证

## 里程碑与提交 / Milestone & Commit

**M1 — Ontology Freeze**：达成后进行**首次 git 提交**，标记为
`v0.1.0 – Foundation (Constitution + Ontology + Core Entity Model)`。
冻结条件（详见 [`ONTOLOGY.md`](ONTOLOGY.md) M1 节）：CONSTITUTION 定稿 · ONTOLOGY 定稿 · Phase 2 核心实体稳定 · index 与目录一致 · **能力验收 C1–C2 达标**（[`CAPABILITIES.md`](CAPABILITIES.md)）。

> **在 M1 之前保持不 commit**——本体尚未稳定，允许反复改。首次提交意味着"专家大脑骨架正式定型"，不是"搭好了几个文件夹"。

_原始资料区（Main_Contract / Project_Info / Subcon_Payments / _Ref）在本次建设中零改动。_
