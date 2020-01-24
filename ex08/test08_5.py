sum = count = 0
avg = 0.0
while (1):
    rating = float(input('請輸入評審給分(1～5)，[結束程式請輸入-1]'))
    if rating == -1:
        break
    sum += rating
    count += 1
avg = sum/count
print('該作品平均得分:' + format(avg,'.2f'))
