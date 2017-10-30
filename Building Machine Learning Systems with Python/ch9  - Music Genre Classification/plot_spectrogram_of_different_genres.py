#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 21:38:17 2017

@author: saurabh
"""
import os
import scipy.io.wavfile
import matplotlib.pyplot as plt

#Plot spectrogram of first 3 audios of each genres in single png

directory = "/home/saurabh/ML/Building Machine Learning Systems with Python/ch9/genres"
i = 1
plt.figure(figsize=(25, 14))

for genre in os.listdir(directory):
    print genre
    subdir = os.path.join(directory, genre)
    for filename in os.listdir(subdir):
        for j in range(0,3):
            matchstring = "0000" + str(j)
            if matchstring in filename:
                conplete_path = os.path.join(subdir, filename)
                sample_rate, X = scipy.io.wavfile.read(conplete_path)
                #print sample_rate, X
                #print i
                plt.subplot(10, 3, i)
                i += 1
                plt.specgram(X, Fs = sample_rate)
                plt.title(filename)
                #plt.show()

plt.suptitle("Spectogram of different music genres")
plt.tight_layout()
plt.savefig('Spectogram of different music genres.png')
plt.close('all')