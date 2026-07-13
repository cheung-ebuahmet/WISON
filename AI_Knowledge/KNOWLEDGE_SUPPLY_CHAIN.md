# KNOWLEDGE_SUPPLY_CHAIN — 知识供给链 / Knowledge Supply Chain
`[v0.3 基础设施 · 项目管理从"补文件"切换为"供燃料" · 每次 OCR/读取前过四问闸门]`

> **核心原则**：OCR 不是"补资料"——它是给 Rule Engine、Reasoning Engine 和未来的 Decision Engine **供燃料（Fuel）**。
> 每完成一次 OCR/结构化，不是"多了一份文档"，而是必须回答四个问题。四个答案都是"没有"→ 这次供给对系统价值有限。

---

## 供给链全图 / The Pipeline

```
Project Documents
        │
        ▼
OCR & Text Extraction ──── 四问闸门 ──────────────────────┐
        │                                                  │
        ▼                                                  ▼
Structured Facts                                    供给价值判定
        │                                         (Capability Δ?)
        ├──► Clause Library
        ├──► Evidence Library
        ├──► Event Library
        ├──► Risk Taxonomy
        │
        ▼
DNA Extraction ─── 有没有新的 DNA？
        │
        ▼
Philosophy Candidate ─── 是否产生可复用商业判断？
        │
        ▼
Rule Generation ─── 是否触发 Trigger→Condition→Decision？
        │
        ▼
Capabilities (C1–C7…) ─── 能力覆盖提升了多少？
```

---

## 四问闸门 / The 4-Question Gate

> **每次供给（OCR/结构化/访谈）后必答。任意一问有实质性答案 → 供给有效。**

| # | 问题 | 回答要求 |
|---|---|---|
| **Q1** | 它补充了哪些**事实（Facts）**？ | 具体条款/数值/流程/定义，标注出处 |
| **Q2** | 它增强了哪些**能力（Capability）**？ | C1–C7 中哪项？覆盖% 提升了多少？ |
| **Q3** | 它消除了哪些**未知（Unknown）**？ | 从 Unknown Registry 中移除了哪条？ |
| **Q4** | 它是否产生了新的 **DNA / Rule / Philosophy**？ | 新 DNA？新 Rule Candidate？新哲学模式？ |

---

## 供给优先级算法 / Supply Prioritization

**不要问"哪些 PDF 还没 OCR"，要问"哪些能力目前没有知识供给"。**

```
Rule ──需要哪些 Clause？──▶ 需要哪些 Evidence？──▶ 来自哪些 Document？──▶ OCR 完成了吗？
```

**排序因子**（权重）：
1. **解锁能力数**（40%）— 一份文件能同时供给 C3+C4+C7 > 只供给 C3
2. **风险等级**（30%）— LD/Warranty/Insurance（CRITICAL/HIGH）> 流程细节
3. **依赖链位置**（20%）— 阻塞下游 Rule 的文件 > 独立文件
4. **文件可得性**（10%）— 已 OCR > 已签未 OCR > 缺失

---

## 供给队列 / Knowledge Queue

> 排序依据：能增加多少 Capability，而非文件是否重要。

### Priority A — 解锁多个 HIGH/CRITICAL 能力
| # | 供给目标 | 解锁能力 | 当前阻塞 | 文件 |
|---|---|---|---|---|
| A1 | Insurance 条款 | C3·C4·C7 | Insurance Exposure 无法判定 | Art 41 · ANX7 |
| A2 | Acceptance 流程 | C2·C3·C6 | 验收触发付款/质保/担保降档无法推理 | Art 15/17 · ANX11 |

### Priority B — 深化已有能力
| # | 供给目标 | 解锁能力 | 当前阻塞 | 文件 |
|---|---|---|---|---|
| B1 | Quality 要求 | C3·C5 | NCR→Claim 链路无条款支撑 | Art 13 · ANX10 B.10 |
| B2 | HSE 细则 | C3 | HSE 违约后果无法推理 | Art 21 |
| B3 | Variation Rates | C3·C6 | VO 计价无法验证 | ANX5 Exh A.07 |

### Priority C — 补完 + 首次实战
| # | 供给目标 | 解锁能力 | 当前阻塞 | 文件 |
|---|---|---|---|---|
| C1 | Performance Tests | C3·C6 | 性能违约无法判定 | Art 16 · ANX10 A.11 |
| C2 | External Contract | C4·C7 | 逐包验证无数据 | 分包合同 |
| C3 | Claim 正式规则 | C6 | C6 无法升级到 🟢 | Art 25 精读 + 实践 |

---

## 供给记录 / Supply Log
> 每次完成供给后登记。格式：`日期 · 来源文件 · Q1/Q2/Q3/Q4 摘要 · Capability Δ`

| 日期 | 供给 | Q1 Facts | Q2 Cap Δ | Q3 Unknowns cleared | Q4 New |
|---|---|---|---|---|---|
| 2026-07-13 | FOA + ANX1-2 GTC + ANX5 A.09 + Art 20/23/24/25/30/42/46 | 17 区 DNA 全绑定 | C1–C7 全验 → C5🟢C7🟢 | COMPANY/价格/Cap/LD/PBG/预付/Warranty/争议/优先权/Engineer | Art 20 B2B 法律基础 |
| 2026-07-13 | Rule Engine 设计 | RULE-001~004 | C5🟢 C7🟢 C3🟡 | Time-bar 形式化 · LD/Warranty Gap 可执行 | Rule Template · Reasoning Protocol |
