# -*- coding: utf-8 -*-
"""
***بسم الله الرحمان الرحیم***

Spyder Editor

Developer Mohammad Azimi
"""

from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import ttk

#for Greate GUI From
win = Tk()
win.title("Welcome to Python Tkinter with Azimi")
win.geometry('600x200')

style = ttk.Style()

style.theme_use('default')

style.configure("black.Horizontal.TProgressbar", background='black')

bar = Progressbar(win, length=200, style='black.Horizontal.TProgressbar')

bar['value'] = 30

bar.grid(column=0, row=0)

win.mainloop()