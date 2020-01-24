a = [0 for x in range(100)]
b = [0 for x in range(100)]

for i in range(100):
    b[i] = i
a[0] = 0
for i in range(1,100):
    a[i] = b[i] + a[i-1]
print(a[50] - a[30])
