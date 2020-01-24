import os
fPath = 'c:/data/'
if os.path.exists(fPath):
    print('%s 路徑為資料夾' %fPath)
else:
    print('%s 資料夾路徑不存在' %fPath)
    
fFile = 'c:/Windows/system.ini'
if os.path.exists(fFile):
    print('%s 路徑為檔案' %fFile)
else:
    print('%s 檔案路徑不存在' %fFile) 