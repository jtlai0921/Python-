def f(A, n):
    index = 0
    for i in range(n):
        if A[i] >= A[index]:
            index = i
            print(index)
    return index

A = [1,3,9,2,5,8,4,9,6,7]
print(f(A, 10))
