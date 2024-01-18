# Write a Pandas program to convert Series of lists to one Series.

import pandas as pd

matrix = []

count=1
for i in range(1,10) :
    list = []
    for j in range(i,10) :
        list.append(count)
        count+=1
    matrix.append(list)

print(matrix)

matrix_as_series = pd.Series(matrix)

print(matrix_as_series)

# merge series

s = matrix_as_series.apply(pd.Series).stack().reset_index(drop=True)
print("One Series")
print(s)