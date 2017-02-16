# -*- coding: utf-8 -*-
"""
Created on Mon Feb 06 16:09:50 2017

@author: saurabh.s1
"""
import csv
import numpy as np

def load_data(input_file):    
    
    X = []
    y = []
    
    with open(input_file) as f:
         csvfile = csv.reader(f, delimiter = ',')
         next(csvfile)
         for row in csvfile:
            if(row[1] == "positive" or row[1] == "negative"):            
                y.append(row[1])
                X.append(row[4])            
    X = np.asarray(X)
    y = np.asarray(y)
    classes = np.unique(y)
    for c in classes:
        print("{} : {}".format(c,np.sum(y == c)))
        
    y = (y == "positive")
    return X,y