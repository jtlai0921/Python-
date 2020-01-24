def F(n) :
    if (n <= 4) :
        return n
    else :
        return n + F(n-3)
    
print(F(14))
