# -*- coding: utf-8 -*-
"""
Created on Thu Mar 02 19:56:38 2017

@author: saurabh.s1
"""

from sklearn.datasets import load_svmlight_file
from sklearn.linear_model import LinearRegression, ElasticNet, ElasticNetCV
from sklearn.cross_validation import KFold
from model import train_model
from plot import plot_y_vs_ypredicted

#Load data and target
X, y = load_svmlight_file('E2006.train')
num_samples, num_features = X.shape


#linear regression with cv without regularization
clf = LinearRegression()
cv = KFold(num_samples, n_folds = 3)
clf, train_score, test_score = train_model(clf, cv, X, y)
print("Train R2 score = {}\nTest R2 score = {}".format(train_score, test_score))
#Train R2 score = 0.99999261654 , overfitting - will not generalize well
#Test R2 score = -0.129615667613


#ElasticNet with cv with alpha = .1
clf = ElasticNet(alpha = .1)
cv = KFold(num_samples, n_folds = 3)
clf, train_score, test_score = train_model(clf, cv, X, y)
print("Train R2 score = {}\nTest R2 score = {}".format(train_score, test_score))
#Train R2 score = 0.606471796547
#Test R2 score = 0.606507736107


#ElasticNetCV with cv and  L1_ratio (Since the inout is very sparse, L1 is preferred)
l1_ratio = [.5, .9, .95, 1.0]
clf = ElasticNetCV(l1_ratio = l1_ratio)
cv = KFold(num_samples , n_folds = 3)
clf, train_score, test_score = train_model(clf, cv, X, y)
print("Train R2 score = {}\nTest R2 score = {}".format(train_score, test_score))
#Train R2 score = 0.653843711527
#Test R2 score = 0.653738364217

print clf.alpha_  # 0.000303368283226
print clf.alphas #None
print clf.l1_ratio_ # 1.0
print clf.l1_ratio #[0.5, 0.9, 0.95, 1.0]
    
#plot    
y_predicted = clf.predict(X)    
plot_y_vs_ypredicted(y, y_predicted)



