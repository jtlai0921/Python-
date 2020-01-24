name = ['' for x in range(5)]
score = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
# 輸入資料
for i in range(5):
     print('輸入第 %d 個學生姓名：' %(i+1), end=' ')
     name[i] = input()
     print('輸入國文成績：', end=' ')
     score[i][0] = eval(input())
     print('輸入英語成績：', end=' ')
     score[i][1] = eval(input())
     score[i][2] = (score[i][0] + score[i][1]) / 2
# 氣泡排序法
for loop in range(1,5):
     for index in range(0, (5-loop)):
          if score[index][2] < score[index+1][2]:
               Temp = score[index]
               score[index] = score[index+1]
               score[index+1] = Temp
               nTemp = name[index]
               name[index] = name[index+1]
               name[index+1] = nTemp
# 表列
print()
print('姓名       國文   英語   平均')
print('====================================')
for p in range(5):
     print(name[p], end = '     ')
     print(score[p][0], end = '     ')
     print(score[p][1], end = '     ')
     print(score[p][2])
     


