age = int(input('請輸入年齡：'))
data = input('是否就學(y|n)：')
if data=='y':
    school=True
else:
    school=False
pay = 0
if age >= 5 and school == True: 
    pay = 10
elif age >= 5 and school == False:
    if age <=17:
        pay = 20
    else :
        pay = 50
print('入場費', pay)