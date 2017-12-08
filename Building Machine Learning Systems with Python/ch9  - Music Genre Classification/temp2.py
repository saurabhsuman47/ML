#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 10:47:50 2017

@author: saurabh
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Dec 07 11:44:25 2017

@author: saurabh.s1
"""
import scipy.io.wavfile
import numpy as np
import scipy as sp
import os
import glob
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from scikits.talkbox.features import mfcc

file_path = "testing/blues.00000.wav"
sample_rate, X = scipy.io.wavfile.read(file_path)
# Compute the spectrum magnitude -> spec = np.abs(fft(framed, nfft, axis=-1))
# Filter the spectrum through the triangle filterbank -> mspec = np.log10(np.dot(spec, fbank.T))
# Use the DCT to 'compress' the coefficients (spectrum -> cepstrum domain) -> ceps = dct(mspec, type=2, norm='ortho', axis=-1)[:, :nceps]
ceps, mspec, spec = mfcc(X)
print(ceps.shape)

#function to generate and save ceps in a file given input wave file
def generate_and_save_ceps(wave_file):
    sample_rate, X = sp.io.wavfile.read(wave_file)
    ceps, mspec, spec = mfcc(X)  #default 13 coefficients
    #ceps is a 2d array #frames*#coefficients
    num_frames = len(ceps)
    ceps_average_over_frames = np.mean(ceps[int(num_frames*0.1):int(num_frames*0.9)], axis=0) # leave starting one-tenth's and last one-tenth's
    ceps_file = wave_file[:-3] + "ceps"
    np.save(ceps_file, ceps_average_over_frames)

##test
#wave_filename = "testing/blues.00000.wav"
#generate_and_save_ceps(wave_filename)
#ceps_file = "testing/blues.00000.ceps.npy"
#ceps = np.load(ceps_file)

#create ceps files for all the wave files for all genres in directory, it is done for faster processing afterwards
directory = "/home/saurabh/ML/Building Machine Learning Systems with Python/ch9  - Music Genre Classification/genres"
for genre in os.listdir(directory):
    print genre
    subdir = os.path.join(directory, genre)
    for filename in os.listdir(subdir):
        if ".wav" in filename:
            input_file = os.path.join(subdir, filename)
            generate_and_save_ceps(input_file)


def read_ceps_and_load(genre_list, base_dir):
    X = []    # list to store ceps coefficients for all audio
    Y = []    # list to store output labels(genres) for all audio
    for genre in genre_list:
        path_regex = os.path.join(base_dir, genre, "*.ceps.npy")
        file_list = glob.glob(path_regex)
        for _file in file_list:
            ceps = np.load(_file)
            X.append(ceps)
            Y.append(genre)

    return np.array(X), np.array(Y)

#test


genre_list = ["classical", "country", "jazz", "metal", "pop", "rock"]
directory = "/home/saurabh/ML/Building Machine Learning Systems with Python/ch9  - Music Genre Classification/genres"
X, y = read_ceps_and_load(genre_list, directory)
labelencoder = preprocessing.LabelEncoder()
y = labelencoder.fit_transform(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state = 42)

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()

#from sklearn.neighbors import KNeighborsClassifier
#classifier = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p = 2)

#from sklearn.ensemble import RandomForestClassifier
#classifier = RandomForestClassifier()
#
#from sklearn.neural_network import MLPClassifier
#classifier = MLPClassifier()

classifier.fit(X_train, y_train)

# Predicting the train and test set results
y_train_pred = classifier.predict(X_train)
y_pred = classifier.predict(X_test)

print "train score" , classifier.score(X_train, y_train)
print "test score" , classifier.score(X_test, y_test)


from sklearn.metrics import confusion_matrix
cm_train = confusion_matrix(y_train, y_train_pred)
cm_test = confusion_matrix(y_test, y_pred)