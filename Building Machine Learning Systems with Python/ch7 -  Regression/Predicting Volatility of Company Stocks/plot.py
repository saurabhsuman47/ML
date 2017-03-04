# -*- coding: utf-8 -*-
"""
Created on Sat Mar 04 17:58:34 2017

@author: saurabh suman
"""
import matplotlib.pyplot as plt


def plot_y_vs_ypredicted(y, y_predicted):
    fig, ax = plt.subplots()
    ax.plot(y, y_predicted,'g.')
    ax.plot([y.min(), y.max()], [y.min(), y.max()],'r-')
    plt.xlabel('Actual Value')
    plt.ylabel('Predicted Value')
    plt.title("Regression over SEC data(Actual Values vs Predicted Values)")
    plt.savefig("Regression over SEC data(Actual Values vs Predicted Values).png")
    plt.show()
    
    fig, ax = plt.subplots()
    ax.plot(y,'r.', label = "Actual Value")
    ax.plot(y_predicted,'g.', label = "Predicted Value")
    ax.legend(loc = "upper right")
    plt.xlabel('Sample no')
    plt.ylabel('Risk (volatility)')
    plt.title("Regression over SEC data(Actual Values and Predicted Values for samples)")
    plt.savefig("Regression over SEC data(Actual Values and Predicted Values for samples).png")
    plt.show()
    

    
    