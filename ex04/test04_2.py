for i in range(3):
    j = 0
    while(j < i):
        print(' ', end='')
        j += 1
    k = 6 - 2 * i
    while(k > 0):
        print('*', end='')
        k -= 1
    print()
