# Write a Pandas program to sort a given Series.

import pandas as pd
import random as rd

list1 =[]
for i in range(0,10) :
    list1.append(rd.randint(1,100))

list1_as_series = pd.Series(list1,name="List1")
print("Before sorting :-",list1_as_series)

list1_as_series_sorted = list1_as_series.sort_values()

print("After sorting :-",list1_as_series_sorted)