datas = {'A001':['汽水',25],'A005':['公主麵',10],
          'A006':['口香糖',8],'A003':['冰棒',20]}
num=input('請輸入貨號：')
if num not in datas:
    print('貨號：{0} 不存在'.format(num))
    name=input('請輸入品名：')
    money=int(input('請輸入售價：'))
    datas[num]=[name,money]
d = datas.get(num)
print('貨號：{0} 品名：{1:s} 售價：{2:d}元'.format(num,d[0],d[1]))
