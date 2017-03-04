# -*- coding: utf-8 -*-
"""
Created on Tue Feb 07 16:16:49 2017

@author: saurabh.s1
"""

import numpy as np
import matplotlib.pyplot as plt
               
def train_model(clf, cv, X, y, name = "optional", plot = False):    
    test_accuracy = []
    train_accuracy = []   
    for train,test in cv:
        X_train = X[train]
        print type(X_train)
        X_test = X[test]
        y_train = y[train]
        y_test = y[test]
        clf.fit(X_train, y_train)

        train_accuracy.append(clf.score(X_train, y_train))
        test_accuracy.append(clf.score(X_test, y_test))       

    return clf, np.mean(train_accuracy), np.mean(test_accuracy)
        
    
