n = int(input('請輸入數值：'))
d = '0'
if n > -10 and n < 10 :
    d='1'
elif n > -100 and n < 100 :
    d='2'
else :
    d='>2'
print(d + ' 位數')