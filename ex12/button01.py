import tkinter as tk

def fnHello():
    lblShow['text'] = 'Hello World!'
    
def fnClear():
    lblShow['text'] = ''

win = tk.Tk()
win.title('按鈕範例')
win.geometry('150x100')
lblShow = tk.Label(win, text='', font=('細明體', 18))
btnHello = tk.Button(win, text='Hello', command=fnHello)
btnClear = tk.Button(win, text='Clear', command=fnClear)
lblShow.pack()
btnHello.pack()
btnClear.pack()
win.mainloop()