# Commercial Contract Knowledge Base — Wison RSGP

> **Claude Code 入口** — 面向合同管理（Commercial / Contract Administration）
> 最后更新: 2026-07-18

---

## 知识库地图

```
_Ref/                                    ← 商业合同知识层（仅商业相关）
├── schema/
│   ├── contract-schema.yaml             ← 合同 v2.0（含 exhibit 级 commercial_relevance）
│   ├── correspondence-schema.yaml       ← 商业函件
│   ├── entity-schema.yaml               ← 商业实体（Company/Person/Package）
│   └── issue-schema.yaml                ← 待建：商业问题
│
├── data/
│   ├── MASTER-INDEX.md                  ← 📍
│   ├── contracts/                       ← 合同 YAML（事实层）
│   │   ├── 10.1-CCECC-Civil-II.yaml     ← ✅ 95% 完整
│   │   ├── 10.2-TCC-Civil-I-III.yaml    ← ✅ 95% 完整
│   │   ├── 12.1-CCECC-MEI-I.yaml        ← ✅ 90% 完整
│   │   ├── 12.2-TCC-MEI-II.yaml          ← 🆕 70% (商业数据已提取，payment条款待补充)
│   │   ├── 99-LONGTAIDI-Fire-Prefab.yaml ← 🆕 50% (tender stage)
│   │   └── EPC-ADNOC-RSGP.yaml          ← ✅ 75% (商业数据+LD已提取)
│   ├── clause-library/                  ← 商业条款知识对象（规则层）
│   │   ├── Key-Personnel.md             ← ✅
│   │   ├── Key-Personnel-LD.md          ← ✅
│   │   └── Payment.md                   ← ✅ 新建
│   ├── commercial-analysis/             ← 商业分析层（解读）
│   │   ├── back-to-back-matrix.md       ← ✅
│   │   └── risk-register.md             ← ✅
│   ├── packages/                        ← 🆕 工作包数据（scope/milestone/接口）
│   ├── claims/                          ← 🆕 索赔与变更追踪（实例层）
│   ├── correspondence/                  ← 商业函件索引 (2 letters)
│   ├── companies/                       ← CCECC / TCC
│   └── people/                          ← Chen Zhiming
│
├── wiki/Commercial/
│   └── Subcontractor-Matrix.md          ← 自动编译
├── tasks/                               ← 成熟度追踪
└── timeline.md                          ← 合同里程碑（不记施工事件）
```

---

## 设计原则

> **"这份资料是否影响付款、变更、索赔、工期、违约责任、风险分配或合同履约？"**

| 答案 | 处理 |
|------|------|
| 会 → | OCR + Schema + Clause + 双向关联 |
| 不会 → | 保留原始文件，OCR 文本可有可无，不结构化 |

---

## 合同商业价值矩阵

| 合同 | 金额 | KP LD | 商业价值 | 成熟度 |
|------|------|:---:|:---:|:---:|
| 10.1 CCECC Civil II | AED 149.8M | AED 10,000 | ⭐ critical | 95% |
| 10.2 TCC Civil I/III | AED 162.1M | AED 10,000 | ⭐ critical | 95% |
| 12.1 CCECC MEI I | AED 160.9M | AED 10,000 | ⭐ critical | 95% |
| 12.2 TCC MEI II | AED 155.5M | AED 10,000 | ⭐ critical | 70% |
| 99 LONGTAIDI Fire Prefab | *(tender)* | *(tender)* | ⭐ high (pre-award) | 50% |
| EPC-ADNOC-RSGP | USD 686.2M | — | ⭐ critical | 75% |

> **Schema v2.0 — LOCKED** ✅ 3/3 合同验证通过（10.1 Attachment 体系 / 10.2 Atchments 体系 / 12.1 Exh A-K 体系）
> 建模原则: `_Ref/Modeling-Principles.md`

---

## 商业条款库（Clause Library）

| 优先级 | 条款 | 状态 |
|:---:|------|:---:|
| ⭐⭐⭐⭐⭐ | Payment | ✅ |
| ⭐⭐⭐⭐⭐ | Variation | ⚠️ 待建 |
| ⭐⭐⭐⭐⭐ | Delay / LD | ✅ KP-LD, ✅ Delay-LD |
| ⭐⭐⭐⭐⭐ | EOT | ⚠️ 待建 |
| ⭐⭐⭐⭐⭐ | Claims / Notice | ⚠️ 待建 |
| ⭐⭐⭐⭐ | Termination | ⚠️ 待建 |
| ⭐⭐⭐⭐ | Performance Security | ⚠️ 待建 |
| ⭐⭐⭐⭐ | Retention | ⚠️ 待建 |
| ⭐⭐⭐⭐ | Advance Payment | ⚠️ 待建 |
| ⭐⭐⭐ | Warranty | ⚠️ 待建 |
| ⭐⭐⭐ | Insurance (商业部分) | ⚠️ 待建 |
| ⭐⭐ | 其他（不主动建 KO） | archive |

