p = 2
x = int(input('請輸入一個正整數：'))
while p <= x: 
    flag = True 
    for i in range(2, p):
        if p % i == 0: 
            flag = False 
            break 
    if flag == True:
        print(p, end=' ')
    p += 1 
