# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 12:07:37 2017

@author: saurabh
"""
import numpy as np

class normalizer(object):
    
    def __init__(self, axis = 1):
        self.axis = axis
    
    def fit(self, X, y = None):
        count = (X > 0).sum(axis = self.axis)
        count[count == 0] = 1       #to avoid division by zero when all element of a row/col is zero
        count = count * 1.0
        self.mean = X.sum(axis = self.axis)/count
        self.mean = (self.mean).reshape(len(self.mean),1)
        t1 = ((X - self.mean) ** 2)
        t1 = t1 * (X > 0)
        t1 = t1.sum(axis = self.axis)
        t1 = np.sqrt(0.1 + (t1 / count))        #add 0.1 to avoid division by zero when all element are same so t1 is zero
        self.std = t1.reshape(len(t1), 1)
    
    def transform(self, X):
        return ((X - self.mean) / self.std) * (X > 0)
    
    def fit_transform(self, X, y = None):
        self.fit(X)
        return self.transform(X)
        
    def inverse_transform(self, X):
        return (X * self.std) + self.mean
    
        
if __name__ == "__main__":
    test = np.array([[1,10],[3,20],[5, 0]])
    norm = normalizer()
    norm.fit(test)
    print("Mean : {}\nStd : {}\n".format(norm.mean, norm.std))
    norm_test = norm.transform(test) 
    inverse_norm_test = norm.inverse_transform(norm_test)   