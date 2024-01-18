# Write a Pandas program to convert a dictionary to a Pandas series.

import pandas as pd
import random as rd

dict = {}

for i in range(0,10) :
    dict[i]=rd.randint(0,100)

print("Dict :-",dict)

dict_as_series = pd.Series(dict,name="dict_as_series")

print("Dict as series :-",dict_as_series)