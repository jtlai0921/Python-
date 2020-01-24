# 顯示 2 - 19 乘法表
def tables():
    for x in range(2, 20):
        for y in range(1, 20):
            print (x, '*', y, '=', x * y, end = ' ')
        print()
# main
tables()
