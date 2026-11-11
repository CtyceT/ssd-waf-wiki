---
title: Over-provisioning（OP，預留空間）
sources: [S1, S3]
updated: 2026-11-11
---
# Over-provisioning：預留使用者看不到的空白空間
SSD 廠商故意保留一部分容量不給使用者用，留給 GC 當工作區。

## 重點
- 廠商可以保留一部分硬碟容量作為 over-provisioning [S3-1]。
- OP 比例 =（實體容量 − 使用者容量）÷ 使用者容量 [S3-2]。
- 這些空間是 GC 的臨時工作區，用來搬有效資料、回收 block [S3-5]。
- 預留空間可以降低寫入放大，並提升壽命與效能 [S1-8][S1-9]。
- 保留較多空白 block 能讓效能比較穩定 [S3-6]；OP 比例越高，SSD 可用得越久 [S3-7]。
- Kingston 的產品：讀取密集型一般 7%，寫入密集型一般 28% [S3-3]；寫入較多的應用建議 32% [S3-4]。
- Wikipedia 列出常見的設定為 0%、7%、14%、28% [S1-11]。

## 來源
- [S1](../sources/S1.md)
- [S3](../sources/S3.md)

## 相關頁面
- [垃圾回收](garbage-collection.md)
- [TRIM](trim.md)

## 待確認
- S1 第 10 句（GB 與 GiB 差 7.37% 的算式）擷取後為亂碼，不使用。依討論決定，簡報不解釋 7% 的由來。
