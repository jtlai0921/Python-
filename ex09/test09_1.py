s1 = input()
set1 = set()
set2 = set()
s2 = s1.split(' ')
for x in s2:
    if(int(x) >= 60):
        set1.add(int(x))
    else:
        set2.add(int(x))
if(set2 == set()):
    print('best case')
else:
    print(max(set2))
if(set1 == set()):
    print('worst case')
else:
    print(min(set1))
