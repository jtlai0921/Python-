import tkinter as tk
from tkinter import messagebox as msgbox
#定義fnOk函式，當按下確定鈕會執行此函式
def fnOk():
    # 取得學歷的value值，即代表第幾個項目
    index = edu.get();
    # 將結果顯示在lblResult標籤
    result = '{0}{1}的學歷是{2}'.format(name.get(), gender.get() , eduAry[index])
    msgbox.showinfo('個人簡歷', result)

win = tk.Tk()
win.title('選按按鈕範例')
win.geometry('450x150')
# 指定tkinter模組的字串物件name，是txtName文字欄的變數
name=tk.StringVar()   
# 指定tkinter模組的字串物件gender，是radM男和radF女選項按鈕的變數
gender=tk.StringVar()
# 指定tkinter模組的整數物件edu，是國小, 國中, 高中職, 大學, 碩博士選項按鈕的變數
edu=tk.IntVar()

# 建立姓名lblName標籤
lblName = tk.Label(win, text='姓名', padx=10, pady=8)
lblName.grid(row=0, column=0)
# 建立txtName文字欄，此文字欄代表變數為name
txtName = tk.Entry(win, width=10, textvariable=name)
txtName.grid(row=0, column=1)
# 建立性別lblGender標籤
lblGender = tk.Label(win, text='性別', padx=10, pady=8)
lblGender.grid(row=1, column=0)
# 建立radM男和radF女選項按鈕，預設 '男' 選項按鈕被選取
gender.set('先生')
radM = tk.Radiobutton(win, text='男', variable=gender ,value='先生');
radM.grid(row=1, column=1)
radF = tk.Radiobutton(win, text='女', variable=gender ,value='小姐');
radF.grid(row=1, column=2)
# 建立學歷lblEdu標籤
lblEdu = tk.Label(win, text='學歷', padx=10, pady=8)
lblEdu.grid(row=2, column=0)
eduAry=['國小', '國中','高中職','大學', '碩博士']
# 建立學歷選項按鈕，有國小, 國中, 高中職, 大學, 碩博士選項，代表變數為edu
for i in range(5):
    tk.Radiobutton(win, text=eduAry[i], variable=edu, value=i).grid(row=2, column=(1+i))
# 預設 '大學' 選項被選取
edu.set(3)
# 建立btnOk按鈕，按下此鈕會執行fnOk函式
btnOk = tk.Button(win, text='確定', command=fnOk )
btnOk.grid(row=3, column=0)
win.mainloop()

