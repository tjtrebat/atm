__author__ = 'Tom'

from Tkinter import *

class ATM:
    def __init__(self, root):
        self.frame = Frame(root, padx=10, pady=10)
        self.frame.pack()
        frame = Frame(self.frame, bd=1, relief=GROOVE)
        frame.grid()
        self.tv_balance = ""
        self.lbl_balance = Label(frame, textvariable=self.tv_balance, height=2, width=21, anchor="nw")
        self.lbl_balance.grid()
        frame = Frame(self.frame, bd=2, relief=SUNKEN)
        frame.grid()
        number_pad = Frame(frame, padx=20)
        number_pad.grid(row=0, column=0)
        for i in range(9):
            Button(number_pad, text=(i + 1), command= lambda x = (i + 1):self.num_click_handler(x)).grid(row=(i / 3), column=(i % 3))
        Button(number_pad, text=0).grid(row=3, column=1)
        button_pad = Frame(frame)
        button_pad.grid(row=0, column=1)
        self.btn_ok = Button(button_pad, width=7, text="OK", state=DISABLED)
        self.btn_ok.grid()
        self.btn_balance = Button(button_pad, width=7, text="Balance")
        self.btn_balance.grid()
        self.btn_withdraw = Button(button_pad, width=7, text="Withdraw")
        self.btn_withdraw.grid()
        Button(button_pad, width=7, text="Done", command=quit).grid()

    def num_click_handler(self, num):
        pass
        

root = Tk()
atm = ATM(root)
root.mainloop()



  