#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 02:21:33 2020

@author: prajwal
"""

#Problem a
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

top_number_string = input ('Enter top number: ')
year = input ('Enter date: ')
top_number = int(top_number_string)
file_name = 'yob'+year+'.txt'


def getTopNames(file_name, top_number):
   df = pd.read_csv(file_name, names = ['Name','Gender', 'Frequency'])
   df = df.sort_values(by = 'Frequency', ascending = False)
   df.reset_index(drop = True, inplace = True)
   data = df.iloc[:top_number, 0]
   print (data)

getTopNames(file_name, top_number)

#Problem b
import os 

entered_name = input('Enter name: ')
count = 0;

for filename in os.listdir('Names'):
    if filename.endswith('.txt'):
        df = pd.read_csv(filename, names = ['Name', 'Gender', 'Frequency'])
        index_names = df.loc[df['Name']== entered_name].index.values
        for i in index_names:
            count = count + int (df.loc[i,'Frequency'])
print ('Frequency = ', count)

#Problem c
#find relative frequency 
entered_name = input('Enter name: ')
name_frequncy = 0;
total_frequency = 0;

for filename in os.listdir('Names'):
    if filename.endswith('.txt'):
        df = pd.read_csv(filename, names = ['Name', 'Gender', 'Frequency'])
        total_frequency = total_frequency + df['Frequency'].sum()
        index_names = df.loc[df['Name']== entered_name].index.values
        for i in index_names:
            name_frequncy = name_frequncy + int (df.loc[i,'Frequency'])
print ('Relative Frequency = ', (count/total_frequency))


#Problem d
#Append a new column with dates'

df_combined = pd.DataFrame(columns = ['Name', 'Gender', 'Frequency', 'Year']) 

for filename in os.listdir('Names'):
    if filename.endswith('.txt'):
        df = pd.read_csv(filename, names = ['Name', 'Gender', 'Frequency'])
        df['Year'] =  int(filename[3:7])
        df_combined = df_combined.append(df, ignore_index = True)









        
        

