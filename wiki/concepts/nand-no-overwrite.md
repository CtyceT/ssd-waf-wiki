---
title: NAND Flash 不能直接覆寫
sources: [S1, S2]
updated: 2026-11-11
---
# NAND Flash 不能直接覆寫
SSD 裡存資料的 NAND Flash 寫過的地方不能直接改，要先擦掉才能再寫。

## 重點
- NAND Flash 不能直接覆寫既有資料 [S2-2]。
- 要在同一個位置寫新資料，必須先把舊資料擦除 [S2-3][S1-3]。
- 而且「寫入」和「擦除」的單位大小不同，細節見 Page 與 Block [S1-4][S1-5]。
- Flash 能被寫入、擦除的次數有限 [S1-15]。

## 相關頁面
- [Page 與 Block](page-and-block.md)
- [壽命與 P/E 次數](endurance.md)

## 來源
- [S1](../sources/S1.md)
- [S2](../sources/S2.md)

## 待確認
- 無
