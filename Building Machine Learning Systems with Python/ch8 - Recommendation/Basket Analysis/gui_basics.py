#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 18:41:45 2017

@author: saurabh
"""

import Tkinter as tk
print tk
"Toplevel widget of Tk which represents mostly the main window of an application. "
#root = tk.Tk()
#label = tk.Label(master = root, text = "Enter something")
#entry = tk.Entry(master = root)
#label.pack(side = tk.LEFT)
#entry.pack()
#
#root.mainloop()

def showstr(event = None):
    print(buttonstr.get())
def showentry(event):
    print entry.get()

root1 = tk.Tk()
label = tk.Label(master = root1, text = "choose a button")
buttonstr = tk.StringVar()
radiobutton1 = tk.Radiobutton(master = root1, text = "option1", variable = buttonstr, value = "option1")
radiobutton2 = tk.Radiobutton(master = root1, text = "option2", variable = buttonstr, value = "option2")
radiobutton3 = tk.Radiobutton(master = root1, text = "option3", variable = buttonstr, value = "option3")
entry = tk.Entry(master = root1)
radiobutton1.config(command = showstr)
radiobutton2.config(command = showstr)
radiobutton3.config(command = showstr)
entry.bind(sequence = '<Return>', func = showentry)

label.pack()
radiobutton1.pack()
radiobutton2.pack()
radiobutton3.pack()
entry.pack()
#label.grid(column=0, row=0)
#radiobutton1.grid(column=0, row=1)
#radiobutton2.grid(column=0, row=2)
#radiobutton3.grid(column=0, row=3)
root1.mainloop()