A = [0 for x in range(5)]
B = [0 for x in range(5)]

for i in range(1, 5):
    A[i] = 2 + i * 4
    B[i] = i * 5
C = 0
for i in range(1, 5):
    if B[i] > A[i]:
        C = C + (B[i] % A[i])
    else:
        C = 1
    print('%3d   %3d   %3d' %(A[i],B[i],C))
          
print(C)
