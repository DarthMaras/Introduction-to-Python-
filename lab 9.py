# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 11:14:54 2022

@author: hsamarag
"""
file_path = "M:\sales.csv"


#check that plotting is working
import pandas as pd

#if you get error. panda cannot read your FILE
file_name = "sales.csv"
sales = pd.read_csv(file_path)

#this should open a new window that you can customise

sales.plot.scatter(x="Store", y="Weekly_Sales")

#Exercise1 Data Exploration
print(file_name.unique(store))

