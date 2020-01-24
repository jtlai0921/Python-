def subpro():
    v1 = 31
    v3 = 33
    print('----- 變數(全域,區域) -----')
    print('v1 = %d, v2 = %d, v3 = %d' %(v1,v2,v3))
    print()

v1 = 100
v2 = 200
print('----- 變數(全域) -----')
print('v1 = %d, v2 = %d' %(v1,v2))
print()
subpro()
print('----- 變數(全域) -----')
print('v1 = %d, v2 = %d' %(v1,v2))
#print('v1 = %d, v2 = %d, v3 = %d' %(v1,v2,v3))  # 錯誤敘述
