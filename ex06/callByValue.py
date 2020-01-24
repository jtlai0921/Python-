def Triple(x, y):
    x = x * 3
    y = y * 3
    print('執行 Triple() 函式 ------')
    print('x = %d      y = %d' %(x, y))
    print()

x = 10
A = [2, 4, 6, 8]
print('呼叫 Triple() 函式前 ------')
print('x = %d      A[1] = %d' %(x, A[1]))
print()
Triple(x, A[1])
print('呼叫 Triple() 函式後 ------')
print('x = %d      A[1] = %d' %(x, A[1]))

