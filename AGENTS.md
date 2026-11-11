# AGENTS.md — SSD 寫入放大 LLM Wiki 與教學簡報

本專案依 Karpathy 的 LLM Wiki 模式建立：**raw（原始資料）→ wiki（LLM 維護的知識庫）→ slides（由 wiki 產生的教學簡報）**。
這份文件是 schema：規定 wiki 的結構、引用方式、工作流程（graph）與檢查規則。任何 AI 修改本專案前都要先讀完。

---

## 1. 三層結構

| 層 | 位置 | 誰寫 | 規則 |
|---|---|---|---|
| 原始資料 | `raw/S#-*.md` | 擷取工具 | **不可修改**。只放原文擷取句，每句編號 |
| Wiki | `wiki/` | LLM | 只能根據 raw 撰寫；每個重點都要引用 |
| 簡報 | `slides/` | LLM | 只能根據 wiki 撰寫；不可直接引用 raw 或外部知識 |

## 2. 引用規則（最重要）

- 引用格式：`[S2-5]` = `raw/S2-*.md` 的第 5 句擷取。
- Wiki 概念頁的「## 重點」區，**每一條**都必須以至少一個引用結尾；沒有來源、由 LLM 推出的內容要改標 `【推論】`。
- 擷取有問題的內容（亂碼、工具自行加入的數字）**不得使用**，改列在該頁的「## 待確認」。
- 「廠商宣稱」要寫明是宣稱，例如「SandForce 宣稱可達 0.5 [S1-18]」。

## 3. Wiki 檔案

```
wiki/
├── index.md          所有頁面的目錄（每頁一行：連結 — 一句話說明 — 來源數）
├── log.md            只能附加的工作紀錄
├── overview.md       全主題導覽
├── sources/S#.md     每篇來源一頁：內容摘要、可靠度、被哪些概念頁使用
├── concepts/*.md     概念頁
└── explainers/*.md   查詢產生的教學示意（比喻、示意計算），一律標【推論】
```

概念頁格式：
```markdown
---
title: 垃圾回收（Garbage Collection, GC）
sources: [S1, S2]
updated: 2026-11-11
---
# 垃圾回收（GC）
一句白話定義。
## 重點
- 每條都以引用結尾 [S1-6]
## 相關頁面
- [寫入放大](write-amplification.md)
## 待確認
- （沒有就寫「無」）
```

`log.md` 每筆以固定前綴開頭，方便用 `grep "^## \[" wiki/log.md` 查詢：
```
## [2026-11-11] ingest | 來源標題
## [2026-11-11] lint | 結果摘要
## [2026-11-11] query | 問題
## [2026-11-11] slides | 結果摘要
```

## 4. 三個操作

- **ingest**：新增一篇 raw → 寫 `sources/S#.md` → 更新或新增概念頁 → 更新 `index.md` → 在 `log.md` 附加紀錄。
- **query**：先讀 `index.md` 找相關頁面，再讀頁面回答並附引用。有用的回答（例如教學比喻）要存回 `explainers/`。
- **lint**：執行 `python3 tools/lint_wiki.py`，修正所有錯誤後在 `log.md` 記錄。

## 5. 簡報產生流程（graph）

```
N1 取得資料(ingest) ─▶ N2 撰寫 Wiki ─▶ N3 Lint 檢查 ──失敗──▶ 回 N2
                                         │通過
                                         ▼
                 N4 查詢 Wiki、產生大綱 slides/plan.md
                                         │
                                         ▼
                 N5 覆蓋檢查：大綱每張投影片需要的內容 Wiki 都有嗎？
                       ├─ 缺內容 ─▶ 回 N1（找新來源）或 N2（補頁面）
                       └─ 需要比喻、示意計算 ─▶ 先存成 explainers/（N2），再回 N3
                                         │通過
                                         ▼
                 N6 產生 HTML 簡報 slides/index.html
                                         │
                                         ▼
                 N7 簡報檢查 tools/check_slides.py
                       ├─ 數字或引用錯 ─▶ 回 N6（若 Wiki 本身缺，回 N2）
                       └─ 教學結構錯 ─▶ 回 N4
                                         │通過
                                         ▼
                 N8 人工審閱 ─▶ 發布
```

- 每個回圈最多重試 2 次；第 3 次仍失敗就停下來交給人判斷。
- **workflow v2（第 1 次執行後的修改）**：
  1. N3 lint：來源沒被任何概念頁使用，從「警告」改為「錯誤」。必須寫成概念頁，或在來源頁註明「不使用：原因」。
  2. 討論階段：決定簡報結構時，立刻列出每個段落需要哪些 Wiki 頁，不要等到 N5 才發現缺口。
  3. N1 ingest：擷取結果中的數字必須逐字出現在原文引號內；擷取工具自己算的數字一律排除。
  4. N7：檢查工具要自我驗證（解析到的張數必須等於 HTML 的張數）。
  5. N8：人工審閱必須包含手機直向與橫向的截圖。
- 每次節點失敗與修正都要記在 `wiki/log.md`。

## 6. 簡報規則

- 檔案：`slides/index.html`，單一 HTML，不需建置；鍵盤 ← → 或點按鈕換頁。
- 觀眾：**完全沒學過的非資工同學**。不出現 FTL、LBA 等縮寫，除非當頁有白話解釋。
- 結構：每張 `<section class="slide">` 都要有 `data-part`，依序涵蓋 `問題 → 原理 → 代價 → 解法 → 測驗 → 總結`。
- 每張投影片都要有 `data-wiki="concepts/x.md,..."`，列出內容來自哪些 Wiki 頁，並在頁尾顯示來源。
- **簡報上的每個數字都必須能在 `data-wiki` 列出的頁面中找到**。比喻用的示意數字要先存進 `explainers/`。
- 總張數 10～16 張。

## 7. 指令

```bash
python3 tools/lint_wiki.py      # N3：檢查 Wiki
python3 tools/check_slides.py   # N5 + N7：檢查大綱覆蓋與簡報
python3 -m http.server 8000     # 本機預覽 http://localhost:8000/slides/
```
