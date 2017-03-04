# -*- coding: utf-8 -*-
"""
Created on Sat Mar 04 17:58:34 2017

@author: saurabh suman
"""
import matplotlib.pyplot as plt

def plot_path(alphas, coefs, title):
    plt.plot(alphas, coefs)
    plt.xscale('log')
    plt.xlim(alphas.max(), alphas.min())
    plt.ylabel("Coefficient Weight")
    plt.xlabel("Alpha (10^alpha)")
    plt.title(title)
    plt.savefig(title + ".png")
    plt.show()

def plot_y_vs_ypredicted(y, y_predicted): 
    fig, ax = plt.subplots()
    ax.plot(y, y_predicted,'g.')
    ax.plot([y.min(), y.max()], [y.min(), y.max()],'r-')
    plt.xlabel('Actual Price')
    plt.ylabel('Predicted Price')
    plt.title("Regression over Boston data(Actual Values vs Predicted Values)")
    plt.savefig("Regression over Boston data(Actual Values vs Predicted Values).png")
    plt.show()
    
    fig, ax = plt.subplots()
    ax.plot(y,'r.', label = "Actual Price")
    ax.plot(y_predicted,'g.', label = "Predicted Price")
    ax.legend(loc = "upper right")
    plt.xlabel('Sample no')
    plt.ylabel('Price')
    plt.title("Regression over Boston data(Actual Values and Predicted Values for samples)")
    plt.savefig("Regression over Boston data(Actual Values and Predicted Values for samples).png")
    plt.show()
    
    