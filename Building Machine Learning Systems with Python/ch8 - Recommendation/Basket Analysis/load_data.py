# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 10:07:13 2017

@author: saurabh
"""
from collections import Counter
from matplotlib import pyplot as plt
import numpy as np

def load_data(filename):
    cnt = Counter()
    S1 = set()
    with open(filename) as f:
        for line in f:
            items = line.strip().split(" ")
            S1.add(frozenset(items))
            for item in items:
                cnt[item] += 1  
    return S1, cnt      

if __name__ == "__main__":
    input_file = "retail.dat"
    T, cnt  =  load_data(input_file)
    labels, values = zip(*cnt.items())
    plt.hist(np.log2(values), range = [0,10], facecolor = "cyan")
    plt.show()
           