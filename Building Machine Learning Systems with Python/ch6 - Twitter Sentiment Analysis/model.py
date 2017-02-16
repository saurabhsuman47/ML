# -*- coding: utf-8 -*-
"""
Created on Tue Feb 07 16:16:49 2017

@author: saurabh.s1
"""

from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.metrics import precision_recall_curve, auc
import numpy as np
import matplotlib.pyplot as plt


def pipeline_tfidf_nb():
    tfidf_vect = TfidfVectorizer( analyzer = "word")
    naive_bayes_clf = MultinomialNB()
    return Pipeline([('vect', tfidf_vect),('nbclf',naive_bayes_clf)])
                
def train_model(clf, cv, X, y, name, plot = False):    
    test_accuracy = []
    train_accuracy = []
    pr_auc_scores = []
    precisions, recalls, thresholds = [], [], []
    for train,test in cv:

        X_train = X[train]
        X_test = X[test]
        y_train = y[train]
        y_test = y[test]

        clf.fit(X_train, y_train)

        train_accuracy.append(clf.score(X_train, y_train))
        test_accuracy.append(clf.score(X_test, y_test))
        
        proba = clf.predict_proba(X_test)
        precision, recall, threshold = precision_recall_curve(y_test, proba[:,1])
        precisions.append(precision)
        recalls.append(recall)
        thresholds.append(threshold)
        pr_auc_scores.append(auc(recall,precision))
    
    if plot:
        scores_to_sort = pr_auc_scores
        median = np.argsort(scores_to_sort)[len(scores_to_sort) / 2]

        plt.plot(recalls[median], precisions[median], 'r-',label = "p/r")
        plt.fill_between(recalls[median], 0, precisions[median], facecolor = 'cyan')
        plt.ylim(.5, 1.05)
        plt.legend(loc = "right center")
        plt.xlabel('recall')
        plt.ylabel('precision')
        plt.title('P/R ({}), auc = {}'.format(name, np.mean(pr_auc_scores)))
        plt.savefig('PR - {}.png'.format(name))
        plt.show()
        
    return np.mean(train_accuracy), np.mean(test_accuracy), np.mean(pr_auc_scores)
        
    
