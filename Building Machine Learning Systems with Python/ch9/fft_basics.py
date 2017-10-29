#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 15:33:24 2017

@author: saurabh
"""

import scipy.io.wavfile
import numpy as np
import matplotlib.pyplot as plt

def generate_fft(wave_filename):
    sample_rate, X = scipy.io.wavfile.read(wave_filename)
    Y1 = sp.fft(X)[:4000]
    Y = abs(Y1)
    plt.plot(range(0, 4000), Y)
    plt.show()

wave_filename1 = "/home/saurabh/sine_a.wav"
generate_fft(wave_filename1)
wave_filename1 = "/home/saurabh/sine_b.wav"
generate_fft(wave_filename1)
wave_filename1 = "/home/saurabh/sine_mix.wav"
generate_fft(wave_filename1)
wave_filename1 = "/home/saurabh/Downloads/heathens.wav"
generate_fft(wave_filename1)