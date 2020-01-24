import random as R
max = 10         # 整數最大值
min = 1          # 整數最小值
num = 8          # 亂數的數量
arr = [0 for x in range(num)]   # 存放所產生的亂數

n = 0       # 串列註標
while (n < num):
    isRepeat = False       # 亂數沒重複
    rnd = R.randint(min, max)   # 產生一個亂數
    for v in arr:         # 讀取串列中元素值 
        if rnd == v:
            isRepeat = True     # 亂數有重複
    if not isRepeat:      # 如果沒有重複
        arr[n] = rnd      # 存放所產生的亂數到串列中
        n += 1
        
for i in range(num):
    print('第 %d 個亂數 : %d' % (i+1, arr[i]))