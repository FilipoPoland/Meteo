import tkinter
from tkinter import *


def callback(u_input):
    if u_input.isdigit():
        print(u_input)
        return True

    elif u_input is "":
        print(u_input)
        return True

    else:
        print(u_input)
        return False


root = Tk()

e = Entry(root)
e.place(x=50, y=50)
reg = root.register(callback)

e.config(validate="key",
         validatecommand=(reg, '% P'))

root.mainloop()