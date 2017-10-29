#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 16:31:18 2017

@author: saurabh
"""

import pysox
import sox

#load and get details of an audio using CSoxStream()
audio = pysox.CSoxStream("/home/saurabh/Downloads/output.mp3")
print audio
print repr(audio)
x = audio.get_signal()
print repr(x)
print x.get_signalinfo()
print(audio.get_encoding())


#transform input to output using Transformer()
tfm = sox.Transformer()
tfm.convert(50000, 2, 8)
tfm.build("/home/saurabh/Downloads/output1.mp3", "/home/saurabh/Downloads/output2.wav")
print tfm.effects_log
audio1 = pysox.CSoxStream("/home/saurabh/Downloads/output2.mp3")
print repr(audio1)
print(audio1.get_signal())
print(audio1.get_encoding())
