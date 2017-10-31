#!/usr/bin/env python2
# -*- coding: utf-8 -*- X.shape[0] X.shape[0] X.shape[0] X.shape[0] X.shape[0] X.shape[0] X.shape[0] X.shape[ X.shape[0]0]
"""
Created on Fri Oct 27 15:33:24 2017

@author: saurabh
"""

import scipy.io.wavfile
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

#generate fft of a audio signal and plots it, with max freq option upto which plot should extend on x axis
def generate_plot_fft(wave_filename, max_freq_plot = None):
    sample_rate, X = scipy.io.wavfile.read(wave_filename)
    duration = ((X.shape[0] / sample_rate))
    N = X.shape[0] # number of samples
    T = 1.0 / sample_rate# sample spacing
    Y = sp.fft(X) # calculate fft
    #factor expands the x scale
    factor = 1
    if max_freq_plot is not None:
        factor = 2*max_freq_plot*T
    xf = np.linspace(0.0, 1*factor/(2.0*T), N*factor/2) #get x axis points =  freq for plotting
    plt.plot(xf, 2.0/N * np.abs(Y[0:N*factor/2])) # plot x and y (number of y points should be equal to x)
    plt.grid()
    plt.show()

# without support max freq upto which it should be plotted option, it plots upto sample_rate/2 Hz
# simple to understand, first check this
#def generate_plot_fft(wave_filename):
#    sample_rate, X = scipy.io.wavfile.read(wave_filename)
#    duration = ((X.shape[0] / sample_rate))
#    Y = sp.fftpack.fft(X) # calculate fft
#    N = X.shape[0] # number of samples
#    T = 1.0 / sample_rate# sample spacing
#    xf = np.linspace(0.0, 1.0/(2.0*T), N/2)
#    plt.plot(xf, 2.0/N * np.abs(Y[0:N/2]))
#    plt.grid()
#    plt.show()


# $ sox --null -r 22050 sine_a.wav synth 0.2 sine 400
# $ sox --null -r 22050 sine_b.wav synth 0.2 sine 3000
# $ sox --combine mix --volume 1 sine_b.wav --volume 0.5 sine_a.wav sine_mix.wav
wave_filename1 = "/home/saurabh/sine_a.wav"
generate_plot_fft(wave_filename1)
wave_filename1 = "/home/saurabh/sine_b.wav"
generate_plot_fft(wave_filename1)
wave_filename1 = "/home/saurabh/sine_mix.wav"
generate_plot_fft(wave_filename1)

wave_filename1 = "/home/saurabh/Downloads/100Hz_44100Hz_16bit_05sec.wav"
generate_plot_fft(wave_filename1, max_freq_plot = 1000)
wave_filename1 = "/home/saurabh/Downloads/100Hz_44100Hz_16bit_30sec.wav"
generate_plot_fft(wave_filename1,  max_freq_plot = 1000)


#generate a signal, generate its , plot the fft
N = 600 # Number of sample points
T = 1.0 / 800.0 # sample spacing
x = np.linspace(0.0, N*T, N) # times at which y should be calculated
y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x) # calculate signal
yf = sp.fft(y) # calculate fft
xf = np.linspace(0.0, 1.0/(2.0*T), N//2) #get x axis points =  freq for plotting
plt.plot(xf, 2.0/N * np.abs(yf[0:N//2])) # plot x and y (number of y points should be equal to x)
plt.grid()
plt.show()