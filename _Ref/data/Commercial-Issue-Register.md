# Commercial Issue Register

> **展示层** — 数据来源: `data/contracts/*.yaml` → `issues: []`
> 最后更新: 2026-07-09

---

## 活跃 Issue

| # | 合同 | 问题 | 触发 | 状态 | 潜在成本 | 截止日 | 关联函件 |
|---|------|------|------|:---:|------|:---:|------|
| 1 | 10.1 | PM 缺位 (Material Breach) | 陈志明 5-25 离岗，6-24 假期届满未归 | **open** | AED 10,000/day | 2026-07-16 | SLT-5312-WSN-CCE-0020 |
| 2 | 12.1 | Milestone No.2 逾期 (Delay LD) | Pkg1 6-15/Pkg3 6-1 到期均未完成 | **open** | AED 160,892/day | 2026-07-16 | SLT-5312-WSN-CCE-0021 |

---

## 已关闭

| # | 合同 | 问题 | 关闭日期 | 结果 |
|---|------|------|:---:|------|
| — | — | — | — | 暂无 |

---

## 端到端链路（#1 PM 缺位）

```
PDF 证据
  Att 05_Key Personnel - LD.docx (AED 10,000/day 表)
  COC_Draft.docx (Sub-Clause 4.3.3 / 4.3.7 / 4.2.4)
      ↓
YAML 事实
  data/contracts/10.1-CCECC-Civil-II.yaml
      ├── commercial_relevance: critical
      ├── liquidated_damages.key_personnel.per_day: 10000
      ├── issues[0]: PM 缺位
      └── linked.clauses: [4.3.3, 4.3.7, 4.2.4]
      ↓
Entity
  data/companies/CCECC.yaml (risk_summary: "PM 缺位 Material Breach")
  data/people/Chen-Zhiming.yaml (status: absent, absence_since: 2026-05-25)
      ↓
Clause Library
  data/clause-library/Key-Personnel.md (规则: 书面通知+替代+批准)
  data/clause-library/Key-Personnel-LD.md (触发: 缺位+未替换 → AED 10,000/day)
      ↓
Correspondence
  data/correspondence/2026-07-09-SLT-5312-WSN-CCE-0020.yaml
      ├── type: notice
      ├── action.deadline: 2026-07-16
      ├── action.status: pending
      └── related.clauses: [4.3.3, 4.3.7, 4.2.4, 10.7, 21.2]
      ↓
Issue Register (本文件)
      ↓
Next Action: 等待 2026-07-16 截止 → CCECC 回复 / 升级 ADNOC
```

---

## Issue 索引（按合同）

| 合同 | 活跃 | 已关闭 | 总数 |
|------|:---:|:---:|:---:|
| 10.1 CCECC Civil II | 1 | 0 | 1 |
| 10.2 TCC Civil I/III | 0 | 0 | 0 |
| 12.1 CCECC MEI I | 1 | 0 | 1 |
| 12.2 TCC MEI II | 0 | 0 | 0 |
