str = input()
A = 0
B = 0
c = 0
d = len(str) % 2
for i in str:
    c += 1
    if(c % 2 == d):
        A += int(i)
    else:
        B += int(i)
if(A > B):
    print(A - B)
else:
    print(B - A)
    
