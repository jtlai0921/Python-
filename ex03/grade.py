score=int(input('請輸入研習的成就分數：'))

if (score>=90 and score<=100) :
    print('研習成績 "優"')
    print('評語：成就非凡')
elif (score>=80 and score<=89) :
    print('研習成績 "甲"')  
    print('評語：表現良好') 
elif (score>=70 and score<=79) :
    print('研習成績 "乙"') 
    print('評語：差強人意') 
elif (score>=60 and score<=69) :
    print('研習成績 "丙"') 
    print('評語：仍須努力') 
elif (score>=0 and score<=59) :
    print('研習成績 "丁"')  
    print('評語：待加強') 
else :
    print('輸入錯誤！')  
    print('分數須在0~100之間')
