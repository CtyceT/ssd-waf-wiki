# Wiki 目錄

主題：SSD 為什麼會寫入放大。先讀 [總覽](overview.md)。

## 概念
- [NAND 不能覆寫](concepts/nand-no-overwrite.md) — 寫過要先擦除 — 2 來源
- [Page 與 Block](concepts/page-and-block.md) — 寫入與擦除單位不同 — 2 來源
- [垃圾回收](concepts/garbage-collection.md) — 為了擦除而搬資料 — 2 來源
- [寫入放大](concepts/write-amplification.md) — 定義、公式、例子 — 3 來源
- [壽命與 P/E 次數](concepts/endurance.md) — 寫入放大如何縮短壽命 — 2 來源
- [TRIM](concepts/trim.md) — 告訴 SSD 哪些資料沒用 — 3 來源
- [Over-provisioning](concepts/over-provisioning.md) — 預留空白空間給 GC — 2 來源

## 教學示意（query 存回）
- [筆記本比喻](explainers/notebook-analogy.md) — 比喻與示意計算，全部標【推論】

## 來源
- [S1 Wikipedia](sources/S1.md) — 最完整的總覽
- [S2 The SSD Review](sources/S2.md) — GC 與 TRIM 步驟
- [S3 Kingston](sources/S3.md) — Over-provisioning
- [S4 SNIA](sources/S4.md) — WAF 標準定義
- [S5 Solidigm](sources/S5.md) — WAF 計算例子
- [S6 Frankie 2012](sources/S6.md) — TRIM 的學術分析
