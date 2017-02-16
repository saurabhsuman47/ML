# -*- coding: utf-8 -*-
"""
Created on Thu Feb 09 14:23:46 2017

@author: saurabh.s1
"""
from load_data import load_data
from model import pipeline_tfidf_nb
from model import train_model
from sklearn.cross_validation import ShuffleSplit
from sklearn.grid_search import GridSearchCV
import pickle

# https://raw.githubusercontent.com/zfz/twitter_corpus/master/full-corpus.csv
input_file = "full-corpus.csv"
X,y = load_data(input_file)

clf = pipeline_tfidf_nb()
cv = ShuffleSplit(n = len(X), test_size = .3, n_iter = 10, random_state = 0)

#clf_param_grid = dict(vect__ngram_range = [(1,1),(1,2),(1,3)],
#                   vect__min_df = [1,2],
#                    vect__stop_words=[None, "english"],
#                    vect__smooth_idf = [False, True],
#                    vect__use_idf = [False, True],
#                    vect__sublinear_tf = [False, True],
#                    vect__binary = [False, True],
#                    nbclf__alpha = [0, 0.01, 0.05, 0.1, 0.5, 1],
#                  )
#
#
#grid_search = GridSearchCV(estimator = clf, param_grid = clf_param_grid, cv = cv, scoring = 'f1')
#grid_search.fit(X, y)
#print grid_search.best_estimator_
#pickle.dump(grid_search.best_estimator_, open("clf.dat","w"))

clf = pickle.load(open("clf.dat","r"))
train_accuracy, test_accuracy, pr_auc = train_model(clf, cv, X, y, name = "pos-neg", plot = True)
print("Train Accuracy = {}\nTest Accuracy = {}\nPrecision Recall Area Under Curve = {}\n".format(train_accuracy, test_accuracy, pr_auc))
