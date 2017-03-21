# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 15:39:06 2017

@author: saurabh
"""

from load_data import load_data
import numpy as np
from scipy.spatial import distance
from sklearn.metrics import r2_score
import math
import os
from normalize import normalizer

data_path = os.path.join("..","ml-100k","u.data")
train_reviews, test_reviews = load_data(data_path, test_percentage = 10)
num_users, num_movies = train_reviews.shape

binary = train_reviews > 0

norm = normalizer()
train_reviews = norm.fit_transform(train_reviews)


 
dist_between_users = distance.pdist(binary, metric = 'correlation') 
dist_between_users = distance.squareform(dist_between_users)
neighbors = dist_between_users.argsort(axis = 1)

filled = train_reviews.copy()
flag = 0
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

##when there is no movie for rating in training data (ratings went to testing data), we get nan values which we need to rate 3 
average_rating = (train_reviews.sum())/(binary.sum())           
for user in range(num_users):
    for movie in range(num_movies):
        if math.isnan(filled[user][movie]):
            filled[user][movie] = average_rating                

filled = norm.inverse_transform(filled)

r2 = r2_score(test_reviews[test_reviews > 0.0], filled[test_reviews > 0.0])
print("R2 Score - Binary neighbors (nearest half considered) : {}".format(r2))

#R2 Score - Binary neighbors (all users considered) : 0.166722650833
#R2 Score - Binary neighbors (nearest half considered) : 0.18
#R2 Score - Normalized reviews for distance calculation (nearest half considered) : 0.295960386592