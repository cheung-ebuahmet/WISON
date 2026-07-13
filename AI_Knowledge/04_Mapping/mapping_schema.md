# Mapping Schema — 映射模板 / Mapping Template
`[v0.3 · 每份商业映射遵守此格式 · Canonical + Operational → Gap → Risk → Action]`

> 每份映射不是一个文档——是一个 **Runtime Data Record**，一端连 `AI_Knowledge/PROFILE.md` + `COMMERCIAL_DNA.md`（Canonical），一端连 `_Ref/data/contracts/*.yaml`（Operational）。两端数据就位后，Gap 自动可判定。

---

## 模板 / Template

```markdown
# [Domain]_Mapping — [商业域] 主合同⇄分包映射

## Canonical（EPC 主合同侧）
| 参数 | 取值 | 出处 |
|---|---|---|
| ... | ... | PROFILE · COMMERCIAL_DNA · GTC Art XX |

## Operational（分包合同侧）
| 参数 | 10.1 CCECC Civil II | 10.2 TCC Civil I/III | 12.1 CCECC MEI I | 12.2 TCC MEI II |
|---|---|---|---|---|
| ... | ... | ... | ... | ⚪ 待提取 |

## Gap Analysis
| Gap | 涉及合同 | 类型 | 差异 | 风险 | 对 Wison 的影响 |
|---|---|---|---|---|---|
| ... | ... | Covered/Partial/Uncovered/Inverse | 量化 | HIGH/MED/LOW | 有利/不利/中性 |

## Rule Binding
| Rule ID | Runtime Status | 判定 |
|---|---|---|
| RULE-XXX | 🟢 可运行 / 🟡 数据不足 / ⚪ 无数据 | Covered/Partial/Uncovered |

## Actions
1. [立即] ...
2. [本周] ...
3. [监控] ...

## Debt Repaid
- [ ] CD-XXX（Mapping 完成后勾选）
```

---

## Gap 类型定义 / Gap Type Taxonomy

| Gap 类型 | 含义 | 示例 |
|---|---|---|
| **Covered** | 分包条款 ≥ 主合同条款 | LD Cap 10% = 10% |
| **Partial** | 分包条款存在但弱于主合同 | Warranty 6mo vs 12mo |
| **Uncovered** | 分包无对应条款 | EPC 有 LD，分包无 LD |
| **Inverse** | 分包条款比主合同更严 → 对 Contractor 有利 | Subcon 付款 45d > EPC 30d → Wison 有 15d float |
| **Not Comparable** | 两者机制不同，不能直接数值对比 | EPC 无 Retention（PBG 替代），Subcon 有 10% |

---

## 数据来源约定 / Source Convention

| 侧 | 权威来源 | 字段级出处 |
|---|---|---|
| Canonical (EPC) | `AI_Knowledge/PROFILE.md` + `COMMERCIAL_DNA.md` | 每条值标 Clause 引用 |
| Operational (Subcon) | `_Ref/data/contracts/*.yaml` | 每条值标 YAML 字段路径 |
| Evidence | `_Ref/data/clause-library/*.md` | 引用时标 KO ID |
