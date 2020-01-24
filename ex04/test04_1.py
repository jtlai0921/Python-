x = 0
n = 5
for i in range(1, n):
    for j in range(1, n):
        if((i+j) == 2):
            x = x + 2
        if((i+j) == 3):
            x = x + 3
        if((i+j) == 4):
            x = x + 4
print(x)
