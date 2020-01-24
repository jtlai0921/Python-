age = int(input("請輸入年齡："))
if age == None: 
    level = 'C'
elif age < 13 :
    level = 'C'
elif age < 18 :
    level = 'T'
else :
    level = 'A'
print("年齡分級是 :", level)