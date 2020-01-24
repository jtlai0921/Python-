import os
fPath = 'c:/data/'
if not os.path.exists(fPath):
    os.mkdir(fPath)
f = open('c:/data/stu.txt', 'a')
f.write('\n趙七海, 66, 87')
f.write('\n陳九東, 83, 88')
f.flush()
f.close()