i1=10
f1=float(i1) #使用float()函式將整數轉型為浮點數
print(i1,f1,type(f1))
f2=1234.5678
i2=int(f2)   #使用int()函式將浮點數轉型為整數(捨棄小數)
print(f2,i2,type(i2))
i3=round(f2) #使用round()函式將浮點數轉型為整數(四捨五入)
print(f2,i3,type(i3))
s=str(i2)    #使用str()函式將整數轉型為字串
print(s,type(s))
b=bool(f1)   #使用bool()函式將浮點數轉型為布林值
print(b,type(b))
