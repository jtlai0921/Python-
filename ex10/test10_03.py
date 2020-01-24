import os
def getFirstLine(fName):
    if os.path.isfile(fName):
        with open(fName, 'r') as f:
            return f.readline()
    else:
        return None
    
fName = 'c:/data/stu.txt'
print(getFirstLine(fName))

