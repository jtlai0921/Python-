def createList(n):
    lst = [0 for i in range(n)]
    import random
    for j in range(n):
        lst[j] = random.randint(-100, 100)
    return lst

def absList(A):
    for k in range(len(A)):
        A[k] = abs(A[k])

arr = createList(5)
print ('建立的串列為：', arr)
absList(arr)
print ('串列絕對值為：', arr)
        
