#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 20:31:56 2017

@author: saurabh
"""

from load_data import load_data
from scipy.sparse import csr_matrix as csr
import os
import random
import numpy as np
from pprint import pprint 
from predictor_regression import regression
from predictor_nearest_neighbors import neighbor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

def split_data(X, test_percentage = 10):
    X = csr(X)
    number_ratings = len(X.indices)
    user_ids = []
    indptr = X.indptr
    for i in range(len(indptr) - 1):
        t1 = indptr[i+1] - indptr[i]
        for j in range(t1):
            user_ids.append(i)
    movie_ids = X.indices
    test_idxs = np.array(random.sample(range(number_ratings), number_ratings/test_percentage))
    
    X = X.toarray()
    train_reviews = np.array(X)
    for idx in test_idxs:
        train_reviews[user_ids[idx]][movie_ids[idx]] = 0
    
    test_reviews = np.zeros_like(X)
    for idx in test_idxs:
        test_reviews[user_ids[idx]][movie_ids[idx]] = X[user_ids[idx]][movie_ids[idx]]

    return train_reviews, test_reviews

X, y = load_data(os.path.join("..", "ml-100k", "u.data"), test_percentage = 10)
X_train, X_test = split_data(X)

regression1 = regression()
regression2 = regression(normalize = True)
neighbor1 = neighbor()
neighbor2 = neighbor(normalize = True)
X_pred1 = regression1.predict(X_train)
X_pred2 = neighbor1.predict(X_train)
X_pred3 = regression2.predict(X_train)
X_pred4 = neighbor2.predict(X_train)

stack_train = np.array([
        X_pred1[X_test > 0],
        X_pred2[X_test > 0],
        X_pred3[X_test > 0],
        X_pred4[X_test > 0]
        ]).T

clf = LinearRegression()
clf.fit(stack_train, X_test[X_test > 0])

stack_test = np.array([
        X_pred1.ravel(),
        X_pred2.ravel(),
        X_pred3.ravel(),
        X_pred4.ravel()            
        ]).T
predicted = clf.predict(stack_test).reshape(X.shape)

r2 = r2_score(y[y > 0], predicted[y > 0])
print r2   

rmse = np.sqrt(mean_squared_error(y[y > 0], predicted[y > 0]))
print rmse 



