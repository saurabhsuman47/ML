# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 16:24:28 2017

@author: saurabh
"""

import numpy as np
from sklearn.linear_model import ElasticNetCV
from sklearn.metrics import r2_score, mean_squared_error
from load_data import load_data 
from normalize import normalizer
import os

data_path = os.path.join("..", "ml-100k","u.data")
X, y = load_data(data_path, test_percentage = 10)
num_users, num_movies = X.shape

binary = (X > 0)
norm = normalizer()
X = norm.fit_transform(X)

predicted = X.copy()

clf = ElasticNetCV(alphas = [0.0125, 0.025, 0.05, .1, .125, .5, 1.0, 2.0, 4.0])
#clf = ElasticNetCV(alphas = [ .1])

for user in range(num_users):
    #bool array for movies rated by user
    movie_user = binary[user]       
    #which users to consider as attributes for regression, in this case all except current user
    neighbors = np.ones((num_users), dtype = bool)
    neighbors[user] = False
    X_train_user = X[neighbors]
    X_train_user = X_train_user[:, movie_user].T
    y_train_user = X[user, movie_user]
    clf.fit(X_train_user, y_train_user)
    X_test_user = X[neighbors]
    X_test_user = X_test_user[:, ~movie_user].T
    predicted[user, ~movie_user] = clf.predict(X_test_user)
    
predicted = norm.inverse_transform(predicted)

r2 = r2_score(y[y > 0], predicted[y > 0])
print r2   #0.286412552103

rmse = np.sqrt(mean_squared_error(y[y > 0], predicted[y > 0]))
print rmse  #0.947386695346  