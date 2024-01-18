# Write a Pandas program to convert a NumPy array to a Pandas series.

import pandas as pd
import random as rd
import numpy as np

# list = []

# for i in range(0,10) :
#     list.append(rd.randint(1,100))

list = [rd.randint(1,100) for _ in range(0,10)]

print("List :-",list)

np_array = np.array(list)

print("NP Array",np_array)

np_array_as_series = pd.Series(np_array,name="Np_array_series")

print("Series :-",np_array_as_series)