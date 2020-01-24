def average(n1, n2):
    a = (n1 + n2) / 2
    return a 

print('輸入第 1 個整數：' , end='')
num1 = eval(input())
num2 = eval(input('輸入第 2 個整數：'))
avg = average(num1, num2)
print('%d 和 %d 兩整數平均為：%0.1f' %(num1, num2, avg), end = '')
