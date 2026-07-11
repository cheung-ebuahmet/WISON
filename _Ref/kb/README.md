# kb/ — 合同知识库（衍生层）

> 镜像 `Main_Contract\` 的目录结构。本层只存 OCRed 产物（.md / .csv），**不含二进制文件**。

## 来源

`Main_Contract/` 中每个有文字层的 PDF → 经 OCR/转换 → 生成同名 `.md` 文件，存放到此处。

## 规则

| 来源 | 产物 | 位置示例 |
|------|------|---------|
| `Main_Contract/ANX 03_SOW/ANX03_ADR-001_..._ocred.pdf` | → `.md` | `kb/ANX 03_SOW/ANX03_ADR-001.md` |
| `Main_Contract/ANX 10_.../Exh B.01_..._ocred.pdf` | → `.md` | `kb/ANX 10_Execution Requirements/ANX10_Exh B.01.md` |

- 文件名去掉 `_ocred` / `_Signed` 及扩展名，加 `.md`
- xlsx 转 `.csv`（一 Sheet 一个）
- 目录结构永远与 `Main_Contract/` 保持镜像同步

## 与 `wiki/` 的区别

| | `kb/` | `wiki/` |
|------|-------|---------|
| 生成方式 | 自动 OCR 产物 | 人工撰写 |
| 内容 | 原文逐页转录 | 分析、摘要、交叉引用 |
| 可再生成 | ✅ 从 raw 重新跑 OCR 即可 | ❌ 人工知识不可再生成 |
