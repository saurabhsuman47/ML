#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 23:19:09 2017

@author: saurabh
"""

import numpy as np
import scipy as sp
import pandas as pd
import os


##Read file
file_path = "train.csv"
df = pd.read_csv(file_path)


##Get relevent columns from the file data for input and output dataset
X = df.iloc[:, [2, 4, 5, 6, 7, 9]] #passenger class, sex, age, sibling count, parent count, fare
y = df.iloc[:, 1]


##Manipulate data
from sklearn import preprocessing
labelencoder = preprocessing.LabelEncoder() # encodes labels to continuous numbers
onehotencoder = preprocessing.OneHotEncoder() # encodes 1 column to n number of columns where n is the number of possible values in the column
X.iloc[:, 1] = labelencoder.fit_transform(X.iloc[:, 1]) # encode sex
#X.iloc[:, -1] = labelencoder.fit_transform(X.iloc[:, -1])
#A = onehotencoder.fit_transform(X.iloc[:, -1:]).toarray()
#X = pd.concat([X, pd.DataFrame(A)], axis=1)


##Code for generating feature based  on whether rate title is present in  preson's name(from kaggle kernel - didnt improve score though)
#name = df.iloc[:, 3]
#feat = []
#titles = set(['Dona', 'Lady', 'the Countess','Capt.', 'Col.', 'Don.', 'Dr.', 'Major', 'Rev.', 'Sir', 'Jonkheer'])
#for i in range(0, 891):
#    flag = 0
#    for title in titles:
#        if title in name[i]:
#            feat.append(1)
#            flag = 1
#            break
#    if flag == 0:
#        feat.append(0)
#X = pd.concat([X, pd.DataFrame(feat)], axis=1)


##Fill empty values with mean values(very important) and scale(didnt improve accuracy)
X = X.fillna(X.mean())
#X = preprocessing.scale(X)


##Splitting the dataset into the Training set and crossvalidation set
from sklearn.cross_validation import train_test_split
X_train, X_cv, y_train, y_cv = train_test_split(X, y, test_size = 0.1, random_state = 0)


##Classifiers of all sorts
#from sklearn.linear_model import LogisticRegression
#clf = LogisticRegression()
#from sklearn.tree import DecisionTreeClassifier
#clf = DecisionTreeClassifier()
from sklearn.ensemble import RandomForestClassifier
#clf = RandomForestClassifier()
clf = RandomForestClassifier(max_depth=6, n_estimators=10) #gives best result =.794 on kaggle
#from sklearn.naive_bayes import GaussianNB
#clf = GaussianNB()
#from sklearn.svm import SVC
#clf = SVC(kernel = 'rbf')
#from sklearn.neural_network import MLPClassifier
#clf = MLPClassifier()
#from sklearn.ensemble import AdaBoostClassifier
#clf = AdaBoostClassifier()
#from sklearn.neighbors import KNeighborsClassifier
#clf = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p = 2)


##Fit the training data
clf.fit(X_train, y_train)


##Measuring accuracy
from sklearn.metrics import confusion_matrix
y_pred = clf.predict(X_cv)
cm = confusion_matrix(y_cv, y_pred)
print "train score" , clf.score(X_train, y_train)
print "test score" , clf.score(X_cv, y_cv)


###-------------------------------------------Test----------------------------------------------------###


##Read test file
test_filepath =  "test.csv"
df1 = pd.read_csv(test_filepath)


##Get relevent columns from the test file data for input
X_test = df1.iloc[:, [1, 3, 4, 5, 6, 8]]


##Manipulate data - same as above(for training data)
labelencoder = preprocessing.LabelEncoder()
X_test.iloc[:, 1] = labelencoder.fit_transform(X_test.iloc[:, 1])
#name = df1.iloc[:, 2]
#feat = []
#titles = set(['Dona', 'Lady', 'the Countess','Capt.', 'Col.', 'Don.', 'Dr.', 'Major', 'Rev.', 'Sir', 'Jonkheer'])
#for i in range(0, 418):
#    flag = 0
#    for title in titles:
#        if title in name[i]:
#            feat.append(1)
#            flag = 1
#            break
#    if flag == 0:
#        feat.append(0)
#X_test = pd.concat([X_test, pd.DataFrame(feat)], axis=1)
X_test = X_test.fillna(X_test.mean())


##Predict for the test values using the trained classifier
y_test_pred = clf.predict(X_test)


##Generate output file
output = pd.concat([ pd.DataFrame(np.arange(892, 1310), columns=['PassengerId']), pd.DataFrame(y_test_pred, columns=['Survived'])], axis = 1)
output.to_csv("output.csv", index=False)


