k = 4
m = 1
for i in range(1, 6):
    for j in range(k):
        print(' ', end='')
    for j in range(m):
        print('*', end='')
    print()
    k = k - 1
    m = m + 2
