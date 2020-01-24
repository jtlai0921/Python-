def stack(arr):
    global n
    m = len(arr)
    print (arr[n], end = '  ')
    if (n >= (m-1)):
        return
    else:
        n = n + 1
        stack(arr)
    n = n - 1
    print (arr[n], end = '  ')
    
n = 0
arr = ['aaa', 'bbb', 'ccc', 'ddd']
stack(arr)