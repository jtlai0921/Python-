import tkinter as tk

#定義fnOk函式，當按下確定鈕會執行此函式
def fnOk():
    vName = name.get()
    vScore=score.get()
    if vScore>=90 :
        level = 'A'
    elif vScore>=80 :
        level = 'B'
    elif vScore>=70 :
        level = 'C'
    elif vScore>=65 :
        level = 'D'
    else :
        level = 'F'
    lblResult['text'] = '{0}成績是{1},等級是{2}'.format(vName, vScore , level)

win = tk.Tk()
win.title('按鈕範例')
win.geometry('110x120')
# 指定tkinter模組的字串物件name，是txtName文字欄的變數
name=tk.StringVar()   
# 指定tkinter模組的整數物件score，是txtScore文字欄的變數
score = tk.IntVar()
# 建立lblName標籤
lblName = tk.Label(win, text='姓名', padx=10, pady=8)
lblName.grid(row=0, column=0)
# 建立txtName文字欄，此文字欄代表變數為name
txtName = tk.Entry(win, width=15, textvariable=name)
txtName.grid(row=0, column=1)
# 建立lblScore標籤
lblScore = tk.Label(win, text='分數', padx=10, pady=8)
lblScore.grid(row=1, column=0)
# 建立txtScore文字欄，此文字欄代表變數為score
txtScore = tk.Entry(win, width=15, textvariable=score)
txtScore.grid(row=1, column=1)
# 建立btnOk按鈕，按下此鈕會執行fnOk函式
btnOk = tk.Button(win, text='確定', command=fnOk )
btnOk.grid(row=2, column=0)
# 建立lblResult標籤
lblResult = tk.Label(win, text='', padx=10, pady=8)
lblResult.grid(row=2, column=1)
win.mainloop()

