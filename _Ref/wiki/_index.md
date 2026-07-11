# WISON Wiki — 合同知识库

> **Karpathy 模式 Layer 2：** LLM 维护的 Markdown 知识图谱
> — 由 `data/contracts/*.yaml` 和 `data/clause-library/` 编译生成。人手只补充分析，不重复填写数据。
>
> 最后更新：2026-07-09

---

## 按主题浏览

| 页面 | 描述 | 状态 |
|------|------|:---:|
| **Commercial/** | | |
| [[Commercial/Liquidated-Damages]] | 误期损害赔偿：触发→计算→各层对比 | 🟡 |
| [[Commercial/Subcontractor-Matrix]] | 四大分包商对比一览 | 🟡 |
| **Contracts/** | | |
| [[Contracts/EPC-Contract-Structure]] | ADNOC EPC 总包合同完整架构 | 🟢 |
| **Engineering/** | | |
| [[Engineering/Performance-Guarantee]] | 性能保证条款：总包→分包背靠背 | 🟢 |
| **HSE/** | | |
| [[HSE/HSE-Obligations]] | HSE 义务：ANX 12 → 分包 HSE 映射 | 🟢 |
| **Insurance/** | | |
| [[Insurance/Insurance-Requirements]] | 保险要求：ANX 07 → 分包背靠背 | 🟢 |

---

## 合同层级

```
ADNOC (Employer)
  └── Wison (Contractor) — EPC Agrmt (FIDIC Silver Book)
        ├── 10.1 CCECC — Civil Pkg II
        ├── 10.2 TCC — Civil Pkg I & III
        ├── 12.1 CCECC — MEI Pkg I
        ├── 12.2 TCC — MEI Pkg II
        └── METS Lab — Lab Testing (pre-qualification)
```

---

## Wiki 约定

- `[[Page-Name]]` = 内部 wiki 链接（WikiLink 语法）
- `→` = 指向原始文件的精确路径（相对于 `D:\Wison`）
- **粗体** = 关键定义或数字（来源：`data/contracts/*.yaml`）
- `🟢 完整 ⚠️ 部分 🔴 缺失` = 文件完整度标记（来源：`tasks/kb-status.md`）

---

## 数据来源

> ⚠️ **Wiki 不保存独立事实。** 所有数值、金额、日期找 YAML；所有条款解释找 clause-library；wiki 仅做展示与导航。
>
> - 合同事实: `_Ref/data/contracts/`
> - 条款规则: `_Ref/data/clause-library/`
> - 建设状态: `_Ref/tasks/kb-status.md`
