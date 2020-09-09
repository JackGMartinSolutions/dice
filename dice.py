#!/usr/bin/env python3
from Tkinter import *
import random

dice_number=0

def role_dice(label):
	dice_number = random.randint(0,6)
	print(dice_number)
	label.config(text=str(dice_number))


def make_window():
    global fnamevar, lnamevar, phonevar, select
    win = Tk()

    frame = Frame(win)
    frame.pack()

    label = Label(win, fg="dark green")
    
    b1 = Button(win, text=" ROLE  ", command=role_dice(label))
    b2 = Button(win, text="Two")
    b3 = Button(win, text="CLOSE", command=win.destroy)

    

   
    b1.pack(side=LEFT)
    b2.pack(side=LEFT)
    b3.pack(side=LEFT)
    label.pack()
    
    return win


win = make_window()
win.mainloop()