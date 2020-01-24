import matplotlib.pyplot as plt
# 建立font字體物件，DFKai-SB表示指定字體為標楷體
font = {'family' : 'DFKai-SB'}  
# 指定plt繪製圖表的字體物件為font，因為圖表的字體會以標楷體呈
plt.rc('font', **font) # pass in the font dict as kwargs

listX = [2014, 2019]
listY = [0, 100000]

plt.plot(listX, listY, color='blue', ls='-.', lw=4, label="歷年銷售量")
plt.legend()
plt.show()