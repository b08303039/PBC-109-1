import tkinter as tk
import tkinter.font as tkFont
import tkinter.messagebox
import pickle


class Page1(tk.Frame):
    
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.createWidgets()
        self.master.title('我的大學')
        self.master.geometry("800x600")

    def usr_login(self):
    # 獲取使用者輸入的usr_name和
        usr_name = self.var_usr_name.get()
        if usr_name != '':
            self.master.destroy()
        else:
            tkinter.messagebox.showinfo('你真的不幫自己取名嗎?', '叫你不設你還真不設啊!\n你這個好傢伙，不幫自己取名，那你也別想玩!')

    def createWidgets(self):
        self.background = tk.Label(self, text='背景', font=('KaiTi', 40)).pack(ipadx=340, ipady=10)
        self.introduction = tk.Label(self, text=('這是發生在2018年的秘辛，你任職台灣的\n某間大學，但因為雙標黨的操作，你被迫從大\n學驅離。當你重新奪回大學，卻發現人事已經被\n雙標黨給滲透，還有被奇怪的勢力占領，所以\n你要打走那些搶走你大學的人，好好加油吧!'), 
                        font=('KaiTi', 20)).pack(side='top')
        self.name = tk.Label(self, text='玩家名稱:', font=('KaiTi', 26)).pack(padx=110, pady=25)
        self.hit = tk.Label(self, text='(你可以不輸入玩家名稱看看)', font=('KaiTi', 20)).pack()
        self.var_usr_name = tk.StringVar()
        self.entry_usr_name = tk.Entry(self, textvariable=self.var_usr_name, font=('KaiTi', 20)).pack(pady=10)
        self.btn_login = tk.Button(self, text='登入', bg='#A877BA', font=('KaiTi', 20), command=self.usr_login)
        self.btn_login.pack(padx=10, pady=10)

page1 =Page1()
page1.mainloop()
