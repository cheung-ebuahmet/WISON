# _Tools — 脚本与自动化工具

> 所有 Claude Code 辅助脚本的集中存放处。
> 每个脚本应该是自包含的、可独立运行的。

---

## 脚本清单

| 脚本 | 功能 | 状态 |
|------|------|:---:|
| `kb_gap_analysis.py` | Main_Contract ↔ kb/ 文件映射 + OCR 缺口检测 | ✅ |

---

## 运行方式

```bash
python D:\Wison\_Tools\<script_name>.py
```

---

## 开发约定

1. **自包含** — 不依赖其他脚本，不假设 CWD
2. **仅读取证据层** — 脚本可读取 `Main_Contract/`、`Subcon_Payments/`，不写入
3. **输出到 _Ref** — 产出的 .md / .yaml 写回 `_Ref/`
4. **命名** — `{功能描述}_{snake_case}.py`
