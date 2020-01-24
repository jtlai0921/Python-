f, i =1.2345, 12345
print(type(f))  #顯示浮點數變值f的類別
f2=float(i)     #用float函式將整數變數i轉成浮點數
print(float(i)) #顯示f2的變數值
print(float.is_integer(f))  #用is_integer()方法檢查變數f是否為整數
print(float.is_integer(f2))  #檢查變數f2是否為整數
print(round(f,2))  #用round()函式將變數f四捨五入到小數二位
print(round(f))    #用round()函式將變數f四捨五入到整數