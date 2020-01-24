import tkinter as tk

win = tk.Tk()
win.title('標籤元件')
win.geometry('400x100')
lbl01 = tk.Label(win, text='跟著實務學習ASP.NET MVC', bg='pink',font=('標楷體', 16))
lbl02 = tk.Label(win, text='跟著實務學習網頁設計', bg='yellow',font=('標楷體', 14))
lbl03 = tk.Label(win, text='跟著實務學習Bootstrap', bg='red', fg='white',font=('標楷體', 12))
lbl01.pack()
lbl02.pack()
lbl03.pack()
win.mainloop()