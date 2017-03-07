# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 14:28:07 2017

@author: saurabh.s1
"""

from sklearn.cross_validation import KFold
from sklearn import neighbors
import numpy as np

def knn_cv(post_features, post_class, n_folds, n_neighbors, length_dataset = -1):
    
    if(length_dataset == -1):
        length_dataset = len(post_class)
    cv = KFold(n = length_dataset, n_folds = n_folds, shuffle = True)
    train_accuracy = []
    test_accuracy = []

    for train,test in cv:
        knn = neighbors.KNeighborsClassifier(n_neighbors = n_neighbors)
        knn.fit(post_features[train],post_class[train])
        train_accuracy.append(knn.score(post_features[train], post_class[train]))
        test_accuracy.append(knn.score(post_features[test], post_class[test]))
        
#    return (sum(train_accuracy)/n_folds), (sum(test_accuracy)/n_folds)
    return np.mean(train_accuracy), np.mean(test_accuracy)

