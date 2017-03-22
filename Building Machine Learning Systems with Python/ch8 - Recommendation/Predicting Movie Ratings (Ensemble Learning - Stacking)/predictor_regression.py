# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 12:11:49 2017

@author: saurabh
"""
from sklearn.linear_model import ElasticNetCV
import numpy as np
from normalize import normalizer

class regression(object):
    
    def __init__(self, normalize = False):
        self.normalize = normalize
        if self.normalize == True:
            self.norm = normalizer()       
   
    def predict(self, X):
        binary  = X > 0
        if self.normalize == True:
            X = self.norm.fit_transform(X)
            
        num_users, num_movies = X.shape
        clf = ElasticNetCV(alphas = [0.1]) 
        predicted = X.copy()
        
        
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
        
        if self.normalize == True:
            predicted = self.norm.inverse_transform(predicted) 
            
        return predicted
        
if __name__ == "__main__":
    from load_data import load_data
    import os
    X, y = load_data(os.path.join("..", "ml-100k", "u.data"), test_percentage = 10)
    regression = regression(normalize = True)
    predicted = (regression.predict(X))
    from sklearn.metrics import r2_score, mean_squared_error
    print r2_score(y[y > 0], predicted[y > 0])
    print np.sqrt(mean_squared_error(y[y > 0], predicted[y > 0]))
#   r2 = 0.214345310048 rmse = 0.995554822399 without normalization
#   r2 = 0.270750567348 rmse = 0.962996362106 with normalization
