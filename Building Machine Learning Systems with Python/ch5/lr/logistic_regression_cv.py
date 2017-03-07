# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 15:08:09 2017

@author: saurabh.s1
"""

from sklearn.linear_model import LogisticRegression
import numpy as np
from sklearn.cross_validation import KFold
from sklearn.metrics import precision_recall_curve
import pickle

def classify(clf,X):
    return 1/(1+np.exp(-(clf.intercept_ + np.dot(X, (clf.coef_).transpose()))))

def logistic_regression_cv(post_features, post_class, C, cv_n_folds, length_dataset = -1, pr = False, dump = True):
    flag = 0
    train_error = []
    test_error = []
    if(length_dataset == -1):
        length_dataset = len(post_class)
    cv = KFold(n = length_dataset, n_folds = cv_n_folds, shuffle = True)
    for train, test in cv: 
        clf = LogisticRegression(C = C,verbose = 0)
        clf.fit(post_features[train], post_class[train])
        train_predicted = classify(clf,post_features[train])
        test_predicted = classify(clf,post_features[test])
        train_error.append(np.mean(abs(post_class[train].reshape(len(train),1) - train_predicted)))
        test_error.append(np.mean(abs(post_class[test].reshape(len(test),1) - test_predicted)))
        if(pr == True):
            precision, recall, thresholds = precision_recall_curve(post_class[test], test_predicted)
        if(dump == True and flag == 0):
            pickle.dump(clf, open("logreg.dat","w"))
            flag = 1
            
    if(pr == True):
        return np.mean(train_error),np.mean(test_error), precision, recall, thresholds
    else:
        return np.mean(train_error),np.mean(test_error)

  

 
