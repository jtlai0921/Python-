import matplotlib.pyplot as plt

font = {'family' : 'DFKai-SB', 'size':'13'}  
plt.rc('font', **font) 

listX = [2014, 2015, 2016, 2017, 2018, 2019]
listY = [43000, 31000, 70500, 68000, 85000, 24000]
plt.plot(listX, listY, color='blue', ls='--', lw=6, label="iPhone歷年銷售量")

plt.title("手機歷年銷售量")
plt.xlim(2013, 2020)
plt.ylim(0, 110000)
plt.xlabel('年度')
plt.ylabel('銷售量')
plt.legend()
plt.show()