---
title: 垃圾回收（Garbage Collection, GC）
sources: [S1, S2]
updated: 2026-11-11
---
# 垃圾回收（GC）
SSD 為了騰出可以擦除的 block，自己在背景把還有用的資料搬家的過程。

## 重點
- 刪除檔案時，作業系統只在自己的表格上把那塊空間標成「空的」[S2-9]。
- SSD 要等作業系統之後再寫到同一個位置，才知道那筆資料已經沒用 [S2-10]。
- 要回收一個 block，必須先把裡面還有效的資料複製到另一個新 block 的空 page [S2-5][S1-6]。
- 複製完之後，才能把原本的 block 整個擦除，留給新資料使用 [S2-6][S1-7]。
- GC 搬資料產生的寫入不是使用者要求的 [S2-7]。
- 平均磨損（wear leveling）通常也在 GC 時一起進行 [S2-8]。

## 相關頁面
- [Page 與 Block](page-and-block.md)
- [寫入放大](write-amplification.md)

## 來源
- [S1](../sources/S1.md)
- [S2](../sources/S2.md)

## 待確認
- 無
