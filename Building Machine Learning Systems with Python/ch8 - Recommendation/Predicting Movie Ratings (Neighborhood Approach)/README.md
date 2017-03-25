This project is about building a recommender system that predicts new movie ratings using past ratings.

Recommender system have become immensely popular and they are used for variety of products(movies, books, music etc). Recommender system provide an user with personalized suggestions from many options available.There are many approaches to design a recommender system such as collaborative filtering and content based filtering.

This project makes use of collaborative filtering - Users collaborate through the system to find best items for each other. 
In collaborative filtering, a user's past ratings as well as ratings of other users are used to build a model. This model is then used to predict items (or ratings for items) that the user may have an interest in.

For the collaborative filtering, neighborhood approach (user-based collaborative filtering) is used.

<p>
In the neighborhood-based approach:</br>
&nbsp;&nbsp;&nbsp;  1) Similarity between each user-user pair is calculated.</br>
&nbsp;&nbsp;&nbsp;  2) A number of users are selected which are closest to the active user.</br>
&nbsp;&nbsp;&nbsp;  3) A prediction for the active user is made by calculating a weighted average of the ratings of the selected users.</br>

Dataset:</br>
&nbsp;&nbsp;&nbsp;   * MovieLens 100K Dataset from Grouplens </br>
&nbsp;&nbsp;&nbsp;   * Link: http://grouplens.org/datasets/movielens/100k/</br>
&nbsp;&nbsp;&nbsp;   * Stable benchmark dataset. 100,000 ratings from 1000 users on 1700 movies. Released 4/1998.</br>
</p>

Contents:

1. load_data.py - contains function for loading the data from data file and returns training set and testing set as numpy array.

2. normalize.py - normalizer class containing functions for normalizing the matrix and inverting it back.

3. main.py - load and normalize data using correlation as metric, calculate pairwise distances, predict the ratings of unrated movies by neighborhood approach. For each user-movie pair (u,m) predicted rating is average of movie m ratings of nearest neighbors of u.

Results:

1. Binary matrix(rated vs not rated) for distance calculation, no normalization (half of nearest neighbors available are considered) - R2 score : 0.19078696037 , rmse : 1.01567341136

2. Binary matrix(rated vs not rated) for distance calculation, with normalization (half of nearest neighbors available are considered) - R2 score : 0.288603157857 , rmse : 0.949859444783

3. Normalized matrix for distance calculation (half of nearest neighbors available are considered) - R2 score : 0.297425092775 , rmse : 0.940868649907
