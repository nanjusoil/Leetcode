1.鴿籠原理，先找出最大最小，再以 最大-最小/n為一個區間，
造出n個bucket，同一個bucket內若有兩個數，則這兩個數彼此之間不可能為maxium gap
故只需將bucket的頭跟bucket的尾比較，即可找出maxium gap