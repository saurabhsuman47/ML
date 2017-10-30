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



