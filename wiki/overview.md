---
title: 總覽：SSD 為什麼會寫入放大
updated: 2026-11-11
---
# 總覽：SSD 為什麼會寫入放大
1. [NAND 不能覆寫](concepts/nand-no-overwrite.md)：寫過的地方要先擦掉才能再寫。
2. [Page 與 Block](concepts/page-and-block.md)：寫入以 page 為單位，擦除卻要整個 block。
3. [垃圾回收](concepts/garbage-collection.md)：為了擦一個 block，要先把裡面還有用的資料搬走。
4. [寫入放大](concepts/write-amplification.md)：搬家產生的額外寫入，讓 SSD 寫得比使用者要求的多。
5. [壽命](concepts/endurance.md)：額外寫入會用掉有限的 P/E 次數。
6. 怎麼減少：[TRIM](concepts/trim.md) 讓 SSD 少搬沒用的資料；[Over-provisioning](concepts/over-provisioning.md) 預留空白空間。

教學用比喻見 [筆記本比喻](explainers/notebook-analogy.md)。
