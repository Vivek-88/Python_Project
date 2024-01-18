# Write a Pandas program to compare the elements of the two Pandas Series.

import pandas as pd
import random as rd

list1 =[]
list2 =[]
for i in range(0,10) :
    list1.append(rd.randint(1,100))
    list2.append(rd.randint(1,100))

list1_as_series = pd.Series(list1,name="List1")
list2_as_series = pd.Series(list2,name="List2")

max_list = pd.Series((max(a,b) for a,b in zip(list1_as_series,list2_as_series)), name="max_list")

min_list = pd.Series((min(a,b) for a,b in zip(list1_as_series,list2_as_series)), name="min_list")


Overall_list = pd.concat([list1_as_series,list2_as_series,max_list,min_list],axis=1)

print(Overall_list)