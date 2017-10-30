#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 21:16:21 2017

@author: saurabh
"""
import scipy.io.wavfile
import matplotlib.pyplot as plt
import numpy as np

#exploring sine waves
#generate sine waves from sox and check their properties, min, max, specgram
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