import decimal  #匯入decimal模組
f1,f2=10.0,3.0  #宣告f1、f2變數並指定變數值為浮點數10.0和3.0
d1=decimal.Decimal(10)    #宣告d1為decimal型別變數，值為整數常值10
d2=decimal.Decimal('3.0') #宣告d2為decimal型別變數，值為字串常值'3.0'
print(type(d1))  #顯示d1變數的類別
print(f1/f2)     #顯示f1除以f2的值
print(d1/d2)     #顯示d1除以d2的值
d3=decimal.Decimal('2.345')  #宣告d3為decimal型別變數，值為字串常值'2.345'
d4=decimal.Decimal('6.78')
print(d3+d4)
print(d3*d4)