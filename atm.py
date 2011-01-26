__author__ = 'Tom'

from Tkinter import *

class ATM:
    def __init__(self, root):
        self.frame = Frame(root, padx=10, pady=10)
        self.frame.pack()
        frame = Frame(self.frame, bd=1, relief=GROOVE)
        frame.grid()
        Label(frame, text="Balance is xxx", height=2, width=20, anchor="nw").grid()
        frame = Frame(self.frame, bd=1, relief=SUNKEN)
        frame.grid()
        for i in range(9):
            Button(frame, text=(i + 1), command= lambda x = i:self.num_click_handler(x)).grid(row=(i / 3), column=(i % 3))
        Button(frame, text=0).grid(row=3, column=1)

root = Tk()
atm = ATM(root)
root.mainloop()



  