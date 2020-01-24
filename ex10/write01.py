import os
fPath = 'c:/data/'
if not os.path.exists(fPath):
    os.mkdir(fPath)
f = open('c:/data/stu.txt', 'w')
f.write('王一心, 85, 90\n')
f.write('張三飛, 75, 87\n')
f.write('周五瑞, 92, 71')
f.flush()
f.close()