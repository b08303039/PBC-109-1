import tkinter as tk
import tkinter.font as tkFont

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
        # 背景和圖片
        self.background = tk.Canvas(self, height = 600, width = 800, bg = 'white').pack()
        self.picture = tk.Canvas(self, height = 240, width = 240, bg = 'blue').place(x = 60, y = 60)
        # 經驗值
        self.exp = tk.Label(self, text = "經驗：100", height = 1, width = 12, bg = 'white', font = f3).place(x = 445, y = 260)
        # 首頁基礎數值
        self.level = tk.Button(self, text = "等級：12", height = 1, width = 15, font = f3, anchor='w').place(x = 60, y = 360)
        self.blood = tk.Button(self, text = "血量：231", height = 1, width = 15, font = f3, anchor='w').place(x = 60, y = 420)
        self.attack = tk.Button(self, text = "攻擊：243", height = 1, width = 15, font =f3, anchor='w').place(x = 60, y = 480)
        self.defend = tk.Button(self, text = "防禦：234", height = 1, width = 15, font =f3, anchor='w').place(x = 400, y = 360)
        self.skill = tk.Button(self, text = "技能：5%攻擊加倍", height = 1, width = 15, font =f3, anchor='w').place(x = 400, y = 420)
        self.dodge = tk.Button(self, text = "閃避：34%", height = 1, width = 15, font =f3, anchor='w').place(x = 400, y = 480)
        # 角色名和自己的名稱
        self.charater_name = tk.Label(self, text = "桐人", height = 1, width = 10, bg = 'white', font =f1).place(x = 420 , y = 100)
        self.name = tk. Label(self, text = "亞斯娜", height = 1, width = 10, bg = 'white', font =f2).place(x = 440 , y = 200)
        # 按鈕
        self.boss = tk.Button(self, text = "關\n卡", height = 2, width = 2, font = f3).place(x = 760 , y = 60)
        self.character = tk.Button(self, text = "角\n色", height = 2, width = 2, font = f3).place(x = 760 , y = 180)
        self.action  = tk.Button(self, text = "行\n動", height = 2, width = 2, font = f3).place(x = 760 , y = 300)

cal = Game()
cal.master.title("Game")
cal.mainloop()
