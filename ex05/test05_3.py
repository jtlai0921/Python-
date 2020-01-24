arr = [0 for x in range(10)]
for i in range(10):
    arr[(i+2) % 10] = eval(input())
    
print(arr)
