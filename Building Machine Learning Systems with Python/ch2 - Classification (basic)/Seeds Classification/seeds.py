# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 13:33:34 2016

@author: saurabh suman
"""

import numpy as np
import random
from collections import Counter
import matplotlib.pyplot as plt

data = [];
labels = [];
distinct_labels_list =[];

#load dataset from the tsv file into data and labels(numpy arrays)
def load_dataset(path):
    global data,labels,distinct_labels_list
    with open(path) as input_file:
        for line in input_file:
            content = line.strip().split('\t')            
            data.append(content[0:-1])
            labels.append(content[-1])    
    data = np.array(data, dtype = float)
    labels = np.array(labels)
    distinct_labels_list = np.unique(labels)        

#generate training and testing dataset from data,labels by random sampling
def split_data1(percentage_testing):
    my_list = np.zeros(len(data),dtype=bool)
    test_idx = random.sample(range(len(data)),percentage_testing*len(data)/100) 
    my_list[test_idx] = 1;
    training_data = data[~my_list]
    training_labels = labels[~my_list]
    testing_data = data[my_list]
    testing_labels = labels[my_list] 
    return training_data, training_labels, testing_data, testing_labels
    
#generate training and testing dataset from data,labels by picking i then skipping skip_count then pick -> skip again ....
def split_data(i,skip_count):
    my_list = np.zeros(len(data),dtype=bool)
    my_list[i::skip_count] = 1;
    training_data = data[~my_list]
    training_labels = labels[~my_list]
    testing_data = data[my_list]
    testing_labels = labels[my_list] 
    return training_data, training_labels, testing_data, testing_labels
    
#mean normalization and feature scaling
def normalize():
    for feature in range(data.shape[1]):
       data[:,feature] -= data[:,feature].mean()
       data[:,feature] /= data[:,feature].std()
    
#returns distance between two vectors
def distance(vector0, vector1):
    return np.linalg.norm(vector0-vector1)
#    return np.sum((vector0-vector1)**2)

#returns most occuring element from an array
def most_common_element(arr):
    most_occuring = Counter(arr).most_common(1)
    return most_occuring[0][0]

#return label for new_example by finding the most common label from the k nearest neighbors                 
def classify_single_knn(training_data, training_labels, new_example, k):
    dist = []
    for i in xrange(len(training_data)):        
        dist.append((distance(training_data[i], new_example),training_labels[i]))
    dist.sort()
    dist = dist[:k]
    return most_common_element([label for _,label in dist])

#calculate prediction labels for testing dataset by calling classify_single_knn for each data in the dataset
def classify_all(training_data, training_labels, testing_data, k):
    pred = np.empty(len(testing_data), dtype = type(labels))
    for i in xrange(len(testing_data)):
        pred[i] = classify_single_knn(training_data, training_labels, testing_data[i],k)
    return pred

#return how correct the prediction are for the testing dataset by comparing with given labels
def accuracy(pred, testing_labels):
    return (pred == testing_labels).mean()
    
#vidualilzation on 2d    
def visualize():
    for color,marker,idx in zip("rgb","^+x",xrange(3)):
        rows = (labels == distinct_labels_list[idx])
        plt.scatter(data[rows,0],data[rows,2],color = color, marker = marker) 
    colors = "cmy" 
    area = np.pi*(7**2)
    training_data = np.empty((data.shape[0],2))
    training_data[:,0] = data[:,0]
    training_data[:,1] = data[:,2]
    for i in np.arange(-2.0,2.5,0.03):
        for j in np.arange(-3.0,2.5,0.05):
            pred = classify_single_knn(training_data, labels, (i,j),7)
            idx = np.where(distinct_labels_list == pred)
            color = colors[idx[0][0]]
            plt.scatter(i, j, s = area,  color = color, marker = "o", alpha = 0.2)
    plt.show()        
    
load_dataset("seeds.tsv")

normalize()

##cross validation##
folds_count = 10 #in how many parts data will be split
k = 7 #k of the knn
overall_accuracy = 0
for fold in xrange(folds_count):
    training_data, training_labels, testing_data, testing_labels = split_data(fold,folds_count)
    pred = classify_all(training_data, training_labels, testing_data, k )
    overall_accuracy += accuracy(pred, testing_labels)
 
print("K = %i\nNumber of folds for Cross-Validation = %i\nAccuracy = %f " %(k, folds_count, (overall_accuracy/folds_count)))

#variation of accuracy over k on randomly split data (percentage specified)##
percentage_testing = 30 #percentage of data to be used for testing
training_data, training_labels, testing_data, testing_labels = split_data1(percentage_testing)   
for k in xrange(5):
    pred = classify_all(training_data, training_labels, testing_data, 2*k+1)
    print("K=%i => Accuracy: %f " %(2*k + 1, accuracy(pred, testing_labels)))

visualize()

