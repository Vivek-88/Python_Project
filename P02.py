# Write a Pandas program to convert a Panda module Series to Python list and it's type.

import pandas as pd

# List of Odd Number
list = [i for i in range(1,11,2)]

list_as_series = pd.Series(list)

print("Series :- ",list_as_series)
print("Type is :-",type(list_as_series))

# Now convert these series to list

print("Series as list :-",list_as_series.tolist())
print("Type is :-",type(list_as_series.tolist()))