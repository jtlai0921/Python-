import tkinter as tk
from tkinter import messagebox as msgbox

def fnOk():
    data = ''
    total = 0
    for i in isfoodCheckAry:
        if isfoodCheckAry[i].get() == True:
            data += foodAry[i] + ", "
            total += priceAry[i]
    result = '{0}您好，你選購的餐點為{1}，總共{2}元'.format(name.get(), data , total)
    msgbox.showinfo('點餐結果', result)

win = tk.Tk()
win.title('核取按鈕範例')
win.geometry('500x130')
name=tk.StringVar()   
lblName = tk.Label(win, text='姓名', padx=10, pady=8)
lblName.grid(row=0, column=0)
txtName = tk.Entry(win, width=10, textvariable=name)
txtName.grid(row=0, column=1)

lblFood = tk.Label(win, text='餐點', padx=10, pady=8)
lblFood.grid(row=1, column=0)
isfoodCheckAry={}
foodAry=['牛肉堡餐', '豬肉堡餐','雞腿堡餐', '香魚堡餐', '招牌堡餐']
priceAry=[120, 110, 130, 90, 150]
for i in range(5):
    isfoodCheckAry[i] = tk.BooleanVar()
    tk.Checkbutton(win, text=foodAry[i],
      variable=isfoodCheckAry[i]).grid(row=1, column=(1+i))

btnOk = tk.Button(win, text='確定', command=fnOk)
btnOk.grid(row=2, column=0)
win.mainloop()

