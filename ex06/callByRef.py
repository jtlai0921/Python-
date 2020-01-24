def Triple(lst):
    for i in range(len(lst)):
        lst[i] = lst[i] * 3
    print('執行 Triple() 函式 ------')
    print('串列 lst = ', lst)
    print()

arr = [2, 4, 6, 8, 10]
print('呼叫 Triple() 函式前 ------')
print('串列 arr = ', arr)
print()
Triple(arr)
print('呼叫 Triple() 函式後 ------')
print('串列 arr = ', arr)

