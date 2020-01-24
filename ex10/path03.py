import os
fPath = 'c:/data/'
if os.path.exists(fPath):
    print('%s 路徑已存在,不必再建立' %fPath)
else:
    print('%s 路徑不存在' %fPath)
    os.mkdir(fPath)
    print('%s 資料夾建立成功' %fPath)
