datas = [['王一',98,75],['林二',86,64],['張三',49,52],['李四',78,85]]
print('姓  名','筆試','術科','總分')
for d in datas:
    name, s1, s2 = tuple(d)
    print('{0:5s}{1:4d}{2:4d}{3:4d}'.format(name,s1,s2,s1+s2))
