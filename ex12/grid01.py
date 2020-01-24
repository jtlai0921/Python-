import tkinter as tk

win = tk.Tk()
win.title('熱門動漫人物')
win.geometry('350x100')
lbl00 = tk.Label(win, text='火影忍者-鳴人', bg='yellow')
lbl03 = tk.Label(win, text='航海王-魯夫', bg='yellow')
lbl12 = tk.Label(win, text='天兵公園-鳥哥', bg='yellow')
lbl21 = tk.Label(win, text='櫻桃小丸子-小丸子', bg='yellow')
lbl00.grid(row=0, column=0)
lbl03.grid(row=0, column=3)
lbl12.grid(row=1, column=2)
lbl21.grid(row=2, column=1)
win.mainloop()