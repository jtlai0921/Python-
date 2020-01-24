def F(a) :
    if (a < 0) :
        return 1
    else :
        return F(a-2) + F(a-3)
    
print(F(7))