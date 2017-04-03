#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 18:41:45 2017

@author: saurabh
"""

import Tkinter as tk
import association_rule_mining


def showentry1(event):
    print entry1.get()
    
def showentry2(event):
    print entry2.get()
    
def compute(event = None):
    testX = frozenset(tuple(entry1.get().split(',')))
    testY = frozenset(tuple(entry2.get().split(',')))
    print association_rule_mining.confidence(testX, testY)
    
root1 = tk.Tk()
label1 = tk.Label(master = root1, text = "X")
label2 = tk.Label(master = root1, text = "Y")
entry1 = tk.Entry(master = root1)
entry2 = tk.Entry(master = root1)
entry1.bind(sequence = '<Return>', func = showentry1)
entry2.bind(sequence = '<Return>', func = showentry2)
button1 = tk.Button(text = "Compute Confidence", command = compute)

#label1.pack(side = tk.LEFT)
#entry1.pack()
#label2.pack(side = tk.LEFT)
#entry2.pack()
label1.grid(column=0, row=0)
entry1.grid(column=1, row=0)
label2.grid(column=0, row=1)
entry2.grid(column=1, row=1)
button1.grid(column = 0, row = 2)
#label.grid(column=0, row=0)

root1.mainloop()
