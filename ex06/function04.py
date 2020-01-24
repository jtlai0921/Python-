def printChar(ch, n):
    for i in range(n):
        print ('%s' %ch, end = '')
    print()

ch1 = 'A'
n1 = 12
printChar(ch1, n1)          # 實引數使用變數
printChar('$', 15)          # 實引數使用常值
printChar('B', n1+4)        # 實引數使用常值
    
