def fib (n):
    if (n == 1 or n == 2):
        return 1
    else:          # n >= 3
        return fib(n-1) + fib(n-2)
    
n = 8
print('費氏數列第 %d 項為 %d' %(n, fib(n)))
n = 20
print('費氏數列第 %d 項為 %d' %(n, fib(n)))