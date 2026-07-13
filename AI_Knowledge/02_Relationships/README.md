# 02_Relationships — 知识图谱 / Knowledge Graph

**目的**：让实体互相关联，AI 才能"推理"而不只是"检索"。

## 主要关系边 / Edges
```
Main Contract  ──governs──▶   Subcontract
Subcontract    ──includes──▶  Variation
Variation      ──affects──▶   Payment
Payment        ──impacts──▶   Claim
Main Contract  ──flows-down──▶ Subcontract   (Back-to-Back 条款流转)
Claim          ──based-on──▶  Notice + Contemporary Records
```

## 记录格式 / Format
每条关系一行，可被工具解析：
```
<源实体>  <关系>  <目标实体>  [条件/条款]  [出处]
例：VO-014  affects  IPC-07  [未获 Instruction → 不计入本期]  [source]
```

## 关系类型词表 / Relation vocabulary
（与 [`ONTOLOGY.md §6`](../ONTOLOGY.md) 同步）

- **结构**：`has`（组织有角色） · `contracts-with`（缔约） · `subcontracts-to`（分包给） · `purchases-from`（采购自） · `splits-into`（拆分为） · `let-as`（发包为） · `contains`（组合体→文件→条款）
- **权限 / 责任**：`holds`（角色持权限） · `authorizes`（权限授权决定） · `delegates`（委托） · `revokes`（撤销） · `responsible-for`（Accountability：角色对某 Requirement 负责）
- **合同 / 优先权**：`governs`（管辖） · `flows-down`（流转，Back-to-Back） · `overrides`（覆盖，如 PCC>GCC） · `takes-precedence-over`（优先于，如 Spec>Drawing） · `conflicts-with`（冲突） · `supersedes`（取代，Amendment） · `requires`（前置条件）
- **因果 / Event·Decision 链**：`triggers`（触发） · `affects`（影响） · `changes`（改变状态） · `produces`（产生动作） · `based-on`（依据）

## Event 推理链 / Reasoning chain
关系不只连"对象与对象"，也连"事件与后果"。核心链：
```
Event ──affects──▶ Object ──changes──▶ State ──triggers──▶ Rule ──produces──▶ Action
```
案例(06)是 Event 序列，规则(05/03)绑定在 `triggers` 上。详见 `ONTOLOGY.md §4–5`。

> Back-to-Back 是本系统最核心的关系：主合同的每一条义务/风险，是否 100% 流转到分包？在这里逐条建 `flows-down` 边并标注差异（gap = 风险敞口）。
