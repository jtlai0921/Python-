f = open('c:/data/invent.txt', 'r')
eof = False
while eof == False:
    line = f.readline()
    if line != '':
        if line != '\n':
            print(line.strip())
    else:
        print("檔案結束")
        eof = True
        f.close()