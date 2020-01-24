def equation(a, b, c):
    d = b**2 - 4*a*c
    boot1 = (-b + d)/(2 * a)
    boot2 = (-b - d)/(2 * a)
    return boot1, boot2

while (1):
    a = eval(input('請輸入第一個係數a：'))
    b = eval(input('請輸入第二個係數b：'))
    c = eval(input('請輸入第三個係數c：'))
    d = b**2 - 4*a*c
    if (d>=0):
        break
    else:
        print('無解, 請重新輸入係數...')
        print()
        
ret = equation(a, b, c)
print('方程式的根為 %0.2f, %0.2f' %(ret[0],ret[1]))
