c = int(input())
list1 = []
for x in range(c):
    s = input()
    list1.append(s.split(' '))
if c == 1:
    list2 = list(range(int(list1[0][0]), int(list1[0][1])))
    print(len(list2))
else:
    set2 = set(range(int(list1[0][0]), int(list1[0][1])))
    set3 = set(range(int(list1[1][0]), int(list1[1][1])))
    set1 = set2 | set3
    for x in range(2, c):
      set1 |= set(range(int(list1[x][0]), int(list1[x][1])))
    print(len(set1))
