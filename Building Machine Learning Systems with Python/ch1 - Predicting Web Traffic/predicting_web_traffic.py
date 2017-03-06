#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 22:53:00 2017

@author: saurabh
"""
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
data = sp.genfromtxt("web_traffic.tsv",delimiter="\t")

x = data[:,0];
y = data[:,1];
x = x[~np.isnan(y)]
y = y[~np.isnan(y)]

fig, ax = plt.subplots()     
area = np.pi*(1.2**2)
ax.scatter(x,y,s=area,c="#00BBBB",alpha = 0.7)
plt.title("Web Traffic over the last month")
plt.xlabel("Time")
plt.ylabel("Hits/Hour")
plt.xticks([w*7*24 for w in range(10)],['week %i' %w for w in range(10)])
plt.grid()
plt.autoscale(tight=True)

def error(f,x,y):
    return sp.sum((f(x)-y)**2)   


fx=sp.linspace(0,x[-1]+100,1000)
for i in range(1,6):
    fp1= sp.polyfit(x,y,i)
    f1 = sp.poly1d(fp1)
    ax.plot(fx,f1(fx),linewidth = 1, label = i)
    
ax.legend(loc = "upper left")
plt.title("Web Traffic prediction using different order polynomial")
plt.savefig("Web Traffic Prediction.png")   
plt.show()

