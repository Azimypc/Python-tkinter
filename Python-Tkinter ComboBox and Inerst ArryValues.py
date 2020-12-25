# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 12:19:40 2020

@author: azimy
"""

from tkinter import *
from tkinter.ttk import*
win = Tk()

win.title("Welcome to Python Tkinter With Mohammad")

win.geometry('600x200')

Combo = Combobox(win)
Combo['values'] = (1,2,3,4,5, "Text")
Combo.current(0) #Set the Selected item
Combo.grid(column = 0 , row = 0)

win.mainloop()