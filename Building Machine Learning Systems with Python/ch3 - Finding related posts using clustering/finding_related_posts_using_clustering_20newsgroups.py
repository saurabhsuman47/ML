# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 10:28:06 2016

@author: saurabh.s1
"""
import sklearn.datasets
from sklearn.cluster import KMeans
import numpy as np
import scipy as sp
from StemmedTfidfVectorizer import StemmedTfidfVectorizer

#path of the dataset
mlcomp_dir = r"C:\Users\saurabh.s1\Downloads\dataset-379-20news-18828_NKZWO"

#select what groups we want in testing and training data
groups=np.array(['comp.graphics', 'comp.os.ms-windows.misc', 'comp.sys.ibm.pc.hardware', 'comp.sys.mac.hardware', 'comp.windows.x', 'sci.space'])

training_data = sklearn.datasets.load_mlcomp(r"20news-18828", "train", mlcomp_root = mlcomp_dir, categories= groups)
testing_data = sklearn.datasets.load_mlcomp(r"20news-18828", "test", mlcomp_root = mlcomp_dir, categories = groups)
#training_data = sklearn.datasets.load_mlcomp(r"20news-18828", "train", mlcomp_root = mlcomp_dir)
#testing_data = sklearn.datasets.load_mlcomp(r"20news-18828", "test", mlcomp_root = mlcomp_dir)


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
vectorizer = StemmedTfidfVectorizer(min_df = 10, max_df = .6, stop_words = 'english', decode_error = 'ignore')
x = vectorizer.fit_transform(training_data.data)
num_samples, num_features = x.shape
km = KMeans(n_clusters = 50, init = 'k-means++', n_init=2, verbose = 0)
km.fit(x)


#taking a new post, vectorizing, finding cluster, finding similar posts, then choosing the most similar
#new_post = "Disk drive problems. Hi, I have a problem with my hard disk. After 1 year it is working only sporadically now. I tried to format it, but now it doesn't boot any more. Any ideas? Thanks."
#new_post_vec = vectorizer.transform([new_post])
#new_post_label = km.predict(new_post_vec)[0]
#
#similar_indices = (km.labels_ == new_post_label).nonzero()[0]
#print len(similar_indices)
#
#similar = []
#for i in similar_indices:
#    dist = sp.linalg.norm((new_post_vec - x[i]).toarray())
#    similar.append((dist,i))
#similar = sorted(similar)
#print similar[0]
#print training_data.data[similar[0][1]]
#print similar[1]
#print training_data.data[similar[1][1]]


#taking some posts from testing data, vectorizing, finding cluster, finding similar posts, then choosing the most similar
output_file = "output.html"
f = open(output_file, 'w')
f.flush()
for i in xrange(10):
    test_post = testing_data.data[i]
    test_post_vec = vectorizer.transform([test_post])
    test_post_km_label = km.predict(test_post_vec)[0]    
    similar_indices = (km.labels_ == test_post_km_label).nonzero()[0]
    similar = []
    for j in similar_indices:
        dist = sp.linalg.norm((test_post_vec - x[j]).toarray())
        similar.append((dist,j))
    similar = sorted(similar)
    most_similar_post_index = similar[0][1]
    s1 = "Post " + str(i+1) + " => Distance: " +  str(similar[0][0]) + "\n"
    f.write("""
      <body bgcolor="#F7F7FB">
          <h1 style="color: red; font-family: 'Liberation Sans',sans-serif; font-size: 100%;">
             <u>{}</u>
          </h1>
    """.format(s1))
    
    s1 = "Original Post  ( Subject: " + testing_data.target_names[testing_data.target[i]] + " )"
    f.write("""
      <h3 style="color: blue; font-family: 'Liberation Sans',sans-serif; font-size: 100%;">
        <u>{}</u>
      </h1>
    """.format(s1))
    test_post = test_post.replace("\n\n","\n")
    f.write("""
      <p style="color: #000000; font-family: 'Times New Roman',sans-serif; font-size: 100%;">
        {}
      </p>
    """.format(test_post.replace("\n","<br />\n")))
    
    s1 = "Most Similar Post  ( Subject: " + training_data.target_names[training_data.target[most_similar_post_index]]  + " , Post Index: " + str(most_similar_post_index) + " )"
    f.write("""
      <h3 style="color: #AA00AA; font-family: 'Liberation Sans',sans-serif; font-size: 100%;">
        <u>{}</u>
      </h1>
    """.format(s1))
    s1 = training_data.data[most_similar_post_index].replace("\n\n","\n")
    f.write("""
      <p style="color: #000000; font-family: 'Times New Roman',sans-serif; font-size: 100%;">
        {}
      </p></body>
    """.format(s1.replace("\n","<br />\n")))
    
f.close()   

    

        
        
        