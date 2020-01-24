def ListSum(arr, n) :
    if (n == 0) :
        return arr[0]
    else :
        return ListSum(arr, n-1) + A[n]

A = [10, -28, 13, 24, -25, 46]
print('A =', A)
print('A 串列各元素數值的總和為', ListSum(A, len(A)-1))