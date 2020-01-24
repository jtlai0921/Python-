import tkinter as tk
from tkinter import messagebox as msgbox
from PIL import ImageTk, Image

def fnOk():
    data = ''
    total = 0
    for i in isCheckAry:
        if isCheckAry[i].get() == True:
            data += booksNameAry[i] + ", "
            total += booksPriceAry[i]
    result = '你選購的書為{0}，總共{1}元'.format(data , total)
    msgbox.showinfo('好書選購', result)

win = tk.Tk()
win.title('優質好書選購')
win.geometry('250x500')

booksIdAry=['AEL019300','AEL019800','AEL019900']
booksNameAry=['C#', 'MVC', 'C語言']
booksPriceAry=[650, 520, 420]
isCheckAry={}
bookImg={}

for i in range(3):
    isCheckAry[i] = tk.BooleanVar()
    bookImg[i] = ImageTk.PhotoImage(Image.open(booksIdAry[i]+".jpg"))
    tk.Checkbutton(win, image=bookImg[i], variable=isCheckAry[i]).pack()

btnOk = tk.Button(win, text='確定', command=fnOk)
btnOk.pack()
win.mainloop()