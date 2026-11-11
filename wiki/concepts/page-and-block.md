---
title: Page 與 Block
sources: [S1, S2]
updated: 2026-11-11
---
# Page 與 Block：寫入和擦除的單位不一樣
Flash 以小單位 page 寫入，卻只能以大單位 block 擦除；這個「大小不一致」就是寫入放大的根源。

## 重點
- Flash 分成很多 block，每個 block 再分成很多 page [S2-1]。
- 寫入的單位是 page [S1-4]。
- 擦除的單位是比較大的 block，一個 block 由多個 page 組成 [S1-5]。
- 資料可以直接寫進空的 page，但只能整個 block 一起擦除 [S2-4]。

## 相關頁面
- [NAND 不能覆寫](nand-no-overwrite.md)
- [垃圾回收](garbage-collection.md)

## 來源
- [S1](../sources/S1.md)
- [S2](../sources/S2.md)

## 待確認
- page、block 的實際大小：S1、S2 的擷取都沒有提供，簡報不使用具體大小。
