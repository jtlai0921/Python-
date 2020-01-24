import os
def readFile(fName):
    line = None
    if os.path.isfile(fName):
        data = open(fName, 'r')
        while line != '':
            line = data.readline()
            print(line)
            
readFile('c:/data/stu.txt')