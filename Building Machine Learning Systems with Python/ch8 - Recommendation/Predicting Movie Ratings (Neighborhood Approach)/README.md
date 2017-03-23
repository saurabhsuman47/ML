This project is about predicting movie ratings.
to do:
  collaborative filtering
  neighborhood approach
  recommendation

Dataset: MovieLens 100K Dataset from Grouplens.
         Link: http://grouplens.org/datasets/movielens/100k/
         Stable benchmark dataset. 100,000 ratings from 1000 users on 1700 movies. Released 4/1998.

Contents:
1) load_data.py - contains function for loading the data from data file and returns training set and testing set as numpy array.
2) normalize.py - normalizer class containg functions for normalazing the matrix and inverting it back.
3) main.py - load and normalize data, calculate pairwise distances, predict the ratings of unrated movies by neighborhood approach. For each user-movie pair (u,m) predicted rating is average of movie m ratings of nearest neighbors of u.
