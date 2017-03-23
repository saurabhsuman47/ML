# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 12:11:49 2017

@author: saurabh
"""
from scipy.spatial import distance
import numpy as np
from normalize import normalizer
import math

class neighbor(object):
    
    def __init__(self, normalize = False):
        self.normalize = normalize
        if self.normalize == True:
            self.norm = normalizer()       
   
    def predict(self, X):
        binary  = X > 0
        if self.normalize == True:
            X = self.norm.fit_transform(X)
            
        num_users, num_movies = X.shape    
        dist_between_users = distance.pdist(binary, metric = 'correlation') 
        dist_between_users = distance.squareform(dist_between_users)
        neighbors = dist_between_users.argsort(axis = 1)
        
        predicted = X.copy()        
        
        for user in range(num_users):
            for movie in range(num_movies):
                if binary[user][movie] == True:
                    continue
                user_neighbors = neighbors[user, 1:]
                neighbor_ratings = [X[neighbor][movie] for neighbor in user_neighbors if binary[neighbor][movie]]
                ratings_to_consider = (len(neighbor_ratings)/2 + 1)
                neighbor_ratings = neighbor_ratings[:ratings_to_consider]
                predicted[user][movie] = np.mean(neighbor_ratings)
        
        ##when there is no movie for rating in training data (ratings went to testing data), we get nan values which we need to rate average rating value 
        average_rating = (X.sum())/(binary.sum())           
        for user in range(num_users):
            for movie in range(num_movies):
                if math.isnan(predicted[user][movie]):
                    predicted[user][movie] = average_rating                
                
        if self.normalize == True:
            predicted = self.norm.inverse_transform(predicted) 
            
        return predicted
        
if __name__ == "__main__":
    from load_data import load_data
    import os
    X, y = load_data(os.path.join("..", "ml-100k", "u.data"), test_percentage = 10)
    neighbor = neighbor(normalize = True)
    predicted = (neighbor.predict(X))
    from sklearn.metrics import r2_score, mean_squared_error
    print r2_score(y[y > 0], predicted[y > 0])
    print np.sqrt(mean_squared_error(y[y > 0], predicted[y > 0]))
#   r2 = 0.18571900871 rmse = 1.00338953915 without normalization
#   r2 = 0.269912516825 rmse = 0.959471180624 with normalization

