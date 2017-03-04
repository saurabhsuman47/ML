# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 15:55:37 2016

@author: saurabh suman
"""

import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import numpy as np
import itertools
import random


#load and extract relevant data
data = load_iris()
features = data['data']
feature_names = data['feature_names']
target = data['target']

#create bool array for selection of samples for testing
test_idx = random.sample(range(150),20)
mylist=np.zeros(features.shape[0],dtype=bool)
mylist[test_idx] = 1


#create separate datasets for training and testing
training_features = features[~mylist,:]
training_target = target[~mylist]
pred_training_target = np.zeros(training_target.shape)
test_features = features[mylist,:]
test_target = target[mylist]
pred_test_target = np.zeros(test_target.shape)


#threshold calculation for classification of iris_setosa
plength = training_features[:,2] #determined by looking at plots of datasets
is_setosa = (training_target == 0)
max_setosa = plength[is_setosa].max()
min_non_setosa = plength[~is_setosa].min()


#selecting only the non-setosa features
training_features1 = training_features[~is_setosa]
training_target1 = training_target[~is_setosa]
is_virginica = (training_target1==2)

   
#threshold calculation for classification
best_accuracy = -1;
for fi in range(training_features1.shape[1]):
    #print fi
    for t in training_features1[:,fi]:
        pred = (training_features1[:,fi]>t)
        acc = (pred==is_virginica).mean()
        if(acc>best_accuracy):
            best_accuracy = acc;
            best_feature = fi;
            best_threshold = t;
            
#classification
for i in xrange(training_features.shape[0]):
    if(training_features[i,2]<(max_setosa + min_non_setosa)/2):
        pred_training_target[i]=0
    else:
        if(training_features[i,best_feature] > best_threshold):
            pred_training_target[i]=2
        else:
            pred_training_target[i]=1

print ("Accuracy on Training Data : %f" %(pred_training_target == training_target).mean())

for i in xrange(test_features.shape[0]):
    if(test_features[i,2]<(max_setosa + min_non_setosa)/2):
        pred_test_target[i]=0
        #print "Iris Setosa"
    else:
        if(test_features[i,best_feature] > best_threshold):
            pred_test_target[i]=2
            #print "Iris Virginia"
        else:
            pred_test_target[i]=1
            #print "Iris Versicolour"

            
print ("Accuracy on Test Data : %f" %(pred_test_target == test_target).mean())   
       