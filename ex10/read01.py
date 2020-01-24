import os
fFile = 'c:/data/stu.txt'
if os.path.isfile(fFile):
    f = open(fFile, 'r')
    str1 = f.read(7)
    print(str1)
    print(f.read())
    f.close()
else:
    print('%s 檔案路徑不存在' %fFile)