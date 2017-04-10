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
    
def checkentry1():
    if(entry1.get() == None or entry1.get() == "enter X"):
        entry1.delete(0, tk.END)
        entry1["bg"] = "red"
        entry1.insert(0, "enter X!!")
        return False
    return True
    
def checkentry2():
    if(entry2.get() == None or entry2.get() == "enter Y"):
        entry2.delete(0, tk.END)
        entry2["bg"] = "red"
        entry2.insert(0, "enter Y!!")
        return False
    return True

#compute supportx
def compute_supportx(event = None):
     if checkentry1() :
        testX = frozenset(tuple(entry1.get().replace(" ", "").split(',')))
        result = association_rule_mining.support(testX)
        label_supportx["text"] = result

#compute supportx
def compute_supporty(event = None):
     if checkentry2() :
        testY = frozenset(tuple(entry2.get().replace(" ", "").split(',')))
        result = association_rule_mining.support(testY)
        label_supporty["text"] = result

#compute confidence    
def compute_confidence(event = None):
    if checkentry1() and checkentry2():
        testX = frozenset(tuple(entry1.get().replace(" ", "").split(',')))
        testY = frozenset(tuple(entry2.get().replace(" ", "").split(',')))
        result = association_rule_mining.confidence(testX, testY)
        label_confidence["text"] = result

#compute lift
def compute_lift(event = None):
    if checkentry1() and checkentry2():
        testX = frozenset(tuple(entry1.get().replace(" ", "").split(',')))
        testY = frozenset(tuple(entry2.get().replace(" ", "").split(',')))
        result = association_rule_mining.lift(testX, testY)
        label_lift["text"] = result

"""widgets for the gui"""    
root1 = tk.Tk()
root1.wm_title("Association Rule Mining")

label1 = tk.Label(master = root1, text = "X", height = 1, width = 25, bg = "#FFE4E1")
label2 = tk.Label(master = root1, text = "Y", height = 1, width = 25, bg = "#FFE4E1")
entry1 = tk.Entry(master = root1)
entry1.insert(0, "enter X")
entry2 = tk.Entry(master = root1)
entry2.insert(0, "enter Y")
entry1.bind(sequence = '<1>', func = clearentry1)
entry2.bind(sequence = '<1>', func = clearentry2)

button_compute_supportx = tk.Button(master = root1, text = "Compute Support X ", command = compute_supportx, height = 1, width = 25, bg = "#E0FFFF")
label_supportx = tk.Label(master = root1, text = "", width = 18, bg = "#F8F8FF")

button_compute_supporty = tk.Button(master = root1, text = "Compute Support Y ", command = compute_supporty, height = 1, width = 25, bg = "#F5F5DC")
label_supporty = tk.Label(master = root1, text = "",  width = 18, bg = "#F8F8FF")

button_compute_confidence = tk.Button(master = root1, text = "Compute Confidence X -> Y", command = compute_confidence, height = 1, width = 25, bg = "#E0FFFF")
label_confidence = tk.Label(master = root1, text = "",  width = 18, bg = "#F8F8FF")

button_compute_lift = tk.Button(master = root1, text = "Compute Lift X -> Y", command = compute_lift, height = 1, width = 25, bg = "#F5F5DC")
label_lift = tk.Label(master = root1, text = "",  width = 18, bg = "#F8F8FF")

"""set positions for widgets"""
label1.grid(column=0, row=0)
entry1.grid(column=1, row=0)
label2.grid(column=0, row=1)
entry2.grid(column=1, row=1)
tk.Label(master = root1).grid(row = 2)
button_compute_supportx.grid(row = 3, column = 0, sticky = "W")
label_supportx.grid(row = 3, column = 1)
button_compute_supporty.grid(row = 4, column = 0, sticky = "W")
label_supporty.grid(row = 4, column = 1)
button_compute_confidence.grid(row = 5, column = 0, sticky = "W")
label_confidence.grid(row = 5, column = 1)
button_compute_lift.grid(row = 6, column = 0, sticky = "W")
label_lift.grid(row = 6, column = 1)

"""display"""
root1.mainloop()