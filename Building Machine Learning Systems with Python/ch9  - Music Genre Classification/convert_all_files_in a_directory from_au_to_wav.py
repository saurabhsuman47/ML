#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 20:44:50 2017

@author: saurabh
"""
#use sox transformer to convert .au file to .wav file so that it can be readed by scipy.io.wavfile.read()

import sox
import os

directory = "/home/saurabh/ML/Building Machine Learning Systems with Python/ch9/genres"
tfm = sox.Transformer()

for genre in os.listdir(directory):
    print genre
    subdir = os.path.join(directory, genre)
    for filename in os.listdir(subdir):
        if ".au" in filename:
            input_file = os.path.join(subdir, filename)
            new_file_name = filename[:-2] + "wav"
            output_file = os.path.join(subdir, new_file_name)
            tfm.build(input_file, output_file)
            os.remove(input_file)
