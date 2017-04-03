#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 14:00:01 2017

@author: saurabh
"""

import pickle
import numpy as np
from load_data import load_data

frequent_itemsets = pickle.load(open("frequent_itemsets.dat"))
input_file = "retail.dat"
T, counts = load_data(input_file)
number_transactions = len(T)

#a = frozenset(['32'])
#if a in frequent_itemsets:
#    print frequent_itemsets[a]
    
def check_frequent_itemsets(x):
    if x in frequent_itemsets:
        return True
    return False

def merge(x, y):    
    S1 = set()
    for i in x:
        S1.add(i)
    for j in y:
        S1.add(j)
    temp_tuple = tuple(S1)            
    return frozenset(temp_tuple)

def support(x): 
    if x in frequent_itemsets:
        return ((1.0 * frequent_itemsets[x]) / number_transactions )
    else:
        return np.nan

def confidence(x, y):  
    xy = merge(x, y)
    return 1.0 * support(xy)/support(x)
    
    
def lift(x, y):
    xy = merge(x, y)
    return ( 1.0 * support(xy)) / (support(x) * support(y))    

def conviction(x, y):
    return (1.0 - (1.0 * support(y))) / (confidence(x, y))
    

if __name__ == "__main__":
    testx = frozenset(["32"])
    testy = frozenset(["39","32"])
#    print merge(testx, testy)
    print support(testx)
    print confidence(testx, testy)
    print lift(testx, testy)
    print conviction(testx, testy)