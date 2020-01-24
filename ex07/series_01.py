def f(n):
    if n <= 0:
        return 0
    else :               # n > 0
        return n + f(n-1)
    
n = 100
sum = f(n)
print('%d + %d + … + 3 + 2 + 1 = %d' %(n, n-1, sum))
    