---

## Exhibit 商业价值一览（10.1 样板）

| Exhibit | 标题 | 商业价值 | 一级主题 |
|---------|------|:---:|------|
| Att 2 | Change Management | ⭐ critical | variation, claim |
| Att 5 | Scope of Work | ⭐ critical | scope, schedule, LD, KP |
| Att 6 | Commercials | ⭐ critical | boq, rates, payment |
| Att 1 | Communication Procedures | ⭐ medium | administrative |
| Att 7 | Owner's Special Requirements | ⭐ medium | back-to-back |
| Att 3 | HSE Requirements | ⭐ low | hse |
| Att 4 | Quality Management | ⭐ low | quality |

---

## 商业问题（Commercial Issues）— 活跃

| # | 合同 | 问题 | 状态 | 潜在成本 |
|---|------|------|:---:|------|
| 1 | 10.1 | 项目经理缺位 (Material Breach) | open | AED 10,000/day |
| 2 | 12.1 | Milestone No.2 逾期 — Delay LD 保留 | open | AED 160,892/day |
| 3 | 12.1 | **CCC-0006 NOTICE OF DEFAULT** | **open** | **待提取** |
| 4 | 12.1 | KP 姓名栏全部为空（合同签署时未填） | open | AED 70,000/day (7人) |
| — | — | *(后续新问题追加此处)* | | |

---

## 知识图谱（Knowledge Graph）← NEW

> **112 节点 / 139 边** — 连接合同、条款、信函、价格、附件、风险、Issue 的关联网络

| 文件 | 说明 |
|------|------|
| [`graph/nodes.yaml`](graph/nodes.yaml) | 所有实体节点（5 类合同 × 40 条款 × 27 附件 × 18 价格点 × 3 信函 × 11 风险 × 2 Issue） |
| [`graph/edges.yaml`](graph/edges.yaml) | 所有关系边（`has_clause` / `has_exhibit` / `flows_down` / `affects` / `references` 等 12 种边类型） |
| [`graph/graph.json`](graph/graph.json) | NetworkX 兼容 JSON 导出 |
| [`graph/README.md`](graph/README.md) | Schema 文档 + 查询指南 |

**查询工具**：`python _tools/query_graph.py`

```bash
python _tools/query_graph.py --stats                          # 统计
python _tools/query_graph.py --node 12.1 --depth 2            # 合同全貌
python _tools/query_graph.py --impact AMDT-12.1-01            # Amdt 影响分析
python _tools/query_graph.py --compare LD                     # LD 跨合同对比
python _tools/query_graph.py --report clause-history --clause GCS-17  # 条款历史
python _tools/query_graph.py --search "Delay LD"              # 关键词搜索
```

**图编译**：`python _tools/build_graph.py`（从 YAML/MD/DOCX 自动编译，无需手动编辑）

**两套合同框架**：

| 框架 | 合同 | 条款体系 | 条款 ID 前缀 |
|------|------|---------|------------|
| MEI | 12.1, 12.2, 99 | GCS 1.0-50.0 + SCS 1-7 | `MEI-GCS-{n}` |
| Civil | 10.1, 10.2 | COC 29 sections | `CIVIL-COC-{n}` |

---

## 下一步

| # | 动作 |
|---|------|
| 1 | ~~建 issue-schema.yaml~~ (deferred — use YAML `issues:` blocks instead) |
| 2 | 补建 5 个 ⭐⭐⭐⭐⭐ 条款 KO (Variation, EOT, Claims, Termination, Security) |
| 3 | ~~99 LONGTAIDI 合同 YAML 新建~~ ✅ 已完成 2026-07-18 |
| 4 | ~~12.2 TCC MEI II 合同 YAML 新建~~ ✅ 已完成 2026-07-18 |
| 5 | ~~EPC 主合同商业数据提取~~ ✅ 已完成 2026-07-18 |
| 6 | ~~12.1 KP 姓名补填~~ ⚠️ 合同中姓名栏为空白 — 见 YAML note |
| 7 | ~~12 封未跟踪信函建 correspondence YAML~~ ✅ 已完成 2026-07-18 |
| 8 | ~~所有 YAML 商业数字加 source 注释~~ ✅ 已完成 2026-07-18 |
| 9 | ~~补全 12 条条款 ko: 链接~~ ✅ 已完成 2026-07-18 |
| 10 | 知识图谱重建（纳入 12.2 + LONGTAIDI + 修复腐败节点） |
| 11 | price-database/_manifest.json 补充 4 个缺失子目录 |
| 12 | CCECC_PkgII CSV 补 `# Source:` 行 |

---

## 原始数据层（只读）

| 数据区 | 路径 |
|--------|------|
| 总包合同 | `D:\Wison\Main_Contract\` |
| 分包合同 + 付款 + 信函 | `D:\Wison\Subcon_Payments\` |
| 命名规则 | `D:\Wison\_Ref\_Wison 文件与文件夹命名规则.md` |
