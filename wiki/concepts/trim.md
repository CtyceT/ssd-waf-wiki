---
title: TRIM
sources: [S1, S2, S6]
updated: 2026-11-11
---
# TRIM：主動告訴 SSD 哪些資料沒用了
作業系統刪檔時順便通知 SSD，讓 SSD 不必再搬那些已經沒用的資料。

## 重點
- 沒有 TRIM 時，作業系統刪檔只改自己的表格，SSD 不知道資料已經沒用 [S2-9][S2-10]。
- 所以在作業系統重新使用那個位置之前，SSD 會一直把那份檔案當成有效資料 [S2-11]。
- 有 TRIM 時，作業系統會把不再有效的位置告訴 SSD [S1-12][S2-12]。
- SSD 因此知道這些位置可以擦除、重新使用 [S1-13]。
- 研究指出 TRIM 等於增加了 SSD 的 over-provisioning [S6-1]。
- 例：10% 的請求是 TRIM 時，原本沒有預留空間的 SSD，等效預留比例會變成 0.11 [S6-2]。

## 來源
- [S1](../sources/S1.md)
- [S2](../sources/S2.md)
- [S6](../sources/S6.md)

## 相關頁面
- [垃圾回收](garbage-collection.md)
- [Over-provisioning](over-provisioning.md)

## 待確認
- 無
