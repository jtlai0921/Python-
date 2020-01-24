import os
if os.path.isfile('myFile.txt'):
    f = open('myFile.txt')
    print(f.read())
    f.close()

f = open('myFile.txt', 'a+')
f.write('The over')
f.close()