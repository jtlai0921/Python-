import matplotlib.pyplot as plt
font = {'family' : 'DFKai-SB'}  
plt.rc('font', **font)

listPercent = [15.5, 18, 34.5, 7, 25]
listBooks = ['七龍珠', '火影忍者', '航海王', '第一神拳', '多啦A夢']
listColors = ['red', 'green', 'blue', 'purple', 'yellow']
listExplode=(0, 0, 0.2, 0, 0.1)

plt.pie(listPercent, labels=listBooks, colors=listColors, 
        explode=listExplode, labeldistance=1.1, autopct='%3.1f%%', 
        pctdistance=0.6, startangle=180)


plt.legend()
plt.show()