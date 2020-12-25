# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 11:09:54 2020

@author: azimy
"""
from tkinter import *
from tkinter import ttk
#for Greate GUI From
win = Tk()
win.title("Welcome to Python Tkinter with Azimi")
win.geometry('600x200')

#Button Evnet Handel
def cliched():
    Lb.configure(text = "I Love Alle the Pepole!")    

#Add a Lable on the from
Lb = Label(win , text = "Python Programming for Alle" , font=("Arial Blod" , 30))
Lb.grid(column = 0 , row = 0)

#Add Button on the form
btn = Button(win , text='Click Me', bg="orange" , fg = "red" , command=cliched)
btn.grid(column = 1 , row = 0 )
win.mainloop()
