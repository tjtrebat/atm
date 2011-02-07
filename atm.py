__author__ = 'Tom'

from Tkinter import *
from PIL import Image, ImageTk
import tkMessageBox

class ATM:
    """ A simple Tk ATM machine demonstration """
    def __init__(self, root):
        """ Create a new ATM instance """
        root.title("ATM")
        self.frame = Frame(root, padx=10, pady=10)
        self.frame.pack()
        frame = Frame(self.frame, padx=20)
        frame.grid()
        self.add_balance(frame)
        number_panel = self.add_number_panel(frame)
        self.add_button_panel(number_panel)
        self.add_money_panel()

    def add_balance(self, frame):
        """ Add the frame for displaying balance """
        frame = Frame(frame, bd=1, relief=GROOVE) # add grooved frame for balance display
        frame.grid()
        balance = open('balance.txt', 'rb')
        num = balance.read()
        self.balance = float(num) if num.strip() else 0.0
        balance.close()
        self.tv_balance = StringVar()
        self.set_lbl_balance()
        self.has_balance = True
        self.lbl_balance = Label(frame, textvariable=self.tv_balance, height=2, width=24)
        self.lbl_balance.grid()

    def add_number_panel(self, frame):
        """ Adds number panel """
        frame = Frame(frame, bd=2, relief=SUNKEN)
        frame.grid()
        number_pad = Frame(frame, padx=20)
        number_pad.grid()
        for i in range(9):
            Button(number_pad, text=(i + 1), command= lambda x = (i + 1):self.num_click_handler(x)).grid(row=(i / 3), column=(i % 3))
        Button(number_pad, text=0, command= lambda x = 0:self.num_click_handler(x)).grid(row=3, column=1)
        return frame

    def add_button_panel(self, frame):
        """ Adds function buttons """
        button_pad = Frame(frame, padx=10)
        button_pad.grid(row=0, column=1)
        self.add_button(button_pad, width=7, command=lambda x= True:self.change_balance(x), text="Deposit")
        self.add_button(button_pad, width=7, command=self.show_balance, text="Balance")
        self.add_button(button_pad, width=7, command=lambda x= False:self.change_balance(x), text="Withdraw")
        self.add_button(button_pad, width=7, text="Done", state=DISABLED)

    def add_button(self, *args, **kwargs):
        """ Adds a Button the the button panel """
        btn = 'btn_%s' % kwargs['text'].lower()
        setattr(self, btn, Button(*args, **kwargs))
        getattr(self, btn).grid()            

    def add_money_panel(self):
        """ Adds a frame for money widgets """
        frame = Frame(self.frame)
        frame.grid(row=0, column=1)
        self.add_money(frame, '20_dollars', row=0, column=0) # add 20 dollar widgets
        self.add_money(frame, '50_dollars', row=1, column=0) # add 50 dollar widgets

    def add_money(self, frame, denomination, **kwargs):
        """ Adds the money image Label and Entry """
        money = self.get_image_label(frame, "%s.jpg" % denomination)
        money.grid(**kwargs)
        tv = "tv_%s" % denomination
        entry = "ent_%s" % denomination
        setattr(self, tv, StringVar())
        setattr(self, entry, Entry(frame, textvariable=getattr(self, tv), state=DISABLED))
        getattr(self, entry).grid(row=kwargs["row"], column=1)

    def get_image_label(self, frame, img):
        """ Returns a new Label configured w/ an image """
        image = Image.open(img)
        photo = ImageTk.PhotoImage(image)
        label = Label(frame, image=photo)
        label.image = photo
        return label

    def change_balance(self, isDeposit):
        """ Event handler for withdraw/deposit buttons """
        self.change_btn_state("disabled")
        self.btn_done.configure(state=ACTIVE)
        self.tv_balance.set("0.00")
        if isDeposit:
            self.btn_done.configure(command=self.deposit)
        else:
            self.btn_done.configure(command=self.withdraw)

    def withdraw(self):
        amount = float(self.tv_balance.get())
        if amount <= 0:
            self.show_balance()
        elif (amount < 20) or not ((amount % 2 == 0) and (amount % 5 == 0)):
            tkMessageBox.showwarning("Withdraw", "I only have 20 and 50 dollar bills.")
            self.tv_balance.set("0.00")
        elif self.balance >= amount:
            self.balance -= amount
            self.save_balance()
            # set dispensed money Entry widgets
            num_50s = 0 # number of 50s
            if amount % 5 == 0:
                num_50s = int(amount // 50)
                if (num_50s > 0) and ((amount - 50 * num_50s) % 20 != 0):
                    num_50s -= 1
            num_20s = int((amount - 50 * num_50s) // 20) # number of 20s
            self.tv_20_dollars.set(str(num_20s))
            self.tv_50_dollars.set(str(num_50s))
        else:
            tkMessageBox.showwarning("Withdraw", "Amount exceeds available balance.")
            self.tv_balance.set("0.00")

    def deposit(self):
        self.balance += float(self.tv_balance.get())
        self.save_balance()

    def num_click_handler(self, num):
        if not self.has_balance:
            amount = float(self.tv_balance.get())
            num = round((amount * 10) + (round(num) / 100), 2)
            self.tv_balance.set("%0.2f" % num)

    def change_btn_state(self, new_state):
        for btn in (self.btn_deposit, self.btn_withdraw):
            btn.configure(state=new_state)
        self.has_balance = False
        # clear money Entry widgets
        self.tv_20_dollars.set("")
        self.tv_50_dollars.set("")

    def show_balance(self):
        self.change_btn_state("active")
        self.btn_done.configure(state=DISABLED)
        self.has_balance = True
        self.set_lbl_balance()

    def save_balance(self):
        # save balance
        balance = open('balance.txt', 'wb')
        balance.write(str(self.balance))
        balance.close()
        self.show_balance()

    def set_lbl_balance(self):
        self.tv_balance.set("Balance is %0.2f" % self.balance)

if __name__ == "__main__":
    root = Tk()
    atm = ATM(root)
    root.mainloop()



  