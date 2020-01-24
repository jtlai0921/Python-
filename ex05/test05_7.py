arr = [y for y in range(10)]
print(arr)
sum = 0
for i in range(1, 9):
    sum = sum - arr[i-1] + arr[i] + arr[i+1]
print(sum)

