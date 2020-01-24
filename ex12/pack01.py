import tkinter as tk

win = tk.Tk()
win.title('熱門動漫人物')
win.geometry('350x100')
lbltop = tk.Label(win, text='火影忍者-鳴人', bg='yellow')
lblleft = tk.Label(win, text='航海王-魯夫', bg='yellow')
lblright = tk.Label(win, text='天兵公園-鳥哥', bg='yellow')
lblbottom = tk.Label(win, text='櫻桃小丸子-小丸子', bg='yellow')
lbltop.pack(side='top')
lblleft.pack(side='left')
lblright.pack(side='right')
lblbottom.pack(side='bottom')
win.mainloop()
