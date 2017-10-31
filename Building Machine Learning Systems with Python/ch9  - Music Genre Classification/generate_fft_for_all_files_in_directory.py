#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 23:19:09 2017

@author: saurabh
"""
import scipy.io.wavfile
import numpy as np
import scipy as sp
import os

#function to generate and save fft in a file given input wave file
def generate_and_save_fft(wave_file):
    sample_rate, X = sp.io.wavfile.read(wave_file)
    Y = abs((sp.fft(X))[:1000])   # change if different number of components are desired
    fft_file = wave_file[:-3] + "fft"
#    print fft_file
    np.save(fft_file, Y)

##test
#wave_filename = "/home/saurabh/Downloads/blues.00000.wav"
#generate_and_save_fft(wave_filename)


#create fft files for all the wave files for all genres in directory, it is done for faster processing afterwards
directory = "/home/saurabh/ML/Building Machine Learning Systems with Python/ch9  - Music Genre Classification/genres"
for genre in os.listdir(directory):
    print genre
    subdir = os.path.join(directory, genre)
    for filename in os.listdir(subdir):
        if ".wav" in filename:
            input_file = os.path.join(subdir, filename)
            generate_and_save_fft(input_file)