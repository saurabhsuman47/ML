# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 12:46:37 2017

@author: saurabh
"""

import numpy as np
from scipy.sparse import csr_matrix as csr
import random


def load_data(input_file, test_percentage):
    data = np.loadtxt(input_file)
    
    rating = data[:, 2]         #1-5
    number_ratings = len(rating)
    
    user_ids = data[:, 0].astype(int)
    user_ids -= 1           #convert to 0 based indexing
    movie_ids = data[:, 1].astype(int)
    movie_ids -= 1          #convert to 0 based indexing
    reviews = csr((rating, (user_ids, movie_ids)), shape = (max(user_ids) + 1, max(movie_ids) + 1))
    reviews = reviews.toarray()
    
    test_idxs = np.array(random.sample(range(number_ratings), number_ratings/test_percentage))
    
    train_reviews = np.array(reviews)
    for idx in test_idxs:
        train_reviews[user_ids[idx]][movie_ids[idx]] = 0
    
    test_reviews = np.zeros_like(reviews)
    for idx in test_idxs:
        test_reviews[user_ids[idx]][movie_ids[idx]] = reviews[user_ids[idx]][movie_ids[idx]]

    return train_reviews, test_reviews
