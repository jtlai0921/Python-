emp_pay = [25000, 230000, 36000, 48000]
count = 0
sum = 0
for i in range(len(emp_pay)):
    count = count + 1
    sum += emp_pay[i]
avg = sum / count
print("薪資總金額是:", sum)
print("平均薪資是:", avg)