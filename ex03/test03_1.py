grade = int(input("請輸入成績："))

if grade>=90 :
    level = 'A'
elif grade>=80 :
    level = 'B'
elif grade>=70 :
    level = 'C'
elif grade>=65 :
    level = 'D'
else :
    level = 'F'

print("成績等級是 :", level)