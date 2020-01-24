lst = [0 for x in range(5)]
print('請依序輸入5個整數...')
for i in range(5):
    print('輸入第 %d 個元素內容：' %(i+1), end = '')
    lst[i] = eval(input())

max = lst[0]
for item in lst:
    if max < item :
        max = item
        
print()
print('最大值為', max)
