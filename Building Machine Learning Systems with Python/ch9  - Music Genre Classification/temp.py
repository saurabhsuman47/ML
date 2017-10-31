#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 18:35:26 2017

@author: saurabh
"""

import scipy.io.wavfile
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import os
import glob


## read a file to get sample_rate and samples
#wave_filename = "/home/saurabh/Downloads/heathens.wav"
#sample_rate, X = scipy.io.wavfile.read(wave_filename)
#print sample_rate, X
#print "max ", np.amax(X)
#print "min ", np.amin(X)
## plot the spectrogram of the samples
## X = np.array([3,1,1,-5,1,1,2,1,1,1,-10,1,4])
#plt.specgram(X, Fs = sample_rate)
#plt.show()
#plt.close('all')

##get curent working directory
#import os
#cwd = os.getcwd()
#print cwd
##glob basics
#import glob
##filepath = os.path.join()/home/saurabh/
#print glob.glob("/home/saurabh/*")


def read_fft_and_load(genre_list, base_dir):
    X = []    # list to store features for all audio
    Y = []    # list to store output labels(genres) for all audio
    for genre in genre_list:
        path_regex = os.path.join(base_dir, genre, "*.fft.npy")
        file_list = glob.glob(path_regex)
        for _file in file_list:
            fft_features = np.load(_file)
            X.append(fft_features[:1000])
            Y.append(genre)

    return np.array(X), np.array(Y)


genre_list = ["classical", "jazz", "country", "pop", "rock", "metal"]
directory = "/home/saurabh/ML/Building Machine Learning Systems with Python/ch9  - Music Genre Classification/genres"
X, Y = read_fft_and_load(genre_list, directory)

