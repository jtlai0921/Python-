def subpro():
    global n
    n = n + 10
    m = 20
    print('---- subpro -----')
    print('n = %d, m = %d' %(n, m))
    
n = 100
m = 200
print('----- main -----')
print('n = %d, m = %d' %(n, m))

subpro()
print('----- main -----')
print('n = %d, m = %d' %(n, m))

subpro()
print('----- main -----')
print('n = %d, m = %d' %(n, m))