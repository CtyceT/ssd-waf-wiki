---
id: S2
title: Garbage Collection and TRIM in SSDs Explained – An SSD Primer
publisher: The SSD Review（作者 Kent Smith, LSI）
url: https://www.thessdreview.com/daily-news/latest-buzz/garbage-collection-and-trim-in-ssds-explained-an-ssd-primer/
published: 2012-04-16
fetched: 2026-11-11
type: 業界文章
note: 擷取到的頁面只有前半部；文章沒有給頁與區塊的具體大小。
---

## 原文擷取

1. "Flash memory is divided into blocks, which is further divided in pages."
2. "NAND flash memory cannot overwrite existing data"
3. "they must first erase old data before writing new data to the same location."
4. "Data can be written directly into an empty page, but only whole blocks can be erased."
5. "all the valid data from one block must be first copied and written into the empty pages of a new block."
6. "Only then can the invalid data in the original block be erased, making it ready for new valid data to be written."
7. "The writes from this step are not from the host system"
8. "Note that wear leveling typically occurs during GC, as data is written to a variety of new blocks"
9. "When the OS deletes the file, it simply marks the space used for that data as free in its logical data table."
10. "it only becomes aware that the data is deleted (or invalid) when the OS tries to write to that location again."
11. （作者留言，2013-12-24）"Without TRIM the file will appear valid to the SSD controller until the OS uses those same sectors or pages for a new file."
12. （同上）"With TRIM the OS has a way to tell the SSD controller that the file locations can be freed up"
