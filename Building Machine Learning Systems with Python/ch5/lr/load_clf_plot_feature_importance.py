# -*- coding: utf-8 -*-
"""
Created on Thu Feb 02 12:51:42 2017

@author: saurabh.s1
"""

import numpy as np
import pickle
import matplotlib.pyplot as plt
clf = pickle.load(open("logreg.dat","r"))
feature_names = np.array((
    'NumTextTokens',
    'NumCodeLines',
    'LinkCount',
    'AvgSentLen',
    'AvgWordLen',
    'NumAllCaps',
    'NumExclams',
    'NumImages'
))
coeff = clf.coef_.transpose().reshape(len(feature_names,))
xy = sorted(zip(coeff, feature_names))
coeff = [x for x,y in xy]
feature_names = [y for x,y in xy]
print coeff
plt.bar(np.arange(8),coeff)
plt.xticks(np.arange(8), feature_names, rotation = 60)
plt.title("Feautre importance for LogReg, C = {}".format(clf.C))
plt.savefig("Feautre importance for LogReg, C = {}.png".format(clf.C))
plt.show()

