print('%d'%(12345))    #顯示數值「12345」,未設寬度時直接顯示整數資料
print('%8d'%(12345))   #顯示數值「ΔΔΔ12345」,設寬度為8,寬度有剩時補空格(靠右對齊)
print('%-8d'%(-12345)) #顯示數值「-12345ΔΔ」,靠左對齊,寬度有剩時補空格
print('%08d'%(12345)) #顯示數值「00012345」,設寬度為8,寬度有剩時補0
print('%3d'%(-12345))  #顯示數值「-12345」,設寬度為3,寬度不足時全部顯示
print('%c'%('A'))        #顯示字元「A」
print('%4c'%('A'))       #顯示字元「ΔΔΔA」,寬度為4有剩補空格
print('%c'%(65))         #顯示字元「A」,65的ASCII碼為「A」
print('%s'%('ABCDE'))    #顯示字串「ABCDE」
print('%8s'%('ABCDE'))   #顯示字串「ΔΔΔABCDE」,設寬度為8,寬度有剩時補空格(靠右對齊)
print('%3s'%('ABCDE'))   #顯示字串「ABCDE」,寬度不足時全部顯示
print('%6.2s'%('ABCDE')) #顯示字串「ΔΔΔΔAB」,設寬度為6並只顯示2字元