set1 = {1,2,3}
set2 = {3,4}
print(set1 | set2)
print(set1.union(set2))
print(set1 & set2)
print(set1.intersection(set2))
print(set1 - set2)
print(set1.difference(set2))
print(set1 ^ set2)
print(set1.symmetric_difference(set2))
set1 = {1,2}
set2 = {1,2,3}
print(set1 <= set2)
print(set1.issubset(set2))
print(set1 >= set2)
print(set1.issuperset(set2))
