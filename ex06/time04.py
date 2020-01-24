import time as T
t1 = T.time()
print('暫停前電腦時間:',t1)
T.sleep(5)
t2 = T.time()
print('暫停後電腦時間:',t2)
print('程式暫停了%f秒' %(t2-t1))
