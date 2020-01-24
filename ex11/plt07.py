import matplotlib.pyplot as plt
font = {'family' : 'DFKai-SB'}  
plt.rc('font', **font)

listIYearX = [2014, 2015, 2016, 2017, 2018, 2019]

listIPhoneY = [43000, 31000, 70500, 68000, 85000, 24000]
plt.bar(listIYearX, listIPhoneY,  label="iPhone")

listAsusY = [23000, 36000, 40500, 58000, 65000, 44000]
plt.bar(listIYearX, listAsusY, bottom=listIPhoneY ,label="ASUS")

listY = [0,0,0,0,0,0]
for n in range(0, 6, 1):
    listY[n] = listIPhoneY[n] + listAsusY[n]
listMiY = [13000, 26000, 50500, 68000, 75000, 54000]
plt.bar(listIYearX, listMiY, bottom=listY, label="小米")

plt.title("手機歷年銷售量")
plt.xlim(2013, 2020)
plt.ylim(0, 300000)
plt.xlabel('年度')
plt.ylabel('銷售量')
plt.legend()
plt.grid(True)
plt.show()
