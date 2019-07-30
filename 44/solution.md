1.去頭去尾，讓pattern轉成*號開頭*號結尾的形式
如果不能去頭去尾，就一定不match

2.轉完後，去match第一個星號跟第二個星號間的pattern(greedy match最前面的，因為最後打算用*cover剩餘的字串)，一路match星號間的pattern下去即可