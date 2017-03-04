# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 12:49:13 2017

@author: saurabh suman
"""

from sklearn.datasets import load_boston

from sklearn.cross_validation import KFold
from model import train_model
from sklearn.linear_model import LinearRegression
import numpy as np
from plot import plot_path, plot_y_vs_ypredicted

#root mean squared error
def rmse(clf, X, y):
    clf.fit(X, y)
    y_predicted = clf.predict(X)
    from sklearn.metrics import mean_squared_error
    print("Root Mean Square Error: {}".format(np.sqrt(mean_squared_error(y, y_predicted))))

#load input and output data
boston = load_boston()
X = boston.data
y = boston.target

# initialize and train model using cross validation
clf = LinearRegression()
cv = KFold(len(X), 10, shuffle = True)
clf, train_score, test_score = train_model(clf, cv, X, y)
print("Train R2 score: {}\nTest R2 score: {}".format(train_score, test_score))
rmse(clf, X, y)
#Train R2 score: 0.741841312823
#Test R2 score: 0.711632756616
#Root Mean Square Error: 4.67950630064

##plot actual price vs predicted price
y_predicted = clf.predict(X)
plot_y_vs_ypredicted(y, y_predicted)

#Regularization Lasso, Ridge 
from sklearn.linear_model import Lasso, Ridge

alphas = [.01, .1, .5]
for alpha in alphas:
    clf = Ridge(alpha = alpha)
    clf, train_score, test_score = train_model(clf, cv, X, y)
    print("Ridge, alpha = {} :\n    Train Accuracy: {}\n    Test Accuracy: {}".format(alpha, train_score, test_score))
    clf = Lasso(alpha = alpha, normalize = False)
    clf, train_score, test_score = train_model(clf, cv, X, y)
    print("Lasso, alpha = {} :\n    Train Accuracy: {}\n    Test Accuracy: {}".format(alpha, train_score, test_score))
#no significant improvement in R2 scores

#Visualizing lasso path
alphas = np.logspace(-3, 2, 100)
lasso = Lasso()
alphas, coefs, _ = lasso.path(X, y, alphas = alphas)
plot_path(alphas, coefs.T, "Lasso path(Coefficient weights vs Alpha)")

#visualizing ridge path
alphas = np.logspace(-3, 5, 100)
ridge = Ridge()
coefs = []
for alpha in alphas:
    ridge.set_params(alpha = alpha)
    ridge.fit(X, y)
    coefs.append(ridge.coef_)
plot_path(alphas, coefs, "Ridge path(Coefficient weights vs Alpha)")




