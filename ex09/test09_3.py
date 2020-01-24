engs = {1: 'One', 2: 'Two', 3: 'Three'}
num = int(input('請輸入整數：'))
if not num in engs:
    print('抱歉查詢不到')
else:
    print('英文為：' + engs[num])
