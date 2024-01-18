# Write a Pandas program to convert a given Series to an array.


import pandas as pd
import random as rd

list1 =[]
for i in range(0,10) :
    list1.append(rd.randint(1,100))

list1_as_series = pd.Series(list1,name="List1")
print(list1_as_series)

arr = pd.array(list1_as_series)
print(arr)
print(type(arr))