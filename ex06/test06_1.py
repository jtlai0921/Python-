import random as R
import time as T

score = 0
t1 = T.time()                 # 計時開始
for i in range(2):
    print('第 %d 題' %(i+1))
    num1 = R.randint(11, 20)  # 亂數製作被乘數 
    num2 = R.randint(1, 10)   # 亂數製作乘數
    right = num1 * num2       # 正確答案
    print('%d * %d = ' %(num1,num2), end='')
    ans = eval(input())       # 測驗者輸入答案
    if (ans == right):
        print('答對了！')
        score += 50
    else:
        print('答錯了！')
        print('正確答案 : %d' %right)
    print()

t2 = T.time()                # 計時結束
print('答題得分 : %d 分' %score)
print('花費時間 : %0.2f 秒' %(t2-t1))
