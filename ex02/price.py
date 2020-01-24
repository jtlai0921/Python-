name=input('請輸入商品名稱：')
num=int(input('請輸入商品數量：'))
price=float(input('請輸入商品單價：'))
print('%-10s%03d件\t總價%.1f元'%(name,num,num*price))