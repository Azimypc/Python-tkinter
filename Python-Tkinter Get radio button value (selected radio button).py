# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 12:37:00 2020

@author: azimy
"""

from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext


win = Tk()
win.title("Welcome to Python Tkinter With Mohammad")
win.geometry('600x200')

txt = scrolledtext.ScrolledText(win , width = 40 , height = 10)
txt.grid(column = 0 , row = 0)
txt.insert(INSERT,' You text goes here')
#txt.delete(1.0 , END)


win.mainloop()