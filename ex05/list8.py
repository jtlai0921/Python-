A = [0 for x in range(2)]
print(A)              # 印出 [0,0]
arr = [A for y in range(4)]
print(arr)            # 印出 [[0,0],[0,0],[0,0],[0,0]]

A = [(2*x+1) for x in range(2)]; print(A)     # 印出 [1,3]
arr = [A for y in range(4)]
print(arr)            # 印出 [[1,3],[1,3],[1,3],[1,3]]

arr = [[0 for x in range(2)] for y in range(4)]
print(arr)            # 印出 [[0,0],[0,0],[0,0],[0,0]]
