import matplotlib.pyplot as plt

listX = [2014, 2019]
listY = [0, 100000]

plt.plot(listX, listY, color='blue', ls='-.', lw=4, label="Sales volume")
plt.legend()
plt.show()