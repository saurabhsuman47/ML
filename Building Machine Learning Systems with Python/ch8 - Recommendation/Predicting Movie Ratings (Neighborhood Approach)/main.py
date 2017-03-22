# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 15:39:06 2017

@author: saurabh
"""
import numpy as np
import math
import os
from scipy.spatial import distance
from sklearn.metrics import r2_score, mean_squared_error
from load_data import load_data
from normalize import normalizer

data_path = os.path.join("ml-100k","u.data")
train_reviews, test_reviews = load_data(data_path, test_percentage = 10)
num_users, num_movies = train_reviews.shape

binary = train_reviews > 0 
norm = normalizer()
train_reviews = norm.fit_transform(train_reviews)

dist_between_users = distance.pdist(binary, metric = 'correlation') 
dist_between_users = distance.squareform(dist_between_users)
neighbors = dist_between_users.argsort(axis = 1)

filled = train_reviews.copy()

for user in range(num_users):
    for movie in range(num_movies):
        if binary[user][movie] == True:
            continue
        user_neighbors = neighbors[user, 1:]
        neighbor_ratings = []
        for neighbor in user_neighbors:
            if binary[neighbor][movie] == True:
                neighbor_ratings.append(train_reviews[neighbor][movie])
        ratings_to_consider = (len(neighbor_ratings)/2 + 1)
        neighbor_ratings = neighbor_ratings[:ratings_to_consider]
        filled[user][movie] = np.mean(neighbor_ratings)

##when there is no movie for rating in training data (ratings went to testing data), we get nan values which we need to rate average rating value 
average_rating = (train_reviews.sum())/(binary.sum())           
for user in range(num_users):
    for movie in range(num_movies):
        if math.isnan(filled[user][movie]):
            filled[user][movie] = average_rating                

filled = norm.inverse_transform(filled)

r2 = r2_score(test_reviews[test_reviews > 0.0], filled[test_reviews > 0.0])
rmse =  np.sqrt(mean_squared_error(test_reviews[test_reviews > 0.0], filled[test_reviews > 0.0]))
print("Binary matrix for dist calculation, with normalization (nearest half considered) - R2 score : {} , rmse : {}".format(r2, rmse))

#Binary matrix for dist calculation, no normalization (nearest half considered) - R2 score : 0.19078696037 , rmse : 1.01567341136
#Binary matrix for dist calculation, with normalization (nearest half considered) - R2 score : 0.288603157857 , rmse : 0.949859444783
#Normalized matrix for dist calculation (nearest half considered) - R2 score : 0.297425092775 , rmse : 0.940868649907
