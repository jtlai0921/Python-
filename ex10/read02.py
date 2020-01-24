import os
fFile = 'c:/data/stu.txt'
if os.path.isfile(fFile):
    with open(fFile, 'r') as f:
        str1 = f.readline()
        print(str1, end='')
        str2 = f.readline(7)
        print(str2)
        print(f.read())
else:
    print(None)