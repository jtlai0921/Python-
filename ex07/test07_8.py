def GCD(a, b) :
    r =  a % b
    if (r == 0):
        return b
    return GCD(b, r)

print(GCD(48,36))