tuple1 = ('正月','花月','梅月')
print(tuple1)
Jan,Feb,Mar = tuple1
print(Feb)
tuple2 = tuple1 + ('桐月',) 
print(tuple2)
tuple1,tuple2 = tuple2,tuple1
print(tuple1)
print(tuple2)
print(len(tuple1))
del(tuple2)
#print(tuple2) #
list1 = list(tuple1)
list1.append('蒲月')
print(list1)
tuple1 = tuple(list1)
print(tuple1)
print(tuple1[0])
print('正月' in tuple1)
for t in tuple1:
    print(t, end=',')
