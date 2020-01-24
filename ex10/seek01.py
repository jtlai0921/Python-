import os
fFile = 'c:/data/stu.txt'
if os.path.isfile(fFile):
    with open(fFile, 'a+') as f:
        f.seek(16)
        str1 = f.readline()
        print(str1, end='')
        f.seek(0)
        str1 = f.readline()
        print(str1, end='')
else:
    print(None)