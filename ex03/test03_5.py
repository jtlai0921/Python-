name = input('輸入英文名:') 
if name.lower() == name :
    print(name + ' 英文名全部小寫')
elif name.upper() == name : 
    print(name + ' 英文名全部大寫')
else :
    print(name + ' 英文名大小寫混合')