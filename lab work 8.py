# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 12:04:34 2022

@author: hsamarag
"""

#Pandas Library

import pandas as pd

#pandas have 3 data structures: Series, DataFrame, and Index

# series = is one-dimensional arrat of indexed data 
 
data = pd.Series([0.3, 0.5, 0.75, 1.0, 1.50, 2.50])
print(data)
# The series wraps both sequence of vlues and a sequence of indices, which we can access with the values and index attributes
# the values are simply a familiar NumPy array:
    
#series to NumPy array
print(data.values)
#he index is an array-like object of type pd.Index
print(data.index)
#data can be accessed by the associated index via the familiar python square bracke [] notation:
print(data[2])
print(data[2:5])

#series object as one-dimensional data and index. the index need not be an integer, like Numpy array gas an implicictly difined integer index..
#series can give strings as an index.

data = pd.Series([0.3, 0.5, 0.75, 1.0, 1.50, 2.50], 
                 index=["x1","x2","x3","x4","x5","x6"])
print(data)

#series-as-dictionary analogy can be made even more clear by constructing a series object directly from a python dictionary
my_dict = {"y1":23, "y2":78.45, "y3":89, "y4":19}
my_series = pd.Series(my_dict)
print(my_series)






# DataFrame is a 2-Dimensional labeled data structure with columns of potentially different types
# data structure also contains rows and collumns .
# arethmetic operations align on both row and collumn labels.

#1) create column names
column_names = ["Company", "Revenue", "Currency"]
#2) create dataframe with column names defined in previous step
df1 = pd.DataFrame(columns = column_names)
#3) print empty DataFrame 
print(df1)

#append rows to empty dataframe by adding dictionaries
df1 = df1.append({"Company": "BCG", "Revenue": "8.6 billion", "Currency": "USD"}, ignore_index=True)
df1 = df1.append({"Company:": "Microsoft", "Revenue": "41.7 billion", "Currency": "USD"}, ignore_index=True)
df1 = df1.append({"Company": "Bain & Company", "Revenue": "4.5 Billion", "Currency": "USD"}, ignore_index=True)
df1 = df1.append({"Company": "JPMorgan Chase Bank", "Revenue":"115.6 billion", "Currency":"USD"}, ignore_index=True)
df1 = df1.append({"Company": "Gtech", "Revenue":"91.2 Million", "Currency":"USD"}, ignore_index=True)
df1 = df1.append({"Company":"Monzo Bank", "Revenue": "66 Million", "Currency":"USD"}, ignore_index=True)

print(df1)