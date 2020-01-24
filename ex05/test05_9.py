A = [[1,1,1],[2,2,2],[3,3,3,3],[4,4,4,4]]
M = 4
N = 3
rowSum = 0
for i in range(M):
     for j in range(N):
         rowSum = rowSum + A[i][j]
     print('The sum of row %d is %d.' %(i, rowSum))
