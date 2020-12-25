# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 12:37:00 2020

@author: azimy
"""

from tkinter import *
from tkinter.ttk import *


win = Tk()
win.title("Welcome to Python Tkinter With Mohammad")
win.geometry('600x200')

Selected = IntVar()

rad1 = Radiobutton(win , text= 'First' , value=1 , variable= Selected)
rad2 = Radiobutton(win , text = 'Second' , value= 2 , variable= Selected)
rad3 = Radiobutton(win , text = 'third' , value=3 , variable= Selected)


def clicked():
    print(Selected.get())
    
btn = Button(win , text = "Click Me" , command=clicked) 
   
rad1.grid(column = 0 , row = 0)
rad2.grid(column = 1 , row = 0)
rad3.grid(column = 2 , row = 0)

btn.grid(column = 3 , row = 0)


win.mainloop()