no=[1,2,3,4]               # 編號
score = [[87,64,88],[93,72,86],[80,88,89],[79,91,90]]     # 成績
print('編號   語文   數理   智力   總分')
print('================================')
for i in range(len(no)):
    print('%2d' %no[i], end = '     ')
    hSum = 0
    for j in range(len(score[i])):
        print('%3d' %score[i][j], end = '    ')
        hSum += score[i][j]
    print('%3d' %hSum)
    
print('%s' %'平均', end = '   ')
for j in range(3):
    vSum = 0
    for i in range(len(no)):
        vSum += score[i][j]
    print('%4.1f' %(vSum/len(no)), end = '   ')
