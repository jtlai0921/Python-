import os
fFile = 'c:/data/stu.txt'
if os.path.isfile(fFile):
    f = open(fFile, 'r')
    lst = f.readlines()
    for lines in lst:
        print(lines.strip())
    f.close()
else:
    print('%s 檔案路徑不存在' %fFile)
