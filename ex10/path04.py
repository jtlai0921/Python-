import os
fPath = 'c:/data/'
if os.path.exists(fPath):
    print('%s 路徑目前存在' %fPath)
    os.rmdir(fPath)
    print('%s 路徑已刪除' %fPath)
else:
    print('%s 路徑不存在' %fPath)