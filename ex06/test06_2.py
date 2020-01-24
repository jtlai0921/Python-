def Max(array):
    bigger = array[0]
    for i in range(len(array)):
        if (array[i] > bigger):
            bigger = array[i]
    return bigger

lstA = [2, 4, 10, 8 ,6]
lstB = [-13, 17, 5]
maxA = Max(lstA)
print('串列 lstA 的最大數：%d' % maxA)
maxB = Max(lstB)
print('串列 lstB 的最大數：%d' % maxB)
if(maxA > maxB):
    biggest = maxA
else:
    biggest = maxB
print('兩串列的最大數為：%d' %biggest)
