import tkinter as tk
import tkinter.font as tkFont
##
from functools import partial
import threading


class Game(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.master.geometry('800x600')
        self.master.minsize(800, 600)
        self.master.maxsize(800, 600)
        self.createWidgets()
    
    def createWidgets(self):
        f1 = tkFont.Font(size = 30, family = "Courier New")
        f2 = tkFont.Font(size = 25, family = "Courier New")
        f3 = tkFont.Font(size = 20, family = "Courier New")
        f4 = tkFont.Font(size = 15, family = "Courier New")
        # 背景
        self.background = tk.Canvas(self, height = 600, width = 800, bg = 'white').pack()
        # 文字
        self.output = tk.Text(self, width=100, height=15, font = f4)
        self.output.place(x = 30, y = 300)
        # 按鈕
        self.back = tk.Button(self, text = "返回", height = 1, width = 4, font = f3, anchor='w').place(x = 35, y = 20)
        ##
        self.a = tk.Button(self, text = "A", height = 1, width = 10, font = f3, anchor='w', command=partial(self.actiontext, 'a')).place(x = 35, y = 120)
        self.b = tk.Button(self, text = "B", height = 1, width = 10, font = f3, anchor='w', command=partial(self.actiontext,'b')).place(x = 220, y = 120)
        self.c = tk.Button(self, text = "C", height = 1, width = 10, font = f3, anchor='w', command=partial(self.actiontext,'c')).place(x = 405, y = 120)
        self.d = tk.Button(self, text = "D", height = 1, width = 10, font = f3, anchor='w', command=partial(self.actiontext,'d')).place(x = 590, y = 120)
        self.e = tk.Button(self, text = "E", height = 1, width = 10, font = f3, anchor='w', command=partial(self.actiontext,'e')).place(x = 35, y = 220)
        self.f = tk.Button(self, text = "F", height = 1, width = 10, font = f3, anchor='w', command=partial(self.actiontext,'f')).place(x = 220, y = 220)
        self.g = tk.Button(self, text = "G", height = 1, width = 10, font = f3, anchor='w', command=partial(self.actiontext,'g')).place(x = 405, y = 220)
        self.h = tk.Button(self, text = "H", height = 1, width = 10, font = f3, anchor='w', command=partial(self.actiontext,'h')).place(x = 590, y = 220)
        # 標題
        self.title = tk.Label(self, text = "行動", height = 1, width = 10, bg = 'white', font = f1).place(x = 600 , y = 25)
        # CD
        self.text = tk.StringVar()
        self.cd = tk.Label(self, text = "冷卻時間:", height = 1, width = 10, bg = 'white', font = f2).place(x = 200 , y = 32)
        self.cdnumber = tk.Label(self, textvariable=self.text, height = 1, width = 2, bg = 'white', font = f2, fg="red")
        self.cdnumber.place(x = 390 , y = 32)
        self.cantrigger = True
        
    def actiontext(self, act):
        if self.cantrigger == True:
            self.write('已成功行動'+ str(act) + '\n')
            self.cooldown(10)

    def write(self, txt):
        self.output.insert('1.0',str(txt))
        self.update_idletasks()
    
    def cooldown(self, cdnum):
        if cdnum > 0:
            self.cantrigger = False
            self.text.set(str(cdnum))
            cdnum -= 1
            t = threading.Timer(1, self.cooldown, args = (cdnum,))
            t.start()
        else:
            self.cantrigger = True
            self.text.set('')

cal = Game()
cal.master.title("Game")
cal.mainloop()
