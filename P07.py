# Write a Pandas program to change the data type of given a column or a Series.

import pandas as pd

list1 = [1,5,8,"vivek","f56",86,80.0,"gh",32]
list2 = ["gj","86",865,97.07,534,87,"u7",86]

list1_as_series = pd.Series(list1,name="List1")
list2_as_series = pd.Series(list2,name="List2")


Overall_list = pd.concat([list1_as_series,list2_as_series],axis=1)

print("Before Changing :-",Overall_list)

Overall_list['List1'] = pd.to_numeric(Overall_list['List1'],errors='coerce')

print("After Changing :-",Overall_list)