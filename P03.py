# Write a Pandas program to add, subtract, multiple and divide two Pandas Series.

import pandas as pd


list1 = [i for i in range(1,10)]

list2 = [i for i in range(11,20)]

list1_as_series = pd.Series(list1,name="List1")
# print(list1_as_series)
list2_as_series = pd.Series(list2,name="List2")

added_list = list2_as_series + list1_as_series
added_list.name="List1 + List2"

print("Summation :-",added_list)

dif_list = list2_as_series - list1_as_series
dif_list.name="List2 - List1"

print("Differenc :-",dif_list)

multi_list = list2_as_series * list1_as_series
multi_list.name="List1 * List2"

print("Multiplication :-",multi_list)

div_list = list2_as_series / list1_as_series
div_list.name = "List2 / List1"

print("Division :-",div_list)



Overall_series = pd.concat([list1_as_series,list2_as_series,added_list,dif_list,multi_list,div_list],axis=1)
print(Overall_series)