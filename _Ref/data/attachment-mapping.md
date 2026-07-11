# Attachment Mapping — 分包合同附件标准对照

> **Claude 导航表** — 用 canonical_type 查询，不需关心各分包编号体系
> 最后更新: 2026-07-09（+12.1 MEI）

---

## Canonical Type → 各合同映射

| Canonical Type | 10.1 CCECC Civil II | 10.2 TCC Civil I/III | 12.1 CCECC MEI I | 商业价值 |
|----------------|:---:|:---:|:---:|:---:|
| **scope** | Att 5 | Att 5 | **Exh A** | critical |
| **schedule** | Att 5 | Att 5 | **Exh A + Exh J** | critical |
| **commercial** | Att 6 | Att 6 | **Exh D** | critical |
| **change_mgmt** | Att 2 | Att 2 | *(无独立 Exhibit)* | critical |
| **measurement** | *(附于 Att 6)* | *(附于 Att 6)* | **Exh B** | critical |
| **kp_ld** | Att 5 | Att 5 | **Exh E** | critical |
| **communication** | Att 1 | Att 1 | **Exh F** | medium |
| **owner_refs** | Att 7 | Att 7 | **Exh K** | medium |
| **quality** | Att 4 | Att 4 | **Exh E** | low |
| **hse** | Att 3 | Att 3 | **Exh H** | low |
| **na** | — | — | **Exh G, I** | archive |

> ✅ **3/3 合同验证通过 — Schema v2.0 无需修改。** 不同编号体系只是数据差异。

---

## 结构差异速查

| 维度 | 10.1 CCECC | 10.2 TCC | 12.1 CCECC |
|------|-----------|---------|-----------|
| Exhibit 体系 | Attachment 1–7 | Attachment 1–7 | **Exh A–K** |
| Part II 目录名 | `Part II_Exhibits` | `Part II Atchments` | `Part II_Exhibits` |
| 包数 | 1 (Pkg II) | 2 (Pkg I+III) | 1 (Pkg I) |
| Amdt | 0 | 0 | **1 (Amdt 01)** |
| Performance LD | 无 | 无 | **有** (MEI 特有) |
| Change Mgmt 独立 Exhibit | ✅ Att 2 | ✅ Att 2 | ❌ (附于 Part I SCS) |
| Measurement 独立 Exhibit | ❌ | ❌ | ✅ Exh B |
| KP-LD 位置 | Att 5 | Att 5 | **Exh E** (Quality) |
| NA Exhibit | 无 | 无 | **Exh G, I** |

---

## 跨合同 KP LD 对比

| 合同 | PM | 总人数 | LD/天 | 备注 |
|------|------|:---:|:---:|------|
| 10.1 CCECC | Zhiming Chen | 7 | AED 10,000 | PM 缺位 → active issue |
| 10.2 TCC | Luo Jingbo | 7 | AED 10,000 | 正常 |
| 12.1 CCECC | *(表中未填)* | 7 | AED 10,000 | 人员姓名待补 |

---

## 约定

- **Claude 查询永远用 canonical_type** — 不问 "Exh D 在哪儿"，问 "commercial 对应哪个文件"
- **编号差异只是 display_name** — 全部进入 mapping 表，不在代码中硬编码
- **新增合同时** — 先对比此表，相同 canonical_type 的标记 `commercial_relevance` 应一致
