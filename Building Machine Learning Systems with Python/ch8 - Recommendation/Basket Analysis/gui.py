#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 18:41:45 2017

@author: saurabh
"""
#https://www.tutorialspoint.com/python/python_gui_programming.htm
import Tkinter as tk
import association_rule_mining

def clearentry1(event):
    entry1.delete(0, tk.END)
    entry1["bg"] = "white"
    
def clearentry2(event):
    entry2.delete(0, tk.END)
    entry2["bg"] = "white"
    
def compute(event = None): 
    if(entry1.get() == None or entry1.get() == "enter X"):
        entry1.delete(0, tk.END)
        entry1["bg"] = "red"
        entry1.insert(0, "enter X!!")
    if(entry2.get() == None or entry2.get() == "enter Y"):
        entry2.delete(0, tk.END)
        entry2["bg"] = "red"
        entry2.insert(0, "enter Y!!")
    testX = frozenset(tuple(entry1.get().replace(" ", "").split(',')))
    testY = frozenset(tuple(entry2.get().replace(" ", "").split(',')))
    result = association_rule_mining.confidence(testX, testY)
    label3["text"] = result

    
root1 = tk.Tk()
label1 = tk.Label(master = root1, text = "X")
label2 = tk.Label(master = root1, text = "Y")
entry1 = tk.Entry(master = root1)
entry1.insert(0, "enter X")
entry2 = tk.Entry(master = root1)
entry2.insert(0, "enter Y")
entry1.bind(sequence = '<1>', func = clearentry1)
entry2.bind(sequence = '<1>', func = clearentry2)
button1 = tk.Button(master = root1, text = "Compute Confidence X -> Y", command = compute)
label3 = tk.Label(master = root1, text = "")

"""set positions for widgets"""
label1.grid(column=0, row=0)
entry1.grid(column=1, row=0)
label2.grid(column=0, row=1)
entry2.grid(column=1, row=1)
button1.grid(column = 0, row = 2)
label3.grid(row = 2, column = 1)

"""display"""
root1.mainloop()
