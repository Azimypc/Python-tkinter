# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 12:05:26 2020

@author: azimy
"""

from tkinter import *

win = Tk()

win.title("Welcome to Python Tkinter With Mohammad")

win.geometry('600x200')

lbl = Label(win, text="Hello")
lbl.grid(column=0, row=0)

txt = Entry(win , width = 10)
txt.grid(column = 1 , row = 0)

def clicked():
    res = "Welcom to " + txt.get()
    lbl.configure(text = res)

btn = Button(win, text="Click Me", command=clicked)

btn.grid(column=2, row=0)

win.mainloop()