__author__ = 'Tom'

from Tkinter import *
from PIL import Image, ImageTk

class ATM:
    def __init__(self, root):
        self.frame = Frame(root, padx=10, pady=10)
        self.frame.pack()
        frame = Frame(self.frame, padx=20)
        frame.grid()
        self.add_balance(frame)
        number_panel = self.add_number_panel(frame)
        self.add_button_panel(number_panel)
        self.add_money()

    def add_balance(self, frame):
        frame = Frame(frame, bd=1, relief=GROOVE) # add grooved frame for balance display
        frame.grid()
        self.balance = 0.0
        self.tv_balance = StringVar()
        self.set_lbl_balance()
        self.has_balance = True
        self.lbl_balance = Label(frame, textvariable=self.tv_balance, height=2, width=24)
        self.lbl_balance.grid()

    def add_number_panel(self, frame):
        frame = Frame(frame, bd=2, relief=SUNKEN)
        frame.grid()
        number_pad = Frame(frame, padx=20)
        number_pad.grid()
        for i in range(9):
            Button(number_pad, text=(i + 1), command= lambda x = (i + 1):self.num_click_handler(x)).grid(row=(i / 3), column=(i % 3))
        Button(number_pad, text=0, command= lambda x = 0:self.num_click_handler(x)).grid(row=3, column=1)
        return frame

    def add_button_panel(self, frame):
        button_pad = Frame(frame, padx=10)
        button_pad.grid(row=0, column=1)
        self.btn_deposit = Button(button_pad, width=7, command=self.deposit, text="Deposit")
        self.btn_deposit.grid()
        self.btn_balance = Button(button_pad, width=7, command=self.set_lbl_balance, text="Balance")
        self.btn_balance.grid()
        self.btn_withdraw = Button(button_pad, width=7, command=self.withdraw, text="Withdraw")
        self.btn_withdraw.grid()
        self.btn_done = Button(button_pad, width=7, text="Done", command=self.done, state=DISABLED)
        self.btn_done.grid()

    def add_money(self):
        # add frame for money widgets
        frame = Frame(self.frame)
        frame.grid(row=0, column=1)
        # add 20 dollar image
        image = Image.open('20_dollars.jpg')
        photo = ImageTk.PhotoImage(image)
        lbl_20_dollars = Label(frame, image=photo)
        lbl_20_dollars.image = photo
        lbl_20_dollars.grid(row=0, column=0)
        # add 50 dollar image
        image = Image.open('50_dollars.jpg')
        photo = ImageTk.PhotoImage(image)
        lbl_50_dollars = Label(frame, image=photo)
        lbl_50_dollars.photo = photo
        lbl_50_dollars.grid(row=1, column=0)
        # Add Entry widgets for withdrawn money
        self.ent_20_dollars = Entry(frame, state=DISABLED)
        self.ent_20_dollars.grid(row=0, column=1)
        self.ent_50_dollars = Entry(frame, state=DISABLED)
        self.ent_50_dollars.grid(row=1, column=1)

    def deposit(self):
        self.change_btn_state("disabled")
        self.btn_done.configure(state=ACTIVE)
        self.tv_balance.set("0.00")
        self.has_deposit = True
        self.has_withdraw = False

    def withdraw(self):
        self.change_btn_state("disabled")
        self.btn_done.configure(state=ACTIVE)
        self.tv_balance.set("0.00")
        self.has_deposit = False
        self.has_withdraw = True

    def done(self):
        self.change_btn_state("active")
        self.btn_done.configure(state=DISABLED)
        self.has_balance = True
        if self.has_withdraw:
            self.balance -= float(self.tv_balance.get())
        elif self.has_deposit:
            self.balance += float(self.tv_balance.get())
        self.set_lbl_balance()
        
    def change_btn_state(self, new_state):
        for btn in (self.btn_deposit, self.btn_balance, self.btn_withdraw):
            btn.configure(state=new_state)
        self.has_balance = False

    def set_lbl_balance(self):
        self.tv_balance.set("Balance is %0.2f" % self.balance)

    def num_click_handler(self, num):
        amount = float(self.tv_balance.get())
        if not self.has_balance:
            num = round((amount * 10) + (round(num) / 100), 2)
            self.tv_balance.set("%0.2f" % num)

root = Tk()
atm = ATM(root)
root.mainloop()



  