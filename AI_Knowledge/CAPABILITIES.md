# CAPABILITIES — 专家能力清单 / Expert Capability Checklist
`[M1 验收已完成 ✅ · v0.1.0 门已过 · 活文档 · 后续能力随 v0.2+ 增量]`

> 验收标准不是"对象建完了吗"，而是：**这个专家现在会做哪些事？还有哪些做不了？**
> 某能力无法实现 → 通常意味着本体缺**对象 / 关系 / 规则**。据此反向补全（服从 [CONSTITUTION](CONSTITUTION.md) 第八条）。
> 状态：✅ 能 · ◐ 概念/法据已立、未形式化规则 · ❌ 未
> **最新 M1 验收**：[`M1_VALIDATION.md`](M1_VALIDATION.md)（2026-07-13 · C1–C7 七问全验 · PASS）

## 能力矩阵 / Capability matrix
| # | 能力 Capability | 依赖 对象/关系/规则 | 状态 | M1 验证与缺口 |
|---|---|---|---|---|
| C1 | 识别谁有权限（who holds Authority） | Party · Role · Authority · Delegation | ✅ | C2 问答可定位：Company Rep 直接行使 All Authority，无独立 Engineer → Profile 实例化已可查；Authority 阈值待分包/现场数据（v0.2） |
| C2 | 判断 Decision 是否有效 | Decision · Authority · Constraint · Delegation | ✅ | C3 问答隐含验证：Variation 须 Company 出 VO/ITP 方产生商业效力，未获即无效；规则尚未形式化写入 03_Rules（v0.2） |
| C3 | 验证 Requirement 是否满足 | Requirement(Satisfied/Outstanding) · Event | ◐ | 设计责任/付款先决等核心 Requirement 已可从 DNA+Clause 查询；Requirement 超类实体细化与判定规则待 v0.2 |
| C4 | 检查 Back-to-Back 是否完整 | `flows-down` · Contract · External Contract | ✅ | Art 20 法律基础已读：须 Company 批准、强制 flows-downs(IP/保密/道德/novation)、pay-when-paid、全责归 Contractor；逐包比对待 v0.2 |
| C5 | 分析 Event 是否触发 Notice（含 Time-bar） | Event · Rule · Notice · Time | ✅ | CVR 14 天刚性时限 + Art 9.2(c) 视同批准已证据绑定；形式化 Time-bar 规则待 v0.2 |
| C6 | 判断 Claim 是否具备合同依据 | Claim · Clause · Evidence · Decision | ◐ | Variation→Claim 链路可追踪（CVR+EOT）；Claim 实体与正式规则待 v0.2 |
| C7 ★ | **Risk Pass-through 验证**（主合同风险是否被 Back-to-Back 覆盖） | Exposure · flows-down · External Contract · Rule | ✅ | 概念+法据+Exposure 模型就位；C4/C7 问答给出完整 LD-Warranty-Security 暴露场景；逐包比对待 v0.2 |

## M1 门 / Gate status
| 条件 | 状态 |
|---|---|
| CONSTITUTION.md 定稿（8 条） | ✅ |
| ONTOLOGY.md 定稿（R1–R5） | ✅ |
| Phase 2 核心实体稳定（Contract/Party/Exposure/External Contract ❄Freeze） | ✅ |
| index.md 与目录一致 | ✅ |
| C1–C2 达 ✅（权限与 Decision 有效性可推理） | ✅ |
| C7 有明确路径（Risk Pass-through 验证） | ✅ |
| Commercial DNA 证据骨架就位（17/21 🟢） | ✅ |
| **C1–C7 七问全验 PASS** | ✅ → `M1_VALIDATION.md` |

## v0.2 目标 / v0.2 roadmap
- C3/C6 → ✅（Requirement 实体细化 + Claim/Variation 规则写入 03_Rules）
- Insurance (DNA 9) · Quality (16) · HSE (17) · Acceptance (15) 补充
- C7 逐包验证（首个 External Contract 实物）
- 首批规则形式化：Time-bar(CVR 14d) · LD Pass-through · Warranty Gap 检测
