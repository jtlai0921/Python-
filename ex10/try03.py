arr = [0 for x in range(5)]
try:
    arr[4] = 40
    print('arr[4] = ', arr[4])
    arr[9] = 90
    print('arr[9] = ', arr[9])
except ZeroDivisionError: 
    print('錯誤類型 : 除數為零')
except IndexError: 
    print('錯誤類型 : 串列註標超出範圍')
except Exception as e:
    print('錯誤類型 :', e)
