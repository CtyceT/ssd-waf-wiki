---
title: 壽命與 P/E 次數
sources: [S1, S2]
updated: 2026-11-11
---
# 壽命與 P/E 次數
Flash 每個 block 能寫入、擦除的次數有限，寫入放大會更快用掉這些次數。

## 重點
- Flash 能被寫入（program）與擦除（erase）的次數有限，稱為 P/E 次數 [S1-15]。
- WA 越低，代表需要的 P/E 次數越少，所以越理想 [S1-16]。
- GC 搬資料的寫入不是使用者要求的 [S2-7]，但一樣會消耗 P/E 次數。【推論】

## 相關頁面
- [寫入放大](write-amplification.md)
- [NAND 不能覆寫](nand-no-overwrite.md)

## 來源
- [S1](../sources/S1.md)
- [S2](../sources/S2.md)

## 待確認
- 各種 Flash 的實際 P/E 次數：來源沒有提供，簡報不使用。
