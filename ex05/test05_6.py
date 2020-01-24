arr = [x for x in range(10)]
print(arr)

for i in range(9):
    hold = arr[i]
    arr[i] = arr[i+1]
    arr[i+1] = hold

print(arr)
