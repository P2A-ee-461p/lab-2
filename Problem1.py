# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 23:55:14 2020

@author: Anthony
"""
import pandas as pandas
import numpy as numpy
from pandas import read_csv
import matplotlib as matplotlib

data1 = read_csv("DF1", index_col=0)

df = pandas.DataFrame(data1)



print("We now will plot columns against other columns for analysis.")

for i in range(0, len(df.columns)):
    for j in range(i+1, len(df.columns)):
            df.plot.scatter(i,j)
matplotlib.pyplot.show()
            
print("From the plots, we observe:")
print("Columns 1 and 3 are correlated")
print("Columns 0 and 2 are correlated")

print("Now we compute the covariance matrix using df.cov()")
print("A covariant matrix shows the covariance between each pair of elements. The pair of features being shown by a given value is the value's position in the covariance matrix")
print("This means that the diagonal of the covariance matrix is the variance of each individual feature")
cov = df.cov()

print("Which yields the following:")
print(cov)

print("We now choose the following covariance matrix that we will generate random values from using numpy:")

cov = [[5,0,0],
       [0,5,4],
       [0,4,5]]


print(cov)

mean = [0,0,0]
data = []
for i in range(1,20):
    samples = numpy.random.multivariate_normal(mean, cov, 2**i)
    df2 = pandas.DataFrame(samples)
    data.append([i,df2.cov()[1].values[2]]) #We extract the covariance between X2 and X3

df2 = pandas.DataFrame(data)
plot = df2.plot.scatter(0,1)
plot.set_ylabel("Covariance")
plot.set_xlabel("2 raised to this value samples")
plot.hlines(y=4, xmin=0, xmax=20)

matplotlib.pyplot.show()  

print("The true covariance is 4. As we take more (double) samples, the covariance tends to approach the true covariance value of 4.")