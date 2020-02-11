#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 22:15:39 2020

@author: prajwal
"""

import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd 

df = pd.read_csv('DF2')
X = df.iloc[:, 1].values
Y = df.iloc[:, 2].values

plt.scatter(X, Y)
plt.show()

Q = np.array([[2,.5],[.5,2]])

XY = np.vstack((X, Y)).transpose()
XYp = np.array([Q@point for point in XY])
print(XYp.shape)

Xp = XYp[:, 0]
Yp = XYp[:, 1]

plt.scatter(Xp, Yp)
plt.show()


print([X[0],Y[0]])
print(Q@[X[0],Y[0]])




