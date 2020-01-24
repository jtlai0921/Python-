name = input('選手姓名：')
score = 0.0
count = 0
total = 0.0
while(score != -1):
    score = float(input('輸入你投擲距離：(輸入-1結束程式)'))
    if(score == -1):
        break
    total += score
    count += 1
    average = total / count
    print('{0:>20s},你的平均成績是:{1:5.1f}'.format (name, average))
