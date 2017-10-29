#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 18:35:26 2017

@author: saurabh
"""

import scipy.io.wavfile
import matplotlib.pyplot as plt
import numpy as np
import os

wave_filename = "/home/saurabh/ML/Building Machine Learning Systems with Python/ch9/genres/rock/rock.00000.wav"
wave_filename1 = "/home/saurabh/Downloads/heathens.wav"

# read a file to get sample_rate and samples
sample_rate, X = scipy.io.wavfile.read(wave_filename)
print sample_rate, X
print "max ", np.amax(X)
print "min ", np.amin(X)
# plot the spectrogram of the samples
# X = np.array([3,1,1,-5,1,1,2,1,1,1,-10,1,4])
plt.specgram(X, Fs = sample_rate)
plt.show()
plt.close('all')

##Plot spectrogram of first 3 audios of each genres in single png
#directory = "/home/saurabh/ML/Building Machine Learning Systems with Python/ch9/genres"
#i = 1
#plt.figure(figsize=(25, 14))
#
#for genre in os.listdir(directory):
#    print genre
#    subdir = os.path.join(directory, genre)
#    for filename in os.listdir(subdir):
#        for j in range(0,3):
#            matchstring = "0000" + str(j)
#            if matchstring in filename:
#                conplete_path = os.path.join(subdir, filename)
#                sample_rate, X = scipy.io.wavfile.read(conplete_path)
#                #print sample_rate, X
#                #print i
#                plt.subplot(10, 3, i)
#                i += 1
#                plt.specgram(X, Fs = sample_rate)
#                plt.title(filename)
#                #plt.show()
#
#plt.suptitle("Spectogram of different music genres")
#plt.tight_layout()
#plt.savefig('Spectogram of different music genres.png')
#plt.close('all')

#testing sine waves
# $ sox --null -r 22050 sine_a.wav synth 0.2 sine 400
# $ sox --null -r 22050 sine_b.wav synth 0.2 sine 3000
# $ sox --combine mix --volume 1 sine_b.wav --volume 0.5 sine_a.wav sine_mix.wav
wave_filename1 = "/home/saurabh/sine_a.wav"
sample_rate, X = scipy.io.wavfile.read(wave_filename1)
print sample_rate, X
print "max ", np.amax(X)
print "min ", np.amin(X)
plt.specgram(X, Fs = sample_rate)
plt.show()
wave_filename1 = "/home/saurabh/sine_b.wav"
sample_rate, X = scipy.io.wavfile.read(wave_filename1)
print sample_rate, X
print "max ", np.amax(X)
print "min ", np.amin(X)
plt.specgram(X, Fs = sample_rate)
plt.show()
wave_filename1 = "/home/saurabh/sine_mix.wav"
sample_rate, X = scipy.io.wavfile.read(wave_filename1)
print sample_rate, X
print "max ", np.amax(X)
print "min ", np.amin(X)
plt.specgram(X, Fs = sample_rate)
plt.show()
plt.close('all')