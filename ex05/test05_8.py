n = 10
A = [6 for y in range(n)]
p = A[0]
q = A[0]
for i in range(n):
    if A[i] > p:
        p = A[i]
    if A[i] < q:
        q = A[i]

print('%3d  %3d ' %(p, q))
