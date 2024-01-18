# Write a Pandas program to add some data to an existing Series.

import pandas as pd
import random as rd

list1 =[]
for i in range(0,10) :
    list1.append(rd.randint(1,100))

list1_as_series = pd.Series(list1,name="List1")
print("Before addition :-",list1_as_series)


adding_list = [rd.randint(100,1000) for _ in range(0,10)]

adding_list_as_series = pd.Series(adding_list)

after_adding = pd.concat([list1_as_series,adding_list_as_series])

print("After adding :-",after_adding)