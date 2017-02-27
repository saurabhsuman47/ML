# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 18:44:57 2016

@author: saurabh.s1
"""

import sklearn.datasets
from sklearn.cluster import KMeans
from StemmedTfidfVectorizer import StemmedTfidfVectorizer
from collections import Counter


#returns most occuring element from an array
def most_common_element(arr):
    most_occuring = Counter(arr).most_common(1)
    return most_occuring[0][0]

#path of the dataset
mlcomp_dir = r"C:\Users\saurabh.s1\Downloads\dataset-379-20news-18828_NKZWO"

#select what groups we want in testing and training data
#groups=np.array(['comp.graphics', 'comp.os.ms-windows.misc', 'comp.sys.ibm.pc.hardware', 'comp.sys.mac.hardware', 'comp.windows.x', 'sci.space'])

#training_data = sklearn.datasets.load_mlcomp(r"20news-18828", "train", mlcomp_root = mlcomp_dir, categories= groups)
#testing_data = sklearn.datasets.load_mlcomp(r"20news-18828", "test", mlcomp_root = mlcomp_dir, categories = groups)
training_data = sklearn.datasets.load_mlcomp(r"20news-18828", "train", mlcomp_root = mlcomp_dir)
testing_data = sklearn.datasets.load_mlcomp(r"20news-18828", "test", mlcomp_root = mlcomp_dir)


#template for varying parameters and checking error on training dataset
#for j in xrange(5,15):
#    vectorizer = StemmedTfidfVectorizer(min_df = j, max_df = .6, stop_words = 'english', decode_error = 'ignore')
#    
#    x = vectorizer.fit_transform(training_data.data)
#    num_samples, num_features = x.shape  
#    
##    num_clusters = len(groups)
#    num_clusters = len(training_data.target_names)
#    km = KMeans(n_clusters = num_clusters, init = 'k-means++', n_init=3, verbose = 0)
#    km.fit(x)
#    
#    error = 0
#    for i in xrange(num_clusters):
#        cluster_indices = (km.labels_ == i).nonzero()[0]
#        cluster_target = most_common_element(training_data.target[cluster_indices])
#        training_data_indices = (training_data.target == cluster_target).nonzero()[0]
#        error += sum(km.labels_[training_data_indices] != i)
# 
#    print('j={} , features={} , errors={}'.format(j, num_features, error))


#vectorizing the training data with StemmedTfidfVectorizer and then clustering using kmeans     
vectorizer = StemmedTfidfVectorizer(min_df = 5, max_df = .6, stop_words = 'english', decode_error = 'ignore')
x = vectorizer.fit_transform(training_data.data)
num_samples, num_features = x.shape
num_clusters = len(training_data.target_names)
#num_clusters = 100
km = KMeans(n_clusters = num_clusters, init = 'k-means++', n_init=4, verbose = 0)
km.fit(x)


#taking a new post, vectorizing, finding cluster, finding similar posts, then predicting the label by choosing the most common label
#new_post = "Disk drive problems. Hi, I have a problem with my hard disk. After 1 year it is working only sporadically now. I tried to format it, but now it doesn't boot any more. Any ideas? Thanks."
#new_post_vec = vectorizer.transform([new_post])
#new_post_label = km.predict(new_post_vec)[0]
#similar_indices = (km.labels_ == new_post_label).nonzero()[0]
##print similar_indices
#new_post_label = most_common_element(training_data.target[similar_indices])
#print training_data.target_names[new_post_label]


#for each post in testing dataset, vectorizing, finding cluster, finding similar posts, then predicting the label by choosing the most common label
#report the error as mismatches
error = 0
for i in xrange(len(testing_data.data)):
    test_post = testing_data.data[i]
    test_post_vec = vectorizer.transform([test_post])
#    print type(test_post_vec)
    test_post_km_label = km.predict(test_post_vec)[0]
    
    similar_indices = (km.labels_ == test_post_km_label).nonzero()[0]
    #print similar_indices
    test_post_predicted_label = most_common_element(training_data.target[similar_indices])
    if(test_post_predicted_label != testing_data.target[i]):
        error += 1

print error
        
        
        