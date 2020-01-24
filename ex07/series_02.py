def g(n):
    if n <= 0:
        return 0
    elif (n % 2 == 0):     # n > 0,為偶數
        return -n + g(n-3)
    else:                  # n > 0,為奇數 
        return n + g(n-3) 

while True:
    n = eval(input('n = '))
    if (n % 3 == 1):
        break
    else:
        print('輸入資料不符, 請重新輸入...')
        
sum = g(n)
if (n % 2 == 1):         # n輸入值為奇數
    print ('1 – 4 + 7 – 10 + ... – %d + %d = %d' %(n-3, n, sum))
else:                    # n輸入值為偶數
    print ('1 – 4 + 7 – 10 + ... + %d - %d = %d' %(n-3, n, sum))