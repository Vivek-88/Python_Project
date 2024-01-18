# Write a Pandas program to create and display a one-dimensional array-like object containing an array of data.

import pandas as pd

# List of Even numbers
list = [x for x in range(0,11,2)]

list_as_object = pd.Series(list)

print(list_as_object)