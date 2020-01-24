lst4 = [10, 21, 32, 43, 54, 65, 76, 87, 98]      
for i in range(len(lst4)):
    print(lst4[i], end = ' ')    # 印出 10 21 32 43 54 65 76 87 98
print()
for j in range(1, 4):
    print(lst4[j], end = ' ')    # 印出 21 32 43
print()
for k in range(5, len(lst4)):
    print(lst4[k], end = ' ')    # 印出 65 76 87 98
print()
for m in range(len(lst4)-1, 5-1, -1):
    print(lst4[m], end = ' ')    # 印出 98 87 76 65
print()
for g in range(0, len(lst4), 2):
    print(lst4[g], end = ' ')    # 印出 10 32 54 76 98